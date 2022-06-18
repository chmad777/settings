#!/bin/sh

if [ $target ]; then
    echo "%{F#e51d0b}什%{F#b1e3ff} $target%{u-}"
else
    echo "%{F#e51d0b}ﲅ %{u-}%{F#b1e3ff} No target"
fi
