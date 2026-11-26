# 07b Science-visual pass on the 20 remaining long videos (extends `07_SCIENCE_VISUAL_PASS.md`)

Status: **self-review, one coder, still frames only.** Same question as Phase 7: when the narration states a number or scale comparison, what is on screen at that moment? No artwork or script is reproduced; this describes devices.

## 1. What was run

- **Videos:** the 20 long videos that have media in the library but no campaign ledger and no campaign ASR (the 21st long video, `alkJ7xScBiw`, has no media: UNAVAILABLE). Together with Phase 7 this now touches **all 44 media-available long videos** (24 + 20).
- **Timing source (new):** no campaign ASR exists for these 20, so I ran local whisper.cpp `small.en` over each file (`scripts/phase7b_asr.py` -> `phase7b_asr/*.json`, segment timestamps only). Machine transcript, **not listening**, uncertified, and a different engine from the campaign's faster-whisper ASR.
- **Selection:** identical rule to Phase 7 (`scripts/phase7b_sample.py`): ASR segments matching the quantity regex, the 2 hits nearest 1/3 and 2/3 of runtime, still frame at segment midpoint. 40 frames from 20 videos (`07b_SAMPLE_FRAMES.csv`, contact sheets `phase7b_frames/sheet1-7.jpg`; frame order = CSV row order).
- **Scheme v1.1:** v1 plus three classes found missing in the Phase 7 holdout, **declared before these frames were viewed**: `TITLE` (label-only card), `EQUATION` (formula or worked calculation on a board), `SCENE` (illustration with no quantity device). For comparison with the 47-frame set, `TITLE` and `EQUATION` are mapped to `LABEL` and `SCENE` to `MECH` ("v1-equivalent").
- Coding: `07b_SCIENCE_VISUAL_CODING_20LONG.csv`; tally `scripts/phase7b_tally.py`.

## 2. Results (counts)

| | Phase 7 (47 frames, 24 videos) | 7b (40 frames, 20 videos) | Pooled v1-equivalent (87 frames, 44 videos) |
|---|---|---|---|
| Device LABEL (v1-equiv) | 15 | 16 (12 plain, 3 EQUATION, 1 TITLE) | **31** |
| MECH (v1-equiv; 7 are SCENE) | 9 | 10 (3 plain, 7 SCENE) | 19 |
| AXIS | 5 | 5 | 10 |
| MAP | 6 | 2 | 8 |
| SBS | 2 | 4 | 6 |
| OBJ | 5 | 1 | 6 |
| SCALEREF | 4 | 2 | 6 |
| TALLY | 1 | 0 | 1 |
| Frames with a spoken quantity | 37 | 33 | 70 |
| ...number restated on screen (YES) | 18 (49%) | 19 (58%) | **37 (53%)** |
| ...PARTIAL | 7 | 9 | 16 |
| ...NO | 9 | 5 | 14 |
| ...UNCLEAR | 3 | 0 | 3 |
| Person as SCALE / PRESENTER | 5 / 6 | 2 / 6 | 7 / 12 |
| Red accent present | 17 | 13 | 30 |

**Replication:** on a fresh set of 20 videos, coded with a different ASR source, the Phase 7 headline holds: about half or more of spoken quantities are on screen at the moment they are spoken (49% then, 58% now; with n of 33 to 37 the gap is within noise), and a direct numeral or unit label is the commonest device (16 of 40; 15 of 47). Shares of the minor devices moved again (MAP 6 -> 2, OBJ 5 -> 1, SBS 2 -> 4), so they stay unstable.

## 3. New observations (OBSERVED, small n)

1. **Elapsed-time labels recur.** A "T = ..." or duration stamp (T=0.0003s, T=0.006s, T=60 nanoseconds; earlier T=1 MONTH, T=100 YEARS, 1 HOUR, 7.25 HOURS) tags the frame: 7 of 87. It carries the time quantity while the picture shows what happens then.
2. **Worked calculation on a board.** A presenter at a board with a formula and the result in red (a chain of units multiplying to 574 MW; a fraction of kcal; a femtosecond conversion): 3 EQUATION frames, all with the figure restated.
3. **Log-scale axes with named landmarks and no numerals** (energy scale with a named particle and the Planck energy; a nanosecond axis with arrow at 1) show relative position, so they were coded PARTIAL.
4. **Magnitude ruler with an arrow** (earthquake magnitude 15 and magnitude 0, same device twice).
5. **Dual units on one label** (470 m/s with 1040 mph; 2 km as -2000 m) and **screen figure more exact than the spoken one** (604,000,000 mph on screen for "600 million"; "16 minutes" earlier against 16.5).
6. **Third-party material appears on screen:** a company logo card and a vendor PDF cover (2 of 40). For an original channel that is a licensing question, not a style to copy.
7. **SCENE frames (7 of 40)** are mostly where the narration carries no number (dates, a page number, a qualitative statement); 5 of the 7 are NA, 2 are NO.
8. The 5 NO frames: 2,000 years, wages, 20 years, a plain world map, 21 people. As in Phase 7, NO means "not on screen at that instant" (ASR offsets are uncertain).

## 4. Limits

- One coder (me); no inter-coder check. Regex-selected quantity moments only; not representative of the whole runtime; stills only.
- ASR from whisper.cpp small.en: some segments are fragments ("meters per second."), a few hits are not quantities (a date, a page number: 7 NA frames), and offsets are uncertified.
- Phase 7 and 7b frames were selected the same way but timed by different ASR engines; pooled totals assume that does not matter, which was not tested.
- 0 Shorts; `alkJ7xScBiw` unavailable. TARGETED_VISUAL, not DEEP_VISUAL.
- No link to performance.

## 5. Update for an original channel (OWNER class, unchanged in spirit)

Storyboard checklist per script quantity: pick label, axis, side-by-side, scale reference, or a worked board calculation; show the time stamp if elapsed time is the point; put the number on screen when it is the claim, and decide on purpose when it is not.
