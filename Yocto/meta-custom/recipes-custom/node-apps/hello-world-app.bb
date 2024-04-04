DESCRIPTION = "Hello World Express.js application"
SECTION = "examples"
LICENSE = "CLOSED"
#LIC_FILES_CHKSUM = "file://LICENSE;md5=efb5758738aa6e637be212c2cd2d013c"

SRC_URI = "file://app.js \
           file://package.json \
           file://package-lock.json \
           file://bom_spdx.json \
          "
inherit npm

S = "${WORKDIR}"

do-compile(){
   npm install
}

do_install() {
    install -d ${D}${libdir}/node_modules/hello-world-express
    cp -r ${S}/app.js ${S}/package.json ${S}/package-lock.json ${S}/bom_spdx.json ${D}${libdir}/node_modules/hello-world-express
}

FILES_${PN} += "${libdir}/node_modules/hello-world-express"
