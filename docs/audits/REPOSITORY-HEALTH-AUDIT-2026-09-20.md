# Strict Git Repository Health Audit — 2026-09-20

Scope: fresh, read-only inspection of the working tree at `/Users/ghilmankhan/workprojects/youtube-intelligence-os`, local Git object database, and live `origin` fetched on 2026-09-20 (Asia/Karachi). Historical audits were used only as claims to retest. The only repository write made by this audit is this requested report; all probes were read-only and temporary probe code lived under `/private/tmp`.

## 1. Executive Verdict

**FINAL HEALTH: NEEDS REMEDIATION.** Git objects are structurally healthy and no credential-shaped secret was detected, but checked-out `main` is one commit behind live `origin/main`; eight pre-audit untracked files and 32 ignored files exist; the ignored inventory DB is an invalid zero-byte file; the generated registry DB is absent; DS-000027 is acquired and committed on live `origin/main` but is not integrated into the normalized 69-channel registry or generated intelligence; dependency/runtime declarations are absent; tests cannot run in the current supported checkout because `pytest` and `openpyxl` are unavailable; several primary docs materially understate current implementation and data.

Current truth has two different counts that must not be conflated:

- normalized registry: **69** channels;
- verified repository holdings after DS-000027: **70** canonical channels, of which **41** are data-ready, **36** have standardized packages, and **29** remain identity-only.

## 2. Current Local HEAD

| Field | Value |
|---|---|
| Repository root | `/Users/ghilmankhan/workprojects/youtube-intelligence-os` |
| Git | `git version 2.50.1 (Apple Git-155)` |
| Branch | `main` |
| HEAD | `dcfe2927eee8c9bca11ac03cf21724c59b440b6b` |
| Subject | `docs: preserve DS-000026 preflight handoff` |
| Upstream | `origin/main` |
| Fetch/push URL | `https://github.com/ghilmanITM360/youtube-intelligence-os.git` |

## 3. Live Remote HEAD

`git fetch --all --prune` completed successfully. This is a live verification, not a cached-ref inference.

| Ref | Commit | Subject |
|---|---|---|
| `origin/main` | `25110136c61ac0cc8bb124a1cacd3aa5fae8a840` | `data: add DS-000027 Dr Ares extraction` |

Fetch also confirmed deletion of remote refs `origin/feat/youtube-channel-registry-and-tracker-2026-09-14` and `origin/fix/repository-audit-remediation-2026-09-14`.

## 4. Ahead/Behind/Divergence

`git rev-list --left-right --count HEAD...origin/main` returned `0 1`.

- Local ahead: **0**.
- Local behind: **1**.
- Diverged: **no**.
- Verdict: **LOCAL BEHIND**. Local `main` is not identical to live `origin/main`.

The missing remote commit contains DS-000027 raw evidence, package, combined exports, manifest files, ledger update, and small registry-builder/test changes. A linked local branch, `codex/ds-000027-dr-ares`, already points at the same commit as `origin/main`; no checkout or merge was performed.

## 5. Working Tree

Baseline before this report:

- staged tracked changes: **0**;
- unstaged tracked changes: **0**;
- tracked worktree: **clean**;
- untracked files: **8**;
- ignored files: **32**;
- stashes: **0**.

After creating this requested report, untracked count is **9**. This report is not treated as a pre-existing health defect.

## 6. Untracked Files

| Item | Classification | Git/live-remote relationship |
|---|---|---|
| `CHANNEL-DATA-DEEP-AUDIT.md` | Audit artifact | Local only |
| `CHANNEL-NICHE-SUBNICHE-AUDIT.md` | Audit artifact | Local only |
| `PROJECT-DATA-ARCHITECTURE-REPORT.md` | Audit/report artifact | Local only |
| `PROJECT-DEEP-TECHNICAL-REPORT.md` | Audit/report artifact | Local only |
| `data/manifests/DS-000027_CONFIG.json` | Canonical acquisition metadata | Byte representation is committed on live `origin/main` |
| `data/manifests/DS-000027_PREFLIGHT.json` | Canonical preflight metadata | Committed on live `origin/main` |
| `data/manifests/DS-000027_VIDEO_SAMPLE_VERIFICATION.json` | Canonical verification metadata | Committed on live `origin/main` |
| `docs/audits/DS-000027_DR_ARES_PREFLIGHT_PROPOSAL_2026-09-20.md` | Historical acquisition proposal | Not in live `origin/main` |
| `REPOSITORY-HEALTH-AUDIT-2026-09-20.md` | Requested audit artifact | Created by this audit |

