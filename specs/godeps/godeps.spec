%global debug_package %{nil}
%global import_path   github.com/rogpeppe/godeps
%global gopath        %{_datadir}/gocode
%global shortrev      c00f01a

Summary: A simple command to manage Go package dependencies.
Name: godeps
Version: r%{shortrev}
Release: 1
License: GNU Affero GPL v3
URL: https://%{import_path}
Source0: https://%{import_path}/tarball/%{shortrev}
BuildRequires: golang git golang-github-kisielk-gotool

%description
%{summary}

%prep
%setup -n rogpeppe-godeps-%{shortrev}

%build

mkdir _build
pushd _build

mkdir -p src/$(dirname %{import_path})
ln -s $(dirs +1 -l) src/%{import_path}
export GOPATH=$(pwd):%{gopath}
go build -v -a %{import_path}

popd

%install

install -d %{buildroot}%{_bindir}
install -p -m 755 _build/godeps %{buildroot}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/godeps

%changelog
* Wed Sep 14 2016 YANG Xudong <xudong.yang@hde.co.jp> rc00f01a-1
- Upgrade to latest commit.

* Tue Jun 14 2016 YANG Xudong <xudong.yang@hde.co.jp> r920c445-1
- Initial build.
