"""Stage E: auto-generated measured sections for VISUAL_RECONSTRUCTION.md (interpretive text is appended from recon/<id>.md if present).
Usage: python3 -B report_video.py <VIDEO_ID> <OUT_DIR>
"""
import csv, json, sys
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np


def rd(p):
    return list(csv.DictReader(open(p, newline="")))


def main(vid, out):
    out = Path(out); d = out / "02_VIDEO_FORENSICS" / vid
    sh, st, mo, asx = rd(d / "SHOTS.csv"), rd(d / "STATES.csv"), rd(d / "MOTIONS.csv"), rd(d / "ASSETS.csv")
    sy, ae = rd(d / "AUDIO_VISUAL_SYNC.csv"), rd(d / "AUDIO_EVENTS.csv")
    qa = json.load(open(d / "QA.json")); src = json.load(open(d / "SOURCE.json"))
    dur = qa["coverage"]["video_duration_sec"]
    sd = np.array([float(r["duration_sec"]) for r in sh]); stdur = np.array([float(r["duration_sec"]) for r in st])
    tagtime = defaultdict(float)
    for r in sh:
        for t in [x for x in r["technique_classes"].split(";") if x]: tagtime[t] += float(r["duration_sec"])
    only_draw = sum(float(r["duration_sec"]) for r in sh if set(r["technique_classes"].split(";")) <= {"ORIGINAL_DRAWING", "MOTION_GRAPHICS"})
    lab = Counter(m["action_label"] for m in mo)
    topA = sorted(asx, key=lambda a: -float(a["on_screen_seconds"]))[:12]
    rel = Counter(r["sync_relation"].split("(")[0] for r in sy)
    L = []
    L.append(f"# VISUAL RECONSTRUCTION — {src['title']} ({vid})\n")
    L.append(f"_Source: {src['format_class']} · {src['probe']['width']}×{src['probe']['height']} @ {src['probe']['fps']} fps · {dur:.1f}s · published {src['published_at'][:10]} · SHA256 `{src['sha256'][:16]}…`_\n")
    L.append("## 1. Measured summary (from per-frame analysis; no interpretation)\n")
    L.append(f"- Frames decoded: **{qa['coverage']['frames_decoded']}** (every frame). Reviewed shots: **{len(sh)}**; stable states: **{len(st)}**; motion rows: **{len(mo)}**; micro-changes below threshold (counted, not tabulated): {qa['counts']['micro_change_episodes_not_tabulated']}.")
    L.append(f"- Shot length: median **{np.median(sd):.1f}s**, mean {sd.mean():.1f}s, p10 {np.percentile(sd, 10):.1f}s, p90 {np.percentile(sd, 90):.1f}s → **{len(sh) / dur * 60:.1f} shots/min**.")
    L.append(f"- Visual-state length: median **{np.median(stdur):.2f}s**, mean {stdur.mean():.2f}s → **{len(st) / dur * 60:.1f} states/min** (a new composition state roughly every {dur / len(st):.1f}s incl. transitions).")
    L.append(f"- Time in transitions/animation (frames between stable states): **{qa['coverage']['transition_gap_sec']:.0f}s ({100 * qa['coverage']['transition_gap_sec'] / dur:.0f}%)**; stable states **{qa['coverage']['stable_state_sec']:.0f}s ({100 * qa['coverage']['stable_state_sec'] / dur:.0f}%)**.")
    L.append(f"- Shot-time by technique tag (reviewer tags; a shot can carry several): " + "; ".join(f"{k} {100 * v / dur:.0f}%" for k, v in sorted(tagtime.items(), key=lambda x: -x[1])) + f". Shots made only of drawn assets + text motion: {100 * only_draw / dur:.0f}% of runtime.")
    L.append(f"- Motion vocabulary (reviewer labels, count): " + ", ".join(f"{k} {v}" for k, v in lab.most_common(14)) + ".")
    L.append(f"- Narration pace: **{qa['stats']['words_per_min']:.0f} words/min** over the voiced span; sync of visual events vs ASR word times: " + ", ".join(f"{k} {v}" for k, v in rel.most_common()) + ".")
    offs = [int(r["offset_ms"]) for r in sy if r["visual_event_type"] == "SHOT_START"]
    L.append(f"- Shot-start offset vs nearest word start: median **{int(np.median(offs))} ms** (p10 {int(np.percentile(offs, 10))}, p90 {int(np.percentile(offs, 90))}); negative = visual before the word. ASR word timing carries about ±100 ms uncertainty.")
    L.append(f"- Reused assets: {sum(a['reuse_status'] == 'REUSED' for a in asx)} of {len(asx)} asset keys appear in more than one shot. Longest on-screen assets:\n")
    L.append("| Asset | Type | Seconds on screen | Shots | Technique class |\n|---|---|---:|---:|---|")
    for a in topA: L.append(f"| {a['asset_id']} | {a['asset_type']} | {a['on_screen_seconds']} | {a['shot_appearances']} | {a['technique_class']} |")
    # ---- hook / retention-oriented windows (observable mechanisms only; no retention statistics exist in public data)
    wd = rd(d / "TRANSCRIPT.csv"); ws = [float(w["start_sec"]) for w in wd]
    short = src["format_class"] == "SHORT"
    wins = ([(0, 1), (1, 3), (3, 10), (10, dur / 2), (dur / 2, dur - 5), (dur - 5, dur)] if short else [(0, 5), (5, 15), (15, 30), (30, 60), (60, dur / 2), (dur / 2, dur - 60), (dur - 60, dur)])
    names = (["first 1s", "1-3s", "3-10s", "10s-midpoint", "midpoint-last5s", "last 5s"] if short else ["0-5s", "5-15s", "15-30s", "30-60s", "60s-midpoint", "midpoint-last60s", "last 60s"])
    L.append("\n## 1b. Hook / retention-oriented structure (observable mechanisms, not retention statistics)\n")
    L.append("| Window | States | Shots | Motion starts | Words/min | Evidence objects introduced* | Shot-start events on a word |\n|---|---:|---:|---:|---:|---:|---:|")
    Aidx = {a["asset_id"]: a for a in asx}
    seen = set()
    for (a, b), nm in zip(wins, names):
        sts = [r for r in st if a <= float(r["start_sec"]) < b]; shs = [r for r in sh if a <= float(r["start_sec"]) < b]; mos = [r for r in mo if a <= float(r["start_sec"]) < b]
        nw = sum(1 for x in ws if a <= x < b); new = 0
        for r in sts:
            for t in r["asset_ids"].split(";"):
                if t and t not in seen and Aidx.get(t, {}).get("asset_type") in ("SCREENSHOT", "LOGO", "CHART", "PHOTO", "VIDEO_FOOTAGE", "IMAGE_STILL"): new += 1
                if t: seen.add(t)
        onw = sum(1 for r in sy if a <= float(r["visual_event_sec"]) < b and r["visual_event_type"] == "SHOT_START" and r["sync_relation"].startswith(("ON_WORD", "BEFORE_WORD")))
        L.append(f"| {nm} ({a:.0f}-{b:.0f}s) | {len(sts)} | {len(shs)} | {len(mos)} | {nw / max(b - a, 0.01) * 60:.0f} | {new} | {onw} |")
    L.append("\n*first appearance of a screenshot/logo/chart/photo/footage/still asset in the window.\n")
    first = [r for r in st if float(r["start_sec"]) < (3 if short else 15)]
    L.append("First visual states (literal): " + " ".join(f"[{r['state_id']} @{float(r['start_sec']):.1f}s] {r['literal_frame_description'][:150]}" for r in first[:4]) + "\n")
    L.append("Closing frames: " + " ".join(f"[{r['state_id']} @{float(r['start_sec']):.1f}s] {r['literal_frame_description'][:130]}" for r in st[-3:]) + "\n")
    L.append("\n## 2. Shot list index\n")
    L.append("Full tables: `SHOTS.csv`, `STATES.csv` (one row per stable state with literal description, visible text, assets, entering motion), `MOTIONS.csv`, `ASSETS.csv`. Evidence: `evidence/sheets/sheet_NNN.jpg` — each tile is the representative frame of one state, labelled with its State_ID and timestamp.\n")
    L.append("| Shot | Start | Dur | States | Purpose |\n|---|---:|---:|---:|---|")
    for r in sh: L.append(f"| {r['shot_id']} | {float(r['start_sec']):.1f} | {float(r['duration_sec']):.1f} | {r['state_count']} | {r['narrative_purpose'][:90]} |")
    p = out / "_pipeline" / "recon" / f"{vid}.md"
    if p.exists(): L.append("\n" + p.read_text())
    (d / "VISUAL_RECONSTRUCTION.md").write_text("\n".join(L) + "\n")
    print("wrote", d / "VISUAL_RECONSTRUCTION.md", len("\n".join(L)))


if __name__ == "__main__":
    main(*sys.argv[1:3])
