#!/bin/bash

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
    if groups $user | grep -q ${groups[$x]} &> /dev/null
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
