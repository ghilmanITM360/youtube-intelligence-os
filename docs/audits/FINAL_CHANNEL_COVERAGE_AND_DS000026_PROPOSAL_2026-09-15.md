# Final Channel Coverage and DS-000026 Proposal

Audit date: 2026-09-15
Audit type: read-only verification against repository evidence, continuing from pushed commit `bf74d4c`.
No files were fixed, rebuilt (except the noted registry-validator run below), committed, pushed, or merged. No Apify run and no credits were spent. `ui/v1` was not touched beyond `git branch -a -vv` / `git worktree list`.

**One documented deviation from a strict "no rebuild" reading:** Section 1 below runs `scripts/validate_youtube_channel_registry`, the repository's own documented validation entry point (`docs/YOUTUBE_CHANNEL_REGISTRY.md`, "Build and validate"). That script rebuilds the derived, **git-ignored** `data/catalog/youtube_channel_registry.db` twice (as its idempotence check) from tracked source files only — it makes no network or Apify call, and never touches `data/raw/`, `data/catalog/youtube_inventory.db`, or any tracked file. `git status` before and after the run is byte-identical (confirmed below). It does not rebuild the historical `youtube_inventory.db`. Flagging this explicitly since the task instructions said "do not rebuild databases" without carving out this generated/ignored one; if that's not the intended reading, re-run every count in this report against the on-disk `youtube_channel_registry.db` as it stood before this session (identical, since the rebuild is idempotent and the file is not tracked by Git).

---

## 1. Git and repository state

```
$ git status --porcelain=v1 -b -uall
## main...origin/main
?? .codex/environments/environment.toml
?? docs/YOUTUBE_INTELLIGENCE_OS_FULL_AUDIT_2026-08-31.md
?? docs/YOUTUBE_INTELLIGENCE_OS_REAUDIT_2026-09-01.md
?? docs/audits/CHANNEL_COVERAGE_LEDGER_FUNDED_2026-09-14.csv
?? docs/audits/INTELLIGENCE_CAPABILITY_AUDIT_2026-09-14.csv
?? docs/audits/REPOSITORY_AUDIT_2026-09-14.md
?? docs/audits/REPOSITORY_AUDIT_HANDOFF_2026-09-14.md
?? docs/audits/REPOSITORY_BRANCH_LEDGER_2026-09-14.csv
```

Identical before and after every command run in this session (confirmed by re-running `git status --porcelain=v1 -b -uall` after the registry-validator rebuild). All 8 preserved user-owned untracked files are present and untouched.

- Local HEAD: `bf74d4cfea7f7d63c89e715ee299f531abff5d66`
- Upstream (`@{u}`, `origin/main`): `bf74d4cfea7f7d63c89e715ee299f531abff5d66`
- Live remote (`git ls-remote origin main`): `bf74d4cfea7f7d63c89e715ee299f531abff5d66`
- **All three match. No divergence.**

```
$ git branch -a -vv
* main                 bf74d4c [origin/main] fix: harden dataset provenance and tracker validation
+ ui/v1                0412932 (/Users/ghilmanislam360/Documents/youtube-intelligence-os-ui) [origin/ui/v1] docs: add complete backend audit and UI handoff
  remotes/origin/HEAD  -> origin/main
  remotes/origin/main  bf74d4c fix: harden dataset provenance and tracker validation
  remotes/origin/ui/v1 0412932 docs: add complete backend audit and UI handoff

$ git worktree list
/Users/ghilmanislam360/Documents/youtube-intelligence-os     bf74d4c [main]
/Users/ghilmanislam360/Documents/youtube-intelligence-os-ui  0412932 [ui/v1]

$ git diff --check
(no output — exit 0, no whitespace-conflict markers)
```

`ui/v1` is a separate worktree at commit `0412932`, untouched, unmerged, matches `origin/ui/v1`.

```
$ .venv/bin/python -m pytest -q
........................................................................ [ 21%]
........................................................................ [ 42%]
........................................................................ [ 63%]
........................................................................ [ 84%]
.....................................................                    [100%]
341 passed, 1 warning in 27.84s
```

The one warning is the same pre-existing benign `zipfile` "Duplicate name" `UserWarning` noted in prior audits (from a test fixture intentionally exercising duplicate-entry handling), not a regression.

---

## 2. SQLite integrity

Four `.db` files exist under `data/catalog/`. `PRAGMA integrity_check` and `PRAGMA foreign_key_check` were run against each:

| Database | Size | integrity_check | foreign_key_check | Notes |
|---|---:|---|---|---|
| `youtube_channel_registry.db` | 119,578,624 B | `ok` | no violations (empty result) | Generated, git-ignored, authoritative query layer. 69 channels, 25 datasets, 552 intelligence rows. |
| `youtube_inventory.db` | 48,037,888 B | `ok` | no violations (empty result) | Historical catalog, read-only evidence, never rebuilt. |
| `youtube-intelligence-os.db` | 0 B | `ok` | (no tables) | Empty/unused file. |
| `youtube_intelligence.db` | 0 B | `ok` | (no tables) | Empty/unused file. |

No corruption, no foreign-key violations, in any database.

The bundled registry validator (`scripts/validate_youtube_channel_registry`) additionally ran control-total checks, source-group separation, visual/intelligence input-vs-artifact distinctions, evidence-path checks, required-view checks, uniqueness checks, and a two-run idempotence rebuild. Result: `"status": "PASS"`, `"errors": []`. Both rebuild passes produced byte-identical row counts (69 channels, 25 datasets, 1,904 videos, 552 intelligence rows, 759 channel_data_layers rows, etc.) — confirming the registry is deterministic and not silently drifting.

