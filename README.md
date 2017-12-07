# MacOsTheme
Set your Mac Os theme depending on the time of the day, the weather and more...

# How does it works

This is a Python3.6+ script that works on Mac Os only. There is a plugin system, and each plugin change a specific part of the OS or it's apps

# Installation

- Install Python 3.6 `brew install python3`
- Clone the repo `git clone https://github.com/paris-ci/MacOsTheme.git`
- Simlink theme.py to a directory in your PATH `ln -s /Users/your_user/theme/theme.py /usr/local/bin/theme`
- In your crontab (`crontab -e`), add `* * * * * theme --plugins wallpaper menu_bar > /dev/null 2>&1` (Don't forget to set your PATH there too)
- You'll probably need to install each plugin separately. For this, see instructions at the beginning of each plugin.py file
