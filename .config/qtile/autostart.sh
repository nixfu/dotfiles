#!/bin/bash 
#volumeicon &
#nm-applet &
spotifyd --no-daemon &
picom --experimental-backends &
feh --bg-fill --randomize ~/.wallpaper/* &
xscreensaver -no-splash &
conky -c ~/.config/conky/qtile.conkyrc &
steam -silent &
telegram-desktop -startintray &
discord --start-minimized &
