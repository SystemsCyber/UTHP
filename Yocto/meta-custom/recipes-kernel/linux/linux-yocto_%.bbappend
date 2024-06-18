# Set the KERNEL_DEFCONFIG variable to point to the custom configuration file
KERNEL_DEFCONFIG = "defconfig"
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI += "file://defconfig \ 
            file://0001-Added-D_CAN0-and-C_CAN1.patch"