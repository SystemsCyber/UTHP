SUMMARY = "Safe Shutdown Recipe"
DESCRIPTION = "Recipe required to safely shutdown the BeagleBone Black in case of power loss"

LICENSE = "CLOSED"

SRC_URI = "file://safe-shutdown.service \
           file://safe-shutdown.sh"

do_install() {
    # Install the safe-shutdown script
    install -d ${D}/opt/scripts
    install -m 0755 ${WORKDIR}/safe-shutdown.sh ${D}/opt/scripts/

    # Install the systemd service file for the safe-shutdown script
    install -d ${D}${systemd_unitdir}/system
    install -m 0644 ${WORKDIR}/safe-shutdown.service ${D}${systemd_unitdir}/system/
}

FILES:${PN} += "/opt/scripts/safe-shutdown.sh \
                ${systemd_unitdir}/system/safe-shutdown.service"

RDEPENDS:${PN} = "systemd bash"

inherit systemd

SYSTEMD_SERVICE:${PN} = "safe-shutdown.service"
SYSTEMD_AUTO_ENABLE = "enable"