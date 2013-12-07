%define Werror_cflags %nil

Summary:        TCP/IP Network Monitor
Name:           iptraf-ng
Version:        1.1.4
Release:        3
License:        GPLv2
Group:          System/Configuration/Networking
Url:            https://fedorahosted.org/iptraf-ng
Source0:	https://fedorahosted.org/releases/i/p/iptraf-ng/%{name}-%{version}.tar.gz
BuildRequires:  xz
BuildRequires:  kernel-headers
BuildRequires:  pkgconfig(ncurses)
Obsoletes:	iptraf

%description
IPTraf-ng is a console-based network statistics utility. It gathers a
variety of information such as TCP connection packet and byte counts,
interface statistics and activity indicators, TCP/UDP traffic
breakdowns, and LAN station packet and byte counts.

%prep
%setup -q
%apply_patches

%build
if [ ! -e configure ]; then
	./autogen.sh;
fi;
sed -i 's/lpanel/lpanelw/g' Makefile
%configure2_5x
%make

%install
%makeinstall_std
install -d -m 0755 %{buildroot}/var/lib/iptraf-ng

%files
%{_sbindir}/*
%{_mandir}/man*/*
/var/lib/iptraf-ng

