import os
import subprocess
import pytest

def test_rtc_dmesg():
    """
    Verify that RTC-related messages are present in the kernel log.

    This test runs 'dmesg | grep rtc' and checks for a string like 'registered as rtc'.
    """
    result = subprocess.run("dmesg | grep rtc", shell=True, capture_output=True, text=True)
    output = result.stdout + result.stderr
    print("dmesg rtc output:\n", output)
    # Check that the output contains a registration message for an RTC device.
    assert "registered as rtc" in output, "RTC not found in dmesg logs"

def test_rtc_device_exists():
    """
    Verify that an RTC device is present on the system.

    This test checks if either /dev/rtc0 or /dev/rtc1 exists.
    """
    rtc0 = "/dev/rtc0"
    rtc1 = "/dev/rtc1"
    print(f"Checking for {rtc0} or {rtc1}")
    assert os.path.exists(rtc0) or os.path.exists(rtc1), "No RTC device found in /dev (rtc0 or rtc1 missing)"