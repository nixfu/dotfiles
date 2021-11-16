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
		OLDIFS="$IFS"
		data=$(playerctl -p ${player} -f "{{position}}+{{mpris:length}}+{{artist}}+{{title}}" metadata)
		IFS="+" read -ra myarray <<< "$data"
		IFS="$OLDIFS"
		pos=${myarray[0]}
		len=${myarray[1]}
		if [ -n "$len" ]; then
			pct=$((100*pos/len))
			mypct="(${pct}%)"
		fi
		artist=${myarray[2]}
		title=${myarray[3]}
		echo -n "${artist} - ${title} ${mypct}"
	fi
done
