# Casually Finance — Channel Editing DNA (PRELIMINARY, n = 10 of 48 local videos)

Source: `EDITING_TIMING_STATISTICS.csv`, `MOTION_OPERATION_TAXONOMY.csv`, per-video `videos/<id>/*`. **Denominator:** 10 validated Shorts (11.8 min, 18,915 native frames) of 48 local videos (10 long-form + 38 Shorts) of 210 public. All are Shorts; no long-form has been analysed in this phase, so nothing below describes the long-form videos. Depth mix: 2 × A, 6 × B (one coarse), 2 × C (`UNRESOLVED_CHANGE` rows remain in the C videos). Selection was by public views and layout diversity, **not random**; every statement is a sample finding, not a channel-wide law. Evidence labels: `DIRECTLY_OBSERVED`, `MEASURED`, `ART_DIRECTION_INFERENCE`, `PLAUSIBLE_HYPOTHESIS`, `UNKNOWN`. The 16 videos of the earlier Oct-12 corpus (`codex/casually-finance-forensic-research`) are `REFERENCE_SUPPORTED` context and are not merged into these numbers.

## A. Patterns seen in all 10 validated videos
| Pattern | Evidence (n = 10 unless stated) |
|---|---|
| **One-frame composition replacement is the dominant edit.** 202 `HARD_CUT_REPLACE` events: every one swaps the whole stage between two consecutive frames, no fade, wipe or blend. | `MEASURED`: from ~7 % of the frame (sparse scenes) to >50 % (screenshot scenes) changes on one frame, on a mostly white canvas. 202 of 609 events; 419 of 609 events last one frame. |
| **Cut rate 12-29 per minute, median ~16.** Scene median 1.7-4.1 s (median of medians 2.83 s). | `MEASURED`, per-video table. Banded-era Shorts cut faster (median 26/min, scene median 1.8 s) than full-bleed Shorts (16/min, 2.9 s) — 2 vs 8 videos only. |
| **Pops, not tweens, build explanations.** 107 `POP_IN` + 46 `OVERLAY_POP`: props, numbers, X marks, bubbles and bills appear fully formed in one frame (2-4 frames when sequenced). | `MEASURED` counts; no scale/opacity easing visible at 30 fps sampling in the one-frame cases. |
| **A static canvas most of the time.** 75 % of all frames contain no stage change (range 58-92 % per video). | `MEASURED` frame-weighted; holds are intentional in the sense that every hold sits between authored events (QA check). |
| **Visuals meet or lead the voice.** Hard cuts precede the nearest ASR word onset by a median 80 ms (p10 -199, p90 +62; 55 % within +-100 ms); captions land on ASR onsets (median +33 ms, 79 % within +-100 ms, 2 banded videos). | `MEASURED`, ASR uncertainty ~100 ms; sign convention: negative = visual first. |
| **White canvas, hand-lettered text, flat vector props and characters.** | `DIRECTLY_OBSERVED` in 10/10 (counterexamples: dark quote cards, photographs, logos used as inserts). |
| **Source evidence inside the explanation.** Screenshots/charts/documents appear in 10/10 videos (70 appearances, 49 distinct IDs) with push-in, scroll, highlight or pop-on callouts. | `DIRECTLY_OBSERVED`. |

## B. Conditional patterns
- **Scroll/zoom of an evidence screenshot** (35 events in 7 videos, 1,361 event-frames, the largest motion budget): used when a document or chart must be read; precedes or accompanies a presenter pop-in. The two numerically fitted push-ins differ: one is **linear** (scale 1.00→1.52 in 0.87 s) and one **decelerates** (1.00→1.43 in 1.7 s); `MEASURED`, `Qof71Ef-3EU`.
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
- **No fade/dissolve or camera shake was found between scenes** in 10/10; the only gradual effects are the zooms, strokes, highlights and one opacity fade above.

## Keyframe-compatible versus complex motion (duration-weighted; user hypothesis 70-80 % / 10-20 %)
Frame-weighted over all 18,915 frames: static hold 75.1 %, plausibly conventional 2D keyframe/compositing 19.3 %, complex continuous animation 2.2 %, undetermined method 3.1 %, screen recording 0.3 %. **Of the 4,713 frames in which anything moves: conventional 77.4 %, complex 8.7 %, undetermined 12.6 %, screen recording 1.3 %, generated/video-based: none identified.** Event counts: conventional 511, undetermined 88, complex 7, screen recording 3 (609 events). So the sample is **consistent with** 70-80 % conventional and 10-20 % complex-or-uncertain **as an upper bound on complexity**; it neither shows nor excludes image-to-video use, because (i) 12.6 % of moving frames are unresolved, (ii) a final MP4 does not reveal the method, and (iii) most 'complex' frames come from one reused overlay clip. Method labels are appearance-based (`ART_DIRECTION_INFERENCE`), never software claims.

## Confidence
Cut and pop timing: high (frame-exact, 10 videos). Easing: low-to-moderate (6 clean fits across 3 videos; 5 linear, 1 decelerating, 1 two-curve). Asset reuse: moderate (analyst IDs). Audio: unlistened. Everything here must be re-run when more videos validate (`scripts/aggregate_channel.py`).
