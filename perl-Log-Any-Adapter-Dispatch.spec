%define upstream_name    Log-Any-Adapter-Dispatch
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Log::Any::Adapter)
BuildRequires: perl(Log::Dispatch)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This Log::Any adapter uses Log::Dispatch for logging.

You may either pass parameters (like _outputs_) to be passed to
'Log::Dispatch->new', or pass a 'Log::Dispatch' object directly in the
_dispatcher_ parameter.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


