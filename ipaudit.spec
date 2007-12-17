Name:           ipaudit
Version:        1.0
Release:        %mkrel 0.beta2.3
Epoch:          0
Summary:        Network Package Audit and Capture
License:        GPL
Group:          Networking/Other
URL:            http://ipaudit.sourceforge.net/
Source0:        http://superb-east.dl.sourceforge.net/sourceforge/ipaudit/ipaudit-1.0BETA2.tar.gz
BuildRequires:  libpcap-devel

%description
A neat packet logging program and auditor. Provides dump capability
and various  levels of logging.


%prep
%setup -q  -n %{name}-%{version}BETA2

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall}

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL README
%attr(0755,root,root) %{_bindir}/total
%attr(0755,root,root) %{_sbindir}/ipaudit
%attr(0755,root,root) %{_sbindir}/ipstrings
%{_mandir}/man1/ipaudit.1*
%{_mandir}/man1/ipstrings.1*
%{_mandir}/man1/total.1*
