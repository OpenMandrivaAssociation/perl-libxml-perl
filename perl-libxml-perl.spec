%define modname	libxml-perl
%define modver	0.08

Summary:	Various perl modules and script for working with XML
Name:		perl-%{modname}
Version:	%{modver}
Release:	19
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/libxml-perl
Source0:	https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/libxml-perl-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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

