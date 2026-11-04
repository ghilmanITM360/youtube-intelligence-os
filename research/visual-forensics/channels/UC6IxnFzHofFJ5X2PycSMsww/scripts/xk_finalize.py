"""Per-video blueprint (state prompts derived from reviewed OBSERVED descriptions), quality_gate.json and continuation_handoff.md.
Usage: python3 -I xk_finalize.py <video_dir> [--report-done] [--art-done]"""
import csv, json, sys, pathlib, datetime
V = pathlib.Path(sys.argv[1]).resolve(); vid = V.name; flags = set(sys.argv[2:])
S = list(csv.DictReader(open(V / "tables/state_ledger.csv"))); cov = json.load(open(V / "coverage.json"))
sm = json.load(open(V / "source_manifest.json"))["source"]; pal = json.load(open(V / "tables/palette_measured.json"))
asrc = json.load(open(V / "asr/asr_vs_catalog_caption.json"))
portrait = int(sm["resolution"].split("x")[1]) > int(sm["resolution"].split("x")[0])
ar = "9:16 1080x1920" if portrait else "16:9 1920x1080"
now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
L = [f"# Reconstruction blueprint — {vid} (source sha {sm['sha256'][:12]})", "",
     "Two uses, kept separate: (A) **evidence-matched reconstruction test** of this source's observable output (internal QA only; source artwork, script, voice and branding remain the creator's and are not reusable assets); (B) **original transfer** — the same mechanics applied to a NEW topic, new drawings and new script (see the channel production manual).", "",
     "## Global tokens (MEASURED unless marked)",
     f"- Aspect {ar}, {sm['frame_rate_avg']} fps CFR.",
     f"- Canvas background exact {pal['background_exact_rgb']}; top quantised bins {', '.join(b['hex_bin_centre'] for b in pal['top_bins'][:5])}; red accent in {pal['holds_with_red_accent']}/{pal['holds']} holds; any saturated colour in {pal['holds_with_any_saturation']}/{pal['holds']} holds. Mean settled ink coverage {pal['mean_dark_ink_frac']*100:.1f}% (max {pal['max_dark_ink_frac']*100:.1f}%).",
     "- Line art: hand-drawn strokes (black on light canvases, white on dark scenes where present - see state descriptions); stick figures minimal, objects detailed (channel-typical, OBSERVED in reviewed videos). Exact brush/stroke width in px, typeface, software: UNAVAILABLE.",
     "- Lettering: hand-lettered all-caps for titles/labels (OBSERVED). Footnotes may use a small serif text block (OBSERVED where present).", "",
     "## Per-state prompts (derived from reviewed descriptions; ESTIMATED layout)", "",
     "| State | Source interval (s) | Image prompt (reconstruction) | Motion into next state | Must stay static | Negative |", "|---|---|---|---|---|---|"]
for i, x in enumerate(S):
    if x["kind"] != "HOLD": continue
    nxt = next((y for y in S[i + 1:] if y["kind"] == "ACTIVITY"), None)
    move = f"{nxt['subtype']} at {nxt['start_pts']}s over {nxt['frames']} frame(s)" if nxt else "end of video (hold)"
    desc = x["description"].replace("|", "/")
    L.append(f"| {x['visual_state_id']} ({x['seg']}) | {x['start_pts']}–{x['end_pts_exclusive']} | {ar}, canvas/lighting as described (video background mode {pal['background_exact_rgb']}), hand-drawn line art: {desc} | {move} | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |")
L += ["", "## Editor construction (OBSERVED grammar → steps)",
      "1. Build each composition as separate layers: canvas, persistent anchors (e.g., ruler/axis), object drawings, labels, red marks.",
      "2. Cuts = replace whole composition on the same canvas (hard cut, 0 frames).",
      "3. Pops = layer visibility on a single frame; write-ons = stroke/mask reveal in reading order over the measured frame count; dissolves = cross-fade over the measured frame count; camera = translate/scale the anchor layer group.",
      "4. Align each event onset to the narration word that names the element (ASR_UNCERTIFIED in source; verify by listening in production).",
      "", "## QA", "- Frame-compare each state against its source tile at native resolution (internal test only).", "- Onset tolerance target: ±2 frames of source event onset (MEASURED source values in visual_event_ledger.csv).",
      "- Legibility at 320 px width; numbers on screen must equal narrated numbers.", "- Listening/AV pass requires a human listener (source analysis has none)."]
