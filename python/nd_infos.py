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

class nd_infos():
    def __init__(self):
        self.class_node = "NukeDiffusion"
        self.default_model = "Stable Diffusion [Default Model]"
        self.settings_file_name = "settings.nukediffusion"

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
