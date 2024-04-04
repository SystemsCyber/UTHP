SUMMARY = "Adafruit DS1307 library for CircuitPython"
LICENSE = "CLOSED"
#LIC_FILES_CHKSUM = "file://LICENSE;md5=<checksum>"
BB_STRICT_CHECKSUM = "0"
SRC_URI = "git://github.com/adafruit/Adafruit_CircuitPython_DS1307.git;protocol=https;branch=main"
SRCREV = "2d22de4fc84100a0e7017a81b626d3cbf41d0490"
S = "${WORKDIR}/git"

inherit setuptools

DEPENDS += "python3"

do_install() {
    install -d ${D}${PYTHON_SITEPACKAGES_DIR}
    cp -r ${S}/adafruit_ds1307 ${D}${PYTHON_SITEPACKAGES_DIR}/
}

FILES_${PN} += "${PYTHON_SITEPACKAGES_DIR}/adafruit_ds1307"

