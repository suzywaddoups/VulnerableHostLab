#!/bin/bash
#Set the account lockout for failed password attempts

if grep -q "auth required pam_tally2.so onerr=fail audit silent deny=5 unlock_time=900" /etc/pam.d/common-auth; then
	echo "already secure"
else
	echo "not found. Adding secure state line."
	result=$(awk '/# here are the per-package modules \(the \"Primary\" block\)/ {print FNR}' /etc/pam.d/common-auth)
	result=$((result+1))
	sed -i "${result}i\auth required pam_tally2.so onerr=fail audit silent deny=5 unlock_time=900" /etc/pam.d/common-auth
fi
