#!/bin/bash

# Script to set SSH LoginGraceTime back to default
# default "#LoginGraceTime 2m"

path_to_file="/etc/ssh/sshd_config"
loginGraceTime="#LoginGraceTime 2m"

sed -i "s/\(.*"LoginGraceTime" *\).*/$loginGraceTime/" $path_to_file
