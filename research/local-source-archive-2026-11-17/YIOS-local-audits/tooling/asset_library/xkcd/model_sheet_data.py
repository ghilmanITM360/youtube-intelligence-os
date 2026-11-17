#!/usr/bin/env python3
"""xkcd What If: measured inputs for model sheets (local only; read-only on ledgers and frames).
usage: <venv python> -I model_sheet_data.py <xkcd asset_library_root>
Writes <root>/_channel/model_sheets/: rhythm_by_video.csv, entering_class_counts.csv, entering_class_durations.csv,
palette_*.csv/.png, canvas_colour.csv, figure_measure_samples.csv (+ figure_measure_check.jpg overlay for viewing).
Rhythm/entering classes come from videos/<id>/tables/state_ledger.csv (MEASURED by the campaign pipeline, every
decoded frame; class labels are reviewer-assigned = OBSERVED). Figure geometry = ESTIMATED (auto pixel rule, checked
by eye on the overlay sheet). Not the CF peach-skin detector: xkcd heads are unfilled circles."""
import collections, csv, glob, json, os, re, statistics, sys
import numpy as np, cv2
from PIL import Image, ImageDraw
root = os.path.abspath(sys.argv[1]); H = os.path.dirname(root); out = f"{root}/_channel/model_sheets"; os.makedirs(out, exist_ok=True)
fmt = {r["video_id"]: r["format"] for r in csv.DictReader(open(f"{root}/_channel/coverage_by_video.csv"))}
L = {v: list(csv.DictReader(open(f"{H}/videos/{v}/tables/state_ledger.csv"))) for v in fmt}
def eclass(sub):
    s = sub.split("+")[0]
    for k, pat in [("DISSOLVE_FADE", r"DISSOLVE|FADE"), ("ZOOM", r"ZOOM"), ("PAN_SLIDE_SCROLL", r"PAN|SCROLL|SLIDE|WHIP"),
                   ("DRAW_ON_TYPE", r"WRITE_ON_TYPE|TYPE_ON"), ("DRAW_ON_STROKE", r"WRITE_ON|DRAW"), ("POP_ON", r"POP_ON|APPEAR"),
                   ("POP_OFF", r"POP_OFF|REMOVE|DISAPPEAR"), ("POSE_SWAP", r"POSE"), ("TEXT_SWAP", r"TEXT_UPDATE|TEXT_SWAP|LABEL_SWAP|COUNT"),
                   ("STATE_SWAP", r"STATE_SWAP|PANEL|LIGHT|FILL|FLICKER|COLOR|COLOUR|GLOW"), ("CUT", r"SCENE_SWAP|CUT|TITLE_CARD|END_CARD"),
                   ("NO_VISIBLE_CHANGE", r"NO_VISIBLE")]:
        if re.search(pat, s): return k
    return "OTHER"
# ---- rhythm per video (MEASURED)
rh, cls, dur = [], collections.Counter(), collections.defaultdict(list)
for v, rows in L.items():
    D = float(rows[-1]["end_pts_exclusive"]); acts = [r for r in rows if r["kind"] != "HOLD" and r["subtype"] != "NO_VISIBLE_CHANGE"]
    holds = [float(r["end_pts_exclusive"]) - float(r["start_pts"]) for r in rows if r["kind"] == "HOLD"]
    on = [float(r["start_pts"]) for r in acts]; gaps = [b - a for a, b in zip(on, on[1:])]
    cuts = sum(1 for r in acts if eclass(r["subtype"]) == "CUT")
    for r in acts:
        k = eclass(r["subtype"]); cls[(fmt[v], k)] += 1; dur[k].append(int(r["frames"]))
    act_frames = sum(int(r["frames"]) for r in acts); tot = sum(int(r["frames"]) for r in rows)
    rh.append(dict(video_id=v, format=fmt[v], duration_s=f"{D:.1f}", events=len(acts), events_per_min=f"{len(acts)/D*60:.1f}", cuts_per_min=f"{cuts/D*60:.1f}",
                   median_event_gap_s=f"{statistics.median(gaps):.2f}", p10_gap_s=f"{np.percentile(gaps,10):.2f}", p90_gap_s=f"{np.percentile(gaps,90):.2f}",
                   median_hold_s=f"{statistics.median(holds):.2f}", p10_hold_s=f"{np.percentile(holds,10):.2f}", p90_hold_s=f"{np.percentile(holds,90):.2f}",
                   activity_frame_share=f"{act_frames/tot:.3f}"))
