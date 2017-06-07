#!/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider(install_type='dnf')
sa.update() #update before trying to install new packages

all_packages = []

all_packages.append("texlive")
all_packages.append("texmaker")
all_packages.append("tex-gastex")
all_packages.append("texlive-collection-fontsrecommended")
all_packages.append("texlive-times")
all_packages.append("texlive-detex")
all_packages.append("tex-adjustbox")
all_packages.append("tex(fullpage.sty)")

#now install all listed packages
sa.install_all(all_packages)
