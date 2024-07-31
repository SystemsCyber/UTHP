DESCRIPTION = "This is a tool for getting detailed decodings of J1587/J1708 (and J2497) messages using the J1587 and J1708 specification PDFs as a reference"
SECTION = "devel/python"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${THISDIR}/LICENSE;md5=9cbb8e86b6798efc990e6ac9a33a8b14"

# Specify the source file location
SRC_URI = "git://github.com/ainfosec/pretty_j1587.git;protocol=https;rev=31ac605d1c0dbcf4fde366e278d20382e3617476;branch=master"
SRC_URI[sha256sum] = "7c72341c6e872d9b9e10a681d77a407e8e2cf4e1b88a315e24bd82a938496ad2"

S = "${WORKDIR}/git"

# Assuming the use of poetry or a similar tool as the build backend
inherit setuptools3
RDEPENDS:${PN} += "perl python python3"

do_compile() {
    # Build the package using the backend specified in pyproject.toml
    # This command depends on the build system used by the package
    #oe_runmake # or custom build command, e.g., poetry build
    echo "++++++++++++++++++++++++ No compile necesary"
}

do_install() {
    # Install executable files
    install -d ${D}${sbindir}
    install -m 0755 ${S}/pretty_j1587.py ${D}${sbindir}/pretty_j1587.py
    install -m 0755 ${S}/fuzzymessages.py ${D}${sbindir}/fuzzymessages.py

    # Rest of the files dump into the /etc/pretty_1587
    install -d ${D}${sysconfdir}/pretty_1587
    install -m 0644 ${S}/canon_functions.py ${D}${sysconfdir}/pretty_1587/canon_functions.py
    install -m 0644 ${S}/config.cfg ${D}${sysconfdir}/pretty_1587/config.cfg
    install -m 0644 ${S}/LICENSE ${D}${sysconfdir}/pretty_1587/LICENSE
    install -m 0644 ${S}/README.md ${D}${sysconfdir}/pretty_1587/README.md
    install -m 0644 ${S}/requirements.txt ${D}${sysconfdir}/pretty_1587/requirements.txt
    install -m 0644 ${S}/samplejson.def ${D}${sysconfdir}/pretty_1587/samplejson.def
    install -m 0644 ${S}/struct_from_J1587.py ${D}${sysconfdir}/pretty_1587/struct_from_J1587.py
    install -m 0644 ${S}/test_pretty_j1587.py ${D}${sysconfdir}/pretty_1587/test_pretty_j1587.py
    # Repeat for other directories and files as necessary
}


