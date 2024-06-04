#!/bin/sh
/sbin/ip link add dev vcan0 type vcan
/sbin/ip link set up vcan0