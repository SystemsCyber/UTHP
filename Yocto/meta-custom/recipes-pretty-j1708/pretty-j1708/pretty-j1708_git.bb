# Recipe created by recipetool
# This is the basis of a recipe and may need further editing in order to be fully functional.
# (Feel free to remove these comments when editing.)

# WARNING: the following LICENSE and LIC_FILES_CHKSUM values are best guesses - it is
# your responsibility to verify that the values are complete and correct.
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=dff86395128c2d1dffad00b26678dfca"

SRC_URI = "git://github.com/ainfosec/pretty_j1587;protocol=https;branch=master"

# Modify these as desired
PV = "1.0+git${SRCPV}"
SRCREV = "31ac605d1c0dbcf4fde366e278d20382e3617476"

S = "${WORKDIR}/git"

do_install() {
    install -d ${D}/home/root/pretty-j1708
    cp -r ${S}/* ${D}/home/root/pretty-j1708/
}

FILES_${PN} += "/home/root/pretty-j1708"
