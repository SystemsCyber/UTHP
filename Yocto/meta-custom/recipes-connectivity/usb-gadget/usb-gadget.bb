DESCRIPTION = "USB Gadget Setup for BeagleBone Black"
LICENSE = "CLOSED"

SRC_URI = "file://bb-usb-gadgets.service \
           file://bb-start-usb-gadgets \
           file://bb-start-acm-ncm-rndis-old-gadget \
           file://bb-mac-addr \
           file://bb-setup-mac-address \
           file://bb-boot \
           file://bbb.io/"

S = "${WORKDIR}"

inherit systemd

do_install() {
    # install startup services
    install -d ${D}/lib/systemd/system/
    #install -m 0755 ${S}/usb-gadget.target ${D}/lib/systemd/system/ --> already used in another recipe
    install -m 0755 ${S}/bb-usb-gadgets.service ${D}/lib/systemd/system/
 
    # install binaries
    install -d ${D}/usr/bin/
    install -m 0755 ${S}/bb-start-usb-gadgets ${D}/usr/bin/
    install -m 0755 ${S}/bb-start-acm-ncm-rndis-old-gadget ${D}/usr/bin/

    # Conf file
    install -d ${D}/etc/default/
    install -m 0755 ${S}/bb-mac-addr ${D}/etc/default/
    install -m 0755 ${S}/bb-boot ${D}/etc/default/
    cp -r ${S}/bbb.io ${D}/etc/default/
    
}

SYSTEMD_AUTO_ENABLE = "enable"
SYSTEMD_SERVICE:${PN} = "bb-usb-gadgets.service"

FILES:${PN} += "/lib/systemd/system \
                /usr/bin \
		        /etc/default/bbb.io"

RDEPENDS:${PN} += "bash"
