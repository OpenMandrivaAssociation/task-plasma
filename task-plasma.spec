Summary:	Metapackage for Plasma 5
Name:		task-plasma
Version:	5.10.5
Release:	4
License:	GPLv2+
Group:		Graphical desktop/KDE
Requires:	task-plasma-minimal >= %{version}
Requires:	distro-plasma-config
Requires:	openmandriva-kde-icons
%ifnarch %{armx}
Requires:	grub2-editor
%endif
Requires:	bluedevil5
Requires:	colord-kde
Requires:	kwayland
Requires:	kwayland-integration
Requires:	kwin-wayland >= %{version}
Requires:	k3b
# (tpg) needs to be updated to KF5
Requires:	digikam
# (bero) needs to be updated to KF5 [or replaced with %{name}-telepathy once that works well]
#Requires:	kopete
Requires:	kamoso
Requires:	ktorrent
Requires:	krita
Requires:	dolphin-plugins
Requires:	audiocd-kio
Requires:	ffmpegthumbs
Requires:	kaccounts-integration
Requires:	kaccounts-providers
Requires:	kdenetwork-filesharing
Requires:	kidentitymanagement
Requires:	zeroconf-ioslave
Requires:	kdeconnect
Requires:	kdegraphics-thumbnailers
Requires:	kget
Requires:	kio-gdrive
# (tpg) kdepim
Requires:	kdepim-runtime
Requires:	akonadi-notes-agent
Requires:	akonadi-search
Requires:	akonadi-calendar-tools
Requires:	kleopatra
Requires:	kaddressbook
Requires:	kmail
Requires:	kmail-account-wizard
Requires:	kontact
Requires:	kalarm
Requires:	korganizer
Requires:	akregator
# end pim
Requires:	kdialog
Requires:	ksystemlog
Requires:	krdc
Requires:	kdenlive
Requires:	kamera
Requires:	kcalc
Requires:	kate
Requires:	kdf
Requires:	kgamma5
Requires:	kwrite
Requires:	konversation
Requires:	spectacle
Requires:	kipi-plugins
Requires:	krfb
Requires:	kwallet-pam
Requires:	signon-kwallet-extension
Requires:	kwave
Requires:	okular
Requires:	sonnet-hunspell
Requires:	speech-dispatcher
Requires:	myspell-dictionary
Requires:	sddm
Requires:	sddm-kcm
Requires:	sddm-theme-breeze
Requires:	skanlite
Requires:	systemd-kcm
Requires:	discover
Requires:	khelpcenter
Requires:	partitionmanager
# (tpg) we have our own wallpapers :)
#Requires:	plasma-workspace-wallpapers
Requires:	discover-notifier
Requires:	print-manager
Requires:	skrooge
Requires:	user-manager
Requires:	ssr
Suggests:	xscreensaver
Suggests:	yakuake

Provides:	task-kde4 = 1:4.14.4
Obsoletes:	task-kde4 <= 1:4.14.3
%rename		task-plasma5 < 5.3-0.6

%description
This package is a meta-package, meaning that its purpose is to contain
the complete dependencies for running the Plasma 5 desktop.

%files

#----------------------------------------------------------------------------

%package telepathy
Summary:	Packages needed to use Telepathy instant messenging in Plasma 5
Group:		Graphical desktop/KDE
Requires:	ktp-approver
Requires:	ktp-send-file
Requires:	ktp-text-ui
Requires:	ktp-auth-handler
Requires:	ktp-filetransfer-handler
Requires:	ktp-call-ui
Requires:	ktp-desktop-applets
Requires:	ktp-kded-module
Requires:	ktp-contact-runner
Requires:	ktp-accounts-kcm
Requires:	ktp-common-internals
Requires:	ktp-contact-list
Requires:	signon-kwallet-extension
# Telepathy needed for KTP
Requires:	telepathy-logger
Requires:	telepathy-mission-control
Suggests:	telepathy-haze
Suggests:	telepathy-gabble

%description telepathy
This package is a meta-package, meaning that its purpose is to contain
dependencies for running Telepathy instant messenging in a Plama 5
desktop environment.

%files telepathy

#----------------------------------------------------------------------------

%package minimal
Summary:	Minimal dependencies needed for Plasma 5
Group:		Graphical desktop/KDE
# Basic
Requires:	dbus-x11
Requires:	oxygen-fonts
Requires:	oxygen-icons
Suggests:	task-pulseaudio
Requires:	task-x11
Requires:	xsettings-kde
Requires:	ark
Requires:	dolphin
Requires:	gwenview
Requires:	pinentry-qt5
Requires:	libproxy-kde
Requires:	libproxy-networkmanager

# Plasma 5
Requires:	breeze
Requires:	breeze-icons
Requires:	oxygen-sounds
Requires:	frameworkintegration
Requires:	kde-cli-tools
Requires:	kinit
Requires:	kded
Requires:	kdeclarative
Requires:	milou
Requires:	baloo5
Requires:	plasma-pa
Requires:	plasma-integration
Requires:	plasma-desktop >= %{version}
Requires:	plasma-framework
Requires:	plasma-workspace >= %{version}
Requires:	kdeplasma-addons
Requires:	kde-gtk-config
Requires:	khotkeys
Requires:	kinfocenter >= 5.8.4
Requires:	kio-extras
Requires:	kmenuedit
Requires:	konsole
Requires:	kscreen5
Requires:	kscreenlocker
Requires:	kservice
Requires:	ksysguard
Requires:	ksshaskpass
Requires:	kwalletmanager
Requires:	kwin-x11 >= %{version}
Requires:	kwrited
Requires:	phonon4qt5-backend
Requires:	plasma-nm
Requires:	powerdevil >= 5.8.4
Requires:	systemsettings
Requires:	solid
Requires:	polkit-kde-agent-1
Requires:	desktop-common-data
Provides:	task-kde4-minimal = 1:4.14.4
Obsoletes:	task-kde4-minimal <= 1:4.14.3

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Plama 5 desktop environment.


%files minimal

#----------------------------------------------------------------------------

%prep

%build

%install

