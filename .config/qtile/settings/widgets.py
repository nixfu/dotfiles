from .theme import colors
from .vars import MOD, TERMINAL, SCRIPT_DIR, BIN_DIR, MY_WX
import os
import socket
import subprocess
from libqtile import widget, bar, pangocffi, utils, hook, qtile

# Use environment vars for some personalized option values
# set this env vars in the .xprofile file via export WTTR_LOCATION="" etc.
stockticker_apikey=os.environ.get('STOCKTICKER_APIKEY','')
stockticker_symbol=os.environ.get('STOCKTICKER_SYMBOL','IBM')
wttr_location=os.environ.get('WTTR_LOCATION','')

# create some shortcuts for colors
text = colors['text'][0]
dark = colors['dark'][0]
light = colors['light'][0]
active = colors['active'][0]
inactive = colors['inactive'][0]
focus = colors['focus'][0]
urgent = colors['urgent'][0]
color1 = colors['color1'][0]
color2 = colors['color2'][0]
color3 = colors['color3'][0]
color4 = colors['color4'][0]


def base(fg='text', bg='dark'):
    return {'foreground': colors['light'], 'background': colors['dark']}

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=14, text="?"):
    return widget.TextBox(
        **base(fg, bg), fontsize=fontsize, text=text, padding=3)

widget_defaults = dict(
    font="Hack Nerd Font Mono", fontsize=14, padding=3, background=colors['dark'])
extension_defaults = widget_defaults.copy()

def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True),
        separator(),
        widget.WindowName(**base(fg='grey'), fontsize=14, padding=5),
        separator(),
    ]


# main bar on primary monitor
primary_widgets = []
primary_widgets_start = [
    separator(),
    *workspaces(),
    separator(),
]
primary_widgets.extend(primary_widgets_start)

primary_widgets_nowplaying = [
    widget.GenPollText(
        update_interval=5, 
        func=lambda: subprocess.check_output(os.path.expanduser("~/.local/bin/scripts/nowplaying.sh")).decode("utf-8"),
        foreground='888888',
    ),
    separator(),
]
if os.path.isfile(os.path.expanduser("~/.local/bin/scripts/nowplaying.sh")):
    primary_widgets.extend(primary_widgets_nowplaying)

primary_widgets_wttr = [
    widget.Wttr(
        location={wttr_location : wttr_location},
        units='s',
        format='%C %c %t/%f %w',
        foreground=colors['color1'],
        mouse_callbacks={
            'Button1':
            lambda: qtile.cmd_spawn(
                TERMINAL + ' -e ' + SCRIPT_DIR + 'show_wx.sh ' + wttr_location)
        },
    ),
    separator(),
]
if wttr_location:
    primary_widgets.extend(primary_widgets_wttr)


# add stockticker widget if env vars defined
primary_widgets_stockticker = [ 
    widget.StockTicker(
        apikey=stockticker_apikey,
        symbol=stockticker_symbol,
        foreground=colors['color3'],
        ),
]
if stockticker_apikey:
    primary_widgets.extend(primary_widgets_stockticker)

primary_widgets_finish = [
    widget.TextBox(
        text=" ₿", padding=0, foreground=colors['color4'], fontsize=12),
    widget.BitcoinTicker(
        foreground=colors['color4'],
        mouse_callbacks={
            'Button1': lambda: qtile.cmd_spawn(TERMINAL + '-e cointop')
        },
        padding=5),
    widget.TextBox(text=" ", foreground=colors['color3'], padding=0),
    widget.Volume(
        foreground=colors['color3'],
        padding=5,
        mouse_callbacks=(
            {
                'Button1':
                lambda: qtile.cmd_spawn(
                    'pactl set-sink-mute @DEFAULT_SINK@ toggle'),
                'Button2':
                lambda: qtile.cmd_spawn('pavucontrol'),
                'Button3':
                lambda: qtile.cmd_spawn(
                    TERMINAL + ' -e ' + SCRIPT_DIR + 'start_spt.sh'),
            }),
    ),
    widget.CheckUpdates(
        update_interval=1800,
        distro="Arch_yay",
        custom_command='checkupdates;paru -Qum',
        display_format="{updates} Updates",
        foreground=colors['color2'],
        colour_have_updates=colors['color2'],
        mouse_callbacks={
            'Button1':
            lambda: qtile.cmd_spawn(TERMINAL + ' -e paru -Syu')
        }),
    widget.TextBox(text="  ", foreground=colors['color1'], padding=0),
    widget.Clock(
        foreground=color1,
        format='%d/%m/%Y - %H:%M ',
        mouse_callbacks=(
            {
                'Button1':
                lambda: qtile.cmd_spawn(
                    TERMINAL + ' -e ' + SCRIPT_DIR + 'show_cal.sh'),
                'Button3':
                lambda: qtile.cmd_spawn(SCRIPT_DIR + 'randomwallpaper.sh'),
            })),
    widget.Systray(background=colors['dark'], padding=5),
    widget.CurrentLayoutIcon(foreground=color2, scale=0.7),
    widget.CurrentLayout(foreground=color2, padding=5),
]
primary_widgets.extend(primary_widgets_finish)


# used when second monitor is connected
secondary_widgets = [
    *workspaces(),
    separator(),
    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
    widget.CurrentLayout(**base(bg='color1'), padding=5),
    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
]
