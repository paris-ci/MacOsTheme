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

def normal():
    pass

def apply_theme(thn:int):
    if thn == 1:
        return day()
    elif thn == 2:
        return night()
    elif thn == 3:
        return normal()
    else:
        return False

