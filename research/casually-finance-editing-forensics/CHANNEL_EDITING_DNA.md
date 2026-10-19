# Casually Finance — Channel Editing DNA (PRELIMINARY; most statistics n = 12 of 48 local videos, era split refreshed at n = 14; snapshot 2026-10-20)

Source: `EDITING_TIMING_STATISTICS.csv`, `MOTION_OPERATION_TAXONOMY.csv`, per-video `videos/<id>/*`. **Denominator:** 12 validated Shorts (13.8 min, 22,231 native frames) of 48 local videos (10 long-form + 38 Shorts) of 210 public. All are Shorts; no long-form has been analysed in this phase, so nothing below describes the long-form videos. Depth mix: 2 × A, 6 × B (one coarse), 4 × C (`UNRESOLVED_CHANGE` rows: 158 events, 22-25 % of frames in the three least-resolved videos). Selection was by public views and layout diversity, **not random**; every statement is a sample finding, not a channel-wide law. Evidence labels: `DIRECTLY_OBSERVED`, `MEASURED`, `ART_DIRECTION_INFERENCE`, `PLAUSIBLE_HYPOTHESIS`, `UNKNOWN`. The 16 videos of the earlier Oct-12 corpus (`codex/casually-finance-forensic-research`) are `REFERENCE_SUPPORTED` context and are not merged into these numbers.

## A. Patterns seen in all 12 validated videos
| Pattern | Evidence (n = 10 unless stated) |
|---|---|
| **One-frame composition replacement is the dominant edit.** 237 `HARD_CUT_REPLACE` events (12/12 videos): every one swaps the whole stage between two consecutive frames, no fade, wipe or blend. | `MEASURED`: from ~7 % of the frame (sparse scenes) to >50 % (screenshot scenes) changes on one frame, on a mostly white canvas. 237 of 720 events; 494 of 720 events last one frame. |
| **Cut rate 12-29 per minute, median ~16.5.** Scene median 1.7-4.1 s (median of medians 2.83 s). | `MEASURED`, per-video table. Era split (current CSV, n = 14: 4 banded, 10 full-bleed): banded median 21/min (range 10.6-29), scene median 1.9 s, static share 82 %; full-bleed median 16/min, scene median 2.9 s, static 72 %; ranges overlap, so this is a tendency in a small sample, not a rule. |
| **Pops, not tweens, build explanations.** 108 `POP_IN` (10 videos) + 46 `OVERLAY_POP` (9 videos): props, numbers, X marks, bubbles and bills appear fully formed in one frame (2-4 frames when sequenced). | `MEASURED` counts; no scale/opacity easing visible at 30 fps sampling in the one-frame cases. |
| **A static canvas most of the time.** 75 % of all frames contain no stage change (range 58-92 % per video; pooled 75.1 %). | `MEASURED` frame-weighted; holds are intentional in the sense that every hold sits between authored events (QA check). |
| **Visuals meet or lead the voice.** Hard cuts precede the nearest ASR word onset by a median 76 ms (p10 -204, p90 +67; 55 % within +-100 ms; n = 238 cuts in 12 videos); captions land on ASR onsets (median +33 ms, 79 % within +-100 ms in the 2 first banded videos; later banded videos give medians +20 to +44 ms, 73-80 % within ±100 ms). | `MEASURED`, ASR uncertainty ~100 ms; sign convention: negative = visual first. |
| **White canvas, hand-lettered text, flat vector props and characters.** | `DIRECTLY_OBSERVED` in 12/12 (counterexamples: dark quote cards, photographs, logos used as inserts). |
| **Source evidence inside the explanation.** Screenshots/charts/documents appear in 12/12 videos (see `ASSET_FAMILY_LIBRARY.csv`) with push-in, scroll, highlight or pop-on callouts. | `DIRECTLY_OBSERVED`. |

## B. Conditional patterns
- **Scroll/zoom of an evidence screenshot** (36 events in 8 videos, 1,461 event-frames, the largest resolved motion budget): used when a document or chart must be read; precedes or accompanies a presenter pop-in. The two numerically fitted push-ins differ: one is **linear** (scale 1.00→1.52 in 0.87 s) and one **decelerates** (1.00→1.43 in 1.7 s); `MEASURED`, `Qof71Ef-3EU`.
- **Progressive stroke/line draw** (13 events in 5 videos): falling price lines and chart lines are drawn left to right; the measured draw (`7bm7XYssqlU`, f0-29) is **linear** at ~0.027 frame widths per frame.
- **Counting by sequential pops** (bills on a timeline, DEBT documents, buildings, houses): each unit appears on a keyword; 1 unit per 6-25 frames.
- **Highlight sweeps** over quoted text (11 events in 5 videos), 10-30 frames each, approximately linear growth (`MEASURED`, two cases).
- **Callback repetition** of the same two scenes for a repeated sentence (`Qof71Ef-3EU`, 0 s and 26 s).
- **Layout era dependent features** (see D).

