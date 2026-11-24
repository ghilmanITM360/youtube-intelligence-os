import csv, json, hashlib, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from shots import SHOTS, EVENTS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VID = "8fADp43wJwU"
SHA = "1fb3c0f4f510fe724749105425e31c8d7f5e9a6053d41e8b67e21f6a2c0a11d9"
P = f"CH-000004_{VID}_{SHA[:8]}_"
FPS = 24

def fr(t): return round(t * FPS)
def out(name): return os.path.join(ROOT, P + name)

# ---------- ledgers ----------
with open(out("shot_ledger.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow("video_id,shot_id,start_pts_seconds,end_pts_seconds,start_frame,end_frame,shot_boundary_evidence,shot_verified,subject,setting,framing,camera_motion,subject_motion,graphics_text,entrance,exit,narrative_function,source_frame_refs,uncertainty".split(","))
    for s in SHOTS:
        measured = "MEASURED" in s["bnd"] and "ESTIMATED" not in s["bnd"]
        ver = "DETECTOR_PLUS_SHEET_REVIEW" if measured else "SHEET_REVIEW_DETECTOR_CANDIDATE"
        w.writerow([VID, s["id"], f"{s['t0']:.3f}", f"{s['t1']:.3f}", fr(s['t0']), fr(s['t1']) - 1, s["bnd"], ver,
                    s["name"], "see report", "see report", "locked-off (no camera move observed at 1fps; native not reviewed except 2.5-6.0s)",
                    "see events", "see report", "hard cut" if measured else "boundary candidate", "hard cut", s["func"][:140],
                    "sheets/sheet_%02d.jpg" % int(s['t0'] // 20), "Intra-shot times from 1fps sheets, +/-1s"])

with open(out("visual_event_ledger.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow("video_id,shot_id,visual_state_id,event_id,start_pts_seconds,end_pts_seconds,start_frame,end_frame,event_class,subject_object_id,before_state,after_state,motion_vector_or_direction,transition_type,source_frame_paths,source_audio_reference,coverage_level,evidence_label,confidence,alternative_interpretation,creative_function_hypothesis,editor_reconstruction_note".split(","))
    for (sid, eid, t0, t1, cls, obj, b, a, tr, lvl, lab, conf, note) in EVENTS:
        w.writerow([VID, sid, sid + "-st", eid, f"{t0:.2f}", f"{t1:.2f}", fr(t0), fr(t1), cls, obj, b, a, "n/a", tr,
                    "sheets/dense_intro.jpg" if lvl == "DENSE_4FPS" else "sheets/sheet_%02d.jpg" % int(t0 // 20),
                    "UNAVAILABLE", lvl, lab, conf, "", "see report", note])

with open(out("audio_visual_alignment.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow("video_id,event_id,audio_source,audio_listening_status,phrase_or_sound,audio_start_pts,audio_end_pts,visual_start_pts,visual_end_pts,lead_lag_seconds,timestamp_method,confidence,limitations".split(","))
    w.writerow([VID, "ALL", "UNAVAILABLE", "NOT_LISTENED", "n/a", "", "", "", "", "", "UNAVAILABLE",
                "n/a", "No ASR run, no human listening. Apify transcript has no timestamps (positional only). Lead/lag not measured."])

# ---------- manifests ----------
manifest = {
 "schema_version": "1.0",
 "source": {"channel_id": "CH-000004", "video_id": VID,
  "file_path": "/Users/ghilmanislam360/GhilmanProjects/video data of what if/videos/YTDown.com_YouTube_If-all-humans-died-when-would-the-last-l_Media_8fADp43wJwU_001_1080p.mp4",
  "sha256": SHA, "bytes": 11798080, "duration_seconds": 303.856327, "time_base": "1/12288",
  "frame_rate_avg": "24/1", "vfr_status": "CFR assumed from r_frame_rate==avg_frame_rate==24/1 (per-frame PTS not audited)",
  "video_streams": [{"codec": "h264", "width": 1920, "height": 1080, "nb_frames": 7291}],
  "audio_streams": [{"codec": "aac", "sample_rate": 44100, "channels": 2, "nb_frames": 13086}],
  "other_copies": [{"path": "~/Documents/YIOS-Media-Library/xkcd Channel/If all humans died, when would the last light go out？ [8fADp43wJwU].mp4", "sha256": "973bb97ae6717fa54d42fe3524fcc6921016a65fa23ccae4b569ea62e91f2b4b", "bytes": 11798131,
     "note": "Same duration/frame count/resolution; bytes differ by 51 (container metadata). Content equivalence NOT byte-proven; frames not compared."}]},
 "execution": {"git_sha": "27987f2b (branch research/senior-health-reports-2026-11-11, repo untouched)", "tool_versions": {"ffmpeg": "homebrew", "imagemagick": "montage"},
  "reader": "Claude (Sonnet 5.5) with visual-ct-scan standard, DEEP mode, 2026-11-17", "date": "2026-11-17"},
 "evidence": {"source_verified": True, "audio_listened": False, "registered_yios_status": "PRIOR_RUN_2026-09-16_HISTORICAL_UNVERIFIED (29 shots / 48 states, 2s sampling); this run does not promote it"},
 "identity": "Catalog video 8fADp43wJwU (CH-000004) mapped as SRC10 in what-if-forensic-source-v1.json with the same sha256 1fb3c0f4... (KNOWN_EXISTING, VERIFIED).",
}
json.dump(manifest, open(out("source_manifest.json"), "w"), indent=1)

coverage = {
 "video_id": VID, "source_sha256": SHA, "requested_mode": "DEEP",
 "review_scope": {"source_seconds_total": 303.856, "overview_sampling_hz": 1,
   "per_frame_detector": "all 7290 frame-to-frame differences (160px gray tblend), shot-boundary candidates >=40 reviewed against sheets",
   "native_intervals_reviewed": [{"range_s": [2.5, 6.0], "step": "0.25s native frames (4 fps)", "frames": 14}, {"single_frames_1280px": [4.0, 117.0, 296.5]}],
   "unreviewed_or_unverified_intervals": ["all intra-shot states outside 2.5-6.0 s are 1 fps samples (+/-1s), not frame-accurate",
      "1fps sheet label k corresponds to source time ~k+0.46 s (verified against boundary 258.458); all ESTIMATED event times already add this offset",
      "camera motion (push/zoom) not verified between samples; treated as locked-off by observation only",
      "weak (white-to-white / dark-to-dark) boundaries at 78.875, 172.125, 191.208, 200.208 are detector candidates confirmed by sheet change only",
      "audio: not listened, no ASR; transcript untimed"]},
 "counts": {"shots": len(SHOTS), "measured_hard_cuts": 26, "weaker_boundaries": 4, "events_logged": len(EVENTS),
            "prior_run_shots_for_comparison": 29},
}
json.dump(coverage, open(out("coverage.json"), "w"), indent=1)

gates = {
 "video_id": VID, "source_sha256": SHA, "requested_mode": "DEEP",
 "gates": {"source_identity": "PASS", "full_temporal_overview": "PASS", "candidate_shots_verified": "PARTIAL",
   "meaningful_state_timing": "PARTIAL", "motion_design_review": "PARTIAL", "creative_design_review": "PASS",
   "visual_script_mapping": "PARTIAL", "production_blueprint": "PASS", "audio_human_listening": "BLOCKED", "final_av_signoff": "BLOCKED"},
 "final_video_status": "VISUAL_ANALYSIS_PARTIAL",
 "limitations": ["intra-shot timing from 1fps samples", "native dense review only 2.5-6.0 s", "four weak shot boundaries unconfirmed at native frames",
                 "no audio listening; transcript untimed", "tool-based 1:1 mapping of transcript to shots is by content order, not timestamps",
                 "spoken '~six million times' vs on-screen '76,000,000' left unresolved"],
 "next_step": "Dense native-frame windows around S02 logo motion, S16 nacelle, S23, S25 lane steps and 4 weak boundaries; human listening pass; then re-gate.",
}
json.dump(gates, open(out("quality_gate.json"), "w"), indent=1)

# ---------- per-shot report ----------
CALLBACK = {
 "S01": "Introduces: red=person-removed mechanic, lamp=light state. Reused: S03-S14 and others.",
 "S02": "Bookended by S31 (same red field + silhouette).",
 "S03": "Leaves right half empty -> filled by S04 inset.",
 "S04": "Reuses S01 red-dissolve mechanic; objects named in narration.",
 "S05": "Plate family 'black silhouette on off-white' (S05, S07, S09, S13, S15, S17).",
 "S06": "Red-dissolve + global darken step (also E012).",
 "S07": "Base plate reused in S09 (callback with glow off).",
 "S08": "Chart/scroll gag; single use.",
 "S09": "Callback to S07: same plate, changed state (reversal).",
 "S10": "Grid reappears conceptually as the five-lane lineup in S25.",
 "S11": "Introduces white time-label (< 6 MONTHS) -> reused as <3 YEARS, 11/3/>20 YEARS, ~4 YEARS, ~100 YEARS.",
 "S12": "Icon sheet reappears as lanes in S25.",
 "S13": "Silhouette family; label pattern.", "S14": "Time-label + dissolve + decay overlay (reused in S17, S23).",
 "S15": "Wind-farm silhouette -> S16 comparison.", "S16": "Column-build system reused in S21.",
 "S17": "Decay overlay system (rust) reused in S23.", "S18": "Prop gag; single use.",
 "S19": "Recolor red->white = discharge (same colour logic as red=life).", "S20": "Fill-drain system.",
 "S21": "Column-build system from S16.", "S22": "Wide road composition reused in S24 (after-time-skip).",
 "S23": "Cropped reuse of S22's pole + panel.", "S24": "Compositional reuse of S22 with changed props.",
 "S25": "Lanes echo S10/S12; ends with barrel hand-off to S26.",
 "S26": "Glow-off beat (radioactivity invisible) before S28 re-introduces glow as cyan.",
 "S27": "Analogy; radial plate; single use.", "S28": "First cyan: becomes the final colour identity.",
 "S29": "Cyan glow + decay graph (S29) -> S30.", "S30": "Cyan stack = final payoff.", "S31": "Bookend of S02.",
}
CONTENT = {"S02": "Decorative (brand)", "S18": "Emotional/humor", "S31": "Essential (CTA/credits)", "S12": "Reinforcing", "S15": "Emotional/humor + reinforcing"}

def block(s):
    n = s["id"]
    attn = [a.strip() for a in s["attn"].split(";")]
    levels = ["Very High", "High", "Medium", "Medium"]
    dom = "\n".join(f"| {a} | see anim/events | see facts | see composition | n/a | {levels[i]} |" for i, a in enumerate(attn))
    dur = s["t1"] - s["t0"]
    return f"""
### {n} - {s['name']}  ({s['t0']:.3f} -> {s['t1']:.3f} s, {dur:.1f} s)

1. **[VISUAL ID]** {n}
2. **[TIMESTAMP]** {s['t0']:.3f}-{s['t1']:.3f} s (start frame {fr(s['t0'])}); boundary: {s['bnd']}. Source PTS timebase 1/12288 @24 fps.
3. **[SCRIPT / SPOKEN WORDS]** {s['spoken']}
4. **[OBJECTIVE VISUAL FACTS]** (OBSERVED) {s['facts']}
5. **[CHANGE FROM PREVIOUS VISUAL]** {s['change']}
6. **[AUDIO + VISUAL SYNCHRONIZATION]** UNAVAILABLE as measurement: audio not listened, transcript untimed. Order-of-content match only (INFERRED): the visual states appear in the same order as the narrated claims.
7. **[ATTENTION STACK]** (INFERRED salience hypothesis, not gaze data) {s['attn']}
8. **[COMPOSITION ANALYSIS]** {s['comp']}
9. **[VISUAL DOMINANCE]** (heuristic ranking from the stack above; no numeric weights)

| Element | Motion | Contrast | Scale | Position | Visual Pull | Dominance |
|---|---|---|---|---|---|---|
{dom}

10. **[RETENTION FUNCTION]** {s['func']}
11. **[VISUAL DNA]** Uses the shared locks in Part B (flat 2D hand-drawn linework; off-white/grey/black base; red = people disappearing; cyan = radioactive glow). Medium: flat 2D limited animation (OBSERVED).
12. **[EXACT RECONSTRUCTION IMAGE PROMPT]** {s['img']} Preserve the observed framing, subject placement, object relationships, lighting hierarchy, visual scale, and empty-space distribution. Do not introduce additional people, props, text, decorations, or background objects not present in the source visual.
13. **[NEGATIVE / DO-NOT-CHANGE PROMPT]** {s['neg']}
14. **[DETAILED ANIMATION / IMAGE-TO-VIDEO PROMPT]** {s['anim']} Continuity lock: preserve identity, placement, environment, lighting, perspective, composition; add nothing new.
15. **[CONCISE ANIMATION PROMPT]** {s['concise']}
16. **[MOTION NEGATIVE PROMPT]** no morphing of line art, no extra objects, no camera spin/zoom, no flicker, no style shift to 3D or photoreal, no added text.
17. **[HOW THE VISUAL IS BUILT]** {s['built']}
18. **[EDIT RECONSTRUCTION]** {s['edit']}
19. **[HOW THE VISUAL FUNCTIONS IN THE VIDEO]** {s['func']} Content-vs-decoration: {CONTENT.get(n, 'Essential/Reinforcing (adds information beyond narration)')}.
20. **[VISUAL EVOLUTION / CALLBACK]** {CALLBACK.get(n, '')}
21. **[LIKELY CREATOR INTENT]** {s['intent']}
22. **[RECONSTRUCTION CONFIDENCE]** {s['conf']}
23. **[EDITOR IMPROVEMENT]** {s['improve']}
"""

part_a = "\n".join(block(s) for s in SHOTS)

# ---------- report ----------
hdr = f"""# Visual CT-Scan Report - xkcd's What If? "If all humans died, when would the last light go out?"

- Video ID: {VID} (CH-000004) | Duration 303.856 s | 1920x1080 @24 fps | H.264 + AAC
- Source: {manifest['source']['file_path']}
- SHA-256: {SHA}
- Mode: DEEP (as requested: full video). Status: **VISUAL_ANALYSIS_PARTIAL** (see Coverage). Audio: **not listened**; **no AV sign-off**.
- Date: 2026-11-17. Repository untouched; all outputs are in this external folder.

## 0. Coverage and method (read first)

- **MEASURED:** per-frame difference signal across all 7,290 frames; 26 hard cuts at native-frame precision (difference spike >= 40). 4 weaker boundaries (white-to-white / dark-to-dark) found as spikes of 12-20 and confirmed by sheet change only. Total {len(SHOTS)} shots.
- **OBSERVED:** all 304 one-second samples reviewed on 16 contact sheets; 14 native frames at 4 fps (2.5-6.0 s) and 3 full frames at 1280 px.
- **ESTIMATED:** every intra-shot event time (+/-1 s). The 1fps sheet label k is actually ~k+0.46 s (verified against the 258.458 s cut), already corrected in the ledgers.
- **UNAVAILABLE / not done:** human listening, ASR, timed transcript, native review of most state changes, retention/CTR data, camera-motion verification.
- **Prior run (2026-09-16, `video_forensics_output/if_all_humans_died`)**: 29 shots / 48 states from 2 s sampling. Treated as HISTORICAL_UNVERIFIED; not promoted. This run finds {len(SHOTS)} shots; difference = weak boundaries and 2 extra short cards.
- **Prompt scope vs evidence:** your master prompt has 23 sections per visual plus synthesis. All 23 are produced per shot ({len(SHOTS)} shots, the meaningful distinct visuals); sub-states inside a shot are in the event ledger (49 events).
- Figures such as retention, CTR or exact easing are not claimed anywhere.

## 1. Literal visual summary (one sentence)
A black-line stick-figure presenter and chalkboard dissolve into red specks, then a series of hand-drawn silhouette plants and diagrams lose their lights one source at a time, ending on a pure black frame of glowing cyan waste blocks and a red end card with a books CTA.

## 2. Script architecture (transcript, positional)
- **Hook:** the viewer-submitted question card (S01) - states the title promise within 8 s; lamp dims at its end.
- **Open loop:** "when would the last artificial light go out?" stays open through the whole sequence of source types.
- **Structure ("elimination ranking"):** grid -> fossil -> nuclear (fuel-rich but auto-shutdown) -> off-grid generators (diesel < 6 months) -> geothermal (< 3 years) -> wind (11 / 3 / > 20 years) -> hydro (~4 years) -> batteries (decades) -> solar (~100 years) -> twist: radioactive glow (centuries).
- **Mini-payoffs:** time labels (S11, S14, S16, S17, S24). **Reversal:** "another contender, and it's a weird one" (S26). **Ultimate payoff:** S30 + final spoken answer. **CTA:** end card only (S31).
- **Alignment with packaging:** title promise ("last light") is answered literally at S30; the thumbnail was not available in this evidence (Not available from supplied evidence).

## 3. Shot timeline (compact)

| Shot | Time (s) | What |
|---|---|---|
""" + "\n".join(f"| {s['id']} | {s['t0']:.2f}-{s['t1']:.2f} | {s['name']} |" for s in SHOTS) + """

## Part A - Per-shot forensic records (23 sections each)
"""

part_b = """

## Part B - Video-level synthesis

### B1. Locks (use in every prompt)
- **CHARACTER LOCK (stick figure):** thin black wobbly outline, large empty circle head, no facial features, straight-line limbs, no fill; occasional hair bun / hard hat as only accessories (OBSERVED). Red version = same figure recolored.
- **RED PARTICLE DISINTEGRATION (effect lock):** outline breaks into small red specks drifting away from the figure's left/top; dissolve lasts roughly 1.5-3 s; appears on every "person removed" beat (S01, S04, S05, S06, S07, S11, S14, S17).
- **ENVIRONMENT LOCK A - silhouette plates:** solid near-black mass on off-white sky, thick black ground strip, line-drawn smoke, pylon at right (S05, S07, S09, S13, S15, S17).
- **ENVIRONMENT LOCK B - dark scenes:** dark grey ground/background with glow cones (S11, S22-S24, S26).
- **COLOR LOCK:** off-white, mid/dark greys, black; red only for people/failure/draining; cyan only for radioactive glow (S28-S30); no other hues except the red end card (S02, S31). Hex codes not measured.
- **TEXT LOCK:** hand-drawn caps for labels (e.g. '< 6 MONTHS'), serif for the question card, clean sans for end-card credits.
- **LIGHT/GLOW LOCK:** a soft white radial glow = "light on"; glow removed = "light out"; this on/off state is the main storytelling variable.

### B2. Creator visual system (supported by repetition)
- **Composition:** locked frames; horizontal silhouette bands; side-by-side column builds (S16, S21, S25); frame-within-frame insets (S04, S15, S16).
- **Motion:** almost no camera movement observed (not verified between samples). Motion = layer pop-ins, glow toggles, recolor, dissolve, fills draining, progressive decay overlays. Hard cuts between shots.
- **Pattern interrupts:** red particle dissolve (every ~10-20 s), global darken step (S06), colour jump (S02, S28 cyan), text label pop-ins.
- **Time-label system:** white caps label bubbles appear when a source "dies" ('< 6 MONTHS', '< 3 YEARS', '11 YEARS', '3 YEARS', '>20 YEARS', '~4 YEARS', '~100 YEARS'), forming a scoreboard the viewer can follow.
- **Humor layer:** speech bubbles, gag props (Eternal LIGHT box, Rhode Island billboard, 'UH OH...', 'MAYDAY!', 'OOPS!', Tom Scott cameo).

### B3. Retention / pacing (qualitative; no metrics)
- **Fast zones:** 8-21 s (four shots in 13 s), 72-100 s (5 short shots).
- **Slow/hold zones:** S08 (7 s chart), S22 (11 s road), S27 (19 s radial), S29 (27 s), S30 (8.6 s static final). Possible retention risk where narration is dense but visuals static; mitigations seen: staged label pop-ins and glow dims.
- **Strongest reveal:** S28 first cyan glow tied to "Cherenkov". **Strongest reversal:** S26 'weird contender' + glow on->off->new glow. **Strongest callback:** S22->S24 same road a century later. **Strongest escalation:** time labels from months -> years -> decades -> centuries.
- **Clip candidates (Shorts):** S11 island (diesel, < 6 months) ~9 s; S14 maintenance gag ~11 s; S15+S16 turbine lifespans ~28 s; S22-S24 solar call box ~29 s; S26-S30 radioactive twist ~65 s. Each needs added context; none promised here.

### B4. Thumbnail-style candidates (from frames; actual thumbnail not available)
1. S30 (285-293 s): single glowing cyan block cluster on black - single dominant promise, mobile-readable; add a short question; title would pair with 'the last light' idea.
2. S01 (0-3 s): large presenter + lamp + question; text-heavy, lower mobile readability.
3. S22: lit road with solar call box; medium readability.

### B5. Script analyzer consensus (seven lenses applied once; not seven external models)
- **Agreement:** strong hook (question card), clear elimination ranking, good humor, time labels as mini-payoffs, answer arrives as the twist.
- **Disagreement:** viral lens would reveal the cyan glow earlier; narrative lens keeps the twist late (current structure supports surprise).
- **Highest-priority risks:** Medium - static holds in S08/S22/S27/S29; Optional - mid-video CTA absent (end-only).
- **Scorecard (qualitative):** Hook Strong; Curiosity Strong; Narrative spine Exceptional; Pacing Strong; Payoffs Exceptional; Emotional engagement Functional (awe/humor, no empathy beats); Intellectual clarity Strong; CTA Functional (end only); Title alignment Excellent; Thumbnail alignment Not available.

### B6. Creator formula
1. **Setup:** viewer question on a card, a presenter who disappears.
2. **Curiosity:** list candidate sources; each fails with a time label.
3. **Visual escalation:** months -> years -> decades -> centuries; scenes get darker and simpler.
4. **Reversal:** the twist contender (radioactive waste glow).
5. **Payoff:** black frame with cyan glow; spoken answer.
**Visual formula:** one object per shot; state change on one variable (glow/colour/label); reuse plates; red = people, cyan = radioactivity.
**Editing formula:** hard cuts between plates; intra-shot changes by layer toggles timed to narrated facts; progressive overlays for decay.
**Retention formula:** open one loop (last light), close many micro-loops (each source's lifespan), then pay off with a surprise.

### B7. Asset list
- Characters: C01 presenter/stick figure; C02 inner chalkboard figure; C03 workers (red); C04 hard-hat operator; C05 seated operators; C06 dial painter.
- Environments: E01 chalkboard; E02 skyline; E03 apartment cutaway; E04-E08 silhouette plates (coal, nuclear, geothermal, wind farm, dam); E09 control room; E10 pipe room; E11 night road; E12 island; E13 diagrams (Cherenkov, tank).
- Objects: lamp, lava lamp, barrel, battery set, solar pole/call box, watch, capsule, generator.
- Graphics: time labels, speech bubbles, charts, decay graph, red particles, cyan glow, rain.
- Image prompts: IP-S01..IP-S31 (in Part A, section 12). Animation prompts: AP-S01..AP-S31 (section 14).

### B8. Rebuild workflow
1. Break the transcript into ~31 beats (one per shot).
2. Define the single state variable per beat (glow/colour/label).
3. Build plates once (silhouette A/B) and reuse (S07->S09, S22->S24).
4. Generate static plates with the section-12 prompts.
5. Animate only: dissolve, glow toggle, fill drain, overlay decay (section 14).
6. Add labels timed to the narrated number.
7. Cut on narrative emphasis; hard cuts only.
8. Insert a state change before any hold > ~8 s.
9. Preserve callbacks (road, plant).
10. Deliver the twist payoff as a simple, quiet final image.

### B9. Notes and open questions
- On-screen **'76,000,000'** vs spoken **'about six million times'**: different quantities may be shown; unresolved.
- **'Tom Scott'** card: on-screen text shows a creator name with a verified check; whether this is an intentional cameo reference is INFERRED.
- Whether the episode text is adapted from the *What If?* books: the end card states 'official adaptation of the What If? books' (OBSERVED), but which book/chapter is **not** established here.
- Credits (OBSERVED, S31): Henry Reich (Writer & Video Director); Lizah van der Aart (Illustration & Video Editing); Ever Salazar (Illustration & Animation); Know Art Studios (Music & Sound Effects); produced by Neptune Studios LLC.
"""

open(out("visual_ct_scan_report.md"), "w").write(hdr + part_a + part_b)

# blueprint = just prompts per shot + locks
bp = f"# Reconstruction Blueprint - {VID} (original, non-infringing production spec)\n\nStatus: derived from OBSERVED frames; for building NEW original assets. Use locks in the report Part B. Do not reuse the source's art, logos, or names beyond the CTA placeholder.\n\n## Build order\n1. Make plates; 2. add state layers; 3. animate only listed motions; 4. add labels; 5. hard cuts.\n"
for s in SHOTS:
    bp += f"\n## {s['id']} {s['name']} ({s['t0']:.2f}-{s['t1']:.2f} s)\n- Image: {s['img']}\n- Negative: {s['neg']}\n- Animation: {s['anim']}\n- Concise: {s['concise']}\n- Edit: {s['edit']}\n"
open(out("reconstruction_blueprint.md"), "w").write(bp)

hand = f"""# Continuation handoff - {VID}
- Source SHA-256: {SHA} (copy: GhilmanProjects/video data of what if/videos/...). Other copy sha 973bb97a... differs by 51 bytes.
- Status: VISUAL_ANALYSIS_PARTIAL; audio not listened; no AV sign-off. No YIOS ledger/status was modified; repository untouched.
- Next work (in order): (1) native dense windows (4-24 fps) at S02 logo motion (8.7-10.7 s), S16 nacelle (128-137 s), S23 (194-200 s), S25 lane steps (210-219 s), and 4 weak boundaries (78.9, 172.1, 191.2, 200.2 s); (2) human listening pass and timed transcript (whisper `-nfa` per project notes); (3) resolve 76,000,000 vs 'six million'; (4) compare with prior run `video_forensics_output/if_all_humans_died`; (5) re-run gates.
- Tools used: ffmpeg per-frame detector `build/` (ydiff in detector/), 1fps frames in frames_1fps, sheets in sheets/.
- Evidence folder: {ROOT}
- Owner of canonical branch: not touched. Disk free was ~26 GiB (98% used).
"""
open(out("continuation_handoff.md"), "w").write(hand)
print("ok", len(SHOTS), len(EVENTS))
