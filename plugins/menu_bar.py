import os
from plugins.utils import utils



def dark_mode(status:bool):

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



def day():
    dark_mode(False)
    return True

def night():
    dark_mode(True)
    return True


def normal():
    return False

def apply_theme(thn:int):
    if thn == 1:
        return day()
    elif thn == 2:
        return night()
    elif thn == 3:
        return normal()
    else:
        return False

