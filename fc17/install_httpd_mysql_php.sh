#!/bin/bash

#the webserver
yum install httpd

#install mysql and the server application
yum install mysql mysql-server

#install php
#php-mcrypt - needed for encryption stuff
yum install php php-mysql php-mcrypt

####POST INSTALL

#starts mysql daemon for now
systemctl start mysqld
#sets up mysql nicely
/usr/bin/mysql_secure_installation
#stops mysql daemon
systemctl stop mysqld
