from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import win, keys

groups = [Group(i) for i in [
    "  一  ", "  二  ", "  三  ", "  四  ", "  五  ", "  六  ", "  七   ", "  八  ", "  九  ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([win], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([win, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
