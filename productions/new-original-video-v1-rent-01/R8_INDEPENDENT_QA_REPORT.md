# V1 Rent R8 full-video independent QA report (2026-11-21)

Subject: `out_full/V1_RENT_FULL_R8_assembled.mp4`, sha256 `f7f11071c70ad02fab71a6e557a36d0c74d15b89754c6b752c65d26d1c13688b`.
Reviewer: separate read-only vision subagent (agent a4543690f22ace7c1) on 143 frames (2 s step) and 14 boundary frames, plus my own checks.
Limits: the reviewer cannot hear. No audio-quality claim is made. Frame names are about 1-2 s off the stated times, so times below are +/-1.5 s. Not done: 4-5 fps full scan, pixel check of every cut, review against doc 22 itself.

Status: NOT publication-approved. Human audio-seam check PENDING. Factual review and owner approval OPEN.

## Technical (passed)
- 1920x1080, 30 fps, 8581 frames, video 286.033 s, audio 286.016 s. The 0.017 s gap is one video frame of rounding. Last narration word ends 285.55 s; the audio tapers to silence by 285.9 s. Not truncation.
- Full decode: no errors. Joins at 75 s, 122.3 s, 147.6 s, 199.5 s, 257 s are clean hard cuts, no flicker or ghosting.
- Seam at 124 s: video is clean (brief white frame at about 124.4 s). Audio seam: **PENDING human listen** (`qa_r8/audition/AUDITION_118-132s_*`).
- On-screen numbers match registers and tsv (2.8, 2.7, about 3, 7.7/25.9/35.3, $1,913, $1,859, +2.9, +2.7, +0.2). Weight bars are to scale.

## P1 (blocking)
| # | Time | Defect | Fix |
|---|---|---|---|
| P1-1 | S090, 251-256.7 s | Narration "matches the market measure today within a fraction of a point" is true for September only (2.8 vs 2.7). October has no BLS 12-month figure, and S087 says so. A screen label "Sept" does not fix a spoken claim. | Owner decision: trim candidate `audio/take2_edited/candidates/CANDIDATE_S090_trim_cut250.95-254.25.wav` (sha 0521dd42...63e75, -3.32 s) or re-record. |
| P1-2 | S099, 282.3-285.6 s (frames f_0142-0143) | Narration and closing text say "every number on screen carries its source tag". Untagged numbers: "+2.8%" (~193 s), red "+2.8%" (~199 s), Zillow "+2.9%" (~243 s). | Add source tags to those three frames (no audio change). Reviewer's alternative, softening the line, would need a re-record, so not chosen. |
| P1-3 | Whole video | Publication checklist items open: human seam listen, owner approval, font licence, BLS evidence not preserved (`evidence/bls/` is empty). | See checklist. |

## P2 (important)
| # | Time | Defect | Proposed action |
|---|---|---|---|
| P2-1 | ~211-215 s | BLS-tagged icon shows "CPI rent trails market rents" in quotes with "Source: BLS factsheet". Reads as a BLS statement; the narration says BLS never said it. Red strike covers only "CPI". | Remove quotes, label "claim we looked for", strike whole phrase, tag "searched: BLS factsheet". |
| P2-2 | ~147 s | "not this" red line sits under "average price of a home" between the lines; reads as an underline. | Strike through both lines or add an X. |
| P2-3 | ~243 s | "no October 2025 BLS data was collected" is on screen, unnarrated and unexplained. | Use narrated wording "BLS printed no 12-month change". Check wording against register C-18. |
| P2-4 | ~23 s, ~35 s | Clipped descenders on "y" ("They answer", "Every month"), in frozen R7 scenes. | Re-render those two scenes only (or accept as P3 if the owner prefers). |
| P2-5 | many | Hand font "g" reads as "q"; "9" in $1,913 and +2.9% can read as "q". Numbers are the core of the video. | Check at phone size. Font change would touch everything, so decide with the owner. |
| P2-6 | ~226 s vs ~193 s | Bar charts use different px per percent (2.8% bar about 170 px, +0.2% about 40 px) with no axis. | Add "not same scale as previous chart" or use one scale. |
| P2-7 | ~221 s | BLS colour flips (olive in most places, orange here; orange also means other things). | Recolour that chart. |
| P2-8 | whole video | Zero authentic source imagery (0 of 143 frames). All documents are drawn. Room plate (~19-21 s) is a raster style outlier with unclear provenance. | See source-imagery assessment below. |
| P2-9 | script headers | Working title "Prices Each Home Every Six Months" implies every rental is measured. BLS samples units and reprices each sampled unit about every six months. | Retitle, e.g. "Why Is Rent So High? How the Official Rent Number Is Measured". Not in the video itself. |

## P3 (minor, document and accept)
Pie wedge animates through unlabeled sizes (~67-69 s). Overlaps: arrow over "Rent" (~47 s), circle over "Shelter" (~65 s), "PANELS" crowding tag (~93 s), "six-month steps" touching Jul box (~143 s), "≠" colliding (~272 s), "illustration, not to scale" touching text (~199 s). Tight edge margins (x=938/960 at ~87 s, 932/960 at ~193 s). Near-empty holds at ~124.4, ~217, ~233, ~263, ~275 s and a static final 4 s (mostly pauses in the narration). Host scale jump at 122.3 s (intentional).

## Source imagery assessment
- Authentic imagery in R8: none. Attribution is by text tag only.
- Proposed inserts (only if they add viewer value, nothing fabricated, never block release):
  1. BLS CPI release table row for rent of primary residence (capture needed in `evidence/bls/`).
  2. Zillow Research data page / ZORI chart crop, from the preserved CSV (can be redrawn from our CSV with attribution rather than screenshotted).
  3. BLS Handbook of Methods page on housing survey sampling and six-month repricing.
- None is added until captured and verified. `evidence/CAPTURE_REQUEST.md` lists the capture.

## Fix plan (nothing rendered yet)
Audio decision P1-1 changes timing after 251 s, so all fixes touching segment 6 (257-286 s) wait for it. Visual fixes P1-2, P2-1/2/3/6/7 sit in segments 3-6 and can be done in one re-render of the affected scenes, followed by reassembly and a focused regression check. R7 and R8 baselines stay preserved.
