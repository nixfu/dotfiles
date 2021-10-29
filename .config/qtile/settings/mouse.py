from libqtile.config import Drag, Click
from libqtile.command import lazy
from .vars import MOD

mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag(
        [MOD],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front())
]
