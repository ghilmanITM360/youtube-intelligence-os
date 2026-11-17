# Visual CT Scan report v2 — `o3FQcd91MIs` (Casual Finance) — gold-standard pilot
<!--KEY_FACTS{
 "total_frames": 8338,
 "pts_equals_index_plus1_over_30": true,
 "boundary_events": 75,
 "single_frame_boundaries": 74,
 "black_dip_events": 1,
 "black_dip_frames": [
  7233,
  7234
 ],
 "black_dip_pts": [
  241.1333,
  241.1667
 ],
 "intra_state_events": 3,
 "content_change_events": 78,
 "states": 76,
 "stable_composition_intervals": 79,
 "shots": 47,
 "measured_episodes": 89,
 "episodes_matching_boundaries": 75,
 "episodes_unmatched": 14,
 "codec_episodes": 11,
 "iframes_total": 111,
 "periodic_iframes_outside_events": 58,
 "periodic_iframes_with_pixel_diff": 56,
 "periodic_edge_fraction_median": 0.929,
 "periodic_max_abs_diff_max": 114,
 "micro_event_max_abs_diff_min": 184,
 "classification_counts": {
  "ADDITIVE_ELEMENT_ENTRY (existing content unchanged)": 13,
  "BLACK_DIP_2F_THEN_REPLACE": 1,
  "BLACK_HOLD_ENTRY": 3,
  "BLACK_HOLD_EXIT": 3,
  "FULL_COMPOSITION_REPLACE (hard cut)": 51,
  "PARTIAL_REPLACE (some content persists)": 4
 },
 "asr_events": 78,
 "asr_median_lag": -0.053,
 "asr_within_0p2": 63,
 "asr_outside_0p2": 15,
 "asr_outside_both_runs": 11,
 "asr_outliers_disagree": 4,
 "state_frames_total": 8336,
 "min_state_frames": 20,
 "median_state_s": 3.367
}KEY_FACTS-->

## 0. Version history
| Version | Date | Content |
|---|---|---|
| v1 (checkpoint, preserved untouched) | 2026-10-24 | `visual_ct_scan_report.md`, ledgers, blueprint, `quality_gate.json` (CT_SCAN PARTIAL) |
| **v2 (this)** | 2026-10-24 | all 75 boundaries natively inspected (5-frame windows, 11 sheets); full-resolution 8,338-frame scan; codec classification substantiated; **3 missed intra-state events found and added**; 76-state specification; original-production package; substantive validator; re-verification of six difficult findings |

v2 lives in `v2/`; v1 files are unchanged (SHA list in `SHA256SUMS`).

## 1. Final independent statuses
| # | Dimension | Status |
|---|---|---|
| 1 | Technical frame coverage | **PASS** — 8,338/8,338 frames, PTS=(i+1)/30 exactly (CFR) |
| 2 | Visual-state coverage | **PASS** — 76 states (+3 sub-state events = 79 stable composition intervals) tile every frame |
| 3 | Native-frame transition verification | **PASS** — 75/75 boundaries + 3 intra-state events viewed at native frames |
| 4 | Deep art-direction & creative analysis | **PASS** — per-state records; palette/contrast measured; inferences labelled |
| 5 | Visual-to-script mapping | **PASS_ASR_UNCERTIFIED** — every state/event tied to ASR words; ASR uncertified |
| 6 | Reconstruction blueprint | **PASS** — 76 original prompts + production package |
| 7 | CT_SCAN completion | **CT_SCAN_COMPLETE_WITH_EVIDENCE** (see §7 for the contract reading) |
| 8 | HUMAN LISTENING: BLOCKED | no one has listened to the source audio |
| 9 | FULL AUDIOVISUAL SIGN-OFF: BLOCKED | requires 8 |

## 2. What changed relative to v1 (corrections, stated plainly)
1. **v1 undercounted content events.** Three real intra-state changes were folded into longer states: `+715%` text appears at f3855 (128.533 s) inside S007.1; a small figure icon at f4417 (147.267 s) inside S009.2; the word `Boring` at f4916 (163.900 s) inside S009.8. They are crisp, localized, max abs diff 184–253, not near any I-frame (see `v2/microevent_crops.jpg`). Content events are therefore **78** (75 boundaries + 3), stable composition intervals **79**. The 76-state table is kept as the parent index; the 3 splits are in `v2/intra_state_events.csv`.
2. v1's statement "87 of 89 episodes are single-frame" mixed content and codec episodes. Corrected accounting: 89 episodes = 75 boundary + 3 micro + 11 codec. Content events: 74 + 3 single-frame, 1 two-black-frame dip.
3. v1's 0.06%-of-pixels sensitivity applied to a 320×180 pass only; a full-resolution pass was added (see §4.4).
4. v1 treated the 47-shot grouping as verified; v2 labels it **INFERRED** (see §4.2).

