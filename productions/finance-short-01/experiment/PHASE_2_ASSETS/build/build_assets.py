"""Build the Phase 2 asset library: SVG sources, PNG exports, manifests, rig data, scene map,
captions, contact sheets and automated QA. Deterministic: same code -> same files.

Run from PHASE_2_ASSETS:  python3 build/build_assets.py
"""
import csv
import hashlib
import json
import re
import struct
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import diagrams as D  # noqa: E402
import env as E  # noqa: E402
import poses_remy as PR  # noqa: E402
import props as P  # noqa: E402
import rig_associate as A  # noqa: E402
import rig_remy as R  # noqa: E402
import scenes as SC  # noqa: E402
import shots as SH  # noqa: E402
import typography as TY  # noqa: E402
from style import C  # noqa: E402

DATE = "2026-10-13"
PROV = ("Original vector artwork authored as SVG code by Claude (claude-opus-5-5) in build/{mod} on "
        f"{DATE}. No AI raster/image generation, stock, competitor or brand assets. Rendered with "
        "Sharp 0.35.5 / librsvg 2.63.2.")
PROV_REMY = PROV + (" Identity landmarks (face outline, ear, eye spacing, nose, curl mass, palette) ported "
                    "from Phase 1 thumbnail_sources/render.mjs shopper() at offset (+159,+42).")
records, jobs = [], []


def doc(inner, vb, title):
    x, y, w, h = vb
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}">'
            f"<title>{title}</title>{inner}</svg>")


def ids_in(svg):
    seen = []
    for i in re.findall(r'\sid="([^"]+)"', svg):
        if i not in seen:
            seen.append(i)
    return seen


def emit(rel, aid, inner, vb, *, category, cls, base, anchor, mod, pivots=None, layers=None, occlusion="",
         compatible="", usage="", facts="", qa="PASS", qa_notes="", png=True, density=144, prov=None):
    out = ROOT / rel / f"{aid}.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    svg = doc(inner, vb, aid)
    out.write_text(svg)
    rec = {"asset_id": aid, "category": category, "class": cls, "base_design": base,
           "svg": str(out.relative_to(ROOT)), "png": "", "viewBox": " ".join(map(str, vb)),
           "width": vb[2], "height": vb[3], "anchor": anchor, "pivots": pivots or "",
           "layers": layers if layers is not None else ids_in(inner)[:40], "occlusion": occlusion,
           "compatible": compatible, "usage": usage, "facts": facts,
           "provenance": (prov or PROV).format(mod=mod), "qa": qa, "qa_notes": qa_notes}
    if png:
        pth = out.with_suffix(".png")
        rec["png"] = str(pth.relative_to(ROOT))
        jobs.append({"svg": str(out), "png": str(pth), "density": density})
    records.append(rec)
    return rec


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    return struct.unpack(">II", head[16:24])


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# ---------------------------------------------------------------- Remy rig -------------------
REST = {"arm_n": (0, 0, 0), "arm_f": (0, 0, 0), "leg_n": (0, 0, 0), "leg_f": (0, 0, 0),
        "hand_n": "relaxed", "hand_f": "relaxed", "flip_n": False, "flip_f": True, "expr": {"preset": "neutral"}}
RCS_VB = (0, 0, 640, 1060)
HEAD_VB = (190, 20, 260, 300)
POSE_VB = (-160, 0, 960, 1060)
PART_PARENT = {"thigh": ("hip", "root"), "shin": ("knee", "thigh"), "shoe": ("ankle", "shin"),
               "upper_arm": ("sho", "torso"), "forearm": ("elb", "upper_arm"), "cuff": ("elb", "upper_arm"),
               "hand": ("wri", "forearm")}


def remy_parts():
    parts = []
    for pid, slot, m, svg in R.evaluate(REST):
        if pid == "head":
            continue
        from geom import svg_matrix
        aid = f"CHR_REMY_PART_{pid.upper()}"
        kind = re.sub(r"_(n|f)(_front)?$", "", pid)
        side = "near (screen-left)" if pid.endswith("_n") else "far (screen-right)" if pid.endswith("_f") else ""
        joint, parent = PART_PARENT.get(kind, ("hip_c" if pid in ("torso", "neck") else "", "upper_body"))
        piv = R.J.get(f"{joint}_{pid[-1]}") if joint in ("hip", "knee", "ankle", "sho", "elb", "wri") else R.J.get(joint)
        emit("characters/main/parts", aid, f'<g transform="{svg_matrix(m)}">{svg}</g>', RCS_VB,
             category="character_part", cls="DERIVED_EXPORT" if kind == "hand" else
             "AUTHORED_BASE" if pid.endswith("_n") or pid in ("neck", "torso") else "DERIVED_STATE",
             base=aid if not pid.endswith("_f") else aid[:-1] + "N", mod="rig_remy.py",
             anchor="Rest-frame placement (RCS 640x1060, ground y=1030)",
             pivots=f"{joint or 'hip_c'} {piv}", occlusion=f"default slot '{slot}' {side}",
             compatible="all Remy poses", usage="Rebuild rig in Remotion", prov=PROV_REMY,
             qa_notes="Far-side parts use darker tone of the same design" if pid.endswith("_f") else "")
        parts.append({"part": pid, "asset_id": aid, "joint": joint, "parent": parent, "pivot": piv, "slot": slot})
    for aid, inner, note in (("CHR_REMY_PART_HEAD_FACE", R.head_face(), "face, ear, cheek plane"),
                             ("CHR_REMY_PART_HAIR", R.head_hair(), "curl mass + fringe; drawn above features"),
                             ("CHR_REMY_PART_HEAD_NEUTRAL", R.head({"preset": "neutral"}), "assembled head")):
        emit("characters/main/parts", aid, inner, HEAD_VB, category="character_part",
             cls="AUTHORED_BASE" if "NEUTRAL" not in aid else "DERIVED_STATE", base=aid, mod="rig_remy.py",
             anchor="RCS head frame", pivots=f"neck {R.J['neck']}", occlusion=note, compatible="all expressions",
             usage="All Remy shots", prov=PROV_REMY)
    return parts


