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
Release:	1
Epoch:		3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pnam}-%{version}.tar.gz
# Source0-md5:	9c13447a7117e06e7a2fd553c4b2228c
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
# we are not allowed to use network while building package
%{__rm} t/05_dns.t

# satisfy rpm version deps, we have 3.9 in repo
# $ rpmvercmp 3.44 3.9
# 3.44 > 3.9
%{__sed} -i -e 's/use EV 3.44/use EV 3.5/' lib/AnyEvent/Impl/EV.pm

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
%{perl_vendorarch}/AnyEvent
%{perl_vendorarch}/AE.pm
%{_mandir}/man3/AE.3pm*
%{_mandir}/man3/AnyEvent*.3pm*
