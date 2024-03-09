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
import pickle

from nd_infos import nd_infos

class nd_paths(): 
    def mainPath(self):
        current_dir = os.path.dirname(__file__)
        main_dir = os.path.dirname(current_dir)
        os.chdir(main_dir)

        return main_dir

    def settingsFile(self):
        settings_file_name = nd_infos().settings_file_name
        settings_file = os.path.join(self.mainPath(), "config", settings_file_name)
        
        if not os.path.exists(settings_file):
            data = {
                    "input_mask": None, 
                    "input_image": None, 
                    "workflow": "txt2img", 
                    "checkpoint": "", 
                    "default_model": False, 
                    "sd_model": "SD", 
                    "p_prompt": "", 
                    "n_prompt": "",
                    "width": 512, 
                    "height": 512, 
                    "seed": -1, 
                    "cfg": 7, 
                    "steps": 20, 
                    "strength": 0.5
                    }
            with open(settings_file, "wb") as file:
                pickle.dump(data, file, protocol=2)

            print("The '{}' file has been created!".format(settings_file_name))
            return settings_file
        
        else:
            return settings_file
    
    def checkpointsPath(self):
        # Defining the default Checkpoints path
        default_ckpt_path = os.path.join(self.mainPath(), "models", "checkpoints")
        if "\\" in default_ckpt_path:
            default_ckpt_path = default_ckpt_path.replace("\\", "/")

        if not os.path.exists(default_ckpt_path):
            os.makedirs(default_ckpt_path)

        # Getting the Checkpoint Path from the checkpoints_path.json
        ckpt_json = os.path.join(self.mainPath(), "checkpoints_path.json")

        if os.path.exists(ckpt_json):
            with open("{}".format(ckpt_json), "r") as f:
                data = json.load(f)

            ckpt_path = data["checkpoint_path"]
            if "\\" in ckpt_path:
                ckpt_path = str(ckpt_path).replace("\\", "/")

            if os.path.exists(ckpt_path):
                return ckpt_path + "/"
            else:
                return default_ckpt_path + "/"
        else:
            print("- Error: 'checkpoints.json' file not found!")

    def outputPath(self):
        output_path = os.path.join(self.mainPath(), "_output")
        return output_path

    def inputPath(self):
        input_path = os.path.join(self.mainPath(), "_input")
        return input_path

    def python_files_path(self):
        python_path = os.path.join(self.mainPath(), "python")

        if os.path.exists(python_path):
            return python_path
        else:
            print("'python' folder not found!")
            return False

    def python_exe(self):
        python_exe_file = os.path.join(self.python_files_path(), "python3.11.6", "python.exe")

        if os.path.exists(python_exe_file):
            return python_exe_file
        else:
            print("'python3.11.6/python.exe' not found!")
            return False
