from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"

keys = [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    Key ([mod], "j", lazy.layout.down()),
    Key ([mod], "k", lazy.layout.up()),
    Key ([mod], "h", lazy.layout.left()),
    Key ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    Key ([mod, "shift"], "l", lazy.layout.grow()),
    Key ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    Key ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    Key ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    Key ([mod], "Tab", lazy.next_layout()),
    Key ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    Key ([mod], "w", lazy.window.kill()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),

    Key ([mod, "control"], "q", lazy.shutdown()),
    Key ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    Key([mod], "b", lazy.spawn("firefox")),

    # File Explorer
    Key([mod], "e", lazy.spawn("pcmanfm")),

    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 2400")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),

]
