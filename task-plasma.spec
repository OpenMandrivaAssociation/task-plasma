Summary:	Metapackage for Plasma 5
Name:		task-plasma
Version:	5.6.3
Release:	0.1
License:	GPLv2+
Group:		Graphical desktop/KDE
Requires:	task-plasma-minimal >= %{version}
Requires:	distro-plasma-config
Requires:	openmandriva-kde-icons
%ifnarch %{armx}
Requires:	grub2-editor
%endif
Requires:	bluedevil5
Requires:	kwayland
# (tpg) needs to be updated to KF5
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
Requires:	kdenetwork-strigi-analyzers
Requires:	kidentitymanagement
Requires:	kremotecontrol
Requires:	zeroconf-ioslave
Requires:	kaccessible
Requires:	jovie
Requires:	kdeconnect
Requires:	kdegraphics-thumbnailers
Requires:	kget
# (tpg) kdepim
Requires:	akonadi-kde
Requires:	akonadi-archivemail-agent
Requires:	akonadi-followupreminder-agent
Requires:	akonadi-mailfilter-agent
Requires:	akonadi-notes-agent
Requires:	akonadi-sendlater-agent
Requires:	akonadi-search
Requires:	akonadi-social-utils-data
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
Requires:	akregator
Requires:	contactthemeeditor
Requires:	headerthemeeditor
Requires:	kdepim-accountwizard
Requires:	kincidenceeditor
# end pim
Requires:	kdepasswd
Requires:	ksystemlog
Requires:	krdc
Requires:	kremotecontrol
Requires:	kdenlive
Requires:	kamera
Requires:	kcalc
Requires:	kate
Requires:	kdf
Requires:	kgamma5
Requires:	kwrite
Requires:	konversation
Requires:	spectacle
Requires:	ksaneplugin
Requires:	kipi-plugins
Requires:	krfb
Requires:	kwalletmanager
Requires:	kwallet-pam
Requires:	kuser
# (tpg) needs to be ported to KF5
Requires:	okular
Requires:	sonnet-hunspell
Requires:	speech-dispatcher
Requires:	myspell-en_GB
Requires:	sddm
Requires:	sddm-kcm
Requires:	sddm-theme-breeze
# (tpg) very experimental systray for Plasma
Requires:	simplesystray
Requires:	skanlite
Requires:	systemd-kcm
Requires:	discover
Requires:	khelpcenter
Requires:	plasma-mediacenter
Requires:	partitionmanager
# (tpg) we have our own wallpapers :)
#Requires:	plasma-workspace-wallpapers
Requires:	discover-notifier
Requires:	print-manager
Requires:	skrooge
Requires:	user-manager
Requires:	xscreensaver
Suggests:	yakuake
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
Requires:	oxygen-fonts
Requires:	oxygen-icons
Requires:	sni-qt
Suggests:	task-pulseaudio
Requires:	task-x11
Requires:	xsettings-kde
Requires:	ark
Requires:	dolphin
Requires:	gwenview
Requires:	kde-l10n-en_GB
Requires:	pinentry-qt5

# Plasma 5
Requires:	breeze
Requires:	breeze-icons
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
Requires:	kinfocenter5
Requires:	kio-extras
Requires:	kmenuedit
Requires:	konsole
Requires:	kscreen5
Requires:	kscreenlocker
Requires:	kservice
Requires:	ksysguard
Requires:	ksshaskpass
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

