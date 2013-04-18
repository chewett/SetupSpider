#!/usr/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider("apt")
sa.update()

all_packages = []

all_packages.append("screen")
all_packages.append("vim")
all_packages.append("git")
all_packages.append("terminator")
all_packages.append("chromium")
all_packages.append("vlc")
all_packages.append("youtube-dl")
all_packages.append("nmap")
all_packages.append("htop")
all_packages.append("byobu")
all_packages.append("irssi")

#now install all listed packages
sa.install_all(all_packages)
