FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI += "file://modify_profile.sh"

do_install:append() {
    install -d ${D}${sysconfdir}/profile.d
    install -m 0644 ${WORKDIR}/modify_profile.sh ${D}${sysconfdir}/profile.d/modify_profile.sh
}