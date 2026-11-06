# RT4_916 — whole-render silent visual review (post-attempt-1 sufficiency check) and attempt 2
Reviewer: orchestrator (Claude, same model family as the render worker; no human; **silent, no audio**). Frozen criteria: ACCEPTANCE_CRITERIA_RT4_916.md (sha a27f4b41…, unchanged). Not continuous playback: no playback capability here and the frozen criteria require "render sheets/frames", not playback; frame samples are NOT called playback.

## 1. Were the original 8 frames sufficient for V1–V4?
Letter of the frozen rule ("reads >=2 render sheets/frames"): yes. For the claims V2 (no clipping) and V4 (no collisions) and the owner-requested scene/transition/lower-panel inspection: NO, 8 of 1440 frames cannot show them. attempt_1 V1–V4 were therefore PROVISIONAL (sample-only); this review supersedes that with the coverage below.

## 2. Coverage of this review (attempt_1 and attempt_2 each)
- Programmatic over ALL 1440 frames (rv_full/full_render_scan.py -> full_render_scan.csv + _summary.json): V1 anchor proxy (teal banner colour present) 1440/1440; V2 proxy: non-background pixels outside the safe margins (y<116, y>1705, x<55, x>1025; panel borders sit at the safe-zone edge by design) 0 frames; lower-panel content series. Proxies, not visual judgement.
- Visual: 62 stride-24 frames (A1/A2 sheets, f0..f1439), before/after pairs for all 26 intended events (B1–B4, 52 frames), slide transition frames f700/f703/f706 at 0.44 scale, f1200 bottom panel at full panel res, f1371/1380/1439 top panel. Never every frame.
- Scene/event boundaries: all 26 intended events show a visible before/after change (pop-on, write-on, stroke, swap, slide). No dissolve/cut: the render has one scene, two panels.
- Transitions: the only transition is the 8-frame bottom-panel horizontal slide with blur (f700–707); f700/703/706 show smeared text sliding left, the next scene entering empty. As intended.
- Text clipping: none seen; SHADOW FOREST label clears the arc and the left marker (f1200 full panel); the f720 "pebble clipped at left edge" earlier note refers to the blurred slide-in frame only.
- Layout continuity: banner, both panel frames and baselines are constant on every sampled frame; only content changes.

## 3. Lower panel: intentional or missing content?
Measured: lower panel carries only its baseline line on 333/1440 frames (23.1 %): f0–269 and f707–769. Evidence it is by design: RT1_intended_timeline.csv (written by make_rt4.py before measurement) schedules the first lower-panel event at f270 ("bottom: large pebble narrator pops on") and the post-slide scene's first content at f770 ("sun-path arc pops on"); the spec (spec_s8_s9.md) allows landscape-style panels with empty areas for Shorts (source Ny9m2l6h478). So: intentional per the intended timeline, NOT missing content. It remains a design weakness (a held, blank half-canvas for 11.25 s at the start and 2.6 s after the slide); the frozen criteria do not require lower-panel content, so no failure is declared.

## 4. M4 unmatched event reconciled (attempt_1: 25/26)
Unmatched: intended f1372 (GOOD NIGHT write-on 1372–1379), nearest measured f1316 (delta −56). Not a render miss: frames 1372–1379 contain the write-on (px_diff_ge12 ≈ 1206 at f1372, text absent f1371, present f1380 — rv_full/f1371_f1380_f1439_top.png). The segmenter classified f1372–1379 as ENCODER_REFRESH (D3-only, px_diff_ge150==0, max_abs_diff 65 < 80; the artifact rule's own text says "visual spot-check required") because teal #1F8A8A on the navy night panel is low contrast. No tolerance issue (the ±2 frame tolerance was not the cause). Defect class: low-contrast label = weak legibility + invisible to the source measurement rule. Frozen M4 for attempt_1 stays PASS (25/26 = 96 % ≥ 80 %, 0 unexplained onsets).
Pipeline limitation (applies beyond RT4): a low-contrast write-on can be absorbed as encoder refresh by the D3-only artifact rule; source-video event counts could be under-counted on dark/low-contrast panels. Not quantified on the 20+ source videos here.
Threshold note: attempt_1 RT_EVALUATION.json contains xk_rt_eval's older built-in targets (events/min 18.4–39.2, hold 1.13–2.84); the verdict in RT_EVALUATION.md used the FROZEN M2/M3 ranges (17.9–28.2 and 1.44–2.84). Re-scored here against frozen: attempt_1 26.0 and 2.00 s PASS; attempt_2 27.0 and 2.00 s PASS.

## 5. attempt_2 (versioned; attempt_1 untouched)
Change: one colour (GOOD NIGHT TEAL -> ink 235) in make_rt4.py (diff in attempt_2/ATTEMPT_2_NOTE.md). Pixel diff vs attempt_1: only frames 1372–1439 differ (68 frames). mp4 sha256 e50b19522cf552321e59899ffe5838fefb9eff5c2d726f836e74663438ce0c6d (local-only). Measured with the unchanged source pipeline:
| Check | attempt_2 |
|---|---|
| M1 | PASS h264 yuv420p 1080x1920 24/1, 1440 frames |
| M2 17.9–28.2 | PASS 27.0 (27 measured activity segments: 26 intended events; the 644 stroke is measured as two segments, same as attempt_1) |
| M3 1.44–2.84 s | PASS 2.00 s |
| M4 ≥80 %, 0 unexplained | PASS 26/26, all delta 0, 0 unexplained |
| M5 | PASS (first segment blank board under banner 30 f, last segment HOLD; no card seen in any sampled frame) |
| V1 | PASS: stacked panels, banner 1440/1440 frames |
| V2 | PASS: 0 frames with ink outside margins; visually no clipping |
| V3 | PASS (pebble narrator, teal, no stick figure/red/dinosaur/what-if; tree/sun/moon more detailed than the pebble) |
| V4 | PASS on 113 reviewed frames; GOOD NIGHT now light and clear of stars |
Verdict: attempt_1 RT4_916_PASS_PORTRAIT now supported by whole-render proxies + 113 viewed frames (previously 8); attempt_2 RT4_916_PASS_PORTRAIT with 26/26 events. Scope unchanged: portrait silent rhythm/format/composition only; no narration sync, audio, story quality; not a continuous-playback review; same-model-family reviewer; weaknesses: 23 % blank lower panel, night labels LEFT BEHIND/SHADOW PILEUP still teal on navy (~3:1 contrast, not changed).
