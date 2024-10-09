"""Module for update-related utilities."""

import traceback
import sys
import subprocess

def update_client():
    """Update the client via pip."""
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-U", "git+https://github.com/KvalitetsIT/os2borgerpc-client.git@feature/OS-20-aendring-af-admin-site"] # TODO Change URL to relase version
        )
        sys.exit(0)
    except subprocess.CalledProcessError:
        print("update_client failed\n", file=sys.stderr)
        traceback.print_exc()