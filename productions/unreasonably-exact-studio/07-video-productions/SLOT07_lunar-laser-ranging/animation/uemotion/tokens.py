"""Colour and typography tokens. Same grammar and font files as tools/animatic.py (the film-wide look)."""
import math, os
from PIL import ImageFont

DESIGN_W, DESIGN_H = 1080, 1920            # final canvas; every coordinate in this package is in these design units

# ---- colour grammar: warm = outbound / away, cool = return / coming home (rule 1 of SCIENTIFIC_VISUAL_DESIGN.md)
BG = (7, 11, 26); WARM = (255, 172, 64); COOL = (96, 200, 255); WHITE = (238, 240, 245)
MOONC = (172, 172, 176); MOOND = (64, 64, 72); EARTHD = (10, 26, 62); EARTHL = (44, 108, 196)
REGO = (112, 110, 108); GOLD = (214, 170, 70); GREY = (120, 126, 140); DIM = (60, 66, 84)
PANEL = (22, 30, 56); GLASS = (170, 210, 235); ALERT = (255, 96, 84)

# ---- ONE sun direction for the whole film (rule 3). 2-D part equals animatic LDIR (toward the sun, screen space; up-left).
SUN_2D = (-0.62, -0.42)
_n = math.sqrt(SUN_2D[0] ** 2 + SUN_2D[1] ** 2 + 0.66 ** 2)
SUN = (SUN_2D[0] / _n, SUN_2D[1] / _n, 0.66 / _n)           # unit 3-D vector, +z toward the viewer

# ---- layout (design units)
SAFE = (60, 150, 1020, 1440)               # key subjects stay in here (same as animatic)
CAPTION_BOX = (60, 1480, 1020, 1730)       # caption band (same as animatic CAP)
MIN_TEXT = 34                              # smallest on-screen type, design units (17 px at the 540-wide proof size)

# ---- typography (same files as animatic.font)
# V3: scientific labels use the caption face (Comic Neue, OFL, assets/fonts/comicneue) so diagrams and subtitles read as one system;
# numbers stay in the mono face. V2 used Helvetica / Arial Bold here (tokens.py.bak_v2).
_CN = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'assets', 'fonts', 'comicneue')
_FONT_FILES = {'sans': os.path.join(_CN, 'ComicNeue-Regular.ttf'), 'bold': os.path.join(_CN, 'ComicNeue-Bold.ttf'),
               'mono': '/System/Library/Fonts/Menlo.ttc'}
_fonts = {}
_FONT_FILES['math'] = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'     # V3: formulas keep a geometric face (Comic Neue's t reads as a dagger, its x-sign is tiny)
def font(px, mono=False, bold=False, math=False):
    """px = size in WORKING pixels (already scaled by the canvas)."""
    px = max(6, int(round(px)))
    key = (px, mono, bold, math)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(_FONT_FILES['math' if math else ('mono' if mono else ('bold' if bold else 'sans'))], px)
    return _fonts[key]

def text_width(s, size, mono=False, bold=False):
    """Width in design units of s at `size` design units (measured at 1:1)."""
    return font(size, mono, bold).getlength(s)

def mix(c1, c2, x):
    x = min(1.0, max(0.0, x)); return tuple(int(round(a + (b - a) * x)) for a, b in zip(c1, c2))
def dim(c, k): return tuple(int(v * k) for v in c)
def lum(c): return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
