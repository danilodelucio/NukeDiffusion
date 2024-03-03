<h1>NukeDiffusion - Stable Diffusion for Nuke</h1> 

<br>**NukeDiffusion** is an integration tool for Nuke that uses [Stable Diffusion](https://stability.ai/) to generate AI images from prompts using local Checkpoints.
<br>It utilizes the official library from [Hugging Face](https://huggingface.co), and you don't need to create any account, everything works locally!

![NukeDiffusion_Cover_v002](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/d230497e-f1d7-4687-9299-7f7487e5718f)
<br>:white_check_mark: Unlimited image generation;
<br>:white_check_mark: Local Checkpoints;
<br>:white_check_mark: No internet connection required;
<br>:white_check_mark: No sign in account required;
<br>:white_check_mark: Free for non-commercial or commercial use;

> [!TIP]
> _You can use the [CivitAI](https://civitai.com/) website to download Checkpoints and try some different Prompts shared by the community._ :wink:

---
For now, the pipeline workflows included are:

- **txt2img**: generates an image from a text description (which is also known as a Prompt);
- **img2img**: generates an image passing an initial image as a starting point for the diffusion process;
- **Inpainting**: replaces or edits specific areas of an image by a provided input mask;

> [!NOTE]
> _For experienced users, **NukeDifussion** does not support ControlNet, Lora and other advanced controls, just the basic setup for image generation._

---

<h1>NukeDiffusion node :radioactive:</h1>

The **NukeDiffusion** node is pretty straightforward, everything you need is in the same panel, and its UI updates accordingly to your workflow option (txt2img/img2img/inpainting).

![NukeDiffusion_NodeUI_v002](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/aa668518-cf08-4596-9539-9b1ceeb0f393)

---
<h1>NukeDiffusion Terminal :robot:</h1>

After clicking on the **Generate Button**, it will open the **NukeDiffusion Terminal**, which will load all the information provided in **NukeDiffusion node**.


![Screenshot 2024-03-03 215656](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/66c97762-9306-4d56-af24-d898053b97ef)

Here you don't have too much to do, just check the information and... wait! :sweat_smile:

---

<details>
<summary><b>txt2img</b></summary>
 
</details>

<details>
<summary><b>img2img</b></summary>
 
</details>

<details>
<summary><b>inpainting</b></summary>
 
</details>

<details>
<summary><b>'triton' Error</b></summary>

The error `ModuleNotFoundError: No module named 'triton'` must be ignored!

Triton is a Open-source GPU programming for neural networks, and what I found regarding to this issue, is that Triton module is not available for Windows.
However, this error does not affect the image generation, just simply ignore it!
 
 ![triton error](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/06a3a408-681a-451a-8e1c-ce354e0a4e2d)

> _I didn't hide this issue because you can check on the Terminal if you get another import module error._
</details>

---

<h1>Installing</h1>
Here is the most annoying part... :persevere:
But don't give up, I'm sure that you can do this! :nerd_face:

Let me break it into a few parts:



<h1>Troubleshooting :hammer_and_wrench:</h1>

For any feedback, suggestions, bugs, or feature requests, please go to the [Issues](https://github.com/danilodelucio/NukeDiffusion/issues) page and create a new issue.



<h1>Support me! :pleading_face:</h1>

![image](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/ee1e5d16-43e2-46bc-bc48-aaf1d7559b87)

This personal project required a significant time and extra hours of hard work to make it available to everyone. 

If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://www.buymeacoffee.com/danilodelucio). :coffee:

Even sharing this tool or sending me a positive message would help me in the same way.

If you believe in this project and want to sponsor it for future updates, reach out on my [Linkedin](https://www.linkedin.com/in/danilodelucio/).


<h1>Cheers! :clinking_glasses:</h1>


