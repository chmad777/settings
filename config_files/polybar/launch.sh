#!/usr/bin/env sh

## Add this to your wm startup file.

# Terminate already running bar instances
killall -q polybar

## Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

## Launch

## Left bar
polybar logo -c ~/.config/polybar/current.ini &
polybar date -c ~/.config/polybar/current.ini &
polybar ip -c ~/.config/polybar/current.ini &
polybar web -c ~/.config/polybar/current.ini &
polybar files -c ~/.config/polybar/current.ini &


## Right bar
polybar power_off -c ~/.config/polybar/current.ini &
polybar battery -c ~/.config/polybar/current.ini &
polybar audio -c ~/.config/polybar/current.ini &
polybar HTB  -c ~/.config/polybar/current.ini &
polybar target  -c ~/.config/polybar/current.ini &


## Center bar
polybar workspaces -c ~/.config/polybar/workspace.ini &
#polybar dir -c ~/.config/polybar/workspace.ini &
