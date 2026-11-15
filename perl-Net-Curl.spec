#
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		pdir	Net
%define		pnam	Curl
Summary:	Net::Curl - object oriented interface to curl
Name:		perl-Net-Curl
Version:	0.60
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/S/SY/SYP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cba3b9e2b4a47ef6b437fe434dbda806
URL:		https://metacpan.org/dist/Net-Curl
BuildRequires:	curl-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Curl provides a Perl interface to libcurl created with
object-oriented implementations in mind.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags} %{rpmcppflags}" \
	OTHERLDFLAGS="%{rpmldflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Net/Curl/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/Curl.pm
%{perl_vendorarch}/Net/Curl
%dir %{perl_vendorarch}/auto/Net/Curl
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Curl/Curl.so
%{_mandir}/man3/*