## 3. Native-frame boundary verification (item 1)
For each of 75 boundaries the window recorded: pre-8, pre-1, the change frame(s), post+1, stable+10, with source PTS (`v2/boundary_windows.csv`, `v2/boundary_verification.csv`, sheets `v2/boundary_sheet_01..11.jpg`). Result: {'ADDITIVE_ELEMENT_ENTRY (existing content unchanged)': 13, 'BLACK_DIP_2F_THEN_REPLACE': 1, 'BLACK_HOLD_ENTRY': 3, 'BLACK_HOLD_EXIT': 3, 'FULL_COMPOSITION_REPLACE (hard cut)': 51, 'PARTIAL_REPLACE (some content persists)': 4}. All were hard replaces on a single frame except the dip. No object movement, camera movement or animation was seen in any window (no intermediate/tweened frame exists; MEASURED + VIEWED). Two windows (EV003, EV020) show slight pre-window instability that coincides with a periodic I-frame (explained, §4.3).

## 4. Re-check of the difficult findings
### 4.1 "74 single-frame replacements and one two-frame black dip" — CONFIRMED
74 single-frame boundaries; the dip is **f7233–f7234 (pts 241.1333–241.1667 s), pure `#000000`**, then arrival frame f7235 (S018.0). The three long black holds are a different black: `#110F10` with light dither (std 0.82). MEASURED + VIEWED.
### 4.2 47 shots vs 76 states — CONFIRMED AS DISTINCT, BUT SHOTS ARE INFERRED
States are measured composition intervals. The 47-shot grouping is reviewer-defined (scene/purpose). A pixel-persistence test could not separate shot boundaries (median persistence 0.02) from intra-shot changes (median 0.12), and two additive changes (EV002, EV036; persistence 1.0) are flagged as shot boundaries. So: **state timing = MEASURED; shot count = INFERRED, no verification claim**.
### 4.3 Periodic 120-frame changes as codec artifacts — SUBSTANTIATED (not assumed)
Evidence: (a) I-frames sit at 120/121-frame spacing (GOP≈4.0 s) plus scene-cut I-frames at edits; (b) 56 of 58 periodic I-frames outside event windows differ from their predecessor at full resolution, with a median 0.929 of changed pixels on edges, hundreds of tiny components, a macroblock-grid noise pattern across the entire frame (`v2/diff_maps_periodic_vs_real.jpg`), and max abs diff ≤ 114; (c) a periodic I-frame inside a zero-texture black hold (f5609) shows **zero** difference; (d) the 3 real micro-events are crisp, localized, max abs diff ≥ 184, and none coincides with an I-frame; (e) the 11 codec episodes all lie within 1 frame of an I-frame. Conclusion: codec refresh, MEASURED + VIEWED. Residual uncertainty: a real very-low-contrast change coinciding with an I-frame would be masked.
### 4.4 Sensitivity limit — UPDATED
320×180 pass: ≈0.06% of pixels (≈560 full-res px). Full-resolution pass: localized changes of ≳1.2k px at contrast ≥150 are detected (the 3 micro-events); codec noise produces ≤~600 px at contrast ≤114 near I/B frames, so **low-contrast changes below ~600 px cannot be separated from noise (blind spot)**. Nothing else exceeds contrast 150 outside the 78 events. A faint sparkle or similarly small low-contrast animation could still exist undetected (UNVERIFIED).
### 4.5 Hard cuts vs object/camera animation — CONFIRMED
0 intermediate frames at any boundary; no in-state translation/scale/rotation/opacity ramps (no frame with a localized, progressive change); camera: none. All apparent 'zooms' and 'pop-ins' are single-frame replacements. MEASURED + VIEWED.
### 4.6 ASR timing agreement and the 15 outliers — RECHECKED (ASR ONLY)
78 events: median lag -0.053 s (visual leads), 63 within ±0.2 s, **15 outside**. Two independent ASR runs (base vs small.en) agree on word starts (median 0.02 s). Of the 15 outliers, 11 are outside under both runs (genuine lead/lag, e.g. EV056 black hold begins 0.73 s before the word; EV075 end card 0.85 s after the last word) and 4 disagree between runs (timing unreliable).

