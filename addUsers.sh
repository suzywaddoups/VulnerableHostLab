#!/bin/bash
#Script to add users/groups to Linux System

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

  #checks if the group exists, if not then creates it
  for group in ${groups[*]}
  do
    groupadd "$group"
  done

  #creates the user accounts, adds them to groups, and sets passwords
  x=0
  created=0
  for user in ${usernames[*]}
  do
    useradd -c ${fullnames[$x]} -g ${groups[$x]} -p $(openssl passwd -1 ${userid[$x]}) -m $user
    echo ${fullnames[$x]}
    let created=$created+1
    x=$x+1
  done
  echo " "
  echo "Complete. $created accounts have been created."
fi
