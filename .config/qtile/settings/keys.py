# Qtile keybindings
from libqtile.config import Key, EzKey, KeyChord
from libqtile.command import lazy
from .vars import MOD, ALT, R_ALT, TERMINAL

keys = [
    ### My applications quick bindings
    EzKey("M-A-b", lazy.spawn('brave'), desc="Run Browser"),
    EzKey("M-A-f", lazy.spawn('firefox'), desc="Run Browser"),
    EzKey("M-A-n", lazy.spawn(TERMINAL + ' -e ncspot'), desc="Run ncspot"),
    EzKey("M-A-s", lazy.spawn('steam'), desc="Run Steam"),
    EzKey("M-A-s", lazy.spawn('spotify'), desc="Run Spotify Desktop"),

    ### The essentials
    EzKey("M-<Return>", lazy.spawn(TERMINAL), desc="run Terminal"),
    EzKey(
        "M-S-<Return>",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc="dmenu_run /usr/bin executables"),
    EzKey(
        "M-A-<Return>",
        lazy.spawn("rofi -modi drun -show drun -show-icons"),
        desc="rofi application launcher (.desktop) apps"),
    EzKey(
        "M-C-<Return>",
        lazy.spawn("xlunch -input /etc/xlunch/entries.dsv -I 30 -W"),
        desc="xlunch application launcher (.desktop) apps"),
    EzKey("M-<Tab>", lazy.next_layout(), desc="Toggle through layout types"),
    EzKey("M-S-c", lazy.window.kill(), desc="Kill active window"),
    EzKey("M-S-r", lazy.restart(), desc="Restart qtile"),
    EzKey("M-S-q", lazy.shutdown(), desc="Shutdown/exit qtile"),

    ### Switch focus to specific monitor (out of three)
    EzKey("M-w", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    EzKey("M-e", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    EzKey("M-r", lazy.to_screen(2), desc="Keyboard focus to monitor 3"),

    ### Switch focus of monitors
    EzKey("M-<period>", lazy.next_screen(), desc="Move focus to next monitor"),
    EzKey("M-<comma>", lazy.next_screen(), desc="Move focus to prev monitor"),

    ### Treetab controls
    EzKey("M-C-j", lazy.section_up(), desc="Move up a section in treetab"),
    EzKey("M-C-k", lazy.section_down(), desc="Move down a section in treetab"),

    ### Window control
    EzKey("M-j", lazy.layout.up(), desc="Move focus up in current stack pane"),
    EzKey(
        "M-k",
        lazy.layout.down(),
        desc="Move focus down in current stack pane"),
    EzKey(
        "M-S-j",
        lazy.layout.shuffle_up(),
        desc="Move widnows up in current stack"),
    EzKey(
        "M-S-k",
        lazy.layout.shuffle_down(),
        desc="Move windows down in current stack"),
    EzKey(
        "M-S-f", lazy.window.toggle_floating(), desc="Toggle window floating"),
    EzKey(
        "M-S-m",
        lazy.window.toggle_fullscreen(),
        desc="Toggle window fullscreen"),

    ### Window Sizing
    EzKey(
        "M-h",
        lazy.layout.shrink(),
        lazy.layout.decrease_master(),
        desc='Shrink window, decrease number in master pane (Tile)'),
    EzKey(
        "M-l",
        lazy.layout.grow(),
        lazy.layout.increase_master(),
        desc='Expand window, decrease number in master pane (Tile)'),
    EzKey("M-n", lazy.layout.normalize(), desc="normalize window size"),
    EzKey(
        "M-m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum size"),

    ### Stack controls
    EzKey(
        "M-S-<space>",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side the main pane occupies(XmonadTall)'),
    EzKey(
        "M-<space>",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'),

    ### Media Controls
    EzKey(
        "<XF86AudioRaiseVolume>",
        lazy.spawn("amixer -c 0 -q set Master 1%+"),
        desc="Volume UP media key"),
    EzKey(
        "<XF86AudioLowerVolume>",
        lazy.spawn("amixer -c 0 -q set Master 1%-"),
        desc="Volume DOWN media key"),
    EzKey(
        "<XF86AudioMute>",
        lazy.spawn("amixer -q -D pulse sset Master toggle"),
        desc="Volume MUTE media key"),

    ### Dmenu scripts launched using the key chord SUPER+p followed by 'key'
    ### To obtain these handy scripts get them from DistroTube here:
    ### https://gitlab.com/dwt1/dmscripts
    KeyChord(
        [MOD], "p", [
            Key(
                [],
                "e",
                lazy.spawn("./.dmscripts/dmconf"),
                desc='Choose a config file to edit'),
            Key(
                [],
                "i",
                lazy.spawn("./.dmscripts/dmscrot"),
                desc='Take screenshots via dmenu'),
            Key(
                [],
                "k",
                lazy.spawn("./.dmscripts/dmkill"),
                desc='Kill processes via dmenu'),
            Key(
                [],
                "l",
                lazy.spawn("./.dmscripts/dmlogout"),
                desc='A logout menu'),
            Key(
                [],
                "m",
                lazy.spawn("./.dmscripts/dman"),
                desc='Search manpages in dmenu'),
            Key(
                [],
                "r",
                lazy.spawn("./.dmscripts/dmred"),
                desc='Search reddit via dmenu'),
            Key(
                [],
                "s",
                lazy.spawn("./.dmscripts/dmsearch"),
                desc='Search various search engines via dmenu'),
        ]),
    # System: screenlock, reboot, and poweroff (calls a shell script)
    EzKey(
        'A-C-<Delete>',
        lazy.spawn("./.dmscripts/dmlogout"),
        desc="Ctrl-Alt-Del logout/lock"),
]
