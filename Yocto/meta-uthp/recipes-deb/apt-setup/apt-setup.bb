FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI += "file://sources.list \
            https://ftp-master.debian.org/keys/archive-key-12-security.asc;sha256sum=74f81645b4e3156d1e9a88c8dd9259271b89c7099d64af89a2a6996b592faa1f \
            https://ftp-master.debian.org/keys/archive-key-12.asc;sha256sum=c2a9a16fde95e037bafd0fa6b7e31f41b4ff1e85851de5558f19a2a2f0e955e2"

LICENSE = "CLOSED"

FILES:${PN} += "*"

do_install() {
    install -d ${D}${sysconfdir}/apt/
    install -m 0644 ${WORKDIR}/sources.list ${D}${sysconfdir}/apt/sources.list

    install -d ${D}/usr/share/keyrings/
    install -m 0644 ${WORKDIR}/*.asc ${D}/usr/share/keyrings/
    # then in trusted.gpg.d
    install -d ${D}${sysconfdir}/apt/trusted.gpg.d/
    install -m 0644 ${WORKDIR}/*.asc ${D}${sysconfdir}/apt/trusted.gpg.d/
}