import subprocess
import pytest

def test_tmux_help_output():
    """Test that 'tmux --h' produces the expected usage output."""
    # Run the command and capture output from both stdout and stderr.
    result = subprocess.run(["tmux", "--h"], capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    
    # Expected output, as provided.
    expected_output = (
        "usage: tmux [-2CDlNuvV] [-c shell-command] [-f file] [-L socket-name]\n"
        "            [-S socket-path] [-T features] [command [flags]]"
    ).strip()
    
    assert output == expected_output, f"Expected output:\n{expected_output}\nBut got:\n{output}"
