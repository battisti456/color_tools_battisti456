from typing import NewType

HexColor = NewType('HexColor',str)
"'#RRGGBB'"
HexColorAlpha = NewType('HexColorAlpha',str)
"'#RRGGBBAA'"
type PillowNamedColor = str
"e.g. 'red', 'blue', 'cyan'"
type TupleRGB = tuple[int,int,int]
"(R,G,B)"
type TupleRGBA = tuple[int,int,int,int]
"(R,G,B,A)"
IntegerColor = NewType('IntegerColor',int)
"integer expression of rgb hex"
IntegerColorAlpha = NewType('IntegerColorAlpha',int)
"integer expression of rgba hex"
type Color = HexColor|HexColorAlpha|PillowNamedColor|TupleRGB|TupleRGBA|IntegerColor|IntegerColorAlpha
"hex code or PIL color-name, RGB, or RBGA"


