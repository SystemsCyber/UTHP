import pytest
import subprocess
import importlib

def test_installation():
    """Ensure the cancat package is installed."""
    try:
        importlib.import_module("cancatlib")
    except ImportError:
        pytest.fail("Cancat package is not installed.")

def test_cli():
    """Ensure that the cancat CLI can be run."""
    command = "CanCat -h" # can't use without a M2
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout) # print the output of the command for -s flag

    assert result.returncode == 0, f"Command failed with return code {result.returncode}"
    assert "error" not in result.stderr.lower(), f"Error in command output: {result.stderr}"
