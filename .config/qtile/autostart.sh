#!/bin/bash 

cmd_exist() { unalias "$1" >/dev/null 2>&1 ; command -v "$1" >/dev/null 2>&1 ;}
__kill() { kill -9 "$(pidof "$1")" >/dev/null 2>&1 ; }
__start() { sleep 1 && "$@" >/dev/null 2>&1 & }
__running() { pidof "$1" >/dev/null 2>&1 ;}

# for spt cli player
if cmd_exist spotifyd ; then
    __start spotifyd --no-daemon
fi

# I use jonaburg picom fork that has rounded corners
if cmd_exist picom ; then
    __kill picom
    __start picom --experimental-backends
fi

if cmd_exist feh ; then
    feh --bg-fill --randomize ~/.wallpaper/* 
fi

if cmd_exist xscreensaver ; then
    __kill xscreensaver
    __start xscreensaver -no-splash
fi

if cmd_exist conky ; then
    __kill conky
    __start conky -c ~/.config/conky/qtile.conkyrc
fi

if cmd_exist steam ; then
    __kill steam
    __start steam -silent
fi

# use 'hide rhythmbox on start' plugin to auto send to systray on startup
if cmd_exist rhythmbox ; then
    __kill rhythmbox
    __start rhythmbox
fi

#if cmd_exist telegram-desktop ; then
#    __kill telegram-deskop
#    __start telegram-desktop -startintray
#fi

if cmd_exist steam ; then
    __kill discord
    __start discord --start-minimized
fi

if [ -f /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 ]; then
	    __kill polkit-gnome-authentication-agent-1
	        __start /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
fi

#volumeicon &
#nm-applet &
#spotifyd --no-daemon &
#picom --experimental-backends &
#feh --bg-fill --randomize ~/.wallpaper/* &
#xscreensaver -no-splash &
#conky -c ~/.config/conky/qtile.conkyrc &
#steam -silent &
#telegram-desktop -startintray &
#discord --start-minimized &
