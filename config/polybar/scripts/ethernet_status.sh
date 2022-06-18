#!/bin/sh
 
echo "%{F#b1e3ff}$(/usr/sbin/ifconfig wlan0 | grep "inet " | awk '{print $2}')%{u-}"
