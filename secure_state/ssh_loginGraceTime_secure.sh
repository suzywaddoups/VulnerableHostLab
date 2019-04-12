#!/bin/bash

# Script to set SSH LoginGraceTime to one minute or less
# default "#LoginGraceTime 2m"

path_to_file="/etc/ssh/sshd_config"
loginGraceTime="LoginGraceTime 60"
# ^ could also set to "1m"

sed -i "s/\(.*"LoginGraceTime" *\).*/$loginGraceTime/" $path_to_file
