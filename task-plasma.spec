Summary:	Metapackage for Plasma 5
Name:		task-plasma
Version:	5.4
Release:	0.3
License:	GPLv2+
Group:		Graphical desktop/KDE
Requires:	task-plasma-minimal
Requires:	distro-plasma-config
Requires:	bluedevil5
Requires:	digikam
Requires:	kopete
# (tpg) kdepim
Requires:	kleopatra
Requires:	akregator
Requires:	importwizard
Requires:	kaddressbook
Requires:	kalarm
Requires:	kmail
Requires:	knotes
Requires:	kontact
Requires:	korganizer
Requires:	storageservicemanager
Requires:	blogilo
Requires:	
# end pim
Requires:	ksystemlog
Requires:	krdc
Requires:	kdenlive
Requires:	kamera
Requires:	kcalc
Requires:	kwrite
Requires:	konversation
Requires:	ksnapshot
Requires:	ksaneplugin
Requires:	krfb
Requires:	kwalletmanager
#Requires:	kwallet-pam
Requires:	kuser
Requires:	okular
Requires:	sonnet-hunspell
Requires:	sddm
Requires:	sddm-kcm
Requires:	sddm-theme-breeze
Requires:	systemd-kcm
Requires:	muon
Requires:	khelpcenter
Requires:	plasma-mediacenter
#Requires:	plasma-workspace-wallpapers
Requires:	plasma5-applet-muonnotifier
Requires:	print-manager
Requires:	user-manager
Conflicts:	task-kde4
BuildArch:	noarch
%rename		task-plasma5 < 5.3-0.6

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
#Requires:	some theme is needed
Requires:	oxygen-fonts
Requires:	sni-qt
Suggests:	task-pulseaudio
Requires:	task-x11
#Requires:	xsettings-kde
# KDE4
Requires:	ark
Requires:	dolphin
Requires:	gwenview

# Plasma 5
Requires:	breeze
Requires:	frameworkintegration
Requires:	kde-cli-tools
Requires:	kinit
Requires:	kded
Requires:	kwrited
Requires:	kdeclarative
Requires:	milou
Requires:	baloo5
Requires:	plasma-pa
Requires:	plasma-desktop
Requires:	plasma-framework
Requires:	plasma-workspace
Requires:	kdeplasma-addons5
Requires:	kde-gtk-config5
Requires:	khotkeys
Requires:	kinfocenter5
Requires:	kio-extras
Requires:	kmenuedit
Requires:	konsole
Requires:	kscreen5
Requires:	kservice
Requires:	ksysguard
Requires:	ksshaskpass
# Requires:	kwin-wayland
Requires:	kwin-x11
Requires:	kwrited
Requires:	phonon4qt5-backend
Requires:	plasma-nm
Requires:	powerdevil >= 5.3.0
Requires:	systemsettings
Requires:	solid
Requires:	polkit-kde-agent-1
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

