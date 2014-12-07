%define modname	libxml-perl
%define modver	0.08

Summary:	Various perl modules and script for working with XML
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	14
License:	Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel
Requires:	perl-XML-Parser

%description
The %{modname} perl module is a collection of smaller Perl modules, scripts,
and documents for working with XML in Perl.  libxml-perl software works
in combination with XML::Parser, PerlSAX, XML::DOM, XML::Grove and others. 

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*

