Name: agdsn-zsh-config
Version: 0.6.0
Release: 1%{?dist}
BuildArch: noarch
Summary: AG DSN Zsh Config for RPM based Linux distributions
License: GPLv2

Requires: zsh

Enhances: zsh, systemd, iproute, git

%description
A modified version of the Grml Zsh configuration
specialised for the needs of system administration and developed for the
residential network Arbeitsgemeinschaft Dresdner Studentennetz (AG DSN).

%install
install -d -m 0755 %{buildroot}%{_sysconfdir}/zsh
install -d -m 0755 %{buildroot}%{_sysconfdir}/skel
install -d -m 0755 %{buildroot}%{_sysconfdir}/profile.d
install -p -m 0644 %(pwd)/zshrc-base-hw.zsh %{buildroot}%{_sysconfdir}/zshrc-agdsn
install -p -m 0644 %(pwd)/zshrc-home.zsh %{buildroot}%{_sysconfdir}/skel/.zshrc-agdsn
install -p -m 0644 %(pwd)/zshrc-home.zsh %{buildroot}%{_sysconfdir}/zsh/newuser.zshrc.recommended
install -p -m 0644 %(pwd)/profile-d-agdsn-zsh-config.sh %{buildroot}%{_sysconfdir}/profile.d/agdsn-zsh-config.sh
# The dirty hack files
install -p -m 0644 %(pwd)/rpm/install-agdsn-zshrc.sh %{buildroot}%{_sysconfdir}/install-agdsn-zshrc.sh
install -p -m 0644 %(pwd)/rpm/uninstall-agdsn-zshrc.sh %{buildroot}%{_sysconfdir}/uninstall-agdsn-zshrc.sh

# This dirty hack with the *agsdn-zshrc.sh files is needed
# because the redhat version of update-alternatives does not have a '--force' option.
# This backups/moves the default /etc/zshrc and /etc/skel/.zshrc into /etc/zsh/
# and moves /etc/zshrc-agdsn and /etc/skel/.zshrc-agdsn to their intended places.
%post
/bin/sh %{_sysconfdir}/install-agdsn-zshrc.sh %{_sysconfdir}

# This script undoes the changes made above.
%preun
/bin/sh %{_sysconfdir}/uninstall-agdsn-zshrc.sh %{_sysconfdir}

%files
%ghost %{_sysconfdir}/zsh/zshrc-default
%ghost %{_sysconfdir}/zsh/skel-zshrc-default

%config %{_sysconfdir}/zshrc-agdsn
%config %{_sysconfdir}/skel/.zshrc-agdsn
%config %{_sysconfdir}/zsh/newuser.zshrc.recommended
%config %{_sysconfdir}/profile.d/agdsn-zsh-config.sh

%{_sysconfdir}/install-agdsn-zshrc.sh
%{_sysconfdir}/uninstall-agdsn-zshrc.sh
