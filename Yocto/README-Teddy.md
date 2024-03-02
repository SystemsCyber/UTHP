### meta-custom Layer

This layer has one main recipe ```bash meta-custom/recipes-core/images/custom-image.bb ``` with the following features:

* Yocto Image inherited
* i2cdetect
* Change the root password

The following are the changes to the kernel

* enabled the i2c-1 for clock sync [TODO: Testing]
* enabled gpio modules
* enabled CAN 
