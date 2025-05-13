import pytest
import subprocess
import os
import sys

@pytest.fixture(scope="session", autouse=True)
def change_working_dir():
    """Change the working directory and update sys.path for imports."""
    truckdevil_path = "/opt/uthp/programs/truckdevil"
    os.chdir(truckdevil_path)
    sys.path.insert(0, truckdevil_path) # needed for python module imports

def test_installation():
    """Ensure the truckdevil package is installed."""
    try:
        import truckdevil
    except ImportError:
        pytest.fail("Truckdevil package is not installed.")

def test_read():
    """Ensure that the truckdevil read script runs without errors."""
    command = "python3 ./truckdevil.py add_device socketcan can0 500000 run_module read_messages set num_messages 5 print_messages"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
    print(result.stdout)

    assert result.returncode == 0, f"Command failed with return code {result.returncode}"
    assert "error" not in result.stderr.lower(), f"Error in command output: {result.stderr}"

def test_write():
    """Ensure that the truckdevil write script runs without errors."""
    command = "python3 ./truckdevil.py add_device socketcan can0 500000 run_module send_messages send 0x0CEA000B ECFE00"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
    print(result.stdout)

    assert result.returncode == 0, f"Command failed with return code {result.returncode}"
    assert "error" not in result.stderr.lower(), f"Error in command output: {result.stderr}"

