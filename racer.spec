Summary:	Car simulator
Summary(pl):	Symulator samochodowy
Name:		racer
Version:	0.5.0
Release:	0.1
License:	Free for non-commercial use
Group:		X11/Applications/Games
Source0:	http://www.racer.nl/download/rr050src.tgz
# Source0-md5:	03793196c9fe3550c9e7c0d9de34a133
Source1:	http://download.tdconline.dk/pub/boomtown/racesimcentral/rr_data%{version}.tgz
# Source1-md5:	9c6f4b03f8ebf9913e0a714ae23efe55
Source2:	%{name}.desktop
Source3:	%{name}.sh
Source4:	%{name}.png
Patch0:		%{name}-%{version}_fmod-3.61_libQ.patch
#Patch0:	%{name}-makefile.patch
#Patch1:	%{name}-string.patch
URL:		http://www.racer.nl
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	libfmod = 3.61
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Racer is a free and open car simulation project, attempting to use
real car and vehicle physics to get a life-like feeling. Cars, tracks,
scenes and such can be created for it, with relative simplicity in
mind (compared to other driving simulations).

%description -l pl
Racer to darmowy i otwarty projekt symulatora, próbuj±cy wykorzystywaæ
rzeczywist± fizykê samochodu i pojazdu, aby uzyskaæ realistyczny
efekt. Samochody, tory, scenerie itp. mog± byæ dla niego stworzone ze
stosunkow± ³atwo¶ci±.

%prep
%setup -q -a 1 -n rr050src
%patch0 -p1
#- (blino) fix ar flags, remove -a option
%{__perl} -pi -e 's,ARFLAGS=-ar(.*),ARFLAGS=-r\1,' src/libs/*/makefile

%build
export OPTFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/racer/data,%{_desktopdir},%{_pixmapsdir}}
install src/racer/main/racer $RPM_BUILD_ROOT%{_bindir}/racer.bin
cp -R racer0.5.0/data/* $RPM_BUILD_ROOT%{_datadir}/racer/data
install racer0.5.0/*.ini $RPM_BUILD_ROOT%{_datadir}/racer
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/racer
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/%{name}.png
%{_datadir}/racer
