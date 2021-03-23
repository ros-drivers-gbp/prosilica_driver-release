%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-prosilica-camera
Version:        1.9.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS prosilica_camera package

License:        BSD
URL:            http://www.ros.org/wiki/prosilica_camera
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-camera-calibration-parsers
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-diagnostic-updater
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-image-transport
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-nodelet-topic-tools
Requires:       ros-noetic-polled-camera
Requires:       ros-noetic-prosilica-gige-sdk
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-self-test
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
BuildRequires:  ros-noetic-camera-calibration-parsers
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-diagnostic-msgs
BuildRequires:  ros-noetic-diagnostic-updater
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-image-transport
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-nodelet-topic-tools
BuildRequires:  ros-noetic-polled-camera
BuildRequires:  ros-noetic-prosilica-gige-sdk
BuildRequires:  ros-noetic-rosconsole
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-self-test
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A ROS driver node for AVT/Prosilica Gigabit Ethernet (GigE) cameras.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Mar 23 2021 Austin Hendrix <namniart@gmail.com> - 1.9.5-1
- Autogenerated by Bloom

