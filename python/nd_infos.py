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


import datetime
import pickle
import base64

class nd_infos():
    def __init__(self):
        self.class_node = "NukeDiffusion"
        self.nukediffusion_version = "v01.0"
        self.default_model = "Stable Diffusion [Default Model]"
        self.settings_file_name = "settings.nukediffusion"
        self.print_terminal = "NukeDiffusion {}, built in Feb 2024.\nCopyright (c) 2024 Danilo de Lucio. All Rights Reserved.".format(self.nukediffusion_version)

        workflow_list = ["txt2img", "img2img", "inpainting"]
        self.workflow_txt2img = workflow_list[0]
        self.workflow_img2img = workflow_list[1]
        self.workflow_inpainting = workflow_list[2]

        sd_model = ["SD", "SDXL"]
        self.sd_model_SD = sd_model[0]
        self.sd_model_SDXL = sd_model[1]

    def random_file_name(self):
        date_time = datetime.datetime.now()
        file_name = str(date_time)[:-7]
        file_name_split = file_name.split(":")
        final_fileName = ("").join(file_name_split).replace(" ", "_")

        return final_fileName
    
    def create_settings_file(self, file_path, data):        
        # Pickling and Encoding data
        pickle_data = pickle.dumps(data, protocol=2)
        encode_data = base64.b64encode(pickle_data)

        with open(file_path, "wb") as file:
            file.write(encode_data)
        
        print("- The '{}' file has been created!".format(self.settings_file_name))
        return

    def read_settings_file(self, file_path):
        with open(file_path, "rb") as file:
            settings_file_data = file.read()

        # Unpickling and Decoding data
        decode_data = base64.b64decode(settings_file_data)
        unpickling_data = pickle.loads(decode_data)

        return unpickling_data
