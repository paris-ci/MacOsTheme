#!/usr/bin/env python3.6
# -*- coding:Utf-8 -*-
"""

"""


def day():
    profile = "Light"
    print(f"\033]50;SetProfile={profile}\a")

    return True


def night():
    profile = "Dark"
    print(f"\033]50;SetProfile={profile}\a")
    return True


def apply_theme(major, minor, location):
    if major == 1:
        day()
    elif major == 2:
        night()
    else:
        return False

    return True
