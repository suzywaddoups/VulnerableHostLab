#!/bin/bash
#Bash Script to quickly run vuln state settings
echo "Account Login Fail:"
./vuln_state/account_loginfail_vuln.sh
echo "--------------------"

echo "Password Requirements:"
./vuln_state/password_requirements_vuln.sh
echo "--------------------"

echo "Service Clients:"
./vuln_state/serviceclients_vuln.sh
echo "--------------------"

echo "SMB Auth:"
./vuln_state/smb_auth_vuln.sh
echo "--------------------"

echo "SSH Banner:"
./vuln_state/ssh_banner_vuln.sh
echo "--------------------"

echo "SSH Idle Timeout:"
./vuln_state/ssh_idleTimeout_vuln.sh
echo "--------------------"

echo "SSH Login Grace Time:"
./vuln_state/ssh_loginGraceTime_vuln.sh
echo "--------------------"

echo "SSH Max Auth Tries:"
./vuln_state/ssh_maxAuthTries_vuln.sh
echo "--------------------"

echo "SSH Root:"
./vuln_state/ssh_root_vuln.sh
echo "--------------------"

echo "Users and Groups (path='secure_state/users_secure.csv'):"
./delUsers.sh
echo "Users and Groups Cont. (path='vuln_state/users_vuln.csv'):"
./addUsers.sh
