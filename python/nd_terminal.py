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
import sys
import time
import random

try:
    from rich.console import Console
    from rich.theme import Theme
    from rich.table import Table
    from rich.progress import track
    from rich.traceback import install
    install()

    from nd_paths import nd_paths
    from nd_infos import nd_infos
    from os_terminal import os_Terminal

    custom_theme = Theme({"success":"green", "alert":"yellow", "error":"red"})
    console = Console(theme=custom_theme)

    import torch

    class NukeDiffusion():
        def __init__(self):
            data = nd_infos().read_settings_file(nd_paths().settingsFile())

            self.input_image = data["input_image"]
            print(self.input_image)
            self.input_mask = data["input_mask"]
            print(self.input_mask)
            self.workflow = data["workflow"]
            self.sd_version = data["sd_model"]
            self.default_model = data["default_model"] 
            self.cuda = data["cuda"]
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
            self.default_model_str = nd_infos().default_model
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
                
                if self.cuda_device() == "cpu":
                    pipeline = StableDiffusionPipeline.from_single_file(self.checkpoint, use_safetensors=True).to(self.cuda_device())
                
                else:
                    pipeline = StableDiffusionPipeline.from_single_file(self.checkpoint, torch_dtype=torch.float16, use_safetensors=True).to(self.cuda_device())
                
            # If not, load the default one
            else:
                from diffusers import AutoPipelineForText2Image

                model_name = "runwayml/stable-diffusion-v1-5"

                if self.cuda_device() == "cpu":
                    pipeline = AutoPipelineForText2Image.from_pretrained(model_name, use_safetensors=True).to(self.cuda_device())
                
                else:
                    pipeline = AutoPipelineForText2Image.from_pretrained(model_name, torch_dtype=torch.float16, use_safetensors=True).to(self.cuda_device())
            
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

                if self.cuda_device() == "cpu":
                    pipeline = StableDiffusionXLPipeline.from_single_file(self.checkpoint, variant="fp16", use_safetensors=True).to(self.cuda_device())

                else:
                    pipeline = StableDiffusionXLPipeline.from_single_file(self.checkpoint, torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to(self.cuda_device())

            # If not, load the default one
            else:
                from diffusers import AutoPipelineForText2Image

                model_name = "stabilityai/stable-diffusion-xl-base-1.0"

                if self.cuda_device() == "cpu":
                    pipeline = AutoPipelineForText2Image.from_pretrained(
                        model_name, variant="fp16", use_safetensors=True).to(self.cuda_device())
                    
                else:
                    pipeline = AutoPipelineForText2Image.from_pretrained(
                        model_name, torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to(self.cuda_device())

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
                
                if self.cuda_device() == "cpu":
                    pipeline = StableDiffusionImg2ImgPipeline.from_single_file(self.checkpoint, use_safetensors=True).to(self.cuda_device())

                else:
                    pipeline = StableDiffusionImg2ImgPipeline.from_single_file(self.checkpoint, torch_dtype=torch.float16, use_safetensors=True).to(self.cuda_device())
            
            # If not, load the default one
            else:
                from diffusers import AutoPipelineForImage2Image

                model_name = "runwayml/stable-diffusion-v1-5"

                if self.cuda_device() == "cpu":
                    pipeline = AutoPipelineForImage2Image.from_pretrained(model_name, variant="fp16", use_safetensors=True).to(self.cuda_device())

                else:
                    pipeline = AutoPipelineForImage2Image.from_pretrained(model_name, torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to(self.cuda_device())

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

                if self.cuda_device() == "cpu":
                    pipeline = StableDiffusionXLImg2ImgPipeline.from_single_file(self.checkpoint, variant="fp16", use_safetensors=True).to(self.cuda_device())
                
                else:
                    pipeline = StableDiffusionXLImg2ImgPipeline.from_single_file(self.checkpoint, torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to(self.cuda_device())
            
            # If not, load the default one
            else:
                from diffusers import AutoPipelineForImage2Image

                model_name = "stabilityai/stable-diffusion-xl-refiner-1.0"

                if self.cuda_device() == "cpu":
                    pipeline = AutoPipelineForImage2Image.from_pretrained(
                        model_name, variant="fp16", use_safetensors=True).to(self.cuda_device())
                
                else:
                    pipeline = AutoPipelineForImage2Image.from_pretrained(
                        model_name, torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to(self.cuda_device())


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

            sd_model_name = "runwayml/stable-diffusion-inpainting"
            sdxl_model_name = "stabilityai/stable-diffusion-xl-base-1.0"

            if self.sd_version == self.sd_model_SD:
                if self.cuda_device() == "cpu":
                    pipeline = AutoPipelineForInpainting.from_pretrained(sd_model_name, variant="fp16").to(self.cuda_device())
                
                else:
                    pipeline = AutoPipelineForInpainting.from_pretrained(sd_model_name, torch_dtype=torch.float16, variant="fp16").to(self.cuda_device())


            elif self.sd_version == self.sd_model_SDXL:
                if self.cuda_device() == "cpu":
                    pipeline = AutoPipelineForInpainting.from_pretrained(sdxl_model_name, use_safetensors=True).to(self.cuda_device())
                
                else:
                    pipeline = AutoPipelineForInpainting.from_pretrained(sdxl_model_name, torch_dtype=torch.float16, use_safetensors=True).to(self.cuda_device())

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
        def cuda_device(self):
            if self.cuda == True:
                if torch.cuda.is_available():
                    return "cuda"
                
                elif torch.backends.mps.is_available():
                    return "mps"
                
                else:
                    console.print("\n:warning:  CUDA is not available, running in CPU...", style="alert")
                    return "cpu"
            else:
                return "cpu"

        def setSeed(self, seed_num):
            seed = -1
            if seed_num == seed:
                seed = torch.Generator()
                seed.seed()
            
            else:
                seed = torch.Generator(device="cpu").manual_seed(seed_num)
                
            return seed

        def ckptPath_check(self, path):
            # Checking if the Checkpoint option exists or not
            if self.default_model == True:
                console.print("\n:warning:  Using the {} checkpoint!\n".format(self.checkpoint_name), style="alert")
                return False
            
            elif os.path.exists(path):
                console.print("\n:warning:  Using a local checkpoint: {}.\n".format(self.checkpoint_name), style="alert")
                return True
    
            else:
                console.print("\n:warning:  Safetensors file doesn't exist or not found. Using a default checkpoint instead!\n", style="error")
                return False

        def printStats(self):
            if self.default_model == True:
                self.checkpoint_name = self.default_model_str
            else:
                self.checkpoint_name = self.checkpoint.split("/")[-1]

            infos_dict = {
                        "Python Version": sys.version[:6],
                        # "Torch version": torch.__version__,
                        "Input Image": self.input_image,
                        "Input Mask": self.input_mask,
                        "Workflow": self.workflow,
                        "Checkpoint": self.checkpoint_name,
                        "SD Model": self.sd_version,
                        "CUDA": self.cuda_device(),
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

            self.file_path = output_path + "/" + final_fileName + ".png"
            console.print("\n[bold]:white_check_mark: The image has been saved at:[/bold]\n" + self.file_path, style="success")

            return self.file_path

        def dl_terminal(self):
            self.terminal_name = 50*" " + "NukeDiffusion Terminal" + 50*" "
            
            os_Terminal().clear()
            os_Terminal().title("NukeDiffusion Terminal")

            console.print(len(self.terminal_name)*"-", style="alert")
            print("")
            console.print(f"[bold]{self.terminal_name}", style="alert")
            print("")
            console.print(len(self.terminal_name)*"-", style="alert")


    ########################################################################################################
    start = time.perf_counter()
    NukeDiffusion()
    end = time.perf_counter()
    
    elapsed_time_seconds = float(end - start)
    elapsed_time_minutes, elapsed_time_seconds = divmod(elapsed_time_seconds, 60)
    console.print(f"\n:clock5: Elapsed time: {int(elapsed_time_minutes):02d}m{int(elapsed_time_seconds):02d}s", style="alert")

    ########################################################################################################
    
except Exception as error:
    console.print("\n- It was not possible to generate your image!", style="error")
    console.print(f"\n- Error: {error}.\n", style="error")
    os_Terminal().pause()


countdown_duration = 60
for remaining in range(countdown_duration, 0, -1):
    sys.stdout.write("\rThis Terminal will be closed in {:2d} seconds.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)