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
Version:	5.251
Release:	2
Epoch:		2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	86457e3a7403976997193d2fc027482e
URL:		http://search.cpan.org/dist/AnyEvent/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AnyEvent extension aims to provide an simple and optimized event
loop for a broad class of applications.

%description -l pl.UTF-8
Rozszerzenie AnyEvent ma za zadanie udostępnić pojedynczą i
zoptymalizowaną pętlę zdarzeń dla szerokiej gamy aplikacji.

%prep
%setup -q -n %{pnam}-%{version}
#we are not allowed to use network while building package
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
%{perl_vendorlib}/AnyEvent.pm
%{perl_vendorlib}/AnyEvent
%{perl_vendorlib}/AE.pm
%{_mandir}/man3/*