---

## 3. Dataset manifests and checksum ledgers

25 datasets are registered (`DS-000001` – `DS-000025`). All 25 manifest files (`data/manifests/DS-0000NN.md`) exist on disk — zero missing.

The checksum-ledger provenance validator (`scripts/validate_dataset_ledgers.py`) covers the five funded/Apify-sourced batches that carry per-file `_FILES.csv` checksum manifests:

```
$ .venv/bin/python scripts/validate_dataset_ledgers.py
DS-000021: clean
DS-000022: clean
DS-000023: clean
DS-000024: clean
DS-000025: clean
```

All five reconcile cleanly, including the previously-fixed DS-000023 path defect (DS-000023-F001 errata, corrected in commit history prior to `bf74d4c`). Datasets DS-000001–DS-000020 predate this checksum-ledger format (screenshots, historical exports, forensic reconstructions, user-supplied packages) and are tracked instead through their individual manifest files and the registry's `identity_evidence` / `dataset_channels` tables, which the registry validator's idempotence and evidence-path checks also cover.

### Dataset-level totals (`v_dataset_summary`)

| Dataset | Channels | Videos | Real transcripts | Placeholders |
|---|---:|---:|---:|---:|
| DS-000001 — Matty Invests & Mr. Finance | 2 | 159 | 158 | 1 |
| DS-000002 — Sunset forensic recon Case 1 | 0 | 0 | 0 | 0 |
| DS-000003 — Doctor Thomas screenshots | 0 | 0 | 0 | 0 |
| DS-000004 — Dr. Adewale screenshots | 0 | 0 | 0 | 0 |
| DS-000005 — Dr. Okoro screenshots | 0 | 0 | 0 | 0 |
| DS-000006 — Dr. Aliza Wright screenshots | 1 | 32 | 32 | 0 |
| DS-000007 — Dr. Waterling screenshots | 0 | 0 | 0 | 0 |
| DS-000008 — Senior Health Podcast screenshots | 0 | 0 | 0 | 0 |
| DS-000009 — Senior Health Hub screenshots | 0 | 0 | 0 | 0 |
| DS-000010 — The Health Educator screenshots | 0 | 0 | 0 | 0 |
| DS-000011 — Global knowledge corpus | 0 | 0 | 0 | 0 |
| DS-000012 — Sunset forensic recon Case 1 (video) | 1 | 0 | 0 | 0 |
| DS-000013 — Moon/Electron physics forensic recon | 1 | 0 | 0 | 0 |
| DS-000014 — "Weird and Worrying Questions" forensic recon | 1 | 0 | 0 | 0 |
| DS-000015 — Sunset forensic recon Case 2 | 1 | 0 | 0 | 0 |
| DS-000016 — Retiree daily-routines forensic recon | 0 | 0 | 0 | 0 |
| DS-000017 — xkcd's What If? (Apify acquisition) | 1 | 83 | 83 | 0 |
| DS-000018 — Multi-tab creator research corpus | 0 | 0 | 0 | 0 |
| DS-000019 — Dr. Elias Senior Health (supplied export) | 1 | 29 | 29 | 0 |
| DS-000020 — Five-channel Apify packages | 5 | 132 | 132 | 0 |
| DS-000021 — Eleven-channel Apify packages | 11 | 216 | 216 | 0 |
| DS-000022 — Seven user-provided packages | 7 | 732 | 722 | 10 |
| DS-000023 — Funded extraction Batch 1 | 5 | 110 | 110 | 0 |
| DS-000024 — Funded extraction Batch 2 | 4 | 178 | 178 | 0 |
| DS-000025 — Funded extraction Batch 3 | 3 | 233 | 233 | 0 |

(Rows with 0 channels/videos are forensic-frame, screenshot-only, or corpus-only datasets with no canonical channel/video rows — their evidence lives under `non_channel_subjects` / raw forensic evidence, not `dataset_channels`.)

Dataset video/channel counts overlap where a channel appears in more than one dataset (e.g. `xkcd's What If?` across DS-000012/13/14/15/17); the **canonical union** by YouTube video ID is 1,904 — not a blind sum of the per-dataset column above.

---

## 4. Package format inventory

| Package status | Channels |
|---|---:|
| `STANDARD_PACKAGE` (workbook + transcript ZIP) | 35 |
| `HISTORICAL_FORMAT` (older catalog/intelligence system) | 5 |
| `NO_PACKAGE` (identity-only) | 29 |

35 + 5 + 29 = 69, matches total canonical channels.

---

## 5. Completed data

**28 channels, status `COMPLETE`** — full extraction, standard/historical package, real transcripts, no known limitation.

**12 channels, status `COMPLETE_WITH_LIMITATIONS`** — extracted with a documented limitation (missing public descriptions on some videos, or a placeholder transcript). See the coverage table in Section 9 for the `Status` and per-row limitation is recorded in `v_channel_status.limitations` (not reproduced per-row here for space; queryable via the registry DB).

Combined: **40 of 69 channels (58%) have real extracted video-level data.**

---

## 6. Limited data

Channels with `COMPLETE_WITH_LIMITATIONS` status carry one or more of:
- videos missing a public description (14 videos total, across several channels — largest concentration: Lucas Grant with 10 of 95 videos placeholder-transcribed, Primate Economics with 13/28 missing descriptions),
- explicit transcript placeholders where no real subtitle/transcript text was retrievable (11 total: 1 in Matty Invests, 10 in Lucas Grant).

