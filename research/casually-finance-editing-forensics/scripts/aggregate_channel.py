#!/usr/bin/env python3
"""Channel-level aggregates from VALIDATED per-video tables only (QA.json all_checks_pass).

Usage: python3 -E aggregate_channel.py
Writes: EDITING_TIMING_STATISTICS.csv, MOTION_OPERATION_TAXONOMY.csv, ASSET_FAMILY_LIBRARY.csv, VALIDATION.json
Every aggregate carries its denominator (validated videos / 48 local / 210 public) and the analysis depth mix.
"""
import csv
import json
import os
import statistics
from collections import Counter, defaultdict

RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
inv = {r["Video_ID"]: r for r in csv.DictReader(open(os.path.join(RDIR, "SOURCE_MEDIA_INVENTORY.csv"))) if r["Canonical_For_Analysis"] == "True"}
vids = sorted(v for v in os.listdir(os.path.join(RDIR, "videos")) if os.path.exists(os.path.join(RDIR, "videos", v, "QA.json")))
valid, invalid = [], []
for v in vids:
    q = json.load(open(os.path.join(RDIR, "videos", v, "QA.json")))
    (valid if q["all_checks_pass"] else invalid).append(v)


def era(v):
    b = json.load(open(os.path.join(RDIR, "videos", v, "auto", "bands.json")))
    return "BANDED_HEADLINE_CAPTION" if b.get("header") and b["stage"][0] > 0.0 else "FULL_BLEED"


def med(x):
    x = [i for i in x if i is not None]
    return round(statistics.median(x), 3) if x else ""


rows = []
for v in valid:
    q = json.load(open(os.path.join(RDIR, "videos", v, "QA.json")))
    d = q["derived_statistics"]
    fp = d["frame_classes_pct"]
    cap = d["caption_offset_ms_vs_asr_onset"]
    al = list(csv.DictReader(open(os.path.join(RDIR, "videos", v, "NARRATION_VISUAL_ALIGNMENT.csv"))))
    cuts = [int(r["Offset_To_Nearest_Word_ms"]) for r in al if r["Composition_Reset_At_Event"] == "True"]
    scs = [float(s["Duration_S"]) for s in csv.DictReader(open(os.path.join(RDIR, "videos", v, "SCENE_TIMELINE.csv"))) if int(s["Duration_Frames"]) > 1]
    i = inv[v]
    rows.append({"Video_ID": v, "Title": i["Public_Title"], "Upload_Date": i["Upload_Date"], "Views_Snapshot": i["Public_Views_Snapshot"], "Resolution": "%sx%s" % (i["Width"], i["Height"]),
                 "Native_FPS_File": i["FPS_Avg"], "Duration_S": i["Duration_S"], "Layout_Era": era(v), "Depth": q["analysis_depth"].split(" ")[0],
                 "Scenes": q["counts"]["scenes"], "Scene_Median_S": med(scs), "Scene_P90_S": round(sorted(scs)[int(0.9 * (len(scs) - 1))], 3), "Hard_Cuts": d["hard_cuts"], "Hard_Cuts_Per_Min": d["hard_cuts_per_min"],
                 "Events": q["counts"]["events"], "Events_Per_Min": d["visual_events_per_min"], "One_Frame_Events": q["counts"]["instant_events"],
                 "Static_Hold_Pct": fp.get("STATIC_HOLD"), "Conventional_Pct": fp.get("CONV"), "ScreenRec_Pct": fp.get("SCREENREC"), "Complex_Pct": fp.get("COMPLEX"), "Indeterminate_Pct": fp.get("INDET", 0),
                 "Cut_Offset_To_Word_Median_ms": med(cuts), "Caption_Offset_Median_ms": cap["median"] if isinstance(cap, dict) else "NOT_MEASURED",
                 "Caption_Within_100ms_Pct": cap["within_100ms_pct"] if isinstance(cap, dict) else "NOT_MEASURED",
                 "Cadence": ("24fps_conformed_to_30" if "conformed" in d["native_cadence"]["interpretation"] else "native" if "no 5-frame" in d["native_cadence"]["interpretation"] else "unresolved")})
fields = list(rows[0].keys())
# aggregate rows
def agg(name, sel):
    r = [x for x in rows if sel(x)]
    if not r:
        return None
    a = {"Video_ID": "AGG:" + name, "Title": "n=%d of %d validated (of 48 local, 210 public)" % (len(r), len(valid))}
    for k in ("Duration_S", "Scenes", "Scene_Median_S", "Hard_Cuts_Per_Min", "Events_Per_Min", "Static_Hold_Pct", "Conventional_Pct", "ScreenRec_Pct", "Complex_Pct", "Indeterminate_Pct", "Cut_Offset_To_Word_Median_ms"):
        vals = [float(x[k]) for x in r if x[k] != ""]
        a[k] = round(statistics.median(vals), 2) if vals else ""
    a["Depth"] = dict(Counter(x["Depth"] for x in r)).__repr__()
    return a
