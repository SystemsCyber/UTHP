#!/bin/bash

echo "Please enter the path to your poky directory:"
read POKY_DIR
if [ ! -d "${POKY_DIR}" ]; then
    echo "The specified directory does not exist. Please check the path and try again."
    exit 1
fi

cd "${POKY_DIR}"
source oe-init-build-env
echo "Please enter the full path of your custom 'am335x-boneblack.dts' file:"
read CUSTOM_DTS_PATH

if [ ! -f "${CUSTOM_DTS_PATH}" ]; then
    echo "The specified file does not exist. Please check the path and try again."
    exit 1
fi
if [ "$(basename ${CUSTOM_DTS_PATH})" != "am335x-boneblack.dts" ]; then
    echo "The file must be named 'am335x-boneblack.dts'. Please rename your file and try again."
    exit 1
fi

TARGET_DTS_DIR="${BUILDDIR}/tmp/work-shared/beaglebone-yocto/kernel-source/arch/arm/boot/dts"

echo "Copying custom DTS file to the target directory..."
cp "${CUSTOM_DTS_PATH}" "${TARGET_DTS_DIR}/"

if [ $? -ne 0 ]; then
    echo "Failed to copy the custom DTS file. Please check the paths and permissions."
    exit 1
fi

echo "Custom DTS file copied successfully."

echo "Starting kernel compilation..."
bitbake -c compile -f virtual/kernel

if [ $? -ne 0 ]; then
    echo "Kernel compilation failed. Please check the output for errors."
    exit 1
fi

echo "Kernel compiled successfully."
