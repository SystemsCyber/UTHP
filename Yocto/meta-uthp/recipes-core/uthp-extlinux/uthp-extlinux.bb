SUMMARY = "Custom extlinux.conf for the UTHP"
DESCRIPTION = "A custom extlinux.conf file for the bootloader"
LICENSE = "CLOSED"

SRC_URI = "file://extlinux.conf"

S = "${WORKDIR}"

do_deploy() {
    install -d ${DEPLOY_DIR_IMAGE}/extlinux
    install -m 0644 ${WORKDIR}/extlinux.conf ${DEPLOY_DIR_IMAGE}/extlinux/extlinux.conf
}

addtask deploy after do_install
