# -----------------------------------------------------------------------------------
#  NukeDiffusion - Stable Diffusion for Nuke
#  Version: v01.0
#  Author: Danilo de Lucio
#  Website: www.danilodelucio.com
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
#  [Summary]
#  NukeDiffusion is an integration tool for Nuke that uses Stable Diffusion
#  to generate AI images from prompts using local Checkpoints.
# -----------------------------------------------------------------------------------


import os
import nuke

from nd_paths import nd_paths
from nd_infos import nd_infos

class sd_node():
    def __init__(self):
        self.class_node = nd_infos().class_node
        self.default_model = nd_infos().default_model

        self.workflow_txt2img = nd_infos().workflow_txt2img
        self.workflow_img2img = nd_infos().workflow_img2img
        self.workflow_inpainting = nd_infos().workflow_inpainting

        self.sd_model_SD = nd_infos().sd_model_SD
        self.sd_model_SDXL = nd_infos().sd_model_SDXL

        self.ckpt_path = nd_paths().checkpointsPath()

    def create(self):
        node = nuke.createNode(self.class_node)
        node["strength"].setVisible(False)
        node["mask_opacity"].setVisible(False)
        node["ckpt"].setValue(self.ckpt_path)

    def writeSettings(self):
        def check_inputs(node, input_num, input_name):
            # Checking if the input Image/Mask is valid or not
            if node.input(input_num) and node.input(input_num).Class() == "Read":
                sd_input = node.input(input_num)
                file_name = nuke.filename(sd_input, nuke.REPLACE)
                extensions_list = [".jpg", ".png", ".tif"]

                if os.path.exists(file_name):
                    for extension in extensions_list:
                        if extension in str(file_name).lower():
                            return file_name
                        
                    else:
                        nuke.message("File extension not supported! Expecting: {}.".format(extensions_list))

                else:
                    nuke.message("The {} input file doesn't exist!".format(input_name))
                    return None
            
            else:
                nuke.message("Please conect a Read node in the input {}!".format(input_name))
                return None

        def setWriteNode(write_id, file_path):
            if write_id == 0:
                write_name = "Write_Image"
            elif write_id == 1:
                write_name = "Write_Mask"

            with nuke.thisNode():
                current_frame = nuke.frame()
                write_node = nuke.toNode(write_name)
                # write_mask["channels"].setValue("rgba")
                write_node["file"].setValue(file_path)
                write_node["create_directories"].setValue(True)

                nuke.execute(write_node, current_frame, current_frame)

        def writeSet_openSD():
            data = {
            "input_image": input_image,
            "input_mask": input_mask,
            "workflow": node["workflow"].value(),
            "checkpoint": node["ckpt"].value(),
            "default_model": node["default_model"].value(),
            "sd_model": node["sd_model"].value(),
            "p_prompt": node["p_prompt"].value(),
            "n_prompt": node["n_prompt"].value(),
            "width": int(node["width"].value()),
            "height": int(node["height"].value()),
            "seed": int(node["seed"].value()),
            "cfg": node["cfg"].value(),
            "steps": int(node["steps"].value()),
            "strength": node["strength"].value(),
            }

            nd_infos().create_settings_file(nd_paths().settingsFile(), data)
            
            # Opening NukeDiffusion Terminal
            python_path = nd_paths().python_files_path()    
            nd_terminal_file = os.path.join(python_path, "nd_terminal.py")
            python_exe_file = nd_paths().python_exe()

            if os.path.exists(nd_terminal_file):
                os.system("start {} -s {}".format(python_exe_file, nd_terminal_file))
                nuke.message("Opening NukeDiffusion Terminal!")

            else:
                nuke.message("It was not possible to open the NukeDiffusion Terminal!")

        node = nuke.thisNode()
        checkpoint = node["ckpt"].value()
        workflow = node["workflow"].value()
        default_model = node["default_model"].value()
        input_image = None
        input_mask = None

        # Checkpoint validation
        if workflow == self.workflow_txt2img or workflow == self.workflow_img2img:
            if default_model == False:
                if not os.path.isfile(checkpoint) or not str(checkpoint).endswith(".safetensors"):
                    return nuke.message("Please select a Checkpoint (.safetensors) file!")
                
        # Checking the Inputs for each workflow before writing the settings
        if workflow == self.workflow_txt2img:
            writeSet_openSD()
            return

        elif workflow == self.workflow_img2img:
            input_image = check_inputs(node, 0, "Image")
            if input_image:
                writeSet_openSD()
                return

        elif workflow == self.workflow_inpainting:
            input_image = check_inputs(node, 0, "Image")
            input_mask = check_inputs(node, 1, "Mask")

            if input_image and input_mask:
                writeSet_openSD()
                return

    def openOutputFolder(self):
        output_path = nd_paths().outputPath()
        if os.path.exists(output_path):
            os.startfile(output_path)
        else:
            nuke.message("Output folder not found!")

    def sdModel_update(self):
        node = nuke.thisNode()
        ckpt_name = node["ckpt"].value()

        if "xl" in ckpt_name or "XL" in ckpt_name:
            node["sd_model"].setValue(self.sd_model_SDXL)
        else:
            node["sd_model"].setValue(self.sd_model_SD)

    def workflow_update(self):
        node = nuke.thisNode()
        workflow = node["workflow"].value()

        if workflow == self.workflow_txt2img:
            node["width"].setVisible(True)
            node["height"].setVisible(True)
            node["strength"].setVisible(False)
            node["mask_opacity"].setVisible(False)
            node["ckpt"].setEnabled(True)
            node["default_model"].setEnabled(True)
            node["default_model"].setValue(False)
        
        if workflow == self.workflow_img2img:
            node["width"].setVisible(False)
            node["height"].setVisible(False)
            node["strength"].setVisible(True)
            node["mask_opacity"].setVisible(False)
            node["ckpt"].setEnabled(True)
            node["default_model"].setEnabled(True)
            node["default_model"].setValue(False)
        
        if workflow == self.workflow_inpainting:
            node["width"].setVisible(True)
            node["height"].setVisible(True)
            node["strength"].setVisible(True)
            node["mask_opacity"].setVisible(True)
            node["ckpt"].setEnabled(False)
            node["default_model"].setValue(True)
            node["default_model"].setEnabled(False)

    def strength_update(self):
        node = nuke.thisNode()
        strength = node["strength"].value()

        if strength < 0:
            node["strength"].setValue(0)
        if strength > 1:
            node["strength"].setValue(1)