## C. Rare / specialised (more complex animation)
- **Money-rain overlay** (`mT2hOLrCYSk`): dozens of overlapping banknote layers change every frame for 85-115 frames, three times; **pixel-identical across the three segments** (first-frame correlation 1.000) so a single clip is reused, trimmed to the phrase (`MEASURED`). Not found in any other analysed video (maximum correlation 0.61, i.e. unrelated content).
- **Door swings** (2), **torn bond tag** (1), **knife rotation** (measured: -60° in 7 frames then +48° in 8 frames, two opposite easing directions in one gesture; `RB5zVghPor8`), **bag-character run cycle** (1), **screen-recorded hover tooltip** (3 events, 1 video, `PLAUSIBLE_HYPOTHESIS`).
- **Opacity fade** (1): black circle to white, 22 frames, linear in 10.7 gray-level steps (`MEASURED`, `DEgQTSsSX9U`).

## D. Counterexamples and drifts
- **Layout eras (sample).** Banded era = persistent two-line headline + bounded stage + caption band (`Qof71Ef-3EU` 09-08, `DEgQTSsSX9U` 09-15; automatic layout profiling also flags 6 further Shorts dated 09-05..09-14, not yet analysed). Full-bleed era = no persistent headline, hand-lettered captions that move per scene (08-21 with a 4-s title; 09-02 with a 6-s title; 09-25 onward without a title). `DIRECTLY_OBSERVED`/`MEASURED`; sample only.
- **Frame cadence drift.** The Aug 21, Sep 2, Sep 8 and Sep 15 videos are a 24 fps timeline conformed to 30 fps by repeating every fifth frame (`MEASURED`); the Sep 25-Oct 18 videos are native 24 fps (one of them, `RB5zVghPor8`, unresolved). Author at the target's delivery rate and expect duplicates if you export 30 fps.
- **Sparse versus dense screens.** `44ggG2I6JPY` has only ~7 % of the frame changing at cuts (small objects on white) versus 25-60 % on screenshot-heavy Shorts, so any pixel-based cut threshold must be per-video.
- **No fade/dissolve or camera shake was found between scenes** in 12/12; the only gradual effects are the zooms, strokes, highlights and one opacity fade above.

## Keyframe-compatible versus complex motion (duration-weighted; user hypothesis 70-80 % / 10-20 %)
Frame-weighted over all 22,231 frames (12 videos): static hold 75.1 %, plausibly conventional 2D keyframe/compositing 17.0 %, complex continuous animation 1.8 %, undetermined method 5.7 %, screen recording 0.3 %. The result **depends on how unresolved changes are treated** (`evidence/pooled_motion_classes.json`):
| Stratum | Videos | Moving frames | Conventional | Complex | Undetermined | Screen rec. |
|---|---:|---:|---:|---:|---:|---:|
| Depth A/B only (changes individually reviewed) | 8 | 3,726 | **93.4 %** | 3.2 % | 1.8 % | 1.7 % |
| All 12 (depth C counts unresolved changes as undetermined) | 12 | 5,527 | 68.5 % | 7.4 % | 23.0 % | 1.1 % |
Frame counts: `evidence/pooled_motion_classes.json`. Event counts (720): conventional 550, undetermined 160, complex 7, screen recording 3; **generated/video-based: none identified in any stratum.** Reading: where changes were actually reviewed, 93 % of moving time is ordinary keyframe/compositing; the only complex-animation signal is the reused money-rain overlay (`mT2hOLrCYSk`, depth C) plus doors, a bond tear and a run cycle. The owner's 70-80 % conventional figure is consistent with the all-12 total; the 10-20 % complex-or-generated share is **not** supported by the reviewed stratum (<=5 %), and the unresolved 23 % cannot be assigned to either side. A final MP4 does not reveal the method; labels are appearance-based (`ART_DIRECTION_INFERENCE`).

## Confidence
Cut and pop timing: high (frame-exact, 10 videos). Easing: low-to-moderate (6 clean fits across 3 videos; 5 linear, 1 decelerating, 1 two-curve). Asset reuse: moderate (analyst IDs). Audio: unlistened. Everything here must be re-run when more videos validate (`scripts/aggregate_channel.py`).
