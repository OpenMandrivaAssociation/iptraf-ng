%define Werror_cflags %nil

Name:           iptraf-ng
Version:        1.1.3.1
Release:        1
Summary:        TCP/IP Network Monitor
License:        GPLv2
Group:          System/Configuration/Networking
Url:            https://fedorahosted.org/iptraf-ng
Source0:	https://fedorahosted.org/releases/i/p/iptraf-ng/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  ncurses-devel
BuildRequires:  xz
BuildRequires:  kernel-headers
Patch0:		iptraf-ng-1.1.3.1-kernel-v3.5-kill-off-token-ring-support.patch
Obsoletes:	iptraf


%description
IPTraf-ng is a console-based network statistics utility. It gathers a
variety of information such as TCP connection packet and byte counts,
interface statistics and activity indicators, TCP/UDP traffic
breakdowns, and LAN station packet and byte counts.

%prep
%setup -q
%patch0 -p1

%build
if [ ! -e configure ]; then
	./autogen.sh;
fi;
%configure2_5x
%make

%install
%makeinstall_std
install -d -m 0755 %{buildroot}/var/lib/iptraf-ng

%files
%_sbindir/*
%_mandir/man*/*
/var/lib/iptraf-ng
