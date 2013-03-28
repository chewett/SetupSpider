#!/bin/python
import sys
sys.path.append("../")
from SetupAutomator import *

sa = SetupAutomator("apt")
sa.update()

all_packages = []

all_packages.append("screen")
all_packages.append("vim")
all_packages.append("git")
all_packages.append("terminator")
all_packages.append("chromium")
all_packages.append("vlc")
all_packages.append("youtube-dl")



#now install all listed packages
sa.install_all(all_packages)
