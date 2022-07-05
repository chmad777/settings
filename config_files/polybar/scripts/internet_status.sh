#!/bin/sh

eth=$(ifconfig eth0 | grep "netmask" | awk '{print $2}')

if [ $(ifconfig wlan0 | grep "netmask" | awk '{print $2}') ]; then
 wlan=$(ifconfig wlan0 | grep "netmask" | awk '{print $2}')
fi

if [ $wlan ]; then
 echo "%{F#ffffff} %{F#b1e3ff}$wlan%{u-}"
elif [ $eth ]; then
 echo "%{F#ffffff} %{F#b1e3ff}$eth%{u-}" 
else
 echo "Not connected"
fi
