# TODO:
# - incorrectly installs itself to perl_vendorarch, but only constants.pl should go there
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AnyEvent
%define		pnam	AnyEvent
Summary:	AnyEvent - provide framework for multiple event loops
Summary(pl.UTF-8):	AnyEvent - szkielet dla wielu pętli zdarzeń
Name:		perl-AnyEvent
Version:	5.31
Release:	3
Epoch:		3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	9c13447a7117e06e7a2fd553c4b2228c
URL:		http://search.cpan.org/dist/AnyEvent/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Suggests:	%{name}-Impl-EV
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AnyEvent extension aims to provide an simple and optimized event
loop for a broad class of applications.

%description -l pl.UTF-8
Rozszerzenie AnyEvent ma za zadanie udostępnić pojedynczą i
zoptymalizowaną pętlę zdarzeń dla szerokiej gamy aplikacji.

%package Impl-Cocoa
Summary:	AnyEvent implementation based on Cocoa::EventLoop
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Cocoa
AnyEvent implementation based on Cocoa::EventLoop..

%package Impl-EV
Summary:	AnyEvent implementation based on libev
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-EV
AnyEvent implementation based on libev (best choice).

%package Impl-Event
Summary:	AnyEvent implementation based on Event
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Event
AnyEvent implementation based on Event (very stable, few glitches).

%package Impl-EventLib
Summary:	AnyEvent implementation based on EventLib
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-EventLib
AnyEvent implementation based on EventLib (leaks memory and worse).

%package Impl-Glib
Summary:	AnyEvent implementation based on Glib
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Glib
AnyEvent implementation based on Glib (slow but very stable).

%package Impl-IOAsync
Summary:	AnyEvent implementation based on IOAsync
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-IOAsync
AnyEvent implementation based on IO::Async.

%package Impl-Irssi
Summary:	AnyEvent implementation for Irssi
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Irssi
AnyEvent implementation used when running within irssi.

%package Impl-POE
Summary:	AnyEvent implementation based on POE
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-POE
AnyEvent implementation based on POE (very slow, some limitations).

%package Impl-Qt
Summary:	AnyEvent implementation based on Qt
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Qt
AnyEvent implementation based on Qt.

%package Impl-Tk
Summary:	AnyEvent implementation based on Tk
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Tk
AnyEvent implementation based on Tk (very broken).

%prep
%setup -q -n %{pnam}-%{version}
# we are not allowed to use network while building package
%{__rm} t/05_dns.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/AnyEvent.pm
%dir %{perl_vendorarch}/AnyEvent
%{perl_vendorarch}/AnyEvent/*.pm
%dir %{perl_vendorarch}/AnyEvent/Impl
# pureperl implementation, works everywhere, requires nothing
%{perl_vendorarch}/AnyEvent/Impl/Perl.pm
%{perl_vendorarch}/AnyEvent/Util
%{perl_vendorarch}/AnyEvent/FAQ.pod
%{perl_vendorarch}/AnyEvent/Intro.pod
%{perl_vendorarch}/AnyEvent/constants.pl
%{perl_vendorarch}/AE.pm
%{_mandir}/man3/AE.3pm*
%{_mandir}/man3/AnyEvent.3pm*
%{_mandir}/man3/AnyEvent::[DFHSTU]*.3pm*
%{_mandir}/man3/AnyEvent::Intro.3pm*
%{_mandir}/man3/AnyEvent::Impl::Perl.3pm*

%files Impl-Cocoa
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/Cocoa.pm
%{_mandir}/man3/AnyEvent::Impl::Cocoa.3pm*

%files Impl-EV
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/EV.pm
%{_mandir}/man3/AnyEvent::Impl::EV.3pm*

%files Impl-Event
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/Event.pm
%{_mandir}/man3/AnyEvent::Impl::Event.3pm*

%files Impl-EventLib
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/EventLib.pm
%{_mandir}/man3/AnyEvent::Impl::EventLib.3pm*

%files Impl-Glib
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/Glib.pm
%{_mandir}/man3/AnyEvent::Impl::Glib.3pm*

%files Impl-IOAsync
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/IOAsync.pm
%{_mandir}/man3/AnyEvent::Impl::IOAsync.3pm*

%files Impl-Irssi
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/Irssi.pm
%{_mandir}/man3/AnyEvent::Impl::Irssi.3pm*

%files Impl-POE
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/POE.pm
%{_mandir}/man3/AnyEvent::Impl::POE.3pm*

%files Impl-Qt
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/Qt.pm
%{_mandir}/man3/AnyEvent::Impl::Qt.3pm*

%files Impl-Tk
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/Tk.pm
%{_mandir}/man3/AnyEvent::Impl::Tk.3pm*