def remy_faces():
    comps = []
    for kind in ("open", "wide", "half", "happy", "closed", "squint"):
        inner = R.eye(R.EYE_L, kind, 0, 0) + R.eye(R.EYE_R, kind, 0, 0)
        if kind == "half":
            inner = f'<g>{inner}</g>'
        aid = f"CHR_REMY_FACE_EYES_{kind.upper()}"
        emit("characters/main/faces", aid, inner, HEAD_VB, category="face_component", cls="AUTHORED_BASE", base=aid,
             mod="rig_remy.py", anchor="RCS head frame; centres L(303,207) R(361,206)",
             occlusion="'half' paints a skin lid: place above eyes, below hair",
             compatible="gaze offset (dx,dy) within +-6px", usage="Expression switches", prov=PROV_REMY)
        comps.append(aid)
    for kind, (bl, br) in R.BROWS.items():
        aid = f"CHR_REMY_FACE_BROWS_{kind.upper()}"
        emit("characters/main/faces", aid, R.path(bl, sw=8) + R.path(br, sw=8), HEAD_VB, category="face_component",
             cls="AUTHORED_BASE", base=aid, mod="rig_remy.py", anchor="RCS head frame", occlusion="below hair layer",
             usage="Expression switches", prov=PROV_REMY)
        comps.append(aid)
    for kind, fn in R.MOUTH.items():
        aid = f"CHR_REMY_FACE_MOUTH_{kind.upper()}"
        emit("characters/main/faces", aid, fn(), HEAD_VB, category="face_component", cls="AUTHORED_BASE", base=aid,
             mod="rig_remy.py", anchor="RCS head frame; mouth centre ~(331,259)",
             occlusion="No lip-sync: Remy is an on-screen actor, the narrator is off-screen",
             usage="Expression switches", prov=PROV_REMY)
        comps.append(aid)
    emit("characters/main/faces", "CHR_REMY_FACE_NOSE", R.path("M336 212 L346 236 L329 241", sw=5), HEAD_VB,
         category="face_component", cls="AUTHORED_BASE", base="CHR_REMY_FACE_NOSE", mod="rig_remy.py",
         anchor="Phase 1 landmark; never changes", usage="All Remy shots", prov=PROV_REMY)
    for preset in R.EXPRESSIONS:
        aid = f"CHR_REMY_EXPR_{preset.upper()}"
        emit("characters/main/expressions", aid, R.head({"preset": preset}), HEAD_VB, category="expression",
             cls="DERIVED_STATE", base="CHR_REMY_PART_HEAD_FACE", mod="rig_remy.py", anchor="RCS head frame",
             pivots=f"neck {R.J['neck']}", compatible=", ".join(k for k, v in PR.POSES.items()
                                                                 if preset in v["compatible"]),
             usage="Head swap / expression switch", prov=PROV_REMY)
    return comps


def remy_hands():
    for shape in R.HANDS:
        aid = f"CHR_REMY_HAND_{shape.upper()}"
        front = shape in ("grip_front", "pen_front")
        emit("characters/main/hands", aid, R.HANDS[shape](), (-20, -60, 120, 110), category="hand",
             cls="AUTHORED_BASE", base=aid, mod="rig_remy.py",
             anchor="Wrist at (0,0); fingers point +x; thumb toward -y",
             pivots="wrist (0,0); attach = translate(wrist) rotate(90) [scale(1,-1) when flip]",
             occlusion=("Draw ABOVE held prop (thumb in front)" if front else
                        "Draw BELOW held prop (fingers behind)" if shape in ("grip_back", "pen_back") else
                        "Under the wrist cuff"),
             compatible=", ".join(k for k, v in PR.POSES.items() if shape in (v["pose"].get("hand_n"),
                                                                          v["pose"].get("hand_f"))) or "-",
             usage="Hand swaps at the wrist", density=288, prov=PROV_REMY,
             qa_notes="Recolour via skin tokens for the associate (derived)")


def resolve(pose):
    p = {**R.DEFAULT_POSE, **pose}
    out = {k: p[k] for k in ("body_dy", "lean", "neck", "head_flip", "hand_n", "hand_f", "flip_n", "flip_f")}
    for side in ("n", "f"):
        arm = p[f"arm_{side}"]
        a = R.ik(side, arm) if isinstance(arm, dict) else arm
        out[f"arm_{side}_deg"] = {"shoulder": round(a[0], 2), "elbow": round(a[1], 2), "wrist": round(a[2], 2)}
        hip, knee, ank = p[f"leg_{side}"]
        out[f"leg_{side}_deg"] = {"hip": hip, "knee": knee, "ankle": ank}
    out["expression"] = p["expr"]
    out["slot_overrides"] = p["slots"]
    out["props"] = [{"id": x["id"], "attach": f"hand_{x['hand']}" if x.get("hand") else "upper_body",
                     "translate_rotate_scale": x["at"]} for x in p["props"]]
    return out


def remy_poses():
    lib = {}
    for name, spec in PR.POSES.items():
        aid = f"CHR_REMY_POSE_{name.upper()}"
        emit("characters/main/poses", aid, R.render(spec["pose"]), POSE_VB, category="pose", cls="DERIVED_STATE",
             base="CHR_REMY_RIG", mod="rig_remy.py + poses_remy.py",
             anchor="Ground contact (314,1030) in RCS; place with scenes.char_tf()",
             pivots="see remy_rig.json joints", layers=None,
             occlusion="Slots back->front: " + " > ".join(R.SLOTS),
             compatible="expressions: " + ", ".join(spec["compatible"]), usage=spec["use"], prov=PROV_REMY)
        lib[name] = {"asset_id": aid, "use": spec["use"], "compatible_expressions": spec["compatible"],
                     **resolve(spec["pose"])}
    return lib


# ---------------------------------------------------------------- associate ------------------
def associate():
    emit("characters/supporting", "CHR_ASSOC_PART_HEAD", A.head({"preset": "content"}), (200, 20, 240, 300),
         category="character_part", cls="AUTHORED_BASE", base="CHR_ASSOC_PART_HEAD", mod="rig_associate.py",
         anchor="RCS head frame", pivots=f"neck {R.J['neck']}", usage="B2 only")
    emit("characters/supporting", "CHR_ASSOC_PART_TORSO", A.torso(), RCS_VB, category="character_part",
         cls="AUTHORED_BASE", base="CHR_ASSOC_PART_TORSO", mod="rig_associate.py", anchor="RCS rest frame",
         pivots=f"hip_c {R.J['hip_c']}", usage="B2 only", qa_notes="Apron badge intentionally blank (no name/brand)")
    for name in ("content", "happy", "neutral"):
        emit("characters/supporting", f"CHR_ASSOC_EXPR_{name.upper()}", A.head({"preset": name}),
             (200, 20, 240, 300), category="expression", cls="DERIVED_STATE", base="CHR_ASSOC_PART_HEAD",
             mod="rig_associate.py", anchor="RCS head frame", usage="B2")
    lib = {}
    for name, spec in A.POSES.items():
        aid = f"CHR_ASSOC_POSE_{name.upper()}"
        emit("characters/supporting", aid, A.render(spec["pose"]), POSE_VB, category="pose", cls="DERIVED_STATE",
             base="CHR_ASSOC_RIG", mod="rig_associate.py", anchor="Ground contact (314,1030); mirror to face left",
             compatible="expressions: " + ", ".join(spec["compatible"]), usage=spec["use"],
             qa_notes="Shares Remy skeleton/limb/hand system, recoloured; distinct head, glasses, bun, apron")
        lib[name] = {"asset_id": aid, "use": spec["use"], **resolve(spec["pose"])}
    return lib


# ---------------------------------------------------------------- props ----------------------
PROPS = [
    ("PRP_STORE_CARD", P.store_card, (-110, -80, 220, 160), "centre", "C03", "F2"),
    ("PRP_OFFER_SHEET", P.offer_sheet, (-180, -230, 360, 460), "centre; text groups offer_headline/offer_if/offer_condition", "C03", "F2;F4"),
    ("PRP_STATEMENT_EMPTY", lambda: P.statement("empty"), (-180, -235, 360, 470), "centre", "C05 (S04C)", "F3"),
    ("PRP_STATEMENT_CHARGED", lambda: P.statement("charged"), (-180, -235, 360, 470), "centre", "C01B, C07B", "F1;F5"),
    ("PRP_PEN", P.pen, (-30, -100, 60, 190), "centre; tip at +y", "C10", ""),
    ("PRP_MARKER", P.marker, (-30, -100, 60, 190), "centre; tip at +y", "C12", ""),
    ("PRP_COIN", P.coin, (-55, -55, 110, 110), "centre", "C06A", "F4"),
    ("PRP_SOFA", P.sofa, (-360, -340, 720, 360), "floor centre (0,0)", "C02, C13, C14", "F2;F10"),
    ("PRP_SOFA_ICON", P.sofa_icon, (-70, -50, 140, 80), "centre", "C05, C09", "F6"),
    ("PRP_PROMO_SIGN", lambda: P.promo_sign("NO", "INTEREST?"), (-230, -20, 460, 340), "top centre of strings (swing pivot)", "C01A, C01B", "F1"),
    ("PRP_PROMO_SIGN_STORE", lambda: P.promo_sign("NO", "INTEREST"), (-230, -20, 460, 340), "top centre of strings", "C02", "F2"),
    ("PRP_PRICE_TAG", P.price_tag, (-50, -70, 100, 200), "string top (swing pivot)", "C02", ""),
    ("PRP_CARD_TERMINAL", P.card_terminal, (-100, -125, 200, 250), "centre", "C03", ""),
    ("PRP_IF_SWITCH_UP", lambda: P.if_switch("up"), (-170, -250, 340, 500), "centre; lever group if_switch_lever_up", "C04", "F2;F4"),
    ("PRP_IF_SWITCH_DOWN", lambda: P.if_switch("down"), (-170, -250, 340, 500), "centre; lever group if_switch_lever_down", "C04 alt / S06A wipe", "F5"),
    ("PRP_CALENDAR_PAGE_PROMO_ENDS", lambda: P.calendar_page("PROMO ENDS", mark="circle", header=C["coral"]), (-140, -165, 280, 310), "centre", "C07A, C12", "F9"),
    ("PRP_CALENDAR_PAGE_PAYMENT_DUE", lambda: P.calendar_page("PAYMENT DUE", header=C["slate"], text=C["paper"]), (-140, -165, 280, 310), "centre", "C12", "F9"),
    ("PRP_MONTH_STRIP", P.month_strip, (-10, -45, 790, 90), "left edge centre; child groups month_01..12", "C05, C06A/B", "F2"),
    ("PRP_DEADLINE_FLAG", P.deadline_flag, (-40, -210, 260, 230), "pole base (0,0)", "C06A, C10", "F4;F9"),
    ("PRP_CLOCK_FACE", P.clock_face, (-165, -165, 330, 330), "centre = hand pivot", "C14", "F10"),
    ("PRP_CLOCK_HAND_MINUTE", lambda: P.clock_hand("minute"), (-20, -120, 40, 140), "pivot (0,0); 12 o'clock at 0deg", "C14", "F10"),
    ("PRP_CLOCK_HAND_HOUR", lambda: P.clock_hand("hour"), (-20, -80, 40, 100), "pivot (0,0)", "C14", "F10"),
    ("PRP_REWIND_ARROW", P.rewind_arrow, (-10, -120, 200, 270), "local origin", "C11", "F8"),
    ("PRP_RECEIPT_CLIP", P.receipt_clip, (-130, -30, 260, 80), "centre", "C05", "F3"),
    ("PRP_MAGNIFIER", P.magnifier, (-95, -95, 230, 230), "lens centre", "C08", "F6"),
    ("PRP_CHECK_BOX_ON", lambda: P.check_box(True, label=None), (-45, -45, 90, 90), "centre", "C10", "F7"),
    ("PRP_CHECK_BOX_OFF", lambda: P.check_box(False, label=None), (-45, -45, 90, 90), "centre", "C10", "F7"),
    ("PRP_STAMP_WAIVED", P.waived_stamp, (-215, -110, 430, 220), "centre (hit pivot)", "C06B, fork", "F4"),
    ("PRP_STAMP_CHARGED", P.charged_stamp, (-225, -110, 450, 220), "centre (hit pivot)", "C07B, fork, compare", "F5;F8"),
]
for n in (0, 1, 3, 6, 12):
    PROPS.append((f"PRP_RECEIPT_ROWS_{n:02d}", (lambda n=n: P.interest_receipt(n, header="DEFERRED INTEREST" if n else "INTEREST")),
                  (-170, -10, 340, 112 + n * 34 + 16), "top centre (print-from point)", "C05-C14", "F3;F10"))
for lvl, rem in ((1.0, False), (0.75, False), (0.45, False), (0.25, False), (0.0, False), (0.3, True)):
    PROPS.append((f"PRP_BALANCE_CARD_{int(lvl * 100):03d}" + ("_REMAINDER" if rem else ""),
                  (lambda lvl=lvl, rem=rem: P.balance_card(lvl, remainder=rem)), (-190, -120, 380, 240),
                  "centre; fill group balance_fill grows from x=-146", "C05-C10", "F4;F5;F7"))


def props():
    bases = {}
    for aid, fn, vb, anchor, usage, facts in PROPS:
        base = re.sub(r"_(EMPTY|CHARGED|UP|DOWN|ROWS_\d+|\d{3}(_REMAINDER)?|ON|OFF|STORE|MINUTE|HOUR|PROMO_ENDS|PAYMENT_DUE)$",
                      "", aid)
        cls = "DERIVED_STATE" if base in bases else "AUTHORED_BASE"
        bases[base] = True
        emit("props", aid, fn(), vb, category="prop", cls=cls, base=base, mod="props.py", anchor=anchor,
             usage=usage, facts=facts, density=144,
             occlusion="Held props sit between hand *_back and hand *_front layers" if aid in (
                 "PRP_OFFER_SHEET", "PRP_STATEMENT_CHARGED", "PRP_STORE_CARD", "PRP_PEN", "PRP_MARKER") else "",
             qa_notes="Schematic: no amounts, rates or dates" if any(k in aid for k in (
                 "STATEMENT", "RECEIPT", "BALANCE", "OFFER", "CALENDAR")) else "")
    for k, v in P.sofa_layers().items():
        emit("props/sofa_layers", f"PRP_SOFA_L_{k.upper()}", v, (-360, -340, 720, 360), category="prop_layer",
             cls="DERIVED_EXPORT", base="PRP_SOFA", mod="props.py", anchor="floor centre (0,0)",
             occlusion="Seated character goes between 'seat' and arm layers",
             usage="C02, C13, C14", density=72)


# ---------------------------------------------------------------- env / diagrams / type -----
def environments():
    for kit, fn in E.KITS.items():
        aid = kit.upper()
        layers = fn()
        emit("environments", aid, E.compose(kit), (0, 0, 1080, 1920), category="environment", cls="AUTHORED_BASE",
             base=aid, mod="env.py", anchor="frame (0,0)", layers=list(layers), density=72,
             occlusion="Characters go between mid and fg layers", usage=E.KITS[kit].__doc__.strip())
        for k, v in layers.items():
            emit("environments/layers", f"{aid}_L_{k.upper()}", v, (0, 0, 1080, 1920), category="environment_layer",
                 cls="DERIVED_EXPORT", base=aid, mod="env.py", anchor="frame (0,0)", density=36,
                 usage=f"Layer of {aid}")
    emit("environments", "ENV_PAPER_MACRO", paper_macro(), (0, 0, 1080, 1920), category="environment",
         cls="AUTHORED_BASE", base="ENV_PAPER_MACRO", mod="build_assets.py", anchor="frame (0,0)", density=36,
         usage="C04 macro background (the offer paper, magnified)")


def paper_macro():
    return (f'<rect width="1080" height="1920" fill="{C["paper"]}"/>'
            + "".join(f'<path d="M0 {y} H1080" stroke="{C["paper_dk"]}" stroke-width="4"/>' for y in range(140, 1920, 64)))


def diagrams():
    stage = E.compose("env_stage")
    for name, fn in D.DIAGRAMS.items():
        aid = name.upper()
        layers = fn()
        emit("diagrams", aid, "".join(f'<g id="{k}">{v}</g>' for k, v in layers.items()), (0, 0, 1080, 1920),
             category="diagram", cls="AUTHORED_BASE", base=aid, mod="diagrams.py", anchor="frame (0,0)",
             layers=list(layers), png=False, usage=fn.__doc__.strip(),
             facts=re.findall(r"F\d+", fn.__doc__ or "") and ";".join(re.findall(r"F\d+", fn.__doc__)) or "",
             qa_notes="Schematic only; reveal in listed layer order")
        prev = ROOT / "diagrams" / f"{aid}__preview_on_stage.svg"
        prev.write_text(doc(stage + "".join(layers.values()), (0, 0, 1080, 1920), aid + " preview"))
        jobs.append({"svg": str(prev), "png": str(prev.with_suffix(".png")), "density": 36})
        records[-1]["png"] = str(prev.with_suffix(".png").relative_to(ROOT))
        for k, v in layers.items():
            emit("diagrams/layers", f"{aid}_L_{k.upper()}", v, (0, 0, 1080, 1920), category="diagram_layer",
                 cls="DERIVED_EXPORT", base=aid, mod="diagrams.py", anchor="frame (0,0)", png=False,
                 usage=f"Layer of {aid}")


def typography(scene_defs):
    emit("typography", "TYP_CAPTION_PLATE", TY.caption_plate(("Caption phrase", "second line")),
         (0, 1280, 1080, 300), category="typography", cls="AUTHORED_BASE", base="TYP_CAPTION_PLATE",
         mod="typography.py", anchor="centre (540,1430); live text", usage="All shots (procedural captions)")
    emit("typography", "TYP_QUALIFIER_STRIP", TY.qualifier("Illustrative offer • U.S. store card", cy=60),
         (0, 0, 1080, 120), category="typography", cls="AUTHORED_BASE", base="TYP_QUALIFIER_STRIP",
         mod="typography.py", anchor="centre; live text", usage="C02, C03, C14 + per-shot qualifiers")
    emit("typography", "TYP_HEADLINE", TY.headline(["NO", "INTEREST?"], top=170, size=130), (0, 0, 1080, 360),
         category="typography", cls="AUTHORED_BASE", base="TYP_HEADLINE", mod="typography.py",
         anchor="centre-top; live text", usage="Optional title card / end card")
    seen = set()
    for sc in scene_defs.values():
        for iid, aid, svg, tf, _ in sc.get("ui", []) + sc["world"]:
            if aid.startswith("TYP_LABEL_") and aid not in seen:
                seen.add(aid)
                emit("typography/labels", aid, f'<g transform="translate(540 60)">{svg}</g>', (0, 0, 1080, 120),
                     category="typography", cls="DERIVED_STATE", base="PRP_LABEL_PILL", mod="props.py",
                     anchor="centre (540,60); live text", usage="Scene labels")


# ---------------------------------------------------------------- scenes & map ---------------
def scenes_and_map():
    S = SC.scenes()
    layouts = {}
    for name, sc in S.items():
        aid = f"SCN_{name}"
        emit("custom_scenes", aid, SC.render_scene(sc), (0, 0, 1080, 1920), category="scene_composition",
             cls="COMPOSITION", base=aid, mod="scenes.py", anchor="frame (0,0); camera group 'camera'",
             layers=[i[0] for i in sc["world"]], usage=", ".join(sc["shots"]), density=72,
             qa_notes=sc["note"])
        lay = SC.layout(name, sc)
        (ROOT / "custom_scenes" / f"{aid}.layout.json").write_text(json.dumps(lay, indent=1, ensure_ascii=False))
        layouts[name] = lay
    return S, layouts