No untracked source-code change exists. Do not delete the DS-000027 proposal or local audit reports without an explicit retention decision.

## 7. Ignored Files

Exactly **32 ignored files** were enumerated:

- `data/catalog/youtube_inventory.db`: 1 zero-byte invalid runtime DB;
- nested DS-000021 and DS-000023 raw copies: 2 exact duplicates of tracked canonical raw JSON;
- DS-000027 ignored acquisition/preflight files: 13 files, approximately 1.1 MiB;
- `outputs/`: 16 files, approximately 15 MiB, including one `.DS_Store`, staging exports, reports, and XLSX inspection output.

The two nested copies were hash-verified exact duplicates:

- DS-000021 pair: SHA-256 `5b4bc03c…` on both paths;
- DS-000023 pair: SHA-256 `50b3f2f1…` on both paths.

DS-000027's live remote commit preserves its immutable actor output and selected evidence, but several local API/preflight response files remain ignored and are not independently present in Git. Their durable necessity must be checked against `DS-000027_SOURCE_ARTIFACTS.csv` and raw checksums before any cleanup.

## 8. Stashes

`git stash list` is empty. **0 stashes**.

## 9. Git Object Integrity

`git fsck --full --strict` reported no corruption, missing objects, or hash mismatch.

| Measure | Result |
|---|---:|
| Corrupt/missing objects | 0 |
| Dangling blobs | 27 |
| Dangling trees | 10 |
| Dangling commits | 0 |
| Loose objects | 781 |
| Loose object size | 68.38 MiB |
| Packed objects | 763 |
| Packs | 1 |
| Pack size | 21.13 MiB |
| Prune-packable | 0 |
| Garbage | 0 |
| Garbage size | 0 bytes |

Dangling blobs/trees are recoverable unreachable objects, not corruption. No destructive prune or GC was run.

## 10. Remote/Branch Health

| Branch/ref | Commit | Upstream | Relation to `origin/main` | Classification |
|---|---|---|---|---|
| `main` | `dcfe292` | `origin/main` | 0 ahead, 1 behind | ACTIVE; update required |
| `codex/ds-000027-dr-ares` | `2511013` | `origin/main` | identical | ACTIVE linked-worktree branch; merged state |
| `origin/main` | `2511013` | — | live default | ACTIVE |
| `origin/ui/v1` | `0412932` | — | 1 unique commit, 24 commits behind; not ancestor of main | DOC-ONLY, STALE CANDIDATE, UNIQUE WORK — KEEP until its audit/handoff document is reviewed |

Former feature/fix remote refs named in the prompt were pruned because the live server reports them deleted. No branch was deleted locally.

## 11. Tags

Tag count: **0**. Important stable states, including V1 completion and dataset milestones, have no immutable release tags. This is traceability debt, not object-integrity damage. No tag was created.

## 12. Repository Size

| Inventory | Files | Logical bytes | Approx. MiB |
|---|---:|---:|---:|
| Local `HEAD` tracked tree | 477 | 169,856,676 | 161.99 |
| Live `origin/main` tracked tree | 502 | 178,327,436 | 170.07 |
| Workspace excluding `.git` | 517 | 193,582,191 | 184.61 |
| `.git` disk usage | — | filesystem-reported | 90 MiB |

Live `origin/main` tracked distribution: 366 files under `data/` totaling 176,491,502 bytes; 64 Python files totaling 1,169,930 bytes; 154 JSON files totaling 73,482,875 bytes; 38 CSV files totaling 63,666,510 bytes; 43 ZIP files totaling 19,951,363 bytes; 51 XLSX files totaling 13,192,335 bytes.

