FILESEXTRAPATHS:prepend := "${THISDIR}/files:"
SRC_URI:append = " \
    file://your-custom-can.dts \
"

do_configure:append(){
 cp ${WORKDIR}/*.dt* ${S}/arch/arm/boot/dts
 echo 'dtb-$(CONFIG_SOC_AM33XX) += mycustom.dtb' >> ${S}/arch/arm/boot/dts/Makefile
}
