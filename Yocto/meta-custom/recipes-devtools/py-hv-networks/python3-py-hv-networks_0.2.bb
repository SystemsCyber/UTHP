DESCRIPTION = "The package provides SAE J1939 support for Python developers"
SECTION = "devel/python"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${THISDIR}/LICENSE;md5=9cbb8e86b6798efc990e6ac9a33a8b14"

# Specify the source file location
SRC_URI = "git://github.com/TruckHacking/py-hv-networks.git;protocol=https;rev=3af73282a7748ad4507edfd2071e7f130b596898;branch=master"
SRC_URI[sha256sum] = "7c72341c6e872d9b9e10a681d77a407e8e2cf4e1b88a315e24bd82a938496ad2"

S = "${WORKDIR}/git"

# Assuming the use of poetry or a similar tool as the build backend
inherit setuptools3



