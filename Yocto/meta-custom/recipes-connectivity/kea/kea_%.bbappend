FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append = " \
    file://kea-custom-config.conf \
    "

# Enable kea-dhcp4 service at boot
SYSTEMD_AUTO_ENABLE = "enable"

do_install:append() {
    install -d ${D}${sysconfdir}/kea
    install -m 0644 ${WORKDIR}/kea-custom-config.conf ${D}${sysconfdir}/kea/kea-dhcp4.conf
}

