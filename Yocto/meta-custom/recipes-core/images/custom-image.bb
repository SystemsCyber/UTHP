SUMMARY = "UTHP Yocto Image"

IMAGE_INSTALL = "packagegroup-core-boot ${CORE_IMAGE_EXTRA_INSTALL}"
LICENSE = "MIT"

inherit core-image
inherit extrausers

# Set rooffs to 2000 MiB by default
IMAGE_OVERHEAD_FACTOR ?= "1.0"
IMAGE_ROOTFS_SIZE ?= "204800"

IMAGE_INSTALL:append = " i2c-tools iproute2 sudo can-utils usbinit python3-core"
# python3-pip python3-fcntl python3-scapy python3-ipython python3-ipython_genutils kernel-modules"

EXTRA_IMAGE_FEATURES = "debug-tweaks"

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