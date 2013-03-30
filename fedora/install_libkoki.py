#!/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider()
sa.update() #update before trying to install new packages

#libkoki dependencies
all_packages = ["gcc", "rubygem-ditz", "PyYAML", "libyaml-devel", "doxygen", "opencv-devel", "scons", "glib2-devel", "freeglut", "mingw32-freeglut", "freeglut-devel"]

#now install all listed packages
sa.install_all(all_packages)
