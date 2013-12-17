#!/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider()
sa.update() #update before trying to install new packages

all_packages = []

all_packages.append("oad")
all_packages.append("wesnoth")

#now install all listed packages
sa.install_all(all_packages)
