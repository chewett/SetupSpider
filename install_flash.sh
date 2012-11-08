#!/bin/bash
su -c 'rpm -ivh adobe-release-x86_64-1.0-1.noarch.rpm'
su -c 'rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux'
su -c 'yum install nspluginwrapper alsa-plugins-pulseaudio flash-plugin'
