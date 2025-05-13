import subprocess
import pytest

def test_python2_version():
    """
    Test that Python 2.7 is installed.
    
    This test runs 'python --version' and checks that the output
    contains 'Python 2.7'. Note that some Python versions output the version
    to stderr, so both stdout and stderr are combined.
    """
    result = subprocess.run(["python", "--version"], capture_output=True, text=True)
    output = result.stdout + result.stderr
    print("python --version output:", output)
    
    assert result.returncode == 0, f"python command failed with return code {result.returncode}"
    assert "Python 2.7" in output, f"Expected Python 2.7 in version output, got: {output}"