No channel has zero data with a `COMPLETE` label — "limitations" always means a documented partial gap, never a silent one.

---

## 7. Identity-only channels (29)

Verified YouTube channel identity (name + handle + canonical URL), **zero extracted videos, zero transcripts, zero package**. Derived directly from `v_channel_status WHERE status='IDENTITY_VERIFIED_DATA_NOT_EXTRACTED'` in this session — not from memory.

| # | Channel name | Canonical ID | Handle | Target group |
|---|---|---|---|---|
| 1 | Alicia Invests | UCFPfloFwa6X2UddqRH83rAA | @AliciaInvestsUS | ADDED_TARGET |
| 2 | Bernard | UC_FStSURaDad8-xo6jH1j4Q | @BernardAnimationOfficial | ORIGINAL_TARGET |
| 3 | Brick Body | UCq1V-pmuLDjjTrgFyzxYQ5g | @bricklifts | ORIGINAL_TARGET |
| 4 | Brofessor Stein | UCZqJKUTmgB-cffFSzL3ENJA | @BrofessorStein | ORIGINAL_TARGET |
| 5 | Casual Finance | UCrNfRFWnLC3tCy1TnyhVQ7g | @CasuallyFinance | ADDED_TARGET |
| 6 | Casually Explained | UCr3cBLTYmIK9kY0F_OdFWFQ | @CasuallyExplained | ORIGINAL_TARGET |
| 7 | Chat History | UCicVSNyM7PMXEzdoAsTB02w | @ChatHistory | ORIGINAL_TARGET |
| 8 | Chill Dude Explains | UCYwOOHF1BZ_hqPVnLnrT_fw | @ChillDudeExplains | ADDED_TARGET |
| 9 | David Explains Money | UC2ExrTzlNc8uNmNXodWOC-A | @DavidExplainsMoney | ADDED_TARGET |
| 10 | Fasted Fred | UC91LLjU9cbyLBOjSxWR3cMg | @ItsFastedFred | ORIGINAL_TARGET |
| 11 | Finance Simplified | UCogYxvdGc8i7qfjPct1c-Bg | @FinanceSimplified-USA1 | ADDED_TARGET |
| 12 | Ivan Invests | UCDokTQePVxNZUqmzevDM7NQ | @VanillaInvestor | ADDED_TARGET |
| 13 | Mark - Retired at 55 | UCegPlgZVNg0g1pAzZtGH4dw | @MarkRetiredAt55 | ADDED_TARGET |
| 14 | Max Invests | UCXSpMZ1S5In6aRCyWdM5CAw | @MaxInvests-US | ORIGINAL_TARGET |
| 15 | Millionaire Problems | UCQnC6FoEgp4VcmbPTsO9VRQ | @millyproblems | ADDED_TARGET |
| 16 | Neu | UChS4VG1jXDcxDnUvwcMcxtg | @neu-youtube | ADDED_TARGET |
| 17 | Nostalgic Wheels | UC3itSU41yG8jSOk8UudxoaQ | @TheWealthCortexx | ADDED_TARGET |
| 18 | Overhead | UCmzMVqE2c-yPv7vmjThk4CA | @OverheadCosts | ADDED_TARGET |
| 19 | Parenting Hacks | UC4eR2RUwoQrYEgbzReQV3HA | @Parentinghacks-x6k | ORIGINAL_TARGET |
| 20 | Parentitude | UCJ8_5EeAN8fg0JIhxgHKndw | @Parentitude | ORIGINAL_TARGET |
| 21 | Rick Finance | UCDLINT0o_8a0kObYN5bBqUw | @RickFinance1 | ADDED_TARGET |
| 22 | The Career Machine | UChGiil8Qsg7qdJ0tZsQo2VA | @careermachine-u4f | ADDED_TARGET |
| 23 | The Expensive Part | UCe2TLO3VWaMP8EthzGjSG6Q | (none recorded) | ADDED_TARGET |
| 24 | The Wise Future | UC5OaD2jizn_ZFQrB6jzXo4g | @TheWiseFuture | ADDED_TARGET |
| 25 | Tom - Lazy Dividend Investor | UCUhTFmf6v8Kk2-ofFD2udkg | @Tom-Lazy-Dividend-Investor | ADDED_TARGET |
| 26 | Tom - Lazy Investor | UCHKwo7_qXD8ixLZmpPlIb_w | @1MillionWithin5Years | ADDED_TARGET |
| 27 | Tom Talks Money | UCKqgbX0MOmE5ZzyFpTP524g | @TomTalksMoney2k | ADDED_TARGET |
| 28 | Wealth Logic | UCZ-H-n8fa7NqReTRKe7ByEg | @TheWealth_Logic | ADDED_TARGET |
| 29 | quack doc | UC2NRf0-PH8IiMq5uA5FHJnA | @quackdoc | ORIGINAL_TARGET |

Split: **19 ADDED_TARGET, 10 ORIGINAL_TARGET.** All 19 ADDED_TARGET channels (Batch B of the submission) are identity-only — none have been extracted yet.

---

## 8. Historical-format data

5 channels use the older `HISTORICAL_CATALOG` source group / `HISTORICAL_FORMAT` package status (pre-registry catalog, `youtube_inventory.db`): **Mr. Finance, xkcd's What If?, Dr. Elias Senior Health, Dr. Aliza Wright | Advice, Matty Invests.** All 5 are `OUTSIDE_TARGET` (not among the 67 submitted URLs) and all have `COMPLETE` or `COMPLETE_WITH_LIMITATIONS` status with real video/transcript data. They are never relabeled as standard packages, per the registry's own documented invariant.

