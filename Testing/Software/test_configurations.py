import pytest
import subprocess

def read_sysfs_file(path):
    """Helper function to read content from a sysfs file."""
    try:
        with open(path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        pytest.fail(f"Failed to read {path}: {str(e)}")

def check_interface_enabled(interface_path):
    """Check if a given interface (I2C, SPI, UART) is enabled by reading sysfs or configfs."""
    content = read_sysfs_file(interface_path)
    return content.lower() in ['1', 'enabled', 'true', 'yes']

@pytest.mark.parametrize("pin_config,expected_value", [
    ("/sys/kernel/debug/pinctrl/44e10800.pinmux/pins_pin_24", "0x32"),  # Adjust path and value
    ("/sys/kernel/debug/pinctrl/44e10800.pinmux/pins_pin_28", "0x32")   # for actual CAN0 and CAN1 settings
])
def test_pin_muxing(pin_config, expected_value):
    """Test pin muxing settings for CAN interfaces."""
    assert read_sysfs_file(pin_config) == expected_value, f"Pin configuration for {pin_config} should be {expected_value}"

@pytest.mark.parametrize("interface,enabled", [
    ("/sys/class/i2c-adapter/i2c-0/status", "enabled"),  # Example path, adjust as necessary
    ("/sys/class/spi-master/spi0/status", "enabled"),
    ("/sys/class/tty/ttyO0/status", "enabled")  # Example for UART, adjust path as needed
])
def test_interface_enabled(interface, enabled):
    """Test whether interfaces like I2C, SPI, and UART are enabled."""
    assert check_interface_enabled(interface), f"{interface} should be enabled"
