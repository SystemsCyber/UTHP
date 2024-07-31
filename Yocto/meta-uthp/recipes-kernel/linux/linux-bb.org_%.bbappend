# Set the KERNEL_DEFCONFIG variable to point to the custom configuration file
# removed: KERNEL_DEFCONFIG = "defconfig"; removed: file://0001-UTHPKv0.0.patch; removed: file://0001-UTHP-TESTING.patch
            
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI += "file://0001-UTHPKv0.0.patch"

# Set the COMPATIBLE_MACHINE variable to include the UTHP
COMPATIBLE_MACHINE = "uthp"
