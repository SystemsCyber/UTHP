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

The build process creates an entire Linux distribution, including the toolchain, from source. Use following steps to build your image.

### Initialize the Build Environment

Run the oe-init-build-env environment setup script to define Yocto Project’s build environment on your build host. You need to be within poky directory.
```bash
cd poky
source oe-init-build-env
```
The script also creates build/ directory. Once the script is run your current directory is the build directory. After the build completes, all files created during the build will be preset in this directory.

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

The image for the BBB will be present in tmp/deploy/images/beaglebone-yocto.
```bash
dd if=core-image-minimal-beaglebone-yocto.wic of=/dev/sdb bs=4M
```