| Event | Visual pts | Lag small.en | Lag base | Agreement | Nearest word context |
|---|---|---|---|---|---|
| EV007 | 18.1667 | -0.293 | -0.293 | BOTH_OUTSIDE_0.2 | [Dave's] …all -time high. Dave's hobbies include watchi |
| EV009 | 24.6667 | -0.233 | 0.207 | BOTH_OUTSIDE_0.2 | [and] …emerging biotech companies, and zinning. It's sa |
| EV010 | 25.6667 | 0.407 | 0.407 | BOTH_OUTSIDE_0.2 | [It's] …companies, and zinning. It's safe to say,… |
| EV013 | 37.4333 | -0.207 | -0.167 | ASR_DISAGREE | [Fast] …for options trading. Fast forward three months, |
| EV017 | 46.9 | -0.32 | -0.2 | ASR_DISAGREE | [His] …risk management? Prayer? His wife's concern? Why |
| EV018 | 51.4 | -0.3 | -0.28 | BOTH_OUTSIDE_0.2 | [forward] …savings account? Fast forward three more mon |
| EV028 | 99.5667 | 0.227 | 0.267 | BOTH_OUTSIDE_0.2 | [fundamentals] …investing is about fundamentals or fair |
| EV029 | 101.2 | -0.24 | -0.2 | ASR_DISAGREE | [valuations.] …fundamentals or fair valuations. But the |
| EV032 | 109.2333 | -0.207 | -0.087 | ASR_DISAGREE | [ride] …650 times earnings, ride trends that make… |
| EV041 | 146.0667 | 0.227 | 0.247 | BOTH_OUTSIDE_0.2 | [outperformed] …irrational approaches have outperformed |
| EV047 | 160.2333 | -0.207 | -0.227 | BOTH_OUTSIDE_0.2 | [sit] …ways. The first, sit on cash like… |
| EV056 | 190.7667 | -0.733 | -0.573 | BOTH_OUTSIDE_0.2 | [And] …dumbest investors win? And the answer is… |
| EV061 | 206.2667 | -0.313 | -0.253 | BOTH_OUTSIDE_0.2 | [Here's] …as a whole. Here's a real example… |
| EV062 | 216.2667 | 0.227 | -0.213 | BOTH_OUTSIDE_0.2 | [33] …saying Amazon is 33 % more volatile… |
| EV075 | 272.3667 | 0.847 | 0.867 | BOTH_OUTSIDE_0.2 | [market.] …in a bull market.… |

Automated timestamps are **not** listening and are not presented as verified.

## 5. Measured / inferred / uncertain
- **MEASURED:** frame count, PTS, CFR; 75 boundaries + 3 micro-events (frame, pts, size, location); black colours; palette, contrast, content coverage, centroids; I-frame structure; ASR lag numbers.
- **OBSERVED (viewed frames):** poses, objects, text, layout, hard-replace nature, absence of tween/camera.
- **INFERRED:** story purpose, attention hypotheses, shot grouping, intent of callbacks, cause of the faint off-white matte near some inserts, font families.
- **UNCERTAIN / UNVERIFIED:** small text in 9 states (S001.4, S001.8, S001.17, S002.0, S004.0, S005.1, S007.2, S009.14, S021.1); sub-600 px low-contrast motion; ASR wording; audio (music/SFX/mix); live thumbnail; finance figures on cards (not fact-checked).

## 6. Deliverables (all in this folder)
`v2/state_spec_76.csv|md` (76 forensic records) · `v2/original_prompts.md` (76 original prompts, no source IP) · `v2/ORIGINAL_PRODUCTION_PACKAGE.md` · `v2/boundary_verification.csv` · `v2/intra_state_events.csv` · `v2/audio_visual_alignment_v2.csv` · `v2/quality_gate_v2.json` · `v2/validate_v2.py` · `v2/key_facts.json` · v1 files preserved.

## 7. CT_SCAN contract reading (not redefined to obtain PASS)
The skill's CT_SCAN mode (SKILL.md) = DEEP + sub-second frame-event ledger with source PTS/frame index + object/camera/motion timeline + audible synchronization + per-state prompts + creative grammar + uncertainties + formal completeness audit. Reference 13 defines the temporal gate (every meaningful state/transition at PTS precision, dense checks of ambiguous windows, explicit unseen gaps) and the creative/reconstruction gate (per distinct state prompts, editor blueprint). Its **audio gate** requires human listening only for `FULL_AV_SIGNOFF_COMPLETE`; reference 07 explicitly allows delivering synchronization as `ASR_ONLY_NOT_AUDIO_VERIFIED`. Therefore listening is not an explicit prerequisite of CT_SCAN, and the verdict is **CT_SCAN_COMPLETE_WITH_EVIDENCE** for the *visual* CT-scan contract, with the audio-synchronization element labelled ASR-only. **If the owner reads 'audible synchronization' as requiring listening, the correct status is CT_SCAN PARTIAL until a listener signs off.** Frame coverage is 33.3 ms (every frame); the 100 ms coverage question is moot.

## 8. Remaining limits
Human listening BLOCKED; AV sign-off BLOCKED; shot grouping inferred; small-text items flagged; low-contrast micro-motion blind spot; OCR deferred; single-video pilot (no channel DNA).
