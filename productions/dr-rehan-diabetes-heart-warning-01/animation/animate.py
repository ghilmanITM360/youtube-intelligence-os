#!/usr/bin/env python3
"""Dr. Rehan Short: keyframe compositor over the existing layered asset package.

  python3 animation/animate.py timeline            # cues -> KEYFRAME_TIMELINE.json
  python3 animation/animate.py frames 0 150 300    # QA stills -> animation/qa/
  python3 animation/animate.py render [start end]  # muted provisional MP4 (or a window)
  python3 animation/animate.py sheet               # CONTACT_SHEET.png

Run from the package root. Uses exports/assets/*.png only (never modifies them).
Timing authority: owner MP3 (sha256 in AUDIO_ALIGNMENT.json), word times from local ASR.
"""
import json, subprocess, sys
from functools import lru_cache
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FPS, W, H = 30, 1080, 1920
ROOT = Path(__file__).resolve().parent.parent
ANIM = ROOT / "animation"
TL = ANIM / "KEYFRAME_TIMELINE.json"
OUT = ANIM / "Dr_Rehan_Heart_Warning_PREVIEW_MUTED.mp4"
AUDIO_END = 45.488  # owner MP3 duration (s); preview length follows it

# ---- cues: seconds on the owner MP3 (see AUDIO_ALIGNMENT.json) --------------
# state: (start_s, camera(from,to,focus_xy), wipe_in, {asset: (op, cue_s, extra)})
# TXT bands: list of cue times, one per card band (title, body).
CUES = [
    ("S01-A", 0.00, (1.00, 1.05, (540, 1150)), False,
     {"CH-diabetes-breath-concerned-front": ("CUT", 0.0), "FX-breath": ("POP_IN", 1.14),
      "TXT-hook": ("TEXT", [0.0, 1.66])}),
    ("S01-B", 3.36, (1.05, 1.09, (540, 1150)), False,
     {"PROP-call": ("POP_IN", 3.90), "TXT-hook-care": ("TEXT", [3.36, 4.30])}),
    ("S02-A", 5.70, (1.08, 1.02, (540, 1000)), True,
     {"CH-doctor-stand-neutral-front": ("CUT", 5.70), "TXT-intro": ("TEXT", [5.85, 6.40])}),
    ("S02-B", 7.34, (1.02, 1.07, (540, 1000)), False,
     {"CH-doctor-open-explaining-front": ("POSE_SWITCH", 7.34)}),
    ("S03-A", 9.80, (1.00, 1.06, (520, 1100)), True,
     {"CH-diabetes-breath-concerned-front": ("CUT", 9.80), "TXT-exertion": ("TEXT", [9.85, 11.0])}),
    ("S03-B", 13.16, (1.00, 1.04, (400, 1100)), False,
     {"PROP-chair": ("CUT", 13.16), "CH-diabetes-sit-concerned-front": ("CUT", 13.16),
      "FX-breath": ("POP_IN", 15.88), "FX-caution": ("POP_IN", 17.04),
      "TXT-symptoms": ("TEXT", [13.2, 14.4])}),
    ("S03-C", 17.58, (1.00, 1.04, (540, 900)), False,
     {"PROP-call": ("POP_IN", 17.62), "FX-caution": ("POP_IN", 18.12),
      "TXT-urgent": ("TEXT", [17.62, 18.64])}),
    ("S04-A", 19.38, (1.00, 1.00, (540, 960)), True,
     {"TXT-groups": ("TEXT", [19.45, 20.40])}),
    ("S04-B", 21.80, (1.00, 1.03, (480, 1000)), False,
     {"CH-diabetes-hold-neutral-front": ("POP_IN", 21.80), "PROP-glucose-kit": ("POP_IN", 22.50),
      "TXT-diabetes": ("TEXT", [21.85, 22.80])}),
    ("S05-A", 23.40, (1.00, 1.02, (540, 1000)), False,
     {"CH-older-man-stand-neutral-front": ("SLIDE_IN", 23.40, -90),
      "TXT-older": ("TEXT", [23.45, 24.40])}),
    ("S05-B", 25.10, (1.02, 1.04, (540, 1000)), False,
     {"CH-older-woman-stand-neutral-front": ("SLIDE_IN", 25.10, 90)}),
    ("S06-A", 26.38, (1.00, 1.02, (540, 1000)), False,
     {"CH-risk-adult-stand-neutral-front": ("POP_IN", 26.38), "PROP-pressure-cuff": ("POP_IN", 27.74),
      "TXT-comorbid": ("TEXT", [26.42, 27.10])}),
    ("S06-B", 28.14, (1.02, 1.04, (540, 1000)), False,
     {"CH-risk-adult-open-neutral-front": ("POSE_SWITCH", 28.14),
      "PROP-pressure-cuff": ("TRANSLATE", 28.14, ("S06-A",)), "PROP-lab-tube": ("POP_IN", 28.70)}),
    ("S07-A", 29.96, (1.00, 1.05, (540, 840)), True,
     {"MED-heart-anterior": ("POP_IN", 30.00), "MED-coronary-overlay": ("DIAGRAM_BUILD", 30.60, "down"),
      "TXT-heart": ("TEXT", [30.05, 31.30])}),
    ("S07-B", 32.66, (1.00, 1.03, (540, 860)), False,
     {"MED-artery-wall": ("POP_IN", 32.66), "MED-plaque": ("DIAGRAM_BUILD", 33.26, "up"),
      "MED-flow": ("DIAGRAM_BUILD", 33.86, "right"), "TXT-artery": ("TEXT", [32.70, 34.20])}),
    ("S07-C", 35.44, (1.06, 1.00, (540, 1200)), True,
     {"CH-doctor-point-explaining-three-quarter": ("CUT", 35.44),
      "CH-diabetes-stand-neutral-front": ("CUT", 35.44), "PROP-assessment": ("POP_IN", 36.10),
      "TXT-assessment": ("TEXT", [35.50, 36.60])}),
    ("S07-D", 38.60, (1.00, 1.06, (540, 900)), True,
     {"PROP-call": ("POP_IN", 38.66), "FX-caution": ("POP_IN", 39.10),
      "TXT-emergency": ("TEXT", [38.70, 39.50])}),
]
EXCLUDED = ["S08-HOLD"]  # editorial placeholder; never in any render
F = lambda s: round(s * FPS)


