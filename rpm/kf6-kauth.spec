%global kf6_version 6.18.0

Name: kf6-kauth
Version: 6.18.0
Release: 1%{?dist}
Summary: Execute actions as privileged user

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kauth

Source0: %{name}-%{version}.tar.bz2

BuildRequires: opt-extra-cmake-modules >= %{kf6_version}
BuildRequires: kf6-kcoreaddons-devel >= %{kf6_version}
BuildRequires: kf6-rpm-macros

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel

%{?_qt6:Requires: %{_qt6}%{?_isa} = %{qt6_version}}
Requires: qt6-qtbase-gui
Requires: kf6-kcoreaddons

%description
KAuth is a framework to let applications perform actions as a privileged user.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: kf6-kcoreaddons-devel >= %{kf6_version}
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc README.md
%license LICENSES/*.txt
%{kf6_datadir}/qlogging-categories6/kauth.*
%{kf6_libdir}/libKF6Auth.so.*
%{kf6_libdir}/libKF6AuthCore.so.*
%{kf6_datadir}/dbus-1/system.d/org.kde.kf6auth.conf
%{kf6_qtplugindir}/kauth/
%{kf6_datadir}/kf6/kauth/
#%{kf6_libexecdir}/kauth/
%{kf6_datadir}/locale/

%files devel
%{kf6_includedir}/KF6/KAuth/
%{kf6_includedir}/KF6/KAuthCore/
%{kf6_includedir}/KF6/KAuthWidgets/
%{kf6_libdir}/libKF6Auth.so
%{kf6_libdir}/libKF6AuthCore.so
%{kf6_libdir}/cmake/KF6Auth/
%{kf6_archdatadir}/mkspecs/modules/qt_KAuth*.pri