print(nd_infos().print_terminal)


# Defining Callbacks
def callback_Workflow():
    kb = nuke.thisKnob().name()
    if kb == "workflow":
        sd_node().workflow_update()

def callback_Generate():
    kb = nuke.thisKnob().name()
    if kb == "generate":
        sd_node().writeSettings()

def callback_Strength():
    kb = nuke.thisKnob().name()
    if kb == "strength":
        sd_node().strength_update()

def callback_openOutputFolder():
    kb = nuke.thisKnob().name()
    if kb == "output_folder":
        sd_node().openOutputFolder()

def callback_sdModel():
    kb = nuke.thisKnob().name()
    if kb == "ckpt":
        sd_node().sdModel_update()


about_tool = """
NukeDiffusion is an integration tool that uses Stable Diffusion to generate AI images from prompts using local Checkpoints.

For more information, please visit the GitHub page.

Developed by: Danilo de Lucio | VFX Compositor & TD.
www.danilodelucio.com | www.github.com/danilodelucio
NukeDiffusion v01.0 (c) 2024
"""


nuke.addKnobChanged(callback_Workflow, nodeClass=sd_node().class_node)
nuke.addKnobChanged(callback_Generate, nodeClass=sd_node().class_node)
nuke.addKnobChanged(callback_Strength, nodeClass=sd_node().class_node)
nuke.addKnobChanged(callback_openOutputFolder, nodeClass=sd_node().class_node)
nuke.addKnobChanged(callback_sdModel, nodeClass=sd_node().class_node)


toolbar_menu = nuke.menu("Nodes")
nd = toolbar_menu.addMenu("NukeDiffusion", icon="NukeDiffusion_tool_icon.png")
nd.addCommand('NukeDiffusion', "sd_node().create()", icon="NukeDiffusion_node_icon.png")
nd.addSeparator()
nd.addCommand("About...", "nuke.message(about_tool)", icon="NukeDiffusion_about_icon.png")