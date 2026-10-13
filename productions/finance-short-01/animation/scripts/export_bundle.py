"""Export the approved Phase 2 asset library into one JSON bundle for the Remotion project.

Nothing is redrawn here. Markup comes from the same generators in PHASE_2_ASSETS/build/
that produced the registered SVGs, and every registered SVG is copied in verbatim (wrapper
stripped). Scenes are captured from scenes.scenes() so the hero compositions are reproduced
exactly. Character instances carry their full pose dicts, so Remotion can re-evaluate the rig
per frame instead of animating flattened pose renders.

Usage (from productions/finance-short-01/animation):
    python3 scripts/export_bundle.py
Writes src/data/bundle.json and src/data/rig_reference.json (parity fixtures for tests).
"""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ANIM = HERE.parent
ASSETS = ANIM.parent / "experiment" / "PHASE_2_ASSETS"
sys.path.insert(0, str(ASSETS / "build"))

import rig_remy as R  # noqa: E402
import rig_associate as A  # noqa: E402
import poses_remy as PR  # noqa: E402
import scenes as SC  # noqa: E402
from style import C, FONT  # noqa: E402

markup = {}


def key(s):
    k = hashlib.sha256(s.encode()).hexdigest()[:12]
    if markup.setdefault(k, s) != s:
        raise SystemExit(f"markup key collision {k}")
    return k


def inner(svg_text):
    m = re.match(r'<svg [^>]*viewBox="([^"]+)"[^>]*>(?:<title>[^<]*</title>)?(.*)</svg>\s*$', svg_text, re.S)
    if not m:
        raise ValueError("unexpected SVG wrapper")
    return [float(v) for v in m.group(1).split()], m.group(2)


# ---- registered assets (verbatim) ------------------------------------------------------------
manifest = json.loads((ASSETS / "manifests/asset_manifest.json").read_text())
SKIP_CATEGORIES = {"pose", "expression", "scene_composition"}
assets, registered_inner = {}, {}
for rec in manifest:
    vb, body = inner((ASSETS / rec["svg"]).read_text())
    registered_inner[rec["asset_id"]] = body
    if rec["category"] in SKIP_CATEGORIES or rec["asset_id"].startswith("SCN_"):
        continue
    assets[rec["asset_id"]] = {"vb": vb, "m": key(body), "category": rec["category"]}
by_body = {}
for aid, body in registered_inner.items():
    by_body.setdefault(body, aid)


def match_asset(body):
    return by_body.get(body)


# ---- rigs ------------------------------------------------------------------------------------
def head_templates(head_fn):
    """Head markup with placeholders for the parts expressions swap: eyes, brows, mouth."""
    saved_eye = R.eye
    R.eye = lambda c, kind, gx, gy: f"{{{{EYE:{c[0]}:{c[1]}}}}}"
    R.BROWS["__ph"] = ("{{BROW_L}}", "{{BROW_R}}")
    R.MOUTH["__ph"] = lambda: "{{MOUTH}}"
    try:
        out = {}
        for blush in (False, True):
            t = head_fn({"eyes": "__ph", "brows": "__ph", "mouth": "__ph", "blush": blush})
            out["blush" if blush else "plain"] = key(t)
        return out
    finally:
        R.eye = saved_eye
        del R.BROWS["__ph"], R.MOUTH["__ph"]


def rig_export(design, head_fn):
    d = {**R.REMY, **(design or {})}
    parts = {}
    for side in ("f", "n"):
        L = d["leg"](side)
        for k in ("thigh", "shin", "shoe"):
            parts[f"{k}_{side}"] = key(L[k])
        for k in ("upper_arm", "forearm", "cuff"):
            parts[f"{k}_{side}"] = key(d[k](side))
    parts["neck"] = key(d["neck"]())
    parts["torso"] = key(d["torso"]())
    return {"parts": parts,
            "hands": {s: key(d["hand"](s)) for s in R.HANDS},
            "head": head_templates(head_fn)}


