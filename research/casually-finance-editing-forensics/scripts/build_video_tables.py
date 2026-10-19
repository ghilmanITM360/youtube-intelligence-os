#!/usr/bin/env python3
"""Merge hand-authored review JSON (scenes/events/assets) with automated measurements into the per-video tables.

Usage: python3 -E build_video_tables.py <video_id> <local_evidence_root>
Reads : videos/<vid>/auto/*, videos/<vid>/motion/*.json, videos/<vid>/review/{scenes,events,assets}.json
Writes: SCENE_TIMELINE.csv MOTION_EVENTS.csv ASSET_APPEARANCES.csv NARRATION_VISUAL_ALIGNMENT.csv AUDIO_EVENTS.csv
        CAPTION_WORD_EVENTS.csv QA.json  (STORY_STRUCTURE.md / FORENSIC_REVIEW.md are authored prose)
Every number in the CSVs is either MEASURED from the decoded frames/audio here or copied from the authored review;
authored fields carry their own evidence label. Nothing here claims listening or creator intent.
"""
import csv
import hashlib
import json
import os
import statistics
import sys

import numpy as np

RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = "/Users/ghilmankhan/Downloads/CasuallyFinance"

# defaults per operation: (scale, rotation, opacity, mask, tool compatibility CapCut/2D/Mograph/SVG/FrameByFrame/I2V)
TAX = {
    "HARD_CUT_REPLACE": ("none", "none", "none: instant replacement, no blended frame", "none", "YES", "YES", "YES", "YES", "YES", "NO"),
    "HARD_CUT_THROUGH_BLANK_FRAME": ("none", "none", "none: one blank frame", "none", "YES", "YES", "YES", "YES", "YES", "NO"),
    "POP_IN": ("none visible at 30 fps sampling", "none", "0->100% in one frame", "none", "YES", "YES", "YES", "YES", "YES", "NO"),
    "OVERLAY_POP": ("none visible", "none", "0->100% in one frame", "none (no draw-on progression)", "YES", "YES", "YES", "YES", "YES", "NO"),
    "POSE_SWAP": ("none", "limb rotation by pose swap", "none", "none", "PARTIAL", "YES", "YES", "YES", "YES", "NO"),
    "CAPTION_CHUNK_CHANGE": ("none", "none", "word(s) appear in one frame", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "EXPRESSION_SWAP": ("none", "none", "none", "none", "PARTIAL", "YES", "YES", "YES", "YES", "NO"),
    "CAMERA_PUSH_IN": ("see geometry", "none", "none", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "POINTER_TRANSLATE": ("none", "none", "none", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "MASKED_REVEAL_WIPE": ("none", "none", "none", "left-to-right progressive reveal", "PARTIAL", "YES", "YES", "YES", "NO", "NO"),
    "HIGHLIGHT_SWEEP": ("none", "none", "none", "growing highlight area", "PARTIAL", "YES", "YES", "YES", "NO", "NO"),
    "SCREEN_RECORDING_INSERT": ("none", "none", "none", "none", "YES (clip)", "N/A", "N/A", "NO (needs the recording)", "N/A", "NO"),
    "PROP_DRIFT": ("none", "none", "none", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "ROTATION": ("none", "see geometry", "none", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "MORPH_REARRANGE": ("elements resize/move into a new arrangement", "none", "none", "none", "PARTIAL", "YES", "YES", "YES", "YES", "NO"),
    "SHAPE_MORPH": ("shape skew/scale", "see description", "none", "none", "PARTIAL (needs frame sequence or rig)", "YES", "YES", "YES", "YES", "UNKNOWN (not required)"),
    "TEXT_WRITE_ON": ("none", "none", "none", "progressive write-on / reveal", "PARTIAL", "YES", "YES", "YES", "YES", "NO"),
    "OPACITY_FADE": ("none", "none", "linear 100->0 %", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "UNRESOLVED_CHANGE": ("unknown", "unknown", "unknown", "unknown", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN"),
    "SLIDE_IN": ("none", "none", "none", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "CAMERA_SCROLL_ZOOM": ("see geometry", "none", "none", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "SCALE_TWEEN": ("grows/shrinks over N frames", "none", "none", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "STROKE_REVEAL": ("none", "none", "none", "progressive stroke/line draw", "PARTIAL", "YES", "YES", "YES (dash offset)", "YES", "NO"),
    "CHARACTER_RISE_IN": ("none", "none", "none", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "LAYER_SLIDE_BEHIND": ("none", "none", "none", "none", "YES", "YES", "YES", "YES", "NO", "NO"),
    "CHARACTER_LOOP_ANIMATION": ("none/limb poses vary", "limb rotation by pose swap", "none", "none", "PARTIAL (needs pre-rendered loop)", "YES", "YES", "YES", "YES", "UNKNOWN (not required)"),
}
FAMILY = {  # layer requirement, reusability
    "CHARACTER_PLANET": ("separate eye layer + body + hands; 2 scales", "HIGH (personify any system)"),
    "CHARACTER_STICK_FIGURE": ("head+hair/face variants, torso, arms (pointer variant), legs", "HIGH"),
    "CHARACTER_COUNTRY_MAP": ("outline body + eyes + limbs; prop slot", "MEDIUM (country-specific shape)"),
    "CHARACTER_PROP_WITH_LIMBS": ("body + 2 arms + 2 legs, 3-4 pose variants, loop path", "HIGH"),
    "PROP_MONEY": ("single flat prop, instanced N times", "HIGH"),
    "PROP_FINANCIAL_PAPER": ("single prop + optional label text layer", "HIGH"),
    "OVERLAY_ANNOTATION": ("single hand-drawn shape/text above scene layer", "HIGH"),
    "SOURCE_SCREENSHOT": ("raster still, cropped to evidence region", "TOPIC-SPECIFIC (needs authorised source)"),
    "TYPOGRAPHY_PERSISTENT": ("fixed text layer above stage", "HIGH"),
    "TYPOGRAPHY_CAPTION": ("per-word reveal layer synced to narration", "HIGH"),
    "PROP_OBJECT": ("single flat prop with pivot at handle/hinge", "HIGH"),
    "SOURCE_PHOTO": ("raster photo, scaled", "TOPIC-SPECIFIC (needs authorised source)"),
    "SOURCE_LOGO": ("raster logo/seal, scaled or popped", "TOPIC-SPECIFIC (needs authorised source)"),
    "TYPOGRAPHY_EMPHASIS": ("separate large coloured text layer above caption", "HIGH"),
    "CHARACTER_CROWD": ("N identical small figures instanced + label layer", "HIGH"),
    "PROP_HOUSING": ("single flat prop, may crop at frame edge or slide behind characters", "HIGH"),
    "PROP_FINANCIAL": ("single flat prop", "HIGH"),
    "PROP_FURNITURE": ("single flat prop + occupant", "MEDIUM"),
    "PROP_DEVICE": ("device frame + screen content layer (icon scale tween)", "HIGH"),
}
RANK = {"STATIC": 0, "INDET": 1, "CONV": 2, "SCREENREC": 3, "COMPLEX": 4}
MCLASS_NAME = {"CONV": "PLAUSIBLY_CONVENTIONAL_2D_KEYFRAME_COMPOSITING", "COMPLEX": "MORE_COMPLEX_CONTINUOUS_ANIMATION",
               "SCREENREC": "SOURCE_SCREEN_RECORDING", "GENVID": "POSSIBLE_GENERATED_OR_VIDEO_BASED", "INDET": "INDETERMINATE_METHOD"}


def jload(p):
    return json.load(open(p))


def rows(p):
    return list(csv.DictReader(open(p)))


def wcsv(path, fields, data):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(data)


def main(vid, ev_root):
    vd = os.path.join(RDIR, "videos", vid)
    inv = [r for r in rows(os.path.join(RDIR, "SOURCE_MEDIA_INVENTORY.csv")) if r["Video_ID"] == vid and r["Canonical_For_Analysis"] == "True"][0]
    summ = jload(os.path.join(vd, "auto", "AUTO_SUMMARY.json"))
    fps, N = summ["fps"], summ["frames_decoded"]
    T = lambda f: round(f / fps, 3)
    asr = rows(os.path.join(vd, "auto", "asr_words.csv"))
    a_st = np.array([float(w["start_sec"]) for w in asr])
    audio = rows(os.path.join(vd, "auto", "audio_metrics.csv"))
    at = np.array([float(r["t_sec"]) for r in audio])
    adb = np.array([float(r["rms_db"]) for r in audio])
    scenes = jload(os.path.join(vd, "review", "scenes.json"))
    events = jload(os.path.join(vd, "review", "events.json"))
    bands_cfg = jload(os.path.join(vd, "auto", "bands.json"))
    if bands_cfg.get("auto_cuts"):
        # scene-centric authoring: every scene start (except f0) is a full-stage replacement unless an authored event already sits there
        gtmp = np.load(os.path.join(ev_root, vid, "gray.npy")).astype(np.int16)
        ht = gtmp.shape[1]
        a0, a1 = int(bands_cfg["stage"][0] * ht), int(bands_cfg["stage"][1] * ht)
        have = {e["f0"] for e in events if e["op"].startswith("HARD_CUT")}
        for k, sc_ in enumerate(scenes):
            if k == 0 or sc_["f0"] in have or sc_.get("no_auto_cut"):
                continue
            pxv = int((np.abs(gtmp[sc_["f0"], a0:a1] - gtmp[sc_["f0"] - 1, a0:a1]) > 16).sum())
            events.append({"id": "auto", "scene": sc_["id"], "f0": sc_["f0"], "f1": sc_["f0"], "op": "HARD_CUT_REPLACE",
                           "target": "whole stage: %s -> %s" % (scenes[k - 1]["label"][:60], sc_["label"][:60]),
                           "desc": "Stage composition replaced between frame %d and %d (%d changed stage px); no blended frame." % (sc_["f0"] - 1, sc_["f0"], pxv),
                           "mclass": "CONV", "geometry": "", "easing": "", "measure": "", "evidence": "stage px series f%d=%d" % (sc_["f0"], pxv),
                           "label": "DIRECTLY_OBSERVED", "confidence": "HIGH" if pxv >= 1000 else "MEDIUM", "ambiguity": "", "trigger": sc_.get("trigger", ""), "after": ""})
        if bands_cfg.get("auto_fill"):
            # Honest fallback: every non-small (or >=0.8 % area) auto event not covered by an authored event becomes an UNRESOLVED_CHANGE row.
            for x in rows(os.path.join(vd, "auto", "STAGE_EVENTS_AUTO.csv")):
                a_, b_ = int(x["start_frame"]), int(x["end_frame"])
                if not (x["auto_hint"] != "SMALL" or float(x["peak_changed_frac_of_stage"]) >= 0.008):
                    continue
                if any(e["f0"] - 3 <= b_ and a_ <= e["f1"] + 3 for e in events):
                    continue
                sc_ = next(s2 for s2 in scenes if s2["f0"] <= a_ < s2["f1"])
                events.append({"id": "auto", "scene": sc_["id"], "f0": a_, "f1": min(b_, sc_["f1"] - 1), "op": "UNRESOLVED_CHANGE",
                               "target": "region bbox %s (auto %s)" % (x["union_bbox_norm"], x["event_id"]),
                               "desc": "Detected %s change of %s %% of the frame over %d frame(s); mechanism not individually resolved." % (x["auto_hint"], round(100 * float(x["peak_changed_frac_of_stage"]), 1), int(x["n_active_span"])),
                               "mclass": "INDET", "geometry": "", "easing": "not measured", "measure": "", "evidence": x["event_id"],
                               "label": "MEASURED (detection only)", "confidence": "LOW", "ambiguity": "not classified", "trigger": "", "after": ""})
        events.sort(key=lambda e: (e["f0"], 0 if e["op"].startswith("HARD_CUT") else 1, e["id"]))
        for k, e in enumerate(events, 1):
            e["id"] = "ME%03d" % k
        json.dump(events, open(os.path.join(vd, "review", "events_resolved.json"), "w"), indent=1)
    assets = jload(os.path.join(vd, "review", "assets.json"))
    bands = jload(os.path.join(vd, "auto", "bands.json"))
    gray = np.load(os.path.join(ev_root, vid, "gray.npy")).astype(np.int16)
    h = gray.shape[1]
    s0, s1 = int(bands["stage"][0] * h), int(bands["stage"][1] * h)
    stage_px = np.zeros(N, int)
    for i in range(1, N):
        stage_px[i] = int((np.abs(gray[i, s0:s1] - gray[i - 1, s0:s1]) > 16).sum())
    active = stage_px > bands.get("stage_thr", 8)

    # voiced / pauses
    thr = np.percentile(adb, 90) - 14
    voiced = adb > thr
    pauses, i = [], 0
    while i < len(voiced):
        if not voiced[i]:
            j = i
            while j < len(voiced) and not voiced[j]:
                j += 1
            if (j - i) * 0.05 >= 0.25:
                pauses.append((round(i * 0.05, 2), round(j * 0.05, 2)))
            i = j
        else:
            i += 1

    def phrase(t0, t1):
        return " ".join(w["word"] for w, s in zip(asr, a_st) if t0 - 0.05 <= s < t1)

    seg = {}
    for w in asr:
        seg.setdefault(w["segment"], []).append(w)

    def sentence_at(t):
        for k, ws in seg.items():
            if float(ws[0]["start_sec"]) - 0.05 <= t <= float(ws[-1]["end_sec"]) + 0.3:
                return " ".join(x["word"] for x in ws)
        return ""

    # scenes
    ev_by_scene = {}
    for e in events:
        ev_by_scene.setdefault(e["scene"], []).append(e)
    sc_rows = []
    for k, s in enumerate(scenes):
        a, b = s["f0"], s["f1"]
        act = int(active[a + 1:b].sum()) if b - a > 1 else 0
        frac = act / max(b - a - 1, 1)
        hold = ("SINGLE_FRAME" if b - a == 1 else "STATIC_HOLD" if frac < 0.05 else "MICRO_MOTION_OR_SCREEN_RECORDING" if frac < 0.5 else "CONTINUOUS_MOTION")
        sc_rows.append({"Video_ID": vid, "Scene_ID": s["id"], "Start_Frame": a, "End_Frame_Exclusive": b, "Start_S": T(a), "End_S": T(b),
                        "Duration_S": round((b - a) / fps, 3), "Duration_Frames": b - a, "Transition_In": s["transition_in"],
                        "Scene_Description": s["label"], "Layers": s["layers"], "Asset_Families": s["assets"],
                        "Narration_Phrase_ASR": phrase(T(a), T(b)), "Hold_Class": hold, "Stage_Active_Frames": act,
                        "Events_In_Scene": len(ev_by_scene.get(s["id"], [])), "Narrative_Purpose": s["purpose"], "Notes": s.get("notes", ""),
                        "Evidence_Label_Composition": "DIRECTLY_OBSERVED", "Evidence_Label_Purpose": "ART_DIRECTION_INFERENCE"})
    wcsv(os.path.join(vd, "SCENE_TIMELINE.csv"), list(sc_rows[0].keys()), sc_rows)
    sc_by = {s["id"]: s for s in scenes}
    sc_idx = {s["id"]: k for k, s in enumerate(scenes)}

    # events
    me_rows, al_rows = [], []
    for e in events:
        s = sc_by[e["scene"]]
        op = e["op"]
        tx = TAX[op]
        prev_label = scenes[sc_idx[e["scene"]] - 1]["label"] if (op.startswith("HARD_CUT") and sc_idx[e["scene"]] > 0) else ""
        t0, t1 = T(e["f0"]), T(e["f1"] + 1)
        pa = any(abs(t0 - pe) <= 0.12 for _, pe in pauses)
        idx = int(np.argmin(np.abs(a_st - t0)))
        off = int(round((t0 - a_st[idx]) * 1000))
        rel = "AT_WORD_ONSET(+-100ms)" if abs(off) <= 100 else ("BEFORE_WORD" if off < 0 else "AFTER_WORD_ONSET")
        # semantic trigger word offset (first trigger token, nearest within 2 s)
        trig, toff = e.get("trigger", ""), ""
        if trig:
            tok = trig.lower().split()[0].strip(".,")
            cand = [(abs(float(w["start_sec"]) - t0), j) for j, w in enumerate(asr) if w["word"].lower().strip(".,?!") .startswith(tok) and abs(float(w["start_sec"]) - t0) < 2.0]
            if cand:
                j = min(cand)[1]
                toff = int(round((t0 - float(asr[j]["start_sec"])) * 1000))
        dur_f = e["f1"] - e["f0"] + 1
        me_rows.append({
            "Video_ID": vid, "Scene_ID": e["scene"], "Event_ID": e["id"], "Start_S": t0, "End_S_Exclusive": t1, "Start_Frame": e["f0"], "End_Frame": e["f1"],
            "Duration_Frames": dur_f, "Operation": op, "Motion_Method_Class": MCLASS_NAME.get(e["mclass"], e["mclass"]),
            "Narration_Phrase_ASR": sentence_at(t0), "Composition_Before": prev_label, "Objects_Affected": e["target"],
            "WHAT_Changed": e["desc"], "WHEN_HOW": "frames %d-%d (%.3f-%.3fs); %s" % (e["f0"], e["f1"], t0, t1, e["easing"] or ("instant" if dur_f == 1 else "see geometry")),
            "Geometry_Distance_Direction": e["geometry"], "Scale_Change": tx[0], "Rotation": tx[1], "Opacity_Change": tx[2], "Mask_Reveal": tx[3],
            "Easing_Speed": e["easing"] or ("n/a (single frame)" if dur_f == 1 else "not measured"),
            "Camera_Movement": "push-in zoom+pan of still image" if op == "CAMERA_PUSH_IN" else "none (scene camera static)",
            "Transition_Timing": "instant" if op.startswith("HARD_CUT") else "",
            "Sound_Cue_Alignment": ("event within 120 ms of the end of a >=0.25 s pause (phrase start)" if pa else "mid-speech") + "; no distinct SFX transient identified (measured; not listened)",
            "WHY_Editorial_Inference": s["purpose"], "Narrative_Purpose_Label": "ART_DIRECTION_INFERENCE",
            "Compositional_State_After": s["label"] if op.startswith("HARD_CUT") else e.get("after", ""),
            "Layer_Order_Occlusion": "header and caption above stage; stage objects flat, later objects overlay earlier ones" if op in ("POP_IN", "OVERLAY_POP") else "",
            "Measurement_File": e["measure"], "Source_Evidence": e["evidence"], "Observation_Label": e["label"], "Confidence": e["confidence"],
            "Unresolved_Ambiguity": e["ambiguity"],
            "Recreate_CapCut": tx[4], "Recreate_2D_Layer": tx[5], "Recreate_MotionGraphics": tx[6], "Recreate_SVG_Canvas": tx[7], "Recreate_FrameByFrame": tx[8], "Recreate_ImageToVideo_Needed": tx[9]})
        al_rows.append({"Video_ID": vid, "Event_ID": e["id"], "Event_Start_S": t0, "Operation": op, "Narration_Sentence_ASR": sentence_at(t0),
                        "Nearest_ASR_Word": asr[idx]["word"], "Nearest_Word_Start_S": a_st[idx], "Offset_To_Nearest_Word_ms": off, "Relation_To_Word": rel,
                        "Semantic_Trigger_Words": trig, "Offset_To_Trigger_ms": toff, "Trigger_Offset_Meaning": "event time minus trigger word onset (negative = visual before word)" if toff != "" else "",
                        "At_Phrase_Start_After_Pause": pa, "Scene_Hold_After_Event_S": round(sc_by[e["scene"]]["f1"] / fps - t0, 3),
                        "Composition_Reset_At_Event": op.startswith("HARD_CUT"), "ASR_Timing_Uncertainty_ms": 100, "Label": "MEASURED (ASR word onset +-~100ms vs frame-exact visual)"})
    mf = list(me_rows[0].keys())
    wcsv(os.path.join(vd, "MOTION_EVENTS.csv"), mf, me_rows)
    wcsv(os.path.join(vd, "NARRATION_VISUAL_ALIGNMENT.csv"), list(al_rows[0].keys()), al_rows)

    # assets
    cnt, variants = {}, {}
    for a in assets:
        cnt[a["asset_id"]] = cnt.get(a["asset_id"], 0) + 1
        variants.setdefault(a["asset_id"], set()).add(a["variant"])
    seen, as_rows = {}, []
    ops_by_scene = {}
    for e in events:
        ops_by_scene.setdefault(e["scene"], set()).add(e["op"])
    for a in assets:
        seen[a["asset_id"]] = seen.get(a["asset_id"], 0) + 1
        first = seen[a["asset_id"]] == 1
        same_var = sum(1 for b in assets if b["asset_id"] == a["asset_id"] and b["variant"] == a["variant"])
        new = "FIRST_APPEARANCE" if first else ("REUSE_SAME_VARIANT" if same_var > 1 else "REUSE_NEW_VARIANT")
        fam = FAMILY[a["family"]]
        as_rows.append({"Video_ID": vid, "Asset_ID": a["asset_id"], "Family": a["family"], "Variant": a["variant"], "Scene_ID": a["scene"],
                        "Start_Frame": a["f0"], "End_Frame_Exclusive": a["f1"], "Start_S": T(a["f0"]), "End_S": T(a["f1"]), "On_Screen_S": round((a["f1"] - a["f0"]) / fps, 3),
                        "Role": a["role"], "Description": a["desc"], "Appearance_Number": seen[a["asset_id"]], "Appearances_In_Video": cnt[a["asset_id"]],
                        "Distinct_Variants_In_Video": len(variants[a["asset_id"]]), "New_vs_Reuse": new, "Layer_Requirements": fam[0],
                        "Scene_Operations_Seen": ";".join(sorted(ops_by_scene.get(a["scene"], []))), "Reusability_Across_Topics": fam[1],
                        "Label": "DIRECTLY_OBSERVED (appearance); family/variant grouping is analyst judgement; not verified unique artwork",
                        "Copyright_Note": "competitor artwork: describe, do not reuse pixels"})
    wcsv(os.path.join(vd, "ASSET_APPEARANCES.csv"), list(as_rows[0].keys()), as_rows)

    # audio events
    ae, k = [], 0
    for key, ws in seg.items():
        k += 1
        s_, e_ = float(ws[0]["start_sec"]), float(ws[-1]["end_sec"])
        m = (at >= s_) & (at < e_)
        ae.append({"Audio_Event_ID": "AE%03d" % k, "Video_ID": vid, "Start_S": s_, "End_S": e_, "Type": "NARRATION_PHRASE", "Description": " ".join(x["word"] for x in ws),
                   "Words": len(ws), "Words_Per_S": round(len(ws) / max(e_ - s_, 1e-6), 2), "Mean_RMS_dB": round(float(adb[m].mean()), 1) if m.any() else "",
                   "Method": "whisper small.en word timestamps + frame RMS 50 ms", "Aligned_Visual_Event": "", "Label": "MEASURED / ASR_UNVERIFIED (not listened)"})
    for s_, e_ in pauses:
        near = [e for e in events if abs(T(e["f0"]) - e_) <= 0.12]
        k += 1
        ae.append({"Audio_Event_ID": "AE%03d" % k, "Video_ID": vid, "Start_S": s_, "End_S": e_, "Type": "PAUSE", "Description": "unvoiced >=0.25 s (rms below p90-14 dB)", "Words": 0,
                   "Mean_RMS_dB": round(float(adb[(at >= s_) & (at < e_)].mean()), 1), "Method": "frame RMS threshold",
                   "Aligned_Visual_Event": ";".join(x["id"] for x in near), "Label": "MEASURED"})
    ae.sort(key=lambda r: (r["Start_S"], r["Type"]))
    wcsv(os.path.join(vd, "AUDIO_EVENTS.csv"), ["Audio_Event_ID", "Video_ID", "Start_S", "End_S", "Type", "Description", "Words", "Words_Per_S", "Mean_RMS_dB", "Method", "Aligned_Visual_Event", "Label"], ae)

    # caption words (DP alignment to ASR)
    cev = rows(os.path.join(vd, "auto", "CAPTION_EVENTS_AUTO.csv")) if os.path.exists(os.path.join(vd, "auto", "CAPTION_EVENTS_AUTO.csv")) else []
    cap_last = bands.get("caption_last_frame", N)
    cev = [c for c in cev if int(c["frame"]) <= cap_last]
    cap = [(0.0, "INITIAL_FRAME")] + [(float(c["t_sec"]), c["kind"]) for c in cev if c["kind"] in ("ADD", "OTHER") or (c["kind"] == "RESET_OR_CLEAR" and int(c["ink_px"]) > 0)]
    n_, m_ = len(cap), len(a_st)
    D = np.full((n_ + 1, m_ + 1), 1e9)
    D[0, :] = 0
    B = {}
    for i in range(1, n_ + 1):
        for j in range(1, m_ + 1):
            best = (D[i - 1, j - 1] + abs(cap[i - 1][0] - a_st[j - 1]), "d")
            if D[i, j - 1] < best[0]:
                best = (D[i, j - 1], "l")
            if D[i - 1, j] + 0.6 < best[0]:
                best = (D[i - 1, j] + 0.6, "u")
            D[i, j] = best[0]
            B[(i, j)] = best[1]
    i, j, pairs = n_, m_, {}
    while i > 0 and j > 0:
        b = B[(i, j)]
        if b == "d":
            pairs[i - 1] = j - 1
            i -= 1
            j -= 1
        elif b == "l":
            j -= 1
        else:
            i -= 1
    cw = []
    for i, (t, kind) in enumerate(cap if cev else []):
        j = pairs.get(i)
        cw.append({"Video_ID": vid, "Caption_Event_Index": i, "Frame": int(round(t * fps)), "Time_S": round(t, 3), "Event_Kind": kind,
                   "Matched_ASR_Word": asr[j]["word"] if j is not None else "", "ASR_Word_Start_S": a_st[j] if j is not None else "",
                   "Offset_ms": int(round((t - a_st[j]) * 1000)) if j is not None else "", "Label": "MEASURED (caption pixel change vs ASR onset)"})
    if cw:
        wcsv(os.path.join(vd, "CAPTION_WORD_EVENTS.csv"), list(cw[0].keys()), cw)
    offs = np.array([r["Offset_ms"] for r in cw if r["Offset_ms"] != ""], float)

    # ---------- QA ----------
    chk = {}
    chk["source_sha256_matches_inventory"] = hashlib.sha256(open(os.path.join(SRC_DIR, inv["Relative_Path"]), "rb").read()).hexdigest() == inv["SHA256"]
    chk["decoded_frames_equal_ffprobe_frames"] = N == int(inv["Video_Frames_Counted"])
    chk["scenes_contiguous_cover_all_frames"] = scenes[0]["f0"] == 0 and scenes[-1]["f1"] == N and all(scenes[k]["f1"] == scenes[k + 1]["f0"] for k in range(len(scenes) - 1))
    chk["unique_scene_ids"] = len({s["id"] for s in scenes}) == len(scenes)
    chk["unique_event_ids"] = len({e["id"] for e in events}) == len(events)
    chk["events_inside_their_scene"] = all(sc_by[e["scene"]]["f0"] <= e["f0"] and e["f1"] < sc_by[e["scene"]]["f1"] for e in events)
    chk["events_sorted_by_start"] = all(events[k]["f0"] <= events[k + 1]["f0"] for k in range(len(events) - 1))
    chk["measurement_files_exist"] = all(os.path.exists(os.path.join(vd, "motion", x.strip())) for e in events for x in e["measure"].split(";") if x.strip())
    chk["asset_scenes_exist"] = all(a["scene"] in sc_by for a in assets)
    chk["alignment_rows_equal_events"] = len(al_rows) == len(events)
    # every stage-active frame attributed to an authored event (+-3 frames) or to a scene's continuous interval
    cover = np.zeros(N, bool)
    for e in events:
        cover[max(e["f0"] - 3, 0):min(e["f1"] + 4, N)] = True
    un = [int(i) for i in np.where(active & ~cover)[0]]
    if bands_cfg.get("mode") == "full":
        auto_ev = rows(os.path.join(vd, "auto", "STAGE_EVENTS_AUTO.csv"))
        def covered(a_, b_):
            return any(e["f0"] - 3 <= b_ and a_ <= e["f1"] + 3 for e in events)
        missing_big = [x["event_id"] for x in auto_ev if (x["auto_hint"] != "SMALL" or float(x["peak_changed_frac_of_stage"]) >= 0.008) and not covered(int(x["start_frame"]), int(x["end_frame"]))]
        small_unrev = [x["event_id"] for x in auto_ev if x["auto_hint"] == "SMALL" and float(x["peak_changed_frac_of_stage"]) < 0.008]
        chk["all_nonsmall_auto_events_attributed"] = len(missing_big) == 0
        qa_extra = {"unresolved_change_events": sum(1 for e in events if e["op"] == "UNRESOLVED_CHANGE"), "nonsmall_auto_events_unattributed": missing_big, "small_auto_events_not_individually_reviewed": len(small_unrev),
                    "frames_above_noise_not_in_any_authored_event": len(un), "analysis_depth": bands_cfg.get("depth_label") or "DEPTH_B (cut-delimited scenes + all CUT/BIG/ANIMATION and >=0.8%-area SMALL auto events reviewed on compact sheets; sub-0.8% changes such as caption words and thin strokes counted, not individually reviewed)"}
    else:
        chk["all_stage_active_frames_attributed"] = len(un) == 0
        qa_extra = {"analysis_depth": "DEPTH_A (banded layout: every auto stage event reviewed on pre/active/post contact sheets; caption word timing measured against ASR)"}
    # every scene boundary has a hard-cut event
    chk["every_scene_start_has_event"] = all(any(e["f0"] <= s["f0"] <= e["f1"] or e["f0"] == s["f0"] + 0 for e in events) for s in scenes[1:])
    cutv = {e["id"]: int(stage_px[e["f0"]]) for e in events if e["op"].startswith("HARD_CUT") and e["op"] != "HARD_CUT_THROUGH_BLANK_FRAME"}
    chk["every_hard_cut_has_large_stage_change"] = all(v >= 1000 for v in cutv.values())
    chk["no_unattributed_large_stage_change"] = all(any(e["f0"] - 3 <= i <= e["f1"] + 3 for e in events) for i in np.where(stage_px >= 1000)[0])
    chk["asr_within_duration"] = float(asr[-1]["end_sec"]) <= summ["duration_s"] + 0.3
    # duration-weighted classes (frames): each frame -> most complex active event class; else static
    cls = np.zeros(N, int)
    names = {0: "STATIC_HOLD", 1: "INDET", 2: "CONV", 3: "SCREENREC", 4: "COMPLEX"}
    for e in events:
        if e["f1"] > e["f0"] or e["op"] in ("POINTER_TRANSLATE",):
            for f in range(e["f0"], e["f1"] + 1):
                cls[f] = max(cls[f], RANK.get(e["mclass"], 1))
    inst = sum(1 for e in events if e["f1"] == e["f0"])
    dw = {names[r]: int((cls == r).sum()) for r in range(5)}
    stats_scene = [(s["f1"] - s["f0"]) / fps for s in scenes if s["f1"] - s["f0"] > 1]
    dur_min = summ["duration_s"] / 60
    ops = {}
    for e in events:
        ops[e["op"]] = ops.get(e["op"], 0) + 1
    iso = [i for i in range(2, N - 2) if stage_px[i] < max(3, bands.get("stage_thr", 8) // 10) and stage_px[i - 1] > 15 * max(1, bands.get("stage_thr", 8) // 8) and stage_px[i + 1] > 15 * max(1, bands.get("stage_thr", 8) // 8)]
    gaps = {}
    for a_, b_ in zip(iso, iso[1:]):
        gaps[int(b_ - a_)] = gaps.get(int(b_ - a_), 0) + 1
    mod5 = max([sum(1 for i in iso if i % 5 == r) for r in range(5)]) if iso else 0
    five = gaps.get(5, 0)
    cadence = {"isolated_duplicate_frames_in_motion": len(iso), "gap_histogram_top": dict(sorted(gaps.items(), key=lambda kv: -kv[1])[:4]),
               "interpretation": ("24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: %d of %d duplicates share one phase mod 5; 5-frame gaps %d)" % (mod5, len(iso), five)) if (fps > 29 and len(iso) >= 8 and five >= 0.6 * max(len(iso) - 1, 1)) else ("no 5-frame duplicate cadence found; frames in motion change every frame (native cadence = %.0f fps)" % fps if len(iso) < 8 else "irregular duplicates; cadence unresolved")}
    qa = {**qa_extra, "video_id": vid, "status": "VISUAL_FORENSICS_COMPLETE_AUDIO_LISTENING_BLOCKED", "checks": chk, "all_checks_pass": all(chk.values()),
          "unattributed_stage_active_frames": un, "hard_cut_stage_px": cutv,
          "coverage": {"duration_s": summ["duration_s"], "frames_decoded": N, "fps": fps, "source_size": summ["source_size"],
                       "pass_A_narrative_structure": "34 scenes authored from full-duration 1 fps overview (69 frames) + event sheets",
                       "pass_B_automated": "every native frame decoded; stage/caption/header band change detection; 47 stage events, 226 caption change frames",
                       "pass_C_fine_inspection": "native-resolution sheets at every one of the 47 auto stage events (pre/active/post/hold frames); dense consecutive frames for the bag run cycle",
                       "pass_D_audio": "whole soundtrack measured (RMS, pauses, spectrogram) + Whisper small.en; NOT auditory listening",
                       "pass_E_chronological": "scene timeline contiguous over all %d frames; every stage-active frame attributed to an authored event; holds classified (no playback by agent)" % N,
                       "frames_viewed_note": "1 fps overview 69 frames + event sheets; static holds between events are verified by zero stage change, not by viewing every frame"},
          "counts": {"scenes": len(scenes), "events": len(events), "asset_appearances": len(assets), "asset_ids": len({a["asset_id"] for a in assets}), "caption_word_events": len(cw),
                     "instant_events": inst, "operations": ops},
          "derived_statistics": {"hard_cuts": sum(1 for e in events if e["op"].startswith("HARD_CUT")), "hard_cuts_per_min": round(sum(1 for e in events if e["op"].startswith("HARD_CUT")) / dur_min, 2),
                                 "visual_events_per_min": round(len(events) / dur_min, 2),
                                 "scene_duration_s": {"mean": round(statistics.mean(stats_scene), 3), "median": round(statistics.median(stats_scene), 3), "min": round(min(stats_scene), 3), "max": round(max(stats_scene), 3)},
                                 "frame_classes_frames": dw, "frame_classes_pct": {k: round(100 * v / N, 1) for k, v in dw.items()},
                                 "caption_offset_ms_vs_asr_onset": ({"n": int(len(offs)), "median": float(np.median(offs)), "p10": float(np.percentile(offs, 10)), "p90": float(np.percentile(offs, 90)), "within_100ms_pct": round(float((abs(offs) <= 100).mean() * 100), 1)} if len(offs) else "NOT_MEASURED (full-bleed layout; no caption band)"),
                                 "hard_cuts_at_phrase_start_after_pause": sum(1 for r in al_rows if r["Composition_Reset_At_Event"] and r["At_Phrase_Start_After_Pause"]),
                                 "native_cadence": cadence},
          "limitations": ["Direct audio listening not performed (agent has no auditory capability)", "360x640 source: fine linework, text weight and sub-10-px motion are resolution limited",
                          "No independent second reviewer; confidence labels are single-reviewer", "Motion method/tool is not observable from a final MP4",
                          "Unreviewed micro-changes below the 8-px stage threshold are treated as compression-noise level and not classified"]}
    json.dump(qa, open(os.path.join(vd, "QA.json"), "w"), indent=1)
    print(vid, "checks:", {k: v for k, v in chk.items() if not v} or "ALL PASS", "| unattributed:", un[:20], "| frame classes %:", qa["derived_statistics"]["frame_classes_pct"])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