ag = [agg("ALL_MEDIANS", lambda x: True), agg("FULL_BLEED", lambda x: x["Layout_Era"] == "FULL_BLEED"), agg("BANDED", lambda x: x["Layout_Era"] != "FULL_BLEED")]
with open(os.path.join(RDIR, "EDITING_TIMING_STATISTICS.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
    w.writerows([a for a in ag if a])

# operations taxonomy
ops = defaultdict(lambda: {"events": 0, "videos": set(), "frames": 0, "conf": Counter(), "labels": Counter(), "tool": None, "class": Counter(), "examples": []})
for v in valid:
    for r in csv.DictReader(open(os.path.join(RDIR, "videos", v, "MOTION_EVENTS.csv"))):
        o = ops[r["Operation"]]
        o["events"] += 1
        o["videos"].add(v)
        o["frames"] += int(r["Duration_Frames"])
        o["conf"][r["Confidence"]] += 1
        o["labels"][r["Observation_Label"].split(" ")[0]] += 1
        o["class"][r["Motion_Method_Class"]] += 1
        o["tool"] = (r["Recreate_CapCut"], r["Recreate_2D_Layer"], r["Recreate_MotionGraphics"], r["Recreate_SVG_Canvas"], r["Recreate_FrameByFrame"], r["Recreate_ImageToVideo_Needed"])
        if len(o["examples"]) < 3 and r["Confidence"] == "HIGH":
            o["examples"].append("%s %s-%s f%s" % (v, r["Start_S"], r["End_S_Exclusive"], r["Start_Frame"]))
meas = {}
for v in valid:
    d = os.path.join(RDIR, "videos", v, "motion")
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            m = json.load(open(os.path.join(d, fn)))
            for k, val in m.items():
                if k.endswith("_fit") and isinstance(val, dict) and val.get("best") not in (None, "UNDETERMINED"):
                    meas.setdefault((m["kind"], k), []).append((v, fn, val["best"], val.get("confidence")))
with open(os.path.join(RDIR, "MOTION_OPERATION_TAXONOMY.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Operation", "Events", "Videos_With_Operation", "Videos_Denominator_Validated", "Total_Frames_In_Events", "High_Confidence_Events", "Method_Class_Counts", "CapCut", "2D_Layer", "MotionGraphics", "SVG_Canvas", "FrameByFrame", "ImageToVideo_Needed", "Example_High_Confidence_Refs", "Evidence_Note"])
    for op, o in sorted(ops.items(), key=lambda kv: -kv[1]["events"]):
        t = o["tool"]
        w.writerow([op, o["events"], len(o["videos"]), len(valid), o["frames"], o["conf"].get("HIGH", 0), dict(o["class"]).__repr__(), *t, "; ".join(o["examples"]),
                    "Counts are labelled events in %d validated videos (depth-mixed); tool columns are plausibility, not the creator's software" % len(valid)])
json.dump({"measured_easing_fits": {"%s/%s" % k: v for k, v in meas.items()}}, open(os.path.join(RDIR, "evidence", "measured_easing_summary.json"), "w"), indent=1)

# assets
fam = defaultdict(lambda: {"app": 0, "videos": set(), "ids": defaultdict(set), "variants": Counter(), "roles": Counter(), "layer": "", "reuse": "", "seconds": 0.0})
for v in valid:
    for r in csv.DictReader(open(os.path.join(RDIR, "videos", v, "ASSET_APPEARANCES.csv"))):
        a = fam[r["Family"]]
        a["app"] += 1
        a["videos"].add(v)
        a["ids"][r["Asset_ID"]].add(v)
        a["variants"][r["Variant"]] += 1
        a["roles"][r["Role"]] += 1
        a["layer"] = r["Layer_Requirements"]
        a["reuse"] = r["Reusability_Across_Topics"]
        a["seconds"] += float(r["On_Screen_S"])
with open(os.path.join(RDIR, "ASSET_FAMILY_LIBRARY.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Asset_Family", "Appearances", "Videos_With_Family", "Videos_Denominator_Validated", "Distinct_Asset_IDs", "IDs_Seen_In_2plus_Videos", "Top_IDs_By_Video_Count", "On_Screen_Seconds_Sum", "Common_Roles", "Layer_Requirements", "Reusability_Across_Topics", "Evidence_Note"])
    for fm, a in sorted(fam.items(), key=lambda kv: -kv[1]["app"]):
        multi = [(i, len(vs)) for i, vs in a["ids"].items() if len(vs) >= 2]
        top = sorted(((i, len(vs)) for i, vs in a["ids"].items()), key=lambda x: -x[1])[:5]
        w.writerow([fm, a["app"], len(a["videos"]), len(valid), len(a["ids"]), len(multi), "; ".join("%s(%d)" % x for x in top), round(a["seconds"], 1),
                    "; ".join("%s(%d)" % x for x in a["roles"].most_common(4)), a["layer"], a["reuse"],
                    "Asset IDs are analyst labels assigned per video; cross-video ID matches indicate the same visual family/character as judged by the reviewer, not a verified identical file. Do not copy source pixels."])

vj = {"generated": "2026-10-20", "validated_videos": valid, "failed_validation": invalid, "validated_count": len(valid), "local_unique_videos": 48, "public_videos": 210,
      "claim": "NOT 100 PERCENT COMPLETE: %d of 48 local videos have per-video forensics; all remain audio-listening BLOCKED and single-reviewer" % len(valid),
      "depth_mix": dict(Counter(r["Depth"] for r in rows)), "layout_mix": dict(Counter(r["Layout_Era"] for r in rows)),
      "per_video_checks": {v: json.load(open(os.path.join(RDIR, "videos", v, "QA.json")))["checks"] for v in vids},
      "known_limitations": ["No direct audio listening", "Single reviewer; no independent visual QA for this phase", "Depth C videos keep UNRESOLVED_CHANGE rows", "Analysis resolution 180 px short side; 20 of 38 Shorts are 360p sources",
                            "Population claims limited to 48 local videos of 210 public", "Prior Oct-12 corpus (16 videos) is reference evidence, not merged into these tables"]}
json.dump(vj, open(os.path.join(RDIR, "VALIDATION.json"), "w"), indent=1)
print(len(valid), "valid;", invalid, "invalid;", "ops", len(ops), "families", len(fam))
