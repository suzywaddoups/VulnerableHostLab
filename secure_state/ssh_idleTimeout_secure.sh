#!/bin/bash

# Script to configure SSH Idle Timeout
# Sets ClientAliveInterval to 300 seconds (5 min) and ClientAliveCountMax to 0 so that no keepalive messages will be sent
# default "#ClientAliveInterval 0"
# default "#ClientAliveCountMax 3"

path_to_file="/etc/ssh/sshd_config"
clientAliveInterval="ClientAliveInterval 300"
clientAliveCountMax="ClientAliveCountMax 0"

sed -i "s/\(.*"ClientAliveInterval" *\).*/$clientAliveInterval/" $path_to_file
sed -i "s/\(.*"ClientAliveCountMax" *\).*/$clientAliveCountMax/" $path_to_file
sudo service sshd restart
