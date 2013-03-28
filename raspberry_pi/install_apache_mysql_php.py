#!/bin/python
import sys
sys.path.append("../")
from SetupAutomator import *

sa = SetupAutomator("apt")
sa.update()

all_packages = []

all_packages.append("apache2")
all_packages.append("mysql-server")
all_packages.append("php5")
all_packages.append("php5-mysql")

#now install all listed packages
sa.install_all(all_packages)

####POST INSTALL

#starts mysql daemon for now
sa.run("sudo service start mysql")
#sets up mysql nicely
sa.run("sudo /usr/bin/mysql_secure_installation")
#stops mysql daemon
sa.run("sudo service stop mysql")
