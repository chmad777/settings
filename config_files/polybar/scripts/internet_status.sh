#!/bin/sh

eth=$(ifconfig eth0 | grep "netmask" | awk '{print $2}')

if [ ${ifconfig | grep "wlan") ]; then
wlan=$(ifconfig wlan0 | grep "netmask" | awk '{print $2}')
fi

if [ $eth ]; then
 echo "%{F#ffffff} %{F#b1e3ff}$eth%{u-}" 
elif [ $wlan ]; then
 echo "%{F#ffffff} %{F#b1e3ff}$wlan%{u-}"
else
 echo "Not connected"
fi
