import subprocess
import pytest

def test_modinfo_can_j1939():
    """Test that modinfo for can-j1939 outputs the expected information."""
    command = "modinfo can-j1939"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip()
    print("modinfo output:", output)
    
    # Ensure the command executed successfully.
    assert result.returncode == 0, f"modinfo command failed with return code {result.returncode}"
    
    # Check that expected fields are present.
    expected_fields = [
        "filename:",
        "alias:",
        "author:",
        "license:",
        "description:",
        "depends:",
        "intree:",
        "name:",
        "vermagic:"
    ]
    for field in expected_fields:
        assert field in output, f"Expected field '{field}' not found in modinfo output"
    
    # Optionally, check for specific expected content.
    assert "PF_CAN SAE J1939" in output, "Expected description 'PF_CAN SAE J1939' not found"
    assert "can_j1939" in output, "Expected name 'can_j1939' not found"

def test_config_can_j1939():
    """Test that /proc/config.gz contains 'CONFIG_CAN_J1939=m'."""
    command = "zcat /proc/config.gz | grep CONFIG_CAN_J1939"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout.strip()
    print("config output:", output)
    
    # Ensure the command executed successfully.
    assert result.returncode == 0, f"zcat command failed with return code {result.returncode}"
    
    # Check for the expected configuration setting.
    assert "CONFIG_CAN_J1939=m" in output, "Expected 'CONFIG_CAN_J1939=m' not found in /proc/config.gz"
