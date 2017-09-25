#!/usr/bin/env python3.6
# -*- coding:Utf-8 -*-

"""
Change the mac theme. Night, day, and normal

Usage : theme.py [night/day/normal/last]

Theme night :

Set the mac to dark mode

Theme day :

Set the mac to light mode

Theme normal :

Reset wallpaper, that's all
"""

import importlib
import sys
from os.path import dirname, basename, isfile
import glob

import coloredlogs
import logging

# Create a logger object.
logger = logging.getLogger(__name__)

# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.



themes = ["night", "day", "normal", "last"]
theme = sys.argv[1]

if not theme in themes:
    logger.critical(f"Invalid theme {theme} passed. Try {themes}")


def list_modules():

    modules = glob.glob(dirname(__file__)+"/plugins/*.py")
    return [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


def apply_theme(thn:int):
    for module in list_modules():
        name = "plugins." + module
        lib = importlib.import_module(name)
        if not hasattr(lib, 'apply_theme'):
            del lib
            del sys.modules[name]
        appendix = ""

        try:
            ret = lib.apply_theme(thn)
            if ret:
                logger.info(f"Theme n°{thn} sucessfully applied for {module}")
            else:
                logger.warning(f"Theme n°{thn} not applied for {module}")

        except Exception as e:
            if hasattr(e, 'message'):
                appendix = e.message

            logging.error(f"Theme n°{thn} ERRORED for module {module}! {appendix}")

ltfilepath = dirname(__file__) + "/last_theme"

if theme == "last":
    with open(ltfilepath, "r") as file:
        theme = file.read()
    coloredlogs.install(level='WARNING', fmt='%(asctime)s %(levelname)s %(message)s')


else:
    coloredlogs.install(level='DEBUG', fmt='%(asctime)s %(levelname)s %(message)s')

if theme == "day":
    apply_theme(1)
elif theme == "night":
    apply_theme(2)
elif theme == "normal":
    apply_theme(3)


with open(ltfilepath, "w") as file:
    file.write(theme)