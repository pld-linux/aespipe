Summary:	AES-encryption tool for tar/cpio and loop-aes images
Name:		aespipe
Version:	2.2d
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://loop-aes.sourceforge.net/aespipe/%{name}-v%{version}.tar.bz2
# Source0-md5:	d7f2acc68062ffc5dc71c01f5c5b8af7
URL:		http://loop-aes.sourceforge.net/
BuildRequires:  autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aespipe is an encryption tool that reads from standard input and
writes to standard output. It uses the AES (Rijndael) cipher.

It can be used as an encryption filter, to create and restore
encrypted tar/cpio backup archives and to read/write and convert
loop-AES compatible encrypted images.

aespipe can be used for non-destructive in-place encryption of
existing disk partitions for use with the loop-AES encrypted loopback
kernel module.

%prep
%setup -q -n %{name}-v%{version}

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
%ifarch %{amd64} 
	amd64
%endif
%ifarch %{ix86}
	x86
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install  aespipe $RPM_BUILD_ROOT%{_bindir}
install  bz2aespipe $RPM_BUILD_ROOT%{_bindir}
install  aespipe.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man1/*
