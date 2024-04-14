import os
import pytest

def is_git_repository(path):
    """Check if a directory contains a .git subdirectory indicating it's a Git repository."""
    return os.path.isdir(os.path.join(path, '.git'))

@pytest.mark.parametrize("project", [
    "BBB_Variants",
    "jupyter-lab",
    "canmatrix",
    "cmap",
    "scapy",
    "python-j1939",
    "TruckDevil",
    "cancat",
    "pretty-j1939",
    "pretty-j1587",
    "sigrok",
    "can2",
    "canelloni"
])
def test_git_clone(project):
    """Test if specific projects have been cloned into /home/debian/."""
    project_path = f"/home/debian/{project}"
    assert is_git_repository(project_path), f"{project} should be a Git repository at {project_path}"
