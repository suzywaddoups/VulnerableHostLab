#!/bin/bash

# Below is the same as the default MaxAuthTries = 6
# Running script will insure it has not been changed

path_to_file="/etc/ssh/sshd_config"
vulnMaxAuthTries="#MaxAuthTries 6"

#Find and replace MaxAuthTries if uncommented value exists and replace with vulnMaxAuthTries
# .* means replace all from beginning to end of line
sed -i "s/\(.*"MaxAuthTries" *\).*/$vulnMaxAuthTries/" $path_to_file
sudo service sshd restart
