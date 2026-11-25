# 03 Corpus completeness (all numbers from `03_CHANNEL_MASTER_INVENTORY.csv`)

Catalog basis: census snapshot 2026-11-04 (91 videos: 45 long, 46 Shorts, 0 live) + the 2026-11-17 upload Aony69nO5kI = **92**. A live RSS fetch on 2026-11-23 (latest 15 only) shows no newer upload. A full live recount was not possible (no browser/API pass was run), so "92" is current only up to that RSS check. 83 is the transcript count, not the channel count.

| Measure | Count |
|---|---|
| Videos inventoried | 92 (45 long, 46 Shorts, 1 unclassified) |
| Videos with full local media (this Mac) | 88 (44 long, 44 Shorts) |
| Videos with catalog transcript | 83 (43 long, 40 Shorts), untimed |
| Videos with provisional local ASR | 64 |
| Videos with any transcript | 86 of 92 (83 catalog + 3 with provisional ASR only: 9VG0yqq_PHM, TIDHee_Q5Gk, 35KZm1yiyIE) |
| Missing media | 4 |
| Script-audited (V001-V083) | 83 |

Visual evidence tier (directive scale), from existing campaign outputs, **not** from new work in this audit:

| Tier | Count | Meaning here |
|---|---|---|
| DEEP_VISUAL | **0** | No video has CT_SCAN_COMPLETE, listening, or full native-frame review |
| TARGETED_VISUAL | 44 (24 long, 20 Shorts) | every frame measured, segments classified by a model reviewer, native views partial, per-video `quality_gate.json` = VISUAL_ANALYSIS_PARTIAL |
| STRUCTURAL_ONLY | 20 long | measurement tables only (population-6, frozen v4 ranges, 116/120 checks pass) |
| TRANSCRIPT_ONLY | 22 Shorts | media exists, no visual analysis |
| MEDIA_ONLY_NO_ANALYSIS | 2 Shorts | media, no transcript, no analysis |
| UNAVAILABLE | 4 | no media |

Unmet by anything on disk: audio listening for all 92; human-verified narration timing for all 92.
