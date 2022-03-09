#!/bin/sh
if [ -n "$1" ]; then
	# in most cases "/etc"
	sysconfdir="$1"
else
	sysconfdir='/etc'
fi

mv $sysconfdir/zshrc $sysconfdir/zsh/zshrc-default
mv $sysconfdir/skel/.zshrc $sysconfdir/zsh/skel-zshrc-default

mv $sysconfdir/zshrc-agdsn $sysconfdir/zshrc
mv $sysconfdir/skel/.zshrc-agdsn $sysconfdir/skel/.zshrc
