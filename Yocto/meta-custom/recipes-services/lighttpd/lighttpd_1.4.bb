DESCRIPTION = "Lightweight web server"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${THISDIR}/LICENSE;md5=9cbb8e86b6798efc990e6ac9a33a8b14"

SRC_URI = "git://github.com/lighttpd/lighttpd1.4.git;protocol=https;rev=4a7514e12ef4e294e4cd43eab8c552d7d9a97e0f;branch=master; \
	   file://lighttpd.conf \
   	   file://lighttpd.service"
SRC_URI[sha256sum] = "7c72341c6e872d9b9e10a681d77a407e8e2cf4e1b88a315e24bd82a938496ad2"

S = "${WORKDIR}/git"

inherit autotools pkgconfig systemd

# Add any extra dependencies needed for compilation
DEPENDS = "pcre zlib openssl autoconf-archive automake libtool autoconf-native automake-native libtool-native m4-native pcre2"

do_configure:prepend() {
    # Debugging output to verify the presence of configure.ac and current directory
    echo "Current working directory: ${PWD}"
    #ls -l ${S}
    WD_DIR="${PWD}"


    # Run autogen.sh if present
    if [ -f ${S}/autogen.sh ]; then
        echo "==== Going to source code to compile it"
        cd ${S}
        chmod +x autogen.sh
        ./autogen.sh
        echo "=====Done with autogen.sh"
	#./configure 
        echo "===== Done with configure\n====DOne Go back to Wordking Directory ${WD}"
    fi

    # Run autoreconf to generate configuration scripts
    autoreconf -fi
    #cd ${WD_DIR} 
}


# Optional: Running 'make check' to execute any tests, typically during do_compile or do_test
do_compile:prepend() {
    echo "++++++++Current working directory during compile: ${PWD}"
    ls -l ${S}
    ls -l ${B}
}

do_compile(){
    cd ${S}
    oe_runmake 
}

do_install() {
    cd ${S}
    oe_runmake 'DESTDIR=${D}' install
   
    install -d ${D}${sysconfdir}/lighttpd
    install -m 0644 ${WORKDIR}/lighttpd.conf ${D}${sysconfdir}/lighttpd/

    # configure startup settings
    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${WORKDIR}/lighttpd.service ${D}${systemd_system_unitdir}

    # Create log directory and set permissions
    install -d ${D}${localstatedir}/lighttpd
    chmod 0777 ${D}${localstatedir}/lighttpd
}

FILES:${PN} += "${sysconfdir}/lighttpd"
FILES:${PN} += "${bindir}/* ${sbindir}/* ${libdir}/* ${sysconfdir}/* ${localstatedir}/*"
FILES:${PN} += "${systemd_system_unitdir}"


SYSTEMD_AUTO_ENABLE = "enable"
SYSTEMD_SERVICE:${PN} = "lighttpd.service"

