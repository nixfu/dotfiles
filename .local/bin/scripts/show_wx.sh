#!/bin/bash
LOC=$1
curl http://wttr.in/${LOC}?QF
read -n 1 -s -r -p "Press any key to continue"
exit
