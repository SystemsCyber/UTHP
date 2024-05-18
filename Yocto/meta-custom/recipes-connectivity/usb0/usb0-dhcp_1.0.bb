DESCRIPTION = "Systemd networkd DHCP to set static IP for usb0"
LICENSE = "CLOSED"

SRC_URI = "file://usb0.network"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${sysconfdir}/systemd/network/
    install -m 0644 ${WORKDIR}/usb0.network ${D}${sysconfdir}/systemd/network/
}


FILES:${PN} += "${sysconfdir}/systemd/network/usb0.network"
