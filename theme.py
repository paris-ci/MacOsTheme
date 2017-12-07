#!/usr/bin/env python3.6
# -*- coding:Utf-8 -*-

"""
Change the mac theme. Night, day, and normal

Usage : theme.py [night/day/normal/last/auto]

Theme night :

Set the mac to dark mode

Theme day :

Set the mac to light mode

Theme normal :

Reset wallpaper, that's all
"""
import argparse
import importlib
import sys
from os.path import dirname, basename, isfile, realpath
import glob

from datetime import datetime, timedelta
import pytz

from astral import Astral


import coloredlogs
import logging


def list_modules():

    modules = glob.glob(dirname(realpath(__file__))+"/plugins/*.py")
    return [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


def apply_theme(major:int, minor:int, location:str):

    """Theme number follow these rules:

    Major - Minor
    1 - 1 : Morning (`args.transition` hour before/after sunrise)
      - 2 : Day

    2 - 1 : Evening (`args.transition` hour before/after sunset)
      - 2 : Night"""

    for module in args.modules:
        name = "plugins." + module
        lib = importlib.import_module(name)
        if not hasattr(lib, 'apply_theme'):
            del lib
            del sys.modules[name]
        appendix = ""

        thn = f"{major} - {minor}"

        try:
            ret = lib.apply_theme(major, minor, location)
            if ret:
                logger.info(f"Theme n°{thn} sucessfully applied for {module}")
            else:
                logger.warning(f"Theme n°{thn} not applied for {module}")

        except Exception as e:
            if hasattr(e, 'message'):
                appendix = e.message

            logging.exception(f"Theme n°{thn} ERRORED for module {module}! {appendix}")


# Create a logger object.

logger = logging.getLogger("theme")
coloredlogs.install(level='DEBUG', fmt='%(asctime)s %(levelname)s %(message)s')

# Themes

theme_rules = {"morning": (1, 1),
               "day"    : (1, 2),
               "evening": (2, 1),
               "night"  : (2, 2),}

# Modules

modules = list_modules()

# Arguments


arg_parser = argparse.ArgumentParser(
    description='''ThemePy - Change your mac theme depending on the time of the day''',

    formatter_class=argparse.RawTextHelpFormatter)

arg_parser.add_argument('theme', type=str,
                        help="Specify theme used", nargs='?', default="auto",
                        choices=list(theme_rules.keys()) + ["auto"])

arg_parser.add_argument('--transition_duration', type=int, dest="transition",
                        help="Number of minutes for transitionning modes (morning/evening)", nargs="?", default=60, const=60)

arg_parser.add_argument('--plugins', dest='modules', type=str, nargs='*', default=modules,
                        help="Execute only a list of plugins", choices=modules)

arg_parser.add_argument('-v' '--verbose', action="store_true", dest="verbose",
                        help="Show debug messages")

args = arg_parser.parse_args()

a = Astral()
city_name = 'Paris'
a.solar_depression = 'civil'
city = a[city_name]

theme = args.theme

if theme == "auto":
    sun = city.sun(date=datetime.now(), local=True)

    sr = sun['sunrise'].replace(tzinfo=pytz.UTC)
    now = datetime.now().replace(tzinfo=pytz.UTC)
    ss = sun['sunset'].replace(tzinfo=pytz.UTC)

    td = timedelta(minutes=args.transition)

    if now < sr - td:
        theme = "night"

    elif now < sr + td:
        theme = "morning"

    elif now < ss - td:
        theme = "day"

    elif now < ss + td:
        theme = "evening"
    else:
        theme = "night"

if not args.verbose:
    coloredlogs.install(level='CRITICAL', fmt='%(asctime)s %(levelname)s %(message)s')
else:
    coloredlogs.install(level='DEBUG', fmt='%(asctime)s %(levelname)s %(message)s')

logger.info(f"Applying {theme} theme")

apply_theme(*theme_rules[theme], city_name)







