Summary:	Ethernet/PPP IP Packet Monitor
Summary(pl):	Monitor pakietów IP dla Ethernet/PPP
Name:		netwatch
Version:	1.0a
Release:	1
License:	GPL
Vendor:		Gordon MacKay Consulting
Group:		Applications/Networking
Source0:	ftp://ftp.slctech.org/pub/%{name}-%{version}.src.tgz
Patch0:		%{name}-CLK_TCK.patch
Patch1:		%{name}-Makefile.patch
URL:		http://www.slctech.org/~mackay/netwatch.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The software enables real-time viewing of network activity. Network
usage is tracked on a per host basis. Packet and byte counts are
available for all host communication. Router statistics and summary
charts are available.

%description -l pl
Oprogramowanie umo¿liwia ogl±danie dzia³alno¶ci w sieci na ¿ywo.
Wydajno¶æ sieci jest ¶ledzona w oparciu o hosty. Liczniki pakietów i
bajtów s± dostêpne dla wszystkich po³±czeñ. Dostêpne s± statystyki
routera i podsumowania

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%doc README README.performance TODO CHANGES BUGS netwatch-%{version}.lsm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT
