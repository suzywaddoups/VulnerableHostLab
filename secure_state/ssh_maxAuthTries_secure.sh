#!/bin/bash

# Script to set SSH MaxAuthTries to 4

path_to_file="/etc/ssh/sshd_config"
secureMaxAuthTries="MaxAuthTries 4"

#Find and replace MaxAuthTries if uncommented value exists and replace with vulnMaxAuthTries
# .* means replace all from beginning to end of line
sed -i "s/\(.*"MaxAuthTries" *\).*/$secureMaxAuthTries/" $path_to_file
sudo service sshd restart
