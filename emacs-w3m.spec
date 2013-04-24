%define rname w3m
%define version 1.4.4
%define release %mkrel 8
%define e21_version 21.4

Summary:	An Emacs interface to w3m, a web browser and pager
Name:		emacs-%{rname}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-autostart.el
License:	GPLv2+
Group:		Networking/WWW
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	emacs >= %{e21_version}
Requires:	w3m
BuildRequires:	emacs-bin >= %{e21_version}
URL:		http://emacs-w3m.namazu.org/
Conflicts:	xemacs
Obsoletes:	emacs-w3
Provides:	emacs-w3
BuildArch:	noarch

%description
Emacs-w3m is a simple Emacs interface to w3m, which is a pager with
WWW capability.
Although it is a pager, it can be used as a text-mode WWW browser.

%package el
Summary: Web Browser sources for GNU Emacs
Group: Editors
Requires: %{name} = %{version}
URL: http://www.cs.indiana.edu/elisp/w3/

%description el
Emacs-w3m is a simple Emacs interface to w3m, which is a pager with
WWW capability.
Although it is a pager, it can be used as a text-mode WWW browser.

This is the elisp source.

%prep
%setup -q

%build
./configure --with-emacs=emacs --libdir=%{_libdir}

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d/
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/emacs/site-start.d/%{rname}.el

make install \
     infodir=%{buildroot}%{_infodir} \
     lispdir=%{buildroot}%{_datadir}/emacs/site-lisp/%{rname}

make install-icons \
     ICONDIR=%{buildroot}%{_datadir}/emacs/%{e21_version}/etc/images/%{rname}

%clean
rm -rf %{buildroot}


%postun
%_remove_install_info %{rname}

%files
%defattr(-,root,root)
%doc README
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*el
%{_infodir}/*
%dir %attr(0755, root, root) %{_datadir}/emacs/site-lisp/%{rname}/
%{_datadir}/emacs/site-lisp/%{rname}/*elc
%{_datadir}/emacs/site-lisp/%{rname}/mew-%{rname}.el
%{_datadir}/emacs/site-lisp/%{rname}/mime-%{rname}.el
%{_datadir}/emacs/site-lisp/%{rname}/octet.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-bitmap.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-e19.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-e20.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-load.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-om.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-ucs.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-xmas.el
%{_datadir}/emacs/%{e21_version}/etc/images/w3m/

%files el
%defattr(-,root,root)
%doc ChangeLog
%dir %attr(0755, root, root) %{_datadir}/emacs/site-lisp/%{rname}/
%{_datadir}/emacs/site-lisp/%{rname}/ChangeLog
%{_datadir}/emacs/site-lisp/%{rname}/ChangeLog.1
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-antenna.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-bookmark.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-bug.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-ccl.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-cookie.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-dtree.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-e21.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-favicon.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-filter.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-form.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-fsf.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-hist.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-image.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-lnum.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-namazu.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-perldoc.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-proc.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-rss.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-search.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-symbol.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-tabmenu.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-util.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-weather.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}.el



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.4-8mdv2011.0
+ Revision: 618054
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.4.4-7mdv2010.0
+ Revision: 428589
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.4.4-6mdv2009.0
+ Revision: 244779
- rebuild

* Wed Feb 06 2008 Olivier Blin <oblin@mandriva.com> 1.4.4-4mdv2008.1
+ Revision: 163014
- require w3m-load only, not the whole w3m

* Wed Feb 06 2008 Adam Williamson <awilliamson@mandriva.org> 1.4.4-3mdv2008.1
+ Revision: 162933
- obsoletes and provides emacs-w3 (acts as a replacement in most ways, and no-one seems to want to maintain emacs-w3)
- adjust autostart.el to fix loading on emacs start (I think...)
- spec clean

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4.4-2mdv2008.1
+ Revision: 136403
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import emacs-w3m


* Thu Jul 20 2006 Olivier Blin <blino@mandriva.com> 1.4.4-2mdv2007.0
- rebuild (emacs-w3m failed to start for an unknown reason)

* Sat Apr 22 2006 Olivier Blin <oblin@mandriva.com> 1.4.4-1mdk
- initial release
