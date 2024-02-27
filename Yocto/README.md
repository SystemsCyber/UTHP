# Yocto Project Build for BeagleBone Black

## Chapter 1: Introduction
### 1.1 Compatible Linux Distribution

Ensure your Build Host meets the following requirements:

- **Disk Space:** 50 Gbytes of free disk space.
- **OS:** Supported Linux distribution (i.e., recent releases of Fedora, openSUSE, CentOS, Debian, or Ubuntu). I use Ubuntu 22.04.1 LTS.

### 1.2 Required Software Versions

- Git 1.8.3.1 or greater.
- tar 1.28 or greater.
- Python 3.6.0 or greater.
- gcc 7.5 or greater.
- GNU make 4.0 or greater.

> **Note:** The Build Host is the system used to construct images in a Yocto Project Development environment.

## Chapter 2: Build Host Setup
### 2.1 Build Host Packages

Install the essential host packages on your build host:

```bash
sudo apt install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev zstd liblz4-tool
```

### 2.2 Clone Poky

```bash
git clone git://git.yoctoproject.org/poky
```

Then move to the poky directory and take a look at existing branches:

```bash
cd poky
git branch -a
```

Check out the kirkstone branch:

```bash
git checkout -t origin/kirkstone -b my-kirkstone
```

## Chapter 3: Building Your Image
### 3.1 Initialize the Build Environment

Run the oe-init-build-env environment setup script to define Yocto Project’s build environment on your build host. You need to be within the poky directory.

```bash
cd poky
source oe-init-build-env
```

This has to be done each time you open a new terminal to make changes to your Yocto system. The script also creates a build/ directory. Once the script is run, your current directory is the build directory. After the build completes, all files created during the build will be present in this directory.

### 3.2 Examine and Update Your Local Configuration File

Once the build environment is set up, a local configuration file named local.conf becomes available in a conf subdirectory of the Build Directory.

For this example, the defaults are set to build for BeagleBone Black and qemuarm:

```bash
MACHINE ?= "beaglebone-yocto"
```

Increase the number of threads that bitbake uses by adding this to the end of local.conf:

```bash
BB_NUMBER_THREADS = "y"
```

Where y is the number of threads you want to use.

## Chapter 4: Start the Build
### 4.1 Build an OS Image

Build an OS image for the target with the following command.

```bash
bitbake core-image-minimal
```

## Chapter 5: Flashing and Running
### 5.1 Flash the Image to BeagleBone Black

The image for the BeagleBone Black will be present in tmp/deploy/images/beaglebone-yocto/.

```bash
dd if=core-image-minimal-beaglebone-yocto.wic of=/dev/sdb bs=4M
```
If you are on a Windows machine, you can use Etcher to flash the image to the SD card.

Connect the BeagleBone Black to your computer and power it up. You can use a serial terminal to connect to the BeagleBone Black. The default baud rate is 115200.

```bash
screen /dev/ttyUSB0 115200
```

or on Windows using PuTTY.
Find the COM port by going to Device Manager and looking under Ports.

## Chapter 6: Kernel Configurations
### 6.1 Changing the Kernel for Driver Configurations

Yocto uses a virtual kernel, which can be used to make modifications to the kernel configurations. Make sure you have the environment set up correctly. This needs to be done each time you open a new terminal.

```bash
source oe-init-build-env
```

Open the Virtual Kernel:

```bash
bitbake -c menuconfig virtual/kernel
```

This will open up a GUI where you can make modifications to the kernel.

## Chapter 7: Adding Layers
### 7.1 Adding Layers to Yocto

Yocto uses layers to manage additions to the base build. You can add your layer inside the build directory.

```bash
bitbake-layers create-layer meta-<your-layer-name>
```

Next, add this layer to your bblayers.conf

```bash
bitbake-layers add-layer meta-<your-layer-name>
```

## Chapter 8: Adding Recipes
### 8.1 Adding Recipes Inside Your Layer

Recipes are added inside your layers and follow a directory structure:

```
/poky
---/build
   ---/meta-<your-layer-name>
      ---/recipes-<recipe-name>
         ---/<recipe-name>
            ---/<recipe-name>.bb
```

This example shows how to add a recipe for the can-utils package.

```bash
mkdir -p meta-custom/recipes-support/can-utils
```

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

Include your recipe in conf/local.conf. Add the following line to include the recipe and its dependencies:

```bash
IMAGE_INSTALL:append = " can-utils iproute2 libsocketcan"
```

Rebuild the image:

```bash
bitbake core-image-minimal
```

### 8.2 Adding a custom user

Under an layer add a recipe, example custom_user.bb 

```bash
inherit extrausers

# Add default user 'uthp' and set the password
EXTRA_USERS_PARAMS = "useradd uthp; \
                      usermod -p '\$5\$Nx2D0wB1k15\$LYl7n9Tvtwo0fmsbs/frfpm7OuDJj2AIvcdWZfhS99C' uthp; "
```

Ensure this recipe is added to the package to be baked in as follows:

```bash

IMAGE_INSTALL:append = " custom_user"
```

## Chapter 9: Changing the Kernel Device Tree
### 9.1 Modifying the Kernel Device Tree

Device Trees are data structures describing the hardware components for the kernel. Modify the device tree for BeagleBone Black in the Yocto build:

```bash
find . -name "am335x-boneblack.dts"
```

This will return the path to the device tree file which you can modify manually. Make note of the includes at the top of the file. 
These are the files that are included in the device tree. Make the necessary changes and save the file.

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
Make sure to remove these lines as well from the DTS file:
- P9_20 (I2C2 SDA)
- P9_19 (I2C2 SCL)
- P9_26 (UART1 RXD)
- P9_24 (UART1 TXD)
  
Rebuild the Kernel:

```bash
bitbake -c menuconfig virtual/kernel
```

Add CAN driver support to the Kernel and bake the Kernel:

```bash
bitbake virtual/kernel
```

To add LED support to the BBB kernel:

Device Drivers --> 
- LED Support (enabled) --> 
    - LED Class Support (enabled) -- LED Support for GPIO connected LEDs (enabled) -- LED Trigger support (enabled) --> 
        - LED Heartbeat Trigger (enabled) -- LED CPU Trigger (enabled) -- LED GPIO activated Trigger (enabled) -- LED GPIO Trigger (enabled)

Finally, remake the image:

```bash
bitbake core-image-minimal
```

Current kernel configuration can be found in the `/poky/build/tmp/work-shared/beaglebone-yocto/kernel-build-artifacts` directory. or by using the following command:

```bash
find . -name ".config"
```
Not tested:
Copy the `.config` file to the kernel source directory and run `bitbake virtual/kernel -c compile -f` to compile the kernel.

## FAQ  
### Nothing changed when using bitbake virtual/kernel:
Clean the Build: Try cleaning the build directory first:

```bash
bitbake -c cleansstate virtual/kernel
```

Force a Rebuild: Force Bitbake to rebuild the kernel even if it thinks it's up to date:

```bash
bitbake -c compile -f virtual/kernel
```

### How to verify Device Tree Overlays are working:

On the host system see the compiled device tree file, decompile it and check the changes are included:

```bash
sudo apt-get install device-tree-compiler
```

```bash
dtc -I dtb -O dts -o am335x-boneblack.dts am335x-boneblack.dtb
```
