#!/usr/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider()
sa.update() #update before trying to install new packages

all_packages = []

#core stuff used
all_packages.append("bash-completion")
all_packages.append("vim")
all_packages.append("screen")
all_packages.append("byobu")
all_packages.append("htop")
all_packages.append("terminator")
all_packages.append("svn")
all_packages.append("p7zip")
all_packages.append("p7zip-plugins")
all_packages.append("git")
all_packages.append("wget")
all_packages.append("aspell-en")
all_packages.append("tar")

all_packages.append("geany")
all_packages.append("gedit")
all_packages.append("gimp")
all_packages.append("inkscape")
all_packages.append("calibre")
all_packages.append("thunderbird")
all_packages.append("gnucash")
all_packages.append("libreoffice")
all_packages.append("youtube-dl")
all_packages.append("ffmpeg")
all_packages.append("avconv")
all_packages.append("gparted")

#web stuff
all_packages.append("eclipse")
all_packages.append("mysql")
all_packages.append("filezilla")
all_packages.append("cssed")
all_packages.append("firefox")

all_packages.append("rhythmbox")
all_packages.append("banshee")
all_packages.append("banshee-community-extensions")
all_packages.append("ipython")
all_packages.append("josm")
all_packages.append("python-bottle")
all_packages.append("MySQL-python")
all_packages.append("myrepos")

#misc networking things
all_packages.append("wireshark")
all_packages.append("aircrack-ng")
all_packages.append("nmap")
all_packages.append("nmap-frontend")

#now install all listed packages
sa.install_all(all_packages)
