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


import time
import json
import os
import sys

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.traceback import install
install()

from nd_paths import nd_paths
from nd_infos import nd_infos

try:
    import torch

    custom_theme = Theme({"success":"green", "alert":"yellow", "error":"red"})
    console = Console(theme=custom_theme)


    class NukeDiffusion():
        def __init__(self):
            with open(nd_paths().settingsFile(), "r") as f:
                data = json.load(f)

            self.input_image = data["input_image"]
            self.input_mask = data["input_mask"]
            self.workflow = data["workflow"]
            self.sd_version = data["sd_model"]
            self.checkpoint = data["checkpoint"]
            self.positive_prompt = data["p_prompt"]
            self.negative_prompt = data["n_prompt"]
            self.width = data["width"]
            self.height = data["height"]
            self.seed = data["seed"]
            self.cfg = data["cfg"]
            self.steps = data["steps"]
            self.strength = data["strength"]

            self.class_node = nd_infos().class_node
            self.default_model = nd_infos().default_model
            self.workflow_txt2img = nd_infos().workflow_txt2img
            self.workflow_img2img = nd_infos().workflow_img2img
            self.workflow_inpainting = nd_infos().workflow_inpainting
            self.sd_model_SD = nd_infos().sd_model_SD
            self.sd_model_SDXL = nd_infos().sd_model_SDXL

            self.sd_model_error = ":cross_mark: SD Model not found!"

            self.dl_terminal()
            self.printStats()

            # txt2img
            if self.workflow == self.workflow_txt2img:
                if self.sd_version == self.sd_model_SD:
                    self.sd_txt2img()
                elif self.sd_version == self.sd_model_SDXL:
                    self.sdxl_txt2img()
                else:
                    console.print(self.sd_model_error, style="error")
                

            # img2img
            elif self.workflow == self.workflow_img2img:
                if self.sd_version == self.sd_model_SD:
                    self.sd_img2img()
                elif self.sd_version == self.sd_model_SDXL:
                    self.sdxl_img2img()
                else:
                    console.print(self.sd_model_error, style="error")

            # inpainting
            elif self.workflow == self.workflow_inpainting:
                self.sd_sdxl_inpainting()

            else:
                console.print(":cross_mark: Workflow option not found!", style="error")
                return
        
        # Creating/Saving the final image
        def createImage(self, pipeline, **kwargs):
            image = pipeline(**kwargs).images[0]

            image.save(self.exportFile())
            return 
        
        # SD Workflows/Pipelines
        def sd_txt2img(self):
            # If local Checkpoint exists, load it
            if self.ckptPath_check(self.checkpoint):
                from diffusers import StableDiffusionPipeline
                
                pipeline = StableDiffusionPipeline.from_single_file(self.checkpoint, torch_dtype=torch.float16, use_safetensors=True).to("cuda")
                
            # If not, load the default one
            else:
                from diffusers import AutoPipelineForText2Image

                pipeline = AutoPipelineForText2Image.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16, use_safetensors=True).to("cuda")
            
            self.createImage(pipeline, 
                            prompt= self.positive_prompt, 
                            negative_prompt= self.negative_prompt, 
                            width= self.width, 
                            height= self.height, 
                            generator= self.setSeed(self.seed), 
                            guidance_scale= self.cfg,
                            num_inference_steps= self.steps
                            )

        def sdxl_txt2img(self):
            # If local Checkpoint exists, load it
            if self.ckptPath_check(self.checkpoint):
                from diffusers import StableDiffusionXLPipeline

                pipeline = StableDiffusionXLPipeline.from_single_file(self.checkpoint, torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to("cuda")

            # If not, load the default one
            else:
                from diffusers import AutoPipelineForText2Image

                pipeline = AutoPipelineForText2Image.from_pretrained(
                    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to("cuda")

            self.createImage(pipeline, 
                            prompt= self.positive_prompt, 
                            negative_prompt= self.negative_prompt, 
                            width= self.width, 
                            height= self.height, 
                            generator= self.setSeed(self.seed), 
                            guidance_scale= self.cfg,
                            num_inference_steps= self.steps
                            )

        def sd_img2img(self):
            from diffusers.utils import load_image

            # If local Checkpoint exists, load it
            if self.ckptPath_check(self.checkpoint):
                from diffusers import StableDiffusionImg2ImgPipeline
                
                pipeline = StableDiffusionImg2ImgPipeline.from_single_file(self.checkpoint, torch_dtype=torch.float16, use_safetensors=True).to("cuda")
            
            # If not, load the default one
            else:
                from diffusers import AutoPipelineForImage2Image

                pipeline = AutoPipelineForImage2Image.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to("cuda")

            pipeline.enable_model_cpu_offload()
            # remove following line if xFormers is not installed or you have PyTorch 2.0 or higher installed
            pipeline.enable_xformers_memory_efficient_attention()

            init_image = load_image(self.input_image).convert("RGB")
            
            self.createImage(pipeline,
                            prompt= self.positive_prompt, 
                            negative_prompt= self.negative_prompt, 
                            image= init_image,
                            generator= self.setSeed(self.seed),
                            num_inference_steps= self.steps,
                            guidance_scale= self.cfg,
                            strength= self.strength
                            )

        def sdxl_img2img(self):
            from diffusers.utils import load_image

            # If local Checkpoint exists, load it
            if self.ckptPath_check(self.checkpoint):
                from diffusers import StableDiffusionXLImg2ImgPipeline

                pipeline = StableDiffusionXLImg2ImgPipeline.from_single_file(self.checkpoint, torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to("cuda")
            
            # If not, load the default one
            else:
                from diffusers import AutoPipelineForImage2Image

                pipeline = AutoPipelineForImage2Image.from_pretrained(
                    "stabilityai/stable-diffusion-xl-refiner-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to("cuda")

            init_image = load_image(self.input_image).convert("RGB")
        
            self.createImage(pipeline,
                            prompt= self.positive_prompt, 
                            negative_prompt= self.negative_prompt, 
                            image= init_image,
                            generator= self.setSeed(self.seed),
                            num_inference_steps= self.steps,
                            guidance_scale= self.cfg,
                            strength= self.strength
                            )

        def sd_sdxl_inpainting(self):
            from diffusers import AutoPipelineForInpainting
            from diffusers.utils import load_image

            if self.sd_version == self.sd_model_SD:
                pipeline = AutoPipelineForInpainting.from_pretrained("runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16, variant="fp16").to("cuda")

            elif self.sd_version == self.sd_model_SDXL:
                pipeline = AutoPipelineForInpainting.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True).to("cuda")

            else:
                console.print(self.sd_model_error, style="error")
                return

            
            init_image = load_image(self.input_image).convert("RGB")
            mask_image = load_image(self.input_mask).convert("RGB")

            self.createImage(pipeline,
                            prompt= self.positive_prompt, 
                            negative_prompt= self.negative_prompt, 
                            image= init_image,
                            mask_image=mask_image,
                            width=self.width,
                            height=self.height,
                            generator= self.setSeed(self.seed),
                            num_inference_steps= self.steps,
                            guidance_scale= self.cfg,
                            strength= self.strength
                            )

        # Additional Methods
        def setSeed(self, seed_num):
            seed = -1
            if seed_num == seed:
                seed = torch.Generator()
                seed.seed()
            else:
                seed = torch.Generator(device="cuda").manual_seed(seed_num)
                
            return seed

        def ckptPath_check(self, path):
            # Checking if the Checkpoint option exists or not
            if os.path.exists(path):
                console.print("\n:warning:  Using a local checkpoint: {}\n".format(self.checkpoint_name), style="alert")
                return True
            
            elif self.default_model in path:
                console.print("\n:warning:  Using a default checkpoint: {}\n".format(self.checkpoint_name), style="alert")
                return False
            
            else:
                console.print("\n:warning:  Safetensors file not found. Using a default checkpoint instead!\n", style="error")
                return False

        def printStats(self):
            self.checkpoint_name = self.checkpoint.split("\\")[-1]

            infos_dict = {
                        "Python Version": sys.version[:6],
                        "Torch version": torch.__version__,
                        "Input Image": self.input_image,
                        "Input Mask": self.input_mask,
                        "Workflow": self.workflow,
                        "Checkpoint": self.checkpoint_name,
                        "SD Model": self.sd_version,
                        "Positive Prompt": self.positive_prompt,
                        "Negative Prompt": self.negative_prompt,
                        "Resolution": f"{self.width}x{self.height}",
                        "Seed": self.seed,
                        "CFG": self.cfg,
                        "Steps": self.steps,
                        "Strength": self.strength
                        }
            
            if self.workflow == self.workflow_txt2img:
                infos_dict.pop("Input Image")
                infos_dict.pop("Input Mask")
                infos_dict.pop("Strength")
            
            elif self.workflow == self.workflow_img2img:
                infos_dict.pop("Input Mask")
                infos_dict.pop("Resolution")

            elif self.workflow_inpainting == self.workflow_inpainting:
                infos_dict.pop("Checkpoint")

            # Generating a Table with the information
            table = Table(show_header=False, 
                        width=len(self.terminal_name),
                        style="dim",
                        show_lines=True)
            
            for key, value in infos_dict.items():
                table.add_row(f"- {key}:", f"{value}")

            console.print(table)

        def exportFile(self):
            final_fileName = nd_infos().random_file_name()
            output_path = nd_paths().outputPath()
            input_path = nd_paths().inputPath()

            if not os.path.exists(output_path):
                os.mkdir(output_path)
                console.print("\n:warning: The OUTPUT folder doesn't exist but has been created!", style="alert")

            elif not os.path.exists(input_path):
                os.mkdir(input_path)
                console.print("\n:warning: The INPUT folder doesn't exist but has been created!", style="alert")

            self.file_path = output_path + "\\" + final_fileName + ".png"
            console.print("\n[bold]:white_check_mark: The image has been saved at:[/bold]\n" + self.file_path, style="success")

            return self.file_path

        def dl_terminal(self):
            self.terminal_name = 30*" " + "NukeDiffusion Terminal" + 30*" "
            
            os.system('cls' if os.name=='nt' else 'clear')
            os.system(f"title {self.terminal_name}")

            console.print(len(self.terminal_name)*"-", style="alert")
            print("")
            console.print(f"[bold]{self.terminal_name}", style="alert")
            print("")
            console.print(len(self.terminal_name)*"-", style="alert")



    ########################################################################################################
    start = time.perf_counter()
    try:
        NukeDiffusion()
    except:
        os.system("pause")
    end = time.perf_counter()

    elapsed_time_seconds = float(end - start)
    elapsed_time_minutes, elapsed_time_seconds = divmod(elapsed_time_seconds, 60)
    console.print(f"\n:clock5: Elapsed time: {int(elapsed_time_minutes):02d}m{int(elapsed_time_seconds):02d}s", style="alert")

    time.sleep(15)
    ########################################################################################################
    
except Exception as error:
    console.print("It was not possible to generate your image!", style="error")
    console.print(f"\n- Error: {error}.\n", style="error")
    os.system("pause")