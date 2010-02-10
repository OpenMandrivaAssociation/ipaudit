Name:           ipaudit
Version:        1.0rc9
Release:        %mkrel 1
Epoch:          0
Summary:        Network Package Audit and Capture
License:        GPLv2
Group:          Networking/Other
URL:            http://%{name}.sourceforge.net/
Source0:        http://superb-east.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A neat packet logging program and auditor. Provides dump capability
and various  levels of logging.


%prep
%setup -q  -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL README
%attr(0755,root,root) %{_bindir}/total
%attr(0755,root,root) %{_sbindir}/ipaudit
%attr(0755,root,root) %{_sbindir}/ipstrings
%{_mandir}/man8/ipaudit.8.*
%{_mandir}/man8/ipstrings.8.*
%{_mandir}/man1/total.1.*
