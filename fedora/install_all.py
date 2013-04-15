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
all_packages.append("terminator")
all_packages.append("svn")
all_packages.append("p7zip")
all_packages.append("p7zip-plugins")
all_packages.append("git")
all_packages.append("wget")
all_packages.append("unrar")
all_packages.append("baobab") #disk analyser

all_packages.append("geany")
all_packages.append("gimp")
all_packages.append("inkscape")
all_packages.append("calibre")
all_packages.append("pidgin")
all_packages.append("thunderbird")
all_packages.append("xchat")
all_packages.append("gnucash")
all_packages.append("libreoffice")
all_packages.append("youtube-dl")
all_packages.append("VirtualBox")

#gstreamer plugs
all_packages.append("gstreamer-plugins-ugly")
all_packages.append("gstreamer-plugins-bad")
all_packages.append("gstreamer-ffmpeg")
all_packages.append("gstreamer1-plugins-good")
all_packages.append("gstreamer1-plugins-ugly")

#web stuff
all_packages.append("eclipse")
all_packages.append("mysql")
all_packages.append("mysql-workbench")
all_packages.append("filezilla")
all_packages.append("cssed")

all_packages.append("rhythmbox")
all_packages.append("banshee")
all_packages.append("banshee-community-extensions")
all_packages.append("vlc")
all_packages.append("ipython")
all_packages.append("josm")
all_packages.append("python-bottle")

#misc networking things
all_packages.append("wireshark")
all_packages.append("aircrack-ng")
all_packages.append("nmap")
all_packages.append("nmap-frontend")

#now install all listed packages
sa.install_all(all_packages)
