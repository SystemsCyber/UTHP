DESCRIPTION = "Canmatrix is a python package to read and write several CAN (Controller Area Network) database formats"
SECTION = "devel/python"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${THISDIR}/LICENSE;md5=9cbb8e86b6798efc990e6ac9a33a8b14"

# Specify the source file location
SRC_URI = "git://github.com/ebroecker/canmatrix.git;protocol=https;rev=3d059da1ff3e4fb60ef8cbf4aebe85b2f5c970c1;branch=development"
SRC_URI[sha256sum] = "7c72341c6e872d9b9e10a681d77a407e8e2cf4e1b88a315e24bd82a938496ad2"

S = "${WORKDIR}/git"

inherit setuptools3
