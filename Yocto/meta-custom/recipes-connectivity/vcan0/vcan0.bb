DESCRIPTION = "Setup vcan0 at boot using systemd service"
LICENSE = "CLOSED"


SRC_URI = "file://setup_vcan.sh \
           file://vcan0.service"

S = "${WORKDIR}"
inherit systemd
do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${WORKDIR}/setup_vcan.sh ${D}${bindir}/setup_vcan.sh

    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${WORKDIR}/vcan0.service ${D}${systemd_system_unitdir}/vcan0.service
}

FILES:${PN} += "${systemd_system_unitdir}/*"
SYSTEMD_AUTO_ENABLE = "enable"
SYSTEMD_SERVICE:${PN} = "vcan0.service"

