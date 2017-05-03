%define version 0.2
Summary: Battery monitor for Apple laptops
Name: wmbatppc
Version: %{version}
Release: 2 
Copyright: DMDZZ / GPL 
Group: X11/Utilities
Source: %name-%{version}.tar.gz
BuildRoot: %{_topdir}/BUILD/%name-%version
Prefix: /usr
Packager: Lou <titelou@free.fr>
Requires: pmud
Vendor: Lou <titelou@free.fr>

%description
A battery monitor for Apple G3 ibooks/powerbooks, using Linux PPC.
Designed for use as a docked app in WindowMaker or AfterStep, but works with all WM.
Does NOT work with older powerbooks than G3.
%prep
%setup
%build
make
%install
strip wmbatppc
echo $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
install -m 755 wmbatppc $RPM_BUILD_ROOT%{prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/man/man1
install -m 644 wmbatppc.1 $RPM_BUILD_ROOT%{prefix}/man/man1
%files
%defattr(-,root,root)
%doc COPYING README 
%{prefix}/bin/*
%{prefix}/man/man1/*

