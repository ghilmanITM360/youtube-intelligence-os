"""Typography components: caption plate, qualifier strip, headline. Text stays live <text>."""
from props import g, t
from style import C, FONT

CAPTION_ZONE = {"x": 90, "y": 1330, "w": 900, "h": 200}  # avoid Shorts UI: bottom ~320px, right ~110px


def caption_plate(lines=("Caption text",), cx=540, cy=1430, size=56):
    w = max(len(s) for s in lines) * size * 0.56 + 70
    h = len(lines) * size * 1.18 + 34
    out = (f'<rect x="{cx - w / 2:.0f}" y="{cy - h / 2:.0f}" width="{w:.0f}" height="{h:.0f}" rx="24" '
           f'fill="{C["ink"]}" fill-opacity=".88"/>')
    for i, s in enumerate(lines):
        y = cy - h / 2 + 17 + size * 0.95 + i * size * 1.18
        out += t(cx, round(y), s, size, fill=C["paper"], ls=0)
    return g(out, id="caption_plate")


def qualifier(text, cx=540, cy=1280, size=24, fill=None, color=None):
    w = len(text) * size * 0.56 + 48
    out = (f'<rect x="{cx - w / 2:.0f}" y="{cy - size:.0f}" width="{w:.0f}" height="{size * 2:.0f}" rx="{size}" '
           f'fill="{fill or C["paper"]}" fill-opacity=".92"/>' + t(cx, cy + size * 0.36, text, size,
                                                                     fill=color or C["ink"], weight=700))
    return g(out, id="qualifier_strip")


def headline(lines, cx=540, top=300, size=120, fill=None, shadow=True):
    out = ""
    for i, s in enumerate(lines):
        y = top + i * size * 0.98
        if shadow:
            out += t(cx + 8, y + 10, s, size, fill=C["navy_dk"], ls=-3)
        out += t(cx, y, s, size, fill=fill or C["paper"], ls=-3)
    return g(out, id="headline")


FONT_SPEC = {"family": FONT, "headline_weight": 800, "caption_weight": 800, "body_weight": 700}
