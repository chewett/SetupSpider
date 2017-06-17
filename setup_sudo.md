How to set up sudo
==================

Preface: This was originally written 5 years ago (2012) while I first
started using linux. The below guide will typically work for most
linux operating systems however there is a better way.

Most distributions have a "can use sudo" group, typically called
`sudo` or `wheel`.

##Original guide

need to add the user to sudo'ers list

run as root: 
visudo

go to the line
root 	(ALL)=ALL		ALL
and add your username below with the same config, eg for chewett
chewett (ALL)=ALL		ALL
