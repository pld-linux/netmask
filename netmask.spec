Summary:	Utility for determining network masks
Summary(pl):	Narz�dzie do wyznaczania maski sieci
Name:		netmask
Version: 	2.3.7
Release:	1
License: 	GPL v2
Group: 		Networking/Utilities
Source0: 	http://http.us.debian.org/debian/pool/main/n/netmask/%{name}_%{version}.tar.gz
# Source0-md5:	6e1b1c0694296bbe37ba8cb6a4902436
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a handy tool for generating terse netmasks in several common
formats. If you've ever maintained a firewall with more than a few
rules in it, you might use netmask to clean up and generalize sloppy
rules left by the netadmin before you. It will also convert netmasks
from one format to another for the day you change your firewall
software.

%description -l pl
Podr�czne narz�dzie do generowania zwi�z�ych masek sieci w kilku
popularnych formatach.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
makeinfo netmask.texi

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*