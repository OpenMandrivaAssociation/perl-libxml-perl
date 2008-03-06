%define module	libxml-perl
%define version 0.08
%define release %mkrel 3

Summary:	Various perl modules and script for working with XML
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://www.cpan.org
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Requires:	perl perl-XML-Parser
BuildRequires:	perl-devel perl-XML-Parser
BuildArch:	noarch

%description
The %{module} perl module is a collection of smaller Perl modules, scripts,
and documents for working with XML in Perl.  libxml-perl software works
in combination with XML::Parser, PerlSAX, XML::DOM, XML::Grove and others. 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Change* README
%{perl_vendorlib}/Data/*
%{perl_vendorlib}/XML/*
%{_mandir}/*/*