Threshold counts on live `origin/main`: **36** files over 1 MiB, **7** over 5 MiB, **3** over 10 MiB, **0** over 50 MiB.

## 13. Largest Files

Largest tracked files on live `origin/main`:

| Bytes | Path | Assessment |
|---:|---|---|
| 18,189,527 | `data/extracted/channel-data/DS-000025/combined/youtube_3_channels_master.csv` | Required derived combined export; large |
| 12,828,893 | `data/manifests/batches/BATCH-000001_FILES.csv` | Canonical provenance inventory; retain |
| 10,986,392 | `data/extracted/channel-data/DS-000021/combined/youtube_11_channels_master.csv` | Required derived export; large |
| 8,574,739 | `data/extracted/channel-data/DS-000024/combined/youtube_4_channels_master.csv` | Required derived export |
| 7,142,564 | DS-000025 `clean.json` | Exact duplicate of `master.json`; policy candidate |
| 7,142,564 | DS-000025 `master.json` | Derived canonical package representation |
| 6,994,665 | DS-000025 Apify raw JSON | Canonical raw evidence; retain |
| 4,942,355 | DS-000023 combined CSV | Required derived export |
| 4,865,160 | DS-000020 combined CSV | Required derived export |
| 4,690,521 each | DS-000021 `clean.json` and `master.json` | Exact duplicate pair; policy candidate |

Large canonical evidence must not be removed solely for size.

## 14. Git History Bloat

All 30 largest blobs found across all refs are still reachable from current refs; no huge obsolete historical-only blob was found. Largest historical blob is the current 18.19 MB DS-000025 combined CSV. Pack storage is only 21.13 MiB because text compresses well; loose-object storage is larger at 68.38 MiB.

Git LFS is not presently mandatory: no tracked file exceeds 50 MiB. Evaluate LFS or object storage only for future binary growth, with explicit provenance hashes and migration implications. Do not rewrite existing history merely to shrink canonical evidence.

## 15. Dataset Inventory

`DS-000026` is a proposal/handoff reference, not an acquired dataset. `DS-000027` is the latest acquired dataset. “Registry” below means represented in the normalized registry, not merely named in a ledger.

