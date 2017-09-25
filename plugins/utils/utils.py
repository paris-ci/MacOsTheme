# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import subprocess


def exec_applescript(script:str):
    SCRIPT = "/usr/bin/osascript<<ENDOFFILEPLEASE\n" + script + "\nENDOFFILEPLEASE"
    subprocess.Popen(SCRIPT, shell=True)

