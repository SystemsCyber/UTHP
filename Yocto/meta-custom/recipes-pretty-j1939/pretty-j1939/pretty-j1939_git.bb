# Recipe created by recipetool
# This is the basis of a recipe and may need further editing in order to be fully functional.
# (Feel free to remove these comments when editing.)

SUMMARY = "python libs and scripts for pretty-printing J1939 logs"
HOMEPAGE = "https://github.com/nmfta-repo/pretty_j1939"
# WARNING: the following LICENSE and LIC_FILES_CHKSUM values are best guesses - it is
# your responsibility to verify that the values are complete and correct.
# NOTE: Original package / source metadata indicates license is: None
#
# NOTE: multiple licenses have been detected; they have been separated with &
# in the LICENSE value for now since it is a reasonable assumption that all
# of the licenses apply. If instead there is a choice between the multiple
# licenses then you should change the value to separate the licenses with |
# instead of &. If there is any doubt, check the accompanying documentation
# to determine which situation is applicable.
LICENSE = "Apache-2.0 & None"
LIC_FILES_CHKSUM = "file://LICENSE;md5=86d3f3a95c324c9479bd8986968f4327"

SRC_URI = "git://github.com/nmfta-repo/pretty_j1939;protocol=https;branch=master"

# Modify these as desired
PV = "0.0.2+git${SRCPV}"
SRCREV = "199431af9e837f299b171c5a71e3d051ad811e1b"

S = "${WORKDIR}/git"

inherit setuptools3


do_install() {
    install -d ${D}/home/root/pretty-j1939
    cp -r ${S}/* ${D}/home/root/pretty-j1939/
}

FILES_${PN} += "/home/root/pretty-j1939"
# WARNING: the following rdepends are determined through basic analysis of the
# python sources, and might not be 100% accurate.
#RDEPENDS:${PN} += "python3-core python3-json"

# WARNING: We were unable to map the following python package/module
# dependencies to the bitbake packages which include them:
#    asteval
#    bitstring
#    defusedxml
#    defusedxml.common
#    unidecode
#    xlrd
