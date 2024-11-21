from libqtile.config import Key
from libqtile.lazy import lazy
win = "mod4"
keys = [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    Key ([win], "j", lazy.layout.down()),
    Key ([win], "k", lazy.layout.up()),
    Key ([win], "h", lazy.layout.left()),
    Key ([win], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    Key ([win, "shift"], "l", lazy.layout.grow()),
    Key ([win, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    Key ([win, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    Key ([win, "shift"], "j", lazy.layout.shuffle_down()),
    Key ([win, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    Key ([win], "Tab", lazy.next_layout()),
    Key ([win, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    Key ([win], "w", lazy.window.kill()),

    # Restart Qtile
    Key([win, "control"], "r", lazy.restart()),

    Key ([win, "control"], "q", lazy.shutdown()),

    # ------------ App Configs ------------

    Key([win], "space", lazy.spawn("rofi -show drun")),

    Key([win], "b", lazy.spawn("librewolf")),

    Key([win], "e", lazy.spawn("nemo")),

    Key([win], "s", lazy.spawn("scrot '%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'")),

    Key([win], "Return", lazy.spawn("kitty")),
]
