# Recipe created by recipetool
# This is the basis of a recipe and may need further editing in order to be fully functional.
# (Feel free to remove these comments when editing.)

# WARNING: the following LICENSE and LIC_FILES_CHKSUM values are best guesses - it is
# your responsibility to verify that the values are complete and correct.
#
# The following license files were not able to be identified and are
# represented as "Unknown" below, you will need to check them yourself:
#   venv/Lib/site-packages/aenum/LICENSE
#   venv/Lib/site-packages/windows_curses-2.1.0.dist-info/LICENSE
#
# NOTE: multiple licenses have been detected; they have been separated with &
# in the LICENSE value for now since it is a reasonable assumption that all
# of the licenses apply. If instead there is a choice between the multiple
# licenses then you should change the value to separate the licenses with |
# instead of &. If there is any doubt, check the accompanying documentation
# to determine which situation is applicable.
DESCRIPTION = "Cmap - CAN Mapping and Configuration"
HOMEPAGE = "https://github.com/CanBusHack/cmap"
LICENSE = "CLOSED" 
LIC_FILES_CHKSUM = ""

SRC_URI = "git://github.com/CanBusHack/cmap;protocol=https;branch=master"

# Modify these as desired
PV = "1.0+git${SRCPV}"
SRCREV = "cb3cf1d29e1d99fb9f4fa863f7246c0df4d9c920"

S = "${WORKDIR}/git"

# NOTE: no Makefile found, unable to determine what needs to be done
do_install() {
    install -d ${D}/home/root/cmap
    cp -r ${S}/* ${D}/home/root/cmap
}

# Since this is a Python script, we might not need to compile anything
do_compile() {
    :
}

FILES_${PN} += "/home/root/cmap"