def bands(png):
    """Vertical runs of opaque rows in a full-canvas text layer (title card, body card)."""
    a = Image.open(ROOT / png).getchannel("A").point(lambda v: 255 if v > 8 else 0)
    rows = [a.crop((0, y, W, y + 1)).getbbox() is not None for y in range(H)]
    runs, y = [], 0
    while y < H:
        if rows[y]:
            y0 = y
            while y < H and rows[y]: y += 1
            if runs and y0 - runs[-1][1] < 24: runs[-1][1] = y
            else: runs.append([y0, y])
        y += 1
    return runs


def keys_for(op, f0, extra, layer, prev_layers):
    if op in ("CUT", "POSE_SWITCH"):
        return [{"f": f0, "opacity": 1, "step": True}]
    if op == "POP_IN":
        return [{"f": f0, "opacity": 0, "s": 0.9}, {"f": f0 + 6, "opacity": 1, "s": 1.04},
                {"f": f0 + 9, "s": 1.0}]
    if op == "SLIDE_IN":
        return [{"f": f0, "opacity": 0, "dx": extra}, {"f": f0 + 12, "opacity": 1, "dx": 0}]
    if op == "DIAGRAM_BUILD":
        return [{"f": f0, "reveal": 0, "dir": extra}, {"f": f0 + 18, "reveal": 1}]
    if op == "TRANSLATE":  # continue from the same asset's position in an earlier state
        p = prev_layers[extra[0]][layer["asset_id"]]
        return [{"f": f0, "dx": p["x"] - layer["x"], "dy": p["y"] - layer["y"], "s": p["scale"] / layer["scale"]},
                {"f": f0 + 18, "dx": 0, "dy": 0, "s": 1}]
    raise ValueError(op)