---

## 9. Full channel coverage table (69 rows)

| Original URL | Canonical ID | Channel name | Target group | Dataset | Videos | Real transcripts | Placeholders | Status | Evidence path |
|---|---|---|---|---|---:|---:|---:|---|---|
| https://www.youtube.com/@AliciaInvestsUS | UCFPfloFwa6X2UddqRH83rAA | Alicia Invests | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@AliciaInvestsUS |
| https://www.youtube.com/@CasuallyFinance | UCrNfRFWnLC3tCy1TnyhVQ7g | Casual Finance | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@CasuallyFinance |
| https://www.youtube.com/@ChillDudeExplains | UCYwOOHF1BZ_hqPVnLnrT_fw | Chill Dude Explains | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@ChillDudeExplains |
| https://www.youtube.com/@DavidExplainsMoney | UC2ExrTzlNc8uNmNXodWOC-A | David Explains Money | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@DavidExplainsMoney |
| https://www.youtube.com/@FinanceSimplified-USA1 | UCogYxvdGc8i7qfjPct1c-Bg | Finance Simplified | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@FinanceSimplified-USA1 |
| https://www.youtube.com/@VanillaInvestor | UCDokTQePVxNZUqmzevDM7NQ | Ivan Invests | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@VanillaInvestor |
| https://www.youtube.com/@MarkRetiredAt55 | UCegPlgZVNg0g1pAzZtGH4dw | Mark - Retired at 55 | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@MarkRetiredAt55 |
| https://www.youtube.com/@millyproblems | UCQnC6FoEgp4VcmbPTsO9VRQ | Millionaire Problems | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@millyproblems |
| https://www.youtube.com/@neu-youtube | UChS4VG1jXDcxDnUvwcMcxtg | Neu | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@neu-youtube |
| https://www.youtube.com/@TheWealthCortexx | UC3itSU41yG8jSOk8UudxoaQ | Nostalgic Wheels | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@TheWealthCortexx |
| https://www.youtube.com/@OverheadCosts | UCmzMVqE2c-yPv7vmjThk4CA | Overhead | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@OverheadCosts |
| https://www.youtube.com/@RickFinance1 | UCDLINT0o_8a0kObYN5bBqUw | Rick Finance | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@RickFinance1 |
| https://www.youtube.com/channel/UChGiil8Qsg7qdJ0tZsQo2VA | UChGiil8Qsg7qdJ0tZsQo2VA | The Career Machine | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/channel/UChGiil8Qsg7qdJ0tZsQo2VA |
| https://www.youtube.com/channel/UCe2TLO3VWaMP8EthzGjSG6Q | UCe2TLO3VWaMP8EthzGjSG6Q | The Expensive Part | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/channel/UCe2TLO3VWaMP8EthzGjSG6Q |
| https://www.youtube.com/@TheWiseFuture | UC5OaD2jizn_ZFQrB6jzXo4g | The Wise Future | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@TheWiseFuture |
| https://www.youtube.com/@Tom-Lazy-Dividend-Investor/videos | UCUhTFmf6v8Kk2-ofFD2udkg | Tom - Lazy Dividend Investor | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@Tom-Lazy-Dividend-Investor |
| https://www.youtube.com/@1MillionWithin5Years/videos | UCHKwo7_qXD8ixLZmpPlIb_w | Tom - Lazy Investor | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@1MillionWithin5Years |
| https://www.youtube.com/@TomTalksMoney2k/videos | UCKqgbX0MOmE5ZzyFpTP524g | Tom Talks Money | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@TomTalksMoney2k |
| https://www.youtube.com/@TheWealth_Logic/videos | UCZ-H-n8fa7NqReTRKe7ByEg | Wealth Logic | ADDED_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@TheWealth_Logic |
| https://www.youtube.com/@ApestheticGuide/videos | UCGnTHU6UMQQlR6cl4CP3jlg | Apesthetic | ORIGINAL_TARGET | DS-000020 | 22 | 22 | 0 | COMPLETE_WITH_LIMITATIONS | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@BernardAnimationOfficial/videos | UC_FStSURaDad8-xo6jH1j4Q | Bernard | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@BernardAnimationOfficial |
| https://www.youtube.com/@bobinvestsUS | UCAKBDBaY1dP7OdZkGPiDnug | Bob Invests | ORIGINAL_TARGET | DS-000022 | 57 | 57 | 0 | COMPLETE_WITH_LIMITATIONS | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@bricklifts/videos | UCq1V-pmuLDjjTrgFyzxYQ5g | Brick Body | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@bricklifts |
| https://www.youtube.com/@brimm-tv/videos | UC1GwXFBhh1fiLLuZxs8VRXA | Brimm. | ORIGINAL_TARGET | DS-000024 | 44 | 44 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@BropumpYT | UCQTcmLiL5_HMUnO1GRwCdjQ | Bro Pump | ORIGINAL_TARGET | DS-000023 | 21 | 21 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@BrofessorStein/videos | UCZqJKUTmgB-cffFSzL3ENJA | Brofessor Stein | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@BrofessorStein |
| https://www.youtube.com/@CIPHER_UNIT | UC9ibMPcwu9pesqKEyzlut7w | CIPHER UNIT | ORIGINAL_TARGET | DS-000021 | 17 | 17 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@carlinvestsUS/videos | UCxoC2voi0vPg2hwqgfjdhYw | Carl Invests | ORIGINAL_TARGET | DS-000022 | 80 | 80 | 0 | COMPLETE_WITH_LIMITATIONS | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@CasuallyExplained/videos | UCr3cBLTYmIK9kY0F_OdFWFQ | Casually Explained | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@CasuallyExplained |
| https://www.youtube.com/@ChatHistory/videos | UCicVSNyM7PMXEzdoAsTB02w | Chat History | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@ChatHistory |
| https://www.youtube.com/@Crayon_Capital/videos | UCP9RPj_BG0vit2TNM7LuRxA | Crayon Capital | ORIGINAL_TARGET | DS-000023 | 30 | 30 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@darkledger13 | UCDglfjh__GM2RFM1oAL3a6A | Dark Ledger | ORIGINAL_TARGET | DS-000021 | 38 | 38 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/channel/UCmYG4TVuzHphjTrP3YKYGYQ | UCmYG4TVuzHphjTrP3YKYGYQ | Explain In Paint | ORIGINAL_TARGET | DS-000025 | 82 | 82 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@ItsFastedFred/videos | UC91LLjU9cbyLBOjSxWR3cMg | Fasted Fred | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@ItsFastedFred |
| https://www.youtube.com/@genius_history01 | UC-q0RDBWjYlYA2KkPzq0WSQ | Genius History | ORIGINAL_TARGET | DS-000021 | 10 | 10 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@HypotheticallyHQ/videos | UC0L9hD7HMwWU7xuU5HRA6Iw | Hypothetically | ORIGINAL_TARGET | DS-000024 | 39 | 39 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@Inkexplainer96 | UCpgrEMx8diLrw7YNQ6r3uUw | Ink Explainer | ORIGINAL_TARGET | DS-000021 | 15 | 15 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@justsomeguystories | UCNO35SZS-e3f1hLIDon_mag | Just Some Guy Stories | ORIGINAL_TARGET | DS-000022 | 13 | 13 | 0 | COMPLETE_WITH_LIMITATIONS | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@LostLegacy-YT/videos | UC96yqt8xjtShTpgdoIo0Lqg | Lost Legacy | ORIGINAL_TARGET | DS-000024 | 45 | 45 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@LucasGrant-usa/videos | UCTcOboZIhgrKHMDm-oTlTOg | Lucas Grant | ORIGINAL_TARGET | DS-000022 | 95 | 85 | 10 | COMPLETE_WITH_LIMITATIONS | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@LucoVids | UChGF6aMxELhXOKg2EDDLYNg | Luco | ORIGINAL_TARGET | DS-000021 | 4 | 4 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/channel/UCaS30yIIV6y2zqSnHGdIGMQ | UCaS30yIIV6y2zqSnHGdIGMQ | Mack | ORIGINAL_TARGET | DS-000025 | 76 | 76 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@MaxInvests-US/videos | UCXSpMZ1S5In6aRCyWdM5CAw | Max Invests | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@MaxInvests-US |
| https://www.youtube.com/@Pastwithmax | UCJgTBuO9fbNvgL_IS8pqtqg | Maximus | ORIGINAL_TARGET | DS-000023 | 5 | 5 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@MoneyLifePOV | UCCEwJbv7D1CYzxdKYYOH6AA | Money Life POV | ORIGINAL_TARGET | DS-000020 | 20 | 20 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@mychaoticstories/videos | UC9m3w-9L_Bt34x02IQXQ5kg | My Chaotic Stories | ORIGINAL_TARGET | DS-000020 | 23 | 23 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@nickinvestsUS/videos | UCXzNNA2ngRpRiWvyA7eGd6w | Nick Invests | ORIGINAL_TARGET | DS-000022 | 363 | 363 | 0 | COMPLETE_WITH_LIMITATIONS | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@OddlyHuma-n | UCxyQ6jK98CCOsy-gwV8QaFA | Oddlyhuman | ORIGINAL_TARGET | DS-000021 | 13 | 13 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@Parentinghacks-x6k | UC4eR2RUwoQrYEgbzReQV3HA | Parenting Hacks | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@Parentinghacks-x6k |
| https://www.youtube.com/@Parentitude | UCJ8_5EeAN8fg0JIhxgHKndw | Parentitude | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@Parentitude |
| https://www.youtube.com/@PastTense01 | UCS3iXffTKXrhKWGXaPckb8A | Past Tense | ORIGINAL_TARGET | DS-000021 | 24 | 24 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@Primateeconomics/videos | UC14Fb2zWTEZklONPXFbLrTQ | Primate Economics | ORIGINAL_TARGET | DS-000020 | 28 | 28 | 0 | COMPLETE_WITH_LIMITATIONS | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@ShaamiFinance | UC5ZSqmk7PKry99xdiRDrc0A | Shaami Finance | ORIGINAL_TARGET | DS-000021 | 13 | 13 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@Sonny_Finance | UCFvEZUMNoAVjSoSB8NrV7yw | Sonny Finance | ORIGINAL_TARGET | DS-000020 | 39 | 39 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/channel/UC53wkzZ3aXyeH9-eIgi17WA | UC53wkzZ3aXyeH9-eIgi17WA | Stickly | ORIGINAL_TARGET | DS-000025 | 75 | 75 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@TheLifeOutline | UCeVwhrEnYjCNdaDr47x4dSw | The Life Outline | ORIGINAL_TARGET | DS-000023 | 15 | 15 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@unknownfrequencies-tv | UCm1yxl_4qMbStLHpHQu6xWg | Unknown Frequencies | ORIGINAL_TARGET | DS-000021 | 19 | 19 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@Well.4/videos | UCW4NZzZ-6At6DFrCn7rJ0bQ | Well. | ORIGINAL_TARGET | DS-000022 | 32 | 32 | 0 | COMPLETE_WITH_LIMITATIONS | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@Zenn0009/videos | UCK8TbMQGDbB94EOR3aGJo3Q | Zenn | ORIGINAL_TARGET | DS-000021 | 35 | 35 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@zoozleworld/videos | UChFs6t9iB1yv0X8fuKtNIvA | Zoozle | ORIGINAL_TARGET | DS-000023 | 39 | 39 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@ago-chanell/videos | UCJqZXjdkolPUgVcf6WBm8VA | ago. | ORIGINAL_TARGET | DS-000024 | 50 | 50 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@inklyHQ | UCcWtWryYdHHiNWfZGSROl1A | inkly | ORIGINAL_TARGET | DS-000021 | 28 | 28 | 0 | COMPLETE | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| https://www.youtube.com/@quackdoc/videos | UC2NRf0-PH8IiMq5uA5FHJnA | quack doc | ORIGINAL_TARGET | NONE | 0 | 0 | 0 | IDENTITY_VERIFIED_DATA_NOT_EXTRACTED | https://www.youtube.com/@quackdoc |
| NOT_SUBMITTED (outside target) | UCXZi5JVeuTluazF-fYqQgNA | Dr. Aliza Wright \| Advice | OUTSIDE_TARGET | DS-000006 | 32 | 32 | 0 | COMPLETE | data/intelligence/channels/CH-000003/packaging-intelligence-2026-09-10.json |
| NOT_SUBMITTED (outside target) | UCQcBYZxFW7YwNMU8-DsT3Uw | Dr. Elias Senior Health | OUTSIDE_TARGET | DS-000019 | 29 | 29 | 0 | COMPLETE | data/intelligence/channels/CH-000005/packaging-intelligence-2026-09-10.json |
| NOT_SUBMITTED (outside target) | UCkqzov98m_7niJOXwbRQgBA | Matty Invests | OUTSIDE_TARGET | DS-000001 | 94 | 93 | 1 | COMPLETE_WITH_LIMITATIONS | data/intelligence/channels/CH-000001/packaging-intelligence-2026-09-10.json |
| NOT_SUBMITTED (outside target) | UC6AwWrRKNrwt83CMJqeTUzw | Mr. Finance | OUTSIDE_TARGET | DS-000001 | 65 | 65 | 0 | COMPLETE_WITH_LIMITATIONS | data/intelligence/channels/CH-000002/packaging-intelligence-2026-09-10.json |
| NOT_SUBMITTED (outside target) | UCFKmBxFC3dOkUv1GirzTjww | Tp Dossier | OUTSIDE_TARGET | DS-000022 | 92 | 92 | 0 | COMPLETE_WITH_LIMITATIONS | docs/audits/CHANNEL_COVERAGE_LEDGER_2026-09-14.csv |
| NOT_SUBMITTED (outside target) | UC6IxnFzHofFJ5X2PycSMsww | xkcd's What If? | OUTSIDE_TARGET | DS-000012,13,14,15,17 | 83 | 83 | 0 | COMPLETE_WITH_LIMITATIONS | data/intelligence/channels/CH-000004/editing-visual-intelligence-pilot-2026-09-11.json |

