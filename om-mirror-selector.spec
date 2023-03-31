Name:		om-mirror-selector
Version:	0.1.2
Release:	3
Summary:	OpenMandriva Lx best mirror selector
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaSoftware/om-mirror-selector
Source0:	https://github.com/OpenMandrivaSoftware/om-mirror-selector/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	systemd-rpm-macros
Requires:	openmandriva-repos >= 4.0-1
Requires:	sed
Requires:	coreutils
Requires:	iputils
BuildArch:	noarch

%description
A tool that helps to determine best mirror 
for yours OpenMandriva's software updates.

%prep
%autosetup

%build
# (tpg) nothing to build

%install
mkdir -p %{buildroot}{%{_bindir},%{_unitdir},%{_presetdir}}
install -m755 %{name}.sh %{buildroot}%{_bindir}/%{name}.sh
install -m644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -m644 %{name}.timer %{buildroot}%{_unitdir}/%{name}.timer

cat > %{buildroot}%{_presetdir}/86-%{name}.preset << EOF
disable %{name}.timer
EOF

%post
%systemd_post %{name}.timer

%files
%{_bindir}/%{name}.sh
%{_presetdir}/86-%{name}.preset
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