| Dataset | Local raw/evidence | Manifest | Package | Registry | Intelligence | Git tracked on live main | Current status |
|---|---|---|---|---|---|---|---|
| DS-000001 | Historical holding | Yes | N/A | Yes | Yes, channel-linked | Manifest/provenance | Registered historical/channel data |
| DS-000002 | Historical holding | Yes | N/A | Relationship only | Conditional visual | Manifest/provenance | Ingested forensic dataset |
| DS-000003 | Historical holding | Yes | N/A | Subject evidence | No channel assignment | Manifest/provenance | Ingested screenshots |
| DS-000004 | Historical holding | Yes | N/A | Subject evidence | No channel assignment | Manifest/provenance | Ingested screenshots |
| DS-000005 | Historical holding | Yes | N/A | Subject evidence | No channel assignment | Manifest/provenance | Ingested screenshots |
| DS-000006 | Historical holding | Yes | N/A | Subject evidence | No channel assignment | Manifest + snapshot | Ingested screenshots |
| DS-000007 | Historical holding | Yes | N/A | Subject evidence | No channel assignment | Manifest/provenance | Ingested screenshots |
| DS-000008 | Historical holding | Yes | N/A | Subject evidence | No channel assignment | Manifest/provenance | Ingested screenshots |
| DS-000009 | Historical holding | Yes | N/A | Subject evidence | No channel assignment | Manifest/provenance | Ingested screenshots |
| DS-000010 | Historical holding | Yes | N/A | Subject evidence | No channel assignment | Manifest/provenance | Ingested screenshots |
| DS-000011 | Historical raw fixture expected locally | Yes | N/A | Global corpus | Used by visual layer | Manifest/provenance | Ingested global knowledge; ignored fixture dependency |
| DS-000012 | Historical holding | Yes | N/A | CH-000004 relationship | Yes | Manifest/provenance | Ingested forensic dataset |
| DS-000013 | Historical holding | Yes | N/A | CH-000004 relationship | Yes | Manifest/provenance | Ingested forensic dataset |
| DS-000014 | Historical holding | Yes | N/A | CH-000004 relationship | Yes | Manifest/provenance | Ingested forensic dataset |
| DS-000015 | Historical holding | Yes | N/A | CH-000004; revision overlap | Yes | Manifest/provenance | Ingested forensic revision |
| DS-000016 | Historical holding | Yes | N/A | No canonical channel | No channel intelligence | Manifest/provenance | Ingested forensic dataset; unmapped |
| DS-000017 | Historical acquisition | Yes | Historical catalog | Yes | Yes | Manifest + thumbnail snapshot | Registered xkcd acquisition |
| DS-000018 | Historical raw fixture expected locally | Yes | N/A | Global research | Used by tests/reports | Manifest/provenance | Ingested creator-research corpus |
| DS-000019 | Historical supplied export | Yes | Historical catalog | Yes | Yes | Manifest + snapshot | Structured registered channel |
| DS-000020 | Yes | Yes + ledgers | Yes, 5 channels | Yes | Yes | Raw + package + manifest | Complete |
| DS-000021 | Yes; 1 ignored nested duplicate | Yes + ledgers | Yes, 11 channels | Yes | Yes | Raw + package + manifest | Complete; duplicate local copy |
| DS-000022 | Yes | Yes + ledgers | Yes, 7 channels | Yes | Yes | Raw + package + manifest | Complete; intentional raw/package duplication |
| DS-000023 | Yes; 1 ignored nested duplicate | Yes + ledgers | Yes, 5 channels | Yes | Yes | Raw + package + manifest | Complete; duplicate local copy |
| DS-000024 | Yes | Yes + ledgers | Yes, 4 channels | Yes | Yes | Raw + package + manifest | Complete |
| DS-000025 | Yes | Yes + ledgers | Yes, 3 channels | Yes | Yes | Raw + package + manifest | Complete |
| DS-000026 | No acquisition | Proposal only | No | No | No | Handoff document only | **NOT A DATASET; proposed/not run** |
| DS-000027 | Yes, including ignored preflight/API evidence | Yes on live main | Yes, 1 channel / 35 videos | **No** | **No** | Yes on live main | Acquired/package-ready; registry/intelligence integration incomplete |

No `DS-000028+` reference or evidence was found.

## 16. Local-vs-Git Data Drift

Yes, local filesystem contains material not represented by checked-out Git:

1. checked-out `main` lacks the entire live DS-000027 commit;
2. 13 ignored DS-000027 acquisition/preflight files exist locally; only a selected evidence set is committed remotely;
3. four pre-existing local reports and one DS-000027 proposal are untracked;
4. `outputs/` retains 15 MiB of operational staging exports;
5. nested DS-000021/023 raw paths are redundant exact copies, not newer evidence;
6. local inventory DB is not newer data: it is zero bytes and invalid.

Live `origin/main` is ahead of the checkout, but even live main does not contain every local preflight/API response or the normalized Dr Ares registry/intelligence integration.

## 17. Channel Count Truth

| Measure | Current verified count |
|---|---:|
| Registry channels | 69 |
| Additional verified local/live-repo channel | 1 — Dr. Ares Senior, DS-000027 |
| Canonical current total | **70** |
| Identity-only | 29 |
| Data-ready | 41 |
| Package-ready | 36 |
| Generated-intelligence | 69 |

The 69-channel registry controls remain: 35 standard-package, 5 historical-catalog, 29 identity-only; 1,904 videos; 1,893 real transcripts; 11 placeholders. DS-000027 adds 1 channel, 35 videos, and 35 real transcripts, producing current holdings of **70 channels, 1,939 videos, 1,928 real transcripts, 11 placeholders**. Dr. Ares exists in committed live Git package/manifest data but is missing from normalized registry and intelligence outputs.

