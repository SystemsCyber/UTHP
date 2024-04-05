DESCRIPTION = "Python library for GPIO access on the BeagleBone Black"
HOMEPAGE = "https://github.com/adafruit/adafruit-beaglebone-io-python"
SECTION = "devel/python"
LICENSE = "CLOSED"
#LIC_FILES_CHKSUM = "file://LICENSE;md5=51a03ecd43cdc00dbac467a7f89e2069"
BB_STRICT_CHECKSUM = "0"
SRC_URI = "git://github.com/adafruit/adafruit-beaglebone-io-python.git;protocol=https;branch=master"
#SRC_URI[sha256sum] = "061aa12c6118b168194b614405cc60b0574aecd533d7be9e12ceab4d02fe47c1"
SRCREV = "cf306ed7f9f24111d0949dd60ac232e81241bffe"

S = "${WORKDIR}/git"

inherit setuptools3

RDEPENDS:${PN} += "python3-core python3-misc"

do_compile:prepend() {
    sed -i 's|/usr/local/|${prefix}/|g' setup.py
}

BBCLASSEXTEND = "native nativesdk"
