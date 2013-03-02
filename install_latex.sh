#!/bin/bash

#texmaker to type stuff
yum install texmaker -y

#this is the installation for gatex automata drawing and other rubbish
yum install tex-gastex -y

#add all the nice fonts
yum install texlive-collection-fontsrecommended texlive-times -y

yum install tex-adjustbox -y

#we want fullpage
yum install 'tex(fullpage.sty)' -y
