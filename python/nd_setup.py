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


import sys
import os

from os_terminal import os_Terminal
from nd_paths import nd_paths
os_Terminal().init_install()


from rich.console import Console
from rich.theme import Theme
from rich.traceback import install
install()
custom_theme = Theme({"success":"green", "alert":"yellow", "error":"red"})
console = Console(theme=custom_theme)


windows_folder = nd_paths().for_windows_path()
linux_folder = nd_paths().for_linux_path()
mac_folder = nd_paths().for_mac_path()


def install_cuda_11():
    # Windows
    if os_Terminal().system == os_Terminal().windows_str:
        os.chdir(windows_folder)
        os.system("{}".format(windows_folder + "/uninstall_dependencies.bat"))
        os.system("{}".format(windows_folder + "/2_CUDA11_install_pytorch.bat"))
        os.system("{}".format(windows_folder + "/4_install_or_update_dependencies.bat"))
    
    # Linux
    elif os_Terminal().system == os_Terminal().linux_str:
        os.chdir(linux_folder)
        os.system("source {}".format(linux_folder + "/activate_nukediffusion-env.sh"))
        os.system("pip freeze | xargs pip uninstall -y")
        os.system("pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu118 --no-warn-script-location")
        os.system("pip install --upgrade diffusers transformers accelerate xformers safetensors rich --no-warn-script-location")
    
    # Mac
    elif os_Terminal().system == os_Terminal().mac_str:
        os.chdir(mac_folder)
        os.system("source {}".format(mac_folder + "/activate_nukediffusion-env.sh"))
        os.system("pip3 freeze | xargs pip uninstall -y")
        os.system("pip3 install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu118 --no-warn-script-location")
        os.system("pip3 install --upgrade diffusers transformers accelerate xformers safetensors rich --no-warn-script-location")

    return


def install_cuda_12():
    # Windows
    if os_Terminal().system == os_Terminal().windows_str:
        os.chdir(windows_folder)
        os.system("{}".format(windows_folder + "/4_install_or_update_dependencies.bat"))
    
    # Linux
    elif os_Terminal().system == os_Terminal().linux_str:
        os.chdir(linux_folder)
        os.system("source {}".format(linux_folder + "/activate_nukediffusion-env.sh"))
        os.system("pip install --upgrade diffusers transformers accelerate xformers safetensors rich --no-warn-script-location")

    # Mac
    elif os_Terminal().system == os_Terminal().mac_str:
        os.chdir(mac_folder)
        os.system("source {}".format(mac_folder + "/activate_nukediffusion-env.sh"))
        os.system("pip3 install --upgrade diffusers transformers accelerate xformers safetensors rich --no-warn-script-location")
    
    return


def install_cpu():
    # Windows
    if os_Terminal().system == os_Terminal().windows_str:
        os.chdir(windows_folder)
        os.system("{}".format(windows_folder + "/uninstall_dependencies.bat"))
        os.system("{}".format(windows_folder + "/2_CPU_install_pytorch.bat"))
        os.system("{}".format(windows_folder + "/4_install_or_update_dependencies.bat"))
    
    # Linux
    elif os_Terminal().system == os_Terminal().linux_str:
        os.chdir(linux_folder)
        os.system("source {}".format(linux_folder + "/activate_nukediffusion-env.sh"))
        os.system("pip freeze | xargs pip uninstall -y")
        os.system("pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cpu --no-warn-script-location")
        os.system("pip install --upgrade diffusers transformers accelerate xformers safetensors rich --no-warn-script-location")

    # Mac
    elif os_Terminal().system == os_Terminal().mac_str:
        os.chdir(mac_folder)
        os.system("source {}".format(mac_folder + "/activate_nukediffusion-env.sh"))
        os.system("pip3 freeze | xargs pip uninstall -y")
        os.system("pip3 install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cpu --no-warn-script-location")
        os.system("pip3 install --upgrade diffusers transformers accelerate xformers safetensors rich --no-warn-script-location")

    return


def install_cuda():
    console.print("\nCheck the 'CUDA Version' in the upper right corner of the table above and select one of the following options:", style="alert")
    print("\n[1] - Install CUDA 11;")
    print("[2] - Install CUDA 12;")
    print("[3] - Use CPU;")

    while True:
        choice = input("-> ")

        if choice == "1":
            install_cuda_11()
            break

        elif choice == "2":
            install_cuda_12()
            break

        elif choice == "3":
            install_cpu()
            break

        else:
            console.print("- Please choose one of the options above!\n", style="error")


import torch

print(f"\n- Python Version: {sys.version[:6]}")
print(f"- Torch version: {torch.__version__}\n")
available_cuda = torch.cuda.is_available()
device_count = torch.cuda.device_count()
device_name = torch.cuda.get_device_name()

if available_cuda or torch.backends.mps.is_available():
    os_Terminal().os_check("nvidia-smi",
                        "nvidia-smi",
                        " ")
    
    console.print("\n- CUDA is available!", style="success")
    console.print(f"    - Device name: {device_name}", style="success")
    install_cuda()

else:
    console.print("- CUDA is not available!", style="error")
    console.print("Using torch for CPU...", style="alert")
    install_cpu()

console.print("\n[bold]:white_check_mark: The NukeDiffusion setup has been completed!", style="success")
input("\nYou can close this window...")