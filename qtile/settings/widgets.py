from libqtile import widget
from .theme import colors
from libqtile.lazy import lazy

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
            active="#ffd47e", # color that the groups will have when they have something inside
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

primary_widgets = [
    *workspaces(),

    separator(),

 powerline('color3', 'text'),
 widget.PulseVolume(
     **base(bg='color3',fg='text'),
    limit_max_volume=True,
    fmt=' Audio {}  ',
    step=5,
    volume_app='pavucontrol',
    fontsize=15,
    update_interval=0.1,
    emoji=True,
    emoji_list=['','','',''],
    mouse_callbacks={
        "Button1":lazy.spawn("pavucontrol")
    }
),


    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65,),

    widget.CurrentLayout(**base(bg='color2',fg='text'), padding=5),

    powerline('red', 'color2'),

    widget.ThermalSensor(
        **base(bg='red',fg='text'),
        tag_sensor='Tctl',
        format='   {temp:.0f}{unit}  '
    ),
     widget.NvidiaSensors(
         **base(bg='red',fg='text'),
        format= '󰾲 {temp}°C'
    ),


    powerline('color1', 'red'),

    icon(bg="color1", fontsize=17, text='󰃰 '),

    widget.Clock(**base(bg='color1',fg='text'), format='%H:%M - %d/%m/%Y '),
]

secondary_widgets = [
    *workspaces(),

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

extension_defaults = widget_defaults.copy()
