#!/usr/bin/env python3
"""Band-aware event segmentation from the stored gray frames of one video.

Usage: python3 -E segment_events.py <video_id> <local_evidence_root> [bands.json]

bands.json (written per video after inspecting the row-activity profile; normalized y of frame height):
  {"header":[0.20,0.30], "stage":[0.30,0.665], "caption":[0.665,0.80], "stage_thr":8, "gap":4}
Outputs under videos/<vid>/auto/:
  STAGE_EVENTS_AUTO.csv   one row per merged stage-activity interval (candidate cuts/animations)
  CAPTION_EVENTS_AUTO.csv one row per caption-band change (word appended / phrase reset), with ink geometry
  bands.json              the bands used
No classification is final here: every row is a CANDIDATE to be confirmed by frame inspection.
"""
import csv
import json
import os
import sys

import numpy as np

RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THR = 16  # gray-level difference that counts as a changed pixel


def segments(sig, thr, gap):
    act = sig > thr
    out, i, n = [], 0, len(sig)
    while i < n:
        if act[i]:
            last = j = i
            while j < n and (act[j] or j - last <= gap):
                if act[j]:
                    last = j
                j += 1
            out.append((i, last))
            i = last + 1
        else:
            i += 1
    return out


def main(vid, ev_root, bands_path=None):
    out = os.path.join(RDIR, "videos", vid, "auto")
    gray = np.load(os.path.join(ev_root, vid, "gray.npy"))
    n, h, w = gray.shape
    fps = json.load(open(os.path.join(out, "AUTO_SUMMARY.json")))["fps"]
    bpath = bands_path or os.path.join(out, "bands.json")
    bands = json.load(open(bpath))
    json.dump(bands, open(os.path.join(out, "bands.json"), "w"), indent=1)
    g = gray.astype(np.int16)
    d = np.concatenate([np.zeros((1, h, w), bool), np.abs(np.diff(g, axis=0)) > THR])
    r = lambda k: (int(bands[k][0] * h), int(bands[k][1] * h))
    s0, s1 = r("stage")
    c0, c1 = r("caption")
    stage = d[:, s0:s1, :]
    sc = stage.sum((1, 2))
    stage_px = stage.shape[1] * stage.shape[2]
    rows = []
    for k, (a, b) in enumerate(segments(sc, bands.get("stage_thr", 8), bands.get("gap", 4)), 1):
        u = stage[a:b + 1].any(0)
        ys, xs = np.where(u)
        pre = max(a - 1, 0)
        post = min(b + 1, n - 1)
        sd = (np.abs(g[post, s0:s1] - g[pre, s0:s1]) > THR).mean()
        ink_pre = (gray[pre, s0:s1] < 235).mean()
        ink_post = (gray[post, s0:s1] < 235).mean()
        first = np.where(stage[a])[0] if sc[a] else np.array([])
        cen0 = cen1 = (None, None)
        yy, xx = np.where(stage[a])
        if len(yy):
            cen0 = (round(float(xx.mean() / w), 3), round(float((yy.mean() + s0) / h), 3))
        yy, xx = np.where(stage[b])
        if len(yy):
            cen1 = (round(float(xx.mean() / w), 3), round(float((yy.mean() + s0) / h), 3))
        rows.append({
            "event_id": "SE%03d" % k, "start_frame": a, "end_frame": b, "n_active_span": b - a + 1,
            "active_frames": int((sc[a:b + 1] > bands.get("stage_thr", 8)).sum()),
            "start_sec": round(a / fps, 3), "end_sec_exclusive": round((b + 1) / fps, 3),
            "peak_changed_px": int(sc[a:b + 1].max()), "peak_changed_frac_of_stage": round(float(sc[a:b + 1].max()) / stage_px, 4),
            "union_bbox_norm": "%.3f,%.3f,%.3f,%.3f" % (xs.min() / w, (ys.min() + s0) / h, (xs.max() + 1) / w, (ys.max() + 1 + s0) / h),
            "pre_post_stage_diff_frac": round(float(sd), 4), "stage_ink_pre": round(float(ink_pre), 4),
            "stage_ink_post": round(float(ink_post), 4), "centroid_first": "%s,%s" % cen0, "centroid_last": "%s,%s" % cen1,
            "auto_hint": ("HARD_CUT_OR_POP" if b - a + 1 <= 2 and sd > 0.08 else
                          "SMALL_LOCAL_CHANGE" if sd < 0.03 and b - a + 1 <= 12 else "ANIMATION_OR_MULTI_FRAME"),
        })
    with open(os.path.join(out, "STAGE_EVENTS_AUTO.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        wr.writeheader()
        wr.writerows(rows)
    # caption band: ink geometry per frame, then change events
    cap = gray[:, c0:c1, :] < 120
    ink = cap.sum((1, 2))
    cdiff = d[:, c0:c1, :].sum((1, 2))
    events = []
    prev = None
    for i in range(n):
        if cdiff[i] > 3:
            ys, xs = np.where(cap[i])
            bb = (xs.min() / w, xs.max() / w, (ys.min() + c0) / h, (ys.max() + c0) / h) if len(xs) else (0, 0, 0, 0)
            kind = "RESET_OR_CLEAR" if ink[i] < 0.5 * ink[i - 1] else ("ADD" if ink[i] > ink[i - 1] else "OTHER")
            events.append({"frame": i, "t_sec": round(i / fps, 3), "changed_px": int(cdiff[i]), "ink_px": int(ink[i]),
                           "ink_prev_px": int(ink[i - 1]), "kind": kind,
                           "text_x0": round(bb[0], 3), "text_x1": round(bb[1], 3), "text_y0": round(bb[2], 3), "text_y1": round(bb[3], 3)})
    with open(os.path.join(out, "CAPTION_EVENTS_AUTO.csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(events[0].keys()))
        wr.writeheader()
        wr.writerows(events)
    print(len(rows), "stage events;", len(events), "caption change frames; hints:",
          {k: sum(1 for x in rows if x["auto_hint"] == k) for k in set(x["auto_hint"] for x in rows)})


if __name__ == "__main__":
    main(*sys.argv[1:4])
