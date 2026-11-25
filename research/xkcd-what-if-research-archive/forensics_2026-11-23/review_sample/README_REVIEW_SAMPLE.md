# Review sample: 60 measured shots viewed and coded

Status: **self-review, one coder, stills only.** First viewing of the machine-measured ledgers (`../ledgers_measured/`): 60 of 719 shots. The other 659 shots and all 2,160 events stay `NOT_VIEWED`.

## What was done
- Batch 1 (24 shots, `SAMPLE.csv`, `scripts/review_sample.py`): 12 long, 12 Shorts, one per video, never the first shot, seed 7. Batch 2 (36 shots, `SAMPLE2.csv`, `scripts/review_sample2.py`): 18 long, 18 Shorts, seed 11, strength strata (below or at least 0.3, 9 each per format), videos with the fewest sampled shots first. 42 of the 44 videos are covered.
- Each shot viewed as three stills: 0.25 s before the shot start, the ledger keyframe, 0.25 s after the start. Sheets: `long_1-2.jpg` (cells 1-12), `long_3-5.jpg` (cells 25-42), `short_1-2.jpg` (cells 13-24), `short_3-5.jpg` (cells 43-60). A cell reads before | keyframe | after; cells follow `SAMPLE.csv` then `SAMPLE2.csv` order (long sheets one cell per row, Shorts two per row).
- Coded in `REVIEWED_SAMPLE.csv` (60 rows): subject, setting, framing, graphics_text, narrative_function, boundary_check, note. `camera_motion` = NOT_ASSESSED_STILLS (stills cannot show motion). Coding code: `scripts/review_sample_code.py` (1-24), `review_sample_code2.py` (25-60).
- Descriptions say what is drawn; no artwork or script is reproduced.
- **boundary_check rule (set after batch 1):** TRUE_CUT = composition or background replaced; FALSE_PROGRESSIVE = same scene, content added, removed, dimmed or text swapped; BORDERLINE = same background, main subject redrawn.

## Result 1: is the shot boundary a real cut?
| | n | TRUE_CUT | FALSE_PROGRESSIVE | BORDERLINE |
|---|---|---|---|---|
| All | 60 | **50 (83%)** | 8 | 2 |
| Long | 30 | 26 | 3 | 1 |
| Shorts | 30 | 24 | 5 | 1 |
| Strength < 0.3 | 29 | 23 | 4 | 2 |
| Strength >= 0.3 | 31 | 27 | 4 | 0 |

- The sample is stratified, not random over all 719 shots, so 83% is a sample figure with wide uncertainty (about 72% to 91% at 95%, one coder), not a channel-wide precision.
- **Strength is not a usable filter.** False or borderline cases sit at 0.088, 0.096, 0.135, 0.139, 0.188, 0.25 and also at 0.496, 0.861, 0.919, 0.953. High strength does not mean a real cut: a large grey glow added to one scene, a thought bubble leaving, a screen dimming all scored 0.86 to 0.95.
- Cases that fail: a drawing or a background tone added to the same scene (most), a card or bubble removed, a text-only swap over an identical pattern, a dimming of the same scene.
- Result relative to the 0.70 precision in the campaign validation: different tests (a visible scene change over a 0.5 s window versus a match within 2 frames); do not average. Reading: roughly 8 in 10 shot candidates are real scene changes.

## Result 2: what the shots are (OBSERVED, n=60, counted from the CSV)
- A shot is usually one drawn scene with one or two labels, a presenter-at-board, a prop or a text-only card. Quantity labels (a unit, a power figure, a multiplier, a price rate) appear in a minority of keyframes.
- Several shots hold many states (a 41 s map shot with depth labels changing; a board that fills; a gradient that changes labels), so a shot is not a single image.
- **Visual end card (found in the sample):** two sampled keyframes were the closing red card with the credits and four book covers and a URL. A check of the last shot of all 20 measured long videos (`endcards_long.jpg`, order in `endcards_order.csv`) shows **the same end card in 20 of 20**. None of the 24 measured Shorts ends on it (`endcards_short.jpg`). The 24 long videos with campaign ledgers were not checked here.
- Third-party material on screen: a search-engine UI with its logo (1 shot).
- The channel's own red series title card appears as a shot (long videos): branding that is not a quantity or science device.

## Limits
- One coder, no second reviewer; 60 shots; three stills per shot; one 0.5 s window. Camera motion, tempo, sync and voice are not assessed. Coding rule for boundaries was fixed after batch 1; batch 1 was not recoded but contains no borderline case.
- End-card check: the last measured shot per video, a keyframe at the middle of the shot; the card's duration and whether it is audio-narrated are not measured.
- Next if wanted: a second reviewer on these 60 rows; or view events, not shots.
