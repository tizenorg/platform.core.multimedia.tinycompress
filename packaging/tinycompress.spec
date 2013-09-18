Name:       tinycompress
Summary:    userspace library for alsa compressed API
Version:    0.2.0
Release:    1
Group:      System/Libraries
License:    LGPL & BSD
Source0:    tinycompress-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires: pkgconfig(alsa)

%description
userspace library for alsa compressed API

%package devel
Summary:    tinycompress headers and libraries for development.
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
tinycompress headers and libraries for development.

%prep
%setup -q -n %{name}-%{version}


%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DVERSION=%{version}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/cplay
%{_libdir}/libtinycompress.so.*

%files devel
%{_libdir}/libtinycompress.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/tinycompress-0.2.0/tinycompress/tinycompress.h
%{_includedir}/tinycompress-0.2.0/tinycompress/tinymp3.h
%{_includedir}/tinycompress-0.2.0/tinycompress/version.h
%{_includedir}/tinycompress-0.2.0/sound/compress_offload.h
%{_includedir}/tinycompress-0.2.0/sound/compress_params.h
