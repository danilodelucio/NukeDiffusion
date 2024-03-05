<h1>NukeDiffusion - Stable Diffusion for Nuke</h1> 

![NukeDiffusion_Cover_v002](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/d230497e-f1d7-4687-9299-7f7487e5718f)

<br>**NukeDiffusion** is an integration tool for Nuke that uses [Stable Diffusion](https://stability.ai/) to generate AI images from prompts using local Checkpoints.
<br>It uses the official library from [Hugging Face](https://huggingface.co), and you don't need to create any account, everything works locally!

:white_check_mark: Unlimited image generation;
<br>✅ Local Checkpoints (SD and SDXL models);
<br>✅ Main workflows included (**txt2img**, **img2img**, **inpainting**);
<br>✅ No internet connection required;
<br>✅ No sign-in account required;
<br>✅ Free for non-commercial or commercial use.
<br>
<br>

> [!TIP]
> _You can use the [CivitAI](https://civitai.com/) website to download Checkpoints and try some different Prompts shared by the community._ 😉
<br>


<h1>Stable Diffusion Requirements 🖥️</h1>

For a complete guide to **Stable Diffusion** requirements, I suggest you read [this article](https://www.andyhtu.com/post/system-requirements-your-complete-guide-to-running-stable-diffusion-efficiently).

In summary, the lower budget setup mentioned in the article is:
- GPU: GTX 1060 (6GB VRAM)
- System RAM: 16GB DDR4
<br>

<h1>Python Compatibility 🐍</h1>

The **NukeDiffusion node** was written in Python 2.7 so that it would be possible to run in all Nuke versions.<br>
For **NukeDiffusion Terminal**, it was written in Python 3.
<br>
<br>

---
Some limitations you need to consider for this first version:

📌 only for Windows (sorry 🐧 and 🍎);
<br>📌 generate single images only (not animation supported);
<br>📌 image files supported: **.jpg**, **.png**, **.tif** (does not support **.exr** and video files);
<br>📌 batch feature for multiple image generation not included.

> [!NOTE]
> _For experienced users, **NukeDifussion** does not support ControlNet, Lora, AnimateDiff and other advanced controls, just the basic setup for image generation._
---
<h1>Workflows :briefcase:</h1>

For now, the included pipeline workflows are:

- **txt2img**: generates an image from a text description (which is also known as a Prompt);
- **img2img**: generates an image passing an initial image (user input) as a starting point for the diffusion process;
- **Inpainting**: replaces or edits specific areas of an image by a provided input mask.
<br>

> [!IMPORTANT]
> _To use the **img2img** and **inpainting** workflows, you must input Read nodes directly to the input image/input mask;_<br>
> _This tool does not export the connected inputs automatically (at least for now), so you should pre-render your inputs in case they have extra nodes below (Roto, Reformat etc)._<br>

---

<h1>NukeDiffusion node ☢️</h1>

The **NukeDiffusion** node is pretty straightforward. Everything you need is in the same panel, and the UI updates accordingly to your workflow option (**txt2img**, **img2img**, **inpainting**).

![NukeDiffusion_NodeUI_v002](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/aa668518-cf08-4596-9539-9b1ceeb0f393)

- `Workflow`: select one of the 3 workflow options to work with: **txt2img**, **img2img** or **inpainting**;

- `Checkpoint`: clicking on the **Refresh** button, will load all the **Checkpoints** available in the directory you specified earlier on `checkpoints_path.json`, or if you are using the default path `./NukeDiffusion/models/checkpoints`;

- `SD Model`: after selecting the **Checkpoint** model, you must indicate its version. By default, if the "XL" or "xl" letters are included in the checkpoint name, it will update the **SD Model** knob to "SDXL", otherwise to "SD";

> [!WARNING]
> Keep in mind to match the **SD Model** to your selected **Checkpoint**.<br>
> **SD** and **SDXL** models were pretrained with different resolutions, and they have different pipelines to produce your image.<br>
> If you provide a **Checkpoint** with the wrong **SD Model**, the **NukeDiffusion Terminal** will close automatically.

- `Positive Prompt`: type everything __you want__ to be generated in your image;

- `Negative Prompt`: type everything __you do not want__ to be generated in your image;

- `Width`: width size for your output image;

- `Height`: height size for your output image;

- `Seed`: If you leave the value as `-1`, your image will be generated randomly. However, if you set any other value, your image will always be the same. It's a good idea to lock the **Seed** and try different settings to see how they affect your image;

- `CFG`: is the Classifier-Free Guidance scale, which controls how closely the image generation process follows the text prompt.
  The higher the value, the more the image will follow the text input (by default, the maximum value is 10, but you can increase it if you want). With a lower value, the image generation deviates from the text input and becomes more creative;
            <details>
            <summary>cfg examples</summary>
            ![nukediffusion_CFG](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/3ae4e5dc-e019-4356-a530-e8f6c95fa6b6)
            </details>

- `Steps`: it's the iterations of sampling and refining for the latent image. With higher steps you can get better images (usually between 20 and 40). Higher than this probably will slow down the image generation and will not have too much difference;
            <details>
            <summary>steps examples</summary>
            ![nukediffusion_Steps](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/775bbcb0-eef7-4c28-9f9e-02cc502fc374)
            </details>
            
- `Strength`: this parameter sets the denoising strength from 0 to 1. It is only used for **img2img** and **inpainting** workflows and requires an initial image. Higher values will produce more deviation from the input image (producing more creative output), and lower values will preserve the input image;
            <details>
            <summary>strength examples</summary>
            ![nukediffusion_Strength](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/34785f19-bc23-4cce-9007-c1bd01eb0920)
            </details>
            
- `Mask Opacity`: this is just for visualization purposes to check the mask input over the image input.

---
<h1>NukeDiffusion Terminal 🤖</h1>

After clicking on the **Generate Image** button, it will open the **NukeDiffusion Terminal**, which will load all the information provided in the **NukeDiffusion node**.


![Screenshot 2024-03-03 215656](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/d8d23db9-7ea7-4d16-a51c-12e75c06cef3)


Here you don't have too much to do, just check the information and... wait! 😅

---
<h2>Some images generated with NukeDiffusion using different workflows 🖼️</h2>

<details>
<summary><b>txt2img</b></summary>
  
![nukediffusion_A](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/215c78fc-68c4-49d3-839a-44b9361131ef)
![nukediffusion_B](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/24b62a96-eea8-4d95-a457-eabb831c76d4)
![nukediffusion_C](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/3d52e3a3-2c78-45ba-ba61-d56c088fb113)
</details>


<details>
<summary><b>img2img</b></summary>
  
![nukediffusion_img2img_A](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/1506ae42-bad6-4c8d-ad4d-99621482e3dd)
</details>


<details>
<summary><b>inpainting</b></summary>
 
</details>

---
<h1>Time waiting ⌛</h1>

This is a subject I need to highlight with you. Since we are generating AI images locally, the time waiting depends exclusively on your machine's performance.

Keep in mind that when you ALWAYS run the code for the first time, it will take a while to load the selected Checkpoint into memory. Then, loading the next AI images will take less time.

The image generation itself is faster than the loading checkpoint process. For all my tests, for example, sometimes I had to wait between 10 and 20 minutes to load the Checkpoint, but it took me 20 seconds to 2-3 minutes to generate the rest of the images (this mentioned time is per single image, of course).

> [!TIP]
> _To generate faster images, try SD models instead of SDXL._

So please, while the cursor blinks on the **NukeDiffusion Terminal**, don't close it! Just ignore the `'triton' module error` message and wait!

---
<h1>Installing ⚙️</h1>
Here is the most annoying part... 😣 <br>
But don't give up, I'm sure you can d[Uploading init.py…]()
o this! 🤓
<br>
<br>
Let me break it into a few parts:
<br>
<br>

<details>
  <summary>1. .nuke</summary>

  Click on the green button to download the **NukeDiffusion** and save it to your `.nuke` folder.

  Open your `init.py` (from the `.nuke` root), and indicate the **NukeDiffusion** folder, like:
  ```python
import nuke

nuke.pluginAddPath('./NukeDiffusion')
  ```

  If you don't have an `init.py` file in your `.nuke` directory, you can create a new text file and paste the code above.
  > _Don't forget to change the file extension to `.py`._

</details>

<details>
  <summary>2. Python</summary>
<br>
  
Since Nuke comes with a built-in Python installation, you need to ensure that your system has **Python3.8+** installed.

To check the Python version on your machine, open the Terminal and type:
```python
python --version
```
![python version](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/97839071-30cb-47b1-bf16-fd219ad27192)

If you don't have it, please visit the [Python](https://www.python.org/) website, download and install it.<br>

> _Please, don't forget to check the "**Add Python to PATH**" option_.

![python add to path](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/6cb32696-1921-4486-9ff9-f14bed42a15c)

</details>

<details>
<summary>3. PyTorch</summary>
  <br>

PyTorch is an open-source framework for building and training neural networks (deep learning). It's highly flexible and dynamic, making it ideal for generating AI images.

> _To learn more about it, please visit [this page](https://www.nvidia.com/en-us/glossary/pytorch/) from the NVidia website._


You need to install **PyTorch 1.7.0+**, but first of all, you need to know the CUDA version of your graphic card.

Open your Terminal and type:
```python
nvidia-smi
```
After displaying some information, you'll see the CUDA version in the upper right corner.

![cuda version](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/1d92f570-4961-4222-ad1d-a4ab9cbe1dc9)


Now, [go to this PyTorch page](https://pytorch.org/get-started/locally/) and select the options that apply to your system.

![pytorch install](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/02dd81cf-fc56-4e6d-b52e-313c60fb9015)

Paste and run the command provided into your Terminal to install PyTorch.

</details>

<details>
  <summary>4. CUDA</summary>
<br>
  
Even after checking the **CUDA** version and installing **PyTorch**, your **CUDA** may be disabled (that was my case). 😒<br>
To check if it is enabled, open the `run_check_cuda.bat` file that I've provided at `./NukeDiffusion/cuda/run_check_cuda.bat`.

If you get `True` as a response you are good to go, otherwise, [go to this page](https://developer.nvidia.com/cuda-gpus) from NVidia and download/install the **CUDA Toolkit**.

After installing it, run the `run_check_cuda.bat` file again and hopefully you are done! 🤞
</details>

<details>
  <summary>5. Python Dependencies</summary>
<br>
  Finally, if you followed all the steps above and everything worked fine, now it's the last part. 🙌

  Open the file `install_dependencies.bat`, it will open the Terminal and install all the necessary Python dependencies for **Stable Diffusion**.

  And that's it, now you are ready to use **NukeDiffusion**! :star_struck:
  
</details>

---
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

<details>
<summary><b>blank error message</b></summary>
 
 ![Screenshot 2024-03-03 200140](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/cde41084-317a-47c5-9024-baba5ab5d5c7)

In **NukeDiffusion** node, when you click on **Refresh** button, it will load all the **Checkpoints** available in the directory you specified earlier on `checkpoints_path.json`, or if you are using the default path `./NukeDiffusion/models/checkpoints`.
If you open a Nuke script and see the `blank error message`, that is because the **Checkpoints pulldown choice menu** is trying to get the last checkpoint loaded in the previous session, which will raise an error.

For now, I suggest you choose one of the 3 following options:

- delete the **NukeDiffusion** node before closing the Nuke script;
- leave the **Checkpoints pulldown choice menu** set to `Stable Diffusion [Default Model]`;
- simply ignore the error message, this will not affect your script at all.

> _Sorry for the inconvenience, I will fix it in the next release!_ 🙏

</details>
<br>

If you have feedback, suggestions, or feature requests, please visit the [Discussions](https://github.com/danilodelucio/NukeDiffusion/discussions) page and create a **New Discussion**.<br>
For bugs, please go to the [Issues](https://github.com/danilodelucio/NukeDiffusion/issues) page and create a **New Issue**.

---
<h1>Support me! 🥺</h1>

![image](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/ee1e5d16-43e2-46bc-bc48-aaf1d7559b87)

This personal project required significant time and extra hours of hard work to make it available to everyone. <br>
It's not perfect, and I still need to work on many features, but for the first version, I believe it can help Nuke users live this experience. 🤖

If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://www.buymeacoffee.com/danilodelucio). :coffee: <br>
You can also share this tool or send me a positive message, it would help me in the same way.

If you believe in this project and want to sponsor it for future updates, reach out on my [Linkedin](https://www.linkedin.com/in/danilodelucio/).


<h1>Cheers! 🥂</h1>


