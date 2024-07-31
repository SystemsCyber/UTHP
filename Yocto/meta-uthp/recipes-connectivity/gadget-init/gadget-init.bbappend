FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI:append = " file://network-gadget-init.service"

do_install:append() {
    install -d ${D}${base_libdir}/systemd/system/basic.target.wants
    install -m 0644 ${WORKDIR}/network-gadget-init.service ${D}${base_libdir}/systemd/system
    ln -sf ../network-gadget-init.service ${D}${base_libdir}/systemd/system/basic.target.wants/
}

# ensure the service is enabled
inherit systemd
SYSTEMD_SERVICE:${PN} = "network-gadget-init.service"
SYSTEMD_AUTO_ENABLE = "enable"