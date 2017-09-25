#!/usr/bin/env python3.6
# -*- coding:Utf-8 -*-


"""

"""
import os

from plugins.utils import utils


def change_wallpaper(image):
    script_path = os.path.dirname(os.path.realpath(__file__)) + "/wallpaper/"

    if os.path.isfile(image):
        path = image
    elif os.path.isfile(script_path + "/" + image):
        path = script_path + "/" + image
    elif os.path.isfile(script_path + "/" + image + ".png"):
        path = script_path + "/" + image + ".png"
    elif os.path.isfile(script_path + "/" + image + ".jpg"):
        path = script_path + "/" + image + ".jpg"
    else:
        raise FileNotFoundError("Image non trouvée")

    utils.exec_applescript(f"""
    tell application "Finder"
        set desktop picture to POSIX file "{path}"
    end tell
    """)


def day():
    change_wallpaper("day")
    return True


def night():
    change_wallpaper("night")
    return True


def normal():
    change_wallpaper("normal")
    return True

def apply_theme(thn:int):
    if thn == 1:
        return day()
    elif thn == 2:
        return night()
    elif thn == 3:
        return normal()
    else:
        return False

