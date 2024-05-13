DESCRIPTION = "Utility to configure pin settings on BeagleBone boards"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${THISDIR}/LICENSE;md5=8fc4c790a2ea7081f1b5b3e809895a6d"

SRC_URI = "git://github.com/beagleboard/bb.org-overlays.git;protocol=https;rev=e851bfae934f300cf10cca695d29e16655cfa089;branch=master"

SRCREV = "e851bfae934f300cf10cca695d29e16655cfa089"

DEPENDS += "dtc-native"

RDEPENDS:${PN} += "dash"

S = "${WORKDIR}/git"

inherit allarch

do_compile() {
    oe_runmake
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${S}/tools/beaglebone-universal-io/config-pin ${D}${bindir}
}

FILES:${PN} += "${bindir}/config-pin"

