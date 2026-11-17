"""Environment kits for 1080x1920 frames. Each returns an ordered dict of layer -> SVG.

Backgrounds carry no captions, prices, rates, dates or brand marks. Floor contact lines are
documented per kit so characters and furniture share one perspective.
"""
from props import INK, g, p
from style import C

W, H = 1080, 1920


def _planks(y0, y1, vp=(540, 560), n=14, color=None):
    """Floor planks converging to a vanishing point (one-point perspective)."""
    out = ""
    for i in range(-2, n + 3):
        xb = -200 + i * (W + 400) / n
        t = (y0 - vp[1]) / (y1 - vp[1])
        xt = vp[0] + (xb - vp[0]) * t
        out += f"M{xt:.0f} {y0}L{xb:.0f} {y1}"
    for y in (y0 + 90, y0 + 230, y0 + 430):
        out += f"M0 {y}H{W}"
    return p(out, sw=4, color=color or C["floor_dk"])


def _pendant(x, y):
    return (p(f"M{x} 0 V{y - 60}", sw=5) + p(f"M{x - 70} {y} Q{x} {y - 110} {x + 70} {y} Z", fill=C["gold"])
            + f'<ellipse cx="{x}" cy="{y + 4}" rx="22" ry="10" fill="{C["gold_pale"]}"/>')


def _plant(x, y, s=1.0, flip=False):
    pot = (f'<path d="M-70 0 L70 0 L52 150 L-52 150 Z" fill="{C["coral_dk"] if False else C["wood"]}" {INK}/>'
           + p("M-70 0 H70", sw=7))
    leaves = ""
    for ang, ln in ((-60, 260), (-30, 300), (0, 320), (28, 290), (58, 240), (-82, 200), (82, 190)):
        leaves += (f'<g transform="rotate({ang})"><path d="M0 0 C-44 -{ln * .45} -30 -{ln * .85} 0 -{ln} '
                   f'C30 -{ln * .85} 44 -{ln * .45} 0 0 Z" fill="{C["plant"]}" {INK}/>'
                   f'<path d="M0 -12 V-{ln * .86}" stroke="{C["plant_dk"]}" stroke-width="5" fill="none"/></g>')
    fx = -1 if flip else 1
    return f'<g transform="translate({x} {y}) scale({fx * s} {s})">{leaves}{pot}</g>'


def _armchair(x, y, s=1.0):
    c, d = C["sage"], "#7FA592"
    out = (f'<rect x="-120" y="-250" width="240" height="190" rx="40" fill="{d}" {INK}/>'
           f'<rect x="-130" y="-100" width="260" height="80" rx="22" fill="{c}" {INK}/>'
           f'<rect x="-160" y="-170" width="60" height="150" rx="26" fill="{c}" {INK}/>'
           f'<rect x="100" y="-170" width="60" height="150" rx="26" fill="{c}" {INK}/>'
           + p("M-110 -20 L-104 0 M110 -20 L104 0", sw=10, color=C["wood_dk"]))
    return f'<g transform="translate({x} {y}) scale({s})">{out}</g>'


def _window(x, y, w, h, frame=None):
    fr = frame or C["paper"]
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{C["sky"]}" {INK}/>'
    out += p(f"M{x + w * .15} {y + h * .45} L{x + w * .45} {y + h * .12} M{x + w * .3} {y + h * .6} "
             f"L{x + w * .62} {y + h * .26}", sw=16, color=C["white"], extra=' stroke-opacity=".6"')
    out += p(f"M{x + w / 2} {y} V{y + h} M{x} {y + h * .55} H{x + w}", sw=14, color=fr)
    out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="none" stroke="{fr}" stroke-width="18"/>'
    out += f'<rect x="{x - 9}" y="{y - 9}" width="{w + 18}" height="{h + 18}" rx="14" fill="none" {INK}/>'
    return out


def store():
    """Furniture showroom. Floor line y=1180; character feet y~1600-1720; sofa centre x~640, floor y~1560."""
    L = {}
    wall = f'<rect width="{W}" height="{H}" fill="{C["wall"]}"/>'
    wall += "".join(p(f"M{x} 120 V1180", sw=3, color=C["wall_dk"]) for x in range(60, W, 120))
    wall += f'<rect width="{W}" height="120" fill="{C["wall_dk"]}"/>' + p("M0 120 H1080", sw=6)
    wall += _window(110, 250, 380, 640) + _window(590, 250, 380, 640)
    L["store_bg_wall"] = wall
    L["store_bg_lights"] = _pendant(300, 330) + _pendant(780, 330)
    floor = f'<rect y="1180" width="{W}" height="{H - 1180}" fill="{C["floor"]}"/>'
    floor += _planks(1180, H) + p("M0 1180 H1080", sw=8)
    floor += f'<rect y="1164" width="{W}" height="22" fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="6"/>'
    L["store_floor"] = floor
    L["store_rug"] = (p("M250 1400 L1010 1400 L1080 1700 L170 1700 Z", fill=C["paper"])
                      + p("M282 1424 L986 1424 L1040 1676 L212 1676 Z", sw=8, color=C["teal_lt"]))
    L["store_mid_displays"] = (_armchair(150, 1250, 0.8) + _plant(990, 1180, 0.55)
                               + f'<rect x="40" y="980" width="150" height="16" rx="6" fill="{C["wood"]}" {INK}/>'
                               + f'<circle cx="80" cy="950" r="26" fill="{C["teal_lt"]}" {INK}/>'
                               + f'<rect x="120" y="924" width="40" height="56" rx="10" fill="{C["gold_pale"]}" {INK}/>')
    L["store_fg_plant"] = _plant(70, 1760, 1.05)
    return L


