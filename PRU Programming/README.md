## PRU Programming on the BeagleBone Black (BBB)

This tutorial covers programming the BeagleBone Black's Programmable Real-Time Units (PRUs)

### Update your OS

```bash
sudo /opt/scripts/tools/update_kernel.sh
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
```
### Setting up your PC

We will compile C code for the PRUs using the TI CCS IDE on our PC and transfer them to the BBB.

### Install CCS

Download and install CCS. Make sure that you select the Sitara option as that's what we're targeting. Note that if you're adding Sitara to and existing CCS installation, you will need to make sure you have exactly the same version of the installer otherwise you'll be forced to do a new installation. Once it's installed, go to the App Center and add in the PRU compiler.

### Install PRU software support package

```bash
git clone git://git.ti.com/pru-software-support-package/pru-software-support-package.git
```
This support package contains the header files you need and also some nice examples in the example/am335x folder. I suggest an example (such as PRU_gpioToggle) to start from. The critical part is that the include and include/am335x folders have some essential stuff.

### Build and deploy

If all goes to plan, you should be able to build in CCS by clicking the hammer icon. The fruits of your labour will be a single .out file in the Debug folder. You need to copy this file to your BeagleBone - via FTP/SSH - so that it can find its final resting place of the PRU.

### Enable the PRU output

Each pin on the BB has multiple modes. In the case of our LED blink, we're expecting pin 27 on the P9 header to be used for PRU output. From the PRU's point of view this is PRU0, register R30 bit 5, but to the BeagleBone it's P9_27. To enable it, you will need to execute the following:
```bash
config-pin P9_27 pruout
```
### Copy your firmware to the PRU

Your out file needs go be copied to a special firmware folder to be accessible.
```bash
sudo -i
cp /path/to/your/file/<filename>.out /lib/firmware/<filename>
```
Then we need to deploy it into PRU0 - confusingly referred to a remoteproc1. (PRU1 is remoteproc2. remoteproc0 is to do with the Cortex M3 co-processor.)

```bash
cd /sys/class/remoteproc/remoteproc1
echo '<filename' > firmware
```
### Test it Out
```bash
echo 'start' > state
```











