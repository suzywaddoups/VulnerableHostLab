#!/bin/bash

# Script to change configure SSH Idle Timeout back to default
# default "#ClientAliveInterval 0"
# default "#ClientAliveCountMax 3"

path_to_file="/etc/ssh/sshd_config"
clientAliveInterval="#ClientAliveInterval 0"
clientAliveCountMax="#ClientAliveCountMax 3"

sed -i "s/\(.*"ClientAliveInterval" *\).*/$clientAliveInterval/" $path_to_file
sed -i "s/\(.*"ClientAliveCountMax" *\).*/$clientAliveCountMax/" $path_to_file
sudo service sshd restart
