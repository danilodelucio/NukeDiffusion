<h1>NukeDiffusion - Stable Diffusion for Nuke</h1> 

![NukeDiffusion_Logo_v001](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/1eac3b38-17e5-4341-81f3-a63471f04356)

<br>**NukeDiffusion** is an integration tool for Nuke that uses [Stable Diffusion](https://stability.ai/) to generate AI images from prompts using local Checkpoints.<br>
It uses the official library from [Hugging Face](https://huggingface.co), and you don't need to create any account, everything works locally!

:white_check_mark: Unlimited image generation;
<br>✅ Local Checkpoints (SD and SDXL models);
<br>✅ Main workflows included (**txt2img**, **img2img**, **inpainting**);
<br>✅ No internet connection required;
<br>✅ No sign-in account required;
<br>✅ Free for non-commercial or commercial use.
<br>
<br>
Some limitations you need to consider for this first version:

📌 only for Windows (sorry 🐧 and 🍎);
<br>📌 generate single images only (no animation supported);
<br>📌 image files supported: **.jpg**, **.png**, **.tif** (does not support **.exr** and video files);
<br>📌 batch feature for multiple image generation not included;
<br>📌 compatible only with CUDA.

> [!NOTE]
> _For experienced users, **NukeDifussion** does not support **ControlNet**, **Lora**, **AnimateDiff** and other advanced controls, just the basic setup for image generation._
<br>

---
<!-- ############################################################# LINKS ############################################################# -->
<h1>Quick Access 🔗</h1>

- [Stable Diffusion Requirements](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#stable-diffusion-requirements-%EF%B8%8F);
- [Python Compatibility](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#python-compatibility-);
- [Workflows](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#workflows-);
- [NukeDiffusion node](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#nukediffusion-node-%EF%B8%8F);
- [NukeDiffusion Terminal](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#nukediffusion-terminal-);
- [Some images generated with NukeDiffusion using different workflows](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#some-images-generated-with-nukediffusion-using-different-workflows-%EF%B8%8F);
- [Waiting time](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#waiting-time-);
- [Installing](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#installing-%EF%B8%8F);
- [Checkpoints](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#checkpoints-);
- [Troubleshooting](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#troubleshooting-%EF%B8%8F);
- [Support me](https://github.com/danilodelucio/NukeDiffusion?tab=readme-ov-file#support-me-);


![NukeDiffusion_cover_FHD_v002](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/133fc83c-c61b-49a4-a05a-c81c5008d591)

---
<!-- ############################################################# DIFFUSION REQUIREMENTS ############################################################# -->
<h1>Stable Diffusion Requirements 🖥️</h1>

For a complete guide to **Stable Diffusion** requirements, I suggest you read [this article](https://www.andyhtu.com/post/system-requirements-your-complete-guide-to-running-stable-diffusion-efficiently).

In summary, the most basic setup mentioned in the article is:
- **GPU**: GTX 1060 (6GB VRAM);
- **System RAM**: 16GB DDR4.

> [!IMPORTANT]
> _Please note that due to the size of the **SDXL models**, which is around 6GB, certain Checkpoints may not be compatible with this setup._
<br>

<!-- ############################################################# PYTHON COMPATIBILITY ############################################################# -->
<h1>Python Compatibility 🐍</h1>

- **NukeDiffusion** comes with a built-in Python installation (version **3.11.6**),
which is used to run **NukeDiffusion Terminal**;

- **NukeDiffusion node** was written in **Python2.7** to make it possible to run in all Nuke versions (hopefully). 😐

<br>

<!-- ############################################################# WORKFLOWS ############################################################# -->
<h1>Workflows 💼</h1>

For now, the included pipeline workflows are:

- **txt2img**: generates an image from a text description (which is also known as a Prompt);
- **img2img**: generates an image passing an initial image (user input) as a starting point for the diffusion process;
- **Inpainting**: replaces or edits specific areas of an image by a provided input mask.
<br>

> [!IMPORTANT]
> _To use the **img2img** and **inpainting** workflows, you must input Read nodes directly to the input image/input mask;_<br>
>
> _This tool does not export the connected inputs automatically (at least for now), so you should pre-render your inputs in case they have extra nodes  (Roto, Reformat etc)._<br>
<br>

<!-- ############################################################# NUKEDIFFUSION NODE ############################################################# -->
<h1>NukeDiffusion node ☢️</h1>

The **NukeDiffusion** node is pretty straightforward. Everything you need is in the same panel, and the UI updates accordingly to your workflow option (**txt2img**, **img2img**, **inpainting**).

![NukeDiffusion_NodeUI_v003](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/545cfbdd-34d3-4c58-9f9f-32e55239d5d9)

- `Workflow`: select one of the 3 workflow options to work with: **txt2img**, **img2img** or **inpainting**;

- `Checkpoint`: by clicking on the **Refresh** button, it will load all the **Checkpoints** available in the directory you specified earlier on `checkpoints_path.json`, or if you are using the default path `./NukeDiffusion/models/checkpoints`;

- `SD Model`: after selecting the **Checkpoint** model, you must indicate its version. By default, if the "XL" or "xl" letters are included in the checkpoint name, it will update the **SD Model** knob to "SDXL", otherwise to "SD";

> [!WARNING]
> _Keep in mind to match the **SD Model** to your selected **Checkpoint**._<br>
> _**SD** and **SDXL** models were pretrained with different resolutions, and they have different pipelines to produce your image._<br>
> _If you provide a **Checkpoint** with the wrong **SD Model**, the **NukeDiffusion Terminal** will close automatically._

- `Positive Prompt`: type everything __you want__ to be generated in your image;

- `Negative Prompt`: type everything __you do not want__ to be generated in your image;

- `Width`: width size of your output image;

- `Height`: height size of your output image;

- `Seed`: If you leave the value as `-1`, your image will be generated randomly. However, if you set any other value, your image will always be the same. It's a good idea to lock the **Seed** and try different settings to see how they affect your image;

- `CFG`: is the Classifier-Free Guidance scale, which controls how closely the image generation process follows the text prompt.
  The higher the value, the more the image will follow the text input (by default, the maximum value is 10, but you can increase it if you want). With a lower value, the image generation deviates from the text input and becomes more creative;
            <details>
            <summary>cfg examples</summary>
            ![nukediffusion_CFG](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/3e3d87ca-7ef0-4a6d-a1e5-7c154caedf0a)
            </details>

- `Steps`: it's the iterations of sampling and refining for the latent image. With higher steps you can get better images (usually between 20 and 40). Higher than this will probably slow down the image generation and will not have too much difference;
            <details>
            <summary>steps examples</summary>
            ![nukediffusion_Steps](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/c062f9b3-3dd3-431f-99ba-daa6016beba0)
            </details>
            
- `Strength`: this parameter sets the denoising strength from 0 to 1. It is only used for **img2img** and **inpainting** workflows and requires an initial image. Higher values will produce more deviation from the input image (producing more creative output), and lower values will preserve the input image;
            <details>
            <summary>strength examples</summary>
            ![nukediffusion_Strength](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/d4ee1e07-4de1-46b5-a9b2-89c807cb822e)
            </details>
            
- `Mask Opacity`: this is just for visualization purposes to check the mask input over the image input.
<br>

<!-- ############################################################# NUKEDIFUSSION TERMINAL ############################################################# -->
<h1>NukeDiffusion Terminal 🤖</h1>

After clicking on the **Generate Image** button, it will open the **NukeDiffusion Terminal**, which will load all the information provided in the **NukeDiffusion node**.


![Screenshot 2024-03-03 215656](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/d8d23db9-7ea7-4d16-a51c-12e75c06cef3)


Here you don't have too much to do, just check the information and... wait! 😅

> [!IMPORTANT]
> _While the cursor blinks on the **NukeDiffusion Terminal**, don't close it! Just ignore the `'triton' module error` message and wait for your image to be generated!_
<br>

<!-- ############################################################# SOME IMAGES GENERATED ############################################################# -->
<h2>Some images generated with NukeDiffusion using different workflows 🖼️</h2>

<details>
<summary><b>txt2img</b></summary>
  
![nukediffusion_txt2img_A](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/5c0ebef6-54fa-469c-aa5e-5b543a0ff058)
![nukediffusion_txt2img_B](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/2a50dd37-6412-471f-8b33-b8e4a54ae7ac)
![nukediffusion_txt2img_C](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/ce2f4bce-c6cd-49a4-a77c-d253424756e6)

</details>


<details>
<summary><b>img2img</b></summary>
  
  ![nukediffusion_img2img_A](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/251e5e4e-3541-41aa-ad4b-b9eff8f1b36c)

</details>


<details>
<summary><b>inpainting</b></summary>
 
</details>
<br>

<!-- ############################################################# WAITING TIME ############################################################# -->
<h1>Waiting time ⌛</h1>

This is a subject I need to highlight with you. 🥸

Since we are generating AI images locally, the waiting time depends exclusively on your machine's performance.

Keep in mind that when you run the code for the first time, it will ALWAYS take a while to load the selected Checkpoint into memory. After that, loading the next AI images will take less time.

The image generation itself is faster than the loading checkpoint process. For example, in all my tests I had to wait around 10 and 20 minutes to load the Checkpoint, but it took me 20 seconds to 2-3 minutes to generate the rest of the images (the referred time is per single image, of course).

> [!TIP]
> _To generate faster images, try **SD** models instead of **SDXL**._
<br>

<!-- ############################################################# INSTALLING ############################################################# -->
<h1>Installing ⚙️</h1>
Here is the most annoying part... 😣 <br>
But don't give up, it will be worth it! 🤓
<br>
<br>

There are a few `.bat` files in the **NukeDiffusion** folder to help you install all the necessary dependencies.<br>

> [!NOTE]
> _All these dependencies will be automatically installed into the `.\NukeDiffusion\python\python3.11.6` directory._

<br>
Let me break it into a few parts:
<br>
<br>
<details>
  <summary>1. .nuke</summary>
<br>
  
  Click on the green button to download the **NukeDiffusion** and save it to your `.nuke` folder.

  Open the `init.py` file from the `.nuke` root, and indicate the **NukeDiffusion** folder, like:
  ```python
import nuke

nuke.pluginAddPath('./NukeDiffusion')
  ```

  If you don't have an `init.py` file in your `.nuke` directory, you can create a new text file and paste the code above.
  > _Don't forget to rename it as `init` and change the file extension to `.py`._
<br>
</details>

<details>
<summary>2. PyTorch / CUDA</summary>
  <br>

PyTorch is an open-source framework for building and training neural networks (deep learning). It's highly flexible and dynamic, making it ideal for generating AI images.

> _To learn more about it, please visit [this page](https://www.nvidia.com/en-us/glossary/pytorch/) from the NVidia website._
<br>

In the `.\NukeDiffusion\cuda` folder, let's run some `.bat` files.<br>
<br>

1- Run the `check_cuda_version.bat` file to display the CUDA version of your graphic card (around the upper right corner).<br>


![cuda version](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/1d92f570-4961-4222-ad1d-a4ab9cbe1dc9)

<br>
2- If your CUDA version is 12, run the `install_pytorch_cuda12.bat` file, otherwise, if it's version 11, run the `install_pytorch_cuda11.bat` (this process can take a while).<br>
<br>

![image](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/b28a66a2-592b-4fec-bb88-4338d75a40da)

<br>
3- Run the `check_cuda_enabled.bat` file to display if your CUDA is enabled and also check if the `torch` module is working.<br>
<br>

![image](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/07265213-ea27-4b10-8bb2-11d54bc7b223)

If you get `CUDA is available!` as a response you are good to go, otherwise, [go to this page](https://developer.nvidia.com/cuda-gpus) from NVidia, download and install the **CUDA Toolkit**, then try again this step until you get enabled CUDA. 🤞


</details>

<details>
  <summary>5. Python Dependencies</summary>
<br>
  
  Finally, if you followed all the steps above and everything worked fine, now it's the last part. 🙌
  <br>

  Open the file `install_or_update_dependencies.bat`, it will open the Terminal and install all the necessary Python dependencies for **Stable Diffusion**.<br>
  
  ![image](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/571a6487-9243-4117-8545-5261f61ac387)


  And that's it, now you are ready to use **NukeDiffusion**! :star_struck:
  
</details>

At the end of this guide, you should see the **NukeDiffusion**'s icon on your left side toolbar when you launch Nuke.<br>

![Screenshot 2024-03-03 145810](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/9e735145-17e2-44a6-98bb-afdb471a15cd)
<br>
<br>

<!-- ############################################################# CHECKPOINTS ############################################################# -->
<h1>Checkpoints ✅</h1>

You can use the [CivitAI](https://civitai.com/) website to download Checkpoints and try some different Prompts shared by the community. 😉

> [!IMPORTANT]
> _For now, **NukeDiffusion** only accepts `.safetensors` files._

If you are unsure about which Checkpoint to use, I'm going to list some of my favourites:

<details>
  <summary>SD models</summary>
  
- [Dreamshaper](https://civitai.com/models/4384?modelVersionId=128713);
- [CarDos Anime](https://civitai.com/models/25399/cardos-anime);
- [Ghostmix](https://civitai.com/models/36520/ghostmix);
- [PicX_real](https://civitai.com/models/241415/picxreal);
  
</details>
<details>
  <summary>SDXL models</summary>

- [Dreamshaper XL](https://civitai.com/models/112902/dreamshaper-xl?modelVersionId=126688);
- [Juggernaut XL](https://civitai.com/models/133005/juggernaut-xl?modelVersionId=288982);
- [PhotoVision XL](https://civitai.com/models/125703/protovision-xl-high-fidelity-3d-photorealism-anime-hyperrealism-no-refiner-needed);
- [Animagine XL](https://civitai.com/models/260267/animagine-xl-v3?modelVersionId=293564);
</details>
<br>

After downloading the Checkpoint, you can put them in `.\NukeDiffusion\models\checkpoints`.<br>
If you have another folder in which you want to use the Checkpoints, you can set a default path in the `checkpoints_path.json` file.

![image](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/a885b9d9-d7ff-4611-a061-9acea7aa599a)

> [!CAUTION]
> _Using a single backslash `\` can cause issues. Please use either a forward slash `/` or double backslash `\\`._

> [!IMPORTANT]
> _If you don't provide a custom Checkpoint and leave the Checkpoint dropdown menu as `Stable Diffusion [Default Model]`, it will download a default model from the [Hugging Face](https://huggingface.co/) repository._

<br>

<!-- ############################################################# TROUBLESHOOTING ############################################################# -->
<h1>Troubleshooting 🛠️</h1>

<details>
<summary><b>'triton' Error</b></summary>
<br>
  
The error `ModuleNotFoundError: No module named 'triton'` must be ignored!

Triton is an Open-source GPU programming for neural networks, and what I found regarding this issue, is that Triton module is not available for Windows.
However, this error does not affect the image generation, so just simply ignore it!
 
 ![triton error](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/06a3a408-681a-451a-8e1c-ce354e0a4e2d)

> _I didn't hide this issue so you can check on the Terminal if you get another import module error._
</details>

<br>

If you have feedback, suggestions, or feature requests, please visit the [Discussions](https://github.com/danilodelucio/NukeDiffusion/discussions) page and create a **New Discussion**.<br>
For bugs, please go to the [Issues](https://github.com/danilodelucio/NukeDiffusion/issues) page and create a **New Issue**.
<br>
<br>

<!-- ############################################################# SUPPORT ME ############################################################# -->
<h1>Support me! 🥺</h1>

![image](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/ee1e5d16-43e2-46bc-bc48-aaf1d7559b87)

This personal project required significant time and extra hours of hard work to make it available to everyone. <br>
It's not perfect, and I still need to work on many features, but for the first version, I believe it can help Nuke users live this experience. 🤖

If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://www.buymeacoffee.com/danilodelucio). :coffee: <br>
You can also share this tool or send me a positive message, it would help me in the same way.

If you believe in this project and want to sponsor it for future updates, reach out on my [Linkedin](https://www.linkedin.com/in/danilodelucio/).

---
Special thanks to Gustavo Goncalves and Leticia Matsuoka for testing this tool and providing valuable feedback for improvement. Also, thanks to Juliana Chen for her support and encouragement.

<h1>Cheers! 🥂</h1>


