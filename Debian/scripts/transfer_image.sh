#!/bin/bash -e


transfer_image() {
    sudo dd if="$1" of="$2" bs=4M status=progress
}

##### Main #####
echo "Welcome to the UTHP microSD card image transfer tool."
echo " ____ ____ ____ ____ "
echo "||U |||T |||H |||P ||"
echo "||__|||__|||__|||__||"
echo "|/__\|/__\|/__\|/__\|"

lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
echo "Select the source device from the above list (e.g. sdb, mmcblk0):"
read -r device
source_device="/dev/$device"

lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
echo "Select the destination device:"
read -r device
destination_device="/dev/$device"

echo "Source device: $source_device"
echo "Destination device: $destination_device"

read -rp "Are you sure you want to proceed with the image transfer? (y/n): " choice
if [[ $choice =~ ^[Yy]$ ]]; then

    transfer_image "$source_device" "$destination_device"

    echo "Image transfer completed successfully."
else
    echo "Image transfer aborted."
fi
