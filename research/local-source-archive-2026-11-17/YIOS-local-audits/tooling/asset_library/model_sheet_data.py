#!/usr/bin/env python3
"""Measured inputs for model sheets (local only). usage: <venv python> -I model_sheet_data.py <asset_library_root>
Writes <root>/_channel/model_sheets/: asset_roster.csv, rhythm_by_video.csv, entering_class_counts.csv,
palette_*.png/.csv, head_ratio_samples.csv. Every number here is MEASURED from ledgers or pixels unless the file says ESTIMATED."""
import collections, csv, glob, json, os, re, statistics, sys
import numpy as np
from PIL import Image
root = os.path.abspath(sys.argv[1]); out = f"{root}/_channel/model_sheets"; os.makedirs(out, exist_ok=True)
rows = []
for p in sorted(glob.glob(f"{root}/*/states_index.csv")): rows += list(csv.DictReader(open(p)))
for r in rows: r["_n"] = int(r["frame_index"])
# ---- asset roster (ledger asset_ids, MEASURED counts)
ids = collections.defaultdict(lambda: {"states": 0, "videos": set(), "ex": []})
for r in rows:
    for a in re.split(r"[;,]", r.get("asset_ids", "") or ""):
        a = a.strip()
        if a and a != "-":
            d = ids[a]; d["states"] += 1; d["videos"].add(r["video_id"]); d["ex"].append((len(re.split(r"[;,]", r["asset_ids"])), r["video_id"], r["file"]))
