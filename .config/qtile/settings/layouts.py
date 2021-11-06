# Layouts and layout rules
from libqtile import layout
from libqtile.config import Match
from .theme import colors

layout_conf = {
    'border_focus': 'DEE2EC',
    'border_normal': '1D2330',
    'border_width': 3,
    'margin': 16
}

layouts = [
    layout.Max(),
    layout.MonadTall(ratio=0.65,**layout_conf),
    layout.MonadWide(**layout_conf),
    #layout.Bsp(**layout_conf),
    #layout.Matrix(**layout_conf),
    layout.RatioTile(**layout_conf),
    #layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    #layout.Zoomy(),
    #layout.Floating(),
]

floating_layout = layout.Floating(float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(wm_class='Conky'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
        Match(wm_class='pinentry-gtk-2'),
        Match(title='Confirmation'), 
        Match(title='Qalculate!'),
        Match(title='GRLevel3'), 
        Match(wm_type='utility'),
        Match(wm_type='notification'),
        Match(wm_type='toolbar'),
        Match(wm_type='splash'),
        Match(wm_type='dialog'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='DBeaver'),
    ],
    border_focus=colors["color4"][0])
