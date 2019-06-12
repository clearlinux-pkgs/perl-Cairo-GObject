#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Cairo-GObject
Version  : 1.004
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Cairo-GObject-1.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/X/XA/XAOC/Cairo-GObject-1.004.tar.gz
Summary  : 'Integrate Cairo into the Glib type system'
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-Cairo-GObject-lib = %{version}-%{release}
Requires: perl-Cairo-GObject-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Cairo)
BuildRequires : perl(ExtUtils::Depends)
BuildRequires : perl(ExtUtils::PkgConfig)
BuildRequires : perl(Glib)
BuildRequires : pkgconfig(cairo-gobject)

%description
Cairo::GObject
==============
Perl module to integrate Cairo into the Glib type system.

%package dev
Summary: dev components for the perl-Cairo-GObject package.
Group: Development
Requires: perl-Cairo-GObject-lib = %{version}-%{release}
Provides: perl-Cairo-GObject-devel = %{version}-%{release}
Requires: perl-Cairo-GObject = %{version}-%{release}

%description dev
dev components for the perl-Cairo-GObject package.


%package lib
Summary: lib components for the perl-Cairo-GObject package.
Group: Libraries
Requires: perl-Cairo-GObject-license = %{version}-%{release}

%description lib
lib components for the perl-Cairo-GObject package.


%package license
Summary: license components for the perl-Cairo-GObject package.
Group: Default

%description license
license components for the perl-Cairo-GObject package.


%prep
%setup -q -n Cairo-GObject-1.004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Cairo-GObject
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Cairo-GObject/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Cairo/GObject.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Cairo/GObject/Install/Files.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Cairo::GObject.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Cairo/GObject/GObject.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Cairo-GObject/LICENSE
