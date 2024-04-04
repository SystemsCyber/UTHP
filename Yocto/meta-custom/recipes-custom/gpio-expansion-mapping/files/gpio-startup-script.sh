#!/bin/sh

### BEGIN INIT INFO
# Provides:          gpio-expansion-mapping
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Startup script to map software GPIOs to expansion pins
# Description:       This script sets up the mapping of software GPIOs to expansion pins during system startup.
### END INIT INFO

# Insert your GPIO mapping commands here using `echo` to export pins
# Example:

# Redirect output to a log file
exec > /var/log/gpio-startup-script.log 2>&1

echo "GPIO Startup Script: Starting up..."


echo 28 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio28/direction

echo "GPIO Startup Script: Configuration applied."
exit 0

