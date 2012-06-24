Summary: Ethernet/PPP IP Packet Monitor 
Summary(pl): Monitor pakiet�w IP dla Ethernet/PPP
Name: netwatch 
Version: 1.0a 
Release: 1 
Copyright: GPL 
Group: System/Network
Group(pl): System/Sie� 
Source: ftp://ftp.slctech.org/pub/%{name}-%{version}.src.tgz 
URL: http://www.slctech.org/~mackay/netwatch.html
BuildRoot: /tmp/%{name}-%{version}-root
Vendor: Gordon MacKay Consulting 

%description 
The software enables real-time viewing of network activity.
Network usage is tracked on a per host basis. Packet
and byte counts are available for all host communication.
Router statistics and summary charts are available.
 
%description -l pl
Oprogramowanie umo�liwia ogl�danie dzia�alno�ci w sie�i na �ywo. Wydajno��
sieci jest �ledzona w oparciu o hosty. Liczniki pakiet�w i bajt�w s�
dost�pne dla wszystkich po��cze�. Dost�pne s� statystyki routera i
podsumowania

%prep
%setup -q

%build
cd $RPM_BUILD_DIR/netwatch-1.0a
./configure
make

%install
cd $RPM_BUILD_DIR/netwatch-1.0a
make install

%files
%doc README
%doc README.performance
%doc TODO
%doc COPYING
%doc CHANGES
%doc BUGS
%doc netwatch.1.0a.lsm
/usr/bin/netwatch
/usr/bin/netresolv
/usr/man/man1/netwatch.1
