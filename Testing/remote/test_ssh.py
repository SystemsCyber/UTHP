import os
import re
import pytest
import paramiko

@pytest.mark.parametrize("command", ["echo SSH_SUCCESS"])
def test_ssh_connection(command):
    """Test SSH connection using Paramiko"""
    ssh_host = os.getenv("SSH_HOST")
    ssh_user = os.getenv("SSH_USER")
    ssh_pass = os.getenv("SSH_PASS")

    assert ssh_host and ssh_user and ssh_pass, "SSH credentials are not set!"

    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_host, username=ssh_user, password=ssh_pass, timeout=10)

        # Execute initial test command
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        print("SSH Output:", output)

        assert "SSH_SUCCESS" in output, f"Initial SSH command failed: {error}"
        print("[SUCCESS] SSH authentication verified.")

        # Execute 'whoami' after SSH success
        stdin, stdout, stderr = ssh.exec_command("whoami")
        whoami_output = stdout.read().decode().strip()
        whoami_error = stderr.read().decode().strip()
        stdin, stdout, stderr = ssh.exec_command("echo $HOSTNAME")
        hostname_output = stdout.read().decode().strip()
        print(f"{whoami_output}@{hostname_output}")
        assert whoami_output == ssh_user, f"'whoami' command failed: {whoami_error}"
        assert re.match(r"^UTHP.*", hostname_output), f"Hostname does not match 'UTHP*': {hostname_output}"
    except Exception as e:
        pytest.fail(f"SSH connection failed: {e}")

    finally:
        ssh.close()

def test_root_login_locked():
    """Test that SSH login as root is not permitted (root user is locked)."""
    ssh_host = os.getenv("SSH_HOST")
    ssh_pass = os.getenv("SSH_PASS")
    assert ssh_host and ssh_pass, "SSH credentials are not set!"
    
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Attempt to connect using the root user
        ssh.connect(ssh_host, username="root", password=ssh_pass, timeout=10)
        pytest.fail("Root login succeeded, but it should be locked.")
    except Exception as e:
        # An exception is expected because root login should be locked.
        print("Root login attempt failed as expected:", e)
    finally:
        try:
            ssh.close()
        except Exception:
            pass