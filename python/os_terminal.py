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
                      "Running on Mac OS...")
    
    def clear(self):
        self.os_check('cls' if os.name=='nt' else 'clear',
                      "clear",
                      "Running on Mac OS...")
        
    def title(self, title_name):
        self.os_check("title {}".format(title_name),
                      "gnome-terminal --title='{}'".format(title_name),
                      "{}".format(title_name))
    
    def start(self):
        nd_terminal_file = str(nd_paths().nd_terminal_file()).replace("\\", "/")
        python_exe_file = str(nd_paths().python_exe()).replace("\\", "/")

        self.os_check("start {} {}".format(python_exe_file, nd_terminal_file),
                    "Linux {} {}".format(python_exe_file, nd_terminal_file),
                    "Mac {} {}".format(python_exe_file, nd_terminal_file))
