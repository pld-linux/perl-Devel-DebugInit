%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	DebugInit
Summary:	Creating a debugger initialization files from C header file macros
Name:		perl-Devel-DebugInit
Version:	0.3
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-C-Scan
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::DebugInit is aimed at C/C++ developers who want access to C macro
definitions from within a debugger. It provides a simple and automated
way of creating debugger initialization files for a specific project. The
initialization files created contain user-defined functions built from
the macro definitions in the project's header files.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Devel/DebugInit.pm
%{perl_sitelib}/Devel/DebugInit
%{_mandir}/man3/*
