"""V2 original artwork: white-canvas, hand-drawn-look characters and props.

Every asset is drawn by code into BOTH an SVG (editable vector source) and a
PNG layer (2x supersampled). Run:  python3 art.py   -> assets/*.svg, assets/*.png
Style recipe: see STYLE_RECIPE_V2.md. All artwork is original; nothing traced.
"""
import math, os, random
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets")
SS = 2  # supersample factor for PNG
INK = "#26221F"  # warm near-black outline
LW = 7  # base outline width at 1x


class Canvas:
    """Records shapes to SVG and draws them with Pillow at SS x."""

    def __init__(self, w, h, seed=1):
        self.w, self.h = w, h
        self.img = Image.new("RGBA", (w * SS, h * SS), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)
        self.svg = []
        self.rng = random.Random(seed)

    # hand-drawn wobble: subdivide edges, nudge points slightly
    def wob(self, pts, amt=1.6, closed=True, step=22):
        out = []
        n = len(pts)
        segs = n if closed else n - 1
        for i in range(segs):
            (x0, y0), (x1, y1) = pts[i], pts[(i + 1) % n]
            k = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
            for j in range(k):
                t = j / k
                out.append((x0 + (x1 - x0) * t + self.rng.uniform(-amt, amt),
                            y0 + (y1 - y0) * t + self.rng.uniform(-amt, amt)))
        if not closed:
            out.append(pts[-1])
        return out

    def poly(self, pts, fill=None, stroke=INK, w=LW, wobble=True):
        p = self.wob(pts) if wobble else list(pts)
        s = [(x * SS, y * SS) for x, y in p]
        if fill:
            self.d.polygon(s, fill=fill)
        if stroke and w:
            self.d.line(s + [s[0]], fill=stroke, width=int(w * SS), joint="curve")
            for x, y in s[:1]:
                r = w * SS / 2
                self.d.ellipse((x - r, y - r, x + r, y + r), fill=stroke)
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in p) + " Z"
        self.svg.append(f'<path d="{d}" fill="{fill or "none"}" stroke="{stroke or "none"}" '
                        f'stroke-width="{w if stroke else 0}" stroke-linejoin="round"/>')

    def line(self, pts, color=INK, w=LW, wobble=True, cap=True):
        p = self.wob(pts, amt=1.0, closed=False) if wobble else list(pts)
        s = [(x * SS, y * SS) for x, y in p]
        self.d.line(s, fill=color, width=int(w * SS), joint="curve")
        if cap:
            r = w * SS / 2
            for x, y in (s[0], s[-1]):
                self.d.ellipse((x - r, y - r, x + r, y + r), fill=color)
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in p)
        self.svg.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
                        f'stroke-linecap="round" stroke-linejoin="round"/>')

    def ell(self, cx, cy, rx, ry, fill=None, stroke=INK, w=LW, wobble=True, n=48):
        pts = [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]
        self.poly(pts, fill, stroke, w, wobble)

    def arc(self, cx, cy, rx, ry, a0, a1, color=INK, w=LW, n=18):
        pts = [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
                cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
        self.line(pts, color, w, wobble=False)

    def limb(self, pts, color, w):
        """Thick outlined tube (arm/leg): ink stroke under colour stroke."""
        self.line(pts, INK, w + 2 * LW)
        self.line(pts, color, w, wobble=False)

    def save(self, name):
        os.makedirs(OUT, exist_ok=True)
        self.img.resize((self.w, self.h), Image.LANCZOS).save(os.path.join(OUT, name + ".png"))
        with open(os.path.join(OUT, name + ".svg"), "w") as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                    f'viewBox="0 0 {self.w} {self.h}">\n' + "\n".join(self.svg) + "\n</svg>\n")


def blob(cx, cy, rx, ry, top=1.0, bot=1.0, n=60):
    """Egg/superellipse: top/bot widen or narrow the halves."""
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        s = math.sin(a)
        k = bot if s > 0 else top
        pts.append((cx + rx * math.cos(a) * (1 + (k - 1) * abs(s)), cy + ry * s))
    return pts


