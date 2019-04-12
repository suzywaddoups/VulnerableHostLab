#! /bin/bash
#Script to enable Root login through ssh

echo "Setting root password to: 1h@v3@llp0w3r"
echo -e "1h@v3@llp0w3r\n1h@v3@llp0w3r" | passwd root

sed -i 's/PermitRootLogin no/PermitRootLogin yes/' /etc/ssh/sshd_config
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

sudo service sshd restart
