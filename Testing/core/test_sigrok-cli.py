import subprocess
import pytest
import os

def test_sigrok_cli_help():
    """Test that the sigrok-cli help output is correct."""
    command = "sigrok-cli -h"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("sigrok-cli stdout:", result.stdout)  # For debugging purposes.
    print("sigrok-cli stderr:", result.stderr)  # For debugging purposes.

    assert result.returncode == 0, f"sigrok-cli command failed with return code {result.returncode}"
    
    # Verify that expected usage/help strings are present.
    expected_phrases = [
        "Usage:",
        "-h, --help",
        "Application Options:"
    ]
    for phrase in expected_phrases:
        assert phrase in result.stdout, f"Expected phrase '{phrase}' not found in sigrok-cli help output."

def test_libsigrokdecode_files_exist():
    """Test that the required libsigrokdecode files exist."""
    file_init = "/usr/share/libsigrokdecode/decoders/can2/__init__.py"
    file_pd = "/usr/share/libsigrokdecode/decoders/can2/pd.py"
    
    assert os.path.isfile(file_init), f"Expected file {file_init} does not exist."
    assert os.path.isfile(file_pd), f"Expected file {file_pd} does not exist."