## 18. SQLite Health

| DB | Exists | Size | Valid | Tables | Tracked | Reproducible/source of truth |
|---|---|---:|---|---|---|---|
| `data/catalog/youtube_inventory.db` | Yes | 0 bytes | **No** | None | Ignored | Intended regenerable catalog, but current file is an invalid placeholder and manifests alone do not prove byte-for-byte reconstruction |
| `data/catalog/youtube_channel_registry.db` | No | — | Not testable | Expected registry schema absent | Ignored | Intended generated view from tracked inputs |

No DB was opened in ordinary create mode. Existing DB inspection used existence/size checks; no absent DB was created.

## 19. Duplicate Files

On live `origin/main`, hash-based inventory found **23 exact-duplicate groups, 52 paths, 24,784,788 duplicate-extra bytes**.

Main classes:

- `clean.json` equals `master.json` exactly for DS-000021, DS-000023, DS-000024, DS-000025, and DS-000027: expected/generated duplicate naming, but versioning policy should justify both;
- six DS-000022 transcript ZIP/workbook package files duplicate raw source artifacts: expected provenance-preserving duplication (raw immutable copy plus standardized package); retain unless package references can safely avoid byte copies;
- actor input copies between preflight and run directories: small expected duplicates;
- `.gitkeep` duplicates: harmless;
- ignored nested DS-000021/023 actor JSON: noncanonical local copies and strongest cleanup candidates after path/hash verification;
- `outputs/` mirrors prior derived exports: noncanonical local staging, but confirm no unique evidence before removal.

## 20. Generated Artifact Policy

| Artifact | Currently tracked? | Deterministic/reconstructable? | Policy finding |
|---|---|---|---|
| SQLite runtime DBs | No | Intended yes | Correctly ignored; zero-byte DB is junk, absent registry DB blocks local queries |
| Master tracker XLSX | Yes | Builder exists, external Node module required | Versioning justified as user-facing artifact; rebuild not clean-clone reproducible |
| Combined CSV/JSON/XLSX | Yes | Packaging scripts exist, dependencies undeclared | Useful durable delivery artifacts; exact JSON duplicates need explicit rationale |
| Intelligence JSON/MD | Yes | Generated from evidence and heuristics | Versioning justified for review, provenance, and model-output stability |
| Raw evidence | Selectively yes | No; canonical source bytes | Must retain |
| Render/QA/staging under `outputs/` | No | Usually yes | Correctly ignored; verify uniqueness before cleanup |
| Audit reports | Mixed | Human/agent analysis | Keep historical reports when cited; local new reports need explicit commit/archive decision |

## 21. Legacy / Extra Files

| Item | Why it looks extra | Still referenced? | Historical value | Safe cleanup candidate? |
|---|---|---|---|---|
| ignored nested DS-000021/023 JSON | Exact duplicate under repeated `apify/<run>/apify/<run>/` | No canonical path need found | Low | Yes, after explicit approval |
| `outputs/.DS_Store` | OS metadata | No | None | Yes |
| other `outputs/` tree | Operational staging duplicates committed packages | Some handoff/audit references possible | Medium | Conditional, not blanket-safe |
| zero-byte `youtube_inventory.db` | Invalid generated DB | Path is documented | None as data | Yes, but deletion not performed |
| pilot intelligence artifacts | Superseded naming/older run | May be cited by docs/tests | High audit lineage | No blanket removal |
| old dataset-specific scripts | Narrow scope | Tests/docs/callers exist | Medium/high | No, until call-site deprecation audit |
| historical audits/handoffs | Date-stamped and superseded | Frequently cross-referenced | High | Keep |
| `origin/ui/v1` unique doc commit | Old and 24 commits behind | Unique commit remains | Unknown until reviewed | Not yet |

## 22. Dependency Health

No `requirements.txt`, `requirements-dev.txt`, `pyproject.toml`, lockfile, `Pipfile`, `package.json`, Node lockfile, `.python-version`, or `.nvmrc` exists.

Observed external dependencies include:

- Python: `openpyxl`, Pillow (`PIL`), macOS `AppKit`/`Foundation`/`Vision`, and formerly/currently `pytest` as runner;
- Node: `@oai/artifact-tool` for workbook/package builders;
- platform tools documented elsewhere: macOS frameworks and optional external utilities.

Current system reports Python **3.9.6** and Node **v24.14.0**, but repository does not declare supported versions or exact packages. `pytest` command is absent, `python3 -m pytest` fails with `No module named pytest`, and current Python also lacks the previously documented workbook environment. A clean clone cannot discover exact runtime dependencies from machine-readable repository metadata.

## 23. Clean Clone Reproducibility

**NOT REPRODUCIBLE** as a complete current system.

A clean clone receives tracked scripts, manifests, selected raw evidence, packages, registry JSON/XLSX, and intelligence artifacts. It cannot reliably recreate the same operational state because:

- runtime versions and third-party packages are undeclared/unlocked;
- ignored historical raw fixtures and runtime SQLite catalog are absent;
- registry DB is generated but no ready environment exists;
- local-only DS-000027 preflight/API evidence and audit artifacts are absent;
- setup instructions rely on a “bundled workspace” runtime not defined by repository metadata;
- some docs contain absolute historical `/Users/...` source paths (valid provenance, not portable input paths);
- workbook regeneration depends on external `@oai/artifact-tool` availability;
- current normalized registry is stale relative to DS-000027.

## 24. Test Health

Attempted in current checkout without installing anything:

```text
pytest -q
zsh:1: command not found: pytest

python3 -m pytest -q
/Library/Developer/CommandLineTools/usr/bin/python3: No module named pytest
```

Classification:

- assertion failures: **0 observed; tests never started**;
- environment failures: **test runner unavailable**;
- missing dependency failures: **pytest missing; openpyxl also unavailable per current DS-000027 preflight and environment checks**;
- missing data failures: **not reached**, but ignored DS-000011/DS-000018/catalog fixtures are documented dependencies for some tests.

Historical claim “341 passed” cannot be reproduced in this environment. It remains a dated historical result, not current test truth.

## 25. CI / Quality Gates

No GitHub Actions, GitLab CI, Jenkins, CircleCI, pre-commit configuration, coverage configuration, dependency scanner, or automated secret scanner is tracked. `pytest.ini` exists but contains only pytest configuration. Tests and validator scripts exist; no machine-enforced clean-clone gate installs dependencies and runs them. Formatting, linting, static typing, coverage thresholds, and security scanning are undeclared.

## 26. Secrets & Security

A value-safe current-tree and all-reachable-history scan checked private-key blocks, Apify token value shapes, GitHub tokens, AWS access keys, Google API keys, and credential-like assignments. **No secret value was detected.** No `.env`, PEM/key, credential JSON, cookie file, or service-account file was found in the working tree or named in history.

| Type | Path/commit | Status | Severity |
|---|---|---|---|
| `APIFY_TOKEN` | Code/docs references only | Environment-variable contract; no value found | None |
| Private/API credentials | Current tree and reachable Git history | No value-shaped match | None |
| Authenticated API response metadata | Ignored DS-000027 local evidence | No token-shaped value found; still potentially sensitive operational metadata | Low; retain privately/review before sharing |

GitHub-hosted secret-scanning results were not available through local Git, so comparison is **CANNOT VERIFY**.

## 27. Documentation Drift

| Document | Classification | Evidence |
|---|---|---|
| `README.md` | **OUTDATED / CONTRADICTORY** | Says repository is not finished product, describes V1 as pilots for five channels, claims operational payload is not in repository; live tree contains substantial tracked raw/package/intelligence data and generalized V1 |
| `AGENTS.md` | **PARTIALLY OUTDATED** | Correct V1 boundaries; “all canonical channels” now conflicts with unintegrated 70th channel DS-000027 |
| `docs/Architecture.md` | **PARTIALLY OUTDATED** | Calls most intelligence planned and assumes populated local catalog, while catalog is zero-byte and V1 exists |
| `docs/Database.md` | **CURRENT as conceptual design; operational note stale** | Correctly distinguishes final DB from local SQLite, but current local DB is invalid |
| `docs/Phases.md` | **PARTIALLY OUTDATED** | Roadmap labels lag current generalized V1 state |
| `docs/PROJECT_SCOPE.md` | **OUTDATED** | Still reports 604 classifications, 303 items, five canonical channels/pilots |
| `docs/PROJECT_STATUS_REPORT_2026-09-13.md` | **HISTORICAL — KEEP** | Correct for date, superseded by DS-000025/027 and later tests |
| `docs/Error_Handling.md` | **PARTIALLY OUTDATED** | Says error classes are not implemented; scripts now implement concrete validation/error behavior |
| `docs/YOUTUBE_CHANNEL_REGISTRY.md` | **OUTDATED** | 69 channels/25 datasets/1,904 videos omit DS-000027 and 70th channel |
| dated audit/handoff docs | **HISTORICAL — KEEP** | Preserve evidence of point-in-time claims; do not treat as current truth |

## 28. `.gitignore` Health

Coverage is good for OS/editor files, secrets, venvs, caches/temp files, logs, raw-data safety defaults, `outputs/`, SQLite runtime files, private first-party analytics, and transient batch state.

Findings:

- canonical raw evidence is intentionally ignored by default and selectively unignored dataset-by-dataset; this protects accidental staging but creates risk of locally acquired evidence never entering Git;
- DS-000027 live commit succeeded through explicit force/add policy, but no DS-000027 unignore stanza exists; future additions under that dataset remain silently ignored;
- generated `outputs/` is correctly ignored;
- SQLite DBs are correctly ignored, but ignore policy hides the zero-byte invalid DB from normal status;
- generated junk already tracked remains tracked regardless of ignore rules;
- no broad canonical-data ignore should be removed without provenance-safe review.

## 29. Safe Cleanup Candidates

No cleanup was performed. Strong candidates, subject to explicit authorization:

1. `outputs/.DS_Store` — no value;
2. zero-byte ignored `data/catalog/youtube_inventory.db` — invalid, contains no data;
3. two ignored nested DS-000021/023 JSON copies — exact hash duplicates of tracked canonical paths;
4. `outputs/` staging exports whose hashes/content are confirmed represented in canonical raw/extracted paths;
5. selected untracked audit reports only after deciding whether to commit, archive externally, or discard.

“Safe cleanup candidates” count in final summary is **3 unconditional file-level candidates plus 2 conditional groups**.

## 30. Items That Must NOT Be Deleted

- canonical raw evidence and its checksums;
- manifests, source-artifact ledgers, package-validation reports, and provenance inventories;
- DS-000027 local-only evidence until representation/retention is explicitly resolved;
- DS-000022 raw/package duplicate pairs: duplication preserves source versus standardized package lineage;
- intelligence outputs needed for reproducible review;
- historical audits, handoffs, and pilot artifacts still cited by docs/tests;
- `origin/ui/v1` until its one unique commit is reviewed;
- dangling objects solely because `fsck` calls them dangling; they are not corruption.

## 31. Required Fixes

Prioritized by correctness and reproducibility:

1. Safely update local `main` to live `origin/main` after deciding how to preserve the nine untracked files; no divergence exists.
2. Integrate DS-000027/Dr. Ares into normalized registry, tracker, counts, intelligence coverage, and current docs; registry must become 70 or explicitly exclude it with a documented rule.
3. Add machine-readable Python/Node runtime and dependency declarations with pinned/compatible versions; document one supported clean setup.
4. Add CI that creates the supported environment and runs validators/tests; distinguish missing fixtures from assertions.
5. Repair/regenerate the ignored inventory DB from authoritative evidence in a controlled environment, generate registry DB, and document whether byte-identical or semantic reconstruction is promised.
6. Reconcile primary docs with generalized V1, tracked payload reality, DS-000027, and current dataset/channel counts.
7. Decide explicit versioning policy for exact derived duplicates (`clean.json`/`master.json`) and large combined exports; preserve raw provenance.
8. Add value-safe automated secret scanning and dependency scanning.
9. Resolve tracker cached hyperlink errors: direct OOXML recheck found **1,090 `HYPERLINK()` formulas and 1,090 cached error cells**, with no `calcPr`; issue is still present.

