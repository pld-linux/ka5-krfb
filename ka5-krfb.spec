%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		krfb
Summary:	krfb
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	65e47bb18eef144e1d6dad82e23311d8
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdnssd-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	libvncserver-devel
BuildRequires:	libxcb-devel
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

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krfb
%attr(755,root,root) %{_libdir}/libkrfbprivate.so.5
%attr(755,root,root) %{_libdir}/libkrfbprivate.so.5.0
%dir %{_libdir}/qt5/plugins/krfb
%attr(755,root,root) %{_libdir}/qt5/plugins/krfb/krfb_framebuffer_qt.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krfb/krfb_framebuffer_xcb.so
%{_desktopdir}/org.kde.krfb.desktop
%{_iconsdir}/hicolor/48x48/apps/krfb.png
%{_iconsdir}/hicolor/scalable/apps/krfb.svgz
%{_datadir}/krfb
%{_datadir}/kservicetypes5/krfb-framebuffer.desktop
%{_datadir}/metainfo/org.kde.krfb.appdata.xml
