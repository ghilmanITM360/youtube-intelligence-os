# Casual Finance: count reconciliation (2026-11-23)

Channel: `@CasuallyFinance`, `UCrNfRFWnLC3tCy1TnyhVQ7g`. Not Casual Economics (`UCo7FvfMJeTRhO-d7xT8IZlg`) and not Casually Explained (`UCr3cBLTYmIK9kY0F_OdFWFQ`, a separate identity-only registry row).

Per-video detail: [CASUAL_FINANCE_COUNT_RECONCILIATION_2026-11-23.csv](CASUAL_FINANCE_COUNT_RECONCILIATION_2026-11-23.csv) (214 IDs).
No source file, database or registry was edited. This note only explains the numbers.

## Verdict

There is no data error. The sources count different things at different dates. The registry's 0 is deliberate, and `finance_economics_complete.db` is the largest verified set of Casual Finance rows.

| Source | Videos | What it measures | Date |
|---|---:|---|---|
| Canonical registry `youtube_channel_registry.db` | 0 | Identity verified, data not extracted (`IDENTITY_VERIFIED_DATA_NOT_EXTRACTED`) | identity 2026-09-14, built 2026-09-28 |
| `research/casually-finance/INDEX.csv`, `finance_economics_complete.db`, finance queue | 206 (33 long, 173 Shorts) | Forensic enumeration snapshot | 2026-10-11 |
| `casually-finance-video-inventory` | 210 (34 long, 176 Shorts) | Public `/videos` and `/shorts` tabs enumerated | 2026-10-19 |
| `reported_videos` in `finance_economics_complete.db` | 220 | Machine A figure from `CHANNEL_DATA_SORT_initial.csv`; no enumeration or receipt found | unknown |
| Live Chrome pass | 4 more IDs | Uploads newer than the 210 (`YUyoWFlaOKg`, `dWdhu3_OI2A`, `d2n4qXk31TA`, `TRupV4DhlxE`) | 2026-11-13 |

## Findings

1. **Registry 0 vs 206.** The channel was added as `ADDED_TARGET` with only identity evidence. Its videos came later from the forensic branch and Machine A. [VISUAL_FORENSICS_REGISTRY_CROSSWALK.csv](../../data/manifests/VISUAL_FORENSICS_REGISTRY_CROSSWALK.csv) records all 210 inventory IDs with `in_registry=false`. The registry is a pinned build, and `finance_economics_complete.db` records its SHA-256. Zero ID overlap with the registry is therefore expected.
2. **206 vs 210.** The ID sets are nested: all 206 are in the inventory, and the 4 extras are new uploads. They are `9eBM5IF_bco` (long) and `7bm7XYssqlU`, `ffIiiPLDFdM`, `Es5c2MKzbDg` (Shorts). This matches 34 vs 33 long and 176 vs 173 Shorts.
3. **220 is unverified.** It appears only as Machine A's reported count. The 2026-10-19 enumeration found 210 with no failed IDs. Treat 220 as unverified, not as 14 missing videos. No ID list for it was found, so its origin stays unresolved.
4. **4 videos exist in no dataset.** The four 2026-11-13 live-only IDs appear in no tracked file outside the Casual Finance forensic report. Live total is therefore at least 214, from two different dates.
5. **Views differ in 200 of 206 rows.** The DB snapshot (Oct 11) and the inventory (Oct 19) differ because views grew. Example: `9N6YCiEHK5I` 34,111 vs 34,117. Do not mix the two columns.
6. **Transcript conflict.** The DB says 206/206 have text: 199 Whisper `base` (`ASR_UNCERTIFIED`) and 7 YouTube auto-caption. The finance queue marks 190 `NOT_REGISTERED` and 176 `BLOCKED_MISSING_SOURCE_TRANSCRIPT`. The queue does not count uncertified ASR as an accepted transcript. Both are consistent with their own rules, and the audit follows the queue.
7. **Naming.** "Casual Finance" (registry, DB) and "Casually Finance" (queue, folders, media) are the same channel ID.

## What was not changed, and options

- Registering the 210 videos in the canonical registry would need the registry's own ingestion workflow and an owner decision. It was not attempted.
- The 14-video 220 gap and the 4 live-only IDs need a fresh public enumeration to close.
- Recommended citation: "206 videos at the 2026-10-11 snapshot, 210 at 2026-10-19, at least 214 live on 2026-11-13".
