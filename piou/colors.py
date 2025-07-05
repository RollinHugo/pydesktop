from typing import Self
from random import choices
import re

class Color:
    RE_COLOR = re.compile(r"^#[1234567890abcdefABCDEF]{6}$")

    def __init__(self, color:str):
        if not self.RE_COLOR.match(color):
            raise ValueError(f"Invalid color : {color}")
        self.color = color

    @classmethod
    def random_colors(cls, k:int=None) -> Self|list[Self]:
        if k is None:
            return cls('#' + ''.join(choices('0123456789ABCDEF', k=6)))
        else:
            return [cls.random_colors() for _ in range(k)]

    @property
    def c(self):
        return self.color

    def __str__(self):
        return self.color

    def __repr__(self):
        return f'Color("{self.color}")'
