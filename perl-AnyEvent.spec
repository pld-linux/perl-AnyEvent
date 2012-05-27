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
Version:	7.01
Release:	1
Epoch:		3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	f26c1d03d7f5fe7d82e6885e5887bf8f
URL:		http://search.cpan.org/dist/AnyEvent/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Suggests:	%{name}-Impl-EV
Obsoletes:	perl-AnyEvent-Impl-Cocoa
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# disable debuginfo, nothing special there
%define		_enable_debug_packages	0

%description
The AnyEvent extension aims to provide an simple and optimized event
loop for a broad class of applications.

%description -l pl.UTF-8
Rozszerzenie AnyEvent ma za zadanie udostępnić pojedynczą i
zoptymalizowaną pętlę zdarzeń dla szerokiej gamy aplikacji.

%package Impl-EV
Summary:	AnyEvent implementation based on libev
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na libev
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-EV
AnyEvent implementation based on libev (best choice).

%description Impl-EV -l pl.UTF-8
Implementacja AnyEvent oparta na libev (najlepszy wybór).

%package Impl-Event
Summary:	AnyEvent implementation based on Event
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na module Event
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Event
AnyEvent implementation based on Event (very stable, few glitches).

%description Impl-Event -l pl.UTF-8
Implementacja AnyEvent oparta na module Event (stabilna, z kilkoma
problemami).

%package Impl-EventLib
Summary:	AnyEvent implementation based on Event::Lib
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na module Event::Lib
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-EventLib
AnyEvent implementation based on Event::Lib (leaks memory and worse).

%description Impl-EventLib -l pl.UTF-8
Implementacja AnyEvent oparta na module Event::Lib (ma wycieki pamięci
i jeszcze gorzej).

%package Impl-FLTK
Summary:	AnyEvent implementation based on FLTK
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na FLTK
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-FLTK
AnyEvent implementation based on FLTK (fltk 2 binding).

%description Impl-FLTK -l pl.UTF-8
Implementacja AnyEvent oparta na FLTK (wiązania fltk 2).

%package Impl-Glib
Summary:	AnyEvent implementation based on GLib
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na GLibie
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Glib
AnyEvent implementation based on GLib (slow but very stable).

%description Impl-Glib -l pl.UTF-8
Implementacja AnyEvent oparta na GLibie (wolna, ale stabilna).

%package Impl-IOAsync
Summary:	AnyEvent implementation based on IO::Async
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na module IO::Async
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-IOAsync
AnyEvent implementation based on IO::Async.

%description Impl-IOAsync -l pl.UTF-8
Implementacja AnyEvent oparta na module IO::Async.

%package Impl-Irssi
Summary:	AnyEvent implementation for Irssi
Summary(pl.UTF-8):	Implementacja AnyEvent dla Irssi
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Irssi
AnyEvent implementation used when running within irssi.

%description Impl-Irssi -l pl.UTF-8
Implementacja AnyEvent używana wewnątrz irssi.

%package Impl-POE
Summary:	AnyEvent implementation based on POE
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na module POE
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-POE
AnyEvent implementation based on POE (very slow, some limitations).

%description Impl-POE -l pl.UTF-8
Implementacja AnyEvent oparta na module POE (bardzo wolna, z
ograniczeniami).

%package Impl-Qt
Summary:	AnyEvent implementation based on Qt
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na Qt
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Qt
AnyEvent implementation based on Qt.

%description Impl-Qt -l pl.UTF-8
Implementacja AnyEvent oparta na Qt.

%package Impl-Tk
Summary:	AnyEvent implementation based on Tk
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na Tk
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-Tk
AnyEvent implementation based on Tk (very broken).

%description Impl-Tk -l pl.UTF-8
Implementacja AnyEvent oparta na Tk (z licznymi błędami).

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

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/AnyEvent

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Cocoa::EventLoop is OSX-only
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/AnyEvent/Impl/Cocoa.pm \
	$RPM_BUILD_ROOT%{_mandir}/man3/AnyEvent::Impl::Cocoa.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/AnyEvent
%{perl_vendorarch}/AnyEvent.pm
%dir %{perl_vendorarch}/AnyEvent
%{perl_vendorarch}/AnyEvent/*.pm
%dir %{perl_vendorarch}/AnyEvent/IO
%{perl_vendorarch}/AnyEvent/IO/*.pm
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
%{_mandir}/man3/AnyEvent::[DFHLSTU]*.3pm*
%{_mandir}/man3/AnyEvent::IO*.3pm*
%{_mandir}/man3/AnyEvent::Intro.3pm*
%{_mandir}/man3/AnyEvent::Impl::Perl.3pm*

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

%files Impl-FLTK
%defattr(644,root,root,755)
%{perl_vendorarch}/AnyEvent/Impl/FLTK.pm
%{_mandir}/man3/AnyEvent::Impl::FLTK.3pm*

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
