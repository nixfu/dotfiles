#!/bin/bash

# make sure playerctl is installed
if ! command -v playerctl &> /dev/null
then
        exit 0
fi

# if you want to filter out browsers
for player in $(playerctl -l |grep -v -e firefox -e chromium)
do 
	status=$(playerctl -p ${player} status)
	if [ "$status" == "Playing" ]; then
		playerctl -p ${player} next
	fi
done
