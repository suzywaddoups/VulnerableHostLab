#!/bin/bash
#Script to delete users from Linux System

#BASIC
#user1 = "ldelaney"
#password1 = "ldelaney"
#useradd -p $(openssl passwd -1 $password1) -c Louise Delaney -m $user1

read -p "User CSV File Path: " filein
# filein="users.csv"
IFS=$'\n'

if [ ! -f "$filein" ]
then
  echo "Cannot find file $filein"
else

  #create arrays of groups, full names, and usernames
  groups=(`cut -d: -f 3 "$filein" | sed 's/ //'`)
  fullnames=(`cut -d: -f 1 "$filein"`)
  userid=(`cut -d: -f 2 "$filein"`)
  usernames=(`cut -d: -f 2 "$filein"`)

  #deletes the user accounts, removes them from group
  for user in ${usernames[*]}
  do
    deluser --remove-home $user
  done
fi
