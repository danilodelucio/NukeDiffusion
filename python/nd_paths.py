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
import json

class nd_paths():
    def mainPath(self):
        current_dir = os.path.dirname(__file__)
        main_dir = os.path.dirname(current_dir)
        os.chdir(main_dir)

        return main_dir

    def settingsFile(self):
        settings_file = os.path.join(self.mainPath(), "config", "settings.json")
        
        if os.path.exists(settings_file):
            return settings_file
        else:
            print("settings.json file not found!")
            False
    
    def checkpointsPath(self):
        # Defining the default Checkpoints path
        default_ckpt_path = os.path.join(self.mainPath(), "models", "checkpoints")
        
        if not os.path.exists(default_ckpt_path):
            os.makedirs(default_ckpt_path)

        # Getting the Checkpoint Path from the checkpoints_path.json
        ckpt_json = os.path.join(self.mainPath(), "checkpoints_path.json")

        if os.path.exists(ckpt_json):
            with open("{}".format(ckpt_json), "r") as f:
                data = json.load(f)

            ckpt_path = data["checkpoint_path"]
            if os.path.exists(ckpt_path):
                return ckpt_path
        else:
            return default_ckpt_path

    def safetensorsList(self):
        # Creating a list with all Safetensors files available in the Checkpoints path
        safetensors_list = []

        for file in os.listdir(self.checkpointsPath()):
            if file.endswith(".safetensors"):
                safetensors_list.append(file)

        return safetensors_list

    def outputPath(self):
        output_path = os.path.join(self.mainPath(), "_output")
        return output_path

    def inputPath(self):
        input_path = os.path.join(self.mainPath(), "_input")
        return input_path

    def python_files_path(self):
        python_path = os.path.join(self.mainPath(), "python")
        return python_path