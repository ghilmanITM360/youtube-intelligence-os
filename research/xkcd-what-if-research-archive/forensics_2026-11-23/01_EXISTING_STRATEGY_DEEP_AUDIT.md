# 01 Existing strategy deep audit: `research/what-if-channel-strategy/`

Audit date 2026-11-23. Files read in full: README, 01, 02, 03, 04, 08; 05, 06 and 07 read in the sections that carry claims (summary tables, constants, method limits). Data files were checked by recomputation, not read line by line. Labels follow the directive: VERIFIED / OBSERVED / MEASURED / INFERRED / UNVERIFIED / CONTRADICTED / SUPERSEDED. Row-level evidence is in `01_STRATEGY_CLAIM_EVIDENCE_MATRIX.csv`.

## 1. What this folder actually is

It is a **new-channel launch strategy** for an original science channel ("Unreasonably Exact"), built on competitor and market research. It is **not** a study of how xkcd's What If? videos are made. Its own README says so: market scan, topic scoring, a 30-day calendar, science pre-check and branding. For xkcd's production methods it reuses other studies (the 83-script audit and the 14-video CH-000004 DNA), and it adds one new visual pass on three **competitor** videos (not xkcd).

Contents: 8 reports (01 to 08), 13 data files, 4 scripts, 10 branding files, one framework JSON. 508,915 bytes. Last commit touching it: `46281fcc` (2026-11-19).

## 2. Strengths (checked)

- **Catalog numbers reproduce exactly.** From `census.csv` (sha256 `104e9865…67b1`, verified): 91 videos (45 long, 46 Shorts), 136,100,769 long views (median 2,505,166), 68,694,845 Shorts views (median 1,059,738), 89 of 91 uploads on Tuesday, gap counts 7d x56, 21d x15, 14d x8, year mix 3/17/14+19/11+27, top-10 long list in the same order.
- **Script-study numbers reproduce.** 37 of 43 long videos open with an attributed question; no CTA in 38 of 43; median long 680 words and 3:16; 56 of 83 transcripts overlap another by 30% or more; 43 long and 40 Shorts.
- **Honest labelling.** Each report separates FACT / DERIVED / INTERPRETATION / HYPOTHESIS, states survivorship and personalisation bias, and says no CTR or retention can be inferred. 04 declares itself STRUCTURAL+, not a CT scan. 06 declares itself an AI pre-check with no domain expert.
- **IP boundary is explicit** (01 §6, 08): techniques yes, expression no.
- **Competitor media hashes check out:** the manifest SHA-256 `f0d9cbcc…` for the Fossil video matches the note in 04; the three MP4s exist under `YIOS-Media-Library/WhatIfCompetitors-MP4/`.

## 3. Weaknesses

1. **Scope mismatch with the xkcd forensic goal.** Nothing here measures xkcd's visuals directly. The only xkcd visual statements are (a) a 10-thumbnail in-browser look (no files kept) and (b) the 14-video Brain numbers (7.77 s median shot, 89.8% locked camera).
2. **It does not use the larger xkcd visual campaign** that already exists on `main` (see `01_STRATEGY_GAPS_AND_CONFLICTS.md` G2): 44 videos with every frame measured, a production manual v0.7 and held-out tests. The strategy cites only the older 14-video Brain.
3. **Metric definitions are mixed.** 7.77 s = median *shot* (Brain, 14 videos); 4.1 s / 59 s = ffmpeg *scene-change candidate* gaps on 3 competitor videos; the campaign uses *hold* (median 2.15 to 2.33 s) and *hard cuts per minute* (4.9 to 6.1). These are not interchangeable and the strategy does not reconcile them.
4. **One duration claim is wrong.** 03 §1 says xkcd 2026 longs run 2:43 to 3:33. The census has 11 long videos from 2026 with durations 2:42 to 4:38.
5. **Market-scan evidence is not reproducible in full.** 02 reports 596 Shorts / 117 longs from 27 searches but exported only 55 rows (the file says so). The searches were run signed-in (region PK).
6. **Scoring inputs F, V, P are analyst ratings** (03 §6, stated). Ranks within about 5 points are ties.
7. **Science verification has no human review** (06, stated), and several sources were search-confirmed, not fetched.
8. **Source book is outside the repo.** The 20-of-56-chapters result cannot be re-run from the repo alone (only hashes are kept). The book folder does exist at `~/Downloads/What_If_Full_Book_15_Files/` on this machine.
9. **Not on `main`.** The folder exists only on the research branch and its origin copy.

## 4. Usable operationally?

| Part | Verdict |
|---|---|
| Catalog and script-study facts (01 §1, 08) | Yes. Recomputed. |
| Topic scoring, calendar, branding | Yes as the owner-approved plan; ratings are judgments, not measurements. |
| Competitor structural findings (04) | As leads only. n = 3, STRUCTURAL+. |
| xkcd visual grammar | **No.** Use the campaign (manual v0.7), not this folder. |
| Science pre-check (06) | As a pre-gate only; each script needs its own claim table (already done for Day 1 and Day 3). |

## 5. Status of the owner's brief questions

See the matrix (25 claims). Totals: VERIFIED 11, MEASURED 3, OBSERVED 3, INFERRED 3, UNVERIFIED 3, CONTRADICTED 1 (C13), SUPERSEDED 1 (C17: the 7.77 s median shot as the sole xkcd pacing number, see conflicts). Verification here means recomputed from repo/local data by me; it is self-review, not independent QA.
