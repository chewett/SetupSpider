#!/bin/bash

#####################
# NOTE
#####################
#
# This works mostlfy for fedora 18 Dell XPS L502x and will need changes
#
# These instructions were found at:
# http://techies.ncsu.edu/wiki/bumblebee
#

yum -y --nogpgcheck install http://install.linux.ncsu.edu/pub/yum/itecs/public/bumblebee-nonfree/fedora18/noarch/bumblebee-nonfree-release-1.0-1.noarch.rpm
yum -y install bumblebee-nvidia
