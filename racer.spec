Summary:	Car simulator
Summary(pl):	Symulator samochodowy
Name:		racer
Version:	0.4.7.1
Release:	1
License:	Free for non-commercial use
Group:		X11/Applications/Games
Source0:	http://www.ringlord.com/%{name}-linux-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.sh
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-string.patch
URL:		http://www.marketgraph.nl/gallery/racer/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description
Racer is a free and open car simulation project, attempting to use
real car and vehicle physics to get a life-like feeling. Cars, tracks,
scenes and such can be created for it, with relative simplicity in
mind (compared to other driving simulations).

%description -l pl
Racer to darmowy i otwarty projekt symulatora, próbuj±cy wykorzystywaæ
rzeczywist± fizykê samochodu i pojazdu, aby uzyskaæ realistyczny
efekt. Samochody, tory, scenerie itp mog± byæ dla niego sworzone ze
stosunkow± ³atwo¶ci±.

%prep
%setup -qn src/racer
%patch0 -p2
%patch1 -p2

%build
export OPTFLAGS="%{rpmcflags}"
./build.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/racer/data,%{_applnkdir}/Games}

install racer/racer $RPM_BUILD_ROOT%{_bindir}/racer.bin
cp -R racer/data/* $RPM_BUILD_ROOT%{_datadir}/racer/data
install racer/*.ini $RPM_BUILD_ROOT%{_datadir}/racer
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/racer

gzip -9nf README.linux

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.linux*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/racer
%{_applnkdir}/Games/*
