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
            margin_y=2,
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
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]

primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        distro='Ubuntu',
        update_interval=1800,
    ),


    powerline('color2', 'color4'),

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

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

extension_defaults = widget_defaults.copy()
