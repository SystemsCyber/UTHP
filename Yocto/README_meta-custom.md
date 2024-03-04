### meta-custom Layer

This layer has one main recipe ```bash meta-custom/recipes-core/images/custom-image.bb ``` with the following features:

* Yocto Image inherited
* i2cdetect
* Change the root password

The following are the changes to the kernel

* enabled the i2c-1 for clock sync [TODO: Testing]
* enabled gpio modules
* enabled CAN 

Modified device tree from the build folder ```bash ./tmp/work-shared/beaglebone-yocto/kernel-source/arch/arm/boot/dts/am335x-boneblack.dts ```

```bash
# append at the end of file

&i2c2 {
    status = "disabled";
};

&uart1 {
    status = "disabled";
};

&am33xx_pinmux {
    dcan0_pins: pinmux_dcan0_pins {
        pinctrl-single,pins = <
            AM33XX_IOPAD(0x97C, PIN_INPUT_PULLUP | MUX_MODE2) /* P9_19: d_can0_rx */
            AM33XX_IOPAD(0x978, PIN_OUTPUT_PULLDOWN | MUX_MODE2) /* P9_20: d_can0_tx */
        >;
    };
};
&am33xx_pinmux {
    dcan1_pins: pinmux_dcan1_pins {
        pinctrl-single,pins = <
            AM33XX_IOPAD(0x984, PIN_INPUT_PULLUP | MUX_MODE2) /* P9_24: d_can1_rx */
            AM33XX_IOPAD(0x980, PIN_OUTPUT_PULLDOWN | MUX_MODE2) /* P9_26: d_can1_tx */
        >;
    };
};
&dcan0 {
    status = "okay";
    pinctrl-names = "default";
    pinctrl-0 = <&dcan0_pins>;
    /* Other necessary properties and configurations */
};

&dcan1 {
    status = "okay";
    pinctrl-names = "default";
    pinctrl-0 = <&dcan1_pins>;
    /* Other necessary properties and configurations */
};


&am33xx_pinmux {
    pinctrl-names = "default";
    pinctrl-0 = <&gpio_pins>;

    gpio_pins: pinmux_gpio_pins {
        pinctrl-single,pins = <
            /* GPIO1_28 */
            AM33XX_IOPAD(0x878, PIN_OUTPUT_PULLUP | MUX_MODE7) /* P9_12 */
        >;
    };
};

&i2c1 {
    status = "okay";
};
```
