<h1>NukeDiffusion - Stable Diffusion for Nuke</h1> 

![NukeDiffusion_Cover_v002](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/d230497e-f1d7-4687-9299-7f7487e5718f)

<br>**NukeDiffusion** is an integration tool for Nuke that uses [Stable Diffusion](https://stability.ai/) to generate AI images from prompts using local Checkpoints.
<br>It uses the official library from [Hugging Face](https://huggingface.co), and you don't need to create any account, everything works locally!

:white_check_mark: Unlimited image generation;
<br>✅ Local Checkpoints;
<br>✅ No internet connection required;
<br>✅ No sign-in account required;
<br>✅ Free for non-commercial or commercial use.
<br>
<br>

> [!TIP]
> _You can use the [CivitAI](https://civitai.com/) website to download Checkpoints and try some different Prompts shared by the community._ 😉
<br>


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
But don't give up, I'm sure you can do this! 🤓
<br>
<br>
Let me break it into a few parts:


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


