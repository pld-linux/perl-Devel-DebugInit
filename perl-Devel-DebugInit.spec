%define	pdir	Devel
%define	pnam	DebugInit
%include	/usr/lib/rpm/macros.perl
Summary:	Devel-DebugInit perl module
Summary(pl):	Modu³ perla Devel-DebugInit
Name:		perl-Devel-DebugInit
Version:	0.3
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-C-Scan
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-DebugInit perl module.

%description -l pl
Modu³ perla Devel-DebugInit.

%prep
%setup -q -n Devel-DebugInit-%{version}

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