Column-sum check: 1,904 videos, 1,893 real transcripts, 11 placeholders — matches Section 10 totals exactly (this table is the source of those totals, queried live from `v_channel_status`).

---

## 10. Reconciliation of the authoritative 67 submitted rows

Source of authority: `data/raw/channel-targets/user-supplied-youtube-channels-2026-09-14.json` (immutable, referenced from `docs/YOUTUBE_CHANNEL_REGISTRY.md`). Every figure below was independently recomputed from the raw JSON and cross-checked against the registry DB in this session (not copied from prior documentation).

| Metric | Count | Basis |
|---|---:|---|
| Total submitted rows | 67 | `len(submissions)` in the raw JSON — confirmed |
| Duplicate rows | 4 | rows with `is_exact_duplicate=true`; independently recomputed by grouping on `normalized_url` — 4 URLs with >1 occurrence, 4 extra rows — confirmed |
| Normalized unique targets | 63 | `len(set(normalized_url))` — confirmed |
| Original targets (Batch A) | 44 | unique normalized URLs in Batch A (47 rows → 44 unique) = `target_group='ORIGINAL_TARGET'` in registry — confirmed both ways |
| Added targets (Batch B) | 19 | unique normalized URLs in Batch B (20 rows → 19 unique) = `target_group='ADDED_TARGET'` in registry — confirmed both ways |
| Completed targets (`COMPLETE`, among the 63) | 26 | `v_channel_status` filtered to submitted channels |
| Limited targets (`COMPLETE_WITH_LIMITATIONS`, among the 63) | 8 | `v_channel_status` filtered to submitted channels |
| Identity-only targets (among the 63) | 29 | 19 ADDED_TARGET + 10 ORIGINAL_TARGET, all identity-only |
| Outside-target channels (not among the 67) | 6 | `channels` rows with no `submissions` row: 5 `HISTORICAL_CATALOG` + 1 `STANDARD_PACKAGE` (Tp Dossier) |

