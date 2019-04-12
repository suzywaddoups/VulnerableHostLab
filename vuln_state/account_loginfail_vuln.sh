#!/bin/bash
#Set the account lockout for failed password attempts

if grep -q "auth required pam_tally2.so onerr=fail audit silent deny=5 unlock_time=300" /etc/pam.d/common-auth; then
	echo "already vulnerable"
else
	echo "vuln state not found.  Setting vuln state."
	sed -i '/auth required pam_tally2.so onerr=fail audit silent deny=5 unlock_time=.*/d' /etc/pam.d/common-auth
fi
