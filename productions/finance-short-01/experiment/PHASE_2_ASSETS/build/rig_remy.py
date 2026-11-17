"""Remy cutout rig (design version remy-2). Original artwork authored as SVG code.

All parts are drawn in ONE rest-pose frame (RCS: viewBox 0 0 640 1060, ground y=1030),
so any part can be re-posed by rotating about its documented pivot. Identity landmarks
(face outline, ear, eye spacing, nose, curl mass, palette) are ported from the Phase 1
thumbnail Remy (render.mjs shopper(), offset +159,+42) and must not be redrawn per shot.
"""
import math

from geom import R, S, T, apply, capsule, mul, svg_matrix
from style import C, SW

VIEWBOX = (0, 0, 640, 1060)
GROUND_Y = 1030

# ---- joints (rest frame) -------------------------------------------------------------
J = {
    "root": (314, 1030), "hip_c": (314, 600), "neck": (314, 296),
    "hip_n": (274, 600), "knee_n": (270, 806), "ankle_n": (266, 986),
    "hip_f": (356, 600), "knee_f": (360, 806), "ankle_f": (364, 986),
    "sho_n": (240, 374), "elb_n": (234, 532), "wri_n": (230, 678),
    "sho_f": (392, 368), "elb_f": (398, 526), "wri_f": (402, 672),
}

STROKE = f'stroke="{C["ink"]}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round"'


