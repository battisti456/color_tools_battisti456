import json
import importlib.resources
from typing import overload

from .types import Color, TupleRGB, PillowNamedColor, HexColor, HexColorAlpha, TupleRGBA

with importlib.resources.open_text('color_tools_battisti456','pillow_named_hexcodes.json') as file:
    PILLOW_NAMED_HEXCODES:dict[PillowNamedColor,HexColor] = json.load(file)

def color_to_tuple_rgb(color:Color) -> TupleRGB|TupleRGBA:
    if isinstance(color,str):
        if color in PILLOW_NAMED_HEXCODES:
            return hex_to_tuple(PILLOW_NAMED_HEXCODES[color])
        return hex_to_tuple(color)#type:ignore
    elif isinstance(color,tuple):
        return color

@overload
def hex_to_tuple(color:HexColor) -> TupleRGB:
    ...
@overload
def hex_to_tuple(color:HexColorAlpha) -> TupleRGBA:
    ...
def hex_to_tuple(color:HexColor|HexColorAlpha) -> TupleRGB|TupleRGBA:
    return tuple(int(color[i:i+2],base = 16) for i in range(1,len(color),2))#type:ignore

def tuple_no_alpha(color:TupleRGB|TupleRGBA) -> TupleRGB:
    if len(color) == 3:
        return color
    else:
        return color[:-1]
