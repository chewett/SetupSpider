#!/bin/bash

#the webserver
yum install httpd -y

#install mysql and the server application
yum install mysql mysql-server -y

#install php
#php-mcrypt - needed for encryption stuff
yum install php php-mysql php-mcrypt -y
yum install -y php-Smarty #this is a templating engine used by SR web

####POST INSTALL

#starts mysql daemon for now
systemctl start mysqld
#sets up mysql nicely
/usr/bin/mysql_secure_installation
#stops mysql daemon
systemctl stop mysqld
