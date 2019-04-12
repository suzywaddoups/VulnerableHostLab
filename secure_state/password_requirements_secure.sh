#!/bin/bash

# Script to set password creation & expiration requirements

# PASSWORD COMPLEXITY RULES
# minlen = 14 password must be 14 characters or more
# dcredit = -1 provide at least one digit
# ucredit = -1 provide at least one uppercase character
# ocredit = -1 provide at least one special character
# lcredit = -1 provide at least one lowercase character

# install pam_pwquality pre-packaged module which will be added to /etc/pam.d/common-password
apt-get -qq install libpam-pwquality
sudo pam-auth-update --force



if grep -q "password	requisite			pam_pwquality.so retry=3" /etc/pam.d/common-password; then
	echo "found"
else
	echo "not found"
	result=$(awk '/# here are the per-package modules \(the \"Primary\" block\)/ {print FNR}' /etc/pam.d/common-password)
	result=$((result+1))
	sed -i "${result}i\password requisite pam_pwquality.so retry=3" /etc/pam.d/common-password
  echo "added line"
fi


path_to_pwquality_file="/etc/security/pwquality.conf"

# Password Settings, defaults are minlen = 8 & 0 for the rest
minlenSetting="minlen = 14"
dcreditSetting="dcredit = -1"
ucreditSetting="ucredit = -1"
ocreditSetting="ocredit = -1"
lcreditSetting="lcredit = -1"

sed -i "s/\(.*"minlen" *\).*/$minlenSetting/" $path_to_pwquality_file
sed -i "s/\(.*"dcredit" *\).*/$dcreditSetting/" $path_to_pwquality_file
sed -i "s/\(.*"ucredit" *\).*/$ucreditSetting/" $path_to_pwquality_file
sed -i "s/\(.*"ocredit" *\).*/$ocreditSetting/" $path_to_pwquality_file
sed -i "s/\(.*"lcredit" *\).*/$lcreditSetting/" $path_to_pwquality_file



# PASSWORD EXPIRATION RULES
# PASS_MAX_DAYS 90 password will expire after 90 days

path_to_logindefs_file="/etc/login.defs"

# Password Settings, default is 99999
expirationSetting="PASS_MAX_DAYS	90"

sed -i "s/\(.*"PASS_MAX_DAYS" *\).*/$expirationSetting/" $path_to_logindefs_file
