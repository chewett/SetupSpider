#!/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider()
sa.update() #update before trying to install new packages

all_packages = []

all_packages.append("fuse-devel")

#now install all listed packages
sa.install_all(all_packages)

sa.run("echo Now install truecrypt from the website")
