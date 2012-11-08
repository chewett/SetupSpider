#!/bin/bash

#install libkoki dependencies

yum install gcc rubygem-ditz PyYAML libyaml-devel doxygen opencv-devel scons glib2-devel freeglut mingw32-freeglut
yum install freeglut-devel

#below probably not needed now
#yum install mesa-libGL-devel mesa-libGLU-devel mesa-libGLw-devel mesa-libOSMesa-devel
