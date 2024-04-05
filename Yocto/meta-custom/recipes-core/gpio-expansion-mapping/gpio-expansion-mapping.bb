SUMMARY = "Startup script to map software GPIOs to expansion pins"
PV = "1.0.1"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://gpio-startup-script.sh \
           "

S = "${WORKDIR}"

inherit update-rc.d 

INITSCRIPT_NAME = "gpio-startup-script.sh"
INITSCRIPT_PARAMS = "defaults"

do_install() {
    install -d ${D}${sysconfdir}/init.d
    install -m 0755 ${S}/gpio-startup-script.sh ${D}${sysconfdir}/init.d/${INITSCRIPT_NAME}
}


