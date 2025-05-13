import subprocess
import re
import pytest
import os
import time
import signal

def test_cli():
    """Ensure that the pretty_j1587 CLI can be run with the help flag."""
    command = "pretty_j1587 -h"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=15)
    print("stdout:", result.stdout)  # For debugging purposes.
    assert result.returncode == 0, f"Command failed with return code {result.returncode}"
    # Check that no error messages appear in stderr.
    assert "error" not in result.stderr.lower(), f"Error in command output: {result.stderr}"


def test_decode_frames():
    """
    Test that the output format from pretty_j1587 is valid.

    This test runs:
      pretty_j1587 
    and verifies that the output contains one or more correctly formatted message blocks.
    Each block is expected to have:
      - A MSG line with a list of hexadecimal values.
      - A MID line with the message identifier.
      - One or more PID lines (each followed by a DATA line).
    """
    command = "pretty_j1587"
    # Start the process in a new process group so we can send it a SIGINT.
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, preexec_fn=os.setsid)

    # Allow the process to run for 15 seconds.
    time.sleep(15)
    # Send SIGINT (Ctrl+C) to the process group.
    os.killpg(proc.pid, signal.SIGINT)
    
    try:
        # Allow a few seconds for the process to clean up.
        stdout, stderr = proc.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, stderr = proc.communicate()

    print("stdout:", stdout)  # For debugging purposes.
    print("stderr:", stderr)  # For debugging purposes.

    # Ensure that some output was captured.
    assert stdout, "No output received from pretty_j1587."

    # Define regular expressions for each expected line.
    msg_pattern = re.compile(r"^MSG: \[[^\]]+\]")
    mid_pattern = re.compile(r"^MID 0x[0-9a-fA-F]+ \(\d+\):\s+.+")
    pid_pattern = re.compile(r"^PID 0x[0-9a-fA-F]+ \(\d+\):\s+.+")
    data_pattern = re.compile(r"^\s+DATA:\s+0x[0-9a-fA-F]+(?:,\s*0x[0-9a-fA-F]+)*")

    lines = stdout.splitlines()
    i = 0
    # Process each block
    while i < len(lines):
        # Skip empty lines.
        if lines[i].strip() == "":
            i += 1
            continue

        # Check MSG line.
        assert msg_pattern.match(lines[i]), f"Line {i+1} does not match MSG format: {lines[i]}"
        i += 1

        # Ensure there is a MID line.
        assert i < len(lines), "Expected MID line after MSG, but reached end of output."
        assert mid_pattern.match(lines[i]), f"Line {i+1} does not match MID format: {lines[i]}"
        i += 1

        # Process one or more PID/DATA pairs.
        # There should be at least one PID/DATA pair following the MID line.
        pid_data_found = False
        while i < len(lines) and lines[i].strip() != "":
            # PID line.
            if not lines[i].startswith("PID"):
                break  # If the line does not start with PID, assume block ended.
            assert pid_pattern.match(lines[i]), f"Line {i+1} does not match PID format: {lines[i]}"
            i += 1

            # DATA line must immediately follow.
            assert i < len(lines), "Expected DATA line after PID, but reached end of output."
            assert data_pattern.match(lines[i]), f"Line {i+1} does not match DATA format: {lines[i]}"
            i += 1
            pid_data_found = True

        assert pid_data_found, "No PID/DATA pairs found in a message block."

    # If we reach here, the output format is valid.
    

def test_j1939db_json_exists():
    """Test that the required files exist at their expected locations."""
    file_path_j1587 = "/opt/uthp/J1587/J1587_201301.pdf.txt"
    file_path_j1708 = "/opt/uthp/J1708/J1708_201609.pdf.txt"
    assert os.path.isfile(file_path_j1587), f"Expected file {file_path_j1587} does not exist."
    assert os.path.isfile(file_path_j1708), f"Expected file {file_path_j1708} does not exist."