def g(body, **attrs):
    a = "".join(f' {k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f"<g{a}>{body}</g>"


def path(d, fill="none", stroke=True, sw=None, color=None, extra=""):
    st = ""
    if stroke:
        st = (f' stroke="{color or C["ink"]}" stroke-width="{sw or SW}" '
              'stroke-linejoin="round" stroke-linecap="round"')
    return f'<path d="{d}" fill="{fill}"{st}{extra}/>'


def shaded(outline, fill, shades=(), lines=()):
    """Base fill, interior shade shapes, then the outline on top (hides shade leaks)."""
    out = path(outline, fill=fill, stroke=False)
    out += "".join(path(d, fill=f, stroke=False) for d, f in shades)
    out += "".join(path(d, stroke=True, sw=w, color=c) for d, c, w in lines)
    return out + path(outline)


# ---- head ----------------------------------------------------------------------------
FACE = ("M235 156 Q231 114 302 107 Q384 100 398 173 L391 238 Q384 276 351 292 "
        "L281 291 Q248 276 244 233 L223 214 L222 181 Z")
HAIR = ("M240 212 Q214 214 212 188 Q194 172 207 148 Q186 128 202 106 Q195 80 226 76 "
        "Q228 52 256 54 Q270 33 296 41 Q318 24 341 43 Q367 33 383 56 Q406 57 411 82 "
        "Q433 95 425 121 Q431 143 410 151 Q396 167 376 168 L362 128 Q318 164 268 146 "
        "L262 204 Q252 216 240 212 Z")
EAR = "M226 190 Q199 186 204 214 Q209 241 246 237 L243 222 L231 210 Z"


def head_face():
    face_shades = [
        # far-side plane toward the ear, and the band under the curl fringe
        ("M236 160 Q246 196 252 236 Q258 268 281 291 Q248 276 244 233 L223 214 L222 181 Z",
         C["skin_dk"]),
        ("M362 132 Q318 168 268 150 L266 170 Q318 186 368 150 Z", C["skin_dk"]),
    ]
    out = shaded(FACE, C["skin"], face_shades)
    out += path("M376 204 Q383 214 382 226", stroke=True, sw=5, color=C["skin_lt"])  # cheek plane
    return out + shaded(EAR, C["skin"], lines=[("M221 203 Q212 212 220 224", C["skin_dk"], 5)])


def head_hair():
    hair_lines = [
        ("M222 104 Q232 92 246 96", C["hair_lt"], 6), ("M252 72 Q266 60 282 66", C["hair_lt"], 6),
        ("M306 56 Q322 46 338 54", C["hair_lt"], 6), ("M356 58 Q372 52 386 64", C["hair_lt"], 6),
        ("M214 160 Q220 146 234 146", C["hair_lt"], 6), ("M392 96 Q412 104 412 124", C["hair_lt"], 6),
        ("M286 92 Q340 72 396 104", C["hair_lt"], 7),  # main swoop highlight
        ("M232 128 Q244 116 258 120", C["hair_lt"], 5),
    ]
    hair_shades = [("M362 128 Q318 164 268 146 L268 128 Q318 146 356 112 Z", C["hair_dk"]),
                   ("M240 212 Q214 214 212 188 Q226 196 246 190 Z", C["hair_dk"])]
    return shaded(HAIR, C["hair"], hair_shades, hair_lines)


def head(expr):
    """Layer order inside the head: face+ear, features (eyes/brows/nose/mouth), hair fringe."""
    return g(head_face(), id="head_face") + features(expr) + g(head_hair(), id="head_hair")


EYE_L, EYE_R = (303, 207), (361, 206)


def eye(c, kind, gx, gy):
    x, y = c[0] + gx, c[1] + gy
    if kind in ("open", "wide", "squint"):
        rx, ry = {"open": (7.5, 12.5), "wide": (9, 15.5), "squint": (8, 6)}[kind]
        out = f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{C["ink"]}"/>'
        if kind != "squint":
            out += f'<circle cx="{x + 2.6}" cy="{y - ry * .36}" r="2.7" fill="{C["white"]}"/>'
        return out
    if kind == "half":
        out = f'<ellipse cx="{x}" cy="{y + 3}" rx="7.5" ry="9.5" fill="{C["ink"]}"/>'
        out += path(f"M{c[0] - 13} {c[1] - 18}H{c[0] + 13}V{c[1] + 1}Q{c[0]} {c[1] + 4} {c[0] - 13} {c[1] + 1}Z",
                    fill=C["skin"], stroke=False)
        return out + path(f"M{c[0] - 11} {c[1] + 1}Q{c[0]} {c[1] + 4} {c[0] + 11} {c[1] + 1}", sw=5)
    if kind == "happy":
        return path(f"M{c[0] - 10} {c[1] + 5}Q{c[0]} {c[1] - 10} {c[0] + 10} {c[1] + 5}", sw=6)
    if kind == "closed":
        return path(f"M{c[0] - 10} {c[1] - 1}Q{c[0]} {c[1] + 9} {c[0] + 10} {c[1] - 1}", sw=6)
    raise ValueError(kind)


BROWS = {
    "neutral": ("M288 186 Q300 181 313 183", "M346 182 Q358 181 371 186"),
    "raised": ("M288 174 Q300 165 314 169", "M345 168 Q359 164 372 172"),
    "worried": ("M287 189 Q301 185 313 178", "M345 177 Q358 184 372 190"),
    "focused": ("M288 180 Q301 183 314 190", "M345 189 Q358 182 371 178"),
    "skeptic": ("M288 172 Q300 164 314 169", "M345 186 Q358 186 371 186"),
    "soft": ("M288 182 Q300 177 313 179", "M346 178 Q359 177 371 182"),
}

MOUTH = {
    "neutral": lambda: path("M315 259 Q330 263 346 258", sw=7),
    "smile": lambda: path("M310 251 Q330 270 352 250", sw=7),
    "frown": lambda: path("M312 266 Q331 251 350 263", sw=7),
    "flat": lambda: path("M316 261 L347 259", sw=7),
    "smirk": lambda: path("M314 262 Q334 263 351 251", sw=7),
    "wavy": lambda: path("M312 262 Q318 256 324 262 Q330 268 336 262 Q342 256 348 262", sw=6),
    "grin": lambda: (path("M308 249 Q331 253 354 248 Q350 279 330 280 Q310 278 308 249 Z", fill=C["mouth"])
                     + path("M313 252 Q331 255 350 251 L348 260 Q331 263 315 261 Z", fill=C["teeth"], stroke=False)
                     + path("M308 249 Q331 253 354 248 Q350 279 330 280 Q310 278 308 249 Z", sw=6)),
    "open": lambda: (path("M317 250 Q332 245 345 251 Q350 272 332 278 Q315 273 317 250 Z", fill=C["mouth"])
                     + path("M321 270 Q332 262 343 269 Q338 277 332 278 Q324 277 321 270 Z", fill=C["tongue"], stroke=False)
                     + path("M317 250 Q332 245 345 251 Q350 272 332 278 Q315 273 317 250 Z", sw=6)),
    "oh": lambda: (f'<ellipse cx="331" cy="263" rx="9" ry="11.5" fill="{C["mouth"]}" '
                   f'stroke="{C["ink"]}" stroke-width="6"/>'),
    "grimace": lambda: (path("M309 251 L353 249 L351 270 L311 271 Z", fill=C["teeth"])
                        + path("M323 251 V270 M338 250 V270 M310 261 H352", sw=3)
                        + path("M309 251 L353 249 L351 270 L311 271 Z", sw=6)),
}

EXPRESSIONS = {
    # preset: eyes, brows, mouth, blush, gaze
    "neutral": ("open", "neutral", "neutral", False),
    "curious": ("open", "raised", "smirk", False),
    "intrigued": ("open", "skeptic", "smirk", False),
    "confused": ("open", "skeptic", "wavy", False),
    "concerned": ("open", "worried", "frown", False),
    "worried_talk": ("open", "worried", "open", False),
    "shocked": ("wide", "raised", "oh", False),
    "alarmed": ("wide", "worried", "grimace", False),
    "relieved": ("closed", "soft", "smile", True),
    "happy": ("happy", "soft", "grin", True),
    "content": ("open", "soft", "smile", True),
    "focused": ("squint", "focused", "flat", False),
    "determined": ("open", "focused", "smirk", False),
    "skeptical": ("half", "skeptic", "flat", False),
    "deadpan": ("half", "neutral", "flat", False),
}


def features(expr):
    eyes, brows, mouth, blush = EXPRESSIONS[expr["preset"]] if "preset" in expr else (None,) * 4
    eyes, brows = expr.get("eyes", eyes), expr.get("brows", brows)
    mouth, blush = expr.get("mouth", mouth), expr.get("blush", blush)
    gx, gy = expr.get("gaze", (0, 0))
    out = ""
    if blush:
        out += f'<ellipse cx="370" cy="244" rx="11" ry="6.5" fill="{C["blush"]}"/>'
        out += f'<ellipse cx="284" cy="247" rx="10" ry="6" fill="{C["blush"]}"/>'
    out += eye(EYE_L, eyes, gx, gy) + eye(EYE_R, eyes, gx, gy)
    bl, br = BROWS[brows]
    out += path(bl, sw=8) + path(br, sw=8)
    out += path("M336 212 L346 236 L329 241", sw=5)  # nose: Phase 1 landmark, never changes
    out += MOUTH[mouth]()
    if expr.get("sweat"):
        out += path("M406 168 Q416 186 410 196 Q400 204 394 194 Q392 184 406 168 Z", fill=C["sky"], sw=4)
    return g(out, id="face_features")


NECK = "M284 262 L281 334 Q315 356 347 333 L344 260 Z"


def neck():
    return shaded(NECK, C["skin"], [("M284 262 L283 300 Q315 318 345 297 L344 260 Z", C["skin_dk"])])


# ---- torso ---------------------------------------------------------------------------
TORSO = ("M238 338 C264 314 362 308 388 330 C410 346 418 378 418 412 L422 540 "
         "Q320 566 214 546 L212 412 C212 378 220 352 238 338 Z")
PELVIS = "M222 532 L414 528 L420 616 Q318 632 216 616 Z"


def torso():
    out = shaded(PELVIS, C["slate"], [("M216 590 Q318 606 420 590 L420 616 Q318 632 216 616 Z", C["slate_dk"])])
    hem = "M214 518 Q320 538 421 512 L422 540 Q320 566 214 546 Z"
    ribs = "".join(f"M{x} {521 + (x - 214) * 0.005 + (8 if 250 < x < 390 else 4)}v20" for x in range(232, 412, 18))
    body = [("M212 412 C212 378 220 352 238 338 C246 364 242 430 248 520 L214 520 Z", C["teal_dk"]),
            ("M396 340 C410 356 416 380 417 412 L420 512 Q410 514 402 515 L398 410 C398 380 392 356 380 334 Z",
             C["teal_dk"]),
            (hem, C["teal_dk"])]
    out += shaded(TORSO, C["teal"], body, [(ribs, C["ink"], 3), ("M352 372 Q370 420 372 482", C["teal_lt"], 6)])
    # neckline + collar (cream shirt points, Phase 1 landmark)
    out += path("M279 330 Q314 356 349 328", fill=C["teal_dk"], sw=6)
    out += shaded("M278 326 Q286 348 300 368 L318 346 Q300 340 288 324 Z", C["paper"],
                  [("M290 344 Q296 356 300 368 L306 360 Q298 352 292 342 Z", C["paper_dk"])])
    out += shaded("M318 346 L338 366 Q350 348 353 322 Q338 336 318 346 Z", C["paper"])
    return out


# ---- limbs -----------------------------------------------------------------------------
def leg(side):
    hip, knee, ankle = J[f"hip_{side}"], J[f"knee_{side}"], J[f"ankle_{side}"]
    tone = C["slate"] if side == "n" else C["slate_dk"]
    thigh = shaded(capsule(hip, 41, knee, 33), tone,
                   lines=[(f"M{hip[0] + 14} {hip[1] + 40}L{knee[0] + 10} {knee[1] - 20}", C["slate_dk"], 4)])
    shin = shaded(capsule(knee, 32, (ankle[0], ankle[1] - 6), 27), tone)
    return {"thigh": thigh, "shin": shin, "shoe": shoe(ankle)}


def shoe(ankle):
    x, y = ankle[0] - 266, ankle[1] - 986
    d = (f"M{232 + x} {966 + y} C{232 + x} {950 + y} {264 + x} {946 + y} {290 + x} {958 + y} "
         f"L{332 + x} {974 + y} C{354 + x} {982 + y} {362 + x} {998 + y} {358 + x} {1014 + y} "
         f"L{354 + x} {1030 + y} L{238 + x} {1030 + y} C{228 + x} {1030 + y} {226 + x} {1018 + y} "
         f"{228 + x} {1004 + y} Z")
    sole = f"M{227 + x} {1016 + y} L{358 + x} {1016 + y} L{354 + x} {1030 + y} L{238 + x} {1030 + y} Z"
    laces = f"M{294 + x} {964 + y} L{302 + x} {978 + y} M{307 + x} {970 + y} L{315 + x} {983 + y}"
    return shaded(d, C["shoe"], [(sole, C["sole"])], [(laces, C["sole"], 4)])


def upper_arm(side):
    sho, elb = J[f"sho_{side}"], J[f"elb_{side}"]
    return shaded(capsule(sho, 33, elb, 28), C["teal"] if side == "n" else C["teal_dk"])


def forearm(side):
    elb, wri = J[f"elb_{side}"], J[f"wri_{side}"]
    tone = C["teal"] if side == "n" else C["teal_dk"]
    return shaded(capsule(elb, 27, (wri[0], wri[1] - 14), 24), tone)


def cuff(side):
    wri = J[f"wri_{side}"]
    return (f'<rect x="{wri[0] - 26}" y="{wri[1] - 30}" width="52" height="26" rx="9" fill="{C["paper"]}" '
            f'{STROKE}/>' + path(f"M{wri[0] - 20} {wri[1] - 17}H{wri[0] + 20}", sw=3, color=C["paper_dkr"]))


# ---- hands: authored pointing +x, wrist at (0,0), thumb toward -y ------------------------
def _hand(body, extra_lines=(), thumb=None):
    out = path(body, fill=C["skin"], stroke=False)
    out += "".join(path(d, sw=3.5, color=C["skin_dk"]) for d in extra_lines)
    out += path(body, sw=HAND_SW)
    if thumb:
        out += _app(thumb)
    return out


def _app(d):
    """Appendage (thumb/finger): filled closed, stroked open so its base merges into the palm."""
    return path(d, fill=C["skin"], stroke=False) + path(d.rstrip(" Z"), sw=HAND_SW)


HAND_SW = 6.5


def _finger(p1, r1, p2, r2):
    d = capsule(p1, r1, p2, r2)
    return path(d, fill=C["skin"], stroke=False) + path(d, sw=HAND_SW)


FIST = ("M-4 -20 C8 -24 32 -24 44 -19 C53 -13 55 3 51 13 C47 21 35 24 22 24 "
        "C10 24 0 22 -4 20 Z")
FIST_FOLDS = ["M53 -4 C47 -3 44 0 45 4", "M52 7 C46 8 43 11 44 15"]
THUMB_ACROSS = "M8 -13 L36 -10 C44 -9.5 45 3 37 3 L8 1 Z"

HANDS = {
    "relaxed": lambda: _hand(
        "M-4 -19 C10 -23 28 -23 40 -20 C54 -17 66 -9 68 3 C69 13 63 21 55 21 "
        "C48 21 44 17 40 17 C30 22 10 23 -4 19 Z",
        ["M48 -13 C56 -9 60 -1 60 8", "M42 -4 C49 0 52 6 51 13"],
        "M4 -18 C12 -30 30 -35 42 -31 C49 -28 49 -21 42 -19 C32 -17 20 -14 12 -11 Z"),
    "point": lambda: (_finger((34, -13), 7.5, (82, -13), 7) + _hand(FIST, FIST_FOLDS)
                      + _app(THUMB_ACROSS)),
    "fist": lambda: _hand(FIST, ["M50 -14 C45 -13 43 -10 44 -6"] + FIST_FOLDS) + _app(THUMB_ACROSS),
    "open": lambda: (_finger((38, -15), 7, (72, -24), 6.5) + _finger((41, -3), 7.5, (79, -5), 7)
                     + _finger((41, 8), 7, (75, 12), 6.5) + _finger((38, 18), 6, (64, 25), 5.5)
                     + _finger((14, -14), 9, (28, -41), 7.5)
                     + _hand("M-4 -20 C8 -25 28 -26 42 -22 L45 21 C32 26 8 26 -4 20 Z", ["M14 2 Q25 9 35 4"])),
    "palm_up": lambda: _hand(
        "M-4 -11 C14 -15 40 -17 62 -17 C77 -17 83 -8 77 -2 C70 5 52 7 38 9 "
        "C22 13 8 15 -4 15 Z",
        ["M44 -8 L70 -9", "M40 1 L64 0"],
        "M7 -13 C14 -28 31 -32 40 -25 C44 -20 39 -15 30 -15 Z"),
    "grip_back": lambda: _hand(
        "M-4 -20 C10 -24 34 -24 52 -20 C66 -17 70 -6 68 4 C66 14 56 18 44 18 "
        "C28 22 8 23 -4 19 Z",
        ["M58 -14 C64 -10 66 -4 65 2", "M50 -2 C57 1 59 7 57 12"]),
    "grip_front": lambda: _app("M8 -12 C14 -24 30 -27 40 -22 C47 -18 45 -9 37 -9 C29 -9 19 -7 10 -5 Z"),
    "pen_back": lambda: _hand(FIST, FIST_FOLDS),
    "pen_front": lambda: _finger((26, -17), 7, (50, -12), 6.5) + _app(THUMB_ACROSS),
    "release": lambda: (_finger((40, -14), 6.5, (74, -16), 6) + _finger((42, -3), 7, (78, 4), 6.5)
                        + _finger((40, 8), 6.5, (70, 20), 6) + _finger((36, 17), 5.5, (58, 30), 5)
                        + _finger((14, -14), 8.5, (32, -36), 7)
                        + _hand("M-4 -19 C8 -24 28 -25 42 -21 L44 20 C32 25 8 25 -4 19 Z")),
}
HAND_FRONT_LAYER = {"grip_back": "grip_front", "pen_back": "pen_front"}


# ---- pose evaluation --------------------------------------------------------------------
DEFAULT_POSE = {
    "body_dy": 0, "lean": 0, "neck": 0, "head_flip": False,
    "arm_n": (6, -4, 0), "arm_f": (-6, 4, 0), "leg_n": (3, 0, 0), "leg_f": (-3, 0, 0),
    "hand_n": "relaxed", "hand_f": "relaxed", "flip_n": False, "flip_f": True,
    "expr": {"preset": "neutral"}, "slots": {}, "props": [],
}

# back-to-front layer slots
SLOTS = ["legF", "legN", "armF", "neck", "torso", "head", "mid", "armN", "prop", "top"]


def ik(side, spec):
    """2-bone IK in the upper-body rest frame: {'ik': (x, y), 'hand_dir': deg, 'elbow': 'down'|'up'}.
    hand_dir is the world direction the fingers point (0 = right, 90 = down, -90 = up)."""
    sx, sy = J[f"sho_{side}"]
    ex, ey = J[f"elb_{side}"]
    wx, wy = J[f"wri_{side}"]
    l1, l2 = math.hypot(ex - sx, ey - sy), math.hypot(wx - ex, wy - ey)
    u_rest = math.degrees(math.atan2(ey - sy, ex - sx))
    f_rest = math.degrees(math.atan2(wy - ey, wx - ex))
    tx, ty = spec["ik"]
    dist = min(max(math.hypot(tx - sx, ty - sy), abs(l1 - l2) + 1), l1 + l2 - 0.5)
    td = math.atan2(ty - sy, tx - sx)
    a = math.acos((l1 * l1 + dist * dist - l2 * l2) / (2 * l1 * dist))
    sols = []
    for b in (1, -1):
        t1 = td + b * a
        elx, ely = sx + l1 * math.cos(t1), sy + l1 * math.sin(t1)
        sols.append((ely, t1, elx))
    sols.sort(reverse=spec.get("elbow", "down") == "down")
    ely, t1, elx = sols[0]
    t2 = math.degrees(math.atan2(ty - ely, tx - elx))
    sho = math.degrees(t1) - u_rest
    elb = t2 - f_rest - sho
    wri = spec.get("hand_dir", t2) - 90 - sho - elb
    wrap = lambda a: (a + 180) % 360 - 180  # noqa: E731  shortest-path angles for tweening
    return (wrap(sho), wrap(elb), wrap(wri))


REMY = {"head": lambda expr: head(expr), "neck": lambda: neck(), "torso": lambda: torso(), "leg": lambda s: leg(s),
        "upper_arm": lambda s: upper_arm(s), "forearm": lambda s: forearm(s), "cuff": lambda s: cuff(s),
        "hand": lambda shape: HANDS[shape]()}


def evaluate(pose, design=None):
    """Forward kinematics. Returns ordered list of (part_id, slot, matrix, svg).
    design: dict of part drawers (defaults to Remy); other characters reuse the skeleton."""
    d = {**REMY, **(design or {})}
    p = {**DEFAULT_POSE, **pose}
    base = T(0, p["body_dy"])
    upper = mul(base, R(p["lean"], *J["hip_c"]))
    parts = []

    def add(pid, slot, m, svg):
        parts.append((pid, p["slots"].get(pid, slot), m, svg))

    for side, slot in (("f", "legF"), ("n", "legN")):
        hip, knee, ank = p[f"leg_{side}"]
        L = d["leg"](side)
        m_th = mul(base, R(hip, *J[f"hip_{side}"]))
        m_sh = mul(m_th, R(knee, *J[f"knee_{side}"]))
        m_ft = mul(m_sh, R(ank, *J[f"ankle_{side}"]))
        add(f"shin_{side}", slot, m_sh, L["shin"])
        add(f"thigh_{side}", slot, m_th, L["thigh"])
        add(f"shoe_{side}", slot, m_ft, L["shoe"])
    add("neck", "neck", upper, d["neck"]())
    add("torso", "torso", upper, d["torso"]())
    m_head = mul(upper, R(p["neck"], *J["neck"]))
    if p["head_flip"]:
        cx = 314
        m_head = mul(m_head, mul(T(cx, 0), mul(S(-1, 1), T(-cx, 0))))
    add("head", "head", m_head, d["head"](p["expr"]))
    hand_mats = {}
    for side, slot in (("f", "armF"), ("n", "armN")):
        arm = p[f"arm_{side}"]
        sho, elb, wri = ik(side, arm) if isinstance(arm, dict) else arm
        m_up = mul(upper, R(sho, *J[f"sho_{side}"]))
        m_fo = mul(m_up, R(elb, *J[f"elb_{side}"]))
        w = J[f"wri_{side}"]
        m_ha = mul(m_fo, mul(R(wri, *w), mul(T(*w), R(90))))
        if p[f"flip_{side}"]:
            m_ha = mul(m_ha, S(1, -1))
        hand_mats[side] = m_ha
        shape = p[f"hand_{side}"]
        add(f"upper_arm_{side}", slot, m_up, d["upper_arm"](side))
        add(f"forearm_{side}", slot, m_fo, d["forearm"](side))
        add(f"hand_{side}", slot, m_ha, d["hand"](shape))
        if shape in HAND_FRONT_LAYER:
            add(f"hand_{side}_front", "top", m_ha, d["hand"](HAND_FRONT_LAYER[shape]))
        add(f"cuff_{side}", slot, m_fo, d["cuff"](side))
    for i, pr in enumerate(p["props"]):
        x, y, rot, sc = pr.get("at", (0, 0, 0, 1))
        anchor = hand_mats[pr["hand"]] if pr.get("hand") else upper
        m = mul(anchor, mul(T(x, y), mul(R(rot), S(sc))))
        add(pr.get("id", f"prop_{i}"), pr.get("slot", "prop"), m, pr["svg"])
    order = {s: i for i, s in enumerate(SLOTS)}
    return sorted(parts, key=lambda t: order[t[1]])  # stable: keeps part order inside a slot


def render(pose, prefix="remy", design=None):
    return "".join(f'<g id="{prefix}__{pid}" data-slot="{slot}" transform="{svg_matrix(m)}">{svg}</g>'
                   for pid, slot, m, svg in evaluate(pose, design))


def world_point(pose, part_id, local_pt, design=None):
    for pid, _, m, _ in evaluate(pose, design):
        if pid == part_id:
            return apply(m, local_pt)
    raise KeyError(part_id)
