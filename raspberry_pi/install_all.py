#!/bin/python
import sys
sys.path.append("../")
from SetupAutomator import *

sa = SetupAutomator("apt")

all_packages = []

all_packages.append("screen")
all_packages.append("vim")

#now install all listed packages
sa.install_all(all_packages)
