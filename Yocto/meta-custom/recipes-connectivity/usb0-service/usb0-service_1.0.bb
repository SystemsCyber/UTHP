DESCRIPTION = "Systemd service to set static IP for usb0"
LICENSE = "CLOSED"

SRC_URI = "file://usb0-static.service"

S = "${WORKDIR}"

do_install() {
    install -d ${D}/lib/systemd/system/
    install -m 0644 ${WORKDIR}/usb0-static.service ${D}/lib/systemd/system/
}


inherit systemd
FILES:${PN} += "/lib/systemd/system/usb0-static.service"

SYSTEMD_PACKAGES = "${PN}"
SYSTEMD_SERVICE:${PN} = "usb0-static.service"