with open(f"{out}/asset_roster.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["asset_id", "states", "videos", "n_videos", "exemplar_files(solo-ish first)"])
    for a, d in sorted(ids.items(), key=lambda kv: -kv[1]["states"]):
        ex = sorted(d["ex"], key=lambda t: (t[0], t[2]))[:6]
        w.writerow([a, d["states"], ";".join(sorted(d["videos"])), len(d["videos"]), ";".join(f"{v}/{fl}" for _, v, fl in ex)])
# ---- rhythm per video + entering classes
cls = collections.Counter(); rh = []
for v in sorted({r["video_id"] for r in rows}):
    rs = sorted({(r["_n"], float(r["source_pts_s"])) for r in rows if r["video_id"] == v}, key=lambda t: t[1])
    ts = [t for _, t in rs]; gaps = [b - a for a, b in zip(ts, ts[1:])]
    dur = ts[-1] if ts else 0
    rh.append(dict(video_id=v, state_frames=len(ts), last_state_pts_s=f"{dur:.1f}", states_per_min=f"{len(ts)/dur*60:.1f}" if dur else "",
                   median_gap_s=f"{statistics.median(gaps):.2f}" if gaps else "", p10_gap_s=f"{np.percentile(gaps,10):.2f}" if gaps else "", p90_gap_s=f"{np.percentile(gaps,90):.2f}" if gaps else ""))
for r in rows: cls[(r.get("entering_class") or "").split(":")[0].strip()] += 1
with open(f"{out}/rhythm_by_video.csv", "w", newline="") as f: w = csv.DictWriter(f, list(rh[0])); w.writeheader(); w.writerows(rh)
with open(f"{out}/entering_class_counts.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["entering_class", "states", "share"]); [w.writerow([k, n, f"{n/len(rows):.4f}"]) for k, n in cls.most_common()]
# ---- palette (median-cut on non-white pixels; sampled frames; MEASURED)
cat = list(csv.DictReader(open(f"{root}/_channel/category_index.csv")))
rng = np.random.default_rng(3)
def palette(sel, name, k=20):
    pick = rng.choice(len(sel), size=min(260, len(sel)), replace=False); px = []
    for i in pick:
        im = Image.open(f"{root}/{sel[i]['rep_file']}"); im.draft("RGB", (480, 270)); a = np.asarray(im.convert("RGB").resize((240, 135)), dtype=np.uint8).reshape(-1, 3)
        a = a[a.min(axis=1) < 235]
        if len(a): px.append(a[rng.choice(len(a), size=min(400, len(a)), replace=False)])
    px = np.concatenate(px).astype(np.int32)
    if name.endswith("_chromatic"): px = px[px.max(axis=1) - px.min(axis=1) > 30]  # drop black/grey/antialias neutrals
    n = len(px)  # exact-flat-colour histogram: 5 bits/channel bins, bin centre reported
    key = (px[:, 0] >> 3) * 1024 + (px[:, 1] >> 3) * 32 + (px[:, 2] >> 3); cnt = collections.Counter(key.tolist()); res = []
    for kk, m in cnt.most_common(400):  # merge bins whose centres are within 24 RGB units of an already-kept colour
        c = np.array([(kk >> 10) * 8 + 4, ((kk >> 5) & 31) * 8 + 4, (kk & 31) * 8 + 4])
        for j, (h, s, cc) in enumerate(res):
            if np.abs(cc - c).sum() < 36: res[j] = (h, s + m / n, cc); break
        else: res.append((f"#{c[0]:02X}{c[1]:02X}{c[2]:02X}", m / n, c))
    res = sorted(((h, s) for h, s, _ in res), key=lambda t: -t[1])[:k]
    with open(f"{out}/palette_{name}.csv", "w", newline="") as f: w = csv.writer(f); w.writerow(["hex", "share_of_non_white_pixels"]); [w.writerow([h, f"{s:.4f}"]) for h, s in res]
    sw = Image.new("RGB", (len(res) * 60, 80), (255, 255, 255))
    for j, (h, s) in enumerate(res): sw.paste(Image.new("RGB", (60, 80), h), (j * 60, 0))
    sw.save(f"{out}/palette_{name}.png"); print(name, len(sel), "frames;", [(h, round(s, 3)) for h, s in res[:10]])
palette([r for r in cat if float(r["white_frac"]) > 0.7 and r["primary"] in ("characters", "props") and "dark_screen" not in r["features"]], "white_canvas_character_prop_frames")
palette([r for r in cat if "full_bleed_scene" in r["features"]], "full_bleed_scenes")
palette([r for r in cat if float(r["white_frac"]) > 0.7 and r["primary"] in ("characters", "props") and "dark_screen" not in r["features"]], "white_canvas_character_prop_frames_chromatic")
palette([r for r in cat if "full_bleed_scene" in r["features"]], "full_bleed_scenes_chromatic")
# ---- stick-figure head ratio (ESTIMATED; solo-figure frames only)
res = []
for r in cat:
    if r["primary"] != "characters" or float(r["white_frac"]) < 0.93: continue
    im = Image.open(f"{root}/{r['rep_file']}")
    if im.size != (1920, 1080): continue
    a = np.asarray(im.convert("RGB"), dtype=np.int16)
    dark = a.max(axis=2) < 80; peach = (a[..., 0] > 215) & (a[..., 1] > 170) & (a[..., 1] < 235) & (a[..., 2] > 130) & (a[..., 2] < 215) & (a[..., 0] - a[..., 2] > 25)
    if peach.sum() < 4000: continue
    ys, xs = np.where(peach); hw, hh = xs.max() - xs.min() + 1, ys.max() - ys.min() + 1
    if not (0.8 < hw / hh < 1.25) or peach.sum() > 0.6 * hw * hh * 1.0 + 1e6: continue
    dy, dx = np.where(dark)
    if len(dy) < 500: continue
    fh = dy.max() - min(dy.min(), ys.min()) + 1
    runs = []
    for y in range(0, 1080, 6):
        row = dark[y]
        if row.any():
            d = np.diff(np.concatenate([[0], row.astype(np.int8), [0]])); s, e = np.where(d == 1)[0], np.where(d == -1)[0]; runs += list(e - s)
    res.append((r["cluster_id"], int(hw), int(hh), int(fh), hw / fh, float(np.median(runs)) if runs else 0))
with open(f"{out}/head_ratio_samples.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["cluster_id", "head_w_px", "head_h_px", "figure_h_px", "head_w_over_figure_h", "median_dark_run_px(ESTIMATED_stroke)"]); [w.writerow(x) for x in res]
if res:
    q = [x[4] for x in res]; print("head/figure n=", len(res), "median", round(statistics.median(q), 3), "p25-p75", round(np.percentile(q, 25), 3), round(np.percentile(q, 75), 3),
                                  "stroke median", statistics.median([x[5] for x in res]))
print("rhythm:", [(x["video_id"][:6], x["states_per_min"], x["median_gap_s"]) for x in rh][:20]); print("classes:", cls.most_common(14))
print("top assets:", [(a, d["states"], len(d["videos"])) for a, d in sorted(ids.items(), key=lambda kv: -kv[1]["states"])[:40]])
