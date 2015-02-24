#
# Conditional build:
%bcond_with	bootstrap	# bootstrap from <= 1.2-rc1 (with speexdsp in base)
%bcond_without	static_libs	# don't build static library

Summary:	An open-source, patent-free speech codec
Summary(pl.UTF-8):	Otwarty kodek mowy, wolny od patentów
Name:		speex
Version:	1.2
%define	subver	rc2
%define	rel	2
Release:	%{subver}.%{rel}
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/speex/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	6ae7db3bab01e1d4b86bacfa8ca33e81
URL:		http://www.speex.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
%if %{with bootstrap}
BuildRequires:	speex-devel >= 1:1.2-beta3
BuildRequires:	speex-devel < 1:1.2-rc2
%else
BuildRequires:	speexdsp-devel >= 1.2
%endif
Obsoletes:	Speex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Speex is a patent-free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%description -l pl.UTF-8
Speex jest wolnym od patentów kodekiem audio zaprojektowanym dla
kompresji mowy (w odróżnieniu od Vorbisa, który jest ogólnego
przeznaczenia). Zapewnia dobrą jakość nawet przy niskim paśmie.
Projekt chciałby być dodatkiem do kodeka Vorbis.

%package devel
Summary:	Speex library - development files
Summary(pl.UTF-8):	Pliki dla programistów używających biblioteki Speex
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	Speex-devel

%description devel
Speex library - development files.

%description devel -l pl.UTF-8
Pliki dla programistów używających biblioteki Speex.

%package static
Summary:	Speex static library
Summary(pl.UTF-8):	Biblioteka statyczna Speex
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	Speex-static

%description static
Speex static library.

%description static -l pl.UTF-8
Biblioteka statyczna Speex.

%package progs
Summary:	speexdec and speexenc utilities
Summary(pl.UTF-8):	Narzędzia speexdec i speexenc
Group:		Applications/Sound
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	Speex-progs

%description progs
Utilities for the Speex codec: speexdec (decodes a Speex file and
produces a WAV or raw file) and speexenc (encodes file from WAV or raw
format using Speex).

%description progs -l pl.UTF-8
Narzędzia do kodeka Speex: speexdec (dekodujące plik Speex i tworzące
plik WAV lub raw) oraz speexenc (kodujący plik z formatu WAV lub raw
przy użyciu kodeka Speex).

%prep
%setup -q -n %{name}-%{version}%{subver}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-ogg-libraries=%{_libdir} \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_DATA=

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libspeex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspeex.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/manual.pdf
%attr(755,root,root) %{_libdir}/libspeex.so
%{_libdir}/libspeex.la
# note: dir shared with speexdsp-devel
%dir %{_includedir}/speex
%{_includedir}/speex/speex.h
%{_includedir}/speex/speex_bits.h
%{_includedir}/speex/speex_callbacks.h
%{_includedir}/speex/speex_config_types.h
%{_includedir}/speex/speex_header.h
%{_includedir}/speex/speex_stereo.h
%{_includedir}/speex/speex_types.h
%{_aclocaldir}/speex.m4
%{_pkgconfigdir}/speex.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libspeex.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/speexdec
%attr(755,root,root) %{_bindir}/speexenc
%{_mandir}/man1/speexdec.1*
%{_mandir}/man1/speexenc.1*
