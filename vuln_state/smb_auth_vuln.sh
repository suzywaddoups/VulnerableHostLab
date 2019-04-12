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


printf "[public]\n   comment = allow access\n   path = /home\n   browsable =yes\n   create mask = 0660\n   directory mask = 0771\n   writable = yes\n   guest ok = yes" >> /etc/samba/smb.conf

systemctl restart smbd

echo "Samba is now configure to allow annonymous login. Make sure the VM's network is BRIDGED. You can access the share through \\\ip_address\Public"
