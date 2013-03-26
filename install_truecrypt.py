#!/bin/python
from SetupAutomator import *

sa = SetupAutomator()
sa.update() #update before trying to install new packages

all_packages = []

all_packages.append("fuse-devel")

#now install all listed packages
sa.install_all(all_packages)

sa.run("echo Now install truecrypt from the website")
