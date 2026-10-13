"""Original finance/household props. Each builder returns SVG drawn around a local anchor.

Text stays live <text> so animation/captions can edit it. No logos, brands, real offers,
dollar amounts, rates or dates are drawn into any prop.
"""
from style import C, FONT, SW_PROP

SW = SW_PROP
INK = f'stroke="{C["ink"]}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round"'


def p(d, fill="none", sw=None, color=None, extra=""):
    if sw == 0:
        return f'<path d="{d}" fill="{fill}"{extra}/>'
    return (f'<path d="{d}" fill="{fill}" stroke="{color or C["ink"]}" stroke-width="{sw or SW}" '
            f'stroke-linejoin="round" stroke-linecap="round"{extra}/>')


def t(x, y, s, size, fill=None, anchor="middle", weight=800, ls=0, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'letter-spacing="{ls}" text-anchor="{anchor}" fill="{fill or C["ink"]}"{extra}>{s}</text>')


def g(body, id=None, **attrs):
    a = f' id="{id}"' if id else ""
    a += "".join(f' {k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f"<g{a}>{body}</g>"


def zigzag(x_right, x_left, y, teeth, depth):
    """Torn-paper edge from x_right back to x_left along baseline y (path continuation)."""
    step = (x_right - x_left) / teeth
    return "".join(f"L{x_right - i * step:.1f} {y + (depth if i % 2 else 0)}" for i in range(teeth + 1))


# ---- payment & paper -------------------------------------------------------------------
def store_card():
    body = '<rect x="-90" y="-57" width="180" height="114" rx="13" fill="%s" %s/>' % (C["teal"], INK)
    shine = p("M18 -52 L50 -52 L-8 52 L-40 52 Z", fill=C["teal_lt"], sw=0, extra=' fill-opacity=".35"')
    chip = ('<rect x="-70" y="-26" width="36" height="28" rx="6" fill="%s" stroke="%s" stroke-width="4"/>'
            % (C["gold"], C["ink"]) + p("M-70 -12 H-34 M-52 -26 V2", sw=3))
    dots = "".join(f'<circle cx="{-66 + grp * 46 + j * 9}" cy="20" r="3.4" fill="{C["paper"]}"/>'
                   for grp in range(3) for j in range(4))
    label = t(-70, 47, "STORE CARD", 15, fill=C["paper"], anchor="start", ls=1.5)
    return g(body + shine + chip + dots + label, id="store_card")


def offer_sheet():
    out = p("M-160 -210 H160 V188" + zigzag(160, -160, 188, 12, 20) + "Z", fill=C["paper"])
    out += f'<rect x="-153" y="-203" width="306" height="70" fill="{C["teal"]}"/>'
    out += t(0, -158, "STORE CARD OFFER", 25, fill=C["paper"], ls=2)
    out += g(t(0, -84, "NO INTEREST", 40, ls=-0.5), id="offer_headline")
    out += g(t(0, 52, "IF", 132, fill=C["coral"], ls=-4), id="offer_if")
    out += g(t(0, 104, "PAID IN FULL", 33, ls=0) + t(0, 140, "WITHIN 12 MONTHS", 24, weight=700, ls=0.5),
             id="offer_condition")
    out += p("M-118 -44 H118", sw=8, color=C["teal_lt"])
    out += g(t(0, 172, "Illustrative offer", 15, weight=600, extra=' font-style="italic"'), id="offer_note")
    return g(out, id="offer_sheet")


def statement(state="empty"):
    """Monthly statement. state: empty | charged (deferred interest row filled)."""
    out = f'<rect x="-160" y="-215" width="320" height="430" rx="12" fill="{C["white"]}" {INK}/>'
    out += f'<rect x="-153" y="-208" width="306" height="64" rx="6" fill="{C["ink"]}"/>'
    out += t(0, -167, "MONTHLY STATEMENT", 22, fill=C["paper"], ls=1)
    rows = [("Purchases", C["paper_dkr"]), ("Payment due", C["paper_dkr"]), ("Promo balance", C["teal_lt"])]
    for i, (label, col) in enumerate(rows):
        y = -104 + i * 62
        out += t(-136, y + 8, label, 22, anchor="start", weight=700)
        out += p(f"M60 {y} H128", sw=14, color=col)
        out += p(f"M-136 {y + 30} H136", sw=2, color=C["paper_dk"])
    y = 92
    out += g(t(-136, y + 8, "Interest charged", 22, anchor="start", weight=800), id="stmt_interest_label")
    if state == "empty":
        out += g(p(f"M86 {y} H118", sw=8, color=C["paper_dkr"]), id="stmt_interest_value_empty")
    else:
        out += g(f'<rect x="-144" y="{y - 30}" width="288" height="58" rx="10" fill="{C["coral_pale"]}" '
                 f'stroke="{C["coral"]}" stroke-width="5"/>' + t(-136, y + 8, "Interest charged", 22,
                                                                anchor="start", weight=800)
                 + p(f"M58 {y} H128", sw=16, color=C["coral"]), id="stmt_interest_value_charged")
    out += t(0, 182, "Schematic statement", 15, weight=600, extra=' font-style="italic"')
    return g(out, id=f"statement_{state}")


def interest_receipt(rows=6, header="DEFERRED INTEREST"):
    """Growable receipt: header + N entry rows + torn foot. Anchor = top centre."""
    w, top, hh, rh = 300, 0, 64, 34
    body_h = hh + rows * rh + 24
    d = f"M{-w / 2} {top} H{w / 2} V{body_h}" + zigzag(w / 2, -w / 2, body_h, 10, 16) + "Z"
    out = p(d, fill=C["paper"])
    out += f'<rect x="{-w / 2 + 6}" y="6" width="{w - 12}" height="{hh - 6}" fill="{C["coral"]}"/>'
    out += t(0, 44, header, 23 if len(header) > 12 else 28, ls=0.5)
    for i in range(rows):
        y = hh + 22 + i * rh
        out += g(f'<circle cx="{-w / 2 + 30}" cy="{y}" r="7" fill="{C["coral"]}"/>'
                 + p(f"M{-w / 2 + 50} {y} H{30 + (i * 37) % 60}", sw=12, color=C["paper_dkr"]),
                 id=f"receipt_row_{i + 1:02d}")
    return g(out, id=f"interest_receipt_{rows:02d}")


def pen():
    """Ballpoint, tip at +y. Teal barrel so it reads against ink outlines."""
    out = p("M-9 -70 H9 V44 L0 72 L-9 44 Z", fill=C["teal"])
    out += p("M-9 44 L0 72 L9 44 Z", fill=C["paper"], sw=5)
    out += p("M-3 64 L0 72 L3 64", fill=C["ink"], sw=3)
    out += f'<rect x="-11" y="-82" width="22" height="30" rx="6" fill="{C["ink"]}"/>'
    out += p("M7 -76 V-40", sw=4, color=C["ink"])
    return g(out, id="pen")


def marker():
    out = f'<rect x="-14" y="-72" width="28" height="120" rx="8" fill="{C["paper"]}" {INK}/>'
    out += f'<rect x="-15" y="-80" width="30" height="40" rx="8" fill="{C["coral"]}" {INK}/>'
    out += p("M-10 48 L10 48 L6 74 L-4 78 Z", fill=C["coral"])
    return g(out, id="marker")


def coin():
    out = f'<circle r="44" fill="{C["teal"]}" {INK}/>'
    out += f'<circle r="32" fill="none" stroke="{C["teal_lt"]}" stroke-width="5"/>'
    out += t(0, 15, "$", 44, fill=C["paper"])
    return g(out, id="payment_coin")


# ---- store / household -----------------------------------------------------------------
SOFA = {"base": "#7E5A7A", "dk": "#654662", "lt": "#9A7896", "leg": C["wood_dk"]}


def sofa_layers():
    """Front-view 3-seat sofa, origin = floor centre. Returns ordered layer dict
    (back-to-front): shadow, legs, back, seat, arm_left, arm_right, pillow.
    A seated character goes between 'seat' and the arms."""
    c = SOFA
    L = {}
    L["shadow"] = f'<ellipse cx="0" cy="2" rx="345" ry="20" fill="{C["navy_dk"]}" fill-opacity=".22"/>'
    L["legs"] = "".join(p(f"M{x - 12} -42 L{x + 12} -42 L{x + 7} 0 L{x - 7} 0 Z", fill=c["leg"], sw=6)
                        for x in (-262, 262))
    back = f'<rect x="-292" y="-318" width="584" height="200" rx="34" fill="{c["dk"]}" {INK}/>'
    for i in range(3):
        x = -282 + i * 190
        back += (f'<rect x="{x}" y="-296" width="184" height="166" rx="30" fill="{c["base"]}" {INK}/>'
                 + p(f"M{x + 26} -272 Q{x + 92} -284 {x + 158} -272", sw=5, color=c["lt"]))
    L["back"] = back
    seat = f'<rect x="-300" y="-132" width="600" height="96" rx="20" fill="{c["dk"]}" {INK}/>'
    for i in range(3):
        x = -290 + i * 194
        seat += (f'<rect x="{x}" y="-168" width="192" height="64" rx="24" fill="{c["base"]}" {INK}/>'
                 + p(f"M{x + 24} -150 H{x + 160}", sw=5, color=c["lt"]))
    seat += p("M-276 -84 H276", sw=4, color=c["base"])
    L["seat"] = seat
    for side, sx in (("arm_left", -1), ("arm_right", 1)):
        x0 = 262 * sx
        d = (f"M{x0 - 46} -40 V-196 C{x0 - 46} -238 {x0 + 46} -238 {x0 + 46} -196 V-40 Z")
        L[side] = (p(d, fill=c["base"]) + p(f"M{x0 - 30} -200 C{x0 - 22} -222 {x0 + 22} -222 {x0 + 30} -200",
                                             sw=5, color=c["lt"]))
    L["pillow"] = (p("M150 -250 C186 -262 236 -258 252 -246 C262 -214 258 -176 248 -160 "
                     "C214 -150 170 -152 146 -162 C138 -190 140 -226 150 -250 Z", fill=C["paper"])
                   + p("M168 -232 L232 -178 M232 -232 L168 -178", sw=4, color=C["paper_dk"]))
    return L


def sofa():
    return g("".join(g(v, id=f"sofa_{k}") for k, v in sofa_layers().items()), id="sofa")


def sofa_icon():
    """Mini sofa glyph for timelines/ledgers (one design, reused as instances)."""
    c = SOFA
    out = f'<rect x="-46" y="-40" width="92" height="34" rx="10" fill="{c["dk"]}" stroke="{C["ink"]}" stroke-width="5"/>'
    out += f'<rect x="-52" y="-16" width="104" height="22" rx="8" fill="{c["base"]}" stroke="{C["ink"]}" stroke-width="5"/>'
    out += f'<rect x="-60" y="-30" width="20" height="38" rx="8" fill="{c["base"]}" stroke="{C["ink"]}" stroke-width="5"/>'
    out += f'<rect x="40" y="-30" width="20" height="38" rx="8" fill="{c["base"]}" stroke="{C["ink"]}" stroke-width="5"/>'
    out += p("M-40 8 V16 M40 8 V16", sw=6, color=C["wood_dk"])
    return g(out, id="sofa_icon")


def promo_sign(text1="NO", text2="INTEREST?"):
    """Hanging store promo sign; strings to the top edge. Anchor = top centre of strings."""
    out = p("M-150 0 L-110 70 M150 0 L110 70", sw=5)
    out += f'<rect x="-210" y="66" width="420" height="230" rx="22" fill="{C["paper"]}" {INK}/>'
    out += f'<rect x="-196" y="80" width="392" height="202" rx="14" fill="none" stroke="{C["teal"]}" stroke-width="6"/>'
    out += g(t(0, 168, text1, 70, ls=-1) + t(0, 250, text2, 70, ls=-2), id="promo_sign_text")
    out += f'<circle cx="-150" cy="0" r="8" fill="{C["ink"]}"/><circle cx="150" cy="0" r="8" fill="{C["ink"]}"/>'
    return g(out, id="promo_sign")


def price_tag():
    out = p("M0 -60 Q14 -30 6 0", sw=3)
    out += p("M-34 0 H34 V92 L0 112 L-34 92 Z", fill=C["paper"])
    out += f'<circle cx="0" cy="16" r="7" fill="{C["wall_dk"]}" stroke="{C["ink"]}" stroke-width="4"/>'
    out += "".join(p(f"M{x} 40 V80", sw=3 + (x % 3), color=C["ink"]) for x in (-20, -12, -6, 2, 8, 16, 22))
    return g(out, id="price_tag")


def card_terminal():
    out = p("M-70 -110 H70 Q84 -110 84 -96 V96 Q84 110 70 110 H-70 Q-84 110 -84 96 V-96 Q-84 -110 -70 -110 Z",
            fill="#3B4F5E")
    out += f'<rect x="-58" y="-90" width="116" height="66" rx="8" fill="{C["teal_pale"]}" {INK.replace(str(SW), "5")}/>'
    out += p("M-40 -60 H24 M-40 -42 H6", sw=6, color=C["teal"])
    out += "".join(f'<rect x="{-54 + c * 40}" y="{-6 + r * 30}" width="28" height="20" rx="5" fill="{C["paper_dk"]}"/>'
                   for r in range(3) for c in range(3))
    return g(out, id="card_terminal")


# ---- time & condition ----------------------------------------------------------------------
def if_switch(state="up"):
    """Wall switch metaphor for the IF condition. state: up (teal/terms met) | down (coral/balance left)."""
    out = f'<rect x="-150" y="-230" width="300" height="460" rx="36" fill="{C["paper"]}" {INK}/>'
    out += f'<rect x="-92" y="-160" width="184" height="320" rx="26" fill="{C["paper_dk"]}" {INK}/>'
    out += f'<circle cx="0" cy="-200" r="9" fill="{C["paper_dkr"]}"/><circle cx="0" cy="200" r="9" fill="{C["paper_dkr"]}"/>'
    up = state == "up"
    lever_y, col = (-118, C["teal"]) if up else (118, C["coral"])
    out += g(f'<rect x="-74" y="{lever_y - 52 if up else lever_y - 92}" width="148" height="144" rx="24" '
             f'fill="{col}" {INK}/>' + t(0, lever_y + (36 if up else -4), "IF", 92, fill=C["paper"], ls=-3),
             id=f"if_switch_lever_{state}")
    return g(out, id=f"if_switch_{state}")


def calendar_page(label="MONTH 12", mark=None, w=240, h=260, header=None, text=None):
    """Tear-off calendar page; mark: None | 'circle' (coral). No real dates or numbers."""
    out = f'<rect x="{-w / 2}" y="{-h / 2}" width="{w}" height="{h}" rx="16" fill="{C["white"]}" {INK}/>'
    out += f'<rect x="{-w / 2 + 6}" y="{-h / 2 + 6}" width="{w - 12}" height="62" rx="10" fill="{header or C["gold"]}"/>'
    out += t(0, -h / 2 + 49, label, 30 if len(label) < 10 else 24, fill=text, ls=0.5)
    out += "".join(f'<circle cx="{-70 + c * 47}" cy="{-24 + r * 42}" r="9" fill="{C["paper_dk"]}"/>'
                   for r in range(4) for c in range(4))
    out += f'<rect x="-60" y="{-h / 2 - 16}" width="16" height="34" rx="6" fill="{C["ink"]}"/>'
    out += f'<rect x="44" y="{-h / 2 - 16}" width="16" height="34" rx="6" fill="{C["ink"]}"/>'
    if mark == "circle":
        out += f'<ellipse cx="47" cy="60" rx="34" ry="28" fill="none" stroke="{C["coral"]}" stroke-width="9"/>'
    return g(out, id=f"calendar_page_{label.lower().replace(' ', '_')}")


def month_strip(n=12, highlight_last=True):
    """12-month strip (schematic; 'M1..M12' only). Anchor = left edge centre."""
    out = ""
    for i in range(n):
        x = i * 64
        last = highlight_last and i == n - 1
        out += g(f'<rect x="{x}" y="-34" width="58" height="68" rx="10" fill="{C["coral_pale"] if last else C["white"]}" '
                 f'stroke="{C["coral"] if last else C["ink"]}" stroke-width="5"/>'
                 + t(x + 29, 12, str(i + 1), 28, fill=C["coral"] if last else C["ink"]), id=f"month_{i + 1:02d}")
    return g(out, id="month_strip")


def deadline_flag(text="PROMO ENDS"):
    out = p("M0 0 V-190", sw=8)
    out += p("M0 -190 H200 L174 -158 L200 -126 H0 Z", fill=C["coral"])
    out += t(96, -150, text, 22, fill=C["ink"], ls=0.5)
    out += f'<ellipse cx="0" cy="0" rx="26" ry="8" fill="{C["ink"]}"/>'
    return g(out, id="deadline_flag")


def clock_face():
    out = f'<circle r="150" fill="{C["gold"]}" {INK}/><circle r="128" fill="{C["paper"]}"/>'
    ticks = ""
    import math
    for i in range(12):
        a = math.radians(i * 30)
        r1, r2 = (112, 92) if i % 3 == 0 else (112, 100)
        ticks += f"M{r1 * math.sin(a):.1f} {-r1 * math.cos(a):.1f}L{r2 * math.sin(a):.1f} {-r2 * math.cos(a):.1f}"
    out += p(ticks, sw=7)
    return g(out, id="clock_face")


def clock_hand(kind="minute"):
    """Clock hand pointing to 12 with pivot at (0,0); rotate for time."""
    if kind == "minute":
        out = p("M0 14 V-104", sw=11)
    else:
        out = p("M0 12 V-66", sw=14)
    return g(out + f'<circle r="12" fill="{C["ink"]}"/>', id=f"clock_hand_{kind}")


def rewind_arrow():
    out = p("M120 -60 C160 20 120 110 20 130", sw=24, color=C["coral"])
    out += p("M138 -98 L92 -40 L160 -36 Z", fill=C["coral"], sw=6)
    return g(out, id="rewind_arrow")


# ---- ledger pieces ---------------------------------------------------------------------------
def balance_card(level=1.0, label="PROMOTIONAL BALANCE", remainder=False):
    """Promotional balance card with a schematic fill bar (no values). level 0..1."""
    w, h = 360, 220
    out = f'<rect x="{-w / 2}" y="{-h / 2}" width="{w}" height="{h}" rx="20" fill="{C["white"]}" {INK}/>'
    out += f'<rect x="{-w / 2 + 6}" y="{-h / 2 + 6}" width="{w - 12}" height="58" rx="14" fill="{C["teal"]}"/>'
    out += t(0, -h / 2 + 46, label, 22, fill=C["paper"], ls=1)
    out += f'<rect x="-150" y="10" width="300" height="56" rx="14" fill="{C["paper_dk"]}" stroke="{C["ink"]}" stroke-width="5"/>'
    if level > 0:
        fill = C["coral"] if remainder else C["teal_lt"]
        out += g(f'<rect x="-146" y="14" width="{292 * level:.1f}" height="48" rx="11" fill="{fill}"/>',
                 id="balance_fill")
    out += g(f'<g transform="translate(-118 -12) scale(.55)">{sofa_icon()}</g>', id="balance_sofa_icon")
    return g(out, id=f"balance_card_{int(level * 100):03d}")


def check_box(checked=True, label="MIN", label_color=None):
    out = f'<rect x="-36" y="-36" width="72" height="72" rx="12" fill="{C["white"]}" {INK}/>'
    if checked:
        out += g(p("M-20 2 L-6 18 L24 -18", sw=12, color=C["teal"]), id="check_mark")
    if label:
        out += t(0, 70, label, 22, fill=label_color)
    return g(out, id=f"check_box_{'on' if checked else 'off'}")


def waived_stamp():
    out = f'<g transform="rotate(-12)"><rect x="-190" y="-62" width="380" height="124" rx="18" fill="none" ' \
          f'stroke="{C["teal"]}" stroke-width="12"/>' + t(0, 26, "WAIVED", 76, fill=C["teal"], ls=4) + "</g>"
    return g(out, id="waived_stamp")


def charged_stamp():
    out = f'<g transform="rotate(-10)"><rect x="-200" y="-62" width="400" height="124" rx="18" fill="none" ' \
          f'stroke="{C["coral"]}" stroke-width="12"/>' + t(0, 24, "CHARGED", 70, fill=C["coral"], ls=3) + "</g>"
    return g(out, id="charged_stamp")


def magnifier():
    out = p("M52 52 L118 118", sw=26, color=C["wood_dk"])
    out += f'<circle r="76" fill="{C["sky"]}" fill-opacity=".35" stroke="{C["ink"]}" stroke-width="14"/>'
    out += p("M-40 -30 A52 52 0 0 1 -6 -54", sw=8, color=C["white"])
    return g(out, id="magnifier")


def receipt_clip():
    """Spike/clip holder labelled 'NOT CHARGED YET' that holds the interest receipt."""
    out = f'<rect x="-120" y="-22" width="240" height="44" rx="12" fill="{C["ink"]}"/>'
    out += t(0, 9, "NOT CHARGED YET", 20, fill=C["paper"], ls=1)
    out += f'<rect x="-30" y="16" width="60" height="22" rx="6" fill="{C["paper_dkr"]}" stroke="{C["ink"]}" stroke-width="5"/>'
    return g(out, id="receipt_clip")


def label_pill(text, fill=None, color=None, size=30, pad=26):
    w = len(text) * size * 0.62 + pad * 2
    out = f'<rect x="{-w / 2:.1f}" y="{-size * 0.95:.1f}" width="{w:.1f}" height="{size * 1.9:.1f}" ' \
          f'rx="{size * 0.95:.1f}" fill="{fill or C["ink"]}"/>'
    return g(out + t(0, size * 0.35, text, size, fill=color or C["paper"], ls=0.5), id="label_" +
             "".join(ch for ch in text.lower().replace(" ", "_") if ch.isalnum() or ch == "_")[:40])
