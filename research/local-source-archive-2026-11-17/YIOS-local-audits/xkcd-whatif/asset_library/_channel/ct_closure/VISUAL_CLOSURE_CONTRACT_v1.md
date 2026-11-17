# Per-video visual-only closure contract v1 (xkcd What If; LOCAL ONLY)

Frozen before the first closure of this pass (stamp in `VISUAL_CLOSURE_CONTRACT_v1.sha256`).
Maps kit reference 13 gates + the campaign per-video contract (CAMPAIGN_GOAL_v1 "Per-video contract") to
checkable criteria. Existing per-video files (quality_gate.json, ledgers, blueprints) are NOT edited; closure
evidence goes to `videos/<id>/closure_v1/` and a new `quality_gate_visual_v1.json`.

## Required visual gates (all must be PASS for VISUAL_ANALYSIS_COMPLETE)
| Gate | Criterion (PASS) | Reuse from rv1 |
|---|---|---|
| V1 source_identity | sha256 of the source file re-computed this pass == source_manifest.json; decoded frame count == ledger last frame + 1 | manifest |
| V2 full_temporal_overview | every decoded frame measured; segments cover every frame exactly once | FULL_FRAME_MEASUREMENTS + segments_v1 (re-checked by script) |
| V3 candidate_shots_verified | every shot cut in shot_ledger viewed (before/after native frames) | rv1 tiles + native before/after |
| V4 meaningful_state_timing | 0 UNRESOLVED segments and 0 unviewed activity frames: every rv1-listed unresolved or unviewed interval viewed at native resolution (frame f-1, f.., f+1) with a written resolution | rv1 onsets (frame-precise) |
| V5 motion_design_review | every ACTIVITY frame viewed (rv1 "all activities viewed at every frame" or closure native view); multi-frame activities have a measured per-frame progress curve (changed px vs previous frame); holds measured still (max changed px within holds reported) | rv1 |
| V6 creative_design_review | every distinct HOLD state viewed at >= 1/2 scale; every on-screen text string read at native resolution and transcribed; palette measured; object continuity across consecutive states checked and any INFERRED claim (e.g. camera drift) confirmed or refuted by measurement | palette_measured.json |
| V7 production_blueprint | per-state image prompt for every distinct HOLD state, corrected to the native review; motion/timing per event from the ledger; continuity rules; QA tests; ORIGINAL-transfer note (no source logo, lockup, name, characters) | reconstruction_blueprint.md (rv1) |

## Separate, NOT required for visual-only closure (reported, never merged)
- visual_script_mapping: depends on narration; stays ASR_UNCERTIFIED / PARTIAL (audio-dependent).
- audio_human_listening, final_av_signoff: BLOCKED_CAPABILITY. Never CT_SCAN_COMPLETE, never FULL_AV_SIGNOFF.
- Held-out rule scores (v7/v8/v9) are rule tests, not per-video gates.
- Per-video render test of the reconstruction is NOT required by ref 13 (prompts + timeline + QA are); stated as not done.

## Status vocabulary
`VISUAL_ANALYSIS_COMPLETE` (visual-only, V1–V7 PASS) — implies nothing about sound.
Otherwise stays `VISUAL_ANALYSIS_PARTIAL` with the failing gate and exact blocker.
Milestone: 20 videos VISUAL_ANALYSIS_COMPLETE under this contract.
Native-frame source: ffmpeg decode of the verified source (frame index = decode order, CFR 24/1), no bulk dumps (only listed frames).