for fm in ("LONG_FORM", "SHORT"):  # busy/calm split = tertiles of events/min within format (descriptive, not a rule)
    xs = sorted(float(r["events_per_min"]) for r in rh if r["format"] == fm); t1, t2 = np.percentile(xs, [33.3, 66.7])
    for r in rh:
        if r["format"] == fm: e = float(r["events_per_min"]); r["rhythm_type"] = "CALM" if e <= t1 else "BUSY" if e >= t2 else "MID"
with open(f"{out}/rhythm_by_video.csv", "w", newline="") as f: w = csv.DictWriter(f, list(rh[0])); w.writeheader(); w.writerows(sorted(rh, key=lambda r: (r["format"], -float(r["events_per_min"]))))
with open(f"{out}/entering_class_counts.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["format", "entering_class", "events", "share_within_format"])
    for fm in ("LONG_FORM", "SHORT"):
        n = sum(c for (g, _), c in cls.items() if g == fm)
        for (g, k), c in sorted(cls.items(), key=lambda kv: -kv[1]):
            if g == fm: w.writerow([fm, k, c, f"{c/n:.4f}"])
with open(f"{out}/entering_class_durations.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["entering_class", "n", "frames_median", "frames_p10", "frames_p90", "seconds_median_at_24fps"])
    for k, xs in sorted(dur.items(), key=lambda kv: -len(kv[1])): w.writerow([k, len(xs), statistics.median(xs), int(np.percentile(xs, 10)), int(np.percentile(xs, 90)), f"{statistics.median(xs)/24:.3f}"])
# ---- palette (5-bit bins merged within 36 RGB units; MEASURED on sampled rep frames)
cat = list(csv.DictReader(open(f"{root}/_channel/category_index.csv"))); rng = np.random.default_rng(3)
def palette(sel, name, k=16, chromatic=False, drop_canvas=True):
    pick = rng.choice(len(sel), size=min(300, len(sel)), replace=False); px = []
    for i in pick:
        im = Image.open(f"{root}/{sel[i]['rep_file']}"); im.draft("RGB", (480, 480)); a = np.asarray(im.convert("RGB").resize((240, 135) if im.size[0] > im.size[1] else (135, 240)), dtype=np.uint8).reshape(-1, 3)
        if drop_canvas: a = a[a.min(axis=1) < 235]
        if len(a): px.append(a[rng.choice(len(a), size=min(400, len(a)), replace=False)])
    px = np.concatenate(px).astype(np.int32)
    if chromatic: px = px[px.max(axis=1) - px.min(axis=1) > 30]
    n = len(px); key = (px[:, 0] >> 3) * 1024 + (px[:, 1] >> 3) * 32 + (px[:, 2] >> 3); cnt = collections.Counter(key.tolist()); res = []
    for kk, m in cnt.most_common(400):
        c = np.array([(kk >> 10) * 8 + 4, ((kk >> 5) & 31) * 8 + 4, (kk & 31) * 8 + 4])
        for j, (h, s, cc) in enumerate(res):
            if np.abs(cc - c).sum() < 36: res[j] = (h, s + m / n, cc); break
        else: res.append((f"#{c[0]:02X}{c[1]:02X}{c[2]:02X}", m / n, c))
    res = sorted(((h, s) for h, s, _ in res), key=lambda t: -t[1])[:k]
    with open(f"{out}/palette_{name}.csv", "w", newline="") as f: w = csv.writer(f); w.writerow(["hex", "share_of_sampled_pixels", "frames_sampled", "pixels"]); [w.writerow([h, f"{s:.4f}", len(pick), n]) for h, s in res]
    sw = Image.new("RGB", (len(res) * 60, 80), (255, 255, 255))
    for j, (h, s) in enumerate(res): sw.paste(Image.new("RGB", (60, 80), h), (j * 60, 0))
    sw.save(f"{out}/palette_{name}.png"); print(name, len(sel), "pool;", [(h, round(s, 3)) for h, s in res[:10]])
canvas = [r for r in cat if not r["features"]]
palette(canvas, "canvas_frames_ink_and_accents"); palette(canvas, "canvas_frames_chromatic", chromatic=True)
palette([r for r in cat if "dark_screen" in r["features"]], "dark_scenes", drop_canvas=False)
palette([r for r in cat if "full_bleed_scene" in r["features"]], "full_bleed_scenes_chromatic", chromatic=True, drop_canvas=False)
# canvas colour: modal pixel of canvas frames (MEASURED)
cc = collections.Counter()
for r in rng.choice(canvas, size=200, replace=False):
    a = np.asarray(Image.open(f"{root}/{r['rep_file']}").convert("RGB"))[::8, ::8].reshape(-1, 3); cc.update(map(tuple, a[a.min(axis=1) > 225]))
with open(f"{out}/canvas_colour.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["rgb_hex", "share_of_light_pixels"]); t = sum(cc.values()); [w.writerow(["#%02X%02X%02X" % k, f"{c/t:.4f}"]) for k, c in cc.most_common(8)]
# ---- figure geometry on opening/narrator frames (ESTIMATED)
samples, tiles = [], []
cands = [(v, L[v][0]) for v in fmt]  # first state of every video: lecture frame (long) / opening (Shorts)
for v, r in cands:
    p = sorted(glob.glob(f"{root}/{v}/states/{r['seg']}_f*.jpg"))
    if not p: continue
    im = np.asarray(Image.open(p[0]).convert("L")); h, wd = im.shape
    dark = (im < 110).astype(np.uint8); n, lab, st, _ = cv2.connectedComponentsWithStats(cv2.dilate(dark, np.ones((5, 5), np.uint8)))
    best = None
    for i in range(1, n):
        x, y, bw, bh, area = st[i]
        if bh > 0.2 * h and bw < 0.4 * wd and bh > 0.9 * bw and (best is None or bh > st[best][3]): best = i
    if best is None: continue
    x, y, bw, bh, _ = st[best]; m = (lab[y:y + bh, x:x + bw] == best) & (dark[y:y + bh, x:x + bw] > 0)
    widths = [(np.ptp(np.where(row)[0]) + 1) if row.any() else 0 for row in m]
    hw, neck = 0, None  # scan down from the top: head widens, then narrows to the neck line before arms start
    for i, wv in enumerate(widths[: int(0.5 * bh)]):
        if i > 5 and hw > 0 and wv <= max(3, 0.25 * hw): neck = i; break
        if i > 5 and hw > 0 and wv > 1.4 * widths[i - 1] > 0: neck = i; break  # head bottom meets the arm line
        hw = max(hw, wv)
    if neck is None or neck < 0.08 * bh: continue
    runs = []
    for row in m[: neck]:
        d = np.diff(np.concatenate([[0], row.astype(np.int8), [0]])); s_, e_ = np.where(d == 1)[0], np.where(d == -1)[0]
        if len(s_) == 2: runs += list(e_ - s_)
    samples.append(dict(video_id=v, format=fmt[v], state=r["seg"], frame_w=wd, frame_h=h, figure_h_px=bh, head_w_px=hw, head_h_px=neck,
                        head_w_over_figure_h=f"{hw/bh:.3f}", stroke_px_median=float(np.median(runs)) if runs else "", stroke_over_frame_h=f"{np.median(runs)/h:.4f}" if runs else "", file=os.path.relpath(p[0], root)))
    t = Image.open(p[0]).convert("RGB"); dr = ImageDraw.Draw(t); dr.rectangle([x, y, x + bw, y + bh], outline=(255, 0, 0), width=4); dr.rectangle([x, y, x + bw, y + neck], outline=(0, 160, 255), width=4)
    t.thumbnail((360, 360)); tiles.append((t, v))
with open(f"{out}/figure_measure_samples.csv", "w", newline="") as f: w = csv.DictWriter(f, list(samples[0])); w.writeheader(); w.writerows(samples)
cols = 8; sheet = Image.new("RGB", (cols * 360, ((len(tiles) + cols - 1) // cols) * 374), (40, 40, 40)); dr = ImageDraw.Draw(sheet)
for i, (t, v) in enumerate(tiles): sheet.paste(t, ((i % cols) * 360, (i // cols) * 374 + 14)); dr.text(((i % cols) * 360 + 2, (i // cols) * 374), f"{i+1} {v}", fill=(255, 255, 0))
sheet.save(f"{out}/figure_measure_check.jpg", quality=85)
for fm in ("LONG_FORM", "SHORT"):
    q = [float(s["head_w_over_figure_h"]) for s in samples if s["format"] == fm]; sw_ = [float(s["stroke_over_frame_h"]) for s in samples if s["format"] == fm and s["stroke_over_frame_h"]]
    if q: print(fm, "n", len(q), "head/fig median", round(statistics.median(q), 3), "p25-75", np.round(np.percentile(q, [25, 75]), 3), "stroke/frame_h median", round(statistics.median(sw_), 4) if sw_ else None)
print("classes", cls.most_common(30))
