# -----------------------------------------------------------------------------------
#  NukeDiffusion - Stable Diffusion for Nuke
#  Version: v01.1
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
import time
import platform
import threading

from nd_paths import nd_paths
from nd_infos import nd_infos
from os_terminal import os_Terminal

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
        node["input_format"].setVisible(True)
        node["ckpt"].setValue(self.ckpt_path)

        with nuke.toNode(node.name()):
            write_image = nuke.toNode("Write_Image")
            write_image["file"].setValue(nd_paths().input_image_path())

            write_mask = nuke.toNode("Write_Mask")
            write_mask["file"].setValue(nd_paths().input_mask_path())

    def writeSettings(self):
        def check_inputs(node, input_num):
            if input_num == 0: # Input Image
                input_path = nd_paths().input_image_path()
                input_str = "Image"

            elif input_num == 1: # Input Mask
                input_path = nd_paths().input_mask_path()
                input_str = "Mask"

            if node.input(input_num):
                if os.path.exists(input_path):
                    return True
        
                else:
                    nuke.message("Please export the Input {} first!".format(input_str))
                    return False
            else:
                nuke.message("Please connect the Input {}!".format(input_str))
                return False
            
        def writeSet_openSD():
            data = {
            "input_image": nd_paths().input_image_path(),
            "input_mask": nd_paths().input_mask_path(),
            "workflow": node["workflow"].value(),
            "checkpoint": node["ckpt"].value(),
            "default_model": node["default_model"].value(),
            "cuda": node["cuda"].value(),
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
        
            if nd_paths().nd_terminal_file():
                os_Terminal().start()

                nuke.message("Opening NukeDiffusion Terminal!")

            else:
                nuke.message("It was not possible to open the NukeDiffusion Terminal!")

        node = nuke.thisNode()
        checkpoint = node["ckpt"].value()
        workflow = node["workflow"].value()
        default_model = node["default_model"].value()

        # Checkpoint validation
        if workflow == self.workflow_txt2img or workflow == self.workflow_img2img:
            if default_model == False:
                if not os.path.isfile(checkpoint) or not str(checkpoint).endswith(".safetensors"):
                    return nuke.message("Please select a Checkpoint (.safetensors) file!")
            
        # Checking/Exporting the Inputs for each workflow before writing the settings
        if workflow == self.workflow_txt2img:
            writeSet_openSD()
            return
        
        elif workflow == self.workflow_img2img:
            if check_inputs(node, 0):
                writeSet_openSD()
                return

        elif workflow == self.workflow_inpainting:
            if check_inputs(node, 0) and check_inputs(node, 1):
                writeSet_openSD()
                return

    def render_write_nodes(self, node, write_id):
        def execute_render(write_node, current_frame):
            nuke.execute(write_node, current_frame, current_frame)
            return

        current_frame = nuke.frame()

        if write_id == 0:
            write_str = "Image"

        elif write_id == 1:
            write_str = "Mask"
            
        with node:
            write_node = nuke.toNode("Write_{}".format(write_str))
        
        if node.input(write_id):
            thread = threading.Thread(target=execute_render, args=(write_node, current_frame))
            thread.start()
            thread.join()
            return
        else:
            nuke.message("Please connect the Input {}!".format(write_str))
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
            node["input_format"].setVisible(True)
            node["strength"].setVisible(False)
            node["mask_opacity"].setVisible(False)
            node["ckpt"].setEnabled(True)
            node["default_model"].setEnabled(True)
            node["default_model"].setValue(False)
        
        if workflow == self.workflow_img2img:
            node["width"].setVisible(False)
            node["height"].setVisible(False)
            node["input_format"].setVisible(False)
            node["strength"].setVisible(True)
            node["mask_opacity"].setVisible(False)
            node["ckpt"].setEnabled(True)
            node["default_model"].setEnabled(True)
            node["default_model"].setValue(False)
        
        if workflow == self.workflow_inpainting:
            node["width"].setVisible(True)
            node["height"].setVisible(True)
            node["input_format"].setVisible(True)
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
NukeDiffusion {} (c) 2024
""".format(nd_infos().nukediffusion_version)

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