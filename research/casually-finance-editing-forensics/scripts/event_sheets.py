#!/usr/bin/env python3
"""Render per-event native-frame contact sheets for review (frames stay outside Git).

Usage: python3 -E event_sheets.py <video_id> <local_evidence_root> [--per-sheet 15] [--cols 5] [--scale 0.7]
                                  [--events SE001,SE004] [--max-long 16]
For each row of STAGE_EVENTS_AUTO.csv: pre frame (start-1), every active frame for spans <= 4 (else up to
--max-long evenly spaced), post frame (end+1) and a hold frame (end+4). Labels read "SE004 f206 pre|act|post|hold".
"""
import argparse
import csv
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_sheet as ms  # noqa: E402


def plan(row, max_long, nframes):
    a, b = int(row["start_frame"]), int(row["end_frame"])
    span = b - a + 1
    pairs = [(max(a - 1, 0), "pre")]
    if span <= 4:
        pairs += [(f, "act") for f in range(a, b + 1)]
    else:
        step = max(1, round(span / max_long))
        acts = list(range(a, b + 1, step))
        if acts[-1] != b:
            acts.append(b)
        pairs += [(f, "act") for f in acts]
    pairs += [(min(b + 1, nframes - 1), "post"), (min(b + 4, nframes - 1), "hold")]
    seen, out = set(), []
    for f, role in pairs:
        if f not in seen:
            seen.add(f)
            out.append((f, role))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vid")
    ap.add_argument("ev_root")
    ap.add_argument("--per-sheet", type=int, default=15)
    ap.add_argument("--cols", type=int, default=5)
    ap.add_argument("--scale", type=float, default=0.7)
    ap.add_argument("--cell-w", type=int, default=0)
    ap.add_argument("--events", default="")
    ap.add_argument("--max-long", type=int, default=16)
    ap.add_argument("--prefix", default="ev")
    a = ap.parse_args()
    rows = list(csv.DictReader(open(os.path.join(ms.RDIR, "videos", a.vid, "auto", "STAGE_EVENTS_AUTO.csv"))))
    if a.events:
        want = set(a.events.split(","))
        rows = [r for r in rows if r["event_id"] in want]
    src, fps = ms.source(a.vid)
    import json
    nframes = json.load(open(os.path.join(ms.RDIR, "videos", a.vid, "auto", "AUTO_SUMMARY.json")))["frames_decoded"]
    groups, cur = [], []
    for r in rows:
        items = [(r["event_id"], f, role) for f, role in plan(r, a.max_long, nframes)]
        if cur and len(cur) + len(items) > a.per_sheet:
            groups.append(cur)
            cur = []
        cur += items
        while len(cur) > a.per_sheet:  # long event overflowing a sheet
            groups.append(cur[:a.per_sheet])
            cur = cur[a.per_sheet:]
    if cur:
        groups.append(cur)
    outdir = os.path.join(a.ev_root, a.vid, "sheets")
    os.makedirs(outdir, exist_ok=True)
    for k, grp in enumerate(groups, 1):
        frames = sorted(set(f for _, f, _ in grp))
        tmp = tempfile.mkdtemp()
        try:
            imgs = dict(zip(frames, ms.extract(src, frames, tmp)))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        labels = ["%s f%d %s" % (e, f, role) for e, f, role in grp]
        name = os.path.join(outdir, "%s_%02d_%s-%s.png" % (a.prefix, k, grp[0][0], grp[-1][0]))
        sc = (a.cell_w / imgs[frames[0]].size[0]) if a.cell_w else a.scale
        ms.sheet([imgs[f] for _, f, _ in grp], labels, a.cols, sc, name)
        print(name)


if __name__ == "__main__":
    main()
