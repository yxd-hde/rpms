%global debug_package %{nil}
%global import_path   github.com/t-yuki/gocover-cobertura
%global gopath        %{_datadir}/gocode
%global rev           51e121ba753c65cdc969ec7edabf651e2a018832
%global shortrev      %(r=%{rev}; echo ${r:0:7})

Summary: Go tool cover to XML (Cobertura) export tool.
Name: golang-github-t-yuki-gocover-cobertura
Version: r%{shortrev}
Release: 1
License: MIT
URL: https://%{import_path}
Source0: https://%{import_path}/tarball/%{shortrev}
BuildRequires: golang
Requires: golang-cover

%description
%{summary}

%prep
%setup -n t-yuki-gocover-cobertura-%{shortrev}

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
install -p -m 755 _build/gocover-cobertura %{buildroot}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/gocover-cobertura


%changelog
* Mon Apr  6 2015 YANG Xudong <xudong.yang@hde.co.jp> - r51e121b-1
- Initial build.
