#!/usr/bin/python3

# Host Grader for the following labs:
# (1) Insecure Service Clients
# (2) User and Password Management
# (3) SSH Server Configuration
# (4) SMB Secure Configuration

import requests
import smtplib
from colorama import Fore, Style
import time
import base64
import subprocess
import paramiko
from smb.SMBConnection import SMBConnection


#TO CHANGE PASSWORD: base64 encoded new email password
emailAccount = '<<Enter New Email Address>>'
emailPassword = <<Enter New base64 Encoded Email Password>>

#Email that will recieve the students' scores on the hard Difficulty
hardDifficultySubmit = '<<Enter New Email Address>>'

#TO CHANGE PASSWORD: base64 encoded new passwords for easy & normal difficulty settings
#default password for easy difficulty mode = enableEasy
easyDifficultyPassword = <<Enter New base64 Encoded Easy Difficulty Password>>
#default password for normal difficulty mode = enableNormal
normalDifficultyPassword = <<Enter New base64 Encoded Normal Difficulty Password>>

def gradeServices(difficulty):
    print(Style.BRIGHT + '\n'+"-" * 31)
    print("Grading Insecure Service Clients Lab...")
    print("=" * 31 + Style.NORMAL)

    message = "-" * 40 + '\n'
    message = message + "Grade for Insecure Service Clients Lab: \n"
    message = message + "-" * 40 + '\n'

    try:
        #Commands
        nisCheck = subprocess.run('''
            dpkg -s nis
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("NIS CHECK: ---", nisCheck.stdout, '---')
        #If/else statements to see if pass or fail
        #create a boolean for each check

        if (nisCheck.stdout.find("install ok installed") !=-1):
            nisCheck = True
        else:
            nisCheck = False

        if (nisCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'The insecure NIS client was NOT uninstalled')
            message = message + "(0/1) FAIL: The insecure NIS client was NOT uninstalled. \n"

            if (difficulty == "1"):
                print("  HINT: Uninstall the insecure NIS client")
                print("    (sudo apt-get remove nis)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'The insecure NIS client was uninstalled')
            message = message + "(1/1) PASS: The insecure NIS client was uninstalled! \n"
    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to execute command')
        message = 'Error: Failed to successfully execute command\n'

    try:
        #Commands
        rshCheck = subprocess.run('''
            dpkg -s rsh-client
            dpkg -s rsh-redone-client
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("RSH CHECK: ---", rshCheck.stdout, '---')
        #If/else statements to see if pass or fail
        #create a boolean for each check

        if (rshCheck.stdout.find("install ok installed") !=-1):
            rshCheck = True
        else:
            rshCheck = False

        if (rshCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'The insecure RSH client was NOT uninstalled')
            message = message + "(0/1) FAIL: The insecure RSH client was NOT uninstalled. \n"

            if (difficulty == "1"):
                print("  HINT: Uninstall the insecure RSH client")
                print("    (sudo apt-get remove rsh-client rsh-redone-client)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'The insecure RSH client was uninstalled')
            message = message + "(1/1) PASS: The insecure RSH client was uninstalled! \n"
    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to execute command')
        message = 'Error: Failed to successfully execute command\n'

    try:
        #Commands
        talkCheck = subprocess.run('''
            dpkg -s talk
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("TALK CHECK: ---", talkCheck.stdout, '---')
        #If/else statements to see if pass or fail
        #create a boolean for each check

        if (talkCheck.stdout.find("install ok installed") !=-1):
            talkCheck = True
        else:
            talkCheck = False

        if (talkCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'The insecure Talk client was NOT uninstalled')
            message = message + "(0/1) FAIL: The insecure Talk client was NOT uninstalled. \n"

            if (difficulty == "1"):
                print("  HINT: Uninstall the insecure Talk client")
                print("    (sudo apt-get remove talk)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'The insecure Talk client was uninstalled')
            message = message + "(1/1) PASS: The insecure Talk client was uninstalled! \n"
    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to execute command')
        message = 'Error: Failed to successfully execute command\n'

    try:
        #Commands
        telnetCheck = subprocess.run('''
            dpkg -s telnet
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("TELNET CHECK: ---", telnetCheck.stdout, '---')
        #If/else statements to see if pass or fail
        #create a boolean for each check

        if (telnetCheck.stdout.find("install ok installed") !=-1):
            telnetCheck = True
        else:
            telnetCheck = False

        if (telnetCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'The insecure Telnet client was NOT uninstalled')
            message = message + "(0/1) FAIL: The insecure Telnet client was NOT uninstalled. \n"

            if (difficulty == "1"):
                print("  HINT: Uninstall the insecure Telnet client")
                print("    (sudo apt-get remove telnet)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'The insecure Telnet client was uninstalled')
            message = message + "(1/1) PASS: The insecure Telnet client was uninstalled! \n"
    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to execute command')
        message = 'Error: Failed to successfully execute command\n'


    return message


def gradeUsers(difficulty):
    print(Style.BRIGHT + '\n'+"-" * 31)
    print("Grading User and Password Management Lab...")
    print("=" * 31 + Style.NORMAL)

    # ############################### #
    # CHECK FOR CORRECT USERS/GROUPS  #
    # ############################### #
    try:
        #Commands
        userCommandOutput = subprocess.run('''

        # Script to check that all users and their correct groups were added to system

        #CHECK FOR USERNAMES

        #CSV file containing all usernames & groups
        user_file="users.csv"

        if [ ! -f "$user_file" ]
        then
          echo "Cannot find file $user_file"
        else
          #create arrays of groups, full names, and usernames
          groups=(`cut -d: -f 3 "$user_file" | sed 's/ //'`)
          fullnames=(`cut -d: -f 1 "$user_file"`)
          userid=(`cut -d: -f 2 "$user_file"`)
          usernames=(`cut -d: -f 2 "$user_file"`)

          x=0
          for user in ${usernames[*]}
          do
            #check for usernames
            if grep -q $user "/etc/passwd"
            then
              :
              # echo $user Found
            else
              :
              # echo $user NOT Found
              userMissing=true
            fi
            #check if users are in correct groups
            if ( groups $user | grep -q ${groups[$x]} ) &> /dev/null
            then
              :
              # echo $user assigned to correct group
            else
              :
              # echo $user NOT assigned to incorrect group
              groupMissing=true
            fi
            x=$x+1
          done

          if [ "$userMissing" = true ]
          then
            echo FAIL: At least one of the above users was not added.
          else
            echo PASS: All users were found.
          fi

          if [ "$groupMissing" = true ]
          then
            echo FAIL: At least one of the above users is assigned to the wrong group.
          else
            echo PASS: All users assigned to correct groups.
          fi

        fi
        ''', stdout=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')

        #If/else statements to see if pass or fail
        message = "-" * 40 + '\n'
        message = message + "Grade for User and Password Management Lab: \n"
        message = message + "-" * 40 + '\n'

        #if cannot find user csv file, print error and exit function
        if (userCommandOutput.stdout.find('Cannot find file') !=-1):
            print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to execute command.  Cannot find user CSV file.')
            message = 'Error: Failed to successfully execute command.  Could not find user CSV file.\n'

            #if cannot find file, include normal system users in email message
            systemUsers = subprocess.run("for user in $(awk -F'[/:]' '{if ($3 >= 1000 && $3 != 65534) print $1}' /etc/passwd); do groups $user; done", stdout=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash' )
            message = message + 'System Users and Groups: \n' + systemUsers.stdout + '\n'
            return message

        #create a boolean for each check
        if (userCommandOutput.stdout.find('PASS: All users were found.') !=-1):
            userPass = True
        else:
            userPass = False

        if (userCommandOutput.stdout.find('PASS: All users assigned to correct groups.') !=-1):
            groupPass = True
        else:
            groupPass = False

        #Check for Users
        if (userPass):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'Missing users added')
            message = message + "(1/1) PASS: Missing users added! \n"
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'Missing users NOT added')
            message = message + "(0/1) FAIL: Missing users were NOT added. \n"

            if (difficulty == "1"):
                print("  HINT: There are two users missing.")
                print("    (use command 'sudo useradd -c <full name> -g <group> -p <password> -m <username>' to create a user, add them to a group, and create the user's home directory.)")

        #Check User Groups
        if (groupPass):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'Incorrect group assignments fixed')
            message = message + "(1/1) PASS: Incorrect group assignments fixed! \n"
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'Incorrect group assignments were NOT fixed')
            message = message + "(0/1) FAIL: Incorrect group assignments were NOT fixed. \n"

            if (difficulty == "1"):
                print("  HINT: Three users are in the incorrect group.")
                print("    (To change a user's primary group, run command 'sudo usermod -g <groupname> <username>')")

        #If test fails for users or groups, return command output in email message
        if not (userPass or groupPass):
            try:
                systemUserGroupsOutput = subprocess.run('''
                    for user in $(getent passwd {1000..60000} | cut -d ':' -f 1); do groups $user; done
                    ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
                message = message + "\t Current System Users/Groups:\n" + systemUserGroupsOutput.stdout + "\n"
            except:
                print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to execute command')
                message = 'Error: Failed to successfully execute command\n'


    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to execute command')
        message = 'Error: Failed to successfully execute command\n'


    # ################################# #
    # CHECK FOR REQUIRED PASSWORD RULES #
    # ################################# #

    # PASSWORD COMPLEXITY RULES
    # minlen = 14 password must be 14 characters or more
    # dcredit = -1 provide at least one digit
    # ucredit = -1 provide at least one uppercase character
    # ocredit = -1 provide at least one special character
    # lcredit = -1 provide at least one lowercase character

    # PASSWORD EXPIRATION RULES
    # PASS_MAX_DAYS 90 = password will expire after 90 days
        # chage -l testuser (output contains "Maximum number of days between password change		: 90")

    # ACCOUNT LOCKOUT RULE
    # Account Lockout after 5 failed attempts for 300sec (5min)
        # passwd -S testuser (output contains "testuser L" if locked, not "testuser P")

    try:
        #Commands
        #Add Test User
        subprocess.run('''
            sudo useradd -m testuser &> /dev/null
            ( echo -e '$ecure1T&$erverz\n$ecure1T&$erverz' | sudo passwd testuser ) &> /dev/null
            ''', shell=True, executable='/bin/bash')

        minLenCheck = subprocess.run('''
            echo -e '$ecure1T&$erverz\nHe11opa$$word\nHe11opa$$word' | sudo runuser -l testuser -c "passwd testuser"
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("MIN CHECK: ---", minLenCheck.stderr, '---')

        dcreditCheck = subprocess.run('''
            echo -e '$ecure1T&$erverz\n$ecure1T&$erverz' | sudo passwd testuser
            echo -e '$ecure1T&$erverz\nHellopa$$word!\nHellopa$$word!' | sudo runuser -l testuser -c "passwd testuser"
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("DCREDIT CHECK: ---", dcreditCheck.stderr, '---')

        ucreditCheck = subprocess.run('''
            echo -e '$ecure1T&$erverz\n$ecure1T&$erverz' | sudo passwd testuser
            echo -e '$ecure1T&$erverz\nhe11opa$$word!\nhe11opa$$word!' | sudo runuser -l testuser -c "passwd testuser"
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("UCREDIT CHECK: ---", ucreditCheck.stderr, '---')

        ocreditCheck = subprocess.run('''
            echo -e '$ecure1T&$erverz\n$ecure1T&$erverz' | sudo passwd testuser
            echo -e '$ecure1T&$erverz\nHe11opassword1\nHe11opassword1' | sudo runuser -l testuser -c "passwd testuser"
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("OCREDIT CHECK: ---", ocreditCheck.stderr, '---')

        lcreditCheck = subprocess.run('''
            echo -e '$ecure1T&$erverz\n$ecure1T&$erverz' | sudo passwd testuser
            echo -e '$ecure1T&$erverz\nHE11OPASSWORD!\nHE11OPASSWORD!' | sudo runuser -l testuser -c "passwd testuser"
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("LCREDIT CHECK: ---", lcreditCheck.stderr, '---')

        passMaxDaysCheck = subprocess.run('''
            echo -e '$ecure1T&$erverz\n$ecure1T&$erverz' | sudo passwd testuser
            sudo chage -l testuser
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("PASS_MAX_DAYS CHECK: ---", passMaxDaysCheck.stdout, '---')

        accountLockoutCheck = subprocess.run('''
            echo -e '$ecure1T&$erverz\n$ecure1T&$erverz' | sudo passwd testuser
            sudo grep "deny=" /etc/pam.d/common-auth | grep "unlock_time="
            ''', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True, universal_newlines=True, executable='/bin/bash')
        # print("ACCOUNT LOCKOUT CHECK: ---", accountLockoutCheck.stdout, '---')

        accountLockoutText = accountLockoutCheck.stdout

        #If/else statements to see if pass or fail
        #MinLen Check
        if (minLenCheck.stderr.find('The password is shorter than 14 characters') !=-1):
            minLenCheck = False
        else:
            minLenCheck = True

        if (minLenCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'Password minimum length rule was NOT fixed')
            message = message + "(0/1) FAIL: Password minimum length rule was NOT fixed. \n"
            if (difficulty == "1"):
                print("  HINT: Install and set the pam_pwquality module's minlen to require at least 14 characters in /etc/security/pwquality.conf")
                print("    (minlen = 14)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'Password minimum length rule is set to 14 characters')
            message = message + "(1/1) PASS: Password minimum length rule is set to 14 characters! \n"

        #Dcredit Check
        if (dcreditCheck.stderr.find('The password contains less than 1 digits') !=-1):
            dcreditCheck = False
        else:
            dcreditCheck = True

        if (dcreditCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'Password dcredit rule was NOT fixed')
            message = message + "(0/1) FAIL: Password dcredit rule was NOT fixed. \n"
            if (difficulty == "1"):
                print("  HINT: Install and set the pam_pwquality module's dcredit to require at least 1 digit in /etc/security/pwquality.conf")
                print("    (dcredit = -1)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'Password dcredit rule is set to contain at least 1 digit')
            message = message + "(1/1) PASS: Password dcredit rule is set to contain at least 1 digit! \n"

        #Ucredit Check
        if (ucreditCheck.stderr.find('The password contains less than 1 uppercase letters') !=-1):
            ucreditCheck = False
        else:
            ucreditCheck = True

        if (ucreditCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'Password ucredit rule was NOT fixed')
            message = message + "(0/1) FAIL: Password ucredit rule was NOT fixed. \n"
            if (difficulty == "1"):
                print("  HINT: Install and set the pam_pwquality module's ucredit to require at least 1 uppercase letter in /etc/security/pwquality.conf")
                print("    (ucredit = -1)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'Password ucredit rule is set to contain at least 1 uppercase letter')
            message = message + "(1/1) PASS: Password ucredit rule is set to contain at least 1 uppercase letter! \n"

        #Ocredit Check
        if (ocreditCheck.stderr.find('The password contains less than 1 non-alphanumeric characters') !=-1):
            ocreditCheck = False
        else:
            ocreditCheck = True

        if (ocreditCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'Password ocredit rule was NOT fixed')
            message = message + "(0/1) FAIL: Password ocredit rule was NOT fixed. \n"
            if (difficulty == "1"):
                print("  HINT: Install and set the pam_pwquality module's ocredit to require at least 1 non-alphanumeric character in /etc/security/pwquality.conf")
                print("    (ocredit = -1)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'Password ocredit rule is set to contain at least 1 non-alphanumeric character')
            message = message + "(1/1) PASS: Password ocredit rule is set to contain at least 1 non-alphanumeric character! \n"

        #Lcredit Check
        if (lcreditCheck.stderr.find('The password contains less than 1 lowercase letters') !=-1):
            lcreditCheck = False
        else:
            lcreditCheck = True

        if (lcreditCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'Password lcredit rule was NOT fixed')
            message = message + "(0/1) FAIL: Password lcredit rule was NOT fixed. \n"
            if (difficulty == "1"):
                print("  HINT: Install and set the pam_pwquality module's lcredit to require at least 1 lowercase letter in /etc/security/pwquality.conf")
                print("    (lcredit = -1)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'Password lcredit rule is set to contain at least 1 lowercase letter')
            message = message + "(1/1) PASS: Password lcredit rule is set to contain at least 1 lowercase letter! \n"

        #MPass_Max_Days Check
        if (passMaxDaysCheck.stdout.find('Maximum number of days between password change		: 90') !=-1):
            passMaxDaysCheck = False
        else:
            passMaxDaysCheck = True

        if (passMaxDaysCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'Password expiration rule was NOT fixed')
            message = message + "(0/1) FAIL: Password expriation rule was NOT fixed. \n"
            if (difficulty == "1"):
                print("  HINT: Set passwords to expire after 90 days in /etc/login.defs")
                print("    (PASS_MAX_Days 90)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'Password is set to expire after 90 days')
            message = message + "(1/1) PASS: Password is set to expire after 90 days! \n"

        #Account Lockout Check
        if (accountLockoutCheck.stdout.find("deny=5") !=-1 and accountLockoutCheck.stdout.find("unlock_time=900") !=-1):
            accountLockoutCheck = False
        else:
            accountLockoutCheck = True

        if (accountLockoutCheck):
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'Password lockout rules were NOT fixed')
            message = message + "(0/1) FAIL: Password lockout rules were NOT fixed. \n"
            message = message + "      Incorrect User's Rule: \' " + accountLockoutText + " \'\n"
            if (difficulty == "1"):
                print("  HINT: Set rules to lock accounts after 5 unsuccessful login attempts for 15 minutes (900 seconds) under the per-package modules section in /etc/pam.d/common-auth")
                print("    (auth required pam_tally2.so onerr=fail audit silent deny=5 unlock_time=900)")
        else:
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'Password is set to lockout after 5 attempts for 900 seconds')
            message = message + "(1/1) PASS: Password is set to lockout after 5 attempts for 900 seconds! \n"

        # sudo userdel testuser
        subprocess.run('''
            ( sudo userdel -f -r testuser > $(tty) ) &>/dev/null
            ''', shell=True, executable='/bin/bash')

    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to execute command')
        message = 'Error: Failed to successfully execute command\n'


    return message


def gradeSSH(difficulty):
    print(Style.BRIGHT + '\n'+"-" * 31)
    print("Grading SSH Server Configuration Lab...")
    print("=" * 31 + Style.NORMAL)

    #Variables
    hostname = "127.0.0.1"
    command = "echo success"
    port = 22
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    ####Check for SSH Root Login
    try:
        #Variables unique to SSH Root Login
        username = "root"
        password = "1h@v3@llp0w3r"

        #Commands
        client.connect(hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        #Check if Root sucessfully logged in & Set Boolean
        stdout = stdout.read()
        if (stdout == b'success\n'):
            sshRootPass = False
        else:
            print(Fore.RED + 'Unknown Exception: '+ Fore.WHITE +'Failed to check SSH Root Login')

    except Exception as e:
        if (str(e) == "Authentication failed."):
            sshRootPass = True
        else:
            print(Fore.RED + 'Unknown Exception: '+ Fore.WHITE +'Failed to check SSH Root Login')
    finally:
        client.close()

    ####Check for SSH Banner
    try:
        #Varialbes Unique to SSH Banner
        username="bwood"
        password="bwood"

        client.connect(hostname, port=port, username=username, password=password)
        banner = client._transport.get_banner()
        if(banner == None):
            sshBannerPass=False
        elif(banner is not None):
            sshBannerPass=True
        else:
            print("Banner could not be scored")
    except Exception as e:
        print(Fore.RED + 'Unknown Exception: '+ Fore.WHITE +'Failed to check SSH Banner')
    finally:
        client.close()
    ####Check for SSH idleTimeout
    try:
        #pull ClientAliveInterval from /etc/ssh/sshd_config
        sshconfig_ClientAliveInterval = subprocess.check_output('''
        grep "ClientAliveInterval" /etc/ssh/sshd_config
        ''', shell=True, universal_newlines=True, executable='/bin/bash')
        sshconfig_ClientAliveInterval.strip()

        index = sshconfig_ClientAliveInterval.find("300") #Try to find 300
        if (index != -1): #300 is found and configuration is accurate
            sshIdleIntervalPass = True
        else:
            sshIdleIntervalPass = False
        if(sshconfig_ClientAliveInterval[0] == "#"): #Check if line is commented out
            sshIdleIntervalPass = False

        #pull sshconfig_ClientAliveCountMax from /etc/ssh/sshd_config
        sshconfig_ClientAliveCountMax = subprocess.check_output('''
        grep "ClientAliveCountMax" /etc/ssh/sshd_config
        ''', shell=True, universal_newlines=True, executable='/bin/bash')
        sshconfig_ClientAliveCountMax.strip()

        index = sshconfig_ClientAliveCountMax.find("0") #Try to find 0
        if (index != -1): #0 is found and configuration is accurate
            sshIdleCountMaxPass = True
        else:
            sshIdleCountMaxPass = False
        if(sshconfig_ClientAliveCountMax[0] == "#"): #Check if line is commented out
            sshIdleCountMaxPass = False
    except Exception as e:
        print(Fore.RED + 'Unknown Exception: '+ Fore.WHITE +'Failed to check SSH idleTimeout')
    ####Check for SSH loginGraceTime
    try:
        #pull LoginGraceTime from /etc/ssh/sshd_config
        sshconfig_LoginGraceTime = subprocess.check_output('''
        grep "LoginGraceTime" /etc/ssh/sshd_config
        ''', shell=True, universal_newlines=True, executable='/bin/bash')
        sshconfig_LoginGraceTime.strip()

        index= sshconfig_LoginGraceTime.find("60") #Try to find 60 (60 seconds)
        if (index != -1): #60 is found and configuration is accurate
            sshLoginGraceTimePass = True
        elif((sshconfig_LoginGraceTime.find("1m"))!= -1): #1m is found and configuration is accurate
            sshLoginGraceTimePass = True
        else:
            sshLoginGraceTimePass = False
        if(sshconfig_LoginGraceTime[0] == "#"): #Check if line is commented out
            sshLoginGraceTimePass = False
    except Exception as e:
        print(Fore.RED + 'Unknown Exception: '+ Fore.WHITE +'Failed to check SSH loginGraceTime')

    ####Check for SSH maxAuthTries
    try:
        #pull MaxAuthTries from /etc/ssh/sshd_config
        sshconfig_MaxAuthTries = subprocess.check_output('''
        grep "MaxAuthTries" /etc/ssh/sshd_config
        ''', shell=True, universal_newlines=True, executable='/bin/bash')
        sshconfig_MaxAuthTries.strip()

        index= sshconfig_MaxAuthTries.find("4") #Try to find 4
        if (index != -1): #Pass; 4 is found and configuration is accurate
            sshMaxAuthTriesPass = True
        else:
            sshMaxAuthTriesPass = False
        if(sshconfig_MaxAuthTries[0] == "#"): #Check if line is commented out
            sshMaxAuthTriesPass = False
    except Exception as e:
        print(Fore.RED + 'Unknown Exception: '+ Fore.WHITE +'Failed to check SSH maxAuthTries')

    ####Provide Feedback and Record Score for SSH Server Configuration
    message = "-" * 40 + '\n'
    message = message + "Grade for SSH Server Configuration Lab: \n"
    message = message + "-" * 40 + '\n'

    try:
        if (sshRootPass): #if sshRoot login passes
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'SSH Root Login was fixed')
            message = message + "(1/1) PASS: SSH Root Login was fixed\n"
        elif(not sshRootPass): #if sshRoot login fails
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'SSH Root Login was NOT fixed')
                if(difficulty =="1"):
                    print("  HINT: Set the PermitRootLogin parameter to no in /etc/ssh/sshd_config")
                    print("    (PermitRootLogin no)")
            message = message + "(0/1) FAIL: SSH Root Login was NOT fixed\n"

        if(sshBannerPass): #if sshBanner passes
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'SSH Warning Banner was fixed')
            message = message + "(1/1) PASS: SSH Warning Banner was fixed\n"
        elif(not sshBannerPass): #if sshBanner fails
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'SSH Warning Banner was NOT fixed')
                if(difficulty =="1"):
                    print("  HINT: Set the Banner parameter to /etc/issue.net in /etc/ssh/sshd_config; Edit etc/issue.net to contain an SSH Warning")
                    print("    (Banner /etc/issue.net)")
            message = message + "(0/1) FAIL: SSH Warning Banner was NOT fixed\n"
        if(sshIdleIntervalPass and sshIdleCountMaxPass): #if sshIdle Timeout passes
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'SSH Idle Timeout was fixed')
            message = message + "(1/1) PASS: SSH Idle Timeout was fixed\n"
        elif(not (sshIdleIntervalPass and sshIdleCountMaxPass)): #if sshIdle Timeout Fails
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'SSH Idle Timeout was NOT fixed')
                if(difficulty =="1"):
                    print("  HINT: Set both the ClientAliveInterval parameter to 300 seconds (5 minutes) and the ClientAliveCountMax parameter to 0 in /etc/ssh/sshd_config")
                    print("    (ClientAliveInterval 300)")
                    print("    (ClientAliveCountMax 0)")
            message = message + "(0/1) FAIL: SSH Idle Timeout was NOT fixed\n"
            message = message + "      " + sshconfig_ClientAliveInterval
            message = message + "      " + sshconfig_ClientAliveCountMax
        if(sshLoginGraceTimePass): #if ssh LoginGraceTime passes
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'SSH LoginGraceTime was fixed')
            message = message + "(1/1) PASS: SSH LoginGraceTime was fixed\n"
        elif(not (sshLoginGraceTimePass)): #if ssh LoginGraceTime Fails
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'SSH LoginGraceTime was NOT fixed')
                if(difficulty =="1"):
                    print("  HINT: Set the LoginGraceTime parameter to 60 seconds in /etc/ssh/sshd_config")
                    print("    (LoginGraceTime 60)")
            message = message + "(0/1) FAIL: SSH LoginGraceTime was NOT fixed\n"
            message = message + "      " + sshconfig_LoginGraceTime
        if(sshMaxAuthTriesPass): #if ssh MaxAuthTries passes
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'SSH MaxAuthTries was fixed')
            message = message + "(1/1) PASS: SSH MaxAuthTries was fixed\n"
        elif(not (sshMaxAuthTriesPass)): #if ssh MaxAuthTries Fails
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'SSH MaxAuthTries was NOT fixed')
                if(difficulty =="1"):
                    print("  HINT: Set the MaxAuthTries parameter to 4 in /etc/ssh/sshd_config")
                    print("    (MaxAuthTries 4)")
            message = message + "(0/1) FAIL: SSH MaxAuthTries was NOT fixed\n"
            message = message + "      " + sshconfig_MaxAuthTries


    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to record grade for SSH')
        message = message + 'Error: Failed to record grade for SSH\n'

    return message


def gradeSMB(difficulty):
    print(Style.BRIGHT + '\n'+"-" * 31)
    print("Grading SMB Secure Configuration Lab...")
    print("=" * 31 + Style.NORMAL)

    #Variables
    userID = ''
    password = ''
    myname = ''
    remote_name = ''
    server_ip= '127.0.0.1'

    try:
        conn = SMBConnection(userID, password, myname, remote_name)
        conn.connect(server_ip, 445)
        shares=conn.listShares()
        sharenames=[]
        for share in shares:
            sharenames.append(share.name)
        if ('public' in sharenames):
            smbAuthPass = False
        elif ('homes' in sharenames):
            smbAuthPass = True
        else:
            raise Exception("Can't find neither the public share nor the homes share")
    except Exception as e:
        print(Fore.RED + 'Unknown Exception: '+ Fore.WHITE +'Failed to check SMB Configuration')
    finally:
        conn.close()

    ####Provide Feedback and Record Score for SMB Server Configuration
    message = "-" * 40 + '\n'
    message = message + "Grade for SMB Server Configuration Lab: \n"
    message = message + "-" * 40 + '\n'

    try:
        if(smbAuthPass): #if smb configuration passes
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.GREEN + 'PASS: '+ Fore.WHITE +'SMB Configuration was fixed')
            message = message + "(1/1) PASS: SMB Configuration was fixed\n"
        elif(not (smbAuthPass)): #if smb configuration Fails
            if (difficulty == "1" or difficulty == "2"):
                print(Fore.RED + 'FAIL: '+ Fore.WHITE +'SMB Configuration was NOT fixed')
                if(difficulty =="1"):
                    print("  HINT: Remove the entire [public] share in /etc/samba/smb.conf and replace it as a [homes] share")
                    print("    ([homes]\n       comment = Home Directories\n       browseable = yes\n       read only = no\n       create mask = 0700\n       directory mask = 0700\n       valid users = %S)")
            message = message + "(0/1) FAIL: SMB Configuration was NOT fixed\n"
            message = message + "      List of SMB Shares: " + str(sharenames)
    except:
        print(Fore.RED + 'Error: '+ Fore.WHITE +'Failed to record grade for SMB')
        message = message + 'Error: Failed to record grade for SMB\n'

    return message


def sendEmail(emailRecipient, subject, message):
    # smtplib module send mail
    TO = emailRecipient
    SUBJECT = subject
    TEXT = subject + '\n' + message

    # Gmail Sign In
    gmail_sender = emailAccount

    passEncoded = emailPassword
    passDecoded = base64.b64decode(passEncoded)
    passDecodedStr = passDecoded.decode("utf-8")

    gmail_passwd = passDecodedStr


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    try:
        server.login(gmail_sender, gmail_passwd)
    except:
        print(Fore.RED + 'ERROR: '+ Fore.WHITE + "Could not login to Mail Server")

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('\nEmail was successfully sent to ' + emailRecipient)
    except:
        print (Fore.RED + 'ERROR: '+ Fore.WHITE +'Could not send email')

    print("\nExiting in 5 seconds...")
    time.sleep(5)
    server.quit()

def main():
    emailMessage = ""

    difficultyMenu = True
    while (difficultyMenu == True):
        print("\n" +"-" *77)
        difficulty = input("Welcome to the Cyber Tower Defense Grader.  Please select a difficulty level: \
                            \n (1) Easy - Hints Provided & Unlimited Number of Tries \
                            \n (2) Normal - No Hints & Unlimited Number of Tries \
                            \n\n (3) Hard - No Hints & Limited Number of Tries \
                            \n\n To Exit Program (exit) \
                            \n \nEnter 1, 2, or 3: ")
        print("\n\n")

        if(difficulty == "1"):
            #User must enter password to use easier modes
            easyModePassword = input("Please Enter Password to use this Mode: ")
            easyModePassword = easyModePassword.encode()
            userInputEncoded = base64.b64encode(easyModePassword)

            if (userInputEncoded == easyDifficultyPassword):
                print("\n\n")
                emailMessage = "(Difficulty: Easy) \n"
                difficultyMenu = False
            else:
                print(Fore.RED + "\nInvalid Password\n\n"+ Fore.WHITE)
                continue

        elif(difficulty == "2"):
            #User must enter password to use easier modes
            normalModePassword = input("Please Enter Password to use this Mode: ")
            normalModePassword = normalModePassword.encode()
            userInputEncoded = base64.b64encode(normalModePassword)

            if (userInputEncoded == normalDifficultyPassword):
                print("\n\n")
                emailMessage = "(Difficulty: Normal) \n"
                difficultyMenu = False
            else:
                print(Fore.RED + "\nInvalid Password\n\n"+ Fore.WHITE)
                continue

        elif(difficulty == "3"):
            emailMessage = "(Difficulty: Hard) \n"
            difficultyMenu = False

        elif(difficulty in ("4", "Exit", "EXIT", "exit", "e", "E", "Ex", "EX", "ex")):
            return

        else:
            print(Fore.RED + "Invalid Entry"+ Fore.WHITE)
            continue

    graderMenu = True
    while (graderMenu == True): # repeat forever unless it reaches "break" or "return"
        print("-" *44)
        grader = input("Select which module would you like to grade: \
                        \n\n (1) Grade Insecure Service Clients Lab \
                        \n\n (2) Grade User and Password Management Lab \
                        \n\n (3) Grade SSH Server Configuration Lab \
                        \n\n (4) Grade SMB Secure Configuration Lab \
                        \n\n (5) Grade All \
                        \n\nEnter 1, 2, 3, 4, or 5: ")

        print("\n\n")

        #HARD difficulty: gather email info before grading
        if (difficulty == "3"):
            #User input for student Name
            studentName = input("Your Full Name(s): ")
            #user input for where to email results
            emailRecipient = hardDifficultySubmit
            print("\n\n")

        if(grader == "1"):
            subject = "'s Insecure Service Clients Lab Grade"
            emailMessage = emailMessage + gradeServices(difficulty)
            graderMenu = False

        elif(grader == "2"):
            subject = "'s User and Password Management Lab Grade"
            emailMessage = emailMessage + gradeUsers(difficulty)
            graderMenu = False

        elif(grader == "3"):
            subject = "'s SSH Server Configuration Lab Grade"
            emailMessage = emailMessage + gradeSSH(difficulty)
            graderMenu = False

        elif(grader == "4"):
            subject = "'s SMB Secure Configuration Lab Grade"
            emailMessage = emailMessage + gradeSMB(difficulty)
            graderMenu = False

        elif(grader == "5"):
            subject = "'s Grade for All Insecure Linux Host Labs"
            emailMessage = emailMessage + gradeServices(difficulty)
            emailMessage = emailMessage + gradeUsers(difficulty)
            emailMessage = emailMessage + gradeSSH(difficulty)
            emailMessage = emailMessage + gradeSMB(difficulty)
            graderMenu = False

        else:
            print(Fore.RED + "Invalid Entry"+ Fore.WHITE)
            continue

        #EASY/NORMAL Difficulty: Ask if Student would like to submit/email results and Send if True
        if (difficulty == "1" or difficulty == "2"):
            emailMenu = True
            while (emailMenu == True): # repeat forever unless it reaches "break" or "return"
                print("\n" + "-" *41)
                studentSubmitResponse = input("Would you like to submit results? (Y/N): ")

                if(studentSubmitResponse in ("Y", "y", "YES", "Yes", "yes")):
                    #User input for student Name
                    studentName = input("Your Full Name(s): ")
                    #user input for where to email results
                    emailRecipient = input("Email To Send Results To: ")
                    #email subject
                    subject = studentName + subject
                    #send results to email
                    sendEmail(emailRecipient, subject, emailMessage)
                    return
                elif(studentSubmitResponse in ("N", "n", "NO", "No", "no")):
                    print("Exiting without Submitting...")
                    return
                else:
                    print(Fore.RED + "Invalid Entry"+ Fore.WHITE)
                    continue

        if (difficulty == "3"):
            #Auto send Results
            #email subject
            subject = studentName + subject
            #send results to email
            sendEmail(emailRecipient, subject, emailMessage)
            return


if __name__ == "__main__":
    main()
