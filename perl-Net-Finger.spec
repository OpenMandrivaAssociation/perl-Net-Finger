%define upstream_name    Net-Finger
%define upstream_version 1.06
Name:		perl-%{upstream_name}
Version:	1.06
Release:	1

Summary:	A Perl implementation of a finger client
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Net-Finger
Source0:	https://cpan.metacpan.org/authors/id/F/FI/FIMM/Net-Finger-1.06.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Finger is a simple, straightforward implementation of a finger client in
Perl -- so simple, in fact, that writing this documentation is almost
unnecessary.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/Net
%{_mandir}/*/*

