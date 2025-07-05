
from libqtile import bar, widget
from libqtile.config import Screen

from widgets import ColoredWidgetArray

screens = [
    Screen(
        top=bar.Bar(
        [
                *ColoredWidgetArray(
                    [
                        widget.CurrentLayout(),
                        widget.GroupBox(),
                        widget.Prompt()
                    ],
                    direction='right'
                ).widgets,
                widget.WindowName(),
                *ColoredWidgetArray(
                    [
                        widget.Chord(
                            chords_colors={
                                "launch": ("#ff0000", "#ffffff"),
                            },
                            name_transform=lambda name: name.upper(),
                        ),
                        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                        # widget.StatusNotifier(),
                        widget.Systray(),
                        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                        widget.QuickExit(),
                    ],
                    direction='left'
                ).widgets
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]