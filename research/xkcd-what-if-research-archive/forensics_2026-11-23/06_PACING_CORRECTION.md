# 06 Pacing comparison, corrected by definition, sample and source (2026-11-23 continuation)

Data: `06_PACING_BY_DEFINITION.csv` (from `scripts/phase6_pacing_v2.py`), `06_ALIGNED_TIMING_TABLE.csv`, `06_BRAIN_VS_CAMPAIGN_SAME_VIDEOS.csv`. The earlier text in `06_LAYER_RECONCILIATION.md` section 2 said 7.77 s and 8.44 s are "the same quantity"; that wording is **withdrawn** here (history kept; it was written before the audit detector and the Brain definition were compared).

## What each number is
| Quantity | Source | Unit actually counted | Sample | Value (long) | Value (Short) |
|---|---|---|---|---|---|
| Brain shot median | Brain v1.0.0 `MASTER_SHOTS` (older encodes, 0/14 hash match) | Brain "shot" with 581 states inside (73% of its edit entries are cut-family); detector and rules differ from the campaign | 14 slugs (11 long-like, 3 odd/Short), 200 shots, **pooled over shots** | 7.77 s median (mean 10.54) | not separable |
| Campaign shot | campaign `shot_ledger.csv` | hard-cut span from the campaign detector (reviewer-classified) | 24 long + 20 Shorts, **median of per-video medians** | **8.44 s** (6.0 to 12.5) | 6.47 s (2.7 to 41.7) |
| Audit measured shot | `ledgers_measured/` | frame-difference boundary candidate; validated P 0.70, R 0.86 on 38 held-out videos, so it **over-detects** | 20 long + 24 Shorts (different videos), median of per-video medians | **6.75 s** (3.5 to 10.0) | 7.15 s (1.8 to 14.7) |
| Hard cuts per minute | campaign | shots minus 1 per minute | same as campaign | 5.25 (3.3 to 7.6) | 6.51 |
| Hard cuts per minute | audit measured | same formula, audit detector | same as audit | 7.35 (4.2 to 13.8) | 5.81 |
| Event gap (campaign calls it "hold") | campaign events | time between consecutive measured visual-event starts, not a visual hold and not a cut interval | 24 long, 20 Shorts | 2.15 s | 2.02 s |
| Event gap | audit events | same | 20 long, 24 Shorts | 2.15 s | 2.12 s |
| Visual events per minute | campaign / audit | machine events; faint-layer events (1,585 long, 204 Short) are in neither ledger | | 22.5 / 21.8 | 23.8 / 19.7 |
| Mean shot interval (a different quantity) | derived: 60 / cuts per minute | | | about 11 s (campaign) | |

## Corrected reading
1. **Not interchangeable.** A shot (hard-cut span, about 7 to 8 s), an event gap (about 2.1 s) and a cut interval (about 11 s mean = 60 / 5.25) answer different questions. None is "xkcd's pacing" alone.
2. **The 7.77 s versus 8.44 s agreement is numerical, not definitional.** Different encodes, different detectors, different samples (Brain pooled shots incl. 3 odd or Short slugs; campaign median of medians for long only). On the 8 IDs in both layers, shot counts agree on 6 and disagree on 2 Shorts (`SLd4hnmeW_g` 1 vs 10, `wBLVmEZV2Oc` 1 vs 5). Do not state they are the same unit.
3. **The audit detector gives a shorter long-video median (6.75 s vs 8.44 s)** and more cuts per minute. That is consistent with its measured over-detection (precision 0.70 against the campaign ledgers on 38 held-out videos; in the viewed 60-shot sample 50 were true cuts, 8 progressive changes and 2 borderline) and it is a different video set, so the cause cannot be separated. Do not pool the two sets into one median; report them side by side with the detector named.
4. **Event gap and events per minute are stable across the two independent sets** (2.15 s vs 2.15 s long; 22.5 vs 21.8 events per minute), which is stronger evidence than the shot median. Both ledgers use the same event definition but different video sets, so it is a replication on disjoint videos, by the same method family.
5. **Not measured:** shots per scene intent, holds as a visual-state interval (state intervals exist only for the pilot video), and faint-layer events. No retention or performance link. Casually Finance timing rules are not used.

Status: MEASURED (machine, two disjoint sets), self-review, no independent review. Strategy edit still needed (owner decision): replace the 7.77 s-only pacing line by the three quantities above with their samples.
