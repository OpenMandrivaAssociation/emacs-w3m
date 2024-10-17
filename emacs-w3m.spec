%define rname w3m
%define emacs_version 24.3
%define git 20120203

Summary:	An Emacs interface to w3m, a web browser and pager
Name:		emacs-%{rname}
Version:	1.5
Release:	0.%{git}.1
License:	GPLv2+
Group:		Networking/WWW
Url:		https://emacs-w3m.namazu.org/
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-autostart.el
BuildRequires:	emacs
Requires:	emacs
Requires:	w3m
Conflicts:	xemacs
Provides:	emacs-w3 = %{EVRD}
BuildArch:	noarch

%description
Emacs-w3m is a simple Emacs interface to w3m, which is a pager with WWW
capability. Although it is a pager, it can be used as a text-mode WWW browser.

%files
%doc README
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*el
%{_infodir}/*
%dir %attr(0755, root, root) %{_datadir}/emacs/site-lisp/%{rname}/
%{_datadir}/emacs/site-lisp/%{rname}/*elc
%{_datadir}/emacs/site-lisp/%{rname}/mew-%{rname}.el
%{_datadir}/emacs/site-lisp/%{rname}/mime-%{rname}.el
%{_datadir}/emacs/site-lisp/%{rname}/octet.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-load.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-ucs.el
%{_datadir}/emacs/%{emacs_version}/etc/images/w3m/

#----------------------------------------------------------------------------

%package el
Summary:	Web Browser sources for GNU Emacs
Group:		Editors
Url:		https://www.cs.indiana.edu/elisp/w3/
Requires:	%{name} = %{EVRD}

%description el
Emacs-w3m is a simple Emacs interface to w3m, which is a pager with WWW
capability. Although it is a pager, it can be used as a text-mode WWW browser.

This is the elisp source.

%files el
%doc ChangeLog
%dir %attr(0755, root, root) %{_datadir}/emacs/site-lisp/%{rname}/
%{_datadir}/emacs/site-lisp/%{rname}/ChangeLog
%{_datadir}/emacs/site-lisp/%{rname}/ChangeLog.1
%{_datadir}/emacs/site-lisp/%{rname}/bookmark-w3m.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-antenna.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-bookmark.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-bug.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-ccl.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-cookie.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-dtree.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-ems.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-favicon.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-fb.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-filter.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-form.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-hist.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-image.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-lnum.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-mail.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-namazu.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-perldoc.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-proc.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-rss.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-search.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-session.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-symbol.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-tabmenu.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-util.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}-weather.el
%{_datadir}/emacs/site-lisp/%{rname}/%{rname}.el

#----------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -fi
./configure --with-emacs=emacs --libdir=%{_libdir}

make

%install
mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d/
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/emacs/site-start.d/%{rname}.el

make install \
     infodir=%{buildroot}%{_infodir} \
     lispdir=%{buildroot}%{_datadir}/emacs/site-lisp/%{rname}

make install-icons \
     ICONDIR=%{buildroot}%{_datadir}/emacs/%{emacs_version}/etc/images/%{rname}

