# Instructions for setting up Debian on the BeagleBone Black

## 1. Flashing the BeagleBone Black with Debian Linux OS
These steps were taken to build the TruckCape recovery SD card.

1. [Download this image](https://rcn-ee.com/rootfs/release/2023-10-07/bullseye-minimal-armhf/am335x-eMMC-flasher-debian-11.8-minimal-armhf-2023-10-07-2gb.img.xz) or find one from this [forum](https://forum.beagleboard.org/t/debian-11-x-bullseye-monthly-snapshot-2023-10-07/31280)
2. Decompress the image using a utility like 7zip (if your imager doesn’t handle `.xz` files automatically).
3. Use Win32DiskImager, Balena Etcher, Rufus, or similar to burn the image to a 4GB (or larger) SD card. This flasher image will overwrite the onboard eMMC.
4. Insert the SD card into the BeagleBone Black. Power it on (connect USB) **while holding the SD boot button** until all four user LEDs light up. After ~30 seconds, LEDs should start a back-and-forth pattern. Flashing takes ~10–15 minutes depending on SD speed.

---

## 2. Connecting to the BeagleBone Black
You can connect via USB ([how-to](https://www.dummies.com/article/technology/computers/hardware/beaglebone/how-to-connect-the-beaglebone-black-via-serial-over-usb-144981/)) or [via IDE](http://192.168.7.2/ide.html). For security, the IDE port may need to be disabled later.

Use an SSH client (e.g. PuTTY) or serial terminal.

- **USB Network:** `ssh debian@192.168.7.2`
- **Serial:** COM[1-9], baud: `115200`

**Credentials:**
```text
Username: debian
Password: temppwd
```

> ⚠️ Be patient after boot. The board may take a moment to enumerate.

Connect Ethernet for internet, then verify connection:
```bash
sudo ifconfig
ping -c 2 8.8.8.8
```
Successful ping should result in `0% packet loss`.

### Update U-Boot
```bash
sudo /opt/u-boot/bb-u-boot-am335x-evm/install.sh
```

---

## 3. Image Verification
Ensure you’re running the expected image:
```bash
sudo beagle-version | egrep -e 'eeprom' -e 'model' -e 'dogtag' ; uname -a
```
Expected output:
```text
eeprom:[A335BNLT000C2042BBBG0642]
model:[TI_AM335x_BeagleBone_Black]
dogtag:[BeagleBoard.org Debian Bullseye Minimal Image 2023-10-07]
Linux BeagleBone 5.10.168-ti-r72 ...
```

---

## 4. Pin Multiplexing
Ensure `config-pin` is available:
```bash
config-pin -q P9_24
```

### Create pin config script
```bash
sudo nano /etc/pin_config.sh
```
Paste in:
```bash
#!/bin/sh -e
# DCAN1
config-pin p9.24 can
config-pin p9.26 can
# DCAN0
config-pin p9.19 can
config-pin p9.20 can
# UARTs
config-pin p9.21 uart
config-pin p9.22 uart
config-pin p9.11 uart
config-pin p9.13 uart
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
Make it executable:
```bash
sudo chmod +x /etc/pin_config.sh
```

### Create systemd service
```bash
sudo nano /lib/systemd/system/pin_config.service
```
Paste in:
```ini
[Unit]
Description=Setup for BBB

[Service]
Type=simple
ExecStart=/bin/bash /etc/pin_config.sh

[Install]
WantedBy=multi-user.target
```
Enable and start:
```bash
sudo chmod 644 /lib/systemd/system/pin_config.service
sudo systemctl start pin_config.service
sudo systemctl enable pin_config.service
```
Verify:
```bash
sudo systemctl status pin_config.service
```

---

## 5. Configuring DT Overlays
Edit `/boot/uEnv.txt`:
```bash
sudo nano /boot/uEnv.txt
```
Uncomment these lines:
```text
#disable_uboot_overlay_emmc=1
disable_uboot_overlay_video=1
disable_uboot_overlay_audio=1
disable_uboot_overlay_wireless=1
disable_uboot_overlay_adc=1
```
Enable cape-universal:
```text
enable_uboot_cape_universal=1
```
Enable PRU UIO:
```text
uboot_overlay_pru=AM335X-PRU-UIO-00A0.dtbo
```
Verify:
```bash
lsmod | grep uio
```
Expected output:
```text
uio_pruss 16384  0
uio_pdrv_genirq 20480  0
uio 20480  2 uio_pruss,uio_pdrv_genirq
```

---

## 6. Start the Network Interfaces

### Enable CAN Interfaces
Edit:
```bash
sudo nano /etc/network/interfaces
```
Append:
```text
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
Check CAN:
```bash
sudo ifconfig
candump any
```

### Add Virtual CAN (vcan)
Create startup script:
```bash
sudo nano /etc/network/vcan-start.sh
```
Paste:
```bash
#!/bin/sh -e
ip link add type vcan
ip link set vcan0 up
ip link add dev vcan1 type vcan
ip link set vcan1 up
ip link add dev vcan2 type vcan
ip link set vcan2 up
exit 0
```
Make executable and create service:
```bash
sudo chmod +x /etc/network/vcan-start.sh
sudo nano /lib/systemd/system/vcan.service
```
Paste:
```ini
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
sudo systemctl start vcan.service
sudo shutdown -r now
```

Check vcan:
```bash
ifconfig
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

### Install essentials:
```bash
sudo apt update
sudo apt install git can-utils python3-pip tmux rtl-sdr -y
```

### Python Setup
```bash
sudo pip3 install --upgrade pip
pip3 install numpy pandas matplotlib python-can can-isotp scapy jupyterlab ipython canmatrix
```

### Python 2.7
```bash
sudo apt install xz-utils build-essential -y
wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz
xz -d Python-2.7.9.tar.xz
tar -xf Python-2.7.9.tar
cd Python-2.7.9
./configure --prefix=/usr/local
make
sudo make altinstall
python2.7 -V
```

### Jupyter Lab
```bash
jupyter server password
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
Then download can2 decoder: !!!
```
git clone https://github.com/kentindell/canhack/
cd canhack/src/can2
```


### 7.11 py-hv-networks !!!
[https://github.com/TruckHacking/py-hv-networks](https://github.com/TruckHacking/py-hv-networks)
```
git clone https://github.com/TruckHacking/py-hv-networks
```
Then install the package:
```
git clone https://github.com/SystemsCyber/py-hv-networks.git
cd py-hv-networks
sudo python3 setup.py install
pip install -r requirements.txt
```

Additional useful repos (clone and follow individual instructions):
- https://github.com/CanBusHack/cmap
- https://github.com/secdev/scapy
- https://github.com/LittleBlondeDevil/TruckDevil
- https://github.com/juergenH87/python-can-j1939
- https://github.com/atlas0fd00m/CanCat
- https://github.com/ainfosec/pretty_j1587
- https://github.com/nmfta-repo/pretty_j1939
- https://github.com/TruckHacking/plc4trucksduck

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

### 7.15 python-can-j1939   !!!
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

## 8. Configuring the User Environment (TODO)
```bash
nano ~/.bashrc
```

---

## References
- [BeagleBone Black](https://beagleboard.org/black)
- [PinMux](https://www.ofitselfso.com/BeagleNotes/BeagleboneBlackPinMuxModes.php)
- [BeyondLogic CAN Setup](https://www.beyondlogic.org/adding-can-to-the-beaglebone-black/)
- [Permanent GPIO Config](https://www.bacpeters.com/2020/01/25/configuring-the-beaglebone-black-gpio-pins-permanently/)

---

> ⚠️ If something isn’t working, double-check kernel version, pin configurations, and overlay settings.

---

*Created for UTHP BeagleBone Black CAN Development Environment, 2024/2025*

