%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	DebugInit
Summary:	Creating a debugger initialization files from C header file macros
Summary(pl):	Tworzenie plików inicjalizacyjnych odpluskwiacza z makr nag³ówków C
Name:		perl-Devel-DebugInit
Version:	0.3
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Modu³ Devel::DebugInit ma s³u¿yæ programistom C/C++, którzy chc±
dostaæ siê do definicji makr C z poziomu odpluskwiacza. Modu³
udostêpnia prosty i zautomatyzowany sposób tworzenia plików
inicjalizacyjnych odpluskwiacza dla danego projektu. Tworzone pliki
inicjalizacyjne zawieraj± podane przez u¿ytkownika funkcje zbudowane z
definicji makr w plikach nag³ówkowych projektu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Devel/DebugInit.pm
%{perl_vendorlib}/Devel/DebugInit
%{_mandir}/man3/*
