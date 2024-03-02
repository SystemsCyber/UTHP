SUMMARY = "Beaglebone Black Customization Linux Image."

IMAGE_INSTALL = "packagegroup-core-boot ${CORE_IMAGE_EXTRA_INSTALL}"

IMAGE_LINGUAS = " "

LICENSE = "MIT"

inherit core-image
inherit extrausers

# Set rooffs to 2000 MiB by default
IMAGE_OVERHEAD_FACTOR ?= "1.0"
IMAGE_ROOTFS_SIZE ?= "204800"

IMAGE_INSTALL:append = " i2c-tools"

# Change root password 
EXTRA_USERS_PARAMS = "\
	usermod -p '\$5\$Nx2D0wB1k15\$LYl7n9Tvtwo0fmsbs/frfpm7OuDJj2AIvcdWZfhS99C' root \
	"
