from typing import Self, Optional
from random import choices
import re

class Color:
    RE_COLOR = re.compile(r"^#[1234567890abcdefABCDEF]{6}$")

    def __init__(self, color:str):
        if not self.RE_COLOR.match(color):
            raise ValueError(f"Invalid color : {color}")
        self.color = color

    @classmethod
    def random_colors(cls, k:int=1) -> list[Self]:
        return [cls.random_color() for _ in range(k)]

    @classmethod
    def random_color(cls) -> Self:
        return cls('#' + ''.join(choices('0123456789ABCDEF', k=6)))

    @property
    def c(self):
        return self.color

    def __str__(self):
        return self.color

    def __repr__(self):
        return f'Color("{self.color}")'


S_base03 = Color('#002b36')
S_base02 = Color('#073642')
S_base01 = Color('#586e75')
S_base00 = Color('#657b83')
S_base0 = Color('#839496')
S_base1 = Color('#93a1a1')
S_base2 = Color('#eee8d5')
S_base3 = Color('#fdf6e3')

S_yellow = Color('#b58900')
S_orange = Color('#cb4b16')
S_red = Color('#dc322f')
S_magenta = Color('#d33682')
S_violet = Color('#6c71c4')
S_blue = Color('#268bd2')
S_cyan = Color('#2aa198')
S_green = Color('#859900')

Solarized = [
    S_yellow,
    S_yellow,
    S_orange,
    S_red,
    S_magenta,
    S_violet,
    S_blue,
    S_cyan,
    S_green
]