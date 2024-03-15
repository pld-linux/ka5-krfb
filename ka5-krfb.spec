#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.4
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		krfb
Summary:	krfb
Name:		ka5-%{kaname}
Version:	23.08.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	812bf1a25c53204d138241743ebbe7b5
URL:		http://www.kde.org/
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5WaylandClient-devel
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
BuildRequires:	kf5-kwayland-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-plasma-wayland-protocols-devel >= 1.5.0
BuildRequires:	kp5-kpipewire-devel
BuildRequires:	libepoxy-devel
BuildRequires:	libvncserver-devel
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	pipewire-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXtst-devel
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
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


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
%attr(755,root,root) %{_bindir}/krfb-virtualmonitor
%{_libdir}/libkrfbprivate.so.5
%dir %{_libdir}/qt5/plugins/krfb
%{_desktopdir}/org.kde.krfb.desktop
%{_desktopdir}/org.kde.krfb.virtualmonitor.desktop
%{_iconsdir}/hicolor/48x48/apps/krfb.png
%{_iconsdir}/hicolor/scalable/apps/krfb.svgz
%{_datadir}/krfb
%{_datadir}/metainfo/org.kde.krfb.appdata.xml
%{_datadir}/qlogging-categories5/krfb.categories
%{_libdir}/libkrfbprivate.so.5.0
%dir %{_libdir}/qt5/plugins/krfb/events
%{_libdir}/qt5/plugins/krfb/events/x11.so
%{_libdir}/qt5/plugins/krfb/events/xdp.so
%dir %{_libdir}/qt5/plugins/krfb/framebuffer
%{_libdir}/qt5/plugins/krfb/framebuffer/pw.so
%{_libdir}/qt5/plugins/krfb/framebuffer/qt.so
%{_libdir}/qt5/plugins/krfb/framebuffer/xcb.so
