#!/usr/bin/env python3
"""Full-bleed layout event segmentation (no fixed header/stage/caption bands).

Usage: python3 -E segment_full.py <video_id> <local_evidence_root>
Per frame: fraction of pixels whose gray level changed by >16 (whole frame). Segments = runs above 0.3 % with gaps <= 2.
Class (auto_hint): CUT (peak>=0.20, span<=3) | BIG_POP (0.03<=peak<0.20, span<=3) | ANIMATION (span>6 or mean>=0.02) | SMALL (caption word / micro change).
Writes videos/<vid>/auto/STAGE_EVENTS_AUTO.csv with the same columns as segment_events.py plus caption-like flag.
"""
import csv, json, os, sys
import numpy as np
RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THR = 16

def segments(sig, thr, gap):
    act = sig > thr; out = []; i = 0; n = len(sig)
    while i < n:
        if act[i]:
            last = j = i
            while j < n and (act[j] or j - last <= gap):
                if act[j]: last = j
                j += 1
            out.append((i, last)); i = last + 1
        else: i += 1
    return out

def main(vid, ev_root):
    out = os.path.join(RDIR, "videos", vid, "auto")
    g = np.load(os.path.join(ev_root, vid, "gray.npy")).astype(np.int16)
    n, h, w = g.shape
    fps = json.load(open(os.path.join(out, "AUTO_SUMMARY.json")))["fps"]
    d = np.concatenate([np.zeros((1, h, w), bool), np.abs(np.diff(g, axis=0)) > THR])
    frac = d.mean((1, 2))
    px = frac * h * w
    segs = segments(frac, 0.003, 2)
    rows = []
    for k, (a, b) in enumerate(segs, 1):
        span = b - a + 1
        pk = float(frac[a:b + 1].max()); mean = float(frac[a:b + 1].mean())
        u = d[a:b + 1].any(0); ys, xs = np.where(u)
        pre, post = max(a - 1, 0), min(b + 1, n - 1)
        sd = float((np.abs(g[post] - g[pre]) > THR).mean())
        cls = ("CUT" if pk >= 0.20 and span <= 3 else "BIG_POP" if pk >= 0.03 and span <= 3 else
               "ANIMATION" if span > 6 and mean >= 0.01 else "ANIMATION" if mean >= 0.02 else "SMALL")
        yy, xx = np.where(d[a])
        c0 = "%.3f,%.3f" % (xx.mean() / w, yy.mean() / h) if len(xx) else ","
        yy, xx = np.where(d[b])
        c1 = "%.3f,%.3f" % (xx.mean() / w, yy.mean() / h) if len(xx) else ","
        rows.append({"event_id": "SE%03d" % k, "start_frame": a, "end_frame": b, "n_active_span": span,
                     "active_frames": int((frac[a:b + 1] > 0.003).sum()), "start_sec": round(a / fps, 3), "end_sec_exclusive": round((b + 1) / fps, 3),
                     "peak_changed_px": int(px[a:b + 1].max()), "peak_changed_frac_of_stage": round(pk, 4),
                     "union_bbox_norm": "%.3f,%.3f,%.3f,%.3f" % (xs.min() / w, ys.min() / h, (xs.max() + 1) / w, (ys.max() + 1) / h),
                     "pre_post_stage_diff_frac": round(sd, 4), "stage_ink_pre": round(float((g[pre] < 235).mean()), 4),
                     "stage_ink_post": round(float((g[post] < 235).mean()), 4), "centroid_first": c0, "centroid_last": c1, "auto_hint": cls})
    with open(os.path.join(out, "STAGE_EVENTS_AUTO.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
    json.dump({"mode": "full", "stage": [0.0, 1.0], "stage_thr": int(0.003 * h * w), "auto_cuts": True}, open(os.path.join(out, "bands.json"), "w"), indent=1)
    import collections
    print(len(rows), "events", dict(collections.Counter(r["auto_hint"] for r in rows)))
    print("changed-frac pctl 50/90/99:", np.percentile(frac, [50, 90, 99]).round(4).tolist(), "frames>0.003:", int((frac > 0.003).sum()))

if __name__ == "__main__":
    main(*sys.argv[1:3])
