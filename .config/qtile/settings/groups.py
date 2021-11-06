# Qtile workspaces
from libqtile.config import Key, Group, Match, DropDown, ScratchPad
from libqtile.command import lazy
from libqtile import hook
from .keys import keys
from .vars import MOD

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons:
# nf-fa-firefox,
# nf-fae-python,
# nf-dev-terminal,
# nf-fa-code,
# nf-oct-git_merge,
# nf-linux-docker,
# nf-mdi-image,
# nf-mdi-layers

group_names = [
    # workspace 1
    ("爵", { 
        'layout': 'monadtall',
        'matches': [
            Match(wm_class='firefox'), 
            Match(wm_class='brave-browser'),
            Match(wm_class='librewolf')
        ]
    }), 

    # workspace 2
    (" ", { 
        'layout': 'monadtall',
        'matches': [
        ]
    }), 

    # workspace 3
    ("", { 
        'layout': 'monadtall',
        'matches': [
            Match(wm_class='discord'), 
            Match(wm_class='telegram-desktop')
        ]
    }), 

    # workspace 4
    (" ", { 
        'layout': 'monadtall',
        'matches': [
        ]
    }), 

    # workspace 5
    (" ", { 
        'layout': 'monadtall',
        'matches': [
        ]
    }), 

    # workspace 6
    (" ", { 
        'layout': 'monadtall',
        'matches': [
        ]
    }), 

    # workspace 7
    (" ", { 
        'layout': 'monadtall',
        'matches': [
        ]
    }), 

    # workspace 8
    (" ", { 
        'layout': 'monadtall', 
        'matches': [
            Match(wm_class='spotify'),
        ]
    }), 

    # workspace 9
    (" ", { 
        'layout': 'floating',
        'matches': [
            Match(wm_class='Steam'), 
        ]
    })
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([MOD], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([MOD, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

# define dropdown scrathpad
dropdowns = [DropDown('term', 'alacritty', x=0.125, y=0.25,
    width=0.75, height=0.5, opacity=0.8,
    on_focus_lost_hide=True)]
groups.append(ScratchPad("scratch", dropdowns))
keys.extend([
    Key([MOD, "shift"], "s", lazy.group["scratch"].dropdown_toggle("term"))
])


# When application launched automatically focus it's group
@hook.subscribe.client_new
def modify_window(client):
    for group in groups:  # follow on auto-move
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            targetgroup = client.qtile.groups_map[group.name]  # there can be multiple instances of a group
            targetgroup.cmd_toscreen(toggle=False)
            break
