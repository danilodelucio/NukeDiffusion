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
import platform

from nd_paths import nd_paths


class os_Terminal():
    def __init__(self):
        self.system = platform.system()
        self.windows_str = "Windows"
        self.linux_str = "Linux"
        self.mac_str = "Darwin"
    
    def os_check(self, windows_cmd, linux_cmd, mac_cmd):
        if self.system == self.windows_str:
            return os.system(windows_cmd)

        elif self.system == self.linux_str:
            return os.system(linux_cmd)

        elif self.system == self.mac_str:
            return os.system(mac_cmd)
        
    def pause(self):
        self.os_check("pause",
                      "read 'Press Enter to continue...'",
                      "echo Running on Mac OS...")
    
    def clear(self):
        self.os_check('cls' if os.name=='nt' else 'clear',
                      "clear",
                      "clear")
        
    def title(self, title_name):
        self.os_check("title {}".format(title_name),
                      "echo Opening {}...".format(title_name),
                      "echo Opening {}...".format(title_name))
    
    def start(self):
        main_path = nd_paths().mainPath()
        nd_terminal_file = str(nd_paths().nd_terminal_file()).replace("\\", "/")

        # Windows
        python_exe_file = os.path.join(nd_paths().mainPath(), "for_windows/nukediffusion-env/Scripts/python.exe").replace("\\", "/")
        # Linux
        nk_linux_env = os.path.join(main_path, "for_linux/nukediffusion-env/bin/activate")
        # Mac
        nk_mac_env = os.path.join(main_path, "for_mac/nukediffusion-env/bin/activate")

        self.os_check("start {} {}".format(python_exe_file, nd_terminal_file),
                    "gnome-terminal -- /bin/bash -c 'source {};python3 {}; exec /bin/bash -i'".format(nk_linux_env, nd_terminal_file),
                    "Mac echo {} {}".format(nk_mac_env, nd_terminal_file))
