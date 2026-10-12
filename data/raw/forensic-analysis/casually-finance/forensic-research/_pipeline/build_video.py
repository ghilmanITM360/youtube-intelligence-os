"""Stage D: merge reviewed annotations + measured features into the per-video deliverable tables.
Reads  : <WORK>/<id>/{visual_auto.json,audio_auto.json,whisper.json}, <OUT>/02_VIDEO_FORENSICS/<id>/{TRANSCRIPT.csv,_SENTENCES.csv},
         <OUT>/_pipeline/annotations/<id>.txt  (+ optional beats/<id>.txt)
Writes : SHOTS/STATES/MOTIONS/ASSETS/AUDIO_EVENTS/AUDIO_VISUAL_SYNC/SEMANTIC_BEATS csv, SENTENCES.csv, SOURCE.json, QA.json, evidence/sheets
Usage  : python3 -B build_video.py <VIDEO_ID> <WORK_ROOT> <OUT_DIR>
Every number here is measured from the file; every description comes from the annotation file written while viewing the frames.
"""
import csv, json, re, shutil, sys, bisect
from collections import defaultdict, Counter
from pathlib import Path
import numpy as np

PREFIX_TYPE = [("HOST", "CHARACTER_HOST"), ("CHAR_", "CHARACTER"), ("MAP_", "CHARACTER_MAP"), ("OBJ_", "OBJECT"), ("BLDG_", "OBJECT_BUILDING"), ("ICON_", "ICON"),
               ("TXT_", "TEXT_LETTERING"), ("LOGO_", "LOGO"), ("SS_", "SCREENSHOT"), ("CHART_", "CHART"), ("IMG_", "IMAGE_STILL"), ("PHOTO_", "PHOTO"),
               ("FOOTAGE_", "VIDEO_FOOTAGE"), ("HL_", "ANNOTATION_OVERLAY"), ("UI_", "UI_OVERLAY"), ("POINTER", "PROP")]
PREFIX_TECH = {"CHARACTER_HOST": "ORIGINAL_DRAWING", "CHARACTER": "ORIGINAL_DRAWING", "CHARACTER_MAP": "ORIGINAL_DRAWING", "OBJECT": "ORIGINAL_DRAWING", "OBJECT_BUILDING": "ORIGINAL_DRAWING",
               "ICON": "ORIGINAL_DRAWING", "TEXT_LETTERING": "MOTION_GRAPHICS", "LOGO": "COMPOSITED_STILLS", "SCREENSHOT": "SCREEN_CAPTURE", "CHART": "SCREEN_CAPTURE",
               "IMAGE_STILL": "COMPOSITED_STILLS", "PHOTO": "STOCK_FOOTAGE", "VIDEO_FOOTAGE": "STOCK_FOOTAGE", "ANNOTATION_OVERLAY": "MOTION_GRAPHICS", "UI_OVERLAY": "MOTION_GRAPHICS", "PROP": "ORIGINAL_DRAWING"}
