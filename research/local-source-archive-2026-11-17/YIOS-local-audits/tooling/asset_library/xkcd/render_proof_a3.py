#!/usr/bin/env python3
"""Silent proof renderer: timeline (attempt 3: short_q pop + MELT_DRIPS/STEAM_WISPS states) -> per-layout MP4 + pre-encode checks (frames rendered in memory, piped to ffmpeg).
usage: <venv python> -I render_proof.py <timeline.json> <out_dir>
Writes <out_dir>/proof_<layout>.mp4, keyframes_<layout>.png (contact sheet for human review), preencode_<layout>.json."""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

T = json.load(open(sys.argv[1])); OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
EV = {e["target"]: e for e in T["events"]}

def render_layout(name, L):
    W, Hh = L["size"]; s = min(W, Hh) / 1000; S = lambda v: int(round(v * s))
    sw = max(1, round(T["stroke_px_at_1080"] * min(W, Hh) / 1080))
    font = lambda px: ImageFont.truetype(T["font"], S(px))
    ink, red, bg = T["ink"], T["red"], T["canvas"]
    def P(x, y): return (S(x) if W >= Hh else S(x), S(y))  # design units are min-side based

    boxes = {}  # element -> pixel bbox at the frame being drawn (clip/overlap check)
    def reg(k, b): boxes[k] = tuple(int(v) for v in b)

    def base_rig(f):
        im = Image.new("RGB", (W, Hh), bg); d = ImageDraw.Draw(im)
        if L["card"] and f >= EV["card_text"]["f"]:  # question card (own style: white card, thin border, left Q marker)
            x0, y0, x1, y1 = L["card"]; d.rectangle([*P(x0, y0), *P(x1, y1)], outline=ink, width=max(2, sw // 3), fill="#FFFFFF")
            n = min(len(T["question"]), f - EV["card_text"]["f"] + 1)
            d.text(P(x0 + 30, y0 + 40), T["question"][:n], font=font(48), fill=ink)
            reg("card", (*P(x0, y0), *P(x1, y1))); reg("card_text", d.textbbox(P(x0 + 30, y0 + 40), T["question"], font=font(48)))
        x0, y0, x1, y1 = L["board"]; d.rectangle([*P(x0, y0), *P(x1, y1)], outline=ink, width=sw); reg("board", (*P(x0, y0), *P(x1, y1)))
        nx0, ny0, nx1, ny1 = L["narrator"]; cx = (nx0 + nx1) / 2; hs = (nx1 - nx0) * 0.32  # 'Pip': rounded-square head + antenna dot
        d.rounded_rectangle([*P(cx - hs, ny0), *P(cx + hs, ny0 + 2 * hs)], radius=S(hs * 0.5), outline=ink, width=sw)
        d.line([*P(cx, ny0), *P(cx, ny0 - 40)], fill=ink, width=sw); d.ellipse([*P(cx - 12, ny0 - 64), *P(cx + 12, ny0 - 40)], fill=ink)
        top = ny0 + 2 * hs; hip = top + (ny1 - top) * 0.55
        d.line([*P(cx, top), *P(cx, hip)], fill=ink, width=sw)
        d.line([*P(cx, top + 60), *P(cx + hs * 1.6, top + 10)], fill=ink, width=sw); d.line([*P(cx, top + 60), *P(cx - hs * 1.2, top + 150)], fill=ink, width=sw)
        d.line([*P(cx, hip), *P(cx - hs, ny1)], fill=ink, width=sw); d.line([*P(cx, hip), *P(cx + hs, ny1)], fill=ink, width=sw)
        reg("narrator", (*P(cx - hs * 1.2, ny0 - 64), *P(cx + hs * 1.6, ny1)))
        if L.get("short_q") and f >= EV["short_q"]["f"]:  # attempt 3: short question pop (9x16 opening inside 1 s)
            d.text(P(*L["short_q"]), EV["short_q"]["text"], font=font(56), fill=ink); reg("short_q", d.textbbox(P(*L["short_q"]), EV["short_q"]["text"], font=font(56)))
        if f >= EV["moon"]["f"]:
            mx, my, r = L["moon"]; d.ellipse([*P(mx - r / 2, my - r / 2), *P(mx + r / 2, my + r / 2)], outline=ink, width=sw, fill="#E4E4E4")
            reg("moon", (*P(mx - r / 2, my - r / 2), *P(mx + r / 2, my + r / 2)))
            d.line([*P(mx - r * .15, my - r * .2), *P(mx + r * .05, my), *P(mx - r * .05, my + r * .2)], fill=ink, width=max(2, sw // 2))  # crack
        if f >= EV["moon_label"]["f"]:
            d.text(P(*L["moon_label"]), EV["moon_label"]["text"], font=font(56), fill=ink); reg("moon_label", d.textbbox(P(*L["moon_label"]), EV["moon_label"]["text"], font=font(56)))
        if f >= EV["red_circle"]["f"]:
            cx2, cy2, cr = L["circle"]; d.ellipse([*P(cx2 - cr, cy2 - cr), *P(cx2 + cr, cy2 + cr)], outline=red, width=sw)
        return im

    def scene(f):
        im = Image.new("RGB", (W, Hh), "#15171C"); d = ImageDraw.Draw(im)  # DARK_FIELD: night
        mx, my, r = L["scene_moon"]; d.ellipse([*P(mx - r, my - r), *P(mx + r, my + r)], fill="#DDE6EE", outline=ink, width=sw); reg("scene_moon", (*P(mx - r, my - r), *P(mx + r, my + r)))
        if f >= EV["scene_label_1"]["f"] and EV["scene_label_1"].get("state") == "MELT_DRIPS":  # attempt 3: melt state on the moon
            for dx, ln in ((-0.35, 0.30), (0.0, 0.42), (0.35, 0.26)):
                x, y0 = mx + dx * r, my + r * (1 - dx * dx) ** 0.5 - 4
                d.line([*P(x, y0), *P(x, y0 + ln * r)], fill="#9FC3E0", width=sw); d.ellipse([*P(x - 14, y0 + ln * r - 6), *P(x + 14, y0 + ln * r + 22)], fill="#9FC3E0")
            reg("melt_drips", (*P(mx - 0.35 * r - 14, my + 0.8 * r), *P(mx + 0.35 * r + 14, my + r + 0.42 * r + 22)))
        if f >= EV["scene_label_2"]["f"] and EV["scene_label_2"].get("state") == "STEAM_WISPS":  # attempt 3: steam state rising from the moon
            for dx in (-0.4, 0.0, 0.4):
                x0 = mx + dx * r; ys = [my - r * (1 - dx * dx) ** 0.5 - 10 - k * 0.1 * r for k in range(6)]
                d.line([P(x0 + (18 if k % 2 else -18), y) for k, y in enumerate(ys)], fill="#F8F8F8", width=max(2, sw // 2), joint="curve")
            reg("steam_wisps", (*P(mx - 0.4 * r - 18, my - r - 10 - 0.5 * r), *P(mx + 0.4 * r + 18, my - 0.9 * r)))
        gy = 0.82 * Hh; d.polygon([(0, Hh), (0, gy), (W * .3, gy - Hh * .05), (W * .6, gy + Hh * .01), (W, gy - Hh * .04), (W, Hh)], fill="#050505")
        for k, key in enumerate(("scene_label_1", "scene_label_2")):
            if f >= EV[key]["f"]: d.text(P(*L["scene_labels"][k]), EV[key]["text"], font=font(56), fill="#F8F8F8"); reg(key, d.textbbox(P(*L["scene_labels"][k]), EV[key]["text"], font=font(56)))
        return im

    glow = Image.new("RGB", (W, Hh), "#101010"); g = ImageDraw.Draw(glow)  # glow plate: radial warm glow (GLOW class)
    cx, cy = W // 2, int(Hh * .45)
    for k in range(60, 0, -1):
        rr = int(min(W, Hh) * .6 * k / 60); c = int(255 * (1 - k / 60) ** 1.5)
        g.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(min(255, 30 + c), min(255, 20 + int(c * .85)), 10 + int(c * .5)))
    glow = glow.filter(ImageFilter.GaussianBlur(6))

    def frame(f):
        if f < EV["scene_night"]["f"]: return base_rig(f)
        a = scene(f); dz = EV["glow_plate"]
        if f < dz["f"]: return a
        t = min(1.0, (f - dz["f"] + 1) / dz["frames"]); return Image.blend(a, glow, t)

    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{Hh}", "-r", str(T["fps"]), "-i", "-",
                            "-c:v", "libx264", "-preset", "slow", "-crf", "12", "-pix_fmt", "yuv420p", "-r", str(T["fps"]), "-movflags", "+faststart", f"{OUT}/proof_{name}.mp4"], stdin=subprocess.PIPE)
    prev, diffs, keys, redpx, layout_check = None, [], {}, [], {}
    M = 16  # safe margin px
    def check(B):
        out = {k: "CLIPPED" for k, b in B.items() if b[0] < M or b[1] < M or b[2] > W - M or b[3] > Hh - M}
        ov = lambda a, b: a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]
        for k, b in B.items():
            if k.endswith("label") or k.startswith("scene_label") or k in ("moon_label", "short_q"):
                for k2, b2 in B.items():
                    if k2 != k and k2 not in ("board",) and ov(b, b2): out[k] = f"OVERLAPS {k2}"
        if "card_text" in B and "card" in B and not (B["card_text"][2] <= B["card"][2] - M // 2): out["card_text"] = "OVERFLOWS card"
        return dict(boxes=B, defects=out)
    keyf = sorted({0, 59} | {e["f"] for e in T["events"]} | {e["f"] - 1 for e in T["events"]} | {23, 175, 191})
    for f in range(T["frames"]):
        a = np.asarray(frame(f), np.uint8); enc.stdin.write(a.tobytes())
        diffs.append(None if prev is None else int((a != prev).any(axis=2).sum())); prev = a
        r, gg, b = [a[..., i].astype(int) for i in range(3)]; redpx.append(int(((r > 170) & (gg < 90) & (b < 100)).sum()))
        if f in keyf: keys[f] = Image.fromarray(a)
        if f in (131, 169): layout_check[f] = check(dict(boxes))
        if f == 131: boxes.clear()
    enc.stdin.close(); enc.wait(); assert enc.returncode == 0
    tw = 320 if W > Hh else 180; th = int(tw * Hh / W); cols = 6
    sheet = Image.new("RGB", (cols * tw, ((len(keys) + cols - 1) // cols) * (th + 18)), (40, 40, 40)); sd = ImageDraw.Draw(sheet)
    for i, (f, im) in enumerate(sorted(keys.items())):
        X, Y = (i % cols) * tw, (i // cols) * (th + 18); sheet.paste(im.resize((tw, th)), (X, Y + 18)); sd.text((X + 3, Y + 3), f"f{f}", fill=(255, 220, 0))
    sheet.save(f"{OUT}/keyframes_{name}.png")
    json.dump(dict(layout=name, size=[W, Hh], stroke_px=sw, layout_check=layout_check, changed_px_per_frame=diffs, red_px_per_frame=redpx), open(f"{OUT}/preencode_{name}.json", "w"))
    print(name, "done")

for name, L in T["layouts"].items(): render_layout(name, L)
