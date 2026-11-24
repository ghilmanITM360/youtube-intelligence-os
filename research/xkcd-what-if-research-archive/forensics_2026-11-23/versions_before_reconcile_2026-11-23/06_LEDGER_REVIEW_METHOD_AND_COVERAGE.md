# 06 Review of the measured ledgers: sampling method, results and what stays unviewed (continuation, 2026-11-23)

Population: `ledgers_measured/ALL_SHOT_LEDGER.csv` (719 shots) and `ALL_EVENT_LEDGER.csv` (2,160 events) for 44 videos (20 long, 24 Shorts), machine-measured. The ledger files themselves still say `NOT_VIEWED` on every row and were not edited; viewed rows live in `review_sample/REVIEWED_SAMPLE.csv`.

## Sampling and prioritisation (documented, reproducible)
- Eligible shot = not the first shot of its video (SH001 has no cut boundary), has a keyframe and a boundary strength. A cell = three stills: 0.25 s before the shot start, the ledger keyframe, 0.25 s after the start (`scripts/review_sample*.py`, seeds 11 and 31).
- Strata: format (long, Short) x boundary strength (< 0.3, >= 0.3). Inside a stratum, videos with the fewest already-sampled shots come first, then random order. Batch 1: 24 shots (checkpoint 7), batch 2: 36 (checkpoint 8), **batch 3 (this continuation): 48, 12 per stratum.**
- Coding per cell: `boundary_check` (TRUE_CUT / FALSE_PROGRESSIVE / BORDERLINE), subject, setting, framing, graphics text, narrative function, a note. Camera motion is **not assessable from stills**; where zoomed or motion-blurred views of the same map appear it is flagged `PAN_OR_ZOOM_INFERRED_FROM_STILLS`.
- Reader: the main session, one coder, same model family as the rest of the audit. **Not independent.**

## Coverage now
| Item | Viewed | Of | Share |
|---|---|---|---|
| Shots viewed and coded | **108** | 719 | 15% |
| Videos with at least one viewed shot | **44** | 44 | 100% (v1: 42) |
| Long / Short shots | 54 / 54 | | |
| Events individually interpreted | 0 (event windows of the pilot video aside) | 2,160 | 0%; 74 small additions and 1,443 + 189 hold-residual runs were viewed, but those are not ledger events |
| Shots not viewed | 611 | 719 | 85% |

The sample is **stratified, not proportional**, so overall rates below are descriptive of the sample.

## Result: how many measured shot boundaries are real cuts
| Group | True cuts | Wilson 95% interval |
|---|---|---|
| All 108 | 83 (77%) | 0.68 to 0.84 |
| Long (n=54) | 43 (80%) | 0.67 to 0.88 |
| Short (n=54) | 40 (74%) | 0.61 to 0.84 |
| Boundary strength < 0.3 (n=53) | 34 (64%) | 0.51 to 0.76 |
| Boundary strength >= 0.3 (n=55) | 49 (89%) | 0.78 to 0.95 |

Others: 22 false progressive changes, 3 borderline. **Update to checkpoint 8:** with 60 shots, strength looked unusable as a filter; with 108 it separates (64% vs 89%), but strength >= 0.3 still contains 6 false boundaries, and one false boundary has strength 0.997 (`xA9aqKGBeOs` t=65.54: the frame dims and a laser appears on the same device). Strength is a weak filter, not a validator.

## Failure modes found in batch 3 (what the detector over-segments)
1. **Camera moves over a map**: the Short `U4cONnQxgvo` (rotated-continents map) supplied 7 of the 14 false boundaries of batch 3 (zoom and pan with motion blur on one background). 9 of its boundaries were sampled in total; 7 are false.
2. **Content added to the same scene** (labels, a split panel, an umbrella, printers): the detector fires on the added content.
3. **Whole-frame dimming or brightening** with a high strength.
4. The opposite error (real cuts missed) is not testable from this sample; earlier validation against campaign ledgers gave recall 0.86.

## What is still not known
- Interpretation columns (subject, setting, narrative function, graphics text) exist for 108 of 719 shots only.
- Per-event interpretation for the 2,160 events: not done. Event timing and counts are MEASURED; classes are `UNCLASSIFIED`.
- 1,585 long and 204 Short faint-layer events and sub-15 px changes were not examined (see `ct_scan_batch/`).
- Shot-level storytelling questions 6.4(1)-(14) are answered for none of the 719 shots; they are answered only for the sampled cells in a limited way (subject, function, text). Treat per-scene claims about the 611 unviewed shots as unsupported.

