<h1>NukeDiffusion - Stable Diffusion for Nuke</h1> 

<br>**NukeDiffusion** is an integration tool for Nuke that uses Stable Diffusion to generate AI images from prompts using local Checkpoints.
<br>It utilizes the official library from Hugging Face, and you don't need to create any account, everything works locally!

![NukeDiffusion_Cover_v002](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/d230497e-f1d7-4687-9299-7f7487e5718f)


<br>:white_check_mark: Unlimited image generation;
<br>:white_check_mark: Local Checkpoints;
<br>:white_check_mark: No internet connection required;
<br>:white_check_mark: No sign in account required;


> [!TIP]
> _You can use the [CivitAI](https://civitai.com/) website to download Checkpoints and try some different Prompts shared by the community._ :wink:


Some limitations:
- Windows only;
- 

---

For now, the pipeline workflows included are:

- **txt2img**: generates an image from a text description (which is also known as a Prompt);
- **img2img**: generates an image passing an initial image as a starting point for the diffusion process;
- **Inpainting**: replaces or edits specific areas of an image by a provided input mask;

---

<details>
<summary><b>txt2img</b></summary>
 
</details>


<h1>'triton' Error :rotating_light:</h1>

> [!IMPORTANT]
> The error `ModuleNotFoundError: No module named 'triton'` must be ignored!

Triton is a Open-source GPU programming for neural networks, and what I found regarding to this issue, is that Triton module is not available for Windows.
However, this error does not affect the image generation, just simply ignore it!
 
 ![triton error](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/06a3a408-681a-451a-8e1c-ce354e0a4e2d)

> _I didn't hide this issue because you can check on the Terminal if you get another import module error._

---


<h1>NukeDiffusion node :radioactive:</h1>

The **NukeDiffusion** node is pretty straightforward, everything you need is in the same panel, and its UI updates accordingly to your workflow option (txt2img / img2img / inpainting).

![NukeDiffusion_NodeUI_v001](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/07bed17b-b564-49d8-8567-26741bd721f5)


<h1>Installing</h1>

<h1>Troubleshooting :hammer_and_wrench:</h1>

For suggestions, questions or bugs report, please go to the [Issues](https://github.com/danilodelucio/NukeDiffusion/issues) page and create a new issue.



<h1>Support me! :pleading_face:</h1>

![image](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/ee1e5d16-43e2-46bc-bc48-aaf1d7559b87)

This personal project required a significant time and extra hours of hard work to make it available to everyone. 

If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://www.buymeacoffee.com/danilodelucio). :coffee:

Even sharing this tool or sending me a positive message would help me in the same way.


<h1>Cheers! :clinking_glasses:</h1>


