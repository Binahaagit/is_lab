#!/bin/bash

echo "Enter username:"
read user

while true
do
    if who | grep -w "$user" >/dev/null
    then
        echo "User "$user" has logged in."
        break
    else
        echo "User not logged in. Checking again in 30s..."
        sleep 30
    fi
done