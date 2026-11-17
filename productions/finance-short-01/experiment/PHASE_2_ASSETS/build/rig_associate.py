"""Store associate (design version assoc-1): neutral supporting character for B2 only.

Reuses Remy's skeleton, limb system and hand library (recoloured) so motion grammar matches,
while head shape, hair, glasses, apron and palette make the identity clearly distinct.
"""
import rig_remy as R
from rig_remy import J, capsule, path, shaded
from style import C

SKIN, SKIN_DK = "#D9A27A", "#B98058"
HAIR, HAIR_LT = "#2B2230", "#4A3C4E"
SHIRT, SHIRT_DK = C["paper"], C["paper_dk"]
APRON, APRON_DK = "#8DB39E", "#6F977F"

FACE = "M246 176 C246 110 290 92 322 92 C362 92 396 116 396 180 C396 244 366 290 320 290 C276 290 246 246 246 176 Z"


def head(expr):
    out = shaded("M222 178 Q232 134 262 112 L268 220 Q244 226 222 178 Z", HAIR)  # back hair
    out += shaded(FACE, SKIN, [("M252 196 Q262 262 304 288 Q262 282 248 226 Z", SKIN_DK)])
    out += shaded("M250 190 Q228 186 232 212 Q236 236 258 232 Z", SKIN)
    preset = R.EXPRESSIONS.get(expr.get("preset", "content"))
    eyes, brows, mouth = expr.get("eyes", preset[0]), expr.get("brows", preset[1]), expr.get("mouth", preset[2])
    gx, gy = expr.get("gaze", (0, 0))
    for c in ((298, 206), (354, 205)):
        out += R.eye((c[0], c[1]), eyes, gx, gy)
        out += f'<circle cx="{c[0]}" cy="{c[1]}" r="21" fill="none" stroke="{C["ink"]}" stroke-width="6"/>'
    out += path("M319 204 Q326 198 333 204", sw=5)
    bl, br = R.BROWS[brows]
    out += path(bl, sw=7, extra=' transform="translate(-4 -8)"') + path(br, sw=7, extra=' transform="translate(-6 -8)"')
    out += path("M334 214 Q344 232 330 238", sw=5)
    out += f'<g transform="translate(-4 4)">{R.MOUTH[mouth]()}</g>'
    hair = ("M246 168 C238 112 278 84 322 84 C370 84 404 112 400 170 C380 140 350 124 322 128 "
            "C300 130 276 138 262 158 L258 196 Z")
    out += shaded(hair, HAIR, lines=[("M280 104 Q318 92 360 104", HAIR_LT, 6)])
    out += shaded("M290 66 C290 38 350 38 350 66 C350 92 290 92 290 66 Z", HAIR,
                  lines=[("M302 58 Q318 48 336 56", HAIR_LT, 5)])
    return out


def neck():
    return shaded("M290 262 L287 336 Q318 352 346 334 L344 262 Z", SKIN,
                  [("M290 262 L289 298 Q318 312 345 296 L344 262 Z", SKIN_DK)])


def torso():
    out = shaded(R.PELVIS, C["slate"])
    out += shaded(R.TORSO, SHIRT, [("M212 412 C212 378 220 352 238 338 C246 364 242 430 248 520 L214 520 Z", SHIRT_DK)])
    apron = "M262 372 L366 368 L380 560 Q320 574 252 562 Z"
    out += shaded(apron, APRON, [("M262 372 L274 372 L268 560 L252 562 Z", APRON_DK)],
                  [("M262 376 L232 336 M366 372 L394 334", APRON_DK, 6)])
    out += shaded("M290 450 H346 V500 Q318 508 290 500 Z", APRON, lines=[("M296 462 H340", APRON_DK, 4)])
    out += f'<rect x="336" y="396" width="34" height="22" rx="5" fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="5"/>'
    out += path("M284 330 Q316 352 350 328", fill=SHIRT_DK, sw=6)
    return out


def upper_arm(side):
    return shaded(capsule(J[f"sho_{side}"], 31, J[f"elb_{side}"], 26), SHIRT if side == "n" else SHIRT_DK)


def forearm(side):
    elb, wri = J[f"elb_{side}"], J[f"wri_{side}"]
    return shaded(capsule(elb, 25, (wri[0], wri[1] - 14), 22), SKIN if side == "n" else SKIN_DK)


def cuff(side):  # rolled sleeve band at the elbow instead of a wrist cuff
    e = J[f"elb_{side}"]
    return f'<rect x="{e[0] - 30}" y="{e[1] - 14}" width="60" height="26" rx="10" fill="{SHIRT}" ' \
           f'stroke="{C["ink"]}" stroke-width="7"/>'


def leg(side):
    L = R.leg(side)
    L["shoe"] = L["shoe"].replace(C["shoe"], C["wood_dk"])
    return L


def hand(shape):
    return R.HANDS[shape]().replace(C["skin"], SKIN).replace(C["skin_dk"], SKIN_DK)


DESIGN = {"head": head, "neck": neck, "torso": torso, "upper_arm": upper_arm, "forearm": forearm,
          "cuff": cuff, "leg": leg, "hand": hand}

POSES = {
    "assoc_stand": dict(pose={"expr": {"preset": "content"}}, compatible=["content", "neutral", "happy"],
                        use="B2 store wide, beside the sofa"),
    "assoc_present": dict(
        pose={"lean": 4, "arm_f": {"ik": (560, 470), "hand_dir": 4}, "hand_f": "palm_up", "flip_f": False,
              "expr": {"preset": "happy"}},
        compatible=["happy", "content", "neutral"], use="B2 presenting the sofa / offer (mirror to face Remy)"),
    "assoc_offer_sheet": dict(
        pose={"lean": 3, "arm_f": {"ik": (540, 520), "hand_dir": -20}, "hand_f": "grip_back", "flip_f": False,
              "expr": {"preset": "content", "gaze": (4, 3)}},
        compatible=["content", "neutral"], use="B2 handing over the offer sheet across the counter"),
}


def render(pose, prefix="associate"):
    return R.render(pose, prefix=prefix, design=DESIGN)
