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
import json

from nd_infos import nd_infos

class nd_paths(): 
    def mainPath(self):
        current_dir = os.path.dirname(__file__)
        main_dir = str(os.path.dirname(current_dir)).replace("\\", "/")
        os.chdir(main_dir)

        return main_dir

    def settingsFile(self):
        settings_file_name = nd_infos().settings_file_name
        settings_file = str(os.path.join(self.mainPath(), "config", settings_file_name)).replace("\\", "/")

        if os.path.exists(settings_file):
            return settings_file
        
        else:
            print("'settings.nukediffusion' not found!")
            return settings_file
    
    def checkpointsPath(self):
        # Defining the default Checkpoints path
        default_ckpt_path = os.path.join(self.mainPath(), "models", "checkpoints").replace("\\", "/")

        if not os.path.exists(default_ckpt_path):
            os.makedirs(default_ckpt_path)

        # Getting the Checkpoint Path from the checkpoints_path.json
        ckpt_json = os.path.join(self.mainPath(), "config", "checkpoints_path.json").replace("\\", "/")

        if os.path.exists(ckpt_json):
            with open("{}".format(ckpt_json), "r") as f:
                data = json.load(f)

            ckpt_path = str(data["checkpoint_path"]).replace("\\", "/")

            if os.path.exists(ckpt_path):
                return ckpt_path + "/"
            else:
                return default_ckpt_path + "/"
        else:
            print("- Error: 'checkpoints.json' file not found!")

    def outputPath(self):
        output_path = os.path.join(self.mainPath(), "_output").replace("\\", "/")
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        return output_path

    def inputPath(self):
        input_path = os.path.join(self.mainPath(), "_input").replace("\\", "/")
            
        if not os.path.exists(input_path):
            os.mkdir(input_path)

        return input_path

    def input_image_path(self):
        input_image_path = self.inputPath() + "/input_image.png"
        return input_image_path

    def input_mask_path(self):
        input_mask_path = self.inputPath() + "/input_mask.png"
        return input_mask_path

    def python_files_path(self):
        python_path = os.path.join(self.mainPath(), "python").replace("\\", "/")

        if os.path.exists(python_path):
            return python_path
        else:
            print("'python' folder not found!")
            return False

    def nd_terminal_file(self):
        nd_terminal_file = str(os.path.join(self.python_files_path(), "nd_terminal.py")).replace("\\", "/")

        if os.path.exists(nd_terminal_file):
            return nd_terminal_file
        else:
            print("'nd_terminal.py' file not found!")
            return False

    def for_windows_path(self):
        for_windows_path = os.path.join(self.mainPath(), "for_windows").replace("\\", "/")
        
        if os.path.exists(for_windows_path):
            return for_windows_path
        else:
            print("'for_windows' folder not found!")
            return

    def for_linux_and_mac_path(self):
        for_linux_and_mac_path = os.path.join(self.mainPath(), "for_linux_and_mac").replace("\\", "/")

        if os.path.exists(for_linux_and_mac_path):
            return for_linux_and_mac_path
        else:
            print("'for_linux' folder not found!")
            return

    def for_mac_path(self):
        for_mac_path = os.path.join(self.mainPath(), "for_mac").replace("\\", "/")

        if os.path.exists(for_mac_path):
            return for_mac_path
        else:
            print("'for_mac' folder not found!")
            return