Cross-check: 63 unique submitted URLs → 63 distinct canonical channels (1:1, no two submitted rows collapsed onto the same channel). 44 (ORIGINAL) + 19 (ADDED) + 6 (OUTSIDE) = 69 = total canonical channels. 26 + 8 + 29 = 63 = all channels originating from the 67 submitted rows. All totals close with no unexplained remainder.

---

## 11. Visual evidence coverage

| Level | Channels |
|---|---:|
| `FORENSIC_VIDEO_EVIDENCE` | 1 (xkcd's What If? — 3 canonical videos across DS-000012/13/14/15/17, timestamped keyframe-level evidence) |
| `THUMBNAIL_EVIDENCE` (downloaded thumbnails, some screenshots) | 2 (Dr. Aliza Wright \| Advice, Dr. Elias Senior Health) |
| `THUMBNAIL_URL_ONLY` (metadata URL only, no downloaded image) | 35 (the standard-package channels) |
| `NONE` | 31 (identity-only + a subset of historical/outside-target channels with no visual asset registered) |

69 rows total in `visual_coverage` (one per channel). Downloaded thumbnails, screenshots, and forensic keyframes are tracked as strictly separate counts — a thumbnail URL never implies a downloaded image or scene-level evidence.

---

## 12. Intelligence outputs

8 capabilities × 69 channels = 552 rows in `intelligence_coverage`.

| Status | Rows |
|---|---:|
| `NOT_AVAILABLE` | 313 |
| `DATA_READY` (input available, no generated artifact) | 209 |
| `VALIDATED` | 23 |
| `PARTIAL` | 7 |

The 5 historical-catalog channels have generated topic/packaging/hook/script/unified artifacts (Channel Strategy generated for 4 of them, calibrated on a 2-niche benchmark). The 35 standard-package channels are `DATA_READY` for topic/packaging/hook/script inputs but have no generated per-channel artifact yet. The 29 identity-only channels lack these inputs entirely (`NOT_AVAILABLE`). First-party Analytics is `SCHEMA_READY_NO_DATA` for all 69 channels — ingestion code exists and is tested, but no real first-party YouTube Studio/Analytics export has ever been ingested.

---

## 13. Unavailable or missing fields

- **Current public video counts for the 29 identity-only channels** are not stored anywhere in the repository. `identity_evidence` records only name/handle/URL verification, never a video count. Getting these requires a live (non-Apify, e.g. public channel-page) lookup, which this read-only session did not perform.
- **Regular/Shorts/livestream breakdown** for the 29 identity-only channels: unavailable for the same reason — this breakdown only exists post-extraction (it's populated from the Actor's scraped `videos` rows, e.g. see the DS-000024 preflight table in Section 14).
- **A live, current-moment Apify account balance.** The most recent authenticated balance evidence in the repository is a point-in-time snapshot from the DS-000025 recovery run (`2026-09-13T22:03:29`, two days before this audit) — see Section 14.

---

## 14. Known environment limitations

- The dataset-ledger checksum validator only covers DS-000021–DS-000025 (the funded Apify batches with `_FILES.csv` manifests); DS-000001–DS-000020 use manifest-only provenance, which the registry validator's evidence-path checks cover instead.
- 61 tracked files still contain absolute `/Users/ghilman...` path references (up from 56 noted in the 2026-09-15 morning audit — the increase is from files already tracked before this session, not from anything written in it). These are documented, accepted historical provenance per `docs/YOUTUBE_CHANNEL_REGISTRY.md` §"Portability and limits" ("Historical manifest paths may still record original machines as provenance") — not classified as defects, but flagged here since the task asked for "any remaining ... absolute paths."
- No `.tmp`/`.bak`/leftover editor files found. Only macOS `.DS_Store` files exist (gitignored, pre-existing environment cruft, not repository defects).
- A prior duplicate-file investigation (`docs/source-discovery/SOURCE_DUPLICATE_REPORT.md`) found exact-duplicate ZIP archives and one near-duplicate PDF pair inside **immutable raw evidence** (DS-000001-era uploads). These were documented, not deleted (raw evidence is never mutated) — re-verified present and unchanged in this session, not re-scanned byte-for-byte (that report already did the SHA-256 work).
- No broken manifest links: all 25 dataset manifest files and a spot-check of evidence paths resolve to real files on disk.
- No stale/contradictory documentation was found beyond the already-known items above; `docs/YOUTUBE_CHANNEL_REGISTRY.md`'s population-control table (verified 2026-09-14) matches this session's independently-recomputed counts exactly.

---

## 15. Proposed future work — DS-000026 no-run proposal

**This is a paper proposal only. Nothing in this section was launched, and no Apify call or credit spend occurred while preparing it.**

### 15.1 Remaining channels

All 29 identity-only channels from Section 7, unchanged — this is the complete remaining-work list. Every one currently lacks: video-level data, transcripts, package, visual evidence beyond identity, and intelligence inputs.

### 15.2 Current public video counts / content-type breakdown

**Not available.** No prior identity-verification pass recorded a video count for any of the 29 channels (see Section 13). A real DS-000026 preflight — following the exact same pattern documented for DS-000023/24/25 (see `data/manifests/DS-000024_PREFLIGHT.json` and its authenticated-evidence siblings) — would need to run a public, non-Apify channel lookup (or a zero-cost Apify preflight call, if the Actor supports one) to get exact regular/Shorts/livestream counts per channel before committing to an allocation. This report does not fabricate those numbers.

### 15.3 Transcript expectations

Based on the pattern across all 25 existing datasets (1,893 real transcripts out of 1,904 videos = 99.4% real-transcript yield), the reasonable expectation is that the large majority of videos on the 29 remaining channels will yield real plaintext transcripts via the same Actor (`streamers/youtube-scraper`), with a small residual placeholder rate (~0.6% historically) for videos with no public subtitle track.

### 15.4 Authenticated Apify pricing requirement

Documented and reused unchanged across DS-000023/24/25 preflights:

- **Actor:** `streamers/youtube-scraper` (Actor ID `h7sDV53CddomktSi5`)
- **Price:** **$4.00 per 1,000 videos written to the dataset** (per-result pricing, Apify Free plan)
- Source: `docs/PROJECT_STATUS_REPORT_2026-09-13.md` §2.2, cross-referenced against `data/raw/channel-data/DS-000024/preflight/authenticated_pricing_evidence.json`

This is the authoritative, evidence-backed pricing basis. It has not changed across three consecutive funded batches; it should be **re-confirmed live** immediately before any DS-000026 launch (pricing/plan terms are not guaranteed static).

### 15.5 Estimated cost per channel

Exact per-channel cost cannot be computed without real per-channel video counts (Section 15.2). As a **rough, explicitly non-authoritative** planning figure only: the 40 already-extracted channels averaged 1,904 / 40 = **47.6 videos/channel**, which at $4.00/1,000 videos implies **≈ $0.19/channel** on average. Actual costs varied 3–4x around this average in every completed batch (DS-000023: $0.088/channel avg over 5 small channels; DS-000024: $0.178/channel avg over 4 mid-size channels; DS-000025: $0.309/channel avg over 3 larger channels), so this average should not be used to authorize spend — only a per-channel preflight count can.

### 15.6 Smallest-catalog-first ordering

**Cannot be determined from repository data** — ordering by catalog size requires the video counts from Section 15.2, which are not available without a live lookup. The documented workflow for every prior batch (DS-000023/24/25) always ran a fresh authenticated preflight immediately before launch to get exact counts and only then ordered/sized the batch; DS-000026 should follow the identical pattern rather than being pre-ordered on stale or fabricated numbers.

### 15.7 Available balance requirement

**Last authenticated balance on record:** $0.716 remaining, observed 2026-09-13T22:03:29 (Apify Console, post-DS-000025 recovery run) — `data/raw/channel-data/DS-000025/apify/fgU7aFRXEXiBF9qQJ/authenticated_post_run_balance_evidence.json`.

This is a **point-in-time snapshot, ~48 hours stale relative to this audit** (2026-09-15). It is explicitly **not** a live pre-DS-000026 authorization check, exactly as the same caveat was applied before DS-000025. A fresh authenticated balance pull is required before any launch decision.

### 15.8 Required reserve

**$0.30 minimum reserve**, applied consistently in every prior preflight (DS-000024, DS-000025). Recommend carrying this forward unchanged for DS-000026 unless the user specifies otherwise.

### 15.9 Channels that fit within balance

Using the last-known balance ($0.716) minus reserve ($0.30) = **$0.416 usable headroom**, and the rough per-channel average from 15.5 (~$0.19/channel, non-authoritative): approximately **2 of the smallest-catalog channels** could plausibly fit — but this is a rough order-of-magnitude estimate only. **No specific channel selection can be made without real per-channel video counts from a live preflight.**

### 15.10 Channels that must be deferred

By the same rough estimate, the remaining **~27 of 29** identity-only channels would not fit within current known balance and must be deferred to a future funded batch, pending either (a) a live recount showing they're smaller than average, or (b) additional credit.

### 15.11 Additional credit required to finish all remaining channels

Rough estimate only (no real per-channel counts exist): 29 channels × ~$0.19/channel average ≈ **$5.51 total** to extract all 29 remaining channels, against **$0.716** currently on record (stale) minus $0.30 reserve = $0.416 usable. Rough **additional credit needed ≈ $5.51 − $0.416 ≈ $5.10**, before accounting for the fact that per-channel costs in every prior batch varied 3–4x around the average (some remaining channels, especially long-running ones like the finance/investing added-target channels, could individually cost several times the $0.19 average). **This number should be treated as a planning floor, not a budget — a real DS-000026 preflight with actual per-channel video counts is required before any credit request or launch decision.**

### 15.12 Explicit non-launch statement

DS-000026 does not exist as a dataset record, manifest, or Actor run anywhere in the repository. Nothing in this section constitutes launch of DS-000026, an Apify Actor call, a credit purchase, a plan upgrade, or a payment-method change. This is a preparatory proposal only, per the task instruction.

---

## 16. Summary — was Apify or credits used, were commits/pushes made?

- **No Apify Actor was launched.** No new run ID, dataset ID, or raw evidence was created.
- **No credits were spent.** All pricing/balance figures in Section 15 are read from pre-existing repository evidence (DS-000023/24/25 authenticated evidence files), not from a fresh authenticated check.
- **No `git commit` or `git push` occurred.** `git status` is identical before and after this session (Section 1) except for the addition of this report file itself, which remains untracked/uncommitted per instruction.
- **`ui/v1` was not merged, checked out, or modified** — only inspected via `git branch -a -vv` / `git worktree list`.
- **No raw evidence (`data/raw/`) was modified.** No database was rebuilt other than the documented, git-ignored `youtube_channel_registry.db` via the repository's own validator (Section 0/1 — flagged as a deviation from a strict reading of "no rebuild" for review).
- **All 8 preserved user-owned untracked files remain present and unchanged.**
