#!/bin/sh

install -d ~/.racer
ln -sf /usr/X11R6/share/racer/data ~/.racer
for f in /usr/X11R6/share/racer/*.ini ; do
	[ -f ~/.racer/`basename $f` ] || cp $f ~/.racer
done

cd ~/.racer && exec /usr/X11R6/bin/racer.bin
