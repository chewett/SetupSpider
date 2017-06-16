#!/bin/bash

#####################
# NOTE
#####################
#
# This works mostlfy for fedora 17 Dell XPS L502x and will need changes
#
# These instructions were found at:
# http://techies.ncsu.edu/wiki/bumblebee
#

yum -y --nogpgcheck install http://install.linux.ncsu.edu/pub/yum/itecs/public/bumblebee-nonfree/fedora17/noarch/bumblebee-nonfree-release-1.0-1.noarch.rpm
yum -y --nogpgcheck install http://install.linux.ncsu.edu/pub/yum/itecs/public/bumblebee/fedora17/noarch/bumblebee-release-1.0-1.noarch.rpm
yum -y install bumblebee-nvidia
