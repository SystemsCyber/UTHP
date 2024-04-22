# Ultimate Truck Hacking Platform (UTHP) Yocto Build Guide

## 1: Introduction

### 1.1 Compatible Linux Distribution

Ensure your Build Host meets the following requirements:

- **Disk Space:** 50 Gbytes of free disk space.
- **OS:** Supported Linux distribution (i.e., recent releases of Fedora, openSUSE, CentOS, Debian, or Ubuntu). I use Ubuntu 22.04.1 LTS. [You may also use Windows Subsystem for Linux (WSL) on Windows 10 or 11.](https://docs.yoctoproject.org/dev-manual/start.html#setting-up-to-use-windows-subsystem-for-linux-wsl-2)

### 1.2 Required Software Versions

- Git 1.8.3.1 or greater.
- tar 1.28 or greater.
- Python 3.6.0 or greater.
- gcc 7.5 or greater.
- GNU make 4.0 or greater.

> **Note:** The Build Host is the system used to construct images in a Yocto Project Development environment.

## 2: Build Host Setup

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

### 2.3 Clone the UTHP Yocto Repository

```bash
git clone https://github.com/SystemsCyber/UTHP
git checkout <desired-branch>
```

Then move to the UTHP/Yocto directory and take a look at existing files:

```bash
cd UTHP/Yocto
```

## 3: Building Your Image

### 3.1 Initialize the Build Environment

Run the oe-init-build-env environment setup script to define Yocto Project’s build environment on your build host. You need to be within the poky directory.

```bash
cd poky
source oe-init-build-env
```

This has to be done each time you open a new terminal to make changes to your Yocto system. The script also creates a build/ directory. Once the script is run, your current directory is the build directory. After the build completes, all files created during the build will be present in this directory.

### 3.2 Examine and Update Your Local Configuration File

Once the build environment is set up, a local configuration file named local.conf becomes available in a conf subdirectory of the Build Directory (i.e., poky/build/conf/local.conf). This file contains settings that control the behavior of the build system. You can modify this file to suit your needs.

For this example, our defaults are set to build for BeagleBone Black:

```bash
MACHINE ?= "beaglebone-yocto"
```

### 3.3 Adding Layers to Your Build

Yocto uses layers to manage additions to the base build. You can add your layer inside the build directory.

```bash
bitbake-layers create-layer meta-<your-layer-name>
```

Next, add this layer to your bblayers.conf

```bash
bitbake-layers add-layer meta-<your-layer-name>
```

For our build, make sure to copy the [meta-custom](meta-custom) layer to the build directory and add it to the bblayers.conf file with the following command:

```bash
bitbake-layers add-layer <path-to-meta-custom-layer>
```

To add our meta-custom layer:

```bash
cp -r ~/UTHP/Yocto/meta-custom ~/poky
bitbake-layers add-layer ../meta-custom/
```

Now take a look and understand the [custom-image.bb file](~/poky/meta-custom/recipes-core/images/custom-image.bb) under ~/poky/meta-custom/recipes-core/images.

> The IMAGE_INSTALL variable is used to specify which packages to include in the image, and the append operator is used to add to the list of packages to be installed. Some of the image installs need to be added as a recipe, which will be discussed in [3.3 Adding Recipes to Your Build](#34-adding-recipes-to-your-build).

If you are following our build, add the meta-openembedded layers for common software tools and utilities such as can-utils:

```bash
cd ~/poky
git clone git://git.openembedded.org/meta-openembedded
cd meta-openembedded
git checkout -t origin/kirkstone -b my-kirkstone
```

You will also need to clone the following repositories and checkout the kirkstone branch:

```bash
git clone https://github.com/Xilinx/meta-jupyter
git clone https://git.openembedded.org/meta-python2
```

Add the meta-oe layer for can-utils support. Within your oe-init-build-env:

```bash
bitbake-layers add-layer ../meta-openembedded/meta-oe
```

### 3.4 Adding Custom Recipes to Your Build

Recipes are added inside your layers and follow a directory structure:

```
/poky
---/build
   ---/meta-<your-layer-name>
      ---/recipes-<recipe-name>
         ---/<recipe-name>
            ---/<recipe-name>.bb
```

You can refer to the [meta-skeleton](~/poky/meta-sekelton) layer for examples of how to create recipes. This example shows how to add a recipe for the can-utils package.
You can also refer to your branch's repo for recipies that have already been made (e.g., https://layers.openembedded.org/layerindex/branch/kirkstone/layers/ )

## 4: Changing the Kernel Device Tree

If you are following the UTHP build, just run:

```bash
bitbake virtual/kernel
```

### 4.1 Modifying the Kernel / Device Tree

> Note: Before making manual changes to the kernel, it is recommended to use the `bitbake -c menuconfig virtual/kernel` command to open the kernel configuration GUI. This will allow you to make changes to the kernel in a more user-friendly manner. If you are following our build, you can [skip](#5-building-the-image) this section.

#### 4.1.2 Modifying the Kernel / Device Tree using menuconfig:

```bash
bitbake -c menuconfig virtual/kernel
```

To compile these changes for the build, run the following command:

```bash
bitbake virtual/kernel
```

#### 4.1.3 Modifying the Device Tree Manually as an example for adding D_CAN0 and D_CAN1:

If you are following our build, you can just run `bitbake virtual/kernel` to compile the changes. To learn about making manual changes to the device tree, continue reading. IF you would like to learn how to include a patch file as a part of the build process, skip to [4.1.4](#414-including-a-patch-file-as-a-part-of-the-build-process).

Device Trees are data structures describing the hardware components for the kernel. To find the device tree for BeagleBone Black in the Yocto build:

```bash
find . -name "am335x-boneblack.dts" -mtime -1
```

This will return the path to the device tree file which you can modify manually located in `~/poky/build/tmp/work-shared`. It's recommend to use the `find` command frequently when working with yocto.

> Make note of the includes at the top of the file. These are the files that are included in the device tree and may have other information that you might be looking for.

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

```
- Networking support --> 
    - CAN bus subsystem support (enabled) --> 
        - Enable everything -- CAN Device Drivers -->
            - <*> Virtual Local CAN Interface (vcan) -- <*> Virtual CAN Tunnel (vxcan) -- <*> Serial / USB serial CAN Adaptors (slcan) -- <*> Platform CAN drivers with Netlink support (NEW) -- [*]   CAN bit-timing calculation (NEW)
            -  <*>   Bosch C_CAN/D_CAN devices -->
                - <*>   Generic Platform Bus based C_CAN/D_CAN driver
            - [*] CAN devices debugging messages
```

```bash
bitbake virtual/kernel
```

#### 4.1.4 Including a Patch File as a Part of the Build Process:

First, change to the kernel source directory:

```bash
cd ~/poky/build/tmp/work-shared/beaglebone-yocto/kernel-source/arch/arm/boot/dts
```

Then, git pull:
```bash
git pull
```

Ensure the dts file is unmodified and there are no changes:

```bash
git status
```

Now make your changes to the dts file. Once you are done, create a patch file:

```bash
git add <name of the dts file>
git commit -m "Added D_CAN0 and D_CAN1" # For example
git format-patch -1
```

Then move the patch file to the meta-custom layer:

```bash
mv 0001-Added-D_CAN0-and-D_CAN1.patch ~/poky/meta-custom/recipes-kernel/linux/files/
```

Add the patch file to the kernel recipe:

```bash
FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
SRC_URI += "file://0001-Added-D_CAN0-and-D_CAN1.patch"
```

#### 4.2 The .config file in kernel source directory produced by the menuconfig:

```bash
find . -name ".config" -mtime -1
```

Copy the `.config` file to the kernel source directory and run `bitbake virtual/kernel -c compile -f` to compile the kernel.

```bash
cp ~/UTHP/Yocto/.config ~/poky/build/<path-to-your-.config-file> 
bitbake virtual/kernel -c compile -f
```

> The linux-yocto_%.bbappend file under the meta-custom layer utlizes the virtual/kernel built through the recipe linux-yocto.

## 5: Building the Image

To build the image, run the following command:

```bash
bitbake custom-image
```

## 6: Flashing the Image to an SD Card

The image for the BeagleBone Black will be present in tmp/deploy/images/beaglebone-yocto/.

```bash
dd if=custom-image-beaglebone-yocto.wic of=/dev/sdb bs=4M
```

If you are on a Windows machine, you can use Etcher to flash the image to the SD card.

Connect the BeagleBone Black to your computer and power it up. You can use a serial terminal to connect to the BeagleBone Black. The default baud rate is 115200.

```bash
screen /dev/ttyUSB0 115200
```

You can also connect via SSH

On the host computer:
```bash
sudo ifconfig usb0 192.168.7.* netmask 255.255.255.0 up
```
```bash
ssh uthp@192.168.7.2
```

or on Windows using PuTTY.
Find the COM port by going to Device Manager and looking under Ports.

## FAQ

### How to verify Device Tree Overlays are working:

On the host system see the compiled device tree file, decompile it and check the changes are included and verify your sanity:

```bash
sudo apt-get install device-tree-compiler
```

```bash
dtc -I dtb -O dts -o am335x-boneblack.dts am335x-boneblack.dtb
```

### How to clean / clear yocto cache?

1. **`-c clean`**: This task cleans up the build artifacts for a specific recipe. It removes the temporary files and build output generated during the compilation process for the specified recipe. It does not remove any downloaded source files or other cached data. This task is useful when you want to clean up the build artifacts for a specific recipe without affecting other recipes.
  
  Example:
  
  ```bash
  bitbake -c clean <recipe-name>
  ```
  
2. **`-c cleanall`**: This task performs a more comprehensive clean-up compared to `-c clean`. It removes not only the build artifacts for a specific recipe but also any downloaded source files, patches, and other cached data associated with the recipe. It effectively resets the recipe's build environment to a clean state, as if it had never been built before. This task is useful when you want to completely clean a recipe and rebuild it from scratch.
  
  Example:
  
  ```bash
  bitbake -c cleanall <recipe-name>
  ```
  
3. **`-c cleansstate`**: This task cleans the shared state cache for a specific recipe. The shared state cache contains pre-built artifacts and metadata that can be reused across multiple builds to speed up the build process. By running `-c cleansstate`, you clear the cache for the specified recipe, forcing BitBake to rebuild the recipe and its dependencies from scratch. This task is useful when you suspect that the cached data for a recipe might be corrupted or outdated.
  
  Example:
  
  ```bash
  bitbake -c cleansstate <recipe-name>
  ```
