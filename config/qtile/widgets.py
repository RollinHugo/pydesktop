from libqtile.widget.base import _Widget
from libqtile.widget import TextBox

from colors import Color, Solarized

class ColoredWidgetArray:
    GL_FONT_NAME = "MesloLGS NF"
    GL_FONT_SIZE = 20
    GL_UNICODE_VALUES = {
        'left': '\uE0B0',
        'right': '\uE0B2'
    }

    def __init__(self,
                 widgets: list[_Widget],
                 direction:str=None,
                 include_first:bool=False,
                 include_last:bool=False,
                 font_name:str=None,
                 font_size:int=None,
                 unicode_values:dict[str,str]=None,
                 colors:list[Color]=None
            ):
        assert direction is None or direction in ('left', 'right')
        assert isinstance(widgets, list) and len(widgets) > 0
        self.font_name = self.GL_FONT_NAME if font_name is None else font_name
        self.font_size = self.GL_FONT_SIZE if font_size is None else font_size
        self.unicode_values = self.GL_UNICODE_VALUES if unicode_values is None else unicode_values
        self.direction = 'left' if direction is None else direction
        self.include_first = include_first
        self.include_last = include_last

        self.widgets = []
        self.__is_sep = []

        if include_first:
            self.widgets.append(self.get_separator())
            self.__is_sep.append(True)

        for widget in widgets[:-1]:
            self.widgets.append(widget)
            self.__is_sep.append(False)
            self.widgets.append(self.get_separator())
            self.__is_sep.append(True)

        if len(widgets) > 1:
            self.widgets.append(widgets[-1])
            self.__is_sep.append(False)
        if self.include_last:
            self.widgets.append(self.get_separator())
            self.__is_sep.append(True)

        if colors:
            self.colors = colors
        else:
            self.colors = Solarized
        self.colorize(self.colors)

    def get_separator(self) -> TextBox:
        return TextBox(
            fmt=self.unicode_values[self.direction],
            font=self.font_name,
            fontsize=self.font_size,
            padding=0,
            markup=False,
        )

    def colorize(self, colors:list[str]|list[Color]) -> None:
        assert isinstance(colors, list) and len(colors) > 1
        colors = [str(c) for c in colors]
        c_idx = 1
        c0, c1 = colors[0], colors[1]
        for w_idx in range(len(self.widgets)):
            if self.direction == 'right':
                w_idx = len(self.widgets) - w_idx - 1
            widget = self.widgets[w_idx]
            widget.background = c1
            if not self.__is_sep[w_idx]:
                c_idx = (c_idx + 1) % len(colors)
                c0 = c1
                c1 = colors[c_idx]
            else:
                widget.foreground = c0

