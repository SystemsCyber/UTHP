DESCRIPTION = "PLC4TRUCKSDUCK installation for BeagleBone Black"
LICENSE = "CLOSED"

# Depend on wget, git, make, and Python
DEPENDS = "wget git-native make python3 python3-pip"

SRC_URI = " \
	http://downloads.ti.com/codegen/esd/cgt_public_sw/PRU/2.1.1/ti_cgt_pru_2.1.1_armlinuxa8hf_busybox_installer.sh;downloadfilename=ti_cgt_pru_installer.sh \
	file://requirements-2.7.txt \
        file://requirements.txt \
"
SRC_URI[md5sum] = "3b97df4966715bdb50f9a9fc58fe6b24"
SRC_URI[sha256sum] = "819a4680296fabf1ae0d4e0184276f8ab5324621d35388026d1b678ea71040c9"
S = "${WORKDIR}"

#do_fetch() {
#    bb.build.exec_func('base_do_fetch', d)
#}


do_compile() {
    echo "Installation directory: ${D}/usr/share/ti/cgt-pru"
    # Install the TI PRU C Compiler
    bash '${WORKDIR}/ti_cgt_pru_installer.sh' --prefix=${D}/usr/share/ti/cgt-pru

    # Clone PRU Software Support Package
    cd ${D}/opt
    git clone https://git.ti.com/cgit/pru-software-support-package/pru-software-support-package/
    
    # Set environment variables if needed
    export PRU_CGT=/usr/share/ti/cgt-pru
    export PRU_SUPPORT=${D}/opt/pru-software-support-package
    
    # Compile PRU binaries and device tree overlays
    oe_runmake
}

do_install() {
    # Install Python dependencies
    pip3 install -r ${WORKDIR}/requirements.txt
    pip2 install -r ${WORKDIR}/requirements-2.7.txt
    
    # Run make install to install services and disable old ones
    oe_runmake install
    
    # Additional configuration for the system
    # You may need to write or append scripts or system service files here
}

FILES:${PN} += "/usr/share/ti/cgt-pru \
                /opt/pru-software-support-package"

