DESCRIPTION = "Flask web api"
SECTION = "application"
LICENSE = "CLOSED"

DEPENDS = "python3-flask"

SRC_URI = "file://uthp-app/app.py \
           file://uthp-app.service \
          "
inherit systemd

S = "${WORKDIR}/uthp-app"

do_install() {
    # Install the web application
    install -d ${D}${libdir}/python3.8/site-packages/uthp-app
    install -m 0644 ${S}/app.py ${D}${libdir}/python3.8/site-packages/uthp-app

    # Setup the service
    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${WORKDIR}/uthp-app.service ${D}${systemd_system_unitdir}

}

FILES:${PN} += "${libdir}/python3.8/site-packages/uthp-app"
SYSTEMD_AUTO_ENABLE = "enable"
SYSTEMD_SERVICE:${PN} = "uthp-app.service"
