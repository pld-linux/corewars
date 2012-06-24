#
# TODO:
# - add desktop file and png icon for package.
#
Summary:	A simulation game
Summary(pl):	Gra symulacyjna
Name:		corewars
Version:	0.9.13
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0a0b8067533b83a96488109ee265f664
Source1:	http://corewars.sourceforge.net/warriors.tar.gz
# Source1-md5:	6ad0dbacddda7253120ff15930d23009
Source2:	http://corewars.sourceforge.net/hill-warriors.tar.gz
# Source2-md5:	b10c44dfc18e39837fe45110df6086d3
URL:		http://corewars.sf.net/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Core Wars is a simulation game. A number of programs are loaded into a
virtual machine and executed. The programs can to crash each other,
manipulate other programs, overwrite as much memory as they can,
etc... The "best" program is selected according to a scoring mechanism
which involves the number of memory cells the program has overwritten,
the number of other programs it has crashed and whether/when it
crashed.

Two different languages are supported. The one called "Corewars" is
easy to learn. The second language, called "Redcode", is harder to
learn but also more powerful.

Additional polish Core Wars documentation is contained in pmars
package.

%description -l pl
Wojny Rdzeniowe s� gr� symulacyjn�. Kilka program�w zostaje
za�adowanych do wirtualnej pami�ci i wykonanych. Programy mog�
wysypywa� inne programy, manipulowa� nimi, nadpisywa� pami��, etc.
Mechanizm wyboru najlepszego programu bierze pod uwag� ilo�� kom�rek
pami�ci, kt�re program nadpisa�, liczb� ubitych program�w oraz
okoliczno�ci �mierci.

U�ywane s� dwa j�zyki. Pierwszy, "Corewars", jest �atwy do nauczenia
si�. Drugi, "Redcode", jest trudniejszy, lecz bardziej pot�ny.

Dodatkowa dokumentacja po polsku dotycz�ca Wojen Rdzeniowych znajduje
si� w pakiecie pmars.

%package warriors
Summary:	Core warriors
Summary(pl):	Wojownicy rdzeniowi
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description warriors
Core warriors.

%description warriors -l pl
Wojownicy rdzeniowi.

%prep
%setup -q -a1 -a2

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mkdir $RPM_BUILD_ROOT%{_datadir}/corewars/warriors
mv warriors $RPM_BUILD_ROOT%{_datadir}/corewars/warriors/all
# TODO: create links to above instead of doubling content
mv hill-warriors $RPM_BUILD_ROOT%{_datadir}/corewars/warriors/hill

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%dir %{_datadir}/corewars
%{_datadir}/corewars/*.cw
%{_datadir}/corewars/*.red

%files warriors
%defattr(644,root,root,755)
%{_datadir}/corewars/warriors
