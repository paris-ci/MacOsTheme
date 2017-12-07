from plugins.utils import utils


def dark_mode(status: bool):
    if status:
        status = "true"
    else:
        status = "false"

    utils.exec_applescript(f"""
    tell application "System Events"
        tell appearance preferences
            set dark mode to {status}
        end tell
    end tell""")


def apply_theme(major, minor, location):
    if major == 1:
        dark_mode(False)
    elif major == 2:
        dark_mode(True)
    else:
        return False

    return True
