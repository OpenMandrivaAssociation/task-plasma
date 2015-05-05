Summary:	Metapackage for Plasma 5
Name:		task-plasma5
Version:	5.3
Release:	0.1
License:	GPLv2+
Group:		Graphical desktop/KDE
Requires:	task-plasma5-minimal
Requires:	oxygen
Requires:	bluedevil5
Requires:	sddm
Conflicts:	task-kde4
BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
the complete dependencies for running the Plasma 5 desktop.

%files

#----------------------------------------------------------------------------

%package minimal
Summary:	Minimal dependencies needed for Plasma 5
Group:		Graphical desktop/KDE
# Basic
Requires:	dbus-x11
#Suggests:	phonon-gstreamer
#Requires:	some theme is needed
Requires:	oxygen-icons
# (tpg) doubt we need this
#Requires:	sni-qt
Suggests:	task-pulseaudio
Requires:	task-x11
#Requires:	xsettings-kde
# Plasma 5
Requires:	breeze
Requires:	frameworkintegration
Requires:	kde-cli-tools
Requires:	kinit
Requires:	kded
Requires:	kwrited
Requires:	kdeclarative
Suggests:	milou
Requires:	baloo5
Requires:	plasma-desktop
Requires:	plasma-framework
Requires:	plasma-workspace
Requires:	kdeplasma-addons5
Requires:	kde-gtk-config5
Requires:	khotkeys
Requires:	kinfocenter5
Requires:	kio-extras
Requires:	kmenuedit
Requires:	kmix
Requires:	konsole
Requires:	kscreen5
Requires:	kservice
Requires:	ksysguard
Requires:	kwin
Requires:	kwrited
Requires:	phonon-gstreamer
Requires:	plasma-nm5
Requires:	powerdevil
Requires:	systemsettings
Requires:	solid
Requires:	desktop-common-data
Conflicts:	task-kde4-minimal

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Plama 5 desktop environment.


%files minimal

#----------------------------------------------------------------------------

%prep

%build

%install

