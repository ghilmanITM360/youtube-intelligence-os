#!/usr/bin/env python3
"""Deep-VF B1: is the long-form opening reuse whole-frame or region/layer-level? (local only, sources read-only)
usage: <venv python> -I opening_reuse.py
For every local LONG_FORM source: verify SHA-256 (campaign/source_hashes_all_2026-11-06.json, else census),
decode native frame n=3 (same frame the library used) as PNG (scratch) + JPEG evidence, then compare to the
modal opening on a 16x9 grid of 120x120 cells (mean |diff| < 4 = SAME). Writes opening_reuse.csv,
opening_cells.csv, variance_map.jpg (per-pixel std across template members) and member_grid.jpg."""
import csv, hashlib, json, os, subprocess, sys, tempfile
import numpy as np, cv2
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif")
OUT = f"{H}/asset_library/_channel/deep_vf/opening"; os.makedirs(OUT, exist_ok=True)
TMP = tempfile.mkdtemp(dir=sys.argv[1] if len(sys.argv) > 1 else None)
hashes = json.load(open(f"{H}/campaign/source_hashes_all_2026-11-06.json"))
cen = {r["video_id"]: r for r in csv.DictReader(open(f"{H}/census/census.csv"))}
longs = sorted(v for v, r in cen.items() if r["format_class"] == "LONG_FORM" and r["local_paths"])
N = 3; frames, meta = {}, {}
for v in longs:
    exp = hashes.get(v, {}).get("sha256") or cen[v]["local_sha256"].split(" | ")[0]; p = None
    for c in cen[v]["local_paths"].split(" | "):  # alternate encodes exist; use the one matching the campaign hash
        h = hashlib.sha256()
        with open(c, "rb") as f:
            for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
        if h.hexdigest() == exp: p = c; break
    if p is None: meta[v] = dict(sha_check="MISMATCH"); continue
    png = f"{TMP}/{v}.png"
    subprocess.run(["ffmpeg", "-v", "error", "-nostdin", "-i", p, "-an", "-vf", f"select=eq(n\\,{N})", "-fps_mode", "passthrough", "-frames:v", "1", "-y", png], check=True)
    im = cv2.imread(png); cv2.imwrite(f"{OUT}/{v}_f{N:03d}.jpg", im, [cv2.IMWRITE_JPEG_QUALITY, 92])
    frames[v] = im.astype(np.int16); meta[v] = dict(sha_check="OK", sha256=exp, publish=cen[v]["publish_datetime"][:10], w=im.shape[1], h=im.shape[0])
vs = [v for v in frames if frames[v].shape == (1080, 1920, 3)]
# modal opening: the frame with the smallest median distance to all others
D = np.array([[np.abs(frames[a] - frames[b]).mean() for b in vs] for a in vs]); ref = vs[int(np.median(D, 1).argmin())]
C = 120; gy, gx = 1080 // C, 1920 // C; cells = []; rows = []
for v in vs:
    d = np.abs(frames[v] - frames[ref]).mean(2); g = d.reshape(gy, C, gx, C).mean((1, 3)); same = g < 4
    for y in range(gy):
        for x in range(gx): cells.append(dict(video_id=v, cy=y, cx=x, mean_abs_diff=f"{g[y, x]:.2f}", same=bool(same[y, x])))
    rows.append(dict(video_id=v, publish=meta[v]["publish"], ref=ref, whole_frame_mean_abs_diff=f"{d.mean():.2f}", px_diff_gt24_frac=f"{(d > 24).mean():.4f}",
                     cells_same=int(same.sum()), cells_total=same.size, sha256=meta[v]["sha256"]))
for v in meta:
    if v not in vs: rows.append(dict(video_id=v, publish=meta[v].get("publish", ""), ref=ref, whole_frame_mean_abs_diff="", px_diff_gt24_frac="", cells_same="", cells_total="", sha256=meta[v].get("sha256", meta[v]["sha_check"])))
for name, data in (("opening_reuse.csv", sorted(rows, key=lambda r: r["publish"])), ("opening_cells.csv", cells)):
    with open(f"{OUT}/{name}", "w", newline="") as fo: w = csv.DictWriter(fo, list(data[0])); w.writeheader(); w.writerows(data)
tmpl = [v for v in vs if (np.abs(frames[v] - frames[ref]).mean(2).reshape(gy, C, gx, C).mean((1, 3)) < 4).sum() >= 0.6 * gy * gx]
S = np.stack([frames[v].mean(2) for v in tmpl]).std(0); vm = np.clip(S * 4, 0, 255).astype(np.uint8)
vm = cv2.cvtColor(vm, cv2.COLOR_GRAY2BGR);
for y in range(gy): cv2.line(vm, (0, y * C), (1919, y * C), (0, 80, 160), 1)
for x in range(gx): cv2.line(vm, (x * C, 0), (x * C, 1079), (0, 80, 160), 1)
cv2.putText(vm, f"std across {len(tmpl)} template openings x4 (ref {ref})", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 2)
cv2.imwrite(f"{OUT}/variance_map.jpg", vm, [cv2.IMWRITE_JPEG_QUALITY, 88])
tw, th = 384, 216; cols = 6; order = sorted(rows, key=lambda r: r["publish"]); order = [r for r in order if r["video_id"] in frames]
sheet = np.full((((len(order) + cols - 1) // cols) * (th + 22), cols * tw, 3), 40, np.uint8)
for i, r in enumerate(order):
    t = cv2.resize(frames[r["video_id"]].astype(np.uint8), (tw, th), interpolation=cv2.INTER_AREA); X, Y = (i % cols) * tw, (i // cols) * (th + 22)
    sheet[Y + 22:Y + 22 + th, X:X + tw] = t; cv2.putText(sheet, f"{r['video_id']} {r['publish']} {r['cells_same']}/{r['cells_total']}", (X + 3, Y + 16), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 1)
cv2.imwrite(f"{OUT}/member_grid.jpg", sheet, [cv2.IMWRITE_JPEG_QUALITY, 85])
print("ref", ref, "videos", len(vs), "template(>=60% cells)", len(tmpl), "sha", {k: sum(m["sha_check"] == k for m in meta.values()) for k in ("OK", "MISMATCH")})
for r in order: print(r["video_id"], r["publish"], r["cells_same"], r["whole_frame_mean_abs_diff"], r["px_diff_gt24_frac"])