RECIPE = {  # tool-agnostic reconstruction methods keyed by the first token of the 'change' note
    "POP_IN": "Layer appears (scale/opacity entrance) within <=3 frames at its final position.", "CUT": "Hard cut: replace the whole composition on one frame.",
    "TEXT_REVEAL": "Text layer revealed in place (typed/wiped on or pop-in) while narration reaches the keyword.", "DRAW_ON": "Reveal a stroke/shape progressively along its path (trim-path / wipe mask) to imitate hand drawing.",
    "ZOOM_IN": "Scale the layer up about the focal point (keyframed scale, optional position offset).", "ZOOM_OUT": "Scale the layer down to reveal more context.", "SCROLL": "Translate a tall screenshot layer vertically behind a fixed mask.",
    "SLIDE_IN": "Translate a layer from off-frame to its resting position.", "SLIDE": "Translate a layer horizontally/vertically to a new resting position.", "HIGHLIGHT": "Overlay a highlighter-coloured rectangle that wipes left-to-right over a text line.",
    "FACE_CHANGE": "Swap the character's face art for another expression (state replacement, no tween).", "POSE_CHANGE": "Swap the character's pose art (state replacement).", "REPOSITION": "Move existing layers to new positions (re-layout).",
    "SCALE_UP": "Increase layer scale.", "SCALE_DOWN": "Decrease layer scale.", "SWAP": "Replace one asset with another in place.", "LOOP_ANIM": "Alternate two or three drawn frames on a short loop.",
    "BUILD": "Add elements one by one on successive frames to assemble a composite.", "EXIT": "Remove the layer(s) (cut or fade) leaving the rest of the composition.", "CROSSFADE": "Opacity cross-dissolve between two compositions.",
    "MORPH": "Replace a drawing with its transformed version (state swap with optional scale pulse).", "ROTATE": "Rotate a layer about a pivot.", "REFRAME": "Change framing/scale of the whole group.", "FADE_IN": "Opacity 0→100.", "HOLD": "No change.",
    "TEXT_SWAP": "Replace text content in place.", "ICON_REVEAL": "Reveal an icon inside an existing container.", "FOOTAGE_CUT": "Cut inside embedded footage (belongs to the source clip).", "FOOTAGE_ACTION": "Motion inside embedded footage.",
    "START": "Opening composition.", "CLEAR": "Remove most layers.", "UI_STATE": "Swap a UI state (e.g. Subscribe → Subscribed).", "RESET": "Clear a chart and re-animate its build.", "BUILD_COMPLETE": "Chart build reaches final state.",
    "SETTLE": "Layer comes to rest.", "STRIKE": "Overlay strike-through line.", "ANIM": "Small UI/element animation.", "MOVE": "Translate a marker to a new target.", "STACK": "Stack layers in z-order.",
    "BUBBLES_REMOVED": "Remove overlay layer.", "OBJECT_EXIT": "Remove object.", "TEXT_EXIT": "Remove text.", "FADE_IN/SLIDE_IN": "Opacity/translate entrance.", "SLIDE_UP": "Translate up into place.", "SLIDE_UP_SETTLE": "Translate up and settle.",
    "SHRINK": "Reduce scale.", "SLIDE_IN:": "Translate in.", "REPLACE": "Replace layer.", "CALLBACK": "Re-use an earlier scene.", "TEXT_SWAP+STRIKE": "Replace text and add strike-through."}


def rd(p):
    return list(csv.DictReader(open(p, newline="")))


def wr(p, rows, cols=None):
    cols = cols or list(rows[0].keys())
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)


def asset_type(k):
    for p, t in PREFIX_TYPE:
        if k.startswith(p): return t
    return "OTHER"


