S = "${WORKDIR}"

SRC_URI = "file://env_path.sh"

do_install:append() {
        install -d ${D}${sysconfdir}/profile.d
	install -m 0644 ${S}/env_path.sh ${D}${sysconfdir}/profile.d/env_path.sh
}
