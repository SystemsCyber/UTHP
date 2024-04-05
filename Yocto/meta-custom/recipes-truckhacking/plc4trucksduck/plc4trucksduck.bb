DESCRIPTION = "PLC writing tool for the Truck Duck, a BeagleBone-based diagnostic tool for heavy vehicles."
HOMEPAGE = "https://github.com/TruckHacking"
PV = "1.0.1"
SECTION = "extras"
LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://${THISDIR}/MIT;md5=9cbb8e86b6798efc990e6ac9a33a8b14"

SRC_URI = " \
    http://downloads.ti.com/codegen/esd/cgt_public_sw/PRU/2.1.1/ti_cgt_pru_2.1.1_armlinuxa8hf_busybox_installer.sh;name=pruccompiler;subdir=${PN} \
    git://git.ti.com/cgit/pru-software-support-package/pru-software-support-package;protocol=https;branch=master;destsuffix=${PN}/pru-ssp;rev=d09576fa217feb446c53a95fed65b2f7db3130aa \
    file://requirements-2.7.txt \
    file://requirements.txt \
"
SRC_URI[pruccompiler.sha256sum] = "819a4680296fabf1ae0d4e0184276f8ab5324621d35388026d1b678ea71040c9"

do_compile() {
    # Custom compilation steps here
    oe_runmake
}
