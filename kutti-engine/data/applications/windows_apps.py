"""
Windows Application Registry
"""

from config.user_preferences import (
    DEFAULT_BROWSER,
    CHROME_PROFILE,
)

WINDOWS_APPS = {

    # ======================================================
    # Browsers
    # ======================================================

    # Opens Chrome directly into your selected profile
    "chrome": f'start chrome --profile-directory="{CHROME_PROFILE}"',

    # Generic Browser
    "browser": f'start chrome --profile-directory="{CHROME_PROFILE}"'
    if DEFAULT_BROWSER == "chrome"
    else f"start {DEFAULT_BROWSER}",

    "edge": "start msedge",

    "firefox": "start firefox",

    # ======================================================
    # Editors
    # ======================================================

    "notepad": "start notepad",

    "wordpad": "start write",

    # ======================================================
    # Utilities
    # ======================================================

    "calculator": "start calc",

    "paint": "start mspaint",

    "explorer": "start explorer",

    "cmd": "start cmd",

    "powershell": "start powershell",

    "task manager": "start taskmgr",

    "control panel": "start control",

    "settings": "start ms-settings:",

    # ======================================================
    # Office
    # ======================================================

    "excel": "start excel",

    "word": "start winword",

    "powerpoint": "start powerpnt",
}