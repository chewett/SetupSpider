#!/usr/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider()
sa.update() #update before trying to install new packages

all_packages = []

#core stuff used
all_packages.append("vim")
all_packages.append("emacs")
all_packages.append("screen")
all_packages.append("byobu")
all_packages.append("htop")
all_packages.append("svn")
all_packages.append("p7zip")
all_packages.append("p7zip-plugins")
all_packages.append("git")
all_packages.append("wget")
all_packages.append("unrar")
all_packages.append("aspell-en")
all_packages.append("tar")
all_packages.append("vnstat")
all_packages.append("youtube-dl")
all_packages.append("mysql")
all_packages.append("ipython")
all_packages.append("python-bottle")
all_packages.append("MySQL-python")

#now install all listed packages
sa.install_all(all_packages)