def remy_head(expr):
    return R.head(expr)


def assoc_head(expr):
    return A.head({**expr, "preset": "content"})


RIGS = {
    "remy": rig_export(None, remy_head),
    "assoc": rig_export(A.DESIGN, assoc_head),
}
FACE = {
    "brows": R.BROWS,
    "mouths": {k: key(f()) for k, f in R.MOUTH.items()},
    "eye_colors": {"ink": C["ink"], "white": C["white"], "skin": C["skin"]},
    "path_style": {"stroke": C["ink"]},
    "expressions": {k: {"eyes": v[0], "brows": v[1], "mouth": v[2], "blush": v[3]} for k, v in R.EXPRESSIONS.items()},
}


def pose_json(pose):
    p = {**R.DEFAULT_POSE, **pose}
    out = {}
    for k, v in p.items():
        if k == "props":
            out[k] = []
            for pr in v:
                out[k].append({"id": pr.get("id"), "hand": pr.get("hand"), "at": list(pr.get("at", (0, 0, 0, 1))),
                               "slot": pr.get("slot", "prop"), "m": key(pr["svg"]), "asset": match_asset(pr["svg"])})
        elif isinstance(v, tuple):
            out[k] = list(v)
        elif isinstance(v, dict) and "ik" in v:
            out[k] = {**v, "ik": list(v["ik"])}
        elif k == "expr":
            out[k] = {kk: (list(vv) if isinstance(vv, tuple) else vv) for kk, vv in v.items()}
        else:
            out[k] = v
    return out


POSES = {"remy": {n: pose_json(s["pose"]) for n, s in PR.POSES.items()},
         "assoc": {n: pose_json(s["pose"]) for n, s in A.POSES.items()}}
COMPAT = {n: s["compatible"] for n, s in PR.POSES.items()}

# ---- scenes: capture the exact hero compositions ---------------------------------------------
captured = []
_render = R.render


def capture_render(pose, prefix="remy", design=None):
    captured.append({"rig": "assoc" if design is A.DESIGN else "remy", "pose": pose_json(pose)})
    return f"@@CHAR{len(captured) - 1}@@"


R.render = capture_render
try:
    scene_defs = SC.scenes()
finally:
    R.render = _render

variants = []


def inst_json(scene, iid, aid, svg, tf, meta):
    item = {"id": iid, "asset": aid, "tf": tf or None}
    m = re.fullmatch(r"@@CHAR(\d+)@@", svg)
    if m:
        item["char"] = {**captured[int(m.group(1))], **{k: (list(v) if isinstance(v, tuple) else v)
                                                       for k, v in meta.items() if k != "expr"}}
        return item
    if registered_inner.get(aid) == svg:
        item["m"] = None  # identical to the registered asset
    else:
        item["m"] = key(svg)
        variants.append(f"{scene}:{iid} ({aid})")
    return item


SCENES = {}
for name, sc in scene_defs.items():
    sid = f"SCN_{name}"
    SCENES[sid] = {"shots": sc["shots"], "camera": sc.get("camera") or None,
                   "world": [inst_json(sid, *w) for w in sc["world"]],
                   "ui": [inst_json(sid, *u) for u in sc.get("ui", [])]}

# ---- timeline (provisional until the corrected MP3 is aligned) -------------------------------
align = json.loads((ASSETS / "AUDIO_ALIGNMENT.json").read_text())
captions = json.loads((ASSETS / "typography/CAPTIONS.json").read_text())
with open(ASSETS / "SCENE_ASSET_MAP.csv", newline="") as fh:
    rows = list(csv.DictReader(fh))
if len(rows) != len(align["phrases"]):
    raise SystemExit(f"{len(rows)} shots vs {len(align['phrases'])} phrases: shot/phrase mapping is not 1:1")
