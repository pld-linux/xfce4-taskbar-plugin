%define		snap 20130504
Summary:	Taskbar plugin which mimicks the Windows 7 taskbar (pinning applications, etc)
Name:		xfce4-taskbar-plugin
Version:	0.%{snap}
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	259533052a8398e50496052699b75787
Patch0:		make.patch
URL:		http://git.xfce.org/panel-plugins/xfce4-taskbar-plugin/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkhotkey-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfce4-panel-devel >= 4.12.0
Requires:	xfce4-panel >= 4.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Taskbar plugin which mimicks the Windows 7 taskbar
(pinning applications, etc)

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libtaskbar.so
%{_datadir}/xfce4/panel/plugins/taskbar.desktop
