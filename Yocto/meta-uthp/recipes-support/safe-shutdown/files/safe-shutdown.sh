#!/bin/bash -e

# Function to read I2C status
read_i2c_status() {
    result=$(i2cget -y -f 0 0x24 0xA)
    echo $result
}

# Function to shutdown the system
shutdown_system() {
    /sbin/shutdown now -h
}

# Function to check power source
check_power_source() {
    status=$(read_i2c_status)
    if [ "$status" = "0x88" ]; then
        shutdown_system
    else
        # Check again after 2 seconds
        sleep 2
        check_power_source
    fi
}

# Main function
main() {
    check_power_source
}

# Execute main function
main