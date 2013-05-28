#!/usr/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider("apt")
sa.update() #update before trying to install new packages

all_packages = []

all_packages.append("mysql-server")
all_packages.append("mysql-client")
all_packages.append("apache2")
all_packages.append("php5")
all_packages.append("libapache2-mod-php5")
all_packages.append("php5-mysql")
all_packages.append("php5-gd")
all_packages.append("php5-curl")
all_packages.append("php5-imagick")
all_packages.append("php5-mcrypt")
all_packages.append("php5-sqlite")

#now install all listed packages
sa.install_all(all_packages)
