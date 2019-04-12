#!/bin/bash
#Configure  SMB
echo "This script requires an OS dependency. Be sure to execute dependencies.sh prior to this script"
if [ -e /etc/samba/smb.conf_backup ];
then
echo "Restoring SMB Config Backup"
sudo mv /etc/samba/smb.conf_backup /etc/samba/smb.conf
cp /etc/samba/smb.conf /etc/samba/smb.conf_backup
bash -c 'grep -v -E "^#|^;" /etc/samba/smb.conf_backup | grep . > /etc/samba/smb.conf';
else
echo "Creating SMB Config Backup"
cp /etc/samba/smb.conf /etc/samba/smb.conf_backup
bash -c 'grep -v -E "^#|^;" /etc/samba/smb.conf_backup | grep . > /etc/samba/smb.conf';
fi


printf "[homes]\n   comment = Home Directories\n   browseable = yes\n   read only = no\n   create mask = 0700\n   directory mask = 0700\n   valid users = %S" >> /etc/samba/smb.conf

echo -e "ldelaney\nldelaney" | sudo smbpasswd -a ldelaney
echo "Created SMB user for ldelaney"

echo -e "breilly\nbreilly" | sudo smbpasswd -a breilly
echo "Created SMB user for breilly"

echo -e "cfarley\ncfarley" | sudo smbpasswd -a cfarley
echo "Created SMB user for cfarley"

systemctl restart smbd

echo "Samba is now configure to require authentication. Make sure the VM's network is BRIDGED. You can access the share through \\\ip_address\homes"

