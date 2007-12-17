%define module  Net-Finger
%define name    perl-%{module}
%define version 1.06
%define release %mkrel 11

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A Perl implementation of a finger client
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch

%description
Net::Finger is a simple, straightforward implementation of a finger client in
Perl -- so simple, in fact, that writing this documentation is almost
unnecessary.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Net
%{_mandir}/*/*

