import json
import importlib.resources
from math import dist

from .types import Color, HexColor, TupleRGB
from .common import color_to_tuple_rgb, hex_to_tuple, tuple_no_alpha

with importlib.resources.open_text('color_tools_battisti456','color_names.json') as file:
    HEX_COLOR_NAMES:dict[HexColor,str] = json.load(file)
TUPLE_COLOR_NAMES:dict[TupleRGB,str] = {hex_to_tuple(color):name for color,name in HEX_COLOR_NAMES.items()}

def color_name(color:Color) -> str:
    rgb = tuple_no_alpha(color_to_tuple_rgb(color))
    min_dist:float = 300
    min_name:str = ""
    for value,name in TUPLE_COLOR_NAMES.items():
        d = dist(rgb,value)
        if d < min_dist:
            min_dist = d
            min_name = name
    return min_name
