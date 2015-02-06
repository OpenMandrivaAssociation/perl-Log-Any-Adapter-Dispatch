%define upstream_name    Log-Any-Adapter-Dispatch
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	This Log::Any adapter uses Log::Dispatch for logging
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Log::Dispatch)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Log::Any::Adapter)
# Looks like this one is also needed
BuildRequires:	perl-Log-Any-Adapter
BuildArch:	noarch

%description
This Log::Any adapter uses Log::Dispatch for logging.

You may either pass parameters (like _outputs_) to be passed to
'Log::Dispatch->new', or pass a 'Log::Dispatch' object directly in the
_dispatcher_ parameter.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-3mdv2011.0
+ Revision: 657787
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 624920
- Fix the dependency on perl-Log-Any-Adapter
- import perl-Log-Any-Adapter-Dispatch

