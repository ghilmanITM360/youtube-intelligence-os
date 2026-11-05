# HELDOUT_EVALUATION_v6 — Population-6 (xkcd What If), measurement-only

Evaluated 2026-11-06 (UTC) under HELDOUT_PROTOCOL_v6.md. Scope: **quantitative rhythm/format ranges only**. No qualitative review, no listening.

## Pins
- Protocol v6: `campaign/HELDOUT_PROTOCOL_v6.md` sha256 `76810c7e550e4e92a1136c7238a89b9e9dd5cdda4d0347217ec9c5caf5fd5e15`, frozen mtime 2026-11-05T17:02:00Z (recorded in `.sha256` and `progress_log.txt` line "pop6 pre-registered").
- Selection: `selection/selection_v6_pop6.json` sha256 `11a554e601eb7adee78a99a228a24024e7d26e350b630d20eb749060eb825b21` (20 long videos; alkJ7xScBiw excluded by protocol, no local file).
- Manual available before Pop-6 data: **v0.7**, `campaign/CHANNEL_PRODUCTION_MANUAL_v0.7.md` sha256 `bb5e76f2da2532bc407658aea79317af742672c13f8cf6f847dd3941d15da95a`, mtime 2026-11-05T16:53:04Z (before freeze).
- Earliest file in any Pop-6 video dir: 2026-11-05T17:02:36Z (36 s after freeze; first ingest completed 17:05:35Z). Ranges are the frozen v4 ranges; none changed after seeing results.
- Script: `scripts/xk_pop6_quant.py` sha256 `b3c2f6e8cb1650ad60bf6f5a07590d5a307a39bffadb4be589c46306d0216044`, mtime 17:02:16Z. Compared with `xk_heldout4_quant.py`: identical Q1/Q3/Q4 ranges and Q4 formula (dev LONG_DEV range ±15 % of range = 0.009..0.243, 3 dp), Q6 −17.3..−15.6 LUFS. A missing segments file gives NOT_EVALUATED, an unparseable loudness gives UNAVAILABLE; neither becomes PASS or 0.
- Raw results: `campaign/pop6_quant.csv` sha256 `76810c7e550e4e92a1136c7238a89b9e9dd5cdda4d0347217ec9c5caf5fd5e15`; stdout `campaign/pop6_quant_stdout.txt`; loudness `campaign/loudness_pop6.txt`; all 64 source hashes `campaign/source_hashes_all_2026-11-06.json`.

## Prep completeness (verified, not assumed)
- 20/20 ingested (INGEST_DONE), 20/20 `segments_v1.csv` and sheets (`campaign/ingest_pop6.log`, 20 lines after this session finished the last 4: DiWFXv9N0Vs, PUtI3xoaHx0, U8F7UNK9jco, 0L44GEJ5pLE).
- 20/20 ebur128 Summary present (`xk_loudness.sh`, rerun under bash; first attempt this session failed on zsh word-splitting, error receipt `campaign/loudness_pop6.err` was 1.6 kB, rerun err = 0 bytes). Loudness is a measurement, not listening.
- 20/20 recorded `source_sha256.txt` == recomputed SHA-256; 0 duplicate hashes among 64 videos.
- Correction: `progress_log.txt` 17:02:06Z "pop6 ingest+prep+loudness done" was premature; ingest really finished 17:05–18:09Z, and the last 4 preps and all loudness were completed after that.

## Score (frozen rule: ≥ 90 % of rows PASS)
**116 / 120 = 96.7 % → quantitative PASS.** Denominator = 20 videos × 6 rules (Q1,Q3,Q4,Q5,Q6,Q7); 0 NOT_EVALUATED, 0 UNAVAILABLE, 0 excluded rows. Q2 and qualitative are NOT_EVALUATED by protocol (no reviewer) and are outside the denominator.

