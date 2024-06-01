from .color_names import color_name
from .common import color_to_tuple_rgb
from .types import Color, TupleRGB, TupleRGBA


def invert(color:Color) -> TupleRGB|TupleRGBA:
    color = color_to_tuple_rgb(color)
    return tuple(255-val for val in color)#type: ignore

__all__ = (
    'color_name',
    'invert'
)