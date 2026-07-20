%global kf_version 6.24.0

Name: kf6-kauth
Version: 6.24.0
Release: 1%{?dist}
Summary: Execute actions as privileged user

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kauth

Source0: %{name}-%{version}.tar.bz2

BuildRequires: kf6-extra-cmake-modules >= %{kf_version}
BuildRequires: kf6-kcoreaddons-devel >= %{kf_version}
BuildRequires: kf6-rpm-macros

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel

BuildRequires: pkgconfig(Qt6DBus)

Requires: qt6-qtbase-gui
Requires: kf6-kcoreaddons

%description
KAuth is a framework to let applications perform actions as a privileged user.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: kf6-kcoreaddons-devel >= %{kf_version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6 -DKDE_INSTALL_LIBEXECDIR=%{kf6_libexecdir}
%cmake_build

%install
%cmake_install

%find_lang_kf6 kauth6_qt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kauth6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kauth.*
%{_kf6_libdir}/libKF6AuthCore.so.*
%{_kf6_datadir}/dbus-1/system.d/org.kde.kf6auth.conf
%{_kf6_plugindir}/kauth/
%{_kf6_datadir}/kf6/kauth/
#%%{_kf6_libexecdir}/kauth/

%files devel
%{_kf6_includedir}/KAuth/
%{_kf6_includedir}/KAuthCore/
#%%{_kf6_includedir}/KAuthWidgets/
%{_kf6_libdir}/libKF6AuthCore.so
%{_kf6_libdir}/cmake/KF6Auth/
#%%{_kf6_archdatadir}/mkspecs/modules/qt_KAuth*.pri

