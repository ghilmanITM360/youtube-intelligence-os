#!/usr/bin/env python3
"""Rules-v3 Short camera budget: merge WHOLE_FRAME_CAMERA moves of one device into one instance.
Instance = maximal run of camera-labelled ACTIVITY segments with no other (non-camera) ACTIVITY segment between them
and <= 3.0 s between the end of one and the start of the next (holds allowed). share = instances / all ACTIVITY.
usage: <venv python> -I camera_instances.py <labels.csv> [...]   (labels csv: video_id, seg, motion_label; any length)"""
import csv, os, sys, collections
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif")

def instances(v, labels):  # labels: {seg: motion_label}
    seg = list(csv.DictReader(open(f"{H}/videos/{v}/tables/segments_v1.csv"))); acts = [s for s in seg if s["kind"] == "ACTIVITY"]
    n, inst, prev_end, run = len(acts), 0, None, False
    for s in acts:
        cam = labels.get(s["seg"]) == "WHOLE_FRAME_CAMERA"; st = float(s["start_pts"]); en = float(s.get("end_pts") or st)
        if cam and not (run and prev_end is not None and st - prev_end <= 3.0): inst += 1
        run = cam; prev_end = en if cam else None
    return dict(activities=n, moves=sum(l == "WHOLE_FRAME_CAMERA" for l in labels.values()), instances=inst, inst_share=round(inst / n, 3) if n else 0)

def demo():
    assert instances.__code__.co_argcount == 2

if __name__ == "__main__":
    L = collections.defaultdict(dict)
    for f in sys.argv[1:]:
        for r in csv.DictReader(open(f)): L[r["video_id"]][r["seg"]] = r["motion_label"]
    for v, lab in L.items(): print(v, instances(v, lab))
