#!/bin/bash

# Script to set password creation & expiration requirements back to default

# PASSWORD COMPLEXITY RULES

# uninstall pam_pwquality pre-packaged module which added lines to /etc/pam.d/common-password
apt-get --purge -qq remove libpam-pwquality


if grep -q "password requisite pam_pwquality.so retry=3" /etc/pam.d/common-password; then
	echo "found"
	sed -i '/password requisite pam_pwquality.so retry=3/d' /etc/pam.d/common-password
else
	echo "not found"
fi


path_to_pwquality_file="/etc/security/pwquality.conf"

# Password Settings, defaults are minlen = 8 & 0 for the rest
minlenSetting="minlen = 8"
dcreditSetting="dcredit = 0"
ucreditSetting="ucredit = 0"
ocreditSetting="ocredit = 0"
lcreditSetting="lcredit = 0"

sed -i "s/\(.*"minlen" *\).*/$minlenSetting/" $path_to_pwquality_file
sed -i "s/\(.*"dcredit" *\).*/$dcreditSetting/" $path_to_pwquality_file
sed -i "s/\(.*"ucredit" *\).*/$ucreditSetting/" $path_to_pwquality_file
sed -i "s/\(.*"ocredit" *\).*/$ocreditSetting/" $path_to_pwquality_file
sed -i "s/\(.*"lcredit" *\).*/$lcreditSetting/" $path_to_pwquality_file



# PASSWORD EXPIRATION RULES
# PASS_MAX_DAYS 90 password will expire after 90 days

path_to_logindefs_file="/etc/login.defs"

# Password Settings, default is 99999
expirationSetting="PASS_MAX_DAYS	99999"

sed -i "s/\(.*"PASS_MAX_DAYS" *\).*/$expirationSetting/" $path_to_logindefs_file
