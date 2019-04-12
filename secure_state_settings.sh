#!/bin/bash
#Bash Script to quickly run secure state settings

echo "Password Requirements:"
./secure_state/password_requirements_secure.sh
echo "--------------------"

echo "Account Login Fail:"
./secure_state/account_loginfail_secure.sh
echo "--------------------"

echo "Service Clients:"
./secure_state/serviceclients_secure.sh
echo "--------------------"

echo "SMB Auth:"
./secure_state/smb_auth_secure.sh
echo "--------------------"

echo "SSH Banner:"
./secure_state/ssh_banner_secure.sh
echo "--------------------"

echo "SSH Idle Timeout:"
./secure_state/ssh_idleTimeout_secure.sh
echo "--------------------"

echo "SSH Login Grace Time:"
./secure_state/ssh_loginGraceTime_secure.sh
echo "--------------------"

echo "SSH Max Auth Tries:"
./secure_state/ssh_maxAuthTries_secure.sh
echo "--------------------"

echo "SSH Root:"
./secure_state/ssh_root_secure.sh
echo "--------------------"

echo "Users and Groups (path ='secure_state/users_secure.csv'):"
./delUsers.sh
echo "Users and Groups Cont. (path='secure_state/users_secure.csv'):"
./addUsers.sh
