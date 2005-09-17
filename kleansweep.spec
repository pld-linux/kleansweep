Summary:	KleanSweep consists of KDE-based (C++) graphical frontend and small helper Perl script that performs actual searching
Summary(pl):	KleanSweep sk�ada si� z graficznego interjesu opartego na KDE
i ma�ego skryptu pomocniczego w Perlu, kt�ry wykonuje poszukiwania
Name:		kleansweep
Version:	0.1.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.bydg.org/~yogin/%{name}-%{version}.tar.bz2
# Source0-md5:	1521d883eb059575a6dbde42866ec4ec
URL:		http://linux.bydg.org/~yogin/
BuildRequires:	docbook-dtd-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	kdelibs >= 3.0
BuildRequires:	perl
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KleanSweep consists of KDE-based (C++) graphical frontend and small
helper Perl script that performs actual searching. All searches,
except for orphaned files, duplicates and dead menu entires are as
fast as usual 'find' would be. KleanSweep requires KDE libraries and
Perl. Note: Author takes no responsibility for any damage caused by
this program. Rate this project at kde-apps.org.

%description -l pl
KleanSweep sk�ada si� z graficznego interjesu opartego na KDE i ma�ego
skryptu pomocniczego w Perlu, kt�ry wykonuje poszukiwania. Wszystkie
poszukiwania, za wyj�tkiem osieroconych plik�w, zduplikowanych i
martwych wpis�w menu, s� tak szybko jak zwyk�e 'szukanie' mo�e by�.
KleanSweep wymaga bibliotek KDE i Perl. Uwaga: Autor nie bierze
odpowiedzialno�ci za jakiekolwiek uszkodzenia spowodowane tym
programem. Oddaj g�os na tej projekt na kde-apps.org.

%prep
%setup -q

%build
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

mv -f $RPM_BUILD_ROOT%{_applnkdir}/System/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/
echo "Categories=Qt;KDE;Utility;System;" >> $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%doc %{_kdedocdir}/en/
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/apps/%{name}/*.png
%{_desktopdir}/%{name}.desktop
