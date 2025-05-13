import os
import re
import subprocess
import pytest

def test_safe_shutdown_log():
    """
    Verify that the safe-shutdown log exists and contains expected entries.

    The log should have entries like:
      Safe shutdown executed at Fri Feb 28 00:45:15 UTC 2025
    """
    log_file = "/var/log/safe-shutdown.log"
    assert os.path.exists(log_file), f"Log file {log_file} does not exist"

    with open(log_file, "r") as f:
        lines = f.readlines()

    # Ensure that the log file is not empty.
    assert lines, "Log file is empty"

    # Look for at least one valid entry.
    pattern = re.compile(r"^Safe shutdown executed at .+")
    matching_lines = [line for line in lines if pattern.match(line)]
    assert matching_lines, "No valid safe shutdown entries found in the log file"

    # Optionally print matched lines for debugging.
    for line in matching_lines:
        print("Matched log line:", line.strip())

def test_safe_shutdown_service_status():
    """
    Verify that the safe-shutdown service is in an expected state.

    This test checks the status of the service by running:
      systemctl is-active safe-shutdown
    and asserts that its status is 'active'.
    """
    service_name = "safe-shutdown"
    result = subprocess.run(
        ["systemctl", "is-active", service_name],
        capture_output=True,
        text=True
    )
    status = result.stdout.strip()
    print(f"Service {service_name} status: {status}")

    # Expect the service to be active.
    assert status == "active", f"Service {service_name} is not active, status: {status}"

def test_safe_shutdown_service_list_units():
    """
    Verify that the safe-shutdown service is running by checking its entry
    in the output of 'systemctl list-units --type=service --state=running'.

    Expected output should contain a line similar to:
      safe-shutdown.service    loaded active running Check Power Source Service
    """
    command = "systemctl list-units --type=service --state=running"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout + result.stderr
    print("systemctl list-units output:\n", output)

    # Check that safe-shutdown.service appears in the output.
    assert "safe-shutdown.service" in output, "safe-shutdown.service not found in running services"
    # Check that the service is reported as running.
    assert "running" in output, "safe-shutdown service not reported as running"
    # Check for the expected description.
    assert "Check Power Source Service" in output, "Expected description 'Check Power Source Service' not found in output"