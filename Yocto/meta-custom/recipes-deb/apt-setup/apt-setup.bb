FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI += "file://sources.list \
            https://repos.rcn-ee.net/debian/conf/repos.rcn-ee.net.gpg.key;sha256sum=8c21e1af012d8697ccfdd0110a1d2d26a764d47bbd5651359b4eaac328338880"
LICENSE = "CLOSED"

FILES:${PN} += "/usr/share/keyrings/repos.rcn-ee.net.gpg"
FILES:${PN} += "${sysconfdir}/apt/sources.list"

do_install() {
    install -d ${D}${sysconfdir}/apt/
    install -m 0644 ${WORKDIR}/sources.list ${D}${sysconfdir}/apt/sources.list

    # create /usr/share/keyrings
    install -d ${D}/usr/share/keyrings 
    install -m 0644 ${WORKDIR}/repos.rcn-ee.net.gpg.key ${D}/usr/share/keyrings/repos.rcn-ee.net.gpg
}

pkg_postinst_apt-setup() {
    rsync -az --progress keyring.debian.org::keyrings/keyrings/ ${D}/usr/share/keyrings/
    chmod 644 ${D}/usr/share/keyrings/*
}
