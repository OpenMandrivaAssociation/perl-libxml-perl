%define upstream_name	 libxml-perl
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Various perl modules and script for working with XML
License:	Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl-XML-Parser

%description
The %{upstream_name} perl module is a collection of smaller Perl modules, scripts,
and documents for working with XML in Perl.  libxml-perl software works
in combination with XML::Parser, PerlSAX, XML::DOM, XML::Grove and others. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
