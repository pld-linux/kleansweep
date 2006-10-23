Summary:	KleanSweep - KDE-based (C++) graphical frontend and script that performs actual searching
Summary(pl):	KleanSweep - graficzny interjes oparty na KDE i skrypt wykonuj±cy poszukiwania
Name:		kleansweep
Version:	0.2.8
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.bydg.org/~yogin/%{name}-%{version}.tar.bz2
# Source0-md5:	289d1f2584a8c999d5aad7efb6664520
URL:		http://linux.bydg.org/~yogin/
BuildRequires:	docbook-dtd-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KleanSweep consists of KDE-based (C++) graphical frontend and small
helper Perl script that performs actual searching. All searches,
except for orphaned files, duplicates and dead menu entires are as
fast as usual 'find' would be. KleanSweep requires KDE libraries and
Perl. Note: Author takes no responsibility for any damage caused by
this program. You can rate this project at kde-apps.org.

%description -l pl
KleanSweep sk³ada siê z graficznego interfejsu opartego na KDE i
ma³ego skryptu pomocniczego w Perlu, który wykonuje poszukiwania.
Wszystkie poszukiwania, za wyj±tkiem osieroconych plików,
zduplikowanych i martwych wpisów menu, s± tak szybkie, jak tylko mo¿e
byæ zwyk³e "szukanie". KleanSweep wymaga bibliotek KDE i Perla. Uwaga:
Autor nie bierze odpowiedzialno¶ci za jakiekolwiek uszkodzenia
spowodowane tym programem. Na ten projekt mo¿na g³osowaæ na
kde-apps.org.

%prep
%setup -q

%build
export CXXFLAGS="%{rpmcflags}"
export QTDIR="%{_usr}"

scons configure \
	qtincludes=%{_includedir}/qt \
	prefix=%{_prefix} %{?debug:debug=full} \
%if "%{_lib}" == "lib64"
	libsuffix=64 \
%endif
	qtlibs=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

DESTDIR=$RPM_BUILD_ROOT scons install

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/System/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/hicolor/*/apps/*.png
%dir %{_datadir}/apps/%{name}
%{_datadir}/apps/%{name}/*.png
%{_datadir}/apps/%{name}/%{name}-rules
%{_datadir}/apps/%{name}/%{name}-blacklist
%{_desktopdir}/%{name}.desktop
