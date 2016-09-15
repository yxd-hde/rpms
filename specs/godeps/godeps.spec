%define import_path   github.com/rogpeppe/godeps
%define build_timestamp %(date -u +"%Y%m%d")

Summary: A simple command to manage Go package dependencies.
Name: godeps
Version: %{build_timestamp}
Release: 1
License: GNU Affero GPL v3
URL: https://%{import_path}
BuildRequires: golang git

%description
%{summary}

%prep


%build

mkdir _build
pushd _build

export GOPATH=$(pwd)
go get -v -u %{import_path}

popd

%install

install -d %{buildroot}%{_bindir}
install -p -m 755 _build/bin/godeps %{buildroot}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/godeps
