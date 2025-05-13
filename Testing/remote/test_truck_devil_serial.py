import pytest
import os
import sys
import subprocess
import paramiko
import pathlib

# send a serial command to verify init
# "#0500000can0"

# recv serial command to verify recv
# should be in the form: "$0cea000b03ecfe00*"

def cleanup():
    ssh_host = os.getenv("SSH_HOST")
    ssh_user = os.getenv("SSH_USER")
    ssh_pass = os.getenv("SSH_PASS")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, username=ssh_user, password=ssh_pass, timeout=5)

    command = "echo '{}' | sudo -S systemctl stop truckdevil-serial".format(ssh_pass)
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()

    assert exit_status == 0, f"Failed to stop truckdevil-serial: {stderr.read().decode()}"

    ssh.close()

@pytest.fixture(scope="session", autouse=True)
def setup():
    """Initialize the test environment."""
    ssh_host = os.getenv("SSH_HOST")
    ssh_user = os.getenv("SSH_USER")
    ssh_pass = os.getenv("SSH_PASS")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, username=ssh_user, password=ssh_pass, timeout=5)

    command = "echo '{}' | sudo -S systemctl start truckdevil-serial".format(ssh_pass)
    stdin, stdout, stderr = ssh.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()

    assert exit_status == 0, f"Failed to start truckdevil-serial: {stderr.read().decode()}"

    ssh.close()
    
@pytest.fixture(scope="session", autouse=True)
def change_working_dir():
    """Change the working directory and update sys.path for imports."""
    truckdevil_path = pathlib.Path(__file__).parent / ".." / "TruckDevil" / "truckdevil"
    os.chdir(truckdevil_path)
    sys.path.insert(0, truckdevil_path) # needed for python module imports

def test_serial_read_write():
    """Ensure that the truckdevil serial read runs without errors."""
    command = "python3 ./truckdevil.py add_device m2 can0 500000 " + os.getenv("TRUCKDEVIL_PORT") + " run_module read_messages set num_messages 5 print_messages"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
    print(result.stdout)

    assert result.returncode == 0, f"Command failed with return code {result.returncode}"
    assert "error" not in result.stderr.lower(), f"Error in command output: {result.stderr}"

    command = "python3 ./truckdevil.py add_device m2 can0 500000 " + os.getenv("TRUCKDEVIL_PORT") + " run_module send_messages send 0x0CEA000C ECFE00"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
    print(result.stdout)

    assert result.returncode == 0, f"Command failed with return code {result.returncode}"
    assert "error" not in result.stderr.lower(), f"Error in command output: {result.stderr}"

    cleanup()
