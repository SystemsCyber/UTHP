DESCRIPTION = "JupyterLab"
LICENSE = "CLOSED"
# LIC_FILES_CHKSUM = "<checksum-of-jupyterlab-license>"

inherit pypi setuptools

SRC_URI = "https://files.pythonhosted.org/packages/a7/56/6c5a78e860c6f09f91aca5ae5577dd6b68da9ac7596ac5877e627365e425/jupyterlab-4.1.5.tar.gz"
SRC_URI[md5sum] = "e2473440775803c2d831c796364b2133"
SRC_URI[sha256sum] = "c9ad75290cb10bfaff3624bf3fbb852319b4cce4c456613f8ebbaa98d03524db"

S = "${WORKDIR}/jupyterlab-4.1.5"


PYPI_PACKAGE = "jupyterlab"

RDEPENDS:${PN} += " \
    python3-core \
    python3-pip \
"

do_install:append() {
    oe_runpip install jupyterlab
    # If necessary, add PATH adjustment commands here
}

