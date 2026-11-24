# 06 Reconciliation of the three visual layers (self-review, MEASURED from existing tables)

Nothing here is new perception. It re-uses the campaign's own ledgers (`shot_ledger.csv`, `visual_event_ledger.csv`, ASR word timestamps) and the Brain's `MASTER_SHOTS`, computed with **one definition set** by `scripts/phase6_timing.py` and `scripts/phase6_brain_vs_campaign.py`. Outputs: `06_ALIGNED_TIMING_TABLE.csv` (44 videos), `06_BRAIN_VS_CAMPAIGN_SAME_VIDEOS.csv`.

## 1. The layers

| Layer | Content | Encodes | Scope |
|---|---|---|---|
| A. Brain v1.0.0 | 200 shots, 14 slugs (11 long-form-like, 3 odd or Short: `worlds-largest-cities`, `earthquake-magnitude-shorts-wBLVmEZV2Oc`, `weird_and_worrying_questions`) | older smaller encodes (0/14 hash match to library) | 146 shots have a resolved YouTube ID, across 10 videos; 54 shots belong to 4 slugs without a canonical ID (SRC01/SRC02 candidates unresolved) |
| B. Campaign (main) | 44 videos with shot + event ledgers (24 long, 20 Shorts), 64 with ASR, 20 more with measurement tables only | library files (64/64 hash-equal) | `VISUAL_ANALYSIS_PARTIAL`; all 718 shot rows flagged `VERIFIED_VISUAL` by its own self-review; listening BLOCKED for 91/91 |
| C. 8fADp43wJwU deep pass (local) | shot + event ledger, per-second stem levels, audio-visual alignment | Brain encode (`1fb3c0f4`) | one video, `VISUAL_ANALYSIS_PARTIAL`, "human listening pass still required" |

## 2. The pacing conflict (G3) is mostly a definition problem, and the number itself holds

| Quantity (same definition across layers) | Brain A (n shots) | Campaign B, median of per-video medians |
|---|---|---|
| **Shot** (hard-cut span), all formats | **7.77 s** (200 shots; the 146 resolved rows also give 7.77 s) | long **8.44 s** (n=24, range 6.0 to 12.5); Short **6.47 s** (n=20, range 2.7 to 41.7) |
| **Event gap** (campaign's "hold": consecutive measured visual events) | not recorded | long **2.15 s** (1.33 to 2.87); Short 2.02 s |
| Hard cuts per minute | not recorded | long **5.25** (3.3 to 7.6); Short 6.51 |
| Visual events per minute | not recorded | long **22.5**; Short 23.8 |

Verdict: 7.77 s (Brain) and 8.44 s (campaign long) are **the same quantity measured on different samples and agree within about 8%**. Earlier in this audit (`01_STRATEGY_GAPS_AND_CONFLICTS.md` G3) I marked 7.77 s as SUPERSEDED. **Corrected:** the number is a valid *shot-duration* median; what is unsupported is using it as the visual-change interval. xkcd's measured visual cadence is an event roughly every **2 s**, a hard cut roughly every **11 s** on average. Claim C17 should read "VERIFIED as a shot median, INCOMPLETE as a pacing rule". The Brain's own text already warns not to turn it into a mandatory duration.

## 3. Cross-encode check: same videos, two measurements

Eight video IDs sit in both the Brain shot table and the campaign ledgers. Shot counts (Brain / campaign): -1-ldW4kpLM 39/36, 4ZVtHknKuvg 18/15, 8fADp43wJwU 29/29, GgEGcxJRDik 2/2, aMshLs0YCTQ 17/12, mEUqVgGf4e0 9/10, **SLd4hnmeW_g 1/10, wBLVmEZV2Oc 1/5**. Median ratio 1.0, so the two layers agree on most videos, but the two Shorts show the Brain recording one long "shot" where the campaign finds 5 to 10 hard cuts. That explains the Brain's 78.9 s tail and inflates its median slightly. **Do not pool Brain and campaign rows** (AGENTS rule 9): the 8 IDs would be counted twice. Use the campaign (library bytes, per-video evidence) as primary and the Brain only for its schema and its 3 videos that the campaign has no ledger for.

## 4. Narration and visual alignment (ASR, NOT listening)

| Metric (ASR word timestamps + ledgers) | Long (n=24) | Short (n=20) |
|---|---|---|
| Narration pace, ASR words per second of speech span | **3.83** (3.43 to 4.23) | 3.88 |
| Compare: script words / full duration (repo inventory) | 3.59 | 3.77 |
| First ASR word | 0.0 s in 44 of 44 | same |
| First measured visual event | 1.96 s (0.04 to 2.92) | 1.54 s |
| Pauses of 0.35 s or more | 9.7 per minute, median 0.46 s | 10.4/min, 0.48 s |
| **Visual events per 100 narrated words** | **10.0** (6.9 to 14.0) | 9.8 |
| Words per shot | 39 (27 to 61) | 32 |

Reading: narration starts at frame 0 with no cold silence; roughly **one visual event per ten spoken words** (about one per 2.6 s) and a hard cut about every 40 words. These are MEASURED from the ledgers. The *relation* (narration causes or leads the visual) is **not** established: the campaign's own lead/lag column is `ASR_UNCERTIFIED`, and listening stays BLOCKED. Outlier: 8fADp43wJwU shows 0.2 pauses per minute and a 1.76 s median pause, which looks like an ASR word-timing artefact (unexplained; do not use that row for pause statistics).

## 5. What the reconciled layer can and cannot support

| Use | Status |
|---|---|
| "xkcd long videos cut roughly every 8 s (median shot), add a visual event roughly every 2 s, and speak about 3.6 to 3.8 words per second" | **MEASURED**, 24 long + 20 Shorts, same definitions |
| "Replicate this cadence and the channel will perform" | **UNVERIFIED**; no retention or performance data, and it is a style description of one channel |
| Shot or event timing for the 20 long videos with measurement tables only, the 24 with no visual analysis | **NOT DONE** (no ledger; would need new analysis) |
| Sync relation between voice and visual | **UNAVAILABLE** (listening blocked) |

## Addendum 2026-11-23 (continuation): superseded wording
Section 2's verdict "the same quantity measured on different samples" is **withdrawn**; see `06_PACING_CORRECTION.md` (different units, samples and detectors; the audit detector gives 6.75 s on 20 other long videos). Section 1 layer counts are refined in `03_CORPUS_COMPLETENESS_REPORT.md` section 3: campaign ledgers cover 44 videos and the audit's measured ledgers cover 44 different videos (0 shared); ASR exists for 88 videos, not 64.
