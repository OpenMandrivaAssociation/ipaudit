Name:           ipaudit
Version:        1.0rc9
Release:        2
Epoch:          0
Summary:        Network Package Audit and Capture
License:        GPLv2
Group:          Networking/Other
URL:            https://%{name}.sourceforge.net/
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


%changelog
* Wed Feb 10 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:1.0rc9-1mdv2010.1
+ Revision: 504010
- Update to 1.0rc9
- Fix spec
- Fix build
- Fix Licence

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0:1.0-0.beta2.4mdv2009.1
+ Revision: 298259
- rebuilt against libpcap-1.0.0

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0:1.0-0.beta2.3mdv2008.1
+ Revision: 140776
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 08 2007 David Walluck <walluck@mandriva.org> 0:1.0-0.beta2.3mdv2008.0
+ Revision: 49716
- spec cleanup


* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.beta2.2mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Tue Jul 05 2005 Lenny Cartier <lenny@mandriva.com> 1.0-0.beta2.1mdk
- 1.0beta2

* Mon May 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.95-5mdk
- rebuild

* Wed Apr 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.95-4mdk
- buildrequires

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.95-3mdk
- rebuild
- patch0: add missing includes

* Wed Aug 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.95-2mdk
- rebuild

* Mon Jul 30 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.95-1mdk
- updated to 0.95

* Fri Jan 12 2001 Lenny Cartier <lenny@mandrakesoft.com>  0.92-1mdk
- updated to 0.92

* Thu Sep 07 2000 Lenny Cartier <lenny@mandrakesoft.com>  0.91.1-3mdk
- clean spec

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.91.1-2mdk
- enable it to build with spechelper
- fix group
- BM

* Fri May 19 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.91.1-1mdk
- created spec file and compiled for Mandrake

