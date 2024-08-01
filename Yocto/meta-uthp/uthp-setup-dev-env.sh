#!/bin/bash
YOCTO_DIR="Yocto"
# Helper functions for setting up the Yocto development environment
function clone_layers() {
    git clone git://git.yoctoproject.org/poky.git "$YOCTO_DIR"
    git clone git://git.openembedded.org/meta-openembedded "$YOCTO_DIR/meta-openembedded"
    git clone git://git.openembedded.org/meta-python2 "$YOCTO_DIR/meta-python2"
    git clone https://github.com/Xilinx/meta-jupyter "$YOCTO_DIR/meta-jupyter"
    git clone git://git.yoctoproject.org/meta-arm "$YOCTO_DIR/meta-arm"
    git clone git://git.yoctoproject.org/meta-ti "$YOCTO_DIR/meta-ti"
    git clone https://github.com/SystemsCyber/UTHP/Yocto/meta-uthp "$YOCTO_DIR/meta-uthp"
}

function checkout-layer() {
    cd "$YOCTO_DIR/$1"
    git checkout "$2"
    cd "$YOCTO_DIR"
}
# This script is used to set up the development environment for the UTHP project.
# check if the script is being run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi
# 1. setup build host
sudo apt install -y gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev zstd liblz4-tool
# 2. Have the user specify the directory where the Yocto project will be cloned
mkdir -p "$YOCTO_DIR"
# 3. Clone the necessary layers
clone_layers
# 4. Checkout the necessary branches
checkout-layer "" "scarthgap"
checkout-layer "meta-openembedded" "scarthgap"
checkout-layer "meta-arm" "scarthgap"
checkout-layer "meta-ti" "scarthgap"
checkout-layer "meta-uthp" "scarthgap"
# 5. Edit the layer.conf files
# meta-python2/meta-jupyter layers are a bit different --> they don't have a scarthgap branch
cp "$YOCTO_DIR/meta-uthp/conf.samples/meta-python2-layer.conf.sample" "$YOCTO_DIR/meta-python2/conf/layer.conf"
cp "$YOCTO_DIR/meta-uthp/conf.samples/meta-jupyter-layer.conf.sample" "$YOCTO_DIR/meta-jupyter/conf/layer.conf"

# Add the meta-uthp conf.samples to their respective directories
cp "$YOCTO_DIR/meta-uthp/conf.samples/local.conf.sample" "$YOCTO_DIR/build/conf/local.conf"
cp "$YOCTO_DIR/meta-uthp/conf.samples/bblayers.conf.sample" "$YOCTO_DIR/build/conf/bblayers.conf"
cp "$YOCTO_DIR/meta-uthp/conf.samples/conf-notes.txt" "$YOCTO_DIR/build/conf/conf-notes.txt"