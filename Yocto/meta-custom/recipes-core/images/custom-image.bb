SUMMARY = "UTHP Yocto Image"

IMAGE_INSTALL = "packagegroup-core-boot ${CORE_IMAGE_EXTRA_INSTALL}"
LICENSE = "MIT"

inherit core-image
inherit extrausers

IMAGE_FEATURES += "package-management"
IMAGE_LINGUAS = "en-us"

# Set rooffs to ~4GB by default TODO: make this dynamic
IMAGE_OVERHEAD_FACTOR ?= "1.0"
IMAGE_ROOTFS_SIZE ?= "3872983"

CORE_OS = " \
    openssh openssh-keygen openssh-sftp-server \
    sudo \
    libgpiod libgpiod-tools libgpiod-dev gpio-expansion-mapping \
    usbutils \
 "

KERNEL_EXTRA_INSTALL = " \
    kernel-modules \
    usb-gadget \
    usb0-dhcp \
    vcan0 \
 "

DEV_SDK_INSTALL = " \
    binutils \
    binutils-symlinks \
    coreutils \
    cpp \
    cpp-symlinks \
    diffutils \
    file \
    gcc \
    gcc-symlinks \
    g++ \
    g++-symlinks \
    gettext \
    git \
    ldd \
    libstdc++ \
    libstdc++-dev \
    libtool \
    make \
    perl-modules \
    pkgconfig \
 "

DEV_EXTRAS = " \
    ntp \
    ntp-tickadj \
 "

EXTRA_TOOLS_INSTALL = " \
    bc \
    bzip2 \
    devmem2 \
    dosfstools \
    ethtool \
    findutils \
    i2c-tools \
    iftop \
    htop \
    less \
    nano \
    procps \
    rsync \
    rtl-sdr \
    sysfsutils \
    tcpdump \
    tmux \
    unzip \
    util-linux \
    wget \
    zip \
 "

CAN_TOOLS = " \
    can-utils \
    libsocketcan \
    libsocketcan-dev \
    iproute2 \
    sigrok-cli \
    can2 \
    truckdevil \
    config-pin \
 "

PREFERRED_VERSION_python = "2.7"
PYTHON_TOOLS = " \
    python \
    python-modules \
    python-importlib-metadata \
    python-enum34 \
    python-six \
    python-attrs \
    python-typing \
 "

PYTHON3_TOOLS = " \
    python3 \
    python3-core \
    python3-setuptools \
    python3-pip \
    python3-bitstring \
    python3-jupyter \
    python3-scapy \
    python3-can \
    python3-cantools \
    python3-six \
    python3-cancat \
    python3-canmatrix \
    python3-cmap \
    python3-future \
    python3-pretty-j1939 \
    python3-pretty-j1587 \
    python3-sae-j1939 \
    python3-jsonschema \
    python3-nest-asyncio \
    python3-numpy \
    python3-pyserial \
    python3-termcolor \
    python3-attrs \
    python3-typing-extensions \
    python3-py-hv-networks \
    python3-flask \
    python3-websockets \
    python3-dev \
    python3-asyncio-glib \
    pamela \
 "

NET_SERVICES = " \
    lighttpd \
    uthp-app-api \ 
    uthp-app-ui \
"



IMAGE_INSTALL += " \
    ${CAN_TOOLS} \
    ${CORE_OS} \
    ${DEV_SDK_INSTALL} \
    ${DEV_EXTRAS} \
    ${EXTRA_TOOLS_INSTALL} \
    ${KERNEL_EXTRA_INSTALL} \
    ${PYTHON_TOOLS} \
    ${PYTHON3_TOOLS} \
    ${NET_SERVICES} \
 "
CORE_IMAGE_EXTRA_INSTALL += "usbinit"

# FIXME: scapy six issues?

TIMEZONE = "America/Denver"
NTP_SERVERS = "pool.ntp.org"

# Add uthp user and set temp root password
EXTRA_USERS_PARAMS = "useradd uthp; \
	usermod -p '\$5\$Nx2D0wB1k15\$LYl7n9Tvtwo0fmsbs/frfpm7OuDJj2AIvcdWZfhS99C' uthp; \
    usermod -p '\$5\$Nx2D0wB1k15\$LYl7n9Tvtwo0fmsbs/frfpm7OuDJj2AIvcdWZfhS99C' root; \
    usermod -aG sudo uthp; \
	"

# Here we give sudo access to sudo members
update_sudoers(){
    sed -i 's/# %sudo/%sudo/' ${IMAGE_ROOTFS}/etc/sudoers
}

disable_bootlogd() {
    echo BOOTLOGD_ENABLE=no > ${IMAGE_ROOTFS}/etc/default/bootlogd
}

set_local_timezone() {
    ln -sf /usr/share/zoneinfo/EST5EDT ${IMAGE_ROOTFS}/etc/localtime
}

ROOTFS_POSTPROCESS_COMMAND += "update_sudoers; \
    set_local_timezone; \
    disable_bootlogd; \
    "


export IMAGE_BASENAME = "uthp"
