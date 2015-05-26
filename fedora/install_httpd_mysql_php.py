#!/bin/env python
import sys
sys.path.append("../")
from SetupSpider import *

sa = SetupSpider(install_type='dnf')
sa.update() #update before trying to install new packages

all_packages = []

all_packages.append("httpd")
all_packages.append("mysql")
all_packages.append("mysql-server")
all_packages.append("php")
all_packages.append("php-mysql")
all_packages.append("php-mcrypt")
all_packages.append("php-Smarty")

#now install all listed packages
sa.install_all(all_packages)

####POST INSTALL

#starts mysql daemon for now
sa.run("sudo systemctl start mysqld")
#sets up mysql nicely
sa.run("sudo /usr/bin/mysql_secure_installation")
#stops mysql daemon
sa.run("sudo systemctl stop mysqld")
