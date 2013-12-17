#!/bin/bash
wget https://dl-ssl.google.com/linux/linux_signing_key.pub
rpm --import linux_signing_key.pub

echo "[google]
name=Google Chrome 64-bit
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64" >> /etc/yum.repos.d/google.repo

yum install google-chrome-stable