## Addendum: batch 4 (continuation of 2026-11-23, after the independent-audit request)
Verified against the files first: `ledgers_measured/ALL_SHOT_LEDGER.csv` has 719 shots and the 44 event ledgers 2,160 events (audit layer); the campaign layer is separate (718 shots, 2,708 events in 44 other videos). Same method as batch 3 (strata format x boundary strength, fewest-sampled videos first, three stills per cell), **seed 47, 48 new shots, cells 109 to 156**, `scripts/review_sample4.py` (sampling) and `scripts/review_sample_code4.py` (coding); sheets `review_sample/b4_long_*.jpg`, `b4_short_*.jpg`. The 108-row file is kept as `review_sample/REVIEWED_SAMPLE_v3_108rows_2026-11-23.csv`. New coded columns for this batch only: pose or expression, humor type, rule note. One coder, same model family: **not independent**. One +0.25 s still (cell 141, the last shot of a Short) was replaced by an earlier frame because the video ends.

| Item | Viewed | Of | Share |
|---|---|---|---|
| Shots viewed and coded | **156** | 719 | 21.7% (v3: 15%) |
| Long / Short shots | 78 / 78 | | |
| Videos with at least one viewed shot | 44 | 44 | 100% |
| Events individually interpreted | 0 | 2,160 | 0% (unchanged; batch 4 interprets shots, not events) |
| Shots not viewed | 563 | 719 | 78% |

| Group | True cuts | Wilson 95% |
|---|---|---|
| All 156 | 119 (76%) | 0.69 to 0.82 |
| Batch 4 alone (48) | 36 (75%) | 0.61 to 0.85 |
| Long (78) / Short (78) | 62 (79%) / 57 (73%) | 0.69 to 0.87 / 0.62 to 0.82 |
| Strength < 0.3 (77) | 50 (65%) | 0.54 to 0.75 |
| Strength >= 0.3 (79) | 69 (87%) | 0.78 to 0.93 |
| Batch 4 only: < 0.3 (24) / >= 0.3 (24) | 16 (67%) / 20 (83%) | 0.47 to 0.82 / 0.64 to 0.93 |

The batch-3 pattern (low strength is much less reliable) replicates in a fresh draw but with wide intervals. Other counts: 33 false progressive changes and 4 borderline over 156; **16 shots (8 in batch 4) carry a camera-move inference** (pan, slide or zoom) in 6 videos.

New failure modes and observations in batch 4 (OBSERVED in stills, one coder):
1. **Counter changes in a fixed diagram** (the FLOORS / GOAL diagram in `J-E8rjWR9rM`): 3 false boundaries; followed by a zoom to Earth.
2. **Overlays on a scene** (a report page over a pool, a calculator panel, a dose-meter inset): 3 false boundaries.
3. **Sideways slides of a wide composition** (`zgBTwtg7H8E` cell 127, `eSPcp-tfGbA` cell 139, a film-strip scroll in `zJNmUWZXj2M` cell 156): camera-like moves that a cut detector splits.
4. **Low strength does not mean no cut**: cell 146 (`zJNmUWZXj2M`) is a true cut at strength 0.106 because both frames are mostly white.
5. **Red series title card** ("xkcd's what if? THE VIDEO SERIES") follows the question beat in 3 of the 24 long cells at 9.4, 11.3 and 11.6 s, and again at 18.9 s (cell 125); with the earlier ten-episode frames (9.4 s, 14.5 s) the card sits between about 9 and 19 s. **Not yet a rule**: it was seen where sampled, not measured on all 44.
6. **A Short can end on full-frame static** (`alBQCm0QpJg` cell 141).
7. **Characters and humour**: the base ring-head stick figure dominates; other characters seen include a child with hair, a duck-like character in a top hat (resembles a known cartoon character, not identified, check before any reuse), a witch and a princess (film-reference gag), a cat, a squirrel and small sprite figures; the shot-level humour is mostly label gags ("SHOWOFF", "PLEASE DON'T"), strike-through corrections, board-contents gags, film-reference gags and callbacks to the opening panel.
8. **Third-party material on screen**: report and code pages, a Wolfram|Alpha interface and ride and vehicle names appear; any production would need its own redraw.

Still not known: interpretation columns exist for 156 of 719 shots, the other 563 are unreviewed; no event of the 2,160 was individually interpreted; camera movement was not measured from motion; pose and expression were noted only as short descriptions, not coded for every shot.
