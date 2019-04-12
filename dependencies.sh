#!/bin/bash
#Bash Script to install dependencies

apt-get install openssh-server
apt-get install net-tools
apt-get install tasksel
tasksel install samba-server

#dependencies for grading script
apt install python3
apt install python3-pip
su -c "pip3 install colorama" sysadmin
su -c "pip3 install paramiko" sysadmin
su -c "pip3 install cryptography==2.4.2" sysadmin
su -c "pip3 install pysmb" sysadmin
