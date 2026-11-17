#!/usr/bin/env python3
"""Deep-VF v2 colour classifier (native colour, no greyscale). Per frame (BGR uint8) returns measured features and one class:
  TITLE_CARD      mean R>150,G<110,B<110 (whole-frame red card)
  PAINTED_PLATE   saturated (S>60,V>60) pixels >= 25% of frame
  GLOW_DARK       dark (V<50) >= 30% of frame and a smooth luminance ramp (>= 20 distinct V levels inside the dark/bright border band)
  TINT_REGION     low-sat tint (25<=S<=60, V>180) >= 4% of frame, saturated share < 25%
  RED_SOLID       a red connected component with area >= 0.3% of frame and fill ratio (area / bbox area) >= 0.45
  RED_MARK        red pixels present (>= 0.02%) but no solid red component
  COLOUR_ACCENT   saturated share 2-25% without red
  LINE_ART        everything else (grey ink on off-white)
usage: <venv python> -I colour_classes.py <video_id> [...]  -> deep_vf/v2/colour_<vid>.csv (library state JPGs, no decode)"""
import csv, glob, os, sys
import numpy as np, cv2
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif"); OUT = f"{H}/asset_library/_channel/deep_vf/v2"

def classify(bgr):
    b, g, r = [bgr[..., i].astype(float) for i in range(3)]
    if r.mean() > 150 and g.mean() < 110 and b.mean() < 110: return "TITLE_CARD", {}
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV); h, s, v = hsv[..., 0], hsv[..., 1].astype(int), hsv[..., 2].astype(int); n = s.size
    sat = ((s > 60) & (v > 60)).mean(); dark = (v < 50).mean(); tint = ((s >= 25) & (s <= 60) & (v > 180)).mean()
    red = ((h <= 8) | (h >= 172)) & (s > 90) & (v > 90)
    k, lab, st, _ = cv2.connectedComponentsWithStats(red.astype(np.uint8), connectivity=8)
    solid = 0.0
    for i in range(1, k):
        x, y, w, hh, a = st[i]
        if a / n >= 0.003 and a / (w * hh) >= 0.45: solid = max(solid, a / n)
    band = (v >= 50) & (v <= 200) & (cv2.dilate((v < 50).astype(np.uint8), np.ones((15, 15))) > 0)
    ramp = len(np.unique(v[band] // 4)) if band.any() else 0
    f = dict(sat=round(sat, 4), dark=round(dark, 4), tint=round(tint, 4), red=round(red.mean(), 5), red_solid=round(solid, 4), ramp_levels=ramp)
    if sat >= 0.25: c = "PAINTED_PLATE"
    elif dark >= 0.30 and ramp >= 20: c = "GLOW_DARK"
    elif solid > 0: c = "RED_SOLID"
    elif tint >= 0.04: c = "TINT_REGION"
    elif red.mean() >= 0.0002: c = "RED_MARK"
    elif sat >= 0.02: c = "COLOUR_ACCENT"
    else: c = "LINE_ART"
    return c, f

def demo():  # one runnable check
    z = np.full((180, 320, 3), 249, np.uint8); assert classify(z)[0] == "LINE_ART"
    t = z.copy(); t[:] = (40, 40, 200); assert classify(t)[0] == "TITLE_CARD"
    m = z.copy(); cv2.circle(m, (160, 90), 40, (0, 0, 230), 2); assert classify(m)[0] == "RED_MARK", classify(m)
    p = z.copy(); cv2.rectangle(p, (100, 50), (160, 120), (0, 0, 230), -1); assert classify(p)[0] == "RED_SOLID"
    q = z.copy(); q[:100] = (40, 120, 240); assert classify(q)[0] == "PAINTED_PLATE"

if __name__ == "__main__":
    demo(); os.makedirs(OUT, exist_ok=True)
    for vid in sys.argv[1:]:
        rows = []
        for p in sorted(glob.glob(f"{H}/asset_library/{vid}/states/*.jpg")):
            im = cv2.imread(p); im = cv2.resize(im, (320, 180) if im.shape[1] > im.shape[0] else (180, 320), interpolation=cv2.INTER_AREA)
            c, f = classify(im); rows.append(dict(video_id=vid, file=os.path.basename(p), cls=c, **{k: f.get(k, "") for k in ("sat", "dark", "tint", "red", "red_solid", "ramp_levels")}))
        with open(f"{OUT}/colour_{vid}.csv", "w", newline="") as fo:
            w = csv.DictWriter(fo, list(rows[0])); w.writeheader(); w.writerows(rows)
        print(vid, len(rows))
