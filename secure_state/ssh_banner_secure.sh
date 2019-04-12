#!/bin/bash

# Script to setup SSH banner message
# default "#Banner none" in /etc/ssh/sshd_config
# default "Ubuntu 18.04.1 LTS" banner message in /etc/issue.net

path_to_ssh_config_file="/etc/ssh/sshd_config"
#sshBannerPath = "/etc/issue.net"
sshBannerPath="Banner \/etc\/issue\.net"

path_to_banner_message_file="/etc/issue.net"
sshBannerMessage="WARNING: Unauthorized access to this system is forbidden and will be prosecuted by law. By accessing this system, you agree that your actions may be monitored and recorded by system personnel."

# Point ssh config file banner to display /etc/issue.net file contents
sed -i "s/\(.*"Banner" *\).*/$sshBannerPath/" $path_to_ssh_config_file

# change text in /etc/issue.net to show sshBannerMessage
echo $sshBannerMessage > $path_to_banner_message_file
sudo service sshd restart
