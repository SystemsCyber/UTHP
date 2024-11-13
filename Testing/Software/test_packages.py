import subprocess
import pytest

def check_package_installed(package):
    """Utility function to check if a package is installed via dpkg."""
    try:
        subprocess.run(['dpkg', '-s', package], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def check_command_version(command, expected_version):
    """Utility function to check a command's version."""
    try:
        result = subprocess.run([command, '--version'], stdout=subprocess.PIPE, text=True)
        return expected_version in result.stdout
    except Exception:
        return False

@pytest.mark.parametrize("package", [
    "python2",
    "python3",
    "ipython3",
    "can-utils",
    "curl",
    "wget",
    "nginx",
    "dhcpd",  # Ensure DHCP server package, adjust name if necessary
    "apache2" # Assuming 'httpd' refers to Apache HTTP Server
])
def test_dpkg_package_installed(package):
    """Test that essential dpkg packages are installed."""
    assert check_package_installed(package), f"Package {package} should be installed via dpkg"

def test_ip_command_version():
    """Test that the IP command is the correct version."""
    assert check_command_version('ip', 'ip utility, iproute2-ss'), "IP command should be from iproute2-ss version 2"

def test_nginx_running():
    """Test if the Nginx service is running."""
    assert subprocess.run(['systemctl', 'is-active', 'nginx'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def test_httpd_running():
    """Test if the Apache HTTP Server (httpd) is running."""
    assert subprocess.run(['systemctl', 'is-active', 'apache2'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def test_dhcp_running():
    """Test if the DHCP server is running."""
    assert subprocess.run(['systemctl', 'is-active', 'isc-dhcp-server'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def test_nginx_configuration():
    """Test that Nginx configuration is valid."""
    assert subprocess.run(['nginx', '-t'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
