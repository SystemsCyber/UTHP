# UTHP User Manual

## Table of Contents
- [UTHP User Manual](#uthp-user-manual)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Basic Navigation](#basic-navigation)
  - [Networking](#networking)
  - [LEDS](#leds)
  - [Using the Terminal](#using-the-terminal)
  - [File System Overview](#file-system-overview)
  - [System Services](#system-services)
  - [Software Overview](#software-overview)
    - [PYTHON](#python)
    - [PYTHON-CAN](#python-can)
    - [PYTHON-CAN-J1939](#python-can-j1939)
    - [CAN-UTILS](#can-utils)
    - [CMAP](#cmap)
    - [SCAPY (with CAN support)](#scapy-with-can-support)
    - [TRUCKDEVIL](#truckdevil)
    - [CANCAT](#cancat)
    - [IPython 3](#ipython-3)
    - [Py-HV-Networks](#py-hv-networks)
    - [PLC4TRUCKSduck](#plc4trucksduck)
    - [Pretty-J1939](#pretty-j1939)
    - [Pretty-J1587](#pretty-j1587)
    - [Sigrok](#sigrok)
    - [RTL-SDR](#rtl-sdr)
    - [Tmux](#tmux)
    - [JupyterLab](#jupyterlab)
    - [CanMatrix](#canmatrix)
    - [Cannelloni](#cannelloni)
  - [System Maintenance](#system-maintenance)
  - [Tips and Tricks](#tips-and-tricks)
  - [Troubleshooting](#troubleshooting)
  - [References](#references)
  - [Version History](#version-history)

---

## Introduction

This manual provides guidance on using the Yocto-based Linux operating system on the UTHP. It covers system navigation, networking, installed utilities, and general usage to help you get the most out heavy-vehicle cyber security research and development with the Ultimate Truck Hacking Platform (UTHP).

---

## Getting Started

- **Default Login:**
  > Should be changed immediately after first login.
  - Username: `uthp`
  - Password: `UTHP-R1-XXXX` (where `XXXX` is the last four digits of the serial number)

- **Accessing the UTHP:**
  - Via serial debug port (USB UART)
    - This will usually be `/dev/ttyACM0` on Linux-based systems or `COMx` on Windows. Some programs you can use are:
      - `screen /dev/ttyACM0 115200` (Linux)
      - `PuTTY` or `Tera Term` (Windows)
      - `minicom` (Linux, requires setup)
      - `picocom` (Linux, requires setup)
  - Via SSH over USB or Ethernet (i.e., over USB `ssh uthp@192.168.7.2`)

---

## Basic Navigation

- `ls` – List files in directory
- `cd` – Change directory
- `pwd` – Show current path
- `cp`, `mv`, `rm` – Manage files
- `cat`, `less`, `more`, `nano` – View/edit files
- `df -h` – Check storage space
- `top` or `htop` – View running processes
- `uname -a` – Show kernel and system information
- `pip3 list & apt show & dpkg -l` – List installed packages
- `find / -name <filename>` – Search for files
- `grep <pattern> <file>` – Search for text in files

---

## Networking

- **Check IP address:**
  ```bash
  ip addr show
  ```
  or
  ```bash
  ifconfig
  ```

- **Ping a host:**
  ```bash
  ping google.com
  ```

## LEDS

The UTHP has 4 LEDs on the front panel. The LED states are as follows:
- **Power LED**: Indicates power status (solid blue when power supplied)
- **Status LED**: Indicates system status (flashing green after operating system boot)
- **CAN LED**: Indicate CAN0 bus activity (flashing orange when CAN messages are being received).
- **PLC LED**: Indicates J1708/PLC bus activity (flashing red when PLC messages are being received).

> Each of these LEDs can be controlled via the `/sys/class/leds/` interface. Documentation for this interface can be found at: https://www.kernel.org/doc/Documentation/leds/leds-class.txt.

---

## Using the Terminal

Here are some tips:

- Use `TAB` for autocomplete
- `history` shows previous commands
- Use `Ctrl + C` to cancel a command
- Use `&` to run a process in the background

---

## File System Overview

- `/etc` – Configuration files
- `/bin`, `/sbin` – System binaries
- `/usr/bin` – User applications
- `/root` – Home directory for root
- `/opt/` – Optional software packages (contains custom applications)
- `/var/log/` – Log files for safe-shutdown, j1708, plc, etc.
---

## System Services

- **Start/Stop Services:**
  ```bash
  systemctl start <service>
  systemctl stop <service>
  ```

- **Check status:**
  ```bash
  systemctl status <service>
  ```

- **List all services:**
  ```bash
  systemctl list-units --type=service
  ```

---

## Software Overview

To locate the installed software, you can use the following commands:
```bash
which <command>
whereis <command>
find / -name <command>
```

### PYTHON

Python is a programming language that is widely used for scripting and automation tasks. The UTHP comes with Python 3 (https://docs.python.org/3/) and Python 2 (https://docs.python.org/2.7/) installed.

### PYTHON-CAN

Python library for CAN bus communication: https://python-can.readthedocs.io/en/stable/.

### PYTHON-CAN-J1939

Python library for J1939 protocol: https://j1939.readthedocs.io/en/latest/.

### CAN-UTILS

CAN utils (https://github.com/linux-can/can-utils) is a collection of Linux command-line tools for interacting with CAN (Controller Area Network) interfaces. These tools are commonly used for debugging, testing, and monitoring CAN bus communication. The suite includes utilities like `candump`, `cansend`, `canplayer`, and others. The UTHP has 4 CAN interfaces: `can0`, `can1`, `can2`, and `can3`, each corresponding to can1, can2, can3, and can4 on the UTHP.

### CMAP

Python-based CAN bus enumeration tool: https://github.com/CanBusHack/cmap.

### SCAPY (with CAN support)

Python-based packet manipulation tool: https://scapy.readthedocs.io/en/latest/.

### TRUCKDEVIL

TruckDevil is a Python-based tool for CAN bus analysis and manipulation. It is designed to work with the UTHP and provides a user-friendly interface for interacting with CAN networks: https://github.com/LittleBlondeDevil/TruckDevil. The UTHP includes custom features provided by the forked repository: https://github.com/Spenc3rB/TruckDevil, to include m2 (https://www.macchina.cc/m2-introduction) style encoding over TCP and Serial from the UTHP usb0 and eth0 interfaces.

### CANCAT

CanCat is a m2 focused software, installed on the UTHP for use with the CanCat specific firmware. It provides a way to capture and transmit arbitrary CAN bus messages, an architecture for analyzing and identifying messages, and a manner for data to be shared.

> Note: this requires the purchase of a separate adapter to connect to the UTHP.

Certainly! Here are the detailed descriptions of each software component along with their respective documentation links:

### IPython 3

IPython 3 is an enhanced interactive Python shell offering advanced features such as introspection, rich media, shell syntax, tab completion, and history. It provides a robust environment for Python development, particularly beneficial for data analysis and scientific computing.

Documentation: https://ipython.org/ipython-doc/3/index.html

### Py-HV-Networks

Py-HV-Networks is a Python library that offers simplified interfaces to TruckDuck network interfaces, facilitating interactions with heavy vehicle networks. It streamlines the process of sending and receiving messages over these networks, aiding in the development and testing of vehicle communication protocols.

Repository: https://github.com/TruckHacking/py-hv-networks

### PLC4TRUCKSduck

PLC4TRUCKSduck is a tool designed for the Truck Duck platform, a BeagleBone-based heavy vehicle diagnostic and debugging tool. This software enables users to write to Power Line Carrier (PLC) networks, allowing for diagnostics and interactions with vehicle systems over PLC.

Repository: https://github.com/TruckHacking/plc4trucksduck

### Pretty-J1939

Pretty-J1939 is a Python library that provides utilities for parsing and pretty-printing J1939 protocol messages, commonly used in heavy-duty vehicles for communication and diagnostics. It assists in interpreting raw J1939 data into human-readable formats, aiding in analysis and debugging.

Repository: https://github.com/nmfta-repo/pretty_j1939

### Pretty-J1587

Pretty-J1587 is a tool for decoding and interpreting J1587/J1708 (and J2497) messages. It uses the J1587 and J1708 specification documents as references to provide detailed decodings of these messages, which are used in vehicle diagnostics and communication.

Repository: https://github.com/ainfosec/pretty_j1587

### Sigrok

Sigrok is an open-source suite of software projects for signal analysis. It supports various devices like logic analyzers, oscilloscopes, and multimeters, providing a standardized interface for capturing and analyzing signals. Sigrok is useful for debugging hardware and analyzing communication protocols.

Getting Started Guide: https://sigrok.org/wiki/Getting_started

### RTL-SDR

RTL-SDR refers to a low-cost software-defined radio that uses DVB-T TV tuners with RTL2832U chips. It allows users to receive and decode a wide range of radio signals, making it popular among hobbyists and professionals for applications like radio scanning, signal analysis, and wireless communication experiments.

Quick Start Guide: https://www.rtl-sdr.com/rtl-sdr-quick-start-guide/

### Tmux

Tmux is a terminal multiplexer that enables users to create, access, and control multiple terminal sessions from a single screen. It allows for the detachment and reattachment of sessions, facilitating persistent workflows and multitasking in terminal environments.

Wiki: https://github.com/tmux/tmux/wiki

### JupyterLab

JupyterLab is the next-generation web-based interface for Project Jupyter. It allows users to work with documents and activities such as Jupyter notebooks, text editors, terminals, and custom components in a flexible and integrated manner. JupyterLab supports interactive data science and scientific computing across multiple programming languages.

Documentation: https://jupyterlab.readthedocs.io/

### CanMatrix

CanMatrix is a Python package designed to read and write various CAN (Controller Area Network) database formats. It implements a Python Can Matrix Object that describes the CAN communication and the necessary objects like board units, frames, signals, and values. CanMatrix also includes tools for converting and comparing CAN databases.

Documentation: https://canmatrix.readthedocs.io/

### Cannelloni

Cannelloni is a tool that tunnels CAN (Controller Area Network) traffic over Ethernet networks. It uses protocols like UDP, TCP, or SCTP to transfer CAN frames between machines, enabling remote CAN communication and integration over IP networks.

Repository: https://github.com/mguentner/cannelloni

These tools collectively enhance the capabilities of the UTHP, providing a comprehensive suite for interacting with, analyzing, and manipulating vehicle communication networks and protocols. 

---

## System Maintenance

- **Check disk usage:**
  ```bash
  df -h
  ```

- **Monitor CPU/memory:**
  ```bash
  top
  ```

- **Edit startup scripts:**
  - `/etc/rc.local` or `systemd` services

---

## Tips and Tricks

- Create aliases in `.bashrc` for common commands

- To reboot:
  ```bash
  reboot
  ```

- To shut down:
  ```bash
  poweroff
  ```

- The UTHP has a safe shutdown feature, which is powered by two supercapacitors. The UTHP may need to be charged for a few minutes before the safe shutdown feature will work, and may not boot properly otherwise.
---

## Troubleshooting

- **No internet via USB?**
  - Check if `usb0` is up: `ip addr show usb0`
  - Check host-side USB-over-Ethernet driver

- **Device won’t boot?**
  - Check serial debug output (will need to be soldered)
  - Reflash SD card: https://github.com/SystemsCyber/UTHP/releases/

---

## References

- [Yocto Project Documentation](https://docs.yoctoproject.org/)
- [BeagleBone Black Wiki](https://beagleboard.org/black)
- [Systemd Documentation](https://www.freedesktop.org/wiki/Software/systemd/)
- [UTHP GitHub](https://github.com/SystemsCyber/UTHP)
- [meta-uthp GitHub](https://github.com/SystemsCyber/meta-uthp)

---

## Version History
- **Version 1.0** – Initial release 4/8/2025. `TruckHacking OS 1.0.4`
