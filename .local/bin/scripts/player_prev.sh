#!/bin/bash

# if you want to filter out browsers
for player in $(playerctl -l |grep -v -e firefox -e chromium)
do 
	status=$(playerctl -p ${player} status)
	if [ "$status" == "Playing" ]; then
		playerctl -p ${player} previous
	fi
done