(V / "reconstruction_blueprint.md").write_text("\n".join(L) + "\n")

acts = [x for x in S if x["kind"] == "ACTIVITY"]
unres = [x["seg"] for x in S if "UNRESOLVED" in x["description"] or x["confidence"] == "LOW"]
gates = {
 "source_identity": "PASS", "full_temporal_overview": "PASS",
 "candidate_shots_verified": "PASS" if all(x["event_class"] for x in acts) else "PARTIAL",
 "meaningful_state_timing": "PARTIAL" if unres else "PASS",
 "motion_design_review": "PASS" if cov["activities_fully_viewed"] == cov["activities"] else "PARTIAL",
 "creative_design_review": "PARTIAL" if "--art-done" in flags else "PENDING",
 "visual_script_mapping": "PARTIAL", "production_blueprint": "PARTIAL",
 "audio_human_listening": "BLOCKED", "final_av_signoff": "BLOCKED"}
qg = dict(video_id=vid, source_sha256=sm["sha256"], requested_mode="DEEP", generated_utc=now,
          review_scope=dict(source_seconds_total=sm["duration_seconds"], overview_sampling_hz="every decoded frame measured",
                            native_intervals_reviewed="settled frame of every HOLD + sampled ACTIVITY frames at 1/4 scale (see coverage.json)",
                            unreviewed_or_unverified_intervals=cov["partially_viewed_activity_intervals"]),
          gates=gates,
          gate_evidence=dict(source_identity="source_manifest.json + census/census.csv (channel tab listing)",
                             full_temporal_overview="tables/FULL_FRAME_MEASUREMENTS.csv all frames; tables/segments_v1.csv covers every frame",
                             candidate_shots_verified="tables/state_ledger.csv every segment classified from viewed tiles",
                             meaningful_state_timing=f"frame-precise onsets from measurements; unresolved: {unres}",
                             motion_design_review=f"{cov['activities_fully_viewed']}/{cov['activities']} activities viewed at every frame",
                             creative_design_review="visual_ct_scan_report.md §4 + tables/palette_measured.json (tile-scale)" if "--art-done" in flags else "not yet written",
                             visual_script_mapping=f"audio_visual_alignment.csv ASR_UNCERTIFIED; ASR-vs-caption ratio {asrc.get('ratio')}",
                             production_blueprint="reconstruction_blueprint.md (derived prompts; no render test yet)",
                             audio_human_listening="campaign/AUDIO_LISTENING_CAPABILITY.json BLOCKED_CAPABILITY"),
          final_video_status="VISUAL_ANALYSIS_PARTIAL", overall="PARTIAL", ct_scan_complete=False, full_av_signoff=False,
          limitations=["no actual listening", "activity in-between frames sampled where noted", "tile-scale (1/4) art review; small text partly illegible",
                       "reconstruction not render-tested per video"],
          reviewer=S[0]["reviewer"], next_step="independent review sample; reconstruction test via channel manual")
(V / "quality_gate.json").write_text(json.dumps(qg, indent=1))
(V / "continuation_handoff.md").write_text(f"""# Continuation handoff — {vid}
- Source sha256 {sm['sha256']}; path {sm['file_path']}; machine A (Ghilmans-Laptop), xkcd stream lock ~/YIOS-local-audits/xkcd-whatif/.xkcd_writer_lock.
- Status {qg['final_video_status']}; gates {json.dumps(gates)}.
- Pending: {', '.join(k for k, v in gates.items() if v != 'PASS')}; unresolved segments {unres}; partially viewed activities {len(cov['partially_viewed_activity_intervals'])}.
- Tools: scripts/xk_ingest.sh, xk_segment.py, xk_sheets.py, xk_build.py, xk_palette.py, xk_asr_check.py, xk_finalize.py (python -I; cv2 venv ~/YIOS-local-audits/tooling/visual-ct-scan-venv).
- Next exact operation: listening by a human (intervals = all speech 0–{sm['duration_seconds']}s); optional full-frame strips for partially viewed activities.
""")
print(vid, gates)
