Summary:	Ethernet/PPP IP Packet Monitor 
Summary(pl):	Monitor pakietów IP dla Ethernet/PPP
Name:		netwatch 
Version:	1.0a 
Release:	1 
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.slctech.org/pub/%{name}-%{version}.src.tgz
URL:		http://www.slctech.org/~mackay/netwatch.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Vendor:		Gordon MacKay Consulting 

%description 
The software enables real-time viewing of network activity. Network
usage is tracked on a per host basis. Packet and byte counts are
available for all host communication. Router statistics and summary
charts are available.

%description -l pl
Oprogramowanie umo¿liwia ogl±danie dzia³alno¶ci w sieæi na ¿ywo.
Wydajno¶æ sieci jest ¶ledzona w oparciu o hosty. Liczniki pakietów i
bajtów s± dostêpne dla wszystkich po³±czeñ. Dostêpne s± statystyki
routera i podsumowania

%prep
%setup -q

%build
cd $RPM_BUILD_DIR/netwatch-1.0a
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_DIR/netwatch-1.0a
%{__make} install

%files
%defattr(644,root,root,755)
%doc README
%doc README.performance
%doc TODO
%doc COPYING
%doc CHANGES
%doc BUGS
%doc netwatch.1.0a.lsm
%attr(755,root,root) %{_bindir}/netwatch
%attr(755,root,root) %{_bindir}/netresolv
%{_prefix}/man/man1/netwatch.1


%clean
rm -rf $RPM_BUILD_ROOT
