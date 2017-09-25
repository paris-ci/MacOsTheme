#!/usr/bin/env python3.6
# -*- coding:Utf-8 -*-

"""
Change the mac theme. Night, day, and normal

Usage : theme.py [night/day/normal]
"""
import sys
import subprocess
import os


themes = ["night", "day", "normal"]
theme = sys.argv[1]

if not theme in themes:
    print(f"Invalid theme {theme} passed. Try {themes}")

def exec_applescript(script:str):
    SCRIPT = "/usr/bin/osascript<<ENDOFFILEPLEASE\n" + script + "\nENDOFFILEPLEASE"
    subprocess.Popen(SCRIPT, shell=True)

def change_wallpaper(image):
    script_path = os.path.dirname(os.path.realpath(__file__))

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

    exec_applescript(f"""
    tell application "Finder"
        set desktop picture to POSIX file "{path}"
    end tell
    """)




def dark_mode(status:bool):

    if status:
        status = "true"
    else:
        status = "false"


    exec_applescript(f"""
    tell application "System Events"
        tell appearance preferences
            set dark mode to {status}
        end tell
    end tell""")



def night():
    change_wallpaper("night")
    dark_mode(True)

    exec_applescript("""
    tell application "iTerm"
    	try
    		set _session to «class Cssn» of «class Ctrm»
    	on error
    		tell me to quit
    	end try
    	
    	tell _session
    		-- Apple script colors are specified in RGB,
    		-- with ranges from 0 to 65535.
    		
    		set fg_color to get «class Fcol»
    		
    		if fg_color is {21074, 26471, 28270} then
    			-- Solarized Dark Theme
    			set «class Fcol» to {28873, 33398, 33872}
    			set «class Bcol» to {0, 7722, 9941}
    			set «class bCol» to {33153, 37008, 37008}
    			set «class Scol» to {0, 10280, 12593}
    			set «class Stco» to {33153, 37008, 37008}
    			set «class Ccol» to {28784, 33410, 33924}
    			set «class Ctxt» to {0, 10207, 12694}
    		end if
    	end tell
    end tell
    """)


def day():
    change_wallpaper("day")
    dark_mode(False)

    exec_applescript("""
    tell application "iTerm"
    	try
    		set _session to «class Cssn» of «class Ctrm»
    	on error
    		tell me to quit
    	end try
    	
    	tell _session
    		-- Apple script colors are specified in RGB,
    		-- with ranges from 0 to 65535.
    		
    		set fg_color to get «class Fcol»
    		
    		if fg_color is {28873, 33398, 33872} then
    			-- Solarized Light Theme
    			set «class Fcol» to {21074, 26471, 28270}
    			set «class Bcol» to {64842, 62778, 56626}
    			set «class bCol» to {18134, 23373, 25098}
    			set «class Scol» to {60138, 58339, 52171}
    			set «class Stco» to {18134, 23373, 25098}
    			set «class Ccol» to {21257, 26684, 28737}
    			set «class Ctxt» to {60037, 58326, 52284}
    		end if
    	end tell
    end tell
    """)

def normal():
    change_wallpaper("normal")
    dark_mode(False)


if theme == "night":
    night()
elif theme == "day":
    day()
elif theme == "normal":
    normal()