# ---------------------------------------------------------------- characters
POSES = {  # right/left arm polylines (viewer's left = L); hand at last point
    "down":    ([(215, 455), (190, 560), (196, 655)], [(385, 455), (410, 560), (404, 655)]),
    "chest":   ([(215, 455), (190, 560), (196, 655)], [(385, 455), (425, 545), (322, 520)]),
    "point":   ([(215, 455), (190, 560), (196, 655)], [(385, 455), (470, 430), (548, 352)]),
    "explain": ([(215, 455), (190, 560), (196, 655)], [(385, 455), (455, 545), (478, 448)]),
    "hold":    ([(215, 455), (190, 560), (196, 655)], [(385, 455), (440, 560), (418, 590)]),
    "phone":   ([(215, 455), (190, 560), (196, 655)], [(385, 455), (468, 430), (452, 300)]),
    "clip":    ([(215, 455), (235, 560), (300, 585)], [(385, 455), (395, 560), (345, 585)]),
    "cane":    ([(215, 455), (170, 560), (150, 640)], [(385, 455), (410, 560), (404, 655)]),
}


def face(c, expr, skin_dark):
    global CHEEK
    ey = 262
    # eyes
    if expr in ("happy",):
        c.arc(248, ey + 6, 18, 14, 200, 340, w=6)
        c.arc(352, ey + 6, 18, 14, 200, 340, w=6)
    elif expr == "squint":
        c.line([(232, ey + 2), (262, ey + 8)], w=6)
        c.line([(368, ey + 2), (338, ey + 8)], w=6)
    else:
        for x in (248, 352):
            c.ell(x, ey, 15, 20, fill=INK, stroke=None, wobble=False)
            c.ell(x - 5, ey - 7, 5, 5, fill="#FFFFFF", stroke=None, wobble=False)
    # brows
    if expr in ("worried", "squint"):
        c.line([(228, ey - 30), (264, ey - 42)], w=6)
        c.line([(372, ey - 30), (336, ey - 42)], w=6)
    elif expr == "think":
        c.line([(228, ey - 40), (266, ey - 40)], w=6)
        c.line([(336, ey - 44), (372, ey - 36)], w=6)
    # cheeks
    for x in (222, 378):
        c.ell(x, ey + 44, 22, 13, fill=CHEEK, stroke=None, wobble=False)
    # nose
    c.arc(300, ey + 38, 10, 8, 20, 160, color=skin_dark, w=5)
    # mouth
    my = ey + 78
    if expr in ("smile", "happy"):
        c.arc(300, my - 10, 28, 18, 20, 160, w=6)
    elif expr == "talk":
        c.ell(300, my, 18, 14, fill="#7A2E2E", w=5)
    elif expr in ("worried", "squint"):
        c.line([(276, my + 4), (288, my - 3), (300, my + 4), (312, my - 3), (324, my + 4)], w=5)
    else:
        c.line([(284, my), (316, my)], w=6)


def person(name, skin, top, pants, pose="down", expr="calm", hair="short", hair_col=INK,
           glasses=False, mustache=False, coat=False, steth=False, prop=None,
           step=False, cuff=False, seed=1):
    c = Canvas(600, 900, seed)
    skin_dark = shade(skin, 0.72)
    # legs
    if step:
        c.limb([(262, 700), (258, 790), (256, 842)], pants, 44)
        c.limb([(338, 700), (380, 760), (372, 812)], pants, 44)
        c.ell(246, 852, 42, 20, fill=INK, stroke=None)
        c.ell(386, 822, 42, 20, fill=INK, stroke=None)
    else:
        c.limb([(262, 700), (258, 790), (256, 842)], pants, 44)
        c.limb([(338, 700), (342, 790), (344, 842)], pants, 44)
        c.ell(246, 852, 42, 20, fill=INK, stroke=None)
        c.ell(354, 852, 42, 20, fill=INK, stroke=None)
    la, ra = POSES[pose]
    # torso
    torso = [(205, 445), (395, 445), (412, 600), (402, 715), (198, 715), (188, 600)]
    c.poly(torso, fill=top)
    c.line([(300, 450), (300, 700)], color=shade(top, 0.8), w=4) if not coat else None
    c.poly([(262, 445), (300, 492), (338, 445)], fill=shade(top, 0.85), w=5)  # collar
    if coat:
        c.poly([(205, 445), (268, 445), (300, 520), (290, 715), (198, 715), (188, 600)], fill="#FFFFFF")
        c.poly([(395, 445), (332, 445), (300, 520), (310, 715), (402, 715), (412, 600)], fill="#FFFFFF")
        c.poly([(352, 560), (390, 560), (390, 600), (352, 600)], fill="#FFFFFF", w=4)  # pocket
        c.line([(362, 548), (364, 578)], color="#3E7CB1", w=5)  # pen
    if steth:
        c.line([(262, 452), (244, 540), (276, 600), (300, 610)], color="#4A4A52", w=7)
        c.line([(338, 452), (350, 520)], color="#4A4A52", w=7)
        c.ell(352, 534, 15, 15, fill="#B9C2CC", w=5)
    # arms (after torso so hands read on top)
    sleeve = "#FFFFFF" if coat else top
    for arm in (la, ra):
        c.limb(arm, sleeve, 40)
    if cuff:  # BP cuff on viewer-left upper arm
        c.poly([(176, 500), (226, 500), (222, 548), (172, 548)], fill="#4C6E91", w=5)
        c.line([(190, 548), (176, 600), (160, 640)], color="#3B3B3B", w=4)
    # props held in right hand
    hx, hy = ra[-1]
    if prop == "meter":
        c.poly([(hx - 30, hy - 70), (hx + 32, hy - 70), (hx + 32, hy + 20), (hx - 30, hy + 20)], fill="#3D84C6")
        c.poly([(hx - 18, hy - 58), (hx + 20, hy - 58), (hx + 20, hy - 26), (hx - 18, hy - 26)], fill="#E9F4FB", w=4)
        c.line([(hx - 8, hy - 42), (hx + 8, hy - 42)], w=4)
        c.ell(hx + 1, hy - 4, 8, 8, fill="#FFFFFF", w=4)
    elif prop == "phone":
        c.poly([(hx - 20, hy - 74), (hx + 18, hy - 74), (hx + 18, hy + 8), (hx - 20, hy + 8)], fill="#2F3A45")
        c.poly([(hx - 12, hy - 64), (hx + 10, hy - 64), (hx + 10, hy - 6), (hx - 12, hy - 6)], fill="#8FD3B0", w=3)
    elif prop == "clip":
        c.poly([(240, 520), (360, 520), (360, 668), (240, 668)], fill="#C99A5B")
        c.poly([(252, 538), (348, 538), (348, 656), (252, 656)], fill="#FFFFFF", w=4)
        c.poly([(276, 510), (324, 510), (324, 532), (276, 532)], fill="#8A8F96", w=4)
        for y in (566, 592, 618):
            c.line([(266, y), (276, y + 8), (290, y - 8)], color="#3FA35B", w=5)
            c.line([(300, y), (336, y)], color="#9AA0A6", w=4)
    elif prop == "pills":
        c.poly([(hx - 24, hy - 76), (hx + 24, hy - 76), (hx + 24, hy + 6), (hx - 24, hy + 6)], fill="#F3A64A")
        c.poly([(hx - 28, hy - 96), (hx + 28, hy - 96), (hx + 28, hy - 74), (hx - 28, hy - 74)], fill="#FFFFFF", w=5)
        c.poly([(hx - 16, hy - 56), (hx + 16, hy - 56), (hx + 16, hy - 24), (hx - 16, hy - 24)], fill="#FFFFFF", w=3)
    elif prop == "cane":
        x0, y0 = la[-1]
        c.line([(x0, y0 - 10), (x0 - 6, 858)], color="#7B5434", w=12)
        c.arc(x0 + 18, y0 - 10, 20, 18, 180, 360, color="#7B5434", w=12)
    # hands
    for (x, y) in (la[-1], ra[-1]):
        c.ell(x, y, 28, 28, fill=skin)
    # head: ears, head, hair
    c.ell(152, 280, 26, 32, fill=skin)
    c.ell(448, 280, 26, 32, fill=skin)
    c.poly(blob(300, 255, 150, 178, top=0.9, bot=1.06), fill=skin)
    hair_shapes(c, hair, hair_col, skin)
    global CHEEK
    CHEEK = mix(skin, "#F07F7F", 0.45)
    face(c, expr, skin_dark)
    if glasses:
        for x in (248, 352):
            c.ell(x, 262, 36, 32, fill=None, w=5, wobble=False)
        c.line([(284, 258), (316, 258)], w=5)
    if mustache:
        c.poly([(268, 326), (300, 316), (332, 326), (322, 336), (300, 330), (278, 336)], fill=hair_col, w=4)
    c.save(name)


def hair_shapes(c, hair, col, skin):
    if hair == "short":
        c.poly([(152, 240), (160, 150), (220, 92), (300, 76), (382, 92), (440, 150), (448, 240),
                (420, 190), (360, 160), (290, 168), (220, 150), (176, 200)], fill=col)
    elif hair == "side":
        c.poly([(150, 250), (158, 150), (230, 88), (320, 80), (400, 100), (448, 160), (450, 248),
                (430, 186), (380, 150), (300, 140), (250, 175), (200, 180), (170, 214)], fill=col)
    elif hair == "bald":
        c.poly([(150, 300), (152, 216), (178, 190), (196, 236), (180, 300)], fill=col)
        c.poly([(450, 300), (448, 216), (422, 190), (404, 236), (420, 300)], fill=col)
    elif hair == "bun":
        c.ell(300, 70, 54, 46, fill=col)
        c.poly([(148, 300), (150, 170), (210, 96), (300, 80), (390, 96), (450, 170), (452, 300),
                (430, 230), (380, 168), (300, 150), (220, 168), (170, 230)], fill=col)
    elif hair == "bob":
        c.poly([(140, 380), (138, 170), (210, 90), (300, 76), (390, 90), (462, 170), (460, 380),
                (420, 380), (424, 220), (372, 160), (300, 180), (220, 160), (176, 220), (180, 380)], fill=col)


def mix(a, b, t):
    a, b = a.lstrip("#"), b.lstrip("#")
    return "#" + "".join("%02X" % int(int(a[i:i+2], 16) * (1 - t) + int(b[i:i+2], 16) * t) for i in (0, 2, 4))


