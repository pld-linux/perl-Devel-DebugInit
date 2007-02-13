#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# fail on too deep recursion
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	DebugInit
Summary:	Creating a debugger initialization files from C header file macros
Summary(pl.UTF-8):	Tworzenie plików inicjalizacyjnych odpluskwiacza z makr nagłówków C
Name:		perl-Devel-DebugInit
Version:	0.3
Release:	12
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2a40f42bf194e4ef5250d6dd59fa00ed
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-C-Scan
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::DebugInit is aimed at C/C++ developers who want access to C
macro definitions from within a debugger. It provides a simple and
automated way of creating debugger initialization files for a specific
project. The initialization files created contain user-defined
functions built from the macro definitions in the project's header
files.

%description -l pl.UTF-8
Moduł Devel::DebugInit ma służyć programistom C/C++, którzy chcą
dostać się do definicji makr C z poziomu odpluskwiacza. Moduł
udostępnia prosty i zautomatyzowany sposób tworzenia plików
inicjalizacyjnych odpluskwiacza dla danego projektu. Tworzone pliki
inicjalizacyjne zawierają podane przez użytkownika funkcje zbudowane z
definicji makr w plikach nagłówkowych projektu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_tests:%{__make} test}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Devel/DebugInit.pm
%{perl_vendorlib}/Devel/DebugInit
%{_mandir}/man3/*
