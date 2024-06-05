# Repository Updates

## [Version 0.0.4] - UTHP Kirkstone - 2024-06-05

### Added
- This file for tracking updates

### Changed
- Yocto/README.md -> Yocto/YOCTOBuildInstructions.md
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

