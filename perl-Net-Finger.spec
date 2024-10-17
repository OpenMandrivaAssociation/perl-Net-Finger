%define upstream_name    Net-Finger
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A Perl implementation of a finger client
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Finger is a simple, straightforward implementation of a finger client in
Perl -- so simple, in fact, that writing this documentation is almost
unnecessary.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.0
+ Revision: 404092
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.06-14mdv2009.0
+ Revision: 258010
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.06-13mdv2009.0
+ Revision: 246082
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.06-11mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-11mdv2008.0
+ Revision: 86690
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-10mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.06-9mdk
- Fix SPEC according to Perl Policy
    - Source URL

* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-8mdk
- spec cleanup
- fix directory ownership
- %%mkrel
- rpmbuildupdate aware
- better summary
- better description
- better url

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.06-7mdk
- rpmbuildupdated