def shade(hexc, k):
    hexc = hexc.lstrip("#")[:6]
    r, g, b = (int(hexc[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02X%02X%02X" % (int(r * k), int(g * k), int(b * k))


# ---------------------------------------------------------------- props
def heart():
    c = Canvas(720, 760, 7)
    c.limb([(300, 230), (300, 90), (380, 40), (470, 70)], "#D9534F", 70)   # aortic arch
    c.limb([(420, 220), (440, 110)], "#5B8DD6", 56)                       # vessel
    body = [(360, 700), (210, 560), (120, 420), (118, 300), (170, 210), (260, 190), (330, 240),
            (360, 260), (420, 200), (520, 190), (600, 250), (620, 360), (580, 490), (480, 600)]
    c.poly(body, fill="#E86A5E", w=8)
    c.poly([(170, 280), (200, 240), (240, 236), (200, 300), (178, 360)], fill="#F6A99A", stroke=None)
    c.save("heart_base")
    o = Canvas(720, 760, 8)  # coronary overlay, separate layer
    o.line([(340, 250), (300, 340), (260, 430), (250, 520), (300, 610)], color="#8E1F2B", w=12)
    o.line([(300, 340), (220, 360), (170, 420)], color="#8E1F2B", w=9)
    o.line([(360, 252), (440, 330), (500, 430), (470, 560)], color="#8E1F2B", w=12)
    o.line([(440, 330), (540, 320), (585, 370)], color="#8E1F2B", w=9)
    o.save("heart_coronary")
    m = Canvas(720, 760, 9)  # narrowing marker on one branch
    m.ell(493, 440, 46, 46, fill=None, stroke="#F4C430", w=10, wobble=False)
    m.save("heart_marker")


def artery():
    c = Canvas(760, 300, 11)
    c.poly([(30, 70), (730, 70), (730, 230), (30, 230)], fill="#F7C9C0", w=8)
    c.poly([(30, 100), (730, 100), (730, 200), (30, 200)], fill="#D94B4B", stroke=None)
    c.save("artery_tube")
    p = Canvas(760, 300, 12)
    p.poly([(250, 100), (300, 76), (380, 60), (460, 76), (510, 100), (470, 150), (380, 158), (290, 150)],
           fill="#F2C94C", w=6)
    p.poly([(270, 200), (330, 210), (420, 214), (490, 200), (430, 176), (330, 176)], fill="#F2C94C", w=6)
    p.save("artery_plaque")
    f = Canvas(760, 300, 13)
    for x0, x1 in ((60, 200), (540, 690)):
        f.line([(x0, 150), (x1, 150)], color="#FFFFFF", w=9)
        f.poly([(x1, 132), (x1 + 26, 150), (x1, 168)], fill="#FFFFFF", stroke=None)
    f.line([(330, 150), (430, 150)], color="#FFFFFF", w=5)
    f.save("artery_flow")


def stairs():
    c = Canvas(1080, 700, 21)
    pts = [(0, 700), (0, 520), (300, 520), (300, 400), (560, 400), (560, 280), (820, 280), (820, 160),
           (1080, 160), (1080, 700)]
    c.poly(pts, fill="#E7E3DC", w=8)
    for y, x0 in ((520, 0), (400, 300), (280, 560), (160, 820)):
        c.line([(x0 + 10, y + 18), (x0 + 250, y + 18)], color="#CFC8BD", w=6, cap=False)
    c.line([(150, 330), (430, 210), (690, 90), (960, -10)], color="#A27B5C", w=12)  # handrail
    for x in (180, 440, 700):
        c.line([(x, 320 - (x - 150) * 0.44), (x, 520 - (x - 150) * 0.46)], color="#A27B5C", w=8)
    c.save("plate_stairs")


def sofa():
    c = Canvas(1080, 520, 22)
    c.line([(0, 470), (1080, 470)], color="#CFC8BD", w=8)
    c.poly([(120, 180), (960, 180), (960, 440), (120, 440)], fill="#7FA7C9", w=8)
    c.poly([(80, 260), (190, 260), (190, 450), (80, 450)], fill="#6C93B5", w=8)
    c.poly([(890, 260), (1000, 260), (1000, 450), (890, 450)], fill="#6C93B5", w=8)
    c.poly([(190, 330), (890, 330), (890, 400), (190, 400)], fill="#8DB4D4", w=7)
    for x in (110, 970):
        c.line([(x, 450), (x, 490)], w=10)
    c.save("plate_sofa")
    w = Canvas(420, 420, 23)  # window
    w.poly([(20, 20), (400, 20), (400, 400), (20, 400)], fill="#DFF0FA", w=8)
    w.line([(210, 20), (210, 400)], w=7)
    w.line([(20, 210), (400, 210)], w=7)
    w.ell(110, 110, 34, 34, fill="#F6D776", stroke=None)
    w.save("plate_window")


def icons():
    c = Canvas(200, 200, 31)  # breathless swirls
    for r, y in ((50, 70), (36, 112), (24, 150)):
        c.arc(100, y, r + 30, 16, 180, 360, color="#3E8FC4", w=9)
        c.line([(30 + 60 - r, y), (130 + r, y)], color="#3E8FC4", w=9)
    c.save("icon_breath")
    c = Canvas(200, 200, 32)  # low battery = unusual tiredness
    c.poly([(30, 60), (160, 60), (160, 140), (30, 140)], fill="#FFFFFF", w=9)
    c.poly([(160, 84), (178, 84), (178, 116), (160, 116)], fill=INK, stroke=None)
    c.poly([(44, 74), (74, 74), (74, 126), (44, 126)], fill="#E0533F", stroke=None)
    c.save("icon_tired")
    c = Canvas(200, 200, 33)  # cold sweat drops
    for x, y, s in ((70, 70, 1), (130, 110, 0.8), (80, 150, 0.6)):
        c.poly([(x, y - 40 * s), (x + 22 * s, y), (x, y + 18 * s), (x - 22 * s, y)], fill="#7CC4E8", w=6)
    c.save("icon_sweat")
    c = Canvas(200, 200, 34)  # radiating discomfort (jaw/arm/back)
    for a in range(0, 360, 45):
        r0, r1 = 30, 80
        x, y = math.cos(math.radians(a)), math.sin(math.radians(a))
        c.line([(100 + r0 * x, 100 + r0 * y), (100 + r1 * x, 100 + r1 * y)], color="#E0533F", w=10)
    c.ell(100, 100, 18, 18, fill="#E0533F", stroke=None)
    c.save("icon_radiate")
    c = Canvas(160, 240, 35)  # lightning = sudden
    c.poly([(90, 10), (20, 130), (74, 130), (50, 230), (140, 90), (84, 90), (120, 10)], fill="#F4C430", w=8)
    c.save("icon_sudden")
    c = Canvas(240, 200, 36)  # curved exertion arrow
    c.line([(20, 180), (60, 110), (120, 60), (190, 40)], color="#E0533F", w=14)
    c.poly([(176, 12), (232, 36), (186, 74)], fill="#E0533F", stroke=None)
    c.save("icon_exert")
    c = Canvas(200, 200, 37)  # check mark
    c.ell(100, 100, 86, 86, fill="#3FA35B", w=8)
    c.line([(58, 104), (88, 134), (146, 70)], color="#FFFFFF", w=18)
    c.save("icon_check")
    c = Canvas(220, 260, 38)  # phone with emergency handset
    c.poly([(30, 10), (190, 10), (190, 250), (30, 250)], fill="#2F3A45")
    c.poly([(46, 34), (174, 34), (174, 214), (46, 214)], fill="#E0533F", w=5)
    c.poly([(80, 90), (104, 80), (118, 112), (108, 122), (126, 152), (140, 144), (156, 168), (138, 186),
            (98, 160), (78, 120)], fill="#FFFFFF", stroke=None)
    c.save("icon_phone")
    c = Canvas(380, 220, 39)  # speech bubble
    c.poly(blob(190, 96, 176, 86) + [], fill="#FFFFFF", w=7)
    c.poly([(80, 160), (60, 214), (130, 172)], fill="#FFFFFF", w=7)
    c.line([(84, 168), (124, 168)], color="#FFFFFF", w=10, wobble=False)
    c.save("bubble")
    g = Image.new("RGBA", (420, 420), (0, 0, 0, 0))  # soft warning glow
    ImageDraw.Draw(g).ellipse((60, 60, 360, 360), fill=(232, 74, 60, 150))
    g.filter(ImageFilter.GaussianBlur(40)).save(os.path.join(OUT, "glow_red.png"))


CAST = {
    # patient: middle-aged man with type 2 diabetes (accessory identity: moustache + green jumper)
    "patient": dict(skin="#C9885A", top="#5DA271", pants="#3D4A5C", hair="short", mustache=True, seed=3),
    "doctor": dict(skin="#9A6444", top="#4FA3A0", pants="#2F5F6E", hair="side", glasses=True,
                   coat=True, steth=True, seed=5),
    "oldman": dict(skin="#E3B58E", top="#A0714F", pants="#5A5A62", hair="bald", hair_col="#F2F2F2",
                   glasses=True, mustache=True, seed=7),
    "oldwoman": dict(skin="#D59F78", top="#8F6BB0", pants="#4E4A60", hair="bun", hair_col="#C9C9CF", seed=9),
    "woman": dict(skin="#B07650", top="#3E8FA8", pants="#3A3F55", hair="bob", seed=11),
}
VARIANTS = [
    ("patient_chest_smile", "patient", dict(pose="chest", expr="smile", step=True)),
    ("patient_chest_pain", "patient", dict(pose="chest", expr="squint", step=True)),
    ("patient_chest_worried", "patient", dict(pose="chest", expr="worried")),
    ("patient_meter", "patient", dict(pose="hold", expr="smile", prop="meter")),
    ("patient_neutral", "patient", dict(pose="down", expr="calm")),
    ("patient_phone", "patient", dict(pose="phone", expr="worried", prop="phone")),
    ("doctor_smile", "doctor", dict(pose="down", expr="smile")),
    ("doctor_explain", "doctor", dict(pose="explain", expr="talk")),
    ("doctor_point", "doctor", dict(pose="point", expr="talk")),
    ("doctor_clip", "doctor", dict(pose="clip", expr="calm", prop="clip")),
    ("oldman", "oldman", dict(pose="cane", expr="calm", prop="cane")),
    ("oldwoman", "oldwoman", dict(pose="down", expr="smile")),
    ("woman_pills", "woman", dict(pose="hold", expr="think", prop="pills", cuff=True)),
]

if __name__ == "__main__":
    for name, who, kw in VARIANTS:
        spec = dict(CAST[who]); spec.update(kw)
        person(name, **spec)
    heart(); stairs(); sofa(); icons()
    print(len(os.listdir(OUT)), "files in", OUT)