def build_timeline():
    handoff = json.loads((ROOT / "KEYFRAME_HANDOFF.json").read_text())
    states = {s["state_id"]: s for s in handoff["states"]}
    prev_layers = {sid: {l["asset_id"]: l for l in s["layers"]} for sid, s in states.items()}
    ends = [c[1] for c in CUES[1:]] + [AUDIO_END]
    out = []
    for (sid, t0, cam, wipe, cues), t1 in zip(CUES, ends):
        f0, f1 = F(t0), F(t1)
        scene = sid.split("-")[0]
        prev_sid = out[-1]["state_id"] if out else None
        same_scene = prev_sid and prev_sid.split("-")[0] == scene
        layers = []
        for l in states[sid]["layers"]:
            a = l["asset_id"]
            entry = {k: l[k] for k in ("asset_id", "png", "x", "y", "scale", "z", "anchor_local", "layer_id")}
            entry["world"] = not a.startswith("TXT-")
            c = cues.get(a)
            if a.startswith("TXT-"):
                bs = bands(l["png"])
                if c is None:  # carried over from previous state of same scene: already revealed
                    entry["bands"] = [{"y": b, "keys": [{"f": f0, "reveal": 1, "step": True}]} for b in bs]
                else:
                    ts = c[1] + [c[1][-1]] * (len(bs) - len(c[1]))
                    entry["bands"] = [{"y": b, "keys": [{"f": F(t), "reveal": 0, "dy": 24},
                                                         {"f": F(t) + 12, "reveal": 1, "dy": 0}]}
                                      for b, t in zip(bs, ts)]
                entry["op"] = "TEXT_REVEAL" if c else "HOLD"
            elif c is None:  # backgrounds / layers persisting from the previous state
                entry["op"] = "HOLD"
                entry["keys"] = [{"f": f0, "opacity": 1, "step": True}]
            else:
                entry["op"] = c[0]
                entry["keys"] = keys_for(c[0], F(c[1]), c[2] if len(c) > 2 else None, l, prev_layers)
            layers.append(entry)
        out.append({"state_id": sid, "scene_id": scene, "start_f": f0, "end_f": f1,
                    "start_s": t0, "end_s": round(t1, 3),
                    "transition_in": "WIPE_8F" if wipe else ("CONTINUE" if same_scene else "CUT"),
                    "camera": {"op": "CAMERA_PUSH", "from": cam[0], "to": cam[1], "focus": cam[2],
                               "ease": "inOutSine", "applies_to": "world layers only; text cards fixed"},
                    "layers": layers})
    tl = {"schema": "dr-rehan-keyframe-timeline/1", "fps": FPS, "canvas": [W, H],
          "duration_f": F(AUDIO_END), "duration_s": AUDIO_END,
          "timing_source": "owner MP3 1015.mp3 — see AUDIO_ALIGNMENT.json",
          "status": "PROVISIONAL_PREVIEW — script, credit and clinical approval pending; muted",
          "excluded_states": EXCLUDED,
          "interpolation": "linear keys eased outCubic; 'step' keys hold; scale pivots on anchor_local",
          "states": out}
    TL.write_text(json.dumps(tl, indent=1))
    print(f"wrote {TL.relative_to(ROOT)}: {len(out)} states, {tl['duration_f']} frames")


# ---- renderer ---------------------------------------------------------------
ease = lambda t: 1 - (1 - t) ** 3
inout = lambda t: 0.5 - 0.5 * __import__("math").cos(3.14159265 * t)


def sample(keys, f, prop, default):
    ks = [k for k in keys if prop in k]
    if not ks or f < ks[0]["f"]:
        return None if prop == "opacity" else default
    for a, b in zip(ks, ks[1:]):
        if a["f"] <= f < b["f"]:
            if b.get("step"): return a[prop]
            t = ease((f - a["f"]) / (b["f"] - a["f"]))
            return a[prop] + (b[prop] - a[prop]) * t
    return ks[-1][prop]


@lru_cache(maxsize=64)
def img(png):
    return Image.open(ROOT / png).convert("RGBA")


@lru_cache(maxsize=128)
def scaled(png, s):
    im = img(png)
    return im if abs(s - 1) < 1e-4 else im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)


def place(canvas, L, f):
    keys = L["keys"]
    if f < keys[0]["f"]: return
    op = sample(keys, f, "opacity", 1)
    op = 1 if op is None else op
    if op <= 0: return
    s = L["scale"] * sample(keys, f, "s", 1)
    dx, dy = sample(keys, f, "dx", 0), sample(keys, f, "dy", 0)
    ax, ay = L["anchor_local"]
    im = scaled(L["png"], round(s, 3))
    # pivot on anchor: anchor stays at (x + scale*ax, y + scale*ay)
    px = L["x"] + L["scale"] * ax - im.width * ax / img(L["png"]).width + dx
    py = L["y"] + L["scale"] * ay - im.height * ay / img(L["png"]).height + dy
    rev = sample(keys, f, "reveal", 1)
    if rev < 1:
        d = next((k["dir"] for k in keys if "dir" in k), "right")
        im = im.copy(); a = im.getchannel("A"); m = Image.new("L", im.size, 0); w, h = im.size
        box = {"right": (0, 0, int(w * rev), h), "down": (0, 0, w, int(h * rev)),
               "up": (0, int(h * (1 - rev)), w, h)}[d]
        m.paste(255, box); im.putalpha(Image.composite(a, m, m))
    if op < 1:
        im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * op)))
    canvas.alpha_composite(im, (round(px), round(py)))


