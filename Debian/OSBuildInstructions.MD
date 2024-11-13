# Instructions for setting up the BeagleBone Black derived from: https://github.com/SystemsCyber/TruckCapeProjects/blob/master/OSBuildInstructions.md
![pinout diagram here](./imgs/beaglebone-black-pinout-1748733925.jpg)
## 1. Flashing the BeagleBone Black with Debian Linux OS

These steps were taken to build the TruckCape recovery SD card. If you have a UTHP from 2024, then these steps have already been done.

1. [Download this image](https://rcn-ee.com/rootfs/release/2023-10-07/bullseye-minimal-armhf/am335x-eMMC-flasher-debian-11.8-minimal-armhf-2023-10-07-2gb.img.xz) or find one from this [forum](https://forum.beagleboard.org/t/debian-11-x-bullseye-monthly-snapshot-2023-10-07/31280)

2. Using a utility like 7zip, decompress the image... or not. Some imagers decompress the image for you.

3. Using Win32DiskImager, Balena Etcher, Rufus, or an Imager of your choice, burn the Debian Linux distribution to a 4GB SD partition. This will be a flasher image that will overwrite the eMMC chip in the BeagleBone Black.

4. Insert the flasher image SD card into to the BeagleBone Black. Power on the BBB (i.e. plug in the USB) while depressing the SD boot button until the 4 user LEDs come on. After about 30 seconds, the flasher program will start as indicated by the user leds cycling in a back-and-forth pattern. The reflashing process could take 10-15 minutes, depending on the speed of the SD card.

## 2. [Connecting the BeagleBone Black via USB](https://www.dummies.com/article/technology/computers/hardware/beaglebone/how-to-connect-the-beaglebone-black-via-serial-over-usb-144981/) or via [IDE](http://192.168.7.2/ide.html) --> This port will probably need to be closed for security reasons.
Using an SSH client, like PuTTY, and a USB to computer connection, connect to the Beagle Bone Black SSH using IP 192.168.7.2 on port 22 or COM[1-9] at a baud of 115200.

### The new login uses the following credentials:

U: `debian`

P: `temppwd`

The availability if this connection may take longer than you might like, but be patient, the board will finish booting and enumerate as a drive on your host computer. 

Connect a live Internet connection by the Ethernet cable into your Beagle Bone Black. Check to see if you have a valid IP address on `eth0`:

```
sudo ifconfig
```
If you would like to test internet connectivity execute the following `ping` command which will send network packets to Google's external server using its IP address.

```
ping -c 2 8.8.8.8
```

The above command connection will show the following output. Successful communication should result in `0% packet loss`.

```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=54 time=10.4 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=54 time=10.2 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1006ms
rtt min/avg/max/mdev = 10.157/10.291/10.425/0.134 ms
```

Update U-Boot to the latest version:
```
sudo /opt/u-boot/bb-u-boot-am335x-evm/install.sh
```

## 3. Image Verification
If you are having troubles, be sure you are using the same version that's documented here. When the kernel changes, the results may be different. 

Enter the following commands to verify your image version, eeprom, and kernel version are the same as the ones used in this document:
```
sudo beagle-version | egrep -e 'eeprom' -e 'model' -e 'dogtag' ; uname -a
```
Output:
```
eeprom:[A335BNLT000C2042BBBG0642]
model:[TI_AM335x_BeagleBone_Black]
dogtag:[BeagleBoard.org Debian Bullseye Minimal Image 2023-10-07]
Linux BeagleBone 5.10.168-ti-r72 #1bullseye SMP PREEMPT Sat Sep 30 03:37:21 UTC 2023 armv7l GNU/Linux
```

## 4. Pin multiplexing

Check that you have the config-pin utility installed:
* `config-pin -c <filename>`
* `config-pin -l <pin>`
* `config-pin -q <pin>`
* `config-pin <pin> <mode>`

Write the following commands to get the CAN hardware to access the pins upon boot. 
Create a file in the /etc directory:

```
sudo nano /etc/pin_config.sh
```
Write the following into the file:
```
#!/bin/sh -e
# DCAN1
config-pin p9.24 can
config-pin p9.26 can 
# DCAN0
config-pin p9.19 can
config-pin p9.20 can
#ttyO2:
config-pin p9.21 uart
config-pin p9.22 uart
#ttyO4:
config-pin p9.11 uart
config-pin p9.13 uart
#ttyO5:
config-pin p8.37 uart
config-pin p8.38 uart
# PWMs
config-pin p8.46 pwm
config-pin p8.45 pwm
config-pin p8.34 pwm
config-pin p8.36 pwm
# GPIO
config-pin p9.12 gpio
config-pin p9.14 gpio

exit 0
```
Make the script executable:
```
sudo chmod +x /etc/pin_config.sh
```
However, these commands need to be run upon boot, so let's make a script to do this and add it to a boot sequence.

```
sudo nano /lib/systemd/system/pin_config.service
```
Add this to the file:
```
[Unit]
Description=Setup for BBB

[Service]
Type=simple
ExecStart=/bin/bash /etc/pin_config.sh

[Install]
WantedBy=multi-user.target
```

Update the service file permission

```
sudo chmod 644 /lib/systemd/system/pin_config.service
```

Start the service

```
sudo systemctl start pin_config.service
```

Verify the service

```
sudo systemctl status pin_config.service
```
Enable the service at boot

```
sudo systemctl enable pin_config.service
```
To confirm the pin_config.service was enabled, look for a symbolic link in `/etc/systemd/system`

```
debian@beaglebone:/etc/systemd/system$ ls -la
lrwxrwxrwx  1 root root   38 Sep 17 04:51 pin_config.service -> /lib/systemd/system/pin_config.service
```

Reboot and verify. `sudo shutdown -r now`

```
debian@beaglebone:~$ config-pin -q p9.24

Current mode for P9_24 is:     can

```

Verify the status of the pin_config.service was successful by looking for an output like this:

```
debian@beaglebone:~$ sudo systemctl status pin_config.service
● pin_config.service - Setup for BBB p
   Loaded: loaded (/etc/systemd/system/pin_config.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since Tue 2020-09-08 23:52:06 UTC; 2min 18s ago
  Process: 856 ExecStart=/bin/bash /home/debian/pin_config.sh (code=exited, status=0/SUCCESS)
 Main PID: 856 (code=exited, status=0/SUCCESS)

Sep 21 14:06:18 beaglebone bash[2040]: Current mode for P9_13 is:     uart
Sep 21 14:06:18 beaglebone bash[2040]: Current mode for P8_37 is:     uart
Sep 21 14:06:18 beaglebone bash[2040]: Current mode for P8_38 is:     uart
Sep 21 14:06:18 beaglebone bash[2040]: Current mode for P8_46 is:     pwm
Sep 21 14:06:18 beaglebone bash[2040]: Current mode for P8_45 is:     pwm
Sep 21 14:06:18 beaglebone bash[2040]: Current mode for P8_34 is:     pwm
Sep 21 14:06:18 beaglebone bash[2040]: Current mode for P8_36 is:     pwm
Sep 21 14:06:18 beaglebone bash[2040]: Current mode for P9_12 is:     gpio
Sep 21 14:06:18 beaglebone bash[2040]: Current mode for P9_14 is:     gpio
Sep 21 14:06:18 beaglebone systemd[1]: pin_config.service: Succeeded.
```
If this doesn't work, be sure to disable the overlays in the uEnv.txt file below.


## 5. Configuring DT Overlays
Edit the file `/boot/uEnv.txt`:
```
sudo nano /boot/uEnv.txt
```
Uncomment the disable_uboot_overlays but leave the emmc commented out:
```
###Disable auto loading of virtual capes (emmc/video/wireless/adc)
#disable_uboot_overlay_emmc=1
disable_uboot_overlay_video=1
disable_uboot_overlay_audio=1
disable_uboot_overlay_wireless=1
disable_uboot_overlay_adc=1
###
```

### 5.1 Enable the cape-universal overlay
Edit the file `/boot/uEnv.txt`:
```
sudo nano /boot/uEnv.txt
```
Ensure the following line is present:
```
enable_uboot_cape_universal=1
```

### 5.2 Enable the PRU uio overlay

By default TI’s REMOTEPROC PRU is enabled, but you can switch to classic UIO in /boot/uEnv.txt: by adding/enabling, this was added as of: 5.10.106-ti-r41 for the v5.10.x-ti branch…
Edit the file `/boot/uEnv.txt`:
```
sudo nano /boot/uEnv.txt
```
Copy the following line to the end of the file and save it:
```
### PRU uio enablement
uboot_overlay_pru=AM335X-PRU-UIO-00A0.dtbo
```
Verify the overlay is enabled:
```
lsmod | grep uio
```
Should show:
```
uio_pruss              16384  0
uio_pdrv_genirq        20480  0
uio                    20480  2 uio_pruss,uio_pdrv_genirq
```


## 6. Start the network interfaces

### 6.1 Enable the CAN interfaces
Edit your `/etc/network/interfaces` file.

```
sudo nano /etc/network/interfaces
```

Add the following lines:

```
allow-hotplug can1
 iface can1 can static
    bitrate 250000

allow-hotplug can0
 iface can0 can static
    bitrate 250000
```
Reboot: `sudo shutdown -r now`

Upon restart, the CAN interfaces should be mounted.

```
debian@beaglebone:~$ sudo ifconfig
[sudo] password for debian:
can0: flags=193<UP,RUNNING,NOARP>  mtu 16
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 10  (UNSPEC)
        RX packets 19375  bytes 155000 (151.3 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 42

can1: flags=193<UP,RUNNING,NOARP>  mtu 16
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 10  (UNSPEC)
        RX packets 50893  bytes 407139 (397.5 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 43

eth0: flags=-28669<UP,BROADCAST,MULTICAST,DYNAMIC>  mtu 1500
        ether ec:24:b8:72:7d:ef  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 55

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 400  bytes 27920 (27.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 400  bytes 27920 (27.2 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

usb0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.7.2  netmask 255.255.255.0  broadcast 192.168.7.255
        inet6 fe80::ee24:b8ff:fe72:7df1  prefixlen 64  scopeid 0x20<link>
        ether ec:24:b8:72:7d:f1  txqueuelen 1000  (Ethernet)
        RX packets 1895  bytes 136356 (133.1 KiB)
        RX errors 0  dropped 4  overruns 0  frame 0
        TX packets 2105  bytes 472901 (461.8 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

usb1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.6.2  netmask 255.255.255.0  broadcast 192.168.6.255
        ether ec:24:b8:72:7d:f5  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
If there is a live CAN bus connected, try `candump any` and confirm message traffic.

```
debian@beaglebone:~$ candump any
  can0  0CFEF100   [8]  FB FF FE AA AA 00 1F FF
  can1  08FE6E0B   [8]  FF FE FF FE FF FE FF FE
  can1  0CF00400   [8]  00 7D 7D 00 00 00 F0 7D
  can0  0CF00400   [8]  00 7D 7D 00 00 00 F0 7D
  can1  18F00E00   [8]  A0 0F FE 71 FF FF FF FF
  can0  18E0FF00   [8]  00 FF FF FF FF FA FF FF
  can1  18FEF200   [8]  00 00 FF FE BF 05 FE FF
  can1  18FEDF00   [8]  86 FF FF FF 7D FF FE 00
  can1  0CF00400   [8]  00 7D 7D 00 00 00 F0 7D
  can0  0CF00400   [8]  00 7D 7D 00 00 00 F0 7D
  can0  18F0000F   [8]  20 7D 7D F3 00 7D FE 63
  can1  10FDA300   [8]  FF FF FA FF FF FF FF FF
  can1  18FEE000   [8]  FF FF FF FF 0F 14 0A 00
  can1  18FD0900   [8]  FF FF FF FF 0C 78 B6 01
  can1  08FE6E0B   [8]  FF FE FF FE FF FE FF FE
  can1  1CEBFF00   [8]  0C 01 7F 02 09 01 84 06
  can0  0CF00400   [8]  00 7D 7D 00 00 00 F0 7D
  can1  0CF00400   [8]  00 7D 7D 00 00 00 F0 7D
  can0  18FEF200   [8]  00 00 FF FE BF 05 FE FF
  can1  18FF4500   [8]  78 2A FA 00 FF 00 00 AC
  can1  18FEDF00   [8]  86 FF FF FF 7D FF FE 00
  can1  1CFE9200   [8]  FF 80 97 FF FF FF FF FF
  can1  18F0010B   [8]  CC FF F0 FF FF 5C FF FF
  can1  0CF00400   [8]  00 7D 7D 00 00 00 F0 7D
  can0  0CF00400   [8]  00 7D 7D 00 00 00 F0 7D
  can1  0CF00300   [8]  FA FE 00 FF FF 0C 00 FF
  can0  18FEE000   [8]  FF FF FF FF 0F 14 0A 00
  can1  18FEEF00   [8]  FE FF FF FE FF FF FF 00
  can1  18FF4800   [8]  00 00 F3 FF 00 00 00 00
  can1  18FEE0CA   [8]  FF FF FF FF FF FF FF FF
  can1  18FEBF0B   [8]  FF FE FE FE FE FE FF FF
  can1  08FE6E0B   [8]  FF FE FF FE FF FE FF FE
  can1  0CF00400   [8]  00 7D 7D 00 00 00 F0 7D
```
### 6.2 Add virtual CAN drivers
The vcan interfaces are great ways to develop hardware without needing to troubleshoot physical CAN connections or have access to a truck.

Write a script to stand up some vcan devices. 
```
sudo nano /etc/network/vcan-start.sh
```
Enter these commands into the file:
```
#!/bin/sh -e
ip link add type vcan 
ip link set vcan0 up
ip link add dev vcan1 type vcan
ip link set vcan1 up
ip link add dev vcan2 type vcan
ip link set vcan2 up
exit 0
```

Make the script executable:
```
sudo chmod +x /etc/network/vcan-start.sh
```
This script should be run upon boot, so let's make a script to do this and add it to a boot sequence.

```
sudo nano /lib/systemd/system/vcan.service
```
Add this to the file:
```
[Unit]
Description=Turn on virtual CAN interfaces

[Service]
Type=simple
ExecStart=/bin/bash /etc/network/vcan-start.sh

[Install]
WantedBy=multi-user.target
```

Start the service

```
sudo systemctl start vcan.service
```

Verify the service

```
sudo systemctl status vcan.service
```
Enable the service at boot

```
sudo systemctl enable vcan.service
```
To confirm the vcan.service was enabled, look for a symbolic link in `/etc/systemd/system`

```
ls -la /etc/systemd/system/multi-user.target.wants/
lrwxrwxrwx  1 root root   32 Nov  7 15:27 vcan.service -> /lib/systemd/system/vcan.service
```
should show a line
```
lrwxrwxrwx  1 root root   32 Nov  7 15:27 vcan.service -> /lib/systemd/system/vcan.service
```

Reboot and verify. `sudo shutdown -r now`
```
debian@beaglebone:~$ ifconfig


vcan0: flags=193<UP,RUNNING,NOARP>  mtu 72
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

vcan1: flags=193<UP,RUNNING,NOARP>  mtu 72
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

vcan2: flags=193<UP,RUNNING,NOARP>  mtu 72
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Now there are 3 vcan channels ready for use. 

## 7. Software Package Installation

### 7.1 Ensure git is installed
```
sudo apt install git -y
```
### 7.2 Install [can-utils](https://elinux.org/Can-utils)
```
sudo apt install can-utils -y
```
Verify the installation and run:
```
cangen vcan0 | candump vcan0
```
### 7.3 Ensure python3 is installed and upgrade pip
```
sudo apt install python3-pip
sudo pip3 install --upgrade pip
```
Verify the installation and run:
```
python3 -V
pip3 -V
```
Install some useful packages:
```
pip3 install numpy pandas matplotlib python-can can-isotp scapy
```
### 7.4 Install python2.7
Install the xz-utils package for extracting the Python tarball:
```
sudo apt install xz-utils -y
```
Verify the installation and run:
```
xz --version
```
Install the build-essential package for compiling the Python source code:
```
sudo apt install build-essential -y
```
Verify the installation and run:
```
gcc --version
```
Get python2.7 from the ftp server and extract it:
```
wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz
tar -xf Python-2.7.9.tar.xz
```
Compile and install Python2.7:
```
cd Python-2.7.9
sudo ./configure --prefix=/usr/local
sudo make altinstall
python2.7 -V
export PATH="/usr/local/bin:$PATH"
```
Clean up the installation files:
```
sudo rm -rf ~/Python-2.7.9*
```
Verify the installation and run:
```
python2.7 -V
```
### 7.5 Install and setup Jupyter-lab
```
sudo pip3 install jupyterlab
```
Set the password:
```
jupyter server password
```
Verify the installation and run:
```
jupyter lab --ip=0.0.0.0 --port=8888 --NotebookApp.allow_origin='http://192.168.7.1'
```
Then open a browser and navigate to http://BeagleBone:8888/lab and enter the password you set above.
### 7.6 Install IPython3 
```
pip install ipython
```
You might get a warning about the directory not being in your PATH. If so, add the following:
```
export PATH="$HOME/.local/bin:$PATH"
```
Verify the installation and run:
```
ipython3 --version
```
### 7.7 Install canmatrix
```
pip install canmatrix
```
Verify the installation and run:
```
python3
>>> import canmatrix
>>> exit()
```
### 7.8 Install tmux
```
sudo apt install tmux -y
```
Example usages:
```
# Session Management
# Create a new session
tmux new-session -s session_name

# Attach to an existing session
tmux attach-session -t session_name

# Detach from the current session (leave it running in the background)
Ctrl-b d

# List existing sessions
tmux list-sessions

# Window Management
# Create a new window
Ctrl-b c

# Switch between windows
Ctrl-b n (next)
Ctrl-b p (previous)
Ctrl-b <window_number>

# Rename the current window
Ctrl-b ,

# Close the current window
Ctrl-b &

# Pane Management
# Split the current window horizontally
Ctrl-b %

# Split the current window vertically
Ctrl-b "

# Navigate between panes
Ctrl-b arrow keys

# Resize panes
Ctrl-b Ctrl-arrow keys

# Close the current pane
Ctrl-b x

# Miscellaneous
# View Tmux help
Ctrl-b ?

# Reload Tmux configuration
Ctrl-b :
source-file ~/.tmux.conf

# Copy mode (to scroll through the terminal output)
Ctrl-b [
```
### 7.9 Install rtl-sdr utils
```
sudo apt install rtl-sdr -y
```
Verify the installation and run:
```
rtl_test -t
```

Create a directory for repositories and building from source:
```
mkdir ~/repositories
cd ~/repositories
```
### 7.10 Sigrok can2 decoder

https://sigrok.org/wiki/Linux#Building_(script,_recommended) 

https://sigrok.org/wiki/Embedded

Install libsigrok dependencies:
```
sudo apt-get install git-core gcc g++ make autoconf autoconf-archive \
  automake libtool pkg-config libglib2.0-dev libglibmm-2.4-dev libzip-dev \
  libusb-1.0-0-dev libftdi1-dev libieee1284-3-dev libvisa-dev nettle-dev libavahi-client-dev \
  libhidapi-dev check doxygen python3-numpy python3-dev python-gi-dev python3-setuptools-git swig default-jdk
```
Install libsigrok from source:
```
git clone git://sigrok.org/libsigrok
cd libsigrok
./autogen.sh
./configure
make
sudo make install
```
Install sigrok-cli from source:
```
git clone git://sigrok.org/sigrok-cli
cd sigrok-cli
./autogen.sh
./configure
make
sudo make install
```
If package isn't found, try running:
```
sudo ldconfig /usr/local/lib
```
Then download can2 decoder:
```
git clone https://github.com/kentindell/canhack/
cd canhack/src/can2
```


### 7.11 py-hv-networks 
[https://github.com/TruckHacking/py-hv-networks](https://github.com/TruckHacking/py-hv-networks)
```
git clone https://github.com/TruckHacking/py-hv-networks
```
Then install the package:
```
git clone https://github.com/SystemsCyber/py-hv-networks.git
cd py-hv-networks
sudo python3 setup.py install
```
```
pip install -r requirements.txt
```

### 7.12 cmap
[https://github.com/CanBusHack/cmap](https://github.com/CanBusHack/cmap)
```
git clone https://github.com/CanBusHack/cmap
```
Verify the installation and run:
```
```

### 7.13 scapy-automotive
[https://github.com/secdev/scapy](https://github.com/secdev/scapy)
Scapy works without any external Python modules on Linux and BSD like operating systems. On Windows, you need to install some mandatory dependencies as described in the documentation.

Also note that Scapy comes as a python installation package, so you can install it using pip:
```
pip install scapy
```
To install:
```
git clone https://github.com/secdev/scapy
cd scapy
sudo ./run_scapy
```

### 7.14 TruckDevil
[https://github.com/LittleBlondeDevil/TruckDevil](https://github.com/LittleBlondeDevil/TruckDevil)
```
git clone https://github.com/LittleBlondeDevil/TruckDevil
```
Install dependencies:
```
pip install -r requirements.txt
```
To run:
```
python3 truckdevil.py
```

### 7.15 python-can-j1939  
[https://github.com/juergenH87/python-can-j1939](https://github.com/juergenH87/python-can-j1939)
Install can-j1939:
```
pip install can-j1939
```
Or clone the repository:
```
git clone https://github.com/juergenH87/python-can-j1939
cd python-can-j1939
pip install .
```

### 7.16 cancat ???
[https://github.com/atlas0fd00m/CanCat](https://github.com/atlas0fd00m/CanCat)
```
git clone https://github.com/atlas0fd00m/CanCat
```

**pretty-j1587 ???**
[https://github.com/ainfosec/pretty_j1587](https://github.com/ainfosec/pretty_j1587)
```
git clone https://github.com/ainfosec/pretty_j1587
```
Verify the installation and run:
```
```
**pretty-j1939 ???**  
[https://github.com/nmfta-repo/pretty_j1939](https://github.com/nmfta-repo/pretty_j1939)
```
git clone https://github.com/nmfta-repo/pretty_j1939
```
Verify the installation and run:
```
```

**PLC4TRUCKSDUCK ???**  
[https://github.com/TruckHacking/plc4trucksduck](https://github.com/TruckHacking/plc4trucksduck)
```
git clone https://github.com/TruckHacking/plc4trucksduck
```

## 8. Configuring the User Environment (TODO)
Run the following command to open the .bashrc file:
```
nano ~/.bashrc
```

## [Reduce Debian](https://wiki.debian.org/ReduceDebian)



# References
- [BeagleBone Black](https://beagleboard.org/black)
- [PinMux](https://www.ofitselfso.com/BeagleNotes/BeagleboneBlackPinMuxModes.php)
- [PinConfig](https://www.beyondlogic.org/adding-can-to-the-beaglebone-black/)
- [Pinconfig2](https://www.bacpeters.com/2020/01/25/configuring-the-beaglebone-black-gpio-pins-permanently/)