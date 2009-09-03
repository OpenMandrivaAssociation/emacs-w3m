%define rname w3m
%define version 1.4.4
%define release %mkrel 7
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

%post
%_install_info %{rname}.info

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

