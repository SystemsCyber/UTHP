# Set the KERNEL_DEFCONFIG variable to point to the custom configuration file
#
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI += "file://custom.cfg"

