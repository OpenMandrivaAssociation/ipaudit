%define name ipaudit
%define version 1.0
%define release 0.beta2.2mdk


Name: %{name}
Summary: Network Package Audit and Capture
Version: %{version}
Release: %{release}
Source: %name-%{version}BETA2.tar.bz2
Group: Networking/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
Buildrequires: libpcap-devel
License: GPL
URL: http://www.sp.uconn.edu/~jrifkin/ipaudit/

%description
A neat packet logging program and auditor. Provides
dump capability and various levels of logging.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q  -n %name-%{version}BETA2


%build

%configure

make CFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="-DNDEBUG" CXXFLAGS="$RPM_OPT_FLAGS -DNO_DEBUG"

%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr (-,root,root)
%doc README ChangeLog COPYING INSTALL AUTHORS
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*

