#!/bin/bash

# Script to remove SSH banner message - back to default
# default "#Banner none" in /etc/ssh/sshd_config
# default "Ubuntu 18.04.1 LTS" banner message in /etc/issue.net

path_to_ssh_config_file="/etc/ssh/sshd_config"
sshBannerPath="#Banner none"

path_to_banner_message_file="/etc/issue.net"
osInfo="$(lsb_release -a | grep Description)"
osInfoString="$(awk -F ":" '{print $2}' <<< $osInfo)"
sshBannerMessage=$osInfoString

# Point ssh config file banner to display /etc/issue.net file contents
sed -i "s/\(.*"Banner" *\).*/$sshBannerPath/" $path_to_ssh_config_file

# change text in /etc/issue.net to show sshBannerMessage
echo $sshBannerMessage > $path_to_banner_message_file
sudo service sshd restart
