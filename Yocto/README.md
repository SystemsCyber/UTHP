# Yocto Project Build for BBB

## Compatible Linux Distribution

Ensure your Build Host meets the following requirements:

- **Disk Space:** 50 Gbytes of free disk space.
- **OS:** Supported Linux distribution (i.e., recent releases of Fedora, openSUSE, CentOS, Debian, or Ubuntu). I use Ubuntu 22.04.1 LTS.

### Required Software Versions:

- Git 1.8.3.1 or greater.
- tar 1.28 or greater.
- Python 3.6.0 or greater.
- gcc 7.5 or greater.
- GNU make 4.0 or greater.

> **Note:** The Build Host is the system used to construct images in a Yocto Project Development environment.

## Build Host Packages

Install the essential host packages on your build host:

```bash
sudo apt install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev zstd liblz4-tool
```
## Clone Poky

```bash
git clone git://git.yoctoproject.org/poky
```
Then move to the poky directory and take a look at existing branches:
```bash
cd poky
git branch -a
```
Check out the kirkstone branch based as we will be using the Kirkstone release:
```bash
git checkout -t origin/kirkstone -b my-kirkstone
```
The above Git checkout command creates a local branch named my-kirkstone. The files available to you in that branch exactly match the repository’s files in the kirkstone release branch.

## Building Your Image

The build process creates an entire Linux distribution, including the toolchain, from the source. Use the following steps to build your image.

### Initialize the Build Environment

Run the oe-init-build-env environment setup script to define Yocto Project’s build environment on your build host. You need to be within poky directory.
```bash
cd poky
source oe-init-build-env
```
This has to be done each time you open a new terminal to make changes to your yocto system. The script also creates build/ directory. Once the script is run your current directory is the build directory. After the build completes, all files created during the build will be preset in this directory.

## Examine and Update Your Local Configuration File
Once the build environment is setup, a local configuration file named local.conf becomes available in a conf subdirectory of the Build Directory.
For this example, the defaults are set to build for BeagleBone Black and qemuarm.

MACHINE ?= “beaglebone-yocto”
MACHINE ?= “qemuarm”

The same can be tested on the hardware and QEMU.
## Start the Build

Build an OS image for the target with the following command.
```bash
bitbake core-image-minimal
```
## Flash the image to BBB and run

The image for the BBB will be present in `tmp/deploy/images/beaglebone-yocto/`.
```bash
dd if=core-image-minimal-beaglebone-yocto.wic of=/dev/sdb bs=4M
```

## Changing the Kernel for driver configurations

Yocto uses a virtual kernel which can used to make modifications to the kernel configurations. Make sure you have the environment setup correctly. This needs to be done each time you open a new terminal.
```bash
source oe-init-build-env
```
Open the Virtual Kernel:
```bash
bitbake -c menuconfig virtual/kernel
```
This will open up a GUI where you can make modifications to the kernel.

## Adding Layers

Yocto uses layers to manage additions to the base build. You can add your layer inside the build directory.
```bash
bitbake-layers create-layer meta-<your-layer-name>
```
Next, add this layer to your bblayers.conf
```bash
bitbake-layers add-layer meta-<your-layer-name>
```

## Adding recipes inside your layer

Recipes are added inside your layers. They follow a directory structure:
```
/poky
---/build
   ---/meta-<your-layer-name>
      ---/recipes-<recipe-name>
         ---/<recipe-name>
            ---/<recipe-name>.bb
```
This example shows how to add a recipe for the `can-utils` package:

```bash
recipetool create -o meta-custom/recipes-support/can-utils/can-utils_git.bb git://github.com/linux-can/can-utils.git
```
Edit can-utils.bb:
```bash
DESCRIPTION = "CAN utilities for Linux"
HOMEPAGE = "https://github.com/linux-can/can-utils"
SECTION = "utils"
LICENSE = "GPL-2.0"
LIC_FILES_CHKSUM = "file://COPYING;md5=393a5ca445f6965873eca0259a17f833"

SRC_URI = "https://github.com/linux-can/can-utils.git;branch=master"
SRCREV = "186bd967173a8a42ff544b5977edcda7c968c1aa"

PV = "1.0+git${SRCPV}"

S = "${WORKDIR}/git"

inherit cmake

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
```

Include your recipe in `conf/local.conf`. Add the following line to include the recipe and its dependencies:
```bash
IMAGE_INSTALL:append = " can-utils iproute2 libsocketcan"
```

Rebuild the image:
```bash
bitbake core-image-minimal
```

## Changing the Kernel Device Tree

Device Trees are data structures describing the hardware components so the kernel can manage and use those components. These include the CPU, memory, hardware buses, and associated peripherals. For the purpose of the Yocto build this is very important as it tells the kernel the configuration of CPU, memory and peripherals for our beaglebone. The default device tree is defined in the file `am335x-boneblack.dtb`. This can be found in the `boot` directory of the Yocto build. The default device tree does not initialize peripherals that we need for the UTHP and so we need to re-define the device tree for our purpose. If you have a pre-built kernel, we need to remove that to edit the device tree:
```bash
bitbake -c clean virtual/kernel
```
Now, we remake the kernel files:
```bash
bitbake -c menuconfig virtual/kernel
```
Just open and exit the menu configuration. This creates the generic device tree files. Next, we modify the device tree:
```bash
cd path-to-your-poky-build/tmp/linux/beaglebone-yocto/kernel-sources/arch/arm/boot/dts/
nano am335x-boneblack.dts   
```
For adding D_CAN0 and D_CAN1, we need to disable `I2C2` and `UART1`. Never disable `UART0`:
```bash
&i2c2 {
    status = "disabled";
};

&uart1 {
    status = "disabled";
};

&am33xx_pinmux {
    dcan0_pins: pinmux_dcan0_pins {
        pinctrl-single,pins = <
            AM33XX_IOPAD(0x97C, PIN_INPUT_PULLUP | MUX_MODE2) /* P9_19: d_can0_rx */
            AM33XX_IOPAD(0x978, PIN_OUTPUT_PULLDOWN | MUX_MODE2) /* P9_20: d_can0_tx */
        >;
    };
};
&am33xx_pinmux {
    dcan1_pins: pinmux_dcan1_pins {
        pinctrl-single,pins = <
            AM33XX_IOPAD(0x984, PIN_INPUT_PULLUP | MUX_MODE2) /* P9_24: d_can1_rx */
            AM33XX_IOPAD(0x980, PIN_OUTPUT_PULLDOWN | MUX_MODE2) /* P9_26: d_can1_tx */
        >;
    };
};
&dcan0 {
    status = "okay";
    pinctrl-names = "default";
    pinctrl-0 = <&dcan0_pins>;
    /* Other necessary properties and configurations */
};

&dcan1 {
    status = "okay";
    pinctrl-names = "default";
    pinctrl-0 = <&dcan1_pins>;
    /* Other necessary properties and configurations */
};
```
Now we rebuild the Kernel:
```bash
bitbake -c menuconfig virtual/kernel
```
Add CAN driver support to the Kernel and bake the Kernel:
```bash
bitbake virtual/kernel
```

Finally, remake the image:
```bash
bitbake core-image-minimal
```