gate = align["pronunciation_gate"]
TIMELINE = {
    "fps": align["fps"],
    "frames_total": int(rows[-1]["end_frame_excl"]),
    "audio": {"file": "experiment/PHASE_2_ASSETS/audio_analysis/source_audio/"
                      + Path(align["source_audio"]["original_path"]).name,
              "sha256": align["source_audio"]["sha256"],
              "duration_s": align["source_audio"]["decoded_duration_s"]},
    "gate": {"result": gate["result"], "final_sync_allowed": gate["result"].startswith("PASS")},
    "timing_status": rows[0]["timing_status"],
    "shots": [{"id": r["shot_id"], "beat": int(r["beat"]), "scene": r["scene_id"], "phrase": i,
               "from": int(r["start_frame"]), "to": int(r["end_frame_excl"]),
               "narration": r["narration"], "qualifier": r["onscreen_qualifier"], "transition": r["transition_in"]}
              for i, r in enumerate(rows)],
    "phrases": [{"i": i, "text": p["text"], "from": p["start_frame"], "to": p["end_frame"]}
                for i, p in enumerate(align["phrases"])],
    "words": [{"i": w["index"], "text": w["display"], "norm": w["norm"], "phrase": w["phrase_index"],
               "from": w["start_frame"], "to": w["end_frame"]} for w in align["words"]],
    "captions": [{"shot": c["shot_id"], "text": c["text"], "from": c["start_frame"], "to": c["end_frame"]}
                 for c in captions["chunks"]],
}

bundle = {
    "schema": "finance-short-01/remotion-bundle/v1",
    "note": "GENERATED by scripts/export_bundle.py from experiment/PHASE_2_ASSETS. Do not hand-edit.",
    "palette": C, "font": FONT,
    "joints": R.J, "slots": R.SLOTS, "hand_front": R.HAND_FRONT_LAYER, "default_pose": pose_json({}),
    "rigs": RIGS, "face": FACE, "poses": POSES, "pose_compatible_expressions": COMPAT,
    "assets": assets, "scenes": SCENES, "timeline": TIMELINE, "markup": markup,
    "report": {"registered_assets": len(manifest), "assets_exported": len(assets),
               "scene_instances_not_identical_to_registered_file": variants},
}

# ---- parity fixtures: Python is the reference implementation ---------------------------------
ref = {"poses": {}, "eyes": [], "ik": []}
for rig, lib, design in (("remy", PR.POSES, None), ("assoc", A.POSES, A.DESIGN)):
    for name, spec in lib.items():
        ref["poses"][f"{rig}:{name}"] = [[pid, slot, list(m)] for pid, slot, m, _ in R.evaluate(spec["pose"], design)]
for kind in ("open", "wide", "half", "happy", "closed", "squint"):
    for g in ((0, 0), (4, -3), (-6, 6), (5, 2)):
        ref["eyes"].append({"c": list(R.EYE_L), "kind": kind, "g": list(g), "out": R.eye(R.EYE_L, kind, *g)})
for side in ("n", "f"):
    for spec in ({"ik": (668, 386), "hand_dir": -4}, {"ik": (214, 486), "hand_dir": -12, "elbow": "up"},
                 {"ik": (150, 470), "hand_dir": -118}, {"ik": (900, 900)}):
        ref["ik"].append({"side": side, "spec": {**spec, "ik": list(spec["ik"])}, "out": list(R.ik(side, spec))})

out_dir = ANIM / "src" / "data"
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "bundle.json").write_text(json.dumps(bundle, separators=(",", ":"), sort_keys=True))
(out_dir / "rig_reference.json").write_text(json.dumps(ref, separators=(",", ":"), sort_keys=True))
print(json.dumps({"assets": len(assets), "markup_blobs": len(markup), "scenes": len(SCENES),
                  "characters_captured": len(captured), "variants": len(variants),
                  "bundle_bytes": (out_dir / "bundle.json").stat().st_size,
                  "gate": TIMELINE["gate"], "frames_total": TIMELINE["frames_total"]}, indent=1))
for v in variants:
    print("  variant:", v)
