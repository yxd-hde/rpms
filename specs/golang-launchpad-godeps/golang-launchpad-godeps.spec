%global debug_package %{nil}
%global import_path   launchpad.net/godeps
%global gopath        %{_datadir}/gocode
%global rev           27

Summary: A simple command to manage Go package dependencies.
Name: golang-launchpad-godeps
Version: 0
Release: r%{rev}
License: GNU Affero GPL v3
URL: https://%{import_path}
Source0: http://bazaar.launchpad.net/~godeps-maintainers/godeps/trunk/tarball/%{rev}
BuildRequires: golang git golang-github-kisielk-gotool

%description
%{summary}

%prep
%setup -n ~godeps-maintainers/godeps/trunk

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
* Fri Apr  3 2015  YANG Xudong <xudong.yang@hde.co.jp> r27-1
- Initial build.

