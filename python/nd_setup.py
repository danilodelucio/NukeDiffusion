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


import time
import sys
import os

from os_terminal import os_Terminal
from nd_paths import nd_paths


class ND_Setup():
    def __init__(self):
        self.venv_name = "nukediffusion-env"
        self.install_dependencies = "install --upgrade diffusers transformers accelerate xformers safetensors rich"
        self.system_folder = None

        # Windows
        if os_Terminal().system == os_Terminal().windows_str:
            self.system_folder = nd_paths().for_windows_path()

        # Linux & Mac
        elif os_Terminal().system == os_Terminal().linux_str or os_Terminal().system == os_Terminal().mac_str:
            self.system_folder = nd_paths().for_linux_and_mac_path()


        self.venv_path = str(os.path.join(self.system_folder, self.venv_name)).replace("\\", "/")

    def pip_venv(self, pip_cmd):
        os.chdir(self.system_folder)

        print(f"\n({self.venv_name})")

        # Windows
        if os_Terminal().system == os_Terminal().windows_str:
            pip_windows = f"{self.venv_name}\\Scripts\\python.exe -m {pip_cmd}\n"
            print(pip_windows)
            os.system(pip_windows)

        # Linux & Mac
        elif os_Terminal().system == os_Terminal().linux_str or os_Terminal().system == os_Terminal().mac_str:
            pip_linux_mac = f"{self.venv_name}/bin/python3 -m {pip_cmd}\n"
            print(pip_linux_mac)
            os.system(pip_linux_mac)
        
        return True

    def uninstall_default_torch(self):
        os.chdir(self.venv_path)

        print("\n- Uninstalling default torch dependencies...\n")
        self.pip_venv("pip uninstall torch torchaudio torchvision -y")

        print("\n- All the default torch dependencies have been uninstalled!\n")
        self.pip_venv("pip list")
        return

    def init_install(self):
        init_install = "install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu121 --no-warn-script-location"

        self.pip_venv("pip install rich")
        self.pip_venv(f"pip {init_install}")
        
        print("\n- 'init_install' has been completed!\n")
        self.pip_venv("pip list")
        return

    def install_cuda_11(self):
        install_torch_11 = "install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu118 --no-warn-script-location"
        
        self.uninstall_default_torch()

        print("\n- Installing Stable Diffusion dependencies...")
        self.pip_venv(f"pip {self.install_dependencies}")

        print("\n- Installing torch for CUDA 11...")
        self.pip_venv(f"pip {install_torch_11}")

        self.pip_venv("pip list")
        return

    def install_cuda_12(self):
        install_torch_12 = "install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu121 --no-warn-script-location"

        self.uninstall_default_torch()

        print("\n- Installing Stable Diffusion dependencies...")
        self.pip_venv(f"pip {self.install_dependencies}")

        print("\n- Installing torch for CUDA 12...")
        self.pip_venv(f"pip {install_torch_12}")
        
        self.pip_venv("pip list")
        return

    def install_cpu(self):
        install_torch_cpu = "install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cpu --no-warn-script-location"

        self.uninstall_default_torch()

        print("\n- Installing Stable Diffusion dependencies...")
        self.pip_venv(f"pip {self.install_dependencies}")

        print("\n- Installing torch for CPU...")
        self.pip_venv(f"pip {install_torch_cpu}")

        self.pip_venv("pip list")
        return

    def installing_cuda(self):
        console.print("\nCheck the 'CUDA Version' in the upper right corner of the table above and select one of the following options:", style="alert")
        print("\n[1] - Install CUDA 11;")
        print("[2] - Install CUDA 12;")
        print("[3] - Use CPU;")

        while True:
            choice = input("-> ")

            if choice == "1":
                print("")
                self.install_cuda_11()
                break

            elif choice == "2":
                print("")
                self.install_cuda_12()
                break

            elif choice == "3":
                print("")
                self.install_cpu()
                break

            else:
                console.print("- Please choose one of the options above!\n", style="error")
                continue

try:
    ND_Setup().init_install()

    from rich.console import Console
    from rich.theme import Theme
    from rich.traceback import install
    install()
    custom_theme = Theme({"success":"green", "alert":"yellow", "error":"red"})
    console = Console(theme=custom_theme)

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
        ND_Setup().installing_cuda()

    else:
        console.print("- CUDA is not available!", style="error")
        console.print("Using torch for CPU...", style="alert")
        ND_Setup().install_cpu()

    console.print("\n[bold]:white_check_mark: The NukeDiffusion setup has been completed!", style="success")
    input("\nYou can close this window...")

except Exception as error:
    print(f"\n- Error: {error}.\n")
    os_Terminal().pause()