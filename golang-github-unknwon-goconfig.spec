# Run tests in check section
%bcond_without check

%global goipath         github.com/Unknwon/goconfig
%global commit          ef1e4c783f8f0478bd8bff0edb3dd0bade552599

%global common_description %{expand:
Configuration file parser for the Go Programming Language.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: Configuration file parser for the Go Programming Language
License: ASL 2.0
URL:     %{gourl}
Source:  %{gosource}

%if %{with check}
BuildRequires: golang(github.com/smartystreets/goconvey/convey)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

Provides: golang-github-Unknwon-goconfig-devel = %{version}-%{release}
Obsoletes: golang-github-Unknwon-goconfig-devel < 0-0.3.20180314gitef1e4c7
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README_ZH.md README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitef1e4c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314gitef1e4c7
- Update with the new Go packaging
- Upstream GIT revision ef1e4c7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20161121git87a46d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20161121git87a46d9
- First package for Fedora

