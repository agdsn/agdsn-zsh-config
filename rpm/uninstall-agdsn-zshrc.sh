#!/bin/sh
if [ -n "$1" ]; then
    # in most cases "/etc"
    sysconfdir="$1"
else
    sysconfdir='/etc'
fi

mv $sysconfdir/zshrc $sysconfdir/zshrc-agdsn
mv $sysconfdir/skel/.zshrc $sysconfdir/skel/.zshrc-agdsn

mv $sysconfdir/zsh/zshrc-default $sysconfdir/zshrc
mv $sysconfdir/zsh/skel-zshrc-default $sysconfdir/skel/.zshrc
