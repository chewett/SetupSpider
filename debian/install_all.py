#!/usr/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider("apt")
sa.update() #update before trying to install new packages

all_packages = []

#core stuff used
all_packages.append("unrar-free")
all_packages.append("sudo")
all_packages.append("vim")
all_packages.append("emacs")
all_packages.append("screen")
all_packages.append("byobu")
all_packages.append("htop")
all_packages.append("terminator")
all_packages.append("subversion")
all_packages.append("git-core")
all_packages.append("wget")
all_packages.append("p7zip-full")
all_packages.append("unrar-free")
all_packages.append("baobab") #disk analyser

all_packages.append("chromium")
all_packages.append("geany")
all_packages.append("gimp")
all_packages.append("inkscape")
all_packages.append("calibre")
#all_packages.append("thunderbird")
all_packages.append("xchat")
all_packages.append("gnucash")
all_packages.append("libreoffice")
#all_packages.append("youtube-dl")
#all_packages.append("VirtualBox")



#web stuff
all_packages.append("eclipse")
#all_packages.append("mysql")
all_packages.append("mysql-workbench")
all_packages.append("filezilla")
all_packages.append("cssed")

all_packages.append("vlc")
all_packages.append("ipython")

#now install all listed packages
sa.install_all(all_packages)
