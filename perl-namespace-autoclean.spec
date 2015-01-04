Name:       perl-namespace-autoclean
Version:    0.19
Release:    1%{?dist}
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    Keep imports out of your namespace
Source:     http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/namespace-autoclean-%{version}.tar.gz
Url:        http://search.cpan.org/dist/namespace-autoclean
BuildArch:  noarch

# Module Build
BuildRequires:  perl
BuildRequires:  perl(Module::Build)
# Module
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:  perl(List::Util)
BuildRequires:  perl(namespace::clean) >= 0.20
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Identify)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(version)
# Optional Tests
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120900
%if 0%{?fedora} || 0%{?rhel} > 7 || 0%{?amzn}
BuildRequires:  perl(Moo) >= 1.000007
%endif
# Runtime
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Sub::Identify)

%{?perl_default_filter}

%description
When you import a function into a Perl package, it will naturally also be
available as a method. The 'namespace::autoclean' pragma will remove all
imported symbols at the end of the current package's compile cycle. Functions
called in the package itself will still be bound by their name, but they won't
show up as methods on your class or instances. This module is very similar to
namespace::clean, except it will clean all imported functions, no matter if you
imported them before or after you 'use'd the pragma. It will also not touch
anything that looks like a method.

%prep
%setup -q -n namespace-autoclean-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING README README.md
%{perl_vendorlib}/namespace/
%{_mandir}/man3/namespace::autoclean.3pm*

%changelog
* Thu Aug 14 2014 Paul Howarth <paul@city-fan.org> - 0.19-1
- Update to 0.19
  - Bump dependency on B::Hooks::EndOfScope, to get the separation of pure-perl
    and XS components (CPAN RT#89245)
  - Repository migrated to the github moose organization
  - Update configure_requires checking in Makefile.PL, add CONTRIBUTING file
  - Changed the code to no longer _require_ Class::MOP; if your class is not a
    Moose class then we don't load Class::MOP, which was particularly
    problematic for Moo classes, as using namespace::autoclean with a Moo class
    "upgraded" it to be a Moose class
  - Using this module just broke overloading in a class (CPAN RT#50938)
  - Add -except to import options; this allows you to explicitly not clean a
    sub.
  - Better method detection for Mouse (GH#4)
  - More comprehensive testing with Moo/Mouse/Moose
  - Fixed cleaning of constants
- This release by ETHER -> update source URL
- Switch to Module::Build::Tiny flow
- Update %%description to remove reference to Class::MOP
- Make %%files list more explicit

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.13-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.13-2
- Perl 5.16 rebuild

* Sat Jan 14 2012 Iain Arnell <iarnell@gmail.com> 0.13-1
- update to latest upstream version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.12-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.12-2
- Perl mass rebuild

* Sun Mar 13 2011 Iain Arnell <iarnell@gmail.com> 0.12-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.09-3
- rebuild against perl 5.10.1

* Thu Sep 17 2009 Stepan Kasal <skasal@redhat.com> 0.09-2
- fix the previous changelog entry

* Wed Sep 16 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- add %%perl_default_filter'ing
- auto-update to 0.09 (by cpan-spec-update 0.01)
- added a new req on perl(B::Hooks::EndOfScope) (version 0.07)
- added a new req on perl(Class::MOP) (version 0.80)
- added a new req on perl(List::Util) (version 0)
- added a new req on perl(namespace::clean) (version 0.11)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08-1
- submission

* Wed Jul 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
