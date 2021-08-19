%define		kdeappsver	21.08.0
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		krfb
Summary:	krfb
Name:		ka5-%{kaname}
Version:	21.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	972a76b5e0c8e5ebbf8ce89d67706312
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdnssd-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	libvncserver-devel
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Krfb Desktop Sharing is a server application that allows you to share
your current session with a user on another machine, who can use a VNC
client to view or even control the desktop.

%description -l pl.UTF-8
Kfrb Współdzielenie Desktopu jest aplikacją serwerową pozwalającą Ci
współdzielić bieżącą sesję z użytkownikiem na innej maszynie, który
może użyć klienta VNC do podejrzenia a nawet kontrolowania Twojego
desktopu.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krfb
%{_libdir}/libkrfbprivate.so.5
%dir %{_libdir}/qt5/plugins/krfb
%{_desktopdir}/org.kde.krfb.desktop
%{_iconsdir}/hicolor/48x48/apps/krfb.png
%{_iconsdir}/hicolor/scalable/apps/krfb.svgz
%{_datadir}/krfb
%{_datadir}/kservicetypes5/krfb-framebuffer.desktop
%{_datadir}/metainfo/org.kde.krfb.appdata.xml
%{_datadir}/kservicetypes5/krfb-events.desktop
%{_datadir}/qlogging-categories5/krfb.categories
%{_libdir}/libkrfbprivate.so.5.0
%dir %{_libdir}/qt5/plugins/krfb/events
%{_libdir}/qt5/plugins/krfb/events/krfb_events_x11.so
%{_libdir}/qt5/plugins/krfb/events/krfb_events_xdp.so
%dir %{_libdir}/qt5/plugins/krfb/framebuffer
%{_libdir}/qt5/plugins/krfb/framebuffer/krfb_framebuffer_pw.so
%{_libdir}/qt5/plugins/krfb/framebuffer/krfb_framebuffer_qt.so
%{_libdir}/qt5/plugins/krfb/framebuffer/krfb_framebuffer_xcb.so
