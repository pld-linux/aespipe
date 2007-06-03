Summary:	AES-encryption tool for tar/cpio and loop-aes images
Summary(pl.UTF-8):	Narzędzie do szyfrowania AES dla tar/cpio i obrazów loop-aes
Name:		aespipe
Version:	2.3d
Release:	1
License:	GPL
Group:		Applications
Source0:	http://loop-aes.sourceforge.net/aespipe/%{name}-v%{version}.tar.bz2
# Source0-md5:	9b5369ab2c0d5439b7cd09d61d6ef479
URL:		http://loop-aes.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.213
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

%description -l pl.UTF-8
aespipe to narzędzie do szyfrowania czytające ze standardowego wejścia
i piszące na standardowe wyjście. Używa szyfru AES (Rijndael).

Może być używane jako filtr szyfrujący, do tworzenia i odtwarzania
zaszyfrowanych archiwów kopii zapasowych tar/cpio oraz do
zapisu/odczytu i konwersji zaszyfrowanych obrazów kompatybilnych z
loop-aes.

aespipe może być używane do niedestruktywnego szyfrowania "w miejscu"
istniejących partycji do używania z modułem jądra szyfrowanego systemu
plików po loopbacku loop-AES.

%prep
%setup -q -n %{name}-v%{version}

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
%ifarch %{x8664} 
	amd64
%endif
%ifarch %{ix86}
	x86
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install aespipe $RPM_BUILD_ROOT%{_bindir}
install bz2aespipe $RPM_BUILD_ROOT%{_bindir}
install aespipe.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
