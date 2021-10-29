# Settings for qtile
import os

# Modifier keys
ALT = "mod1"    # Left Alt
MOD = "mod4"    # Windows/Super
R_ALT = "mod3"    # Right Alt

# Programs
# TERMINAL = "st"
# TERMINAL = "kitty"
TERMINAL = "alacritty"

# Location of script files (must have a trailing slash!)
SCRIPT_DIR = os.path.expanduser('~/.local/bin/scripts/')
BIN_DIR = os.path.expanduser('~/.local/bin/')

# Whether or not the primary monitor should spawn a systray
# NOTE :: When embedding qtile inside of another desktop environment (such
#         as mate) this should be `False` as the DE systray and qtile's
#         end up fighting each other and both loose...!
WITH_SYS_TRAY = True

MY_WX = 'London'
