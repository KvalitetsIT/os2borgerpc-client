"""Module for update-related utilities."""

import traceback
import sys
import subprocess
from os2borgerpc.client.config import get_config, has_config

def update_client():
    """Update the client via pip."""
    try:
        installUrl = get_config("client_update_url") if has_config("client_update_url") else "git+https://github.com/KvalitetsIT/os2borgerpc-client.git"
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-U", installUrl ]
        )
        sys.exit(0)
    except subprocess.CalledProcessError:
        print("update_client failed\n", file=sys.stderr)
        traceback.print_exc()