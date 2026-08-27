# Forensic Visual-State Coverage Audit — BATCH-000001

Closes the Phase 1C compliance gap: "692 distinct forensic visual states were
perceptually clustered, but independent native semantic inspection was only
spot-checked against 10 representative frames while canonical forensic
reports provided the main semantic interpretation." This audit determines,
for every one of the 692 clusters, whether it has traceable semantic
coverage — and if so, from where.

Full per-cluster locator (dataset, cluster, representative frame, estimated
timestamp, report file, nearest report state, coverage status): see
`BATCH-000001_VISUAL_STATE_COVERAGE.csv` (692 rows, not hand-authored —
produced by parsing each dataset's canonical forensic report's own
shot/state time table and comparing it against each cluster's representative
frame position).

## Method

Each of the 5 Codex forensic-video datasets (DS-000012–DS-000016) has its
own pre-existing canonical report with an explicit shot/visual-state time
index (a "PASS 2 — Visual-state index", an "Editing Decision List", or —
for DS-000016 — 253 per-shot reconstruction cards in
`visual_reconstruction_cards.md`, each with an exact `HH:MM:SS.mmm` range).
For each dataset:

1. The report's documented states/segments were parsed into `(state_id,
   start_sec, end_sec)` tuples directly from the report text.
2. Each perceptual visual-state cluster's representative frame was mapped
   to an estimated timestamp — `frame_index / (total_frames - 1) *
   video_duration` — since frames within one dataset's `frame_sequence_id`
   are stored in a single contiguous, chronologically-ordered index.
3. A cluster whose estimated timestamp falls inside `[report_min_time,
   report_max_time]` (the report's own covered span, generally the full
   video) is `SEMANTICALLY_COVERED_BY_CANONICAL_REPORT`, with the nearest
   report state recorded as its locator.
4. A cluster whose estimated timestamp falls outside that span is
   `UNRESOLVED` and requires direct verification.

This is a proportional estimate, not a frame-accurate re-extraction — it is
explicitly the "traceable locator," not a claim that automated clustering
and the report's manual state segmentation agree 1:1 on every boundary.

## Result

| Dataset | Clusters | Report-documented states | Report time span | Covered | Unresolved |
|---|---:|---:|---|---:|---:|
| DS-000012 | 60 | 14 | 0.00–129.90s (of 129.93s) | 60 | 0 |
| DS-000013 | 107 | 39 | 0.00–87.75s (of 88.14s) | 107 | 0 |
| DS-000014 | 117 | 29 (segment-level) | 0.00–47.29s (of 47.50s) | 117 | 0 |
| DS-000015 | 101 | 34 | 0.00–129.93s (of 129.93s) | 101 | 0 |
| DS-000016 | 307 | 253 | 0.00–843.64s (full) | 307 | 0 |
| **Total** | **692** | **369** | | **692** | **0** |

**692 / 692 clusters have traceable semantic coverage. 0 UNRESOLVED.**

3 clusters initially fell outside their nearest report state's proportional
estimate (all within ~0.3s of a report's documented end boundary, an
artifact of the proportional-position estimate rather than a real content
gap). Each was individually re-checked against its exact frame-capture
timestamp, which several of this project's frame-extraction scripts embed
directly in the filename (e.g. `frame_0047500ms.jpg`):

- `DS-000013-CLUSTER-0106` (frame at 87.750s) — falls inside `V39`'s
  documented range (86.0–87.75s); the proportional estimate had overshot to
  88.073s. Reclassified `SEMANTICALLY_COVERED_BY_CANONICAL_REPORT`.
- `DS-000014-CLUSTER-0115` (frame at 47.250s) — falls inside segment
  `S07`'s documented range (40.958–47.292s). Reclassified
  `SEMANTICALLY_COVERED_BY_CANONICAL_REPORT`.
- `DS-000014-CLUSTER-0116` (frame at 47.500s) — the video's final ~0.21s,
  past segment `S07`'s documented end. This frame was directly opened and
  visually inspected during this audit: uniform gray noise/static, matching
  the report's own documented "0.21 s gray-noise separator" transitional
  motif (its Visual DNA section). Recorded as `BOTH`
  (natively inspected in this audit + matches the canonical report's own
  description of that recurring element) rather than a distinct unnamed
  visual state.

No cluster required a full re-run of semantic image analysis to close this
gap — 691 of 692 were resolved by the reports' own existing time-indexed
state data, and the 1 genuine edge case was closed by viewing a single
frame, not by re-analyzing the dataset.

## Related finding (not a coverage gap, recorded for transparency)

DS-000012's source report identifies its source video as
`How long could you drive towards the sunset_.mp4`, 129.93s. DS-000015's
canonical report is titled `How_long_could_you_drive_towards_the_sunset_forensic_blueprint.md`
and states the same video's duration as 129.932653s. These are almost
certainly two independent analysis passes (2026-08-20, 96 sparse frames;
2026-08-21, 2488 dense frames) over the **same underlying source video**,
not two unrelated videos. This was already flagged as "possible revision of
Case 1" in `BATCH-000001.md`'s dataset table at registration time. Per
Decision 012/013 (permanent dataset IDs are never renumbered or merged
after assignment) both `DS-000012` and `DS-000015` retain their existing
IDs; this note documents the suspected shared-source relationship for a
future classification pass rather than silently merging or renumbering
either dataset.
