# Set the KERNEL_DEFCONFIG variable to point to the custom configuration file
KERNEL_DEFCONFIG = "defconfig"
FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"
SRC_URI += "file://defconfig"