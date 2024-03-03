<h1>NukeDiffusion - Stable Diffusion for Nuke</h1> 

<br>**NukeDiffusion** is an integration tool for Nuke that uses Stable Diffusion to generate AI images from prompts using local Checkpoints.
<br>It utilizes the official library from Hugging Face, and you don't need to create any account, everything works locally!

![NukeDiffusion_Cover_v002](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/d230497e-f1d7-4687-9299-7f7487e5718f)


<br>:white_check_mark: Unlimited image generation;
<br>:white_check_mark: Local Checkpoints;
<br>:white_check_mark: No internet connection required;
<br>:white_check_mark: No sign in account required;

---

For now, the pipeline workflows included are:

- **txt2img**: generates an image from a text description (which is also known as a Prompt);
- **img2img**: generates an image passing an initial image as a starting point for the diffusion process;
- **Inpainting**: replaces or edits specific areas of an image by a provided input mask;

---

<details>
<summary><b>txt2img</b></summary>
 
</details>


---


<h1>NukeDiffusion node</h1>

The NukeDiffusion node is pretty straightforward, everything you need is in the same panel, and its UI updates accordingly to your workflow option (txt2img / img2img / inpainting).

![NukeDiffusion_NodeUI_v001](https://github.com/danilodelucio/NukeDiffusion/assets/47226196/07bed17b-b564-49d8-8567-26741bd721f5)


<h1>Installing</h1>
