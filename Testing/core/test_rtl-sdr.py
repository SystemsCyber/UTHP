import os
import subprocess
import pytest

def test_rtl_sdr_help():
    """Test that the rtl_sdr help output is correct."""
    command = "rtl_sdr"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Some tools print help text to stderr instead of stdout, so combine both.
    output = result.stdout + result.stderr
    print("rtl_sdr output:", output)  # For debugging purposes.
    
    # List of expected phrases taken from the rtl_sdr help output.
    expected_phrases = [
        "rtl_sdr, an I/Q recorder for RTL2832 based DVB-T receivers",
        "Usage:",
        "-f frequency_to_tune_to [Hz]",
        "[-s samplerate (default: 2048000 Hz)]",
        "[-d device_index (default: 0)]",
        "[-g gain (default: 0 for auto)]",
        "[-p ppm_error (default: 0)]",
        "[-b output_block_size (default: 16 * 16384)]",
        "[-n number of samples to read (default: 0, infinite)]",
        "[-S force sync output (default: async)]",
        "filename (a '-' dumps samples to stdout)"
    ]
    
    for phrase in expected_phrases:
        assert phrase in output, f"Expected phrase '{phrase}' not found in rtl_sdr output"

def test_libusb_package_installed():
    """Test that the libusb-1.0-0 package is installed."""
    command = "dpkg -l | grep libusb"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Combine stdout and stderr for completeness.
    output = result.stdout + result.stderr
    print("dpkg output:", output)  # For debugging purposes.
    
    # The command should succeed.
    assert result.returncode == 0, f"dpkg command failed with return code {result.returncode}"
    
    # Check that the output contains the expected package name.
    assert "libusb-1.0-0" in output, "Expected 'libusb-1.0-0' not found in dpkg output"
