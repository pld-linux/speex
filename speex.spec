Summary:	An open-source, patent-free speech codec
Summary(pl):	Otwarty kodek mowy, wolny od patentów
Name:		speex
Version:	1.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.speex.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	c4264e345adf071d8455f0cab115b4de
URL:		http://www.speex.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Speex

%description
Speex is a patent-free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%description -l pl
Speex jest wolnym od patentów kodekiem audio zaprojektowanym dla
kompresji mowy (w odró¿nieniu od Vorbisa, który jest ogólnego
przeznaczenia). Zapewnia dobr± jako¶æ nawet przy niskim pa¶mie.
Projekt chcia³by byæ dodatkiem do kodeka Vorbis.

%package devel
Summary:	Speex library - development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych biblioteki Speex
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	Speex-devel

%description devel
Speex library - development files.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych biblioteki Speex.

%package static
Summary:	Speex static library
Summary(pl):	Biblioteka statyczna Speex
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	Speex-static

%description static
Speex static library.

%description static -l pl
Biblioteka statyczna Speex.

%package progs
Summary:	speexdec and speexenc utilities
Summary(pl):	Narzêdzia speexdec i speexenc
Group:		Applications/Sound
Requires:	%{name} = %{version}
Obsoletes:	Speex-progs

%description progs
Utilities for the Speex codec: speexdec (decodes a Speex file and
produces a WAV or raw file) and speexenc (encodes file from WAV or
raw format using Speex).

%description progs -l pl
Narzêdzia do kodeka Speex: speexdec (dekoduj±ce plik Speex i tworz±ce
plik WAV lub raw) oraz speexenc (koduj±cy plik z formatu WAV lub raw
przy u¿yciu kodeka Speex).

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/manual.pdf
%attr(755,root,root) %{_libdir}/libspeex.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/manual.pdf
%{_libdir}/libspeex.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
