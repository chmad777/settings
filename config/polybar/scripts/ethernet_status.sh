#!/bin/sh

eth=$(ifconfig eth0 | grep "netmask" | awk '{print $2}')
wlan=$(ifconfig wlan0 | grep "netmask" | awk '{print $2}')

if [ $eth ]; then
 echo "%{F#ffffff} {F#b1e3ff}$eth%{u-}" 
elif [ $wlan ]; then
 echo "%{F#ffffff} {F#b1e3ff}$wlan%{u-}"
else
 echo "Not connected"
fi
