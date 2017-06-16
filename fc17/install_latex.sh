#!/bin/bash

#texmaker to type stuff
yum install texmaker

#this is the installation for gatex automata drawing and other rubbish
yum install tex-gastex

#add all the nice fonts
yum install texlive-collection-fontsrecommended texlive-times

#we want fullpage
yum install 'tex(fullpage.sty)'
