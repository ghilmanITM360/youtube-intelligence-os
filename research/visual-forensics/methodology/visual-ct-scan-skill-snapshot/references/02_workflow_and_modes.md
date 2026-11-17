# 02 — Operational workflow, modes, scale, checkpoint and acceptance

## Start with exact context

1. Identify Machine A/B, current repository root/HEAD and assigned writer; do not switch the active Finance branch just to analyze video.
2. Confirm source file, YouTube ID, provenance, SHA256, manifest version, duplicates and local-only dependency availability.
3. Check live five-hour usage (90%-used threshold), weekly (95%-used threshold), context warnings, and disk. Record unavailable indicators honestly. If imminent, only create safe handoff.
4. Reconcile the per-Video-ID YIOS ledger and historical work (including exact source hashes), avoid repetition.
5. Define mode and `coverage_contract` in writing. Different modes have different completion labels.

## Progressive cost budget

- Inventory thousands of files with hashes/ffprobe/metadata; **not** full high-cost decoding.
- Structural overview (full beginning to end, 1fps or adaptive baseline + boundaries) per selected video.
- Candidate detection (cuts / states / text / object motion) as index, not truth.
- DEEP: verify meaningful candidate states across complete source, dense sampling of tiny/ambiguous intervals, original motion where available, and active missing-event search.
- CT_SCAN: contiguous full video shot/state timeline and native-frame intervals on significant visual changes. Report whether 100ms coverage was achieved across entire video; 100ms sampling is not frame-accurate at 30/60fps. Do not write one huge textual paragraph per frame when nothing changes.
- Reconstruction: editorial blueprint and original prompt system from verified facts.
- Channel: minimum multi-video variety, supporting cases, counterexamples, temporal/format cohorts, caveats.

## Stage gate transitions

`SOURCE_AVAILABLE` → `STRUCTURAL_ANALYSIS_COMPLETE` → `VISUAL_ANALYSIS_PARTIAL` → `VISUAL_ANALYSIS_COMPLETE` (per existing YIOS contract) → `AUDIO_REVIEW_PENDING`/`AUDIO_REVIEW_COMPLETE` → `FULL_AV_SIGNOFF_COMPLETE` only with actual qualified full AV review. `HISTORICAL_UNVERIFIED` and `IDENTITY_UNVERIFIED` remain separate; never promote based on claims alone.

No forced status promotion: If unresolved event timing or uninspected gaps remain, `VISUAL_ANALYSIS_PARTIAL`. A transcript spot-check never replaces audible listening. A sample cannot certify whole-channel review.

## Per-video phase plan

A ingest; B temporal coverage; C shot list; D state/event ledger; E design, illustration and typography; F camera/motion/facial; G transitions/story/script alignment; H sound; I attention hypotheses; J production reconstruction; K error/improvement scorecard; L validate and seal.

Every phase must write direct evidence and `PASS/PARTIAL/BLOCKED/NOT_APPLICABLE` for relevant gate. On a pause, record next precise ID/time range, source SHA and known replay/analysis commands.

## Domain applicability map

Cartoon: character, line/silhouette, animation, facial, gesture, layered 2D camera; live action: lens/lighting/blocking; infotainment: charts and text; AI imagery: temporal consistency with uncertain origin; Shorts: first-second hook + short-lived overlays; long-form: chapter pace and visual motif cadence. Apply relevant domains explicitly, mark irrelevant ones N/A, never omit quietly.

## Disk and external evidence

Prefer bounded sheets + dense-window clips, not unbounded image extraction. On reported Machine B only ~28 GiB free / 97% used in latest source handoff: recheck live disk. Do not duplicate 454 MP4s or overwrite external evidence. Quote the source folder with **trailing space** `"/Users/ghilmanislam360/Downloads/all channels videos data /"` whenever copying actual paths.
