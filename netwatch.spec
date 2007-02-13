Summary:	Ethernet/PPP IP Packet Monitor
Summary(pl.UTF-8):	Monitor pakietów IP dla Ethernet/PPP
Name:		netwatch
Version:	1.0a
Release:	2
License:	GPL
Vendor:		Gordon MacKay Consulting
Group:		Applications/Networking
#Source0Download:	http://www.slctech.org/~mackay/netwatch.htm
Source0:	http://www.slctech.org/~mackay/%{name}-%{version}.src.tgz
# Source0-md5:	0d9bbfe6930e058ea6c5eb9bacffdb77
Patch0:		%{name}-CLK_TCK.patch
Patch1:		%{name}-Makefile.patch
URL:		http://www.slctech.org/~mackay/netwatch.html
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The software enables real-time viewing of network activity. Network
usage is tracked on a per host basis. Packet and byte counts are
available for all host communication. Router statistics and summary
charts are available.

%description -l pl.UTF-8
Oprogramowanie umożliwia oglądanie działalności w sieci na żywo.
Wydajność sieci jest śledzona w oparciu o hosty. Liczniki pakietów i
bajtów są dostępne dla wszystkich połączeń. Dostępne są statystyki
routera i podsumowania.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%doc README README.performance TODO CHANGES BUGS netwatch-%{version}.lsm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT
