# YIOS Progress Report — Verification (2026-11-11)

Verified: `~/Downloads/YIOS_COMPLETE_PROJECT_PROGRESS_REPORT_2026-11-11.md` against this machine's repo
(`/Users/ghilmanislam360/Documents/youtube-intelligence-os`, branch `research/finance-economics-intelligence`).
Method: read-only git, `gh`, sqlite, csv and filesystem checks. Nothing was modified, committed or pushed.
Legend: MATCH = confirmed now; STALE = was true, changed; NOT VERIFIABLE = evidence not on this machine.

## MATCH
| Claim | Result |
|---|---|
| Registry SHA-256 `39e7a28b…2f654` | identical |
| Registry channels / videos | 75 / 2,303 |
| Finance queue | 1,612 unique IDs, 27 channels; `FROZEN_ORIGINAL_966`=966, other layers 386+197+63=646 |
| Fully accepted | 558 rows with `accepted_batch_id`; 558 `COMPLETE_LIMITED_EVIDENCE` |
| Local MP4 inventory | 454 files, 4,361,600,146 bytes (`~/Documents/YIOS-Media-Library`) |
| MP4 per folder | CasuallyFinance 216, xkcd 88, MonkeBiznis 63, PrimitiveEducation 44, PrimateEconomics 29, casual_economics 11, BarelyEvolved 3 |
| Seal verification | 28 rows: 5 PASS, 9 SUPERSEDED, 10 PASS_HEAVY_FILES_LOCAL_ONLY, 4 FAIL |
| Commit SHAs | efd3dc0a, 3c6145cc, ff2ff896, 3e587c75, 9a4023af, 7cba97ef, 2697d3c6 all exist |
| Reanalysis progress | 26/558, all SEMANTIC_REVIEW_PENDING (git log) |
| Open draft PRs | #36, #38, #39, #41, #43, #45, #47 open+draft; 20 open total |

## STALE (report is older than reality)
| Report says | Now |
|---|---|
| PR #48 open, not merged | MERGED 2026-11-09T20:11:19Z, merge commit `fd029485` = `origin/main` |
| 33 local / 54 remote branches | 27 local / 56 remote |
| 3 worktrees | 4 (different names/locations) |
| `.git` ~5.9 GB | 5.4 GB |
| PR totals 40 (19 merged, 1 closed, 20 open) | 41 (20 merged, 1 closed, 20 open) |

## NOT VERIFIABLE on this machine
- `~/workprojects/...` and `~/YIOS-local-audits/...` do not exist here (this machine uses `~/Documents/YIOS-local-audits`, only up to 2026-11-05). The report likely describes another machine.
- Commit `34a79e46` (`cleanup/yios-phase2-batch1`) is not in this repo (report itself says unpushed).
- 2026-11-10 Finance Apify run (`finance-apify-run`, `FINANCE_VIDEO_MASTER_ALL.*`, `TRANSCRIPTS_ALL.jsonl`, `BATCH_RUN_MANIFEST.json`) not found anywhere searched. Unverified: 24/24 channels, 1,093 rows, 1,264/1,266 transcripts, 2 gaps, $4.388 spend.
- Stage A (124/120/115/190 and the 89-channel niche table) and `Finance_List.csv` / `Economics_List.csv`: folders absent here. Unverified.
- Legacy LFS MP4 pointers: report says 17; a pointer-text scan of `origin/research/casually-finance-consolidated` found 19 files (may include the registry DB). Unresolved.
- Not checked: GitHub-side LFS object availability, Machine B state, CI status of every PR.

## Next
Run the same checks on the machine that holds `~/YIOS-local-audits/2026-11-10-*` to close the NOT VERIFIABLE rows.
