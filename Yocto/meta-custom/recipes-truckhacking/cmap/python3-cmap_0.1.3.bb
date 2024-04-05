DESCRIPTION = "Scientific colormaps for python, with no dependencies beyond numpy"
SECTION = "devel/python"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${THISDIR}/LICENSE;md5=9cbb8e86b6798efc990e6ac9a33a8b14"

# Specify the source file location
SRC_URI = "file://cmap-0.1.3.tar.gz"

S = "${WORKDIR}/cmap-0.1.3"

# Assuming the use of poetry or a similar tool as the build backend
inherit setuptools3

# Skip the standard Python setup.py configuration phase
#do_configure() {
#    # Use the backend tool to configure if necessary
#    # e.g., poetry install or custom configuration commands
#}

do_compile() {
    # Build the package using the backend specified in pyproject.toml
    # This command depends on the build system used by the package
    #oe_runmake # or custom build command, e.g., poetry build
    echo "++++++++++++++++++++++++ No compile necesary"
}

do_install() {
    # Install the package into the appropriate location
    # Adjust these commands based on the actual build backend and file structure
    install -d ${D}${libdir}/python${PYTHON_BASEVERSION}/site-packages/cmap
    cp -r ${S}/src/cmap ${D}${libdir}/python${PYTHON_BASEVERSION}/site-packages/cmap
    # Repeat for other directories and files as necessary
}

