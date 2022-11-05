#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	More-UTF8
Summary:	Test::More::UTF8 - Enhancing Test::More for UTF8-based projects
Summary(pl.UTF-8):	Test::More::UTF8 - rozszerzenie Test::More dla projektów opartych na UTF-8
Name:		perl-Test-More-UTF8
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7f306c38691e861425559035d0807312
URL:		https://metacpan.org/release/Test-More-UTF8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enhancing Test::More for UTF8-based projects.

%description -l pl.UTF-8
Rozszerzenie Test::More dla projektów opartych na UTF-8

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/More/UTF8.pm
%{perl_vendorlib}/Test/More/UTF8
%{_mandir}/man3/Test::More::UTF8.3pm*