## 32. Final Verification Checklist

| Check | Result |
|---|---|
| Live remote fetched | PASS |
| Local equals live main | FAIL — behind 1 |
| Tracked changes/staged files | PASS — none |
| Untracked/ignored fully enumerated | PASS |
| Dataset IDs through highest acquisition checked | PASS — DS-000027 latest; DS-000026 proposal only; no DS-000028+ |
| Channel count reconciled | PASS — registry 69, actual canonical 70 |
| Git object integrity | PASS — no corruption |
| Branch/tag audit | PASS |
| Current/history large blobs inspected | PASS |
| Exact tracked duplicates hashed | PASS |
| SQLite opened safely | PASS — no absent DB created |
| Dependencies declared | FAIL |
| Tests execute in current environment | FAIL |
| CI exists | FAIL |
| Secret-shaped values detected | PASS — none detected |
| Docs aligned | FAIL |
| Clean clone reproduces current system | FAIL |

### Previous-claim cross-check

| Historical claim | Current result |
|---|---|
| 477 tracked files | **CHANGED** — local HEAD still 477; live main is 502 |
| ~170 MB tracked size | **STILL TRUE** — live main 178,327,436 bytes / 170.07 MiB |
| 69 vs 70 channels | **RESOLVED** — registry 69; verified holdings 70 after DS-000027 |
| DS-000027 state | **CHANGED** — acquired/package committed live; registry/intelligence still incomplete |
| zero-byte historical DB | **STILL TRUE** — `youtube_inventory.db` is 0 bytes |
| absent registry DB | **STILL TRUE** |
| missing dependency manifests | **STILL TRUE** |
| 341 historical tests | **CANNOT VERIFY** — current environment lacks pytest |
| stale remote branches | **CHANGED** — feature/fix refs pruned; `origin/ui/v1` remains stale with one unique doc commit |
| duplicate nested raw artifacts | **STILL TRUE** — two ignored exact copies |
| tracker cached hyperlink errors | **STILL TRUE** — 1,090 formulas / 1,090 cached errors |
| documentation drift | **STILL TRUE** |

```text
REPOSITORY HEALTH AUDIT COMPLETE

Local branch: main
Local HEAD: dcfe2927eee8c9bca11ac03cf21724c59b440b6b
Live origin/main: 25110136c61ac0cc8bb124a1cacd3aa5fae8a840
Ahead: 0
Behind: 1
Tracked worktree clean: YES
Untracked files: 9 (8 before this requested report)
Ignored files: 32
Stashes: 0
Git object corruption: NONE
Tracked files: 477 local HEAD; 502 live origin/main
Tracked size: 169,856,676 bytes local; 178,327,436 bytes live
Canonical channels: 70 (registry currently 69)
Latest dataset: DS-000027
Local data missing from Git: YES
Generated DB status: inventory DB zero-byte/invalid; registry DB absent
Tests reproducible: NO
Clean clone reproducible: NO
Secrets detected: NONE by value-safe current-tree/history scan
Stale branch candidates: 1 (origin/ui/v1; unique doc commit requires review)
Safe cleanup candidates: 3 unconditional files + 2 conditional groups

FINAL HEALTH:
NEEDS REMEDIATION

TOP REMEDIATIONS:
1. Update local main to live origin/main after preserving untracked work.
2. Integrate DS-000027 and channel 70 into registry, tracker, intelligence, and docs.
3. Declare and pin supported runtimes/dependencies.
4. Add clean-environment CI and restore reproducible tests/databases.
5. Resolve documentation drift, duplicate-derived policy, and tracker cached hyperlink errors.
```
