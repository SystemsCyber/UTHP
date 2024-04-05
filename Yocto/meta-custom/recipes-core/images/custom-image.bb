SUMMARY = "UTHP Yocto Image"

IMAGE_INSTALL = "packagegroup-core-boot ${CORE_IMAGE_EXTRA_INSTALL}"
LICENSE = "MIT"

inherit core-image
inherit extrausers

# Set rooffs to ~4GB by default
IMAGE_OVERHEAD_FACTOR ?= "1.0"
IMAGE_ROOTFS_SIZE ?= "3872983"

IMAGE_INSTALL:append = " i2c-tools iproute2 sudo kernel-modules ntp can-utils usbinit libgpiod libgpiod-tools libgpiod-dev gpio-expansion-mapping \
                        python python3 python3-core python3-setuptools python3-ipython python3-ipython-genutils python3-venv python3-pip python3-scapy \
                        python3-bitstring python-importlib-metadata python-enum34 python-six python3-cmap \
                        python-attrs python-future python-typing python2.7-canmatrix python3-github-cancat"

# python3-fcntl python3-scapy python3-pip"
# python3-ipython-genutils" # ipython needs to be installed via pip or custom recipe

TIMEZONE = "America/Denver"
NTP_SERVERS = "pool.ntp.org"

# Add uthp user and set temp root password
EXTRA_USERS_PARAMS = "useradd uthp; \
	usermod -p '\$5\$nqWQ3Hm3qq0DiJIg\$eOzUIVEIdlQKKD64WMO6I8JirEeGzTPwCj13S.wgnQ8' uthp; \
    usermod -p '\$5\$nqWQ3Hm3qq0DiJIg\$eOzUIVEIdlQKKD64WMO6I8JirEeGzTPwCj13S.wgnQ8' root; \
    usermod -aG sudo uthp; \
	"

# Here we give sudo access to sudo members
update_sudoers(){
    sed -i 's/# %sudo/%sudo/' ${IMAGE_ROOTFS}/etc/sudoers
}

ROOTFS_POSTPROCESS_COMMAND += "update_sudoers;"