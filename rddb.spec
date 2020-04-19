Name:           rddb
Version:        0.1
Release:        42%{?dist}
Summary:        The only debugging tool that matters

License:        BSD-2-Clause
URL:            https://github.com/universal-rddb/rddb
Source0:        %{name}-%{version}.tar.gz

%description
This tool prevents you from asking your coworkers stupid questions.

%define debug_package %{nil}
%prep
%autosetup

%build
sed -e"s|@DATADIR@|%{_datadir}|" rddb.in > rddb

%install
sed -e"s|@DATADIR@|%{buildroot}/%{_datadir}|" -e"s|@BINDIR@|%{buildroot}/%{_bindir}|" install.sh.in > install.sh
chmod +x install.sh
rm -rf $RPM_BUILD_ROOT
./install.sh


%files
%license LICENSE
%{_bindir}/rddb
%{_datadir}/rddb/*

%changelog
* Sun Apr 19 2020 Hunter Gilbert <hunter.gilbert@outlook.com>
-  Initial rpm package created
