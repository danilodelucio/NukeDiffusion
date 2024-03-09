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


import sys
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"success":"green", "alert":"yellow", "error":"red"})
console = Console(theme=custom_theme)

try:
    import torch

    print("")
    print(f"- Python Version: {sys.version[:6]}")
    print(f"- Torch version: {torch.__version__}")
    available_cuda = torch.cuda.is_available()
    device_count = torch.cuda.device_count()
    device_name = torch.cuda.get_device_name()

    print("")
    if available_cuda:
        console.print("- CUDA is available!", style="success")
        console.print(f"    - Device name: {device_name}", style="success")
    else:
        console.print("- CUDA is not available!", style="alert")

except Exception as error:
    print("")
    console.print(f"- {error}!", style="error")