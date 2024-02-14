from libqtile.config import Screen
from libqtile import bar
from .widgets import primary_widgets


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.92)


screens = [Screen(top=status_bar(primary_widgets))]
