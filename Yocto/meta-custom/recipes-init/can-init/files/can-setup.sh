#!/bin/sh
### BEGIN INIT INFO
# Provides:          can-setup
# Required-Start:    $network
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Set up CAN interfaces
### END INIT INFO

modprobe can
modprobe can_raw
modprobe can_bcm
modprobe can-j1939
# Set up virtual CAN interface (remove if not needed)
ip link add dev vcan0 type vcan
ip link set vcan0 up
ip link add dev vcan1 type vcan
ip link set vcan1 up
# Additional commands for physical CAN interfaces
ip link set can0 type can bitrate 500000
ip link set up can0
ip link set can1 type can bitrate 500000
ip link set up can1