def main(vid, work_root, out):
    out = Path(out); work = Path(work_root) / vid; d = out / "02_VIDEO_FORENSICS" / vid
    va = json.load(open(work / "visual_auto.json")); aa = json.load(open(work / "audio_auto.json")); wj = json.load(open(work / "whisper.json"))
    z = np.load(work / "features.npz")
    meta = next(r for r in rd(out / "00_MANIFEST/SELECTED_18.csv") if r["video_id"] == vid)
    cat = next(r for r in rd(out / "01_CHANNEL_METADATA/all-videos-metadata.csv") if r["video_id"] == vid)
    words = rd(d / "TRANSCRIPT.csv"); sents = rd(d / "_SENTENCES.csv")
    fps, dur = va["fps"], va["duration"]
    wst = [float(w["start_sec"]) for w in words]; wen = [float(w["end_sec"]) for w in words]
    # ---- annotations
    ann, order, heads, cur_head = {}, [], [], None
    for ln, line in enumerate(open(out / "_pipeline/annotations" / f"{vid}.txt")):
        line = line.rstrip("\n")
        if not line or line.startswith("# "): continue
        if line.startswith("#"):
            p = line[1:].split("|"); cur_head = dict(label=p[0], purpose=p[1] if len(p) > 1 else "", tech=p[2] if len(p) > 2 else ""); heads.append(cur_head); cur_head["first_state"] = None; continue
        p = line.split("|")
        if len(p) != 6: raise SystemExit(f"annotation line {ln + 1} has {len(p)} fields: {line[:80]}")
        sid = p[0]
        if sid in ann: raise SystemExit("duplicate annotation " + sid)
        ann[sid] = dict(desc=p[1], text=p[2], layout=p[3], assets=p[4], change=p[5], head=cur_head)
        order.append(sid)
        if cur_head is not None and cur_head["first_state"] is None: cur_head["first_state"] = sid
    states_auto = {s["state_id"]: s for s in va["states"]}
    missing = [s for s in states_auto if s not in ann]; extra = [s for s in ann if s not in states_auto]
    # ---- shots from headers (a header starts a shot at its first state)
    shot_of, shots = {}, []
    for h in heads:
        if h["first_state"] is None: continue
        shots.append(dict(shot_id=f"SH{len(shots) + 1:03d}", head=h, states=[]))
    cur = None; hmap = {h["first_state"]: s for h, s in zip([h for h in heads if h["first_state"]], shots)}
    for s in va["states"]:
        if s["state_id"] in hmap: cur = hmap[s["state_id"]]
        cur["states"].append(s["state_id"]); shot_of[s["state_id"]] = cur["shot_id"]
    # ---- episodes -> target state
    eps = [e for e in va["episodes"]]
    st_list = va["states"]; st_starts = [s["start"] for s in st_list]
    ep_target = {}
    for e in eps:
        if e["cls"] == "MICRO_CHANGE": continue
        k = bisect.bisect_left(st_starts, e["t1"] - 0.05)
        if k < len(st_list): ep_target[e["ep_id"]] = st_list[k]["state_id"]
    by_target = defaultdict(list)
    for e in eps:
        if e["ep_id"] in ep_target: by_target[ep_target[e["ep_id"]]].append(e)
    # ---- assets
    first_desc, asset_states = {}, defaultdict(list)
    for sid in order:
        for tok in [t for t in ann[sid]["assets"].split(";") if t.strip()]:
            k, _, ds = tok.partition("="); k = k.strip()
            if ds and k not in first_desc: first_desc[k] = ds.strip()
            asset_states[k].append(sid)
    # ---- STATES.csv
    srows = []
    for i, s in enumerate(st_list):
        a = ann[s["state_id"]]; sh = shot_of[s["state_id"]]
        w_in = [k for k in range(len(words)) if wen[k] > s["start"] and wst[k] < s["end"]] if False else None
        i0 = bisect.bisect_left(wen, s["start"] + 1e-6); i1 = bisect.bisect_left(wst, s["end"] - 1e-6)
        wids = [words[k]["word_id"] for k in range(i0, i1)]
        narr = " ".join(words[k]["word"] for k in range(i0, min(i1, i0 + 40)))
        ent = by_target.get(s["state_id"], [])
        per_sheet = 16 if meta["height"] > meta["width"] else 12
        srows.append(dict(video_id=vid, state_id=s["state_id"], shot_id=sh, start_sec=s["start"], end_sec=s["end"], duration_sec=s["dur"], first_word_id=wids[0] if wids else "", last_word_id=wids[-1] if wids else "",
                          narration_words=narr + (" …" if i1 - i0 > 40 else ""), literal_frame_description=a["desc"], visible_text=a["text"], layout_focal_point=a["layout"], asset_ids=a["assets"].replace("=", "§").split(";") and ";".join(t.split("=")[0].strip() for t in a["assets"].split(";") if t.strip()),
                          change_entering_state=a["change"], entering_episode_ids=";".join(e["ep_id"] for e in ent), representative_frame_sec=s["rep_t"], evidence_sheet=f"evidence/sheets/sheet_{i // per_sheet + 1:03d}.jpg",
                          confidence="OBSERVED; timing from per-frame pixel-difference (±1 frame); description from reviewed frame at representative_frame_sec"))
    # ---- SHOTS.csv
    shrows = []
    for k, sh in enumerate(shots):
        first, last = states_auto[sh["states"][0]], states_auto[sh["states"][-1]]
        start = first["start"]
        # transition-in = episodes targeting the first state
        ent = by_target.get(sh["states"][0], [])
        if k == 0: tin = "START"
        elif ent:
            big = max(ent, key=lambda e: e["peak_frac"])
            tin = f"{big['cls']} measured: {big['n_frames']} frame(s), peak {100 * big['peak_frac']:.0f}% of pixels changed; reviewed: {ann[sh['states'][0]]['change']}"
        else: tin = f"NO_PIXEL_EPISODE_BEFORE_STATE; reviewed: {ann[sh['states'][0]]['change']}"
        aids = sorted({t.split("=")[0].strip() for s in sh["states"] for t in ann[s]["assets"].split(";") if t.strip()})
        mcount = sum(len(by_target.get(s, [])) for s in sh["states"][1:])
        shrows.append(dict(video_id=vid, shot_id=sh["shot_id"], start_sec=start, end_sec=None, duration_sec=None, first_state_id=sh["states"][0], last_state_id=sh["states"][-1], state_count=len(sh["states"]), motion_episode_count=mcount,
                           asset_ids=";".join(aids), narrative_purpose=sh["head"]["purpose"], technique_classes=sh["head"]["tech"], transition_in=tin, transition_out="", scene_subject=ann[sh["states"][0]]["desc"][:160],
                           confidence="OBSERVED; shot boundaries set by frame review (pixel-diff candidate boundaries used as cross-check)"))
    for k, r in enumerate(shrows):
        r["end_sec"] = shrows[k + 1]["start_sec"] if k + 1 < len(shrows) else dur
        r["duration_sec"] = round(r["end_sec"] - r["start_sec"], 3)
        r["transition_out"] = shrows[k + 1]["transition_in"].split(";")[0] if k + 1 < len(shrows) else "END"
    # ---- MOTIONS.csv: one row per target state with entering episodes
    mrows = []
    for i, s in enumerate(st_list):
        ent = by_target.get(s["state_id"], [])
        if not ent: continue
        prev = st_list[i - 1]["state_id"] if i else ""
        a = ann[s["state_id"]]; lab = re.split(r"[:+ ]", a["change"].strip())[0] if a["change"] else ""
        f0 = min(e["f0"] for e in ent); f1 = max(e["f1"] for e in ent)
        nf = sum(e["n_frames"] for e in ent); peak = max(e["peak_frac"] for e in ent); meanf = float(np.mean([e["mean_frac"] for e in ent]))
        bx0, by0, bx1, by1 = min(e["bbox_x0"] for e in ent), min(e["bbox_y0"] for e in ent), max(e["bbox_x1"] for e in ent), max(e["bbox_y1"] for e in ent)
        dx = sum(e["centroid_dx"] for e in ent); dy = sum(e["centroid_dy"] for e in ent)
        direction = "no net centroid shift" if abs(dx) < 0.02 and abs(dy) < 0.02 else (("RIGHT " if dx > 0.02 else "LEFT " if dx < -0.02 else "") + ("DOWN" if dy > 0.02 else "UP" if dy < -0.02 else "")).strip() + f" (centroid Δ {dx:+.2f},{dy:+.2f} of frame)"
        t0, t1 = f0 / fps, (f1 + 1) / fps
        speed = "instantaneous (<=2 frames)" if nf <= 2 else f"{nf} active frames over {t1 - t0:.2f}s"
        clss = Counter(e["cls"] for e in ent).most_common(1)[0][0]
        mrows.append(dict(video_id=vid, motion_id=f"M{len(mrows) + 1:04d}", shot_id=shot_of[s["state_id"]], target_shot_id=shot_of[s["state_id"]] if shot_of.get(prev) != shot_of[s["state_id"]] else shot_of[s["state_id"]],
                          source_state=prev, target_state=s["state_id"], start_sec=round(t0, 3), end_sec=round(t1, 3), duration_sec=round(t1 - t0, 3), observed_action=a["change"], action_label=lab,
                          direction_or_path=direction, speed=speed, easing="NOT_ASSESSED (cannot be separated from linear without tracked element positions)" if nf > 2 else "N/A (instantaneous)",
                          auto_episode_class=clss, episode_ids=";".join(e["ep_id"] for e in ent), active_frames=nf, peak_changed_pixel_fraction=round(peak, 4), mean_changed_pixel_fraction=round(meanf, 4),
                          changed_region_bbox_norm=f"{bx0:.2f},{by0:.2f},{bx1:.2f},{by1:.2f}", crosses_shot_boundary=shot_of.get(prev) != shot_of[s["state_id"]],
                          label_vs_measure_check=("LABEL_IMPLIES_INSTANT_BUT_>3_ACTIVE_FRAMES(may include follow-on animation)" if lab in ("CUT", "POP_IN", "FACE_CHANGE", "POSE_CHANGE", "SWAP", "TEXT_SWAP", "REFRAME", "EXIT", "REPLACE") and nf > 3 else "consistent"),
                          purpose=a["head"]["purpose"] if a["head"] else "", tool_agnostic_reconstruction_method=RECIPE.get(lab, "See observed_action; rebuild by keyframing the described layer change."),
                          confidence="MEASURED timing/region; action wording from reviewed before/after frames"))
    # ---- ASSETS.csv
    state_dur = {s["state_id"]: s["dur"] for s in st_list}
    arows = []
    for k in sorted(asset_states, key=lambda x: min(order.index(s) for s in asset_states[x])):
        sts = asset_states[k]; shs = sorted({shot_of[s] for s in sts}); t = asset_type(k)
        ds = first_desc.get(k, "")
        arows.append(dict(video_id=vid, asset_id=k, asset_type=t, description=ds, technique_class=PREFIX_TECH.get(t, "UNKNOWN"), first_state=sts[0], last_state=sts[-1], state_appearances=len(sts), shot_appearances=len(shs),
                          on_screen_seconds=round(sum(state_dur[s] for s in sts), 2), first_shot=shs[0], reuse_status="REUSED" if len(shs) > 1 else "SINGLE_SHOT",
                          source_or_recreation_method={"ORIGINAL_DRAWING": "Draw as flat-fill hand-drawn vector/raster art with irregular black outline; export transparent PNG.", "MOTION_GRAPHICS": "Typeset/animate text or UI layer in the editor.",
                                                       "COMPOSITED_STILLS": "Place a third-party logo/still as a transparent PNG layer.", "SCREEN_CAPTURE": "Screen-capture or screenshot the cited source page; crop to the relevant region; layer in editor.",
                                                       "STOCK_FOOTAGE": "Embed third-party clip/photo inside a drawn frame; keep source audio if used."}.get(PREFIX_TECH.get(t, ""), "Unknown"),
                          confidence="OBSERVED type/appearance; technique class is an appearance-based inference, not a software/artist claim"))
    # ---- SENTENCES.csv (+ keep word table)
    wr(d / "SENTENCES.csv", sents)
    # ---- AUDIO_EVENTS.csv
    arws = []
    def ae(t0, t1, typ, desc, inten, method, conf, notes=""):
        arws.append(dict(audio_event_id=f"AE{len(arws) + 1:04d}", video_id=vid, start_sec=round(t0, 3), end_sec=round(t1, 3), type=typ, description=desc, intensity_db=inten, source_method=method, confidence=conf, notes=notes))
    # narration blocks: words separated by pauses >= 0.35 s
    bstart = wst[0]; bwords = 1
    for k in range(1, len(words)):
        if wst[k] - wen[k - 1] >= 0.35:
            sl = slice(int(bstart / aa["hop_sec"]), int(wen[k - 1] / aa["hop_sec"]) + 1)
            ae(bstart, wen[k - 1], "NARRATION_PHRASE", f"voiced phrase, {bwords} word(s), {bwords / max(wen[k - 1] - bstart, 0.01):.1f} words/s", "", "WHISPER_BASE_WORD_TIMING", "HIGH(timing ±0.1s)")
            bstart, bwords = wst[k], 0
        bwords += 1
    ae(bstart, wen[-1], "NARRATION_PHRASE", f"voiced phrase, {bwords} words", "", "WHISPER_BASE_WORD_TIMING", "HIGH(timing ±0.1s)")
    for p in aa["pauses"]:
        if p["dur"] >= 0.5:
            lvl = "digital/near-digital silence" if p["rms_db_mean"] < -70 else "very low noise floor" if p["rms_db_mean"] < -50 else "audible room tone/ambience or non-speech sound"
            ae(p["start"], p["end"], "PAUSE", f"pause {p['dur']:.2f}s; {lvl}", p["rms_db_mean"], "WORD_GAP+RMS", "HIGH", f"spectral flatness {p['flatness']}")
    for o in aa["onsets"]:
        ae(o["t"], o["t"] + 0.15, "SPEECH_TRANSIENT", "strong spectral-flux onset coinciding with speech (likely plosive/emphasis, not SFX)" if o["under_speech"] else "NON_SPEECH_TRANSIENT_CANDIDATE", o["rms_db"], "SPECTRAL_FLUX_Z>12", "LOW", f"z={o['z']}, high-minus-mid dB {o['high_minus_mid']}")
    arws.sort(key=lambda r: (r["start_sec"], r["audio_event_id"]))
    for i, r in enumerate(arws): r["audio_event_id"] = f"AE{i + 1:04d}"
    # ---- SYNC rows: shot starts and motion starts relative to nearest word
    def nearest(t):
        k = bisect.bisect_right(wst, t) - 1
        if k >= 0 and t < wen[k]:
            off = int(round((t - wst[k]) * 1000)); return k, ("ON_WORD_START" if off <= 80 else "DURING_WORD"), off
        cand = []
        if k >= 0: cand.append((abs(t - wen[k]), k, int(round((t - wen[k]) * 1000)), "AFTER_WORD(visual follows)"))
        if k + 1 < len(words): cand.append((abs(wst[k + 1] - t), k + 1, -int(round((wst[k + 1] - t) * 1000)), "BEFORE_WORD(visual leads)"))
        dist, j, off, rel = min(cand)
        if rel.startswith("BEFORE") and abs(off) <= 80: rel = "ON_WORD_START"
        if dist > 0.5: rel = "IN_PAUSE(" + rel.split("(")[0] + ")"
        return j, rel, off
    sync = []
    ids = {r["state_id"]: r for r in srows}
    def tok(s): return set(re.findall(r"[a-z0-9$%.]{3,}", s.lower()))
    for r in shrows:
        t = r["start_sec"]; k, rel, off = nearest(t)
        sync.append(dict(video_id=vid, sync_id=f"SY{len(sync) + 1:05d}", visual_event_type="SHOT_START", shot_id=r["shot_id"], state_id=r["first_state_id"], motion_id="", visual_event_sec=t, sentence_id=words[k]["sentence_id"], word_id=words[k]["word_id"],
                         trigger_word=words[k]["word"], word_start_sec=words[k]["start_sec"], word_end_sec=words[k]["end_sec"], offset_ms=off, sync_relation=rel, text_token_match="", audio_event_id="",
                         confidence="MEASURED visual time (frame-exact) vs ASR word time (Whisper ±~100ms)", notes=ann[r["first_state_id"]]["change"][:80]))
    for m in mrows:
        t = m["start_sec"]; k, rel, off = nearest(t)
        vt = tok(ids[m["target_state"]]["visible_text"])
        near = {re.sub(r"[^a-z0-9$%.]", "", words[j]["word"].lower()) for j in range(max(0, k - 6), min(len(words), k + 7))}
        match = sorted(vt & near)
        sync.append(dict(video_id=vid, sync_id=f"SY{len(sync) + 1:05d}", visual_event_type="MOTION_START", shot_id=m["shot_id"], state_id=m["target_state"], motion_id=m["motion_id"], visual_event_sec=t, sentence_id=words[k]["sentence_id"], word_id=words[k]["word_id"],
                         trigger_word=words[k]["word"], word_start_sec=words[k]["start_sec"], word_end_sec=words[k]["end_sec"], offset_ms=off, sync_relation=rel, text_token_match=";".join(match)[:80], audio_event_id="",
                         confidence="MEASURED visual time (frame-exact) vs ASR word time (Whisper ±~100ms)", notes=m["action_label"]))
    # ---- SEMANTIC_BEATS.csv
    brows = []
    bp = out / "_pipeline/beats" / f"{vid}.txt"
    sidx = {s["sentence_id"]: i for i, s in enumerate(sents)}
    if bp.exists():
        for line in open(bp):
            line = line.rstrip("\n")
            if not line or line.startswith("#"): continue
            p = line.split("|"); a, _, b = p[0].partition("-"); b = b or a
            ss = sents[sidx[a]: sidx[b] + 1]
            txt = " ".join(x["text"] for x in ss); nw = sum(int(x["word_count"]) for x in ss); t0, t1 = float(ss[0]["start_sec"]), float(ss[-1]["end_sec"])
            brows.append(dict(video_id=vid, beat_id=f"B{len(brows) + 1:03d}", start_sec=t0, end_sec=t1, duration_sec=round(t1 - t0, 2), first_sentence_id=a, last_sentence_id=b, beat_types=p[1], viewer_intent=p[2], devices=p[3] if len(p) > 3 else "",
                              words=nw, words_per_sec=round(nw / (t1 - t0), 2) if t1 > t0 else "", rhetorical_questions=sum(x["is_question"] == "True" for x in ss), numbers_sentences=sum(x["has_number"] == "True" for x in ss),
                              pause_before_sec=ss[0]["gap_before_sec"], text=txt, text_status="ASR_UNVERIFIED (Whisper base; proper nouns/numbers need check against on-screen text)", confidence="INTERPRETATION (reviewer judgement on transcript + visuals)"))
    # ---- write
    wr(d / "STATES.csv", srows); wr(d / "SHOTS.csv", shrows); wr(d / "MOTIONS.csv", mrows); wr(d / "ASSETS.csv", arows); wr(d / "AUDIO_EVENTS.csv", arws); wr(d / "AUDIO_VISUAL_SYNC.csv", sync)
    if brows: wr(d / "SEMANTIC_BEATS.csv", brows)
    # evidence sheets (recompressed copies of the review sheets)
    from PIL import Image
    ev = d / "evidence" / "sheets"; ev.mkdir(parents=True, exist_ok=True)
    for sp in sorted((work / "sheets").glob("sheet_*.jpg")):
        im = Image.open(sp); im.thumbnail((1600, 1600)); im.save(ev / sp.name, quality=62, optimize=True)
    # ---- QA
    sd = np.array([s["dur"] for s in st_list]); shd = np.array([r["duration_sec"] for r in shrows])
    qa = dict(video_id=vid, checks={}, coverage={}, counts={}, caveats=[])
    qa["checks"]["state_timeline_starts_at_zero"] = abs(st_list[0]["start"]) < 1e-6
    qa["checks"]["state_timeline_ends_at_duration"] = abs(st_list[-1]["end"] - dur) < 0.05
    mt = {m["target_state"]: m for m in mrows}
    gaps = [(st_list[i - 1]["end"], st_list[i]["start"], st_list[i]["state_id"]) for i in range(1, len(st_list)) if st_list[i]["start"] - st_list[i - 1]["end"] > 0.002]
    qa["checks"]["every_inter_state_gap_explained_by_a_motion_row"] = all(g[2] in mt and abs(mt[g[2]]["end_sec"] - g[1]) < 0.06 and mt[g[2]]["start_sec"] <= g[1] + 0.06 for g in gaps)
    qa["checks"]["no_overlapping_states"] = all(st_list[i]["start"] >= st_list[i - 1]["end"] - 0.002 for i in range(1, len(st_list)))
    qa["checks"]["state_time_plus_transition_gaps_equals_duration"] = abs(float(sd.sum()) + sum(g[1] - g[0] for g in gaps) - dur) < 0.1
    qa["checks"]["shots_cover_duration"] = abs(sum(shd) - dur) < 0.1
    qa["checks"]["all_auto_states_annotated"] = not missing; qa["checks"]["no_orphan_annotations"] = not extra
    qa["checks"]["unique_state_ids"] = len({r["state_id"] for r in srows}) == len(srows); qa["checks"]["unique_shot_ids"] = len({r["shot_id"] for r in shrows}) == len(shrows)
    qa["checks"]["unique_motion_ids"] = len({r["motion_id"] for r in mrows}) == len(mrows); qa["checks"]["unique_sync_ids"] = len({r["sync_id"] for r in sync}) == len(sync)
    qa["checks"]["unique_audio_event_ids"] = len({r["audio_event_id"] for r in arws}) == len(arws); qa["checks"]["unique_asset_ids"] = len({r["asset_id"] for r in arows}) == len(arows)
    qa["checks"]["motion_states_resolve"] = all(m["target_state"] in ids and (m["source_state"] in ids or m["source_state"] == "") for m in mrows)
    qa["checks"]["sync_links_resolve"] = all(s["word_id"] in {w["word_id"] for w in words} and s["state_id"] in ids for s in sync)
    qa["checks"]["asset_refs_resolve"] = all(t.split("=")[0].strip() in {a["asset_id"] for a in arows} for r in srows for t in r["asset_ids"].split(";") if t)
    qa["checks"]["transcript_monotonic_nonneg_durations"] = all(wst[i] <= wen[i] and (i == 0 or wst[i] >= wst[i - 1] - 0.001) for i in range(len(words)))
    qa["checks"]["transcript_within_video_duration"] = wen[-1] <= dur + 0.5
    qa["checks"]["audio_events_within_duration"] = all(0 <= r["start_sec"] <= r["end_sec"] <= dur + 0.5 for r in arws)
    qa["checks"]["every_shot_has_purpose"] = all(r["narrative_purpose"] for r in shrows)
    qa["coverage"] = dict(video_duration_sec=round(dur, 3), frames_decoded=va["frames"], fps=fps, stable_state_sec=round(float(sd.sum()), 3), transition_gap_sec=round(sum(g[1] - g[0] for g in gaps), 3), speech_first_word_sec=wst[0], speech_last_word_end_sec=wen[-1],
                          visual_method="EVERY frame decoded (native fps, gray low-res) for change detection; one representative full-res frame per state reviewed on labelled contact sheets (not every frame viewed)",
                          audio_method="Whole soundtrack analysed by signal processing (loudness/pauses/transient flux) and spectrogram strips inspected; NOT auditory listening")
    qa["counts"] = dict(label_vs_measure_conflicts=sum(m["label_vs_measure_check"] != "consistent" for m in mrows), words=len(words), sentences=len(sents), states=len(st_list), shots_reviewed=len(shrows), auto_boundary_episodes=sum(1 for e in eps if e["cls"] in ("HARD_CUT", "WIPE_DISSOLVE_OR_LARGE_REPLACEMENT")), motion_rows=len(mrows),
                        micro_change_episodes_not_tabulated=sum(1 for e in eps if e["cls"] == "MICRO_CHANGE"), assets=len(arows), audio_events=len(arws), sync_rows=len(sync), beats=len(brows),
                        low_confidence_words=sum(w["text_status"] == "ASR_UNVERIFIED" for w in words), speech_onsets_non_speech=sum(not o["under_speech"] for o in aa["onsets"]))
    qa["stats"] = dict(state_dur_median=round(float(np.median(sd)), 2), state_dur_mean=round(float(sd.mean()), 2), shot_dur_median=round(float(np.median(shd)), 2), shot_dur_mean=round(float(shd.mean()), 2),
                       states_per_min=round(len(st_list) / dur * 60, 1), shots_per_min=round(len(shrows) / dur * 60, 1), words_per_min=round(len(words) / (wen[-1] - wst[0]) * 60, 1))
    qa["missing_annotations"] = missing; qa["orphan_annotations"] = extra
    qa["caveats"] += ["ASR transcript is machine output (Whisper base): proper nouns and some numbers are unverified; on-screen text is the better source where visible.",
                      "Pixel-difference thresholds cannot see changes confined to <0.03% of pixels; 'MICRO_CHANGE' episodes are counted but not tabulated.",
                      "Easing cannot be distinguished from linear motion with this evidence; recorded as NOT_ASSESSED.",
                      "Audio: no listening panel; 'music' and 'SFX' claims are limited to what spectrograms and measured loudness show."]
    qa["checks"] = {k: bool(v) for k, v in qa["checks"].items()}
    qa["status"] = "QA_PENDING" if not all(qa["checks"].values()) else "PASS_STRUCTURAL"
    json.dump(qa, open(d / "QA.json", "w"), indent=1)
    src = dict(video_id=vid, title=cat["title"], format_class=cat["format_class"], published_at=cat["published_at"], url=cat["watch_url"], local_file=meta["local_path"], sha256=meta["sha256"], probe=dict(width=meta["width"], height=meta["height"], fps=meta["fps"], video_codec=meta["video_codec"], audio_codec=meta["audio_codec"], audio_tracks=meta["audio_tracks"], duration_local_sec=meta["local_duration_sec"], duration_public_sec=meta["duration_sec_public"]),
               identity=dict(status="SOURCE_VERIFIED", confidence=meta["identity_confidence"], evidence=meta["identity_evidence"]), public_metadata_snapshot=dict(views=cat["views"], likes=cat["likes"], collected_at=cat["collected_at"], snapshot=cat["snapshot"]),
               asr=dict(model=wj["asr_model"], language=wj["language"], elapsed_sec=wj["elapsed_sec"]), analysis_params=va["params"], tools=dict(ffmpeg="system", python="3.9", whisper="openai-whisper 20240930 (local, base)"))
    json.dump(src, open(d / "SOURCE.json", "w"), indent=1)
    print(vid, "QA:", qa["status"], {k: v for k, v in qa["checks"].items() if not v}, qa["counts"], qa["stats"])


if __name__ == "__main__":
    main(*sys.argv[1:4])
