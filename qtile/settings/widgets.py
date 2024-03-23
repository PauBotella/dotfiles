from libqtile import widget
from .theme import colors
from libqtile.command import lazy

def base(fg='light', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=110,
        padding=-2
    )


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
            active="#DFFF00", # color that the groups will have when they have something inside
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]

rofi_command = "rofi -show p -modi p:'rofi-power-menu --symbols-font \"Symbols Nerd Font Mono\"' -font \"UbuntuMono Nerd Font 16\" -theme simple-tokyonight -theme-str 'window {width: 8em;location: northeast;} listview {lines: 6;}'"

primary_widgets = [
    *workspaces(),

    separator(),


    powerline('color3', 'text'),

    icon(bg="color3", text='󰕾 '),
    
    widget.Volume(**base(bg='color3',fg='text'),
                    fmt='Audio',
                    mouse_callbacks = {"Button1":lazy.spawn("pavucontrol"),
                                        "Button4": lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
                                        "Button5": lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")}
),

    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2',fg='text'), padding=5),

    powerline('verderaro', 'color2'),


    icon(bg="verderaro", fontsize=17, text=''),

    widget.ThermalSensor(
        **base(bg='verderaro',fg='text'),
        tag_sensor='Tctl',
        format='   {temp:.0f}{unit}  '
    ),
     widget.NvidiaSensors(
         **base(bg='verderaro',fg='text'),
        format= '󰾲 {temp}°C'
    ),


    powerline('color1', 'verderaro'),

    icon(bg="color1", fontsize=17, text='󰃰 '),

    widget.Clock(**base(bg='color1',fg='text'), format='%H:%M - %d/%m/%Y '),



powerline('color4', 'color1'),


    icon(bg="text", fontsize=17, text=''),

    widget.TextBox(
        **base(bg='color4',fg='text'),
        fmt='⏻  ',
        mouse_callbacks = {"Button1":lazy.spawn(rofi_command)}
    ),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
