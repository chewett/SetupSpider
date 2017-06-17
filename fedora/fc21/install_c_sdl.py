#!/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider()
sa.update() #update before trying to install new packages

all_packages = []

all_packages.append("SDL*")
all_packages.append("gcc-c++")
all_packages.append("gdb")
all_packages.append("valgrind")

#now install all listed packages
sa.install_all(all_packages)

#install all the c stuff
sa.group_install('Development Tools')