def place_text(canvas, L, f):
    full = img(L["png"])
    for b in L["bands"]:
        r = sample(b["keys"], f, "reveal", 1)
        if f < b["keys"][0]["f"] or r <= 0: continue
        y0, y1 = b["y"]
        band = full.crop((0, y0, W, y1))
        if r < 1:  # left-to-right type-on wipe with a short fade
            m = Image.new("L", band.size, 0); m.paste(255, (0, 0, int(W * min(1, r * 1.15)), y1 - y0))
            band = band.copy(); band.putalpha(Image.composite(band.getchannel("A"), m, m).point(lambda v: int(v * min(1, r * 2))))
        canvas.alpha_composite(band, (0, round(y0 + sample(b["keys"], f, "dy", 0))))


FONT = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 30)


def stamp(canvas):
    d = ImageDraw.Draw(canvas)
    d.rectangle((0, H - 70, W, H), fill=(24, 40, 44, 255))
    d.text((W // 2, H - 35), "PROVISIONAL PREVIEW · MUTED · NOT FOR PUBLICATION", font=FONT,
           fill=(245, 236, 220), anchor="mm")


def state_at(tl, f):
    for s in tl["states"]:
        if s["start_f"] <= f < s["end_f"]: return s
    return tl["states"][-1]


def render_state(s, f):
    world = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    layers = sorted(s["layers"], key=lambda l: l["z"])
    for L in layers:
        if L["world"]: place(world, L, f)
    c = s["camera"]; t = inout(min(1, (f - s["start_f"]) / max(1, s["end_f"] - s["start_f"] - 1)))
    z = c["from"] + (c["to"] - c["from"]) * t
    if abs(z - 1) > 1e-3:
        fx, fy = c["focus"]; cw, ch = W / z, H / z
        x0 = min(max(fx - cw / 2, 0), W - cw); y0 = min(max(fy - ch / 2, 0), H - ch)
        world = world.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))
    for L in layers:
        if not L["world"]: place_text(world, L, f)
    return world


def frame(tl, f):
    s = state_at(tl, f)
    im = render_state(s, f)
    k = f - s["start_f"]
    if s["transition_in"] == "WIPE_8F" and k < 8 and s["start_f"] > 0:
        prev = tl["states"][tl["states"].index(s) - 1]
        old = render_state(prev, s["start_f"] - 1)
        edge = int(W * ease((k + 1) / 8))
        old.paste(im.crop((0, 0, edge, H)), (0, 0)); im = old
    stamp(im)
    return im.convert("RGB")


def render(a=None, b=None):
    tl = json.loads(TL.read_text())
    a, b = a or 0, b or tl["duration_f"]
    out = OUT if (a, b) == (0, tl["duration_f"]) else ANIM / "qa" / f"window_{a}_{b}.mp4"
    out.parent.mkdir(exist_ok=True)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264",
                          "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                          "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)
    for f in range(a, b):
        p.stdin.write(frame(tl, f).tobytes())
    p.stdin.close(); p.wait()
    print(out.relative_to(ROOT))


def stills(fs):
    tl = json.loads(TL.read_text()); (ANIM / "qa").mkdir(exist_ok=True)
    for f in fs:
        frame(tl, f).save(ANIM / "qa" / f"f{f:04d}.png")


def sheet():
    tl = json.loads(TL.read_text())
    fs = [s["end_f"] - 2 for s in tl["states"]]
    tw, th, cols = 270, 480, 6
    rows = -(-len(fs) // cols)
    m = Image.new("RGB", (tw * cols, (th + 40) * rows), "white"); d = ImageDraw.Draw(m)
    small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
    for i, (f, s) in enumerate(zip(fs, tl["states"])):
        x, y = (i % cols) * tw, (i // cols) * (th + 40)
        m.paste(frame(tl, f).resize((tw, th)), (x, y))
        d.text((x + 6, y + th + 8), f"{s['state_id']}  {s['start_s']:.2f}-{s['end_s']:.2f}s", font=small, fill="black")
    m.save(ANIM / "CONTACT_SHEET.png")


if __name__ == "__main__":
    cmd, *args = sys.argv[1:] or ["timeline"]
    {"timeline": lambda: build_timeline(),
     "frames": lambda: stills([int(x) for x in args]),
     "render": lambda: render(*[int(x) for x in args]),
     "sheet": lambda: sheet()}[cmd]()