| Rule | PASS | FAIL |
|---|---|---|
| Q1 events/min 15.75–32.65 (observed 17.3–27.5) | 20 | 0 |
| Q3 median hold 1.02–2.58 s | 18 | 2 |
| Q4 activity share 0.009–0.243 (observed 0.021–0.197) | 20 | 0 |
| Q5 1920x1080 24/1 | 20 | 0 |
| Q6 −17.3…−15.6 LUFS (observed −16.8…−16.1) | 20 | 0 |
| Q7 last HOLD 235–240 f | 18 | 2 |

## FAIL rows (all listed, none excused)
1. UXA-Af-JeCE Q3 median hold 2.71 s (> 2.58), 208 s video.
2. aIIBBj6KR-Y Q3 median hold 2.96 s (> 2.58), 173 s video.
3. jgafb8G7i4o Q7 last segment HOLD 231 f (< 235), 241 s video; sequence …HOLD 63, ACTIVITY 1, HOLD 231.
4. DiWFXv9N0Vs Q7 last segment ACTIVITY 1 f after HOLD 238 (final 1-frame activity; segmenter classification, not a 235–240 f closing hold), 168 s video.
Pattern note (hypothesis, not fact): three of four fail by a single 1-frame ACTIVITY segment near the end or a hold slightly outside range; Q7 may be sensitive to 1-frame segmenter artefacts. Not investigated further; no rule changed.

## Subgroups
Durations 159–274 s (median 192 s). Longest 10: 2 fails (UXA-Af-JeCE Q3, jgafb8G7i4o Q7) of 60 rows (96.7 %); the other 10: 2 fails of 60. Longest 5 (fs28lEq9smw, EFRUL7vKdU8, jgafb8G7i4o, 0EytSWiKrFg, gp5G1QG6cXc) 1 fail of 30. No long-duration collapse is visible, but all 20 are 2.7–4.6 min, so videos far longer than this are not covered.
Exploratory (not scored): activity share ≥ 0.15 in 2 videos, gp5G1QG6cXc (0.183) and U8F7UNK9jco (0.197), i.e. continuous-motion candidates that still passed Q4 under the widened range.

## Unseen / independence
- Video IDs: 0 overlap with the 44 DEV + earlier held-out video dirs; 0 duplicate source hashes; `selection_v2..v5` mention none of them.
- Prior exposure (not "unseen" in the strong sense): **21 Shorts in the DEV/held-out corpus are narration excerpts** (6-word-block coverage; `short_long_text_reuse_population.csv`, relation TEXT_EXCERPT_CANDIDATE) of Pop-6 long videos — text-level, from catalog captions, not visual inspection of the long videos. Two longs are named as topic siblings in `selection_v1.json` reasons: fs28lEq9smw (sibling of early Short _efsqO-4OoQ) and DiWFXv9N0Vs (sibling of Short mEUqVgGf4e0). No re-encode duplicates found by hash (hash only; perceptual duplication not tested).
- Scope: Unseen for the **quantitative script** = no reviewer, no tuning, ranges frozen before data. This is **not** an independent qualitative review; none was done. The ranges themselves were derived from DEV plus held-outs 1–5, which are the same channel/format, so this tests within-channel generalisation only.
- The same model family wrote the script, protocol and this evaluation (limitation).

## Limitations
- Measures rhythm/format only; says nothing about narration sync, audio content, visual detail, story type, or production acceptance. Not FULL_AV_SIGNOFF, not CT_SCAN_COMPLETE; audio listening remains BLOCKED_CAPABILITY.
- Story-type title prediction stays at the earlier 1/3 (held-out-5) with no fresh valid evidence; v0.7 already demoted it to a descriptive n=1 note.
- Segments for 3 of 4 FAILs depend on the 1-frame ACTIVITY classification.

## Manual implication
No manual change made. Manual v0.7 ranges survive this population at 96.7 %. Any v0.8 (e.g. Q3 upper bound 2.58 → ≥ 2.96, Q7 1-frame tolerance) would be written after this score is frozen and must not be called validated on Population-6.
