%global debug_package %{nil}
%global import_path   github.com/kisielk/gotool
%global gopath        %{_datadir}/gocode
%global rev           d678387370a2eb9b5b0a33218bc8c9d8de15b6be
%global shortrev      %(r=%{rev}; echo ${r:0:7})

Summary: A library of some of the utility functions provided by (but not exported) by cmd/go
Name: golang-github-kisielk-gotool
Version: r%{shortrev}
Release: 2
License: MIT
URL: https://%{import_path}
Source0: https://%{import_path}/tarball/%{shortrev}
BuildRequires: golang

%description
%{summary}

%prep
%setup -n kisielk-gotool-%{shortrev}

%install

install -d %{buildroot}/%{gopath}/src/%{import_path}

cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LEGAL LICENSE README.md
%{gopath}/*


%changelog
* Fri Apr  3 2015 YANG Xudong <xudong.yang@hde.co.jp> - rd678387-1
- Initial build.
