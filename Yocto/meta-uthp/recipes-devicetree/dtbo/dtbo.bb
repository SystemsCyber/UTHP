FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI += "file://BB-UTHP-DCAN.dtbo \
            file://MCP251xFD-SPI.dtbo"
LICENSE = "CLOSED"
FILES:${PN} += "*"

do_install() {
    install -d ${D}/opt/uthp/dtbo
    install -m 0644 ${WORKDIR}/BB-UTHP-DCAN.dtbo ${D}/opt/uthp/dtbo/
    install -m 0644 ${WORKDIR}/MCP251xFD-SPI.dtbo ${D}/opt/uthp/dtbo/
}

