import os
import sys
import pytest

@pytest.fixture(scope="session", autouse=True)
def change_working_dir():
    """Change the working directory and update sys.path for imports."""
    cmap_path = "/opt/uthp/programs/cmap"
    os.chdir(cmap_path)
    sys.path.insert(0, cmap_path) # needed for python module imports

def test_installation():
    """Ensure the cmap package is installed."""
    try:
        from lib.uds_node import UDSNode
        from lib.net_can_bus import NetworkCanBus
        from lib.service import Service
    except ImportError:
        pytest.fail("CMAP package is not installed or not in Python path.")

def test_directories():
    """Check if all necessary directories exist in the cloned repo."""
    required_dirs = ["venv", "lib", "old"]
    missing_dirs = [d for d in required_dirs if not os.path.isdir(d)]
    
    if missing_dirs:
        pytest.fail(f"Missing directories: {', '.join(missing_dirs)}")
