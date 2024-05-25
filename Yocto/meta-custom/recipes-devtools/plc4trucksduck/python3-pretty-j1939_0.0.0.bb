DESCRIPTION = "python libs and scripts for pretty-printing J1939 logs"
SECTION = "devel/python"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${THISDIR}/LICENSE;md5=9cbb8e86b6798efc990e6ac9a33a8b14"

# Specify the source file location
#git://github.com/atlas0fd00m/CanCat.git
SRC_URI = "git://github.com/nmfta-repo/pretty_j1939.git;protocol=https;rev=199431af9e837f299b171c5a71e3d051ad811e1b;branch=master"
SRC_URI[sha256sum] = "7c72341c6e872d9b9e10a681d77a407e8e2cf4e1b88a315e24bd82a938496ad2"

S = "${WORKDIR}/git"

# Assuming the use of poetry or a similar tool as the build backend
inherit setuptools3

#do_compile() {
#    # Build the package using the backend specified in pyproject.toml
#    # This command depends on the build system used by the package
#    #oe_runmake # or custom build command, e.g., poetry build
#    echo "++++++++++++++++++++++++ No compile necesary"
#}

#do_install() {
#    # Install the package into the appropriate location
#    # Adjust these commands based on the actual build backend and file structure
#    install -d ${D}${libdir}/python${PYTHON_BASEVERSION}/site-packages/cmap
#    cp -r ${S}/src/cmap ${D}${libdir}/python${PYTHON_BASEVERSION}/site-packages/cmap
#    # Repeat for other directories and files as necessary
#}


