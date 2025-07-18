#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_with	fltk	# FLTK binding (requires a long chain of non-existing packages)
%bcond_with	qt3	# Qt3 binding
#
%define		pdir	AnyEvent
%define		pnam	AnyEvent
Summary:	AnyEvent - provide framework for multiple event loops
Summary(pl.UTF-8):	AnyEvent - szkielet dla wielu pętli zdarzeń
Name:		perl-AnyEvent
Version:	7.17
Release:	1
Epoch:		3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/AnyEvent/%{pnam}-%{version}.tar.gz
# Source0-md5:	7ac0d8f410061ec2a62c6ca9341f5fed
Patch0:		%{name}-noarch.patch
URL:		https://metacpan.org/dist/AnyEvent
BuildRequires:	perl-Canary-Stability
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Suggests:	%{name}-Impl-EV
Obsoletes:	perl-AnyEvent-Impl-Cocoa
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AnyEvent extension aims to provide an simple and optimized event
loop for a broad class of applications.

%description -l pl.UTF-8
Rozszerzenie AnyEvent ma za zadanie udostępnić pojedynczą i
zoptymalizowaną pętlę zdarzeń dla szerokiej gamy aplikacji.

%package IOAIO
Summary:	IOAIO I/O model for AnyAvent module
Summary(pl.UTF-8):	Model we/wy IOAIO dla modułu AnyEvent
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description IOAIO
IOAIO I/O model for AnyAvent module.

%description IOAIO -l pl.UTF-8
Model we/wy IOAIO dla modułu AnyEvent.

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

%package Impl-UV
Summary:	AnyEvent implementation based on UV
Summary(pl.UTF-8):	Implementacja AnyEvent oparta na UV
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description Impl-UV
AnyEvent implementation based on UV.

%description Impl-UV -l pl.UTF-8
Implementacja AnyEvent oparta na UV.

%prep
%setup -q -n %{pnam}-%{version}
%patch -P0 -p1
# we are not allowed to use network while building package
%{__rm} t/05_dns.t

%build
PERL_CANARY_STABILITY_NOPROMPT=1 \
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
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/AnyEvent/Impl/Cocoa.pm \
	$RPM_BUILD_ROOT%{_mandir}/man3/AnyEvent::Impl::Cocoa.3pm

%if %{without fltk}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/AnyEvent/Impl/FLTK.pm
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/AnyEvent::Impl::FLTK.3pm*
%endif

%if %{without qt3}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/AnyEvent/Impl/Qt.pm
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/AnyEvent::Impl::Qt.3pm*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/AnyEvent.pm
%dir %{perl_vendorlib}/AnyEvent
%{perl_vendorlib}/AnyEvent/*.pm
%dir %{perl_vendorlib}/AnyEvent/IO
%{perl_vendorlib}/AnyEvent/IO/Perl.pm
%dir %{perl_vendorlib}/AnyEvent/Impl
# pureperl implementation, works everywhere, requires nothing
%{perl_vendorlib}/AnyEvent/Impl/Perl.pm
%{perl_vendorlib}/AnyEvent/Util
%{perl_vendorlib}/AnyEvent/FAQ.pod
%{perl_vendorlib}/AnyEvent/Intro.pod
%{perl_vendorlib}/AnyEvent/constants.pl
%{perl_vendorlib}/AE.pm
%{_mandir}/man3/AE.3pm*
%{_mandir}/man3/AnyEvent.3pm*
%{_mandir}/man3/AnyEvent::[DFHLSTU]*.3pm*
%{_mandir}/man3/AnyEvent::IO*.3pm*
%{_mandir}/man3/AnyEvent::Intro.3pm*
%{_mandir}/man3/AnyEvent::Impl::Perl.3pm*

%files IOAIO
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/IO/IOAIO.pm

%files Impl-EV
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/EV.pm
%{_mandir}/man3/AnyEvent::Impl::EV.3pm*

%files Impl-Event
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/Event.pm
%{_mandir}/man3/AnyEvent::Impl::Event.3pm*

%files Impl-EventLib
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/EventLib.pm
%{_mandir}/man3/AnyEvent::Impl::EventLib.3pm*

%if %{with fltk}
%files Impl-FLTK
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/FLTK.pm
%{_mandir}/man3/AnyEvent::Impl::FLTK.3pm*
%endif

%files Impl-Glib
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/Glib.pm
%{_mandir}/man3/AnyEvent::Impl::Glib.3pm*

%files Impl-IOAsync
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/IOAsync.pm
%{_mandir}/man3/AnyEvent::Impl::IOAsync.3pm*

%files Impl-Irssi
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/Irssi.pm
%{_mandir}/man3/AnyEvent::Impl::Irssi.3pm*

%files Impl-POE
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/POE.pm
%{_mandir}/man3/AnyEvent::Impl::POE.3pm*

%if %{with qt3}
%files Impl-Qt
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/Qt.pm
%{_mandir}/man3/AnyEvent::Impl::Qt.3pm*
%endif

%files Impl-Tk
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/Tk.pm
%{_mandir}/man3/AnyEvent::Impl::Tk.3pm*

%files Impl-UV
%defattr(644,root,root,755)
%{perl_vendorlib}/AnyEvent/Impl/UV.pm
%{_mandir}/man3/AnyEvent::Impl::UV.3pm*