def timing_and_map(S, layouts):
    al = json.loads((ROOT / "AUDIO_ALIGNMENT.json").read_text())
    ph, fps = al["phrases"], al["fps"]
    dur = al["source_audio"]["decoded_duration_s"]
    end_hold = 8
    rows, cap = [], []
    for i, shot in enumerate(SH.SHOTS):
        sid, beat, scene = shot[0], shot[1], shot[2]
        start = 0.0 if i == 0 else (ph[i - 1]["end_s"] + ph[i]["start_s"]) / 2
        end = dur + end_hold / fps if i == len(SH.SHOTS) - 1 else (ph[i]["end_s"] + ph[i + 1]["start_s"]) / 2
        lay = layouts[scene]
        assets = sorted({w["asset_id"] for w in lay["world"]} | {u["asset_id"] for u in lay["ui"]})
        persistent = [w["asset_id"] for w in lay["world"] if w["asset_id"].startswith(("ENV_", "PRP_SOFA_L"))]
        rows.append({
            "beat": beat, "shot_id": sid, "scene_id": f"SCN_{scene}",
            "start_s": round(start, 3), "end_s": round(end, 3),
            "start_frame": round(start * fps), "end_frame_excl": round(end * fps),
            "narration_start_s": ph[i]["start_s"], "narration_end_s": ph[i]["end_s"],
            "timing_status": "PROVISIONAL_PENDING_CORRECTED_MP3",
            "narration": ph[i]["text"], "viewer_understanding": shot[3], "composition": shot[4],
            "remy_pose_expression": shot[5], "supporting_characters": shot[6], "fg_mg_bg": shot[7],
            "persistent_components": ";".join(sorted(set(persistent))) or "-",
            "enter_exit": shot[8], "animation_method": shot[9],
            "independent_layers": ";".join(w["instance"] for w in lay["world"][-6:]),
            "asset_ids": ";".join(assets),
            "reuse_vs_new": "reuses library instances; scene layout authored for this shot" if i else
                            "opening layout authored; sign + rig reused later",
            "transition_in": shot[10], "fact_ids": shot[11], "onscreen_qualifier": shot[12]})
        words = [w for w in al["words"] if w["phrase_index"] == i]
        chunk = []
        for w in words:
            chunk.append(w)
            text = " ".join(x["display"] for x in chunk)
            left = len(words) - words.index(w) - 1
            if w is words[-1] or ((len(chunk) >= 4 or len(text) >= 20 or re.search(r"[,:]\W*$", w["display"]))
                                  and left != 1):
                cap.append({"shot_id": sid, "text": text.replace("“", "").replace("”", ""),
                            "start_s": chunk[0]["start_s"], "end_s": chunk[-1]["end_s"],
                            "start_frame": chunk[0]["start_frame"], "end_frame": chunk[-1]["end_frame"],
                            "timing_status": "PROVISIONAL_ASR_DTW"})
                chunk = []
    with open(ROOT / "SCENE_ASSET_MAP.csv", "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0]))
        wr.writeheader()
        wr.writerows(rows)
    (ROOT / "typography" / "CAPTIONS.json").write_text(json.dumps(
        {"fps": fps, "status": "PROVISIONAL until corrected MP3 is re-aligned",
         "style": "TYP_CAPTION_PLATE, Avenir Next 800, 56px, max 2 lines, centre x=540, y~1430",
         "chunks": cap}, indent=1, ensure_ascii=False))
    return rows, cap


# ---------------------------------------------------------------- contact sheets -------------
def sheet(name, cells, cols, cw, ch, bg="#E9E4DA", title=""):
    rows = (len(cells) + cols - 1) // cols
    W, H = cols * cw, rows * ch + 70
    body = (f'<rect width="{W}" height="{H}" fill="{bg}"/><text x="24" y="46" font-family="Avenir Next" '
            f'font-size="30" font-weight="800" fill="{C["ink"]}">{title}</text>')
    for i, (label, inner, vb) in enumerate(cells):
        x, y = (i % cols) * cw, (i // cols) * ch + 70
        body += (f'<svg x="{x + 6}" y="{y + 4}" width="{cw - 12}" height="{ch - 40}" viewBox="{vb}">{inner}</svg>'
                 f'<text x="{x + cw / 2}" y="{y + ch - 12}" font-family="Avenir Next" font-size="{min(17, int(cw * 1.75 / max(len(label), 1)))}" font-weight="700" '
                 f'text-anchor="middle" fill="{C["ink"]}">{label}</text>')
    path = ROOT / "contact_sheets" / f"{name}.svg"
    path.parent.mkdir(exist_ok=True)
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{body}</svg>')
    jobs.append({"svg": str(path), "png": str(path.with_suffix(".png")), "density": 72})


def contact_sheets(S, rows):
    sheet("remy_pose_sheet", [(k, R.render(v["pose"]), "-160 0 960 1060") for k, v in PR.POSES.items()], 5, 320, 400,
          title="Remy (remy-2) pose library: 19 poses from one rig")
    p1 = ('<g transform="translate(159 42)">' + Path(ROOT.parent / "thumbnail_sources" / "thumbnail_A.svg").read_text()
          .split('<g id="head">')[1].split("</g>")[0] + "</g>")
    p1 = (f'<g stroke="{C["ink"]}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round">{p1}</g>'
          .replace("${C.skin}", C["skin"]))
    cells = [("PHASE 1 reference head", p1, "190 20 260 300")]
    cells += [(e, R.head({"preset": e}), "190 20 260 300") for e in R.EXPRESSIONS]
    sheet("remy_expression_sheet", cells, 4, 260, 330, title="Remy expressions vs Phase 1 head (identity locked)")
    gz = [("gaze centre", (0, 0)), ("gaze right", (5, 0)), ("gaze left", (-5, 0)), ("gaze up", (2, -5)),
          ("gaze down", (2, 5))]
    cells = [(lbl, R.head({"preset": "neutral", "gaze": g}), "190 20 260 300") for lbl, g in gz]
    cells += [("tilt fwd +7", R.render({"neck": 7, "expr": {"preset": "concerned", "gaze": (4, 4)}}), "160 0 340 400"),
              ("tilt back -7", R.render({"neck": -7, "expr": {"preset": "relieved"}}), "160 0 340 400"),
              ("mirrored (faces left)", f'<g transform="translate(640 0) scale(-1 1)">{R.render({"expr": {"preset": "curious"}})}</g>', "140 0 340 400")]
    sheet("remy_gaze_tilt_sheet", cells, 4, 260, 330, title="Gaze directions, head tilts, mirroring")
    hc = []
    for shape in R.HANDS:
        inner = R.HANDS[shape]()
        if shape in R.HAND_FRONT_LAYER:
            inner += R.HANDS[R.HAND_FRONT_LAYER[shape]]()
        hc.append((shape, inner, "-20 -60 120 110"))
    sheet("remy_hands_sheet", hc, 5, 240, 230, title="Hand library (wrist at origin; *_back/*_front sandwich held props)")
    ex = ""
    for pid, slot, m, svg in R.evaluate(REST):
        from geom import svg_matrix
        ex += f'<g transform="{svg_matrix(m)}">{svg}</g>'
    for j, (x, y) in R.J.items():
        ex += (f'<circle cx="{x}" cy="{y}" r="9" fill="{C["coral"]}" stroke="{C["ink"]}" stroke-width="3"/>'
               f'<text x="{x + 12}" y="{y - 10}" font-family="Avenir Next" font-size="16" font-weight="700" fill="{C["ink"]}">{j}</text>')
    sheet("remy_rig_pivots_sheet", [("rest pose + joint pivots (RCS)", ex, "0 0 640 1060")], 1, 700, 1140,
          title="Rig pivots")
    ac = [(k, A.render(v["pose"]), "-160 0 960 1060") for k, v in A.POSES.items()]
    ac += [(e, A.head({"preset": e}), "200 20 240 300") for e in ("content", "happy", "neutral")]
    sheet("associate_sheet", ac, 6, 260, 360, title="Store associate (assoc-1): supporting character, B2 only")
    pc = [(aid, fn(), " ".join(map(str, vb))) for aid, fn, vb, *_ in PROPS]
    sheet("props_sheet", pc, 6, 260, 260, bg="#CFC9BE", title="Props and states")
    sheet("environments_sheet", [(k, E.compose(k), "0 0 1080 1920") for k in E.KITS], 4, 300, 560,
          title="Environment kits")
    stage = E.compose("env_stage")
    sheet("diagrams_sheet", [(k, stage + "".join(f().values()), "0 0 1080 1920") for k, f in D.DIAGRAMS.items()],
          3, 360, 660, title="Layered diagrams (schematic, no values)")
    by_scene = {}
    for r in rows:
        by_scene.setdefault(r["scene_id"], []).append(r)
    cells = []
    for name, sc in S.items():
        rr = by_scene[f"SCN_{name}"]
        lbl = f"{'/'.join(r['shot_id'] for r in rr)}  {rr[0]['start_s']:.1f}-{rr[-1]['end_s']:.1f}s"
        cells.append((lbl, SC.render_scene(sc), "0 0 1080 1920"))
    sheet("storyboard_scenes_sheet", cells, 6, 300, 570, title="Storyboard hero frames (provisional timings)")
    sheet("mobile_scale_check", cells, 8, 180, 360, title="Phone-scale check (~1/6)")


# ---------------------------------------------------------------- QA ----------------------------
def qa():
    texts, issues = [], []
    landmark = R.FACE
    files = [str(ROOT / r["svg"]) for r in records]
    for i in range(0, len(files), 100):  # system libxml2 well-formedness check
        res = subprocess.run(["xmllint", "--noout", *files[i:i + 100]], capture_output=True, text=True)
        for line in res.stderr.splitlines():
            if ".svg:" in line:
                bad = Path(line.split(":")[0]).stem
                issues.append((bad, "XML: " + line.split(":", 2)[-1].strip()))
                for r in records:
                    if r["asset_id"] == bad:
                        r["qa"] = "FAIL"
    for rec in records:
        svg = (ROOT / rec["svg"]).read_text()
        for t in re.findall(r"<text[^>]*>([^<]*)</text>", svg):
            texts.append((rec["asset_id"], t))
            if re.search(r"\$\s?\d|\d+(\.\d+)?\s?%", t) and not t.startswith("TRUE 0%") and "0% period" not in t:
                issues.append((rec["asset_id"], f"numeric money/rate text: {t}"))
        if any(k in rec["asset_id"] for k in ("OFFER", "PROMO_SIGN", "RECEIPT", "LEDGER")) and "0%" in svg:
            issues.append((rec["asset_id"], "deferred-interest asset contains '0%'"))
        if rec["asset_id"].startswith("CHR_REMY_POSE_") and landmark not in svg:
            issues.append((rec["asset_id"], "Remy face landmark path missing"))
        if rec["png"]:
            w, h = png_size(ROOT / rec["png"])
            rec["png_px"] = f"{w}x{h}"
        rec["sha256_svg"] = sha(ROOT / rec["svg"])
        rec["sha256_png"] = sha(ROOT / rec["png"]) if rec["png"] else ""
    with open(ROOT / "qa" / "text_inventory.csv", "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["asset_id", "text"])
        wr.writerows(texts)
    return issues


def main():
    parts = remy_parts()
    comps = remy_faces()
    remy_hands()
    pose_lib = remy_poses()
    assoc_lib = associate()
    props()
    environments()
    diagrams()
    S, layouts = scenes_and_map()
    typography(S)
    rows, cap = timing_and_map(S, layouts)
    contact_sheets(S, rows)
    (ROOT / "qa").mkdir(exist_ok=True)
    jf = ROOT / "qa" / "_render_jobs.json"
    jf.write_text(json.dumps(jobs))
    subprocess.run(["node", str(HERE / "render.mjs"), str(jf)], check=True)
    jf.unlink()
    usage = {}
    for name, lay in layouts.items():
        for w in lay["world"] + lay["ui"]:
            usage.setdefault(w["asset_id"], set()).add(f"SCN_{name}")
    for rec in records:
        if rec["asset_id"] in usage:
            rec["usage"] = (rec["usage"] + " | scenes: " + ", ".join(sorted(usage[rec["asset_id"]]))).strip(" |")
    issues = qa()
    known = {r["asset_id"] for r in records}
    for name, lay in layouts.items():  # every instance in every scene must resolve to a registered asset
        for w in lay["world"] + lay["ui"]:
            if w["asset_id"] not in known:
                issues.append((f"SCN_{name}", f"unregistered asset_id {w['asset_id']}"))
    rig = {"design_version": "remy-2", "frame": {"viewBox": RCS_VB, "ground_y": R.GROUND_Y, "ground_point": [314, 1030]},
           "joints": R.J, "slots_back_to_front": R.SLOTS, "parts": parts,
           "hierarchy": "root -> body_dy -> {legs: hip->knee->ankle} and upper_body(rotate lean @hip_c) -> "
                        "{neck, torso, head(rotate neck @neck), arms: shoulder->elbow->wrist->hand}",
           "transform_rule": "world = parent * translate(pivot) * rotate(angle) * translate(-pivot); all parts "
                             "drawn in one rest frame. Hand: forearm * rotate(wrist @wri) * translate(wri) * "
                             "rotate(90) [* scale(1,-1) if flip].",
           "angle_sign": "SVG degrees, positive = clockwise on screen; lean + = forward (toward screen-right)",
           "suggested_limits_deg": {"lean": [-10, 12], "neck": [-12, 12], "shoulder": [-170, 120], "elbow": [-150, 20],
                                    "wrist": [-60, 60], "hip": [-95, 30], "knee": [0, 100]},
           "hands": list(R.HANDS), "hand_front_layers": R.HAND_FRONT_LAYER,
           "expressions": {k: dict(zip(("eyes", "brows", "mouth", "blush"), v)) for k, v in R.EXPRESSIONS.items()},
           "gaze_rule": "add (dx,dy) to both eye centres; keep within +-6px",
           "face_components": comps, "poses": pose_lib}
    (ROOT / "characters" / "main" / "remy_rig.json").write_text(json.dumps(rig, indent=1))
    (ROOT / "characters" / "supporting" / "associate_rig.json").write_text(json.dumps(
        {"design_version": "assoc-1", "skeleton": "identical to remy-2 joints", "poses": assoc_lib,
         "palette": {"skin": A.SKIN, "hair": A.HAIR, "apron": A.APRON, "shirt": A.SHIRT}}, indent=1))
    (ROOT / "manifests").mkdir(exist_ok=True)
    (ROOT / "manifests" / "asset_manifest.json").write_text(json.dumps(records, indent=1, ensure_ascii=False))
    (ROOT / "manifests" / "scene_layouts.json").write_text(json.dumps(layouts, indent=1, ensure_ascii=False))
    cols = ["asset_id", "category", "class", "base_design", "svg", "png", "png_px", "viewBox", "anchor", "pivots",
            "occlusion", "compatible", "usage", "facts", "qa", "qa_notes", "sha256_svg", "sha256_png", "provenance"]
    with open(ROOT / "ASSET_REGISTER.csv", "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        wr.writeheader()
        for rec in records:
            wr.writerow({**rec, "layers": ";".join(rec["layers"])})
    counts = {}
    for rec in records:
        counts[rec["class"]] = counts.get(rec["class"], 0) + 1
    report = {"records": len(records), "by_class": counts,
              "by_category": {c: sum(1 for r in records if r["category"] == c) for c in sorted({r["category"] for r in records})},
              "png_files": sum(1 for r in records if r["png"]), "issues": issues,
              "shots": len(rows), "caption_chunks": len(cap)}
    (ROOT / "qa" / "automated_qa.json").write_text(json.dumps(report, indent=1, ensure_ascii=False))
    print(json.dumps(report, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
