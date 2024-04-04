SUMMARY = "Beaglebone Black Customization Linux Image."

IMAGE_INSTALL = "packagegroup-core-boot ${CORE_IMAGE_EXTRA_INSTALL}"

IMAGE_LINGUAS = " "

LICENSE = "MIT"

inherit core-image
inherit extrausers
# Python Support
PREFERRED_VERSION_python = "2.7"
# Set rooffs to 2000 MiB by default
IMAGE_OVERHEAD_FACTOR ?= "1.0"
IMAGE_ROOTFS_SIZE ?= "204800"

IMAGE_INSTALL:append = " i2c-tools libgpiod libgpiod-tools libgpiod-dev can-utils python python3 python3-adafruit-bbio gpio-expansion-mapping python3-bitstring python-importlib-metadata python-enum34 python-six python-attrs python-future python-typing python2.7-canmatrix python3-cmap python3-github-cancat"

# Change root password 
EXTRA_USERS_PARAMS = "\
	usermod -p '\$5\$Nx2D0wB1k15\$LYl7n9Tvtwo0fmsbs/frfpm7OuDJj2AIvcdWZfhS99C' root; \
	useradd uthp; \
	usermod -p '\$5\$Nx2D0wB1k15\$LYl7n9Tvtwo0fmsbs/frfpm7OuDJj2AIvcdWZfhS99C' uthp; \
	"
