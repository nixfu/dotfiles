# Qtile workspaces
from libqtile.config import Key, Group, Match
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
    (" ", { 'layout': 'monadtall' }), 
    (" ", { 'layout': 'monadtall' }), 
    (" ", { 'layout': 'monadtall' }), 
    (" ", { 'layout': 'monadtall' }), 
    (" ", { 'layout': 'monadtall' }), 
    (" ", { 'layout': 'monadtall' }), 
    (" ", { 'layout': 'monadtall' }), 
    (" ", { 'layout': 'monadtall' }), 
    (" ", { 'layout': 'floating'  })
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend(
        [
    # Switch to workspace N
            Key([MOD], actual_key, lazy.group[group.name].toscreen()),
    # Send window to workspace N
            Key([MOD, "shift"], actual_key, lazy.window.togroup(group.name))
        ])
