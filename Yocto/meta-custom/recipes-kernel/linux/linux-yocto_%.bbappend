# Set the KERNEL_DEFCONFIG variable to point to the custom configuration file
KERNEL_DEFCONFIG = "defconfig"

FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI += "file://defconfig \
            file://0001-boneblack-uthp-changes.patch \
           "
