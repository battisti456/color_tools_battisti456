import json
import importlib.resources
from typing import overload

from .types import Color, TupleRGB, PillowNamedColor, HexColor, HexColorAlpha, TupleRGBA, IntegerColor, IntegerColorAlpha
from .exceptions import InvalidColor

with importlib.resources.open_text('color_tools_battisti456','pillow_named_hexcodes.json') as file:
    PILLOW_NAMED_HEXCODES:dict[PillowNamedColor,HexColor] = json.load(file)

def color_to_tuple_rgb(color:Color) -> TupleRGB|TupleRGBA:
    if isinstance(color,str):
        if color in PILLOW_NAMED_HEXCODES:
            return hex_to_tuple(PILLOW_NAMED_HEXCODES[color])
        return hex_to_tuple(color)#type:ignore
    elif isinstance(color,tuple):
        return color
    elif isinstance(color,int):
        return color_to_tuple_rgb(integer_to_hex(color))
def color_to_integer_rgb(color:Color) -> IntegerColor|IntegerColorAlpha:
    return hex_to_integer(tuple_to_hex(color_to_tuple_rgb(color)))

@overload
def tuple_to_hex(color:TupleRGB) -> HexColor:
    ...

@overload
def tuple_to_hex(color:TupleRGBA) -> HexColorAlpha:
    ...

def tuple_to_hex(color:TupleRGB|TupleRGBA) -> HexColor|HexColorAlpha:
    to_return = "#"
    for val in color:
        hex_val = hex(val)[2:]
        if len(hex_val) == 1:
            hex_val = '0' + hex_val
        to_return += hex_val

    return to_return#type:ignore

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

@overload
def integer_to_hex(color:IntegerColor) -> HexColor:
    ...
@overload
def integer_to_hex(color:IntegerColorAlpha) -> HexColorAlpha:
    ...

def integer_to_hex(color:IntegerColor|IntegerColorAlpha) -> HexColor|HexColorAlpha:
    py_hex:str=  hex(color)
    if len(py_hex) not in (8,10):
        raise InvalidColor(f"Color integer '{color}' results in hex code '{py_hex}' which does not have the correct number of bits to be a hex color.")
    return "#" + py_hex[2:]#type:ignore

@overload
def hex_to_integer(color:HexColor) -> IntegerColor:
    ...

@overload
def hex_to_integer(color:HexColorAlpha) -> IntegerColorAlpha:
    ...

def hex_to_integer(color:HexColor|HexColorAlpha) -> IntegerColor|IntegerColorAlpha:
    return int(color[1:],16)#type:ignore