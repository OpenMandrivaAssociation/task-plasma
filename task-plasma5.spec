Summary:	Metapackage for Plasma 5
Name:		task-plasma5
Version:	5.2
Release:	0.1
License:	GPLv2+
Group:		Graphical desktop/KDE
Requires:	task-plasma5-minimal
Requires:	oxygen
Requires:	plasma5-bluedevil
Requires:	sddm
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
Suggests:	preload
Suggests:	readahead
Requires:	rosa-elementary-theme
Requires:	rosa-icons
Requires:	sni-qt
Suggests:	task-pulseaudio
Requires:	task-x11
#Requires:	xsettings-kde
# Plasma 5
Requires:	breeze
Requires:	frameworkintegration
Requires:	kde-cli-tools
Requires:	kinit
Requires:	kwrited
Suggests:	plasma5-applet-milou
Requires:	plasma5-baloo
Requires:	plasma5-decoration-aurorae
Requires:	plasma5-desktop
Requires:	plasma5-kdeplasma-addons
Requires:	plasma5-khotkeys
Requires:	plasma5-kinfocenter
Requires:	plasma5-kio-extras
Requires:	plasma5-kscreen
Requires:	plasma5-ksysguard
Requires:	plasma5-kwin
Requires:	plasma5-nm
Requires:	plasma5-powerdevil
Requires:	plasma5-systemsettings

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Plama 5 desktop environment.


%files minimal

#----------------------------------------------------------------------------

%prep

%build

%install