def checkout():
    """Counter medium shot. Counter top y=1190 (x>=470); customer feet y~1880; associate behind counter."""
    L = {}
    wall = f'<rect width="{W}" height="{H}" fill="{C["wall"]}"/>'
    wall += "".join(p(f"M{x} 0 V1500", sw=3, color=C["wall_dk"]) for x in range(60, W, 120))
    wall += f'<rect x="520" y="420" width="500" height="22" rx="6" fill="{C["wood"]}" {INK}/>'
    for i, (w, h, col) in enumerate(((90, 120, C["teal_lt"]), (70, 90, C["gold_pale"]), (110, 70, C["sage"]),
                                     (60, 130, C["coral_pale"]))):
        x = 560 + i * 115
        wall += f'<rect x="{x}" y="{420 - h}" width="{w}" height="{h}" rx="10" fill="{col}" {INK}/>'
    wall += _window(60, 260, 340, 560)
    L["checkout_bg_wall"] = wall
    floor = f'<rect y="1500" width="{W}" height="{H - 1500}" fill="{C["floor"]}"/>' + _planks(1500, H, (300, 900))
    floor += p("M0 1500 H1080", sw=8)
    L["checkout_floor"] = floor
    counter = f'<rect x="470" y="1190" width="640" height="760" fill="{C["wood"]}" {INK}/>'
    counter += "".join(p(f"M{x} 1260 V1920", sw=5, color=C["wood_dk"]) for x in (640, 820, 1000))
    counter += f'<rect x="440" y="1150" width="680" height="60" rx="12" fill="{C["floor_lt"]}" {INK}/>'
    L["checkout_counter"] = counter
    return L


def living_room():
    """Home. Floor line y=1240; sofa centre x=540, floor y=1640; wall calendar slot x700-960 y330-640."""
    L = {}
    wall = f'<rect width="{W}" height="{H}" fill="#D7E6DC"/>'
    wall += "".join(p(f"M{x} 0 V1000", sw=10, color="#CADBD0") for x in range(40, W, 80))
    wall += f'<rect y="1000" width="{W}" height="240" fill="{C["paper"]}"/>' + p("M0 1000 H1080", sw=6)
    wall += "".join(p(f"M{x} 1030 V1210", sw=4, color=C["paper_dk"]) for x in range(80, W, 160))
    wall += _window(110, 300, 360, 520, frame=C["white"])
    wall += (p("M90 280 Q70 560 110 860 L60 860 Q40 560 70 280 Z", fill=C["gold_pale"])
             + p("M490 280 Q510 560 470 860 L520 860 Q540 560 510 280 Z", fill=C["gold_pale"]))
    wall += p("M50 270 H530", sw=10, color=C["wood_dk"])
    L["living_bg_wall"] = wall
    floor = f'<rect y="1240" width="{W}" height="{H - 1240}" fill="{C["floor"]}"/>' + _planks(1240, H, (540, 700))
    floor += f'<rect y="1226" width="{W}" height="22" fill="{C["white"]}" stroke="{C["ink"]}" stroke-width="6"/>'
    L["living_floor"] = floor
    L["living_rug"] = (f'<ellipse cx="540" cy="1690" rx="500" ry="130" fill="{C["paper"]}" {INK}/>'
                       f'<ellipse cx="540" cy="1690" rx="440" ry="100" fill="none" stroke="{C["teal_lt"]}" stroke-width="10"/>')
    lamp = (p("M960 1240 V760", sw=10) + p("M900 1240 H1020", sw=10)
            + p("M880 760 L1040 760 L1000 640 L920 640 Z", fill=C["paper"]))
    table = (f'<rect x="820" y="1190" width="190" height="20" rx="8" fill="{C["wood"]}" {INK}/>'
             + p("M840 1210 V1330 M990 1210 V1330", sw=10, color=C["wood_dk"]))
    L["living_mid_props"] = lamp + table + _plant(915, 1188, 0.4)
    L["living_fg_plant"] = _plant(1010, 1800, 0.9, flip=True)
    return L


def stage():
    """Navy explanation stage (Phase 1 thumbnail world). Optional floor band y>=1500."""
    dots = ('<defs><pattern id="stage_dots" width="36" height="36" patternUnits="userSpaceOnUse">'
            f'<circle cx="3" cy="3" r="1.6" fill="{C["paper"]}" opacity=".10"/></pattern></defs>')
    out = dots + f'<rect width="{W}" height="{H}" fill="{C["navy_bg"]}"/>'
    out += f'<rect width="{W}" height="{H}" fill="url(#stage_dots)"/>'
    out += f'<circle cx="940" cy="1660" r="480" fill="{C["navy_mid"]}"/><circle cx="75" cy="180" r="285" fill="{C["navy_mid"]}"/>'
    return {"stage_bg": out,
            "stage_floor": f'<rect y="1560" width="{W}" height="360" fill="{C["navy_dk"]}" fill-opacity=".55"/>'
                           + p("M0 1560 H1080", sw=4, color=C["navy_mid"])}


KITS = {"env_store": store, "env_checkout": checkout, "env_living_room": living_room, "env_stage": stage}


def compose(kit):
    return "".join(g(v, id=k) for k, v in KITS[kit]().items())
