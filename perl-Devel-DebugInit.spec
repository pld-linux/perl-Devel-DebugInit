%include	/usr/lib/rpm/macros.perl
Summary:	Devel-DebugInit perl module
Summary(pl):	Modu³ perla Devel-DebugInit
Name:		perl-Devel-DebugInit
Version:	0.3
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-DebugInit-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-C-Scan
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-DebugInit perl module.

%description -l pl
Modu³ perla Devel-DebugInit.

%prep
%setup -q -n Devel-DebugInit-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Devel/DebugInit
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz

%{perl_sitelib}/Devel/DebugInit.pm
%{perl_sitelib}/Devel/DebugInit
%{perl_sitearch}/auto/Devel/DebugInit

%{_mandir}/man3/*
