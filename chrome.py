#!/usr/bin/env python3.6
# -*- coding:Utf-8 -*-

import shutil
import os

bck_loc = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/BACKUP.nibjplbnmmklkfnkpecgbffkifmdbjed")
plu_loc = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Extensions/nibjplbnmmklkfnkpecgbffkifmdbjed")

def day():
    if os.path.exists(plu_loc):
        shutil.rmtree(bck_loc)
        shutil.move(plu_loc, bck_loc)
    return True

def night():
    if os.path.exists(bck_loc) and not os.path.exists(plu_loc):
        shutil.copytree(bck_loc, plu_loc)
    return True

def apply_theme(thn:int):
    if thn == 1:
        return day()
    elif thn == 2:
        return night()
    else:
        return False
