#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AnyEvent
%define		pnam	AnyEvent
Summary:	AnyEvent - provide framework for multiple event loops
Summary(pl):	AnyEvent - szkielet dla wielu p�tli zdarze�
Name:		perl-AnyEvent
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	aa4cbbb028aba63119c3ed44b2e14001
URL:		http://search.cpan.org/dist/AnyEvent/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AnyEvent extension aims to provide an simple and optimized event
loop for a broad class of applications.

%description -l pl
Rozszerzenie AnyEvent ma za zadanie udost�pni� pojedyncz� i
zoptymalizowan� p�tl� zdarze� dla szerokiej gamy aplikacji.

%prep
%setup -q -n %{pnam}-%{version}

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
%{perl_vendorlib}/AnyEvent.pm
%{perl_vendorlib}/AnyEvent
%{_mandir}/man3/*
