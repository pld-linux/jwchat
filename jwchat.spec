# TODO:
# - webapp configuration for other httpd servers

Summary:	Web based jabber client
Summary(pl.UTF-8):	Webowy klient jabbera
Name:		jwchat
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/jwchat/jwchat-1.0.tar.gz
# Source0-md5:	8504585af4769895e17d1a2c9c092089
#Patch0:		%{name}-DESTDIR.patch
Source1:	%{name}-httpd.conf
URL:		http://blog.jwchat.org/jwchat/
Requires:       webapps
Requires:       webserver(access)
Requires:       webserver(alias)
Requires:       webserver(indexfile)
# Requires:	apache(mod_negotiation)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _sysconfdir     /etc/webapps/%{name}

%description
JWChat is a full featured, web-based Jabber client. Written using AJAX
technology it relies on JavaScript and HTML at the client-side only. It
supports basic
jabber instant messaging, roster management and groupchats based on the
MUC protocol.

%description -l pl.UTF-8
JWChat jest klientem jabbera działającym w pełni w przeglądarce. JWChat
komunikuje się z serwerem jabbera przez protokół XEP-0206 lub XEP-0025. Dzięki
temu może działać nawet jeżeli jedyna komunikacja z serwerem jest możliwa
poprzez http proxy.

%prep
%setup -q -c
mv %{name}-%{version}/{AUTHORS,ChangeLog,README,COPYING,config.js} .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir},%{_sysconfdir}}

cp -a %{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/jwchat
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install -p config.js $RPM_BUILD_ROOT%{_sysconfdir}/config.js
ln -s %{_sysconfdir}/webapps/%{name}/httpd.conf $RPM_BUILD_ROOT%{_datadir}/jwchat/config.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/jwchat
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config.js
