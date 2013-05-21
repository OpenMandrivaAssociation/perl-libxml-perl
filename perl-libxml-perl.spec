%define upstream_name	 libxml-perl
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Various perl modules and script for working with XML
License:	Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel
BuildArch:	noarch
Requires:	perl-XML-Parser

%description
The %{upstream_name} perl module is a collection of smaller Perl modules, scripts,
and documents for working with XML in Perl.  libxml-perl software works
in combination with XML::Parser, PerlSAX, XML::DOM, XML::Grove and others. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Change* README
%{perl_vendorlib}/Data/*
%{perl_vendorlib}/XML/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-4mdv2012.0
+ Revision: 765390
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-2
+ Revision: 667470
- mass rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 407788
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.08-4mdv2009.0
+ Revision: 223807
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.08-3mdv2008.1
+ Revision: 180828
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.08-2mdv2007.0
+ Revision: 108474
- enable test, rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-libxml-perl

* Fri Nov 26 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.08-1mdk
- 0.08
- remove MANIFEST and empty directories

* Tue Aug 10 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.07-10mdk
- Rebuild for new perl

