DESCRIPTION = "Express Application Serving an SPA"
LICENSE = "CLOSED"

SRC_URI = "file://app.js \
           file://package.json \
           file://package-lock.json \
           file://controller/ \
           file://public/ \
           file://views/ \
           file://postcss.config.js \
           file://tailwind.config.js \
           file://express.service"

S = "${WORKDIR}"

# Add the inheritance for npm-related functions provided by meta-nodejs or a similar layer
inherit npm 
#DEPENDS += "nodejs-native"
#RDEPENDS:${PN} += "nodejs"

# Override do_configure and do_compile to do nothing
do_configure() {
    :
}

do_compile() {
    :
}

do_install() {
    install -d ${D}${libdir}/node/${PN}
    #cp -R ${S}/* ${D}${libdir}/node/${PN}/
    install -m 0655 ${S}/app.js ${D}${libdir}/node/${PN}/
    install -m 0655 ${S}/package.json ${D}${libdir}/node/${PN}/
    install -m 0655 ${S}/package-lock.json ${D}${libdir}/node/${PN}/
    cp -r ${S}/controller/ ${D}${libdir}/node/${PN}/
    cp -r ${S}/public/ ${D}${libdir}/node/${PN}/
    cp -r ${S}/views/ ${D}${libdir}/node/${PN}/
    install -m 0655 ${S}/postcss.config.js ${D}${libdir}/node/${PN}/
    install -m 0655 ${S}/tailwind.config.js ${D}${libdir}/node/${PN}/

    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${S}/express.service ${D}${systemd_system_unitdir}/
}

do_install:append() {
    cd ${S}
    npm install --production --prefix=${D}${libdir}/node/${PN}/
    chown -R root:root ${D}${libdir}/node/${PN}/
}

RDEPENDS:${PN} = "nodejs"

FILES:${PN} += "${libdir}/node/${PN} \
		/lib/systemd/system"

SYSTEMD_AUTO_ENABLE = "enable"
SYSTEMD_SERVICE:${PN} = "express.service"
