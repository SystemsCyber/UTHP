# Recipe created by recipetool
# This is the basis of a recipe and may need further editing in order to be fully functional.
# (Feel free to remove these comments when editing.)

# WARNING: the following LICENSE and LIC_FILES_CHKSUM values are best guesses - it is
# your responsibility to verify that the values are complete and correct.
LICENSE = "GPL-2.0-only"
LIC_FILES_CHKSUM = "file://LICENSE;md5=b234ee4d69f5fce4486a80fdaf4a4263"

SRC_URI = "git://github.com/secdev/scapy;protocol=https;branch=master"

# Modify these as desired
PV = "1.0+git${SRCPV}"
SRCREV = "5a1abdc4cee779cf3a8afd337aace8917ab66127"

S = "${WORKDIR}/git"

#inherit setuptools3

do_install() {
    install -d ${D}/home/root/scapy
    cp -r ${S}/* ${D}/home/root/scapy/
}

FILES_${PN} += "/home/root/scapy/"

RDEPENDS_${PN} = ""

# WARNING: the following rdepends are determined through basic analysis of the
# python sources, and might not be 100% accurate.
#RDEPENDS:${PN} += "python3-compression python3-core python3-crypt python3-ctypes python3-datetime python3-difflib python3-fcntl python3-html python3-io python3-json python3-logging python3-math python3-multiprocessing python3-netclient python3-numbers python3-pickle python3-profile python3-shell python3-stringold python3-threading"

# WARNING: We were unable to map the following python package/module
# dependencies to the bitbake packages which include them:
#    Crypto.Cipher
#    Crypto.Hash
#    Crypto.Protocol.KDF
#    Cryptodome.Cipher
#    Cryptodome.Hash
#    Cryptodome.Protocol.KDF
#    IPython
#    IPython.terminal.prompts
#    __builtin__
#    __pypy__
#    bpython
#    bpython.curtsies
#    brotli
#    can
#    can.interface
#    cartopy.crs
#    colorama
#    cryptography
#    cryptography.exceptions
#    cryptography.hazmat.backends
#    cryptography.hazmat.backends.openssl.backend
#    cryptography.hazmat.primitives
#    cryptography.hazmat.primitives.asymmetric
#    cryptography.hazmat.primitives.asymmetric.dh
#    cryptography.hazmat.primitives.asymmetric.x25519
#    cryptography.hazmat.primitives.ciphers
#    cryptography.hazmat.primitives.ciphers.aead
#    cryptography.hazmat.primitives.cmac
#    cryptography.hazmat.primitives.hashes
#    cryptography.hazmat.primitives.hmac
#    cryptography.hazmat.primitives.kdf.hkdf
#    cryptography.hazmat.primitives.kdf.pbkdf2
#    cryptography.utils
#    geoip2.database
#    geoip2.errors
#    graphviz
#    intelhex
#    lzw
#    matplotlib
#    matplotlib.collections
#    matplotlib.lines
#    mock
#    prompt_toolkit
#    prompt_toolkit.formatted_text
#    prompt_toolkit.shortcuts.dialogs
#    ptpython.ipython
#    ptpython.repl
#    pyannotate_runtime
#    pyx
#    traitlets.config.loader
#    vpython
#    winreg
#    zstandard
