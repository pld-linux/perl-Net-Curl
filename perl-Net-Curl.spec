#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Curl
Summary:	Net::Curl -
Summary(pl.UTF-8):	Net::Curl - object oriented interface to curl
Name:		perl-Net-Curl
Version:	0.25
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	556a932ddf14757e05d3e1b527b28c49
URL:		http://search.cpan.org/dist/Net-Curl/
BuildRequires:	curl-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Thread)'

%description
Net::Curl provides a Perl interface to libcurl created with
object-oriented implementations in mind.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Net/Curl.pm
%{perl_vendorarch}/Net/Curl
%dir %{perl_vendorarch}/auto/Net/Curl
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Curl/Curl.so
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Curl/Curl.bs
%{_mandir}/man3/*
