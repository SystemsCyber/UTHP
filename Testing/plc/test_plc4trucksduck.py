import pytest
import subprocess
import importlib
import time
import signal
import re
import os

# plc4trucksduck_host needs to be restarted as a service every time this is run

def test_service():
    """Ensure that the plc4trucksduck service is running."""
    command = "systemctl is-active --quiet plc4trucksduck"
    result = subprocess.run(command, shell=True)
    assert result.returncode == 0, "plc4trucksduck service is not running."

def test_installation():
    """Ensure the hv_networks package is installed."""
    try:
        importlib.import_module("hv_networks")
    except ImportError:
        pytest.fail("hv_networks package is not installed.")

def test_send():
    """Ensure that the j1708send command works"""
    command = "j1708send 48656C6C6F2C20504C4321" # Hello, PLC!
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout) # print the output of the command for -s flag
    assert result.returncode == 0, f"Command failed with return code {result.returncode}"
    assert "error" not in result.stderr.lower(), f"Error in command output: {result.stderr}"  
    with open("/var/log/plc4trucksduck.log", "r") as log_file:
        log = log_file.read()
    assert re.search(r"UDP", log), "Message not sent successfully"
    
def test_receive():
    """Ensure that the j1708dump command is force-terminated (with SIGINT) after a timeout."""
    command = "j1708dump --validate true"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(30) # wait for 10 seconds
    process.send_signal(signal.SIGINT)
    result = process.communicate()
    # print the output of the command for -s flag
    print(result[0]) # stdout
    assert "error" not in result[1].lower(), f"Error in command output: {result[1]}"

def test_pru_method_rpmsg():
    """Ensure that the PRU method for rpmsg available in sysfs """
    assert os.path.isdir("/sys/class/rpmsg/") == True, "PRU method for rpmsg not available in sysfs"
