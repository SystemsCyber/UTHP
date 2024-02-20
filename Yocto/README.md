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
sudo apt install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint3 xterm python3-subunit mesa-common-dev zstd liblz4-tool
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
bitbake core-image-minimal```
```

## Adding custom recipe to add a custom user

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

## Override Existing Functionality in a Yocta Image

A use case may arrise to modify existing functionility in a Yocto Linux Project forexample to change default ```bass /etc/issue``` that displays a custom message when Linux boot.

The following are is the step by step process to achieve this

1. Idenify the base recipe you wish to override:

```bash
find meta/ -name issue 
```

This command outputs:

```bash
meta/recipes-core/base-files/base-files/issue
```

Now identify which file uses it to display the message in the image. Quick way is to grep throogh files in the base meta layer and make:

```bash
find meta/ -type f -name "*.bb" -o -name "*.bbappend" | xargs grep "/issue"|more
```

closest output is the recipe:

```bash
meta/recipes-core/base-files/base-files_3.0.14.bb:           file://issue.net \
meta/recipes-core/base-files/base-files_3.0.14.bb:           file://issue \
meta/recipes-core/base-files/base-files_3.0.14.bb:             ${sysconfdir}/issue /${sysconfdir}/issue.net \
meta/recipes-core/base-files/base-files_3.0.14.bb:	install -m 644 ${WORKDIR}/issue*  ${D}${sysconfdir}
meta/recipes-core/base-files/base-files_3.0.14.bb:		printf "${DISTRO_NAME} " >> ${D}${sysconfdir}/issue
meta/recipes-core/base-files/base-files_3.0.14.bb:		printf "${DISTRO_NAME} " >> ${D}${sysconfdir}/issue.net
meta/recipes-core/base-files/base-files_3.0.14.bb:			printf "%s " $distro_version_nodate >> ${D}${sysconfdir}/issue
meta/recipes-core/base-files/base-files_3.0.14.bb:			printf "%s " $distro_version_nodate >> ${D}${sysconfdir}/issue.net
meta/recipes-core/base-files/base-files_3.0.14.bb:		printf "\\\n \\\l\n" >> ${D}${sysconfdir}/issue
meta/recipes-core/base-files/base-files_3.0.14.bb:		echo >> ${D}${sysconfdir}/issue
meta/recipes-core/base-files/base-files_3.0.14.bb:
```

Using this base script overide the message displayed changing the file ```bash /etc/issue ```.

2. Add custom message

Under the custom recipe folder e.g ```bash */recipe-custom/base-files/ ``` create a append recipe that has an extenssion *.bbappend" with the same file name as the file you wish to overide "base-files_3.0.14.bb" as follows "base-files_%.bbappend". The "%" is used to mask any version of the latest file. Place the message in the folder "*/recipe-custom/base-files/files/example_issue" and make reference to the file in append recipe as follows:

```bash
S = "${WORKDIR}"

SRC_URI = "file://exaple_issue"

do_install:append() {
        install -m 0644 ${S}/example_issue ${D}${sysconfdir}/issue
        echo "Systems Engineering - CSU" >> ${D}${sysconfdir}/issue
        echo "Yocto [Beaglebone Black], Distro version: ${DISTRO_VERSION}" >> ${D}${sysconfdir}/issue
}
```

This code appends a new file to "base-files_3.0.14.bb" during bitbake command execution. NOTE: since we are overriding the functionality there is no neeed to append the append recipe to IMAGE_INSTALL.
