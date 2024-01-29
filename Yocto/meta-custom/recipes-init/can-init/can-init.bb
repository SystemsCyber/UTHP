LICENSE = "CLOSED"

FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI += "file://can-setup.sh"

do_install() {
    install -d ${D}${sysconfdir}/init.d
    install -m 0777 ${WORKDIR}/can-setup.sh ${D}${sysconfdir}/init.d/
}

pkg_postinst_${PN} () {
    if [ -z "$D" ]; then
        update-rc.d can-setup.sh defaults
    fi
}
