#!/usr/bin/env python3.6
# -*- coding:Utf-8 -*-


"""

"""
import json
import logging
import os

import time
import urllib.parse
import urllib.request

from plugins.utils import utils
import shutil

logger = logging.getLogger("theme")
script_path = os.path.dirname(os.path.realpath(__file__)) + "/wallpaper/"


def get_file_name(prefix, weather_name):
    summaries = {'rain': 'drizzle rain shower',
                 'wind': 'breez gale wind',  # breez matches both breeze and breezy
                 'thunder': 'thunder',
                 'snow': 'snow',
                 'cloudy': 'cloud'}

    def get_weather_summary():
        for summary, words in summaries.items():
            for word in words.split():
                if word in weather_name:
                    return summary
        return 'normal'

    image = get_weather_summary()

    if os.path.isfile(script_path + "/" + image + ".png"):
        imfile = image + ".png"
    elif os.path.isfile(script_path + "/" + image + ".jpg"):
        imfile = image + ".jpg"
    else:
        raise FileNotFoundError("Image non trouvée")

    fn = prefix + '-' + imfile

    logger.debug(f"FileName : {fn}")

    return fn


def change_wallpaper(image_prefix, location):
    weather_json_url = r'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where' \
                       r'%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + \
                       urllib.parse.quote(location) + \
                       '%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

    weather_json = json.loads(urllib.request.urlopen(weather_json_url).read().decode('utf-8'))
    weather = str(weather_json['query']['results']['channel']['item']['condition']['text']).lower()

    for file in os.listdir(script_path + "/Current"):
        if file.endswith(".jpg") or file.endswith(".png"):
            current = file
            break
    else:
        current = ""

    imfile = get_file_name(image_prefix, weather)

    if current == imfile:
        return True

    path = script_path + "/" + imfile

    # utils.exec_applescript(f"""
    # tell application "Finder"
    #    set desktop picture to POSIX file "{path}"
    # end tell
    # """)

    current_dir = script_path + "/current/"
    shutil.rmtree(current_dir, True)
    os.mkdir(current_dir)
    shutil.copyfile(path, current_dir + imfile)

    # "Mac OS X:Library:Desktop Pictures:Plants:"
    utils.exec_applescript(f"""
    tell application "System Events"
        tell current desktop
            set pictures folder to "{current_dir}"
            set picture rotation to 1 -- (0=off, 1=interval, 2=login, 3=sleep)
            set change interval to 1.0 -- seconds
        end tell
    end tell
    """)

    time.sleep(2)

    utils.exec_applescript(f"""
    tell application "System Events"
        tell current desktop
            set pictures folder to "{current_dir}"
            set picture rotation to 1 -- (0=off, 1=interval, 2=login, 3=sleep)
            set change interval to 3600 -- seconds
        end tell
    end tell
    """)


def apply_theme(major, minor, location):
    if major == 1:
        if minor == 1:
            change_wallpaper("morning", location)
        else:
            change_wallpaper("day", location)
    elif major == 2:
        if minor == 1:
            change_wallpaper("evening", location)
        else:
            change_wallpaper("night", location)
    else:
        return False

    return True
