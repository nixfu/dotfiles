from .theme import colors
from .vars import MOD, TERMINAL, SCRIPT_DIR, BIN_DIR, MY_WX
import os
import socket
import subprocess
from libqtile import widget, bar, pangocffi, utils, hook, qtile
from libqtile.widget import base

# Get the icons used at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

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
    font="Ubuntu Mono", fontsize=12, padding=2, background=colors['dark'])

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
primary_widgets = [
    *workspaces(),
    separator(),
    widget.Image(
        filename="~/.config/qtile/icons/python-white.png",
        scale="False",
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(TERMINAL)}),
    separator(),
    widget.Wttr(
        location={MY_WX: MY_WX},
        units='s',
        format='%C %c %t %w',
        foreground=colors['color3'],
        padding=2,
        mouse_callbacks={
            'Button1':
            lambda: qtile.cmd_spawn(
                TERMINAL + ' -e ' + SCRIPT_DIR + 'show_wx.sh')
        },
    ),
    widget.TextBox(
        text=" ⟳", padding=2, foreground=colors['color1'], fontsize=14),
    widget.CheckUpdates(
        update_interval=1800,
        distro="Arch",
        display_format="{updates} Updates",
        foreground=colors['color1'],
        mouse_callbacks={
            'Button1':
            lambda: qtile.cmd_spawn(TERMINAL + ' -e sudo pacman -Syu')
        }),
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

# used when second monitor is connected
secondary_widgets = [
    *workspaces(),
    separator(),
    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
    widget.CurrentLayout(**base(bg='color1'), padding=5),
    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
]
