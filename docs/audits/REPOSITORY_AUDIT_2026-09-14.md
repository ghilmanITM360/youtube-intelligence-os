# Repository, Git, Data, and Intelligence Audit — 2026-09-14

## 1. Executive summary

Audit verdict: the live GitHub repository contains the DS-000025 completion at `a22c8d25eedcb092f5773ac3ebe789aaa0ebddc8`, but this working tree is still at `56296874e821152b993ff9a01bf86a2cced43b4f` and is 11 commits behind `origin/main`. Nothing is ahead or diverged. A normal fast-forward is possible, but no pull, commit, push, checkout, rebuild, extraction, or dataset mutation was performed.

The live tree has 25 durable dataset manifests. The scraped-channel package layer contains 35 packages, 35 unique YouTube canonical channel IDs, and 1,601 unique video IDs: 1,591 real transcripts, 10 explicit verified placeholders, zero absent transcript files, and 14 uploader-empty public descriptions. These figures were recomputed from remote Git blobs, package workbooks, transcript ZIPs, combined JSON/CSV, manifests, and checksums.

The claimed original 44-channel reconciliation is not independently reproducible from the repository: no authoritative 44-URL input ledger or list of the ten remaining targets is tracked or present locally. The repository proves 35 stored channels; it does not prove which 34 are original targets, that Tp Dossier is the sole extra, or the identities of the purported ten remaining channels. DS-000026 is therefore **not ready for extraction or evidence-complete planning**.

The intelligence layer is real code, not documentation-only: five of the eight audited capabilities are implemented and validated, two are implemented but coverage/calibration-limited, and one is data-ready only. Production UI, dashboard, API, RAG/vector store, embeddings, MCP server, custom agent workflow, scheduled automation, YouTube API integration, and alternative scraper are not built.

## 2. Audit scope and timestamp

- Repository: `/Users/ghilmanislam360/Documents/youtube-intelligence-os`
- Baseline: `2026-09-14 11:02:20 PKT (+0500)`, Asia/Karachi
- Fetch completed: `2026-09-14 11:03:22 PKT (+0500)`
- Git: `2.50.1 (Apple Git-155)`
- Audit mode: read-only except these five uncommitted report files
- Usage checks: 2% at start; 34% primary / 5% weekly during audit; no threshold action required

Evidence covered the local working tree, all local refs, fetched remote-tracking refs, `git ls-remote`, authenticated GitHub API results, live `origin/main` blobs, history, manifests, raw evidence, workbooks, ZIPs, generated intelligence artifacts, SQLite in read-only mode, validators, and tests.

## 3. Authoritative evidence hierarchy

1. Repository rules: `AGENTS.md` and raw-evidence immutability/provenance requirements.
2. Immutable raw artifacts plus actual byte hashes.
3. Dataset manifests, file/checksum ledgers, source-artifact ledgers, and validation reports.
4. Recomputed structural results from the actual JSON, CSV, XLSX, ZIP, and SQLite files.
5. Source code, tests, and committed generated intelligence outputs.
6. Live GitHub API/`git ls-remote` for remote state.
7. Narrative status reports, handoffs, README, scope, and phase documents; these are context, not final truth when later evidence supersedes them.

Authoritative-for-purpose files include `data/manifests/DS-*.md`, their ledgers, raw evidence, and `data/intelligence/system/*`. `docs/DATA_INVENTORY.md`, `docs/PROJECT_STATUS_REPORT_2026-09-13.md`, and `docs/DS-000025_CONTINUATION_HANDOFF.md` contain time-bound or stale statements described below.

## 4. Local Git snapshot

| Item | Result |
|---|---|
| Branch | `main` |
| Local HEAD | `56296874e821152b993ff9a01bf86a2cced43b4f` |
| Upstream tracking ref after fetch | `origin/main` = `a22c8d25eedcb092f5773ac3ebe789aaa0ebddc8` |
| Ahead / behind | 0 / 11 |
| Tracked modified | 0 |
| Staged | 0 |
| Pre-audit untracked | 3 |
| Pre-audit untracked paths | `.codex/environments/environment.toml`; two older audit Markdown files in `docs/` |
| Stash | none |
| Tags | none |
| Submodules | none; no `.gitmodules` |
| Sparse checkout / partial clone | not configured |
| Hooks | no active custom hooks; sample hooks only |
| Git LFS | CLI unavailable; no LFS attributes or pointer files found |
| Diff / cached diff / diff check | empty / empty / pass |

The audit reports add five more untracked files; final expected untracked count is 8. Existing uncommitted user files were not changed.

Historical checkpoints were verified in history:

- Reported latest HEAD `a22c8d25...`: live `main` tip and DS-000025 completion.
- Raw checkpoint `c105e059...`: parent of final DS-000025 commit; preserves raw run evidence.
- Status report `19dd42f...`: project status through DS-000024; later superseded by two DS-000025 commits.

The difference is not a rewritten checkpoint: the local checkout simply remained at an earlier commit while the remote advanced by 11 commits.

## 5. Live GitHub snapshot

Authenticated GitHub inspection verified:

- Repository: `ghilmanITM360/youtube-intelligence-os`
- Visibility: private
- Default branch: `main`
- Live branches: `main` at `a22c8d25...`; `ui/v1` at `0412932a...`
- Open PRs: 0; draft PRs: 0; repository PR history returned 0 records
- Actions runs: 0; therefore no recent failed workflow exists, but there is also no CI proof
- Releases/tags: 0/0
- Branch-list protection flags: false for both branches
- Full ruleset/protection details: not inspectable; GitHub returned 403 requiring a plan upgrade or public repository
- Local `origin/*` refs match `git ls-remote` live SHAs after fetch
- No Git LFS configuration/pointers or API-exposed large-file warning was found; large artifacts are ordinary Git blobs

`origin/main` is a local remote-tracking ref. It is cited only after the independent live checks above.

## 6. Complete branch matrix

The canonical CSV is [REPOSITORY_BRANCH_LEDGER_2026-09-14.csv](./REPOSITORY_BRANCH_LEDGER_2026-09-14.csv).

| Branch | Type | HEAD | Upstream/live | Ahead | Behind | Worktree | Status |
|---|---|---|---|---:|---:|---|---|
| `main` | local | `5629687` | `origin/main` / `a22c8d2` | 0 | 11 | current | behind; fast-forwardable |
| `ui/v1` | local | `0412932` | `origin/ui/v1` / same | 0 | 0 | `youtube-intelligence-os-ui` | synchronized with its remote; not merged to `main` |
| `main` | live remote | `a22c8d2` | default | — | — | — | unprotected |
| `ui/v1` | live remote | `0412932` | — | — | — | other worktree | unprotected; unmerged to `main` |

No local-only or remote-only branch exists. Fetch pruned no branch. `ui/v1` contains one documentation commit relative to its base and adds two UI/backend handoff documents; do not archive it until those documents are reviewed for integration.

## 7. Pull-versus-push delta

| Branch | Pull would receive | Push would send | Fast-forward safe | Action required |
|---|---:|---:|---|---|
| `main` | 11 commits | 0 commits | yes; local is ancestor | separate approval for `git pull --ff-only origin main` |
| `ui/v1` | 0 | 0 | already equal | none |

Incoming `main` commits, newest first:

| SHA | Subject |
|---|---|
| `a22c8d25` | data: complete DS-000025 funded channel extraction |
| `c105e059` | data: checkpoint DS-000025 actor evidence |
| `19dd42f6` | docs: add project status through DS-000024 |
| `57491326` | data: add DS-000024 funded channel extraction |
| `9f5e41d8` | data: preserve DS-000024 raw extraction evidence |
| `4fbdd57f` | data: add funded channel extraction batch one |
| `b138af0e` | data: finalize Lucas Grant transcript recovery evidence |
| `a6223dca` | data: add seven user-provided channel packages |
| `b69c214c` | data: complete DS-000021 artifact registration |
| `78ad5d72` | data: add eleven-channel YouTube dataset packages |
| `6aaa1c4b` | data: add five-channel YouTube dataset packages |

The incoming range affects 235 files with 765,206 insertions and one deletion. It adds DS-000020–DS-000025 artifacts/raw evidence/manifests, new validators and tests, and updates `.gitignore`, `docs/DATA_INVENTORY.md`, and `scripts/README.md`. There are no outgoing commits or outgoing files. No merge/rebase decision is required because there is no divergence.

## 8. Worktree, stash, tag, and remote status

- Worktrees: two, both valid and on distinct branches.
- Stashes: zero.
- Tags: zero locally and remotely.
- Remote: one named `origin`; public HTTPS URL contains no embedded credentials.
- Git objects after fetch: 888 loose objects / 29.34 MiB; packed objects 42.14 MiB; no garbage.

## 9. Repository size and storage map

### Working copy

| Scope | Size |
|---|---:|
| Whole checkout including `.git` and ignored local evidence | 977,404 KiB (about 954.5 MiB) |
| `data/` | 870,996 KiB (about 850.6 MiB) |
| `data/raw/` | 801,732 KiB (about 782.9 MiB) |
| `data/intelligence/` | 8,784 KiB |
| `data/manifests/` | 13,300 KiB |
| `.git/` on disk | 74,368 KiB (about 72.6 MiB) |

The local `data/extracted/` is nearly empty because the checkout predates the six package commits; the files exist in live `origin/main`.

### Live tracked tree

- 454 tracked files, 168,723,590 logical bytes (about 160.9 MiB).
- `data/`: 333 files / 167,196,282 bytes.
- `data/extracted/`: 119 files / 113,423,563 bytes.
- `data/raw/`: 74 files / 31,102,785 bytes.
- `data/intelligence/`: 66 files / 8,833,277 bytes.
- `data/manifests/`: 71 files / 13,811,193 bytes.
- Current local HEAD tracks 222 files.
- Ignored local entries: 3,058 = 1,745 raw, 1,301 `.venv`, 5 pytest cache, 4 `.DS_Store`, and 3 catalog DB files.

File types by live-tree count/size: JSON 140/69.41 MB; CSV 31/60.72 MB; ZIP 42/19.56 MB; XLSX 48/12.44 MB; PNG 2/4.26 MB; Python 57/1.03 MB; Markdown 99/0.93 MB; text 5/0.18 MB; SQL 10/0.034 MB; remaining small support files.

Largest 20 tracked paths are ordinary Git blobs:

| Bytes | Path |
|---:|---|
| 18,189,527 | DS-000025 combined master CSV |
| 12,828,893 | batch file inventory CSV |
| 10,986,392 | DS-000021 combined master CSV |
| 8,574,739 | DS-000024 combined master CSV |
| 7,142,564 | DS-000025 clean JSON |
| 7,142,564 | DS-000025 master JSON; same blob as clean JSON |
| 6,994,665 | DS-000025 original raw Actor JSON |
| 4,942,355 | DS-000023 combined master CSV |
| 4,865,160 | DS-000020 combined master CSV |
| 4,690,521 | DS-000021 clean JSON |
| 4,690,521 | DS-000021 master JSON; same blob as clean JSON |
| 4,600,928 | DS-000021 raw Actor JSON |
| 3,579,689 | DS-000024 clean JSON |
| 3,579,689 | DS-000024 master JSON; same blob as clean JSON |
| 3,526,627 | DS-000025 combined workbook |
| 3,479,388 | DS-000024 raw Actor JSON |
| 3,421,753 | Nick Invests transcript ZIP |
| 3,421,753 | Nick Invests immutable source ZIP; same blob |
| 2,312,448 | DS-000021 combined workbook |
| 2,147,603 | DS-000023 authenticated pricing screenshot |

Proven duplicates include clean/master JSON pairs and byte-identical DS-000022 source/canonical workbooks and ZIPs. These are intentional lineage copies, not unexplained duplicate datasets.

### Top-level map

| Path | Purpose/state |
|---|---|
| `data/raw/` | immutable/source evidence, mostly intentionally ignored locally; selected raw Actor evidence tracked |
| `data/extracted/` | packaged channel workbooks, transcript ZIPs, combined outputs, validation reports |
| `data/normalized/` | reserved; effectively empty (`.gitkeep`) for the new package layer |
| `data/intelligence/` | channel, cross-channel, blueprint, and system intelligence outputs |
| `data/manifests/` | durable dataset identity, file checksums, lineage, batch inventory |
| `data/catalog/` | regenerable gitignored SQLite indexes; not canonical evidence |
| `scripts/` | ingestion, validation, reporting, packaging, orchestration |
| `tests/` | unit/integration tests and synthetic fixtures |
| `schemas/` | SQLite migrations/contracts |
| `docs/` | scope, phases, plans, reports, handoffs, decisions |
| `channels/`, `config/`, `logs/` | currently reserved/minimal scaffolding |

Confirmed flow:

```text
raw immutable source evidence
→ extracted/canonical channel packages and combined records
→ catalog/canonical intelligence records where explicitly registered
→ intelligence artifacts
→ reports and unified orchestration
```

The scraped package population is not automatically loaded into the 303-item intelligence catalog.

## 10. Dataset inventory

There are 25 live durable dataset manifests, not 24.

| ID | Title/source | Layer/status | Manifest-introducing commit |
|---|---|---|---|
| DS-000001 | Matty Invests & Mr. Finance package | canonical competitor / structured | `d6213be` |
| DS-000002 | Wealthy Retirees forensic reconstruction | forensic / ingested | `065e0b4` |
| DS-000003 | Doctor Thomas screenshots | screenshot / ingested | `065e0b4` |
| DS-000004 | Dr Adewale screenshots | screenshot / ingested | `065e0b4` |
| DS-000005 | Dr Okoro screenshots | screenshot / ingested | `065e0b4` |
| DS-000006 | Dr Aliza screenshots + linked Apify | canonical competitor / structured | `065e0b4` |
| DS-000007 | Dr Waterling screenshots | screenshot / ingested | `065e0b4` |
| DS-000008 | Senior Health Podcast screenshots | screenshot / ingested | `065e0b4` |
| DS-000009 | Senior Health Hub screenshots | screenshot / ingested | `065e0b4` |
| DS-000010 | Health Educator screenshots | screenshot / ingested | `065e0b4` |
| DS-000011 | global YouTube training knowledge | document corpus / ingested | `065e0b4` |
| DS-000012 | Sunset forensic case 1 | forensic / ingested | `065e0b4` |
| DS-000013 | Moon/Electron forensic case | forensic / ingested | `065e0b4` |
| DS-000014 | Weird/Worrying forensic case | forensic / ingested | `065e0b4` |
| DS-000015 | Sunset forensic case 2 | forensic / ingested | `065e0b4` |
| DS-000016 | Retiree routines forensic case | forensic / ingested | `065e0b4` |
| DS-000017 | xkcd What If? Apify acquisition | canonical competitor / structured | `f0139ef` |
| DS-000018 | 2026 algorithm research document | research source / structured | `5d6fc75` |
| DS-000019 | Dr Elias supplied channel export | canonical competitor / structured | `24021ae` |
| DS-000020 | five-channel Apify packages | package / structured registered | `6aaa1c4` |
| DS-000021 | eleven-channel Apify packages | package / structured registered | `78ad5d7` |
| DS-000022 | seven user-provided packages | package / validated source package | `a6223dc` |
| DS-000023 | funded extraction batch 1 | package / structured registered | `4fbdd57` |
| DS-000024 | funded extraction batch 2 | package / structured registered | `5749132` |
| DS-000025 | funded extraction batch 3 | package / structured registered | `a22c8d2` |

DS-000020/21/23/24/25 have combined JSON/CSV/XLSX, per-channel workbook, per-channel transcript ZIP, validation report, manifest, checksum ledger, and source-artifact ledger. DS-000022 is a user-supplied package set: it has per-channel workbook/ZIP source and canonical copies plus validation/recovery/overlap evidence, but no dataset-wide combined JSON/CSV/XLSX and no original Actor raw/run IDs.

All DS-000020–25 artifacts are tracked at live `main`; most are not materialized in the current local checkout because it is behind.

## 11. Channel coverage ledger

The complete 35-row canonical ledger, including handles and YouTube channel IDs, is [CHANNEL_COVERAGE_LEDGER_2026-09-14.csv](./CHANNEL_COVERAGE_LEDGER_2026-09-14.csv).

| Dataset | Packages | Videos | Regular | Shorts | Live | Real | Placeholders | Missing descriptions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| DS-000020 | 5 | 132 | 118 | 14 | 0 | 132 | 0 | 14 |
| DS-000021 | 11 | 216 | 216 | 0 | 0 | 216 | 0 | 0 |
| DS-000022 | 7 | 732 | 732 | 0 | 0 | 722 | 10 | 0 |
| DS-000023 | 5 | 110 | 110 | 0 | 0 | 110 | 0 | 0 |
| DS-000024 | 4 | 178 | 178 | 0 | 0 | 178 | 0 | 0 |
| DS-000025 | 3 | 233 | 233 | 0 | 0 | 233 | 0 | 0 |
| **Total** | **35** | **1,601** | **1,587** | **14** | **0** | **1,591** | **10** | **14** |

All 35 canonical channel IDs are unique. All 1,601 video IDs are unique within and across these six datasets. The ten Lucas Grant files are explicit placeholders for members-only videos with captions unavailable; zero transcript files referenced by workbook rows are absent.

Raw Apify/source-run accounting across the whole repository:

- 10 runs have retained raw payloads: DS-000017 (1) plus DS-000020–25 (9, including two targeted recovery runs).
- One legacy DS-000006 run is documented (`bD7JBsuj7LK5Wt2rk`, cost `$0.128`) without retained raw payload.
- Total documented Actor runs: 11; retained raw runs: 10; legacy raw-evidence gap: 1.
- DS-000022 original user packages have no supplied original run/dataset IDs; its single targeted recovery run is retained.

Cost evidence exists for DS-000006 (`$0.128`), DS-000022 recovery (`$0.040`), DS-000023 (`$0.440`), DS-000024 (`$0.712`), and DS-000025 (`$0.932`, from its two-run checkpoint evidence). Recorded balances are historical point-in-time evidence, not a live credit balance.

## 12. Original 44-channel reconciliation

This required reconciliation is **blocked by missing source evidence**, not by channel-name ambiguity.

- No file in the live tracked tree, ignored non-raw project files, or the three pre-existing untracked files contains the original normalized 44 URLs.
- The DS-000025 handoff says to reconstruct the ledger but does not contain the list.
- The repository proves 35 stored unique channel IDs.
- It does not independently prove that exactly 34 are from the original 44, that Tp Dossier is the only outside target, or the exact remaining ten.

Therefore the requested per-original-URL table cannot be populated without inventing evidence. Current evidence-safe classification is:

| Population | Count | Status |
|---|---:|---|
| Stored package channels | 35 | verified by canonical IDs |
| Purported original-target members | 34 | historical/user claim; not independently reproducible |
| Tp Dossier as purported extra | 1 | plausible but original list absent |
| Purported remaining targets | 10 | arithmetic claim only; URLs/names/IDs unavailable |
| Exact unique original targets | unknown from repository | original 44-URL ledger missing |

The ten remaining channels must not be reconstructed from model memory or display names.

## 13. Raw/extracted/normalized/intelligence architecture

The repository maintains two distinct populations:

1. The legacy/canonical intelligence catalog: five `CH-*` channels, 303 content items, 302 available transcripts and one unavailable transcript.
2. The later scraped package layer: 35 YouTube canonical channel IDs and 1,601 video records in DS-000020–25.

There is no repository contract asserting these are the same population, and this audit did not combine them. `data/normalized/` does not currently bridge DS-000020–25 into the SQLite catalog.

## 14. Available data fields and formats

The DS-000020/21/23/24/25 combined Actor-derived records expose, where supplied: video ID/URL/title/type/date/duration; channel ID/name/handle/URL/description/joined date/location/total videos/views/subscriber count; view/like/comment counts; description and links/hashtags/collaborators; thumbnail/avatar/banner URLs; membership/age/paid/monetization/verification flags; source/input/order fields; plaintext/subtitle/transcription references; translated title/text; AI summary/description; description-recovery and provenance blocks.

CSV flattens the canonical record and includes `transcript_plaintext`, unavailable reason, and Actor transcription URL. Workbooks use five sheets: Channel Overview, All Videos, Descriptions, Verification, and Analysis. ZIPs contain per-video transcript text plus index/readme members. JSON preserves nested Actor/source structure; raw JSON preserves source bytes.

The intelligence catalog additionally stores channel/video snapshots, normalized public metrics, transcript provenance, visual assets, OCR/semantic observations, classifications, and dataset/run/source-file lineage. First-party Analytics supports CSV, TSV, and XLSX contracts, but only synthetic fixtures are present.

## 15. Artifact-integrity results

Fresh live-blob checks:

- JSON parses: DS20 8/8; DS21 6/6; DS22 5/5; DS23 11/11; DS24 16/16; DS25 28/28.
- CSV parses: 28/28 relevant files.
- XLSX opens/CRC: DS20 6/6; DS21 12/12; DS22 14/14 source+canonical; DS23 6/6; DS24 5/5; DS25 4/4.
- ZIP CRC: DS20 5/5; DS21 11/11; DS22 14/14 source+canonical; DS23 5/5; DS24 4/4; DS25 3/3.
- Workbook rows, combined records where present, ZIP transcript references, raw IDs, and cross-dataset IDs reconcile to 1,601 unique IDs.
- No null video IDs or within/across-package duplicate video IDs were found.
- Placeholder transcripts are explicitly labeled.
- Nine combined-workbook transcript values exceed Excel's 32,767-character cell limit: 3 in DS-000021, 1 in DS-000023, 5 in DS-000024. Full text remains in CSV, JSON/raw evidence, and transcript ZIPs; this is not transcript loss.

Checksum/manifest ledger findings at live tip:

| Dataset | Result |
|---|---|
| DS-000020 | 26/26 ledger rows match current paths/bytes/hashes |
| DS-000021 | 35/39 match; 4 historical rows point to shared scripts/docs changed by later commits |
| DS-000022 | 44/47 match; 3 shared validator/test/inventory files changed later |
| DS-000023 | 39/43 match; 3 shared files changed; one raw path is malformed/nested in the ledger while the actual tracked raw file is one directory higher |
| DS-000024 | 36/38 match; 2 shared packager/test files changed later |
| DS-000025 | all 24 listed rows match; however 26 dataset-scoped tracked files are not included in its file ledger |

DS-000025 raw original and recovery SHA-256 values match their frozen source evidence. All files involved are tracked on live `main`. The mismatch pattern does not show mutated raw evidence; it shows historical ledgers containing mutable shared repository files and incomplete/path-defective ledger coverage.

Path/link findings:

- 79/79 repository-relative Markdown links resolve in the live tree.
- Many source-artifact CSV rows retain historical absolute `/Users/ghilmankhan/...` or Downloads paths; these are non-portable source locators, not current repository paths.
- DS-000025 manifest's “cross-dataset overlap evidence” link resolves but incorrectly points to the DS-000024 overlap report instead of DS-000025.

## 16. Intelligence capability matrix

The canonical CSV is [INTELLIGENCE_CAPABILITY_AUDIT_2026-09-14.csv](./INTELLIGENCE_CAPABILITY_AUDIT_2026-09-14.csv).

| Capability | Audit status | Coverage | Material limitation |
|---|---|---:|---|
| Topic Opportunity | `IMPLEMENTED_AND_VALIDATED` | 5 | public association, not retention causality |
| Packaging | `IMPLEMENTED_AND_VALIDATED` | 5 | CH-000001/2 title-only; thumbnails absent |
| Hook | `IMPLEMENTED_AND_VALIDATED` | 5 | positional timing approximations when transcripts are untimed |
| Script | `IMPLEMENTED_AND_VALIDATED` | 5 | opportunity linkage can be `PARTIAL` |
| Editing/Visual | `IMPLEMENTED_PARTIAL` | 1 | evidence only for CH-000004; four channels correctly return `NOT_AVAILABLE` |
| Unified orchestration | `IMPLEMENTED_AND_VALIDATED` | 5 | requires local catalog; medical validation external source absent |
| Channel Strategy | `IMPLEMENTED_PARTIAL` | 4 | `GENERALIZED_WORKING`; only two channels per niche; zero robust cross-niche patterns |
| First-party Analytics | `DATA_READY_ONLY` | 0 real | code/contract/synthetic tests exist; no real Studio export |

Cross-niche calibration contains 7 heuristic results: 3 conflicting, 2 insufficient, 1 channel-specific, 1 niche-specific, and zero `ROBUST_CROSS_NICHE_PATTERN` results.

Explicitly not built in tracked code: production UI, dashboard, HTTP/API service, RAG/vector store, embeddings, MCP server, production custom-agent workflow, scheduler/automation, YouTube Data API integration, and alternative scraper. The `ui/v1` branch adds documentation only.

## 17. Test and validation results

| Check | Result | Interpretation |
|---|---|---|
| Focused intelligence suite in current checkout | 167/167 pass | uses available local catalog/raw fixtures |
| Full current-checkout unittest discovery | 249 pass / 250 run / 1 error | only `pytest` missing for first-party test import |
| Full live `origin/main` archive suite | 222 pass / 239 run / 17 errors | clean archive intentionally lacks gitignored catalog and DS-000011 raw fixture; bundled runtime lacks pytest |
| Package structural integrity | 35/35 packages pass | direct read-only JSON/CSV/XLSX/ZIP/ID reconciliation |
| `git diff --check` | pass | no tracked diff issues |

The historical 17-error pattern is reproduced exactly in a clean live-tree archive: 15 errors require the gitignored SQLite catalog, one requires the untracked DS-000011 raw fixture, and one requires unavailable `pytest`. These are environment/fixture failures, not 17 newly discovered code regressions. No dependency was installed and no fixture/catalog was generated.

Additional existing validators exposed current issues:

- `inventory_catalog.py verify`: DS-000001–11 and DS-000017–19 passed; DS-000012–16 raise a `TypeError` because `REFERENCE_ONLY` rows have null canonical paths. This is a validator compatibility defect, not proof of missing forensic data.
- `register_structured_source.py verify`: DS-000001 passes; DS-000006, DS-000017, and DS-000019 report manifest-agreement failure despite clean SQLite integrity/foreign keys and no raw hash mismatch. The validator's manifest/count expectations are stale or inconsistent and require later diagnosis.

## 18. Documentation contradictions

1. `docs/DATA_INVENTORY.md` says 24 durable datasets and ends at DS-000024; live manifests prove 25 and DS-000025 exists.
2. `docs/PROJECT_STATUS_REPORT_2026-09-13.md` at `19dd42f` correctly reports the earlier DS-000024 checkpoint but is stale after `a22c8d25`.
3. `docs/DS-000025_CONTINUATION_HANDOFF.md` records pending packaging/registration work that the later completion commit finished.
4. README and `docs/PROJECT_SCOPE.md` open with older “ingestion foundation/not finished system” language while later sections and `AGENTS.md` say V1 intelligence is complete.
5. `docs/Phases.md` says direct V1 work superseded the old sequence while later formal phases remain planned; phase numbering is historical rather than an execution checklist.
6. The AGENTS “V1 complete” statement is materially supported for topic/packaging/hook/script/orchestration, but it must be read with its own qualifiers: editing evidence on one channel, strategy only `GENERALIZED_WORKING`, and first-party real data absent.
7. Central documentation does not contain the original 44-URL target ledger even though the DS-000025 handoff calls for reconstructing it.
8. The funded extraction plan covers DS-000023–25 only; no funded DS-000026 plan exists.

## 19. Security and credential-scan result

Scanned all 454 live tracked files for high-confidence private-key, GitHub PAT, AWS access-key, Slack-token, JWT, and credential-bearing URL patterns. Result: 0 matches in 0 files. A second local scan excluding `.git`, `.venv`, raw evidence, and the new reports also returned 0 files. Remotes were displayed only in redacted/non-credential form. This is a pattern scan, not a formal secret-scanning product guarantee.

## 20. Confirmed facts

- Live DS-000025 completion SHA and both historical checkpoint SHAs are valid.
- Local `main` has no tracked/staged modification and is 11 commits behind, 0 ahead.
- Live and remote-tracking refs match after successful fetch.
- 25 live dataset manifests exist.
- DS-000020–25 totals are 35 packages / 1,601 unique videos / 1,591 real transcripts / 10 placeholders / 14 missing descriptions.
- Package files and IDs reconcile; all packages parse/open and ZIP CRC checks pass.
- Catalog population is 19 datasets / 5 channels / 303 videos / 604 classification rows and is separate from the package population.
- The canonical local SQLite catalog is healthy but stale relative to DS-000020–25.
- Intelligence code/artifacts/tests exist; V2 product infrastructure does not.

## 21. Unresolved uncertainties

- Original normalized 44 URLs and exact ten remaining targets.
- Independent proof that Tp Dossier is outside the original target list.
- Full GitHub ruleset details due plan/API restriction.
- Whether historical absolute source locations still exist on the prior machine/user account.
- Correct intended policy for mutable shared files in historical dataset checksum ledgers.
- Whether DS-000020–25 should ever be ingested into the 303-item catalog; no current contract says so.

## 22. Risks and limitations

- Starting work from this checkout would omit the last six datasets and related code/tests.
- Pulling before reviewing untracked files is avoidable risk, even though no incoming path currently collides with the eight untracked paths.
- Missing original target evidence could cause duplicate or wrong DS-000026 channel selection.
- GitHub has no CI runs and both branches appear unprotected.
- Ordinary Git blobs include large CSV/JSON/XLSX/ZIP files; repository growth will continue without an explicit storage policy.
- The local catalog is reproducible in principle but some OCR/native-AI observations require reruns; it is not a one-command byte-for-byte authority.
- Public metrics and historical cost/balance evidence are point-in-time observations.

## 23. Prioritized recommended next actions

1. Review these uncommitted audit files and the three pre-existing untracked files.
2. In a separate approved operation, fast-forward only: `git pull --ff-only origin main`; then rerun `git status` and SHA checks.
3. Supply or recover the authoritative original 44-URL list; normalize it to canonical channel IDs and create a durable target ledger before choosing DS-000026.
4. Only then prepare a no-run DS-000026 proposal with live public counts, duplicate checks, cost ceiling, and reserve protection.
5. Separately schedule documentation/validator corrections: inventory DS-000025 omission, DS-000025 overlap link, DS-000023 ledger path, mutable shared-ledger policy, DS-000012–16 null-path verifier, and missing pytest environment.

## 24. DS-000026 readiness decision

**Decision: NOT READY.** DS-000025 is present and internally reconciled on live `main`, but this checkout is 11 commits behind and the authoritative 44-target input is missing. DS-000026 must not be launched. Evidence-complete planning can begin only after an approved fast-forward and recovery of the original target list.

Exact next action: review the five audit deliverables, then separately authorize a fast-forward-only pull of `main`; do not select DS-000026 channels until the original 44-URL ledger is supplied or recovered.
