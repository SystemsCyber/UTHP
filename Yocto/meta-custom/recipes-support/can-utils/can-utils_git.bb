# Recipe created by recipetool
# This is the basis of a recipe and may need further editing in order to be fully functional.
# (Feel free to remove these comments when editing.)

# WARNING: the following LICENSE and LIC_FILES_CHKSUM values are best guesses - it is
# your responsibility to verify that the values are complete and correct.
#
# The following license files were not able to be identified and are
# represented as "Unknown" below, you will need to check them yourself:
#   LICENSES/GPL-2.0-only.txt
LICENSE = "Unknown"
LIC_FILES_CHKSUM = "file://LICENSES/GPL-2.0-only.txt;md5=f9d20a453221a1b7e32ae84694da2c37"

SRC_URI = "git://github.com/linux-can/can-utils.git;protocol=https;branch=master"

# Modify these as desired
PV = "1.0+git${SRCPV}"
SRCREV = "186bd967173a8a42ff544b5977edcda7c968c1aa"

S = "${WORKDIR}/git"

inherit cmake

# Specify any options you want to pass to cmake using EXTRA_OECMAKE:
EXTRA_OECMAKE = ""

# Override build directory if necessary
B = "${WORKDIR}/build"

do_configure() {
    cmake ${S} -DCMAKE_INSTALL_PREFIX=${D}
}

do_compile() {
    oe_runmake
}

do_install() {
    oe_runmake install
}

BBCLASSEXTEND = "native"
