# Repository Updates

## [Version 0.1.5] - UTHP Kirkstone - 2024-06-05

### Added
- This file for tracking updates

### Changed
- Yocto/README.md -> Yocto/YOCTOBuildInstructions.md -> Yocto/README.md
- Yocto/conf.samples/bblayers.conf.sample -- changed structure to match the new Yocto build instructions
- Yocto/meta-custom/recipes-core/images/custom-image.bb:
    - Deleted DEV_EXTRA's ntp because systemd-timesyncd is already included in the image
    - Deleted rsync because it is not needed
    - Deleted tcpdump because it is not needed
    - Deleted usbinit recipe because it is a SysV init script and not needed
    - Deleted gpio-expansion-mapping recipe because it is a SysV init script and not needed
    - Changed the passwords
    - Removed the 'CORE_IMAGE_EXTRA_INSTALL' variable
    - Deleted recipes-pru

### Fixed
- n/a

### Removed
- Any web development recipes in respect to deliverables

## Ultimate Truck Hacking Platform (UTHP)

Welcome to the Ultimate Truck Hacking Platform (UTHP) repository. This repository contains the source code and documentation for the UTHP project. 
1. To get started on the debian version of the UTHP, please refer to the OSBuildInstructions document under the `UTHP/Operating System` directory. 
2. To get started on the yocto version of the UTHP, please refer to the README.md document under the `UTHP/Yocto` directory.
3. Examples of software that can be run on the UTHP are located under the `UTHP/Examples` directory.
