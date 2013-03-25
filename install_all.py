#!/bin/python
from SetupAutomator import *

sa = SetupAutomator()

all_packages = []

#core stuff used
all_packages.append("vim")
all_packages.append("emacs")
all_packages.append("screen")
all_packages.append("htop")
all_packages.append("terminator")
all_packages.append("svn")
all_packages.append("p7zip")
all_packages.append("p7zip-plugins")
all_packages.append("git")
all_packages.append("wget")
all_packages.append("unrar")


all_packages.append("geany")
all_packages.append("gimp")
all_packages.append("inkscape")
all_packages.append("calibre")
all_packages.append("pidgin")
all_packages.append("thunderbird")
all_packages.append("xchat")
all_packages.append("gnucash")
all_packages.append("libreoffice")
all_packages.append("vlc")
all_packages.append("youtube-dl")

#web stuff
all_packages.append("eclipse")
all_packages.append("mysql")
all_packages.append("mysql-workbench")
all_packages.append("filezilla")
all_packages.append("cssed")

all_packages.append("banshee")
all_packages.append("vlc")
all_packages.append("ipython")
all_packages.append("josm")
all_packages.append("python-bottle")

all_packages.append("wireshark")

sa.install_all(all_packages)
