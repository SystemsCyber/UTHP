# Recipe created by recipetool
# This is the basis of a recipe and may need further editing in order to be fully functional.
# (Feel free to remove these comments when editing.)

SUMMARY = "SAE J1939 stack implementation"
HOMEPAGE = "https://github.com/juergenH87/python-can-j1939"
# WARNING: the following LICENSE and LIC_FILES_CHKSUM values are best guesses - it is
# your responsibility to verify that the values are complete and correct.
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=8f86157104a2f8879e96acbeffbb0ffd"

SRC_URI = "git://github.com/juergenH87/python-can-j1939;protocol=https;branch=master"

# Modify these as desired
PV = "1.0+git${SRCPV}"
SRCREV = "df8f694aefa9581428d9d70cceff6c05df890fcb"

S = "${WORKDIR}/git"

#inherit setuptools3

do_install() {
    install -d ${D}/home/root/python-can-j1939
    cp -r ${S}/* ${D}/home/root/python-can-j1939/
}

FILES_${PN} += "/home/root/python-can-j1939"

# WARNING: the following rdepends are from setuptools install_requires. These
# upstream names may not correspond exactly to bitbake package names.
#RDEPENDS:${PN} += "python3-numpy python3-pytest python3-python-can"

# WARNING: the following rdepends are determined through basic analysis of the
# python sources, and might not be 100% accurate.
#RDEPENDS:${PN} += "python3-core python3-logging python3-netclient python3-threading"

# WARNING: We were unable to map the following python package/module
# dependencies to the bitbake packages which include them:
#    can
#    pythoncom
