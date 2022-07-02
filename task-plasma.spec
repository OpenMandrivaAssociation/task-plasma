Summary:	Metapackage for Plasma 5
Name:		task-plasma
Version:	5.25.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Requires:	task-plasma-minimal >= %{version}
Requires:	distro-plasma-config
Requires:	openmandriva-kde-icons
%ifnarch %{armx}
Requires:	grub2-editor
%endif
Requires:	bluedevil5
Requires:	drkonqi
# (crazy) FIXME: need -wayland task
Requires:	kwayland
Requires:	kwayland-integration
Requires:	kwin-wayland >= %{version}
Requires:	plasma-workspace-wayland >= %{version}
# Part of KApps, but not useful to people with computers
# that don't have optical drives -- let's not make it a
# hard requirement
Suggests:	k3b
Requires:	kbackup
# (tpg) Falkon is our default web browser
Requires:	falkon-kde
Requires:	falkon-plugins
Requires:	digikam
Requires:	kopete
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
# (crazy) FIXME: need -pim task
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
%ifnarch %{armx}
Requires:	plymouth-kcm
%endif
Requires:	sonnet-hunspell
Requires:	speech-dispatcher
Requires:	myspell-dictionary
Requires:	sddm
Requires:	sddm-kcm
Requires:	sddm-theme-breeze
Requires:	skanlite
Requires:	systemd-kcm
Requires:	khelpcenter
Requires:	partitionmanager
Requires:	discover
Requires:	discover-notifier
Requires:	discover-backend-packagekit
Requires:	print-manager
Requires:	kuser
Requires:	ssr
Requires:	kde-gtk-config
Requires:	plasma-firewall
Requires:	plasma-systemmonitor
Requires:	plasma-disks
Suggests:	xscreensaver
Suggests:	yakuake
Suggests:	skrooge
Recommends:	om-repo-picker
Recommends:	om-feeling-like
Recommends:	om-update-config
Recommends:	om-user-manager
Provides:	task-kde4 = 1:4.14.4
Obsoletes:	task-kde4 <= 1:4.14.3
%rename		task-plasma5

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
%if %omvver > 4050000
Requires:	kwin-wayland >= %{version}
Requires:	plasma-workspace-wayland >= %{version}
%else
Requires:	task-x11
Requires:	kwin-x11 >= %{version}
Requires:	plasma-workspace-x11 >= %{version}
%endif
Requires:	xsettingsd
Conflicts:	xsettings-kde
Requires:	ark
Requires:	kate
Requires:	dolphin
Requires:	konsole
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
%ifnarch %{armx}
Requires:	plasma-nm
%else
Requires:	cmst
%endif
Requires:	plasma-integration
Requires:	plasma-desktop >= %{version}
Requires:	plasma-framework
Requires:	plasma-vault
Requires:	plasma-browser-integration
Requires:	plasma-workspace >= %{version}
Requires:	kdeplasma-addons
Requires:	khotkeys
Requires:	kinfocenter >= 5.8.4
Requires:	kio-extras
Requires:	kmenuedit
Requires:	kscreen5
Requires:	kscreenlocker
Requires:	kservice
Requires:	ksshaskpass
Requires:	kwalletmanager
Requires:	kwrited
Requires:	phonon4qt5-backend
Requires:	plasma-pa
Requires:	powerdevil >= 5.8.4
Requires:	systemsettings
Requires:	solid
Requires:	polkit-kde-agent-1
Requires:	om-user-manager
Requires:	xdg-desktop-portal-kde
Requires:	distro-release-desktop
Suggests:	task-pulseaudio
Provides:	task-kde4-minimal = 1:4.14.4
Obsoletes:	task-kde4-minimal <= 1:4.14.3

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Plama 5 desktop environment.

%files minimal

#----------------------------------------------------------------------------

%package mobile-minimal
Summary:	Minimal set of packages for Plasma Mobile
Group:		Graphical desktop/KDE
# Basic
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
Requires:	plasma-pa
Requires:	plasma-integration
Requires:	plasma-desktop >= %{version}
Requires:	plasma-framework
Requires:	plasma-vault
Requires:	plasma-browser-integration
Requires:	plasma-workspace >= %{version}
# FIXME This should really be "Requires:", but as of
# 5.20.4, kscreenlocker on Plasma Mobile fails to unlock
# even if the password is supplied correctly.
# In the mean time, Plasma Mobile without lock screen is
# usable, so let's not block further testing on this...
#Conflicts:	kscreenlocker
Requires:	kservice
Requires:	ksshaskpass
Requires:	kwalletmanager
Requires:	phonon4qt5-backend
Requires:	qmlkonsole
Requires:	plasma-nm
Requires:	powerdevil >= 5.8.4
Requires:	solid
Requires:	polkit-kde-agent-1
Requires:	xdg-desktop-portal-kde
Requires:	milou
Requires:	kconfig

# FIXME at some point, we probably want to support plasma-mobile on X11
# as well...
Requires:	kwin-wayland >= %{version}
Requires:	qt5-qtwayland

# Key Plasma Mobile specific bits (stuff that is either
# required or active in the default config)
Requires:	plasma-mobile
Requires:	qt5-qtvirtualkeyboard
Requires:	kweather
Requires:	kclock
Requires:	angelfish
Requires:	plasma-settings
Requires:	distro-release-desktop
Suggests:	task-pulseaudio

%description mobile-minimal
This package is a meta-package, meaning that its purpose is to contain
a minimal version of the mobile version of the Plama 5 desktop environment.


%files mobile-minimal
#----------------------------------------------------------------------------

%package mobile
Summary:	Packages for Plasma Mobile
Group:		Graphical desktop/KDE
# Basic
Requires:	%{name}-mobile-minimal = %{EVRD}
Requires:	alligator
Requires:	spacebar
Requires:	maui-pix
Requires:	kaidan
Requires:	calindori
Requires:	keysmith
Requires:	kalk
Requires:	plasma-phonebook
#Requires:	plasma-camera
# plasma-camera is better, but doesn't work (yet) on
# PinePhone, so let's use a workaround for now
Suggests:	megapixels
Requires:	index-fm
Requires:	telegram-desktop
Requires:	qmlkonsole
Requires:	buho
Requires:	okular-mobile
Requires:	okular-pdf
Requires:	okular-postscript
Requires:	okular-epub
Requires:	okular-kimgio
Requires:	discover
Requires:	discover-backend-packagekit
Requires:	kscreen
Requires:	kmix
Requires:	plasma-pa
Requires:	vvave
Requires:	koko
Requires:	nota
Requires:	station
Requires:	communicator
Requires:	kube
Requires:	itinerary
Requires:	clip

%description mobile
This package is a meta-package, meaning that its purpose is to contain
the mobile version of the Plasma 5 desktop environment.

%files mobile
#----------------------------------------------------------------------------

%prep

%build

%install
