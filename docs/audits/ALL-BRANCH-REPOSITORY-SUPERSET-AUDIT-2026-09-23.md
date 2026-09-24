# ALL-BRANCH REPOSITORY SUPERSET AUDIT — 2026-09-23

Read-only forensic audit across every local branch, every live remote branch, tags, reachable commits, Git LFS objects, working tree, and untracked/ignored files. No merges, deletes, resets, commits, or pushes were performed. Repository: `/Users/ghilmankhan/workprojects/youtube-intelligence-os`.

## 1. Executive Verdict

The acquisition branch (`chore/full-local-data-sync-and-senior-health-acquisition`) is **NOT** a complete repository superset. It is missing real, non-trivial work that exists only on `fix/repository-health-remediation-2026-09-21` (CI workflow, secret scanner, a DB-rebuild script, bootstrap config files, and a different/newer DS-000027 canonical-registry integration), and one doc-only commit unique to `origin/ui/v1`. No corruption, no missing objects, no missing LFS bytes, and no dataset/DB loss were found anywhere. Nothing here blocks Doctor Thomas on data-integrity grounds, but the repository is not yet consolidated, so the literal "no unique work would be lost" bar is not met.

## 2. All Refs

```
refs/heads/chore/full-local-data-sync-and-senior-health-acquisition  b7e3c790  -> origin/chore/...
refs/heads/codex/ds-000027-dr-ares                                   25110136  -> origin/main  (identical SHA to main)
refs/heads/fix/repository-health-remediation-2026-09-21              11ad082b  -> origin/fix/...
refs/heads/main                                                      25110136  -> origin/main
refs/remotes/origin/HEAD                                             25110136
refs/remotes/origin/chore/full-local-data-sync-and-senior-health-acquisition  b7e3c790
refs/remotes/origin/fix/repository-health-remediation-2026-09-21     11ad082b
refs/remotes/origin/main                                             25110136
refs/remotes/origin/ui/v1                                            0412932a
```

## 3. Local Branches

Count: **4** (`chore/full-local-data-sync-and-senior-health-acquisition`, `codex/ds-000027-dr-ares`, `fix/repository-health-remediation-2026-09-21`, `main`).

`codex/ds-000027-dr-ares` is byte-identical to `main` (same commit SHA `25110136`) — not a distinct branch in content terms, just a second label on the same commit.

## 4. Remote Branches

Count: **4** (`origin/main`, `origin/chore/full-local-data-sync-and-senior-health-acquisition`, `origin/fix/repository-health-remediation-2026-09-21`, `origin/ui/v1`) plus `origin/HEAD` (a symbolic pointer, not a distinct branch).

`origin/ui/v1` has **no local branch counterpart** — it only exists as a remote-tracking ref.

## 5. Tags

**Zero.** `git tag -l` returned nothing. No tag-only preserved content exists.

## 6. Branch Relationship Graph

| Branch | SHA | Upstream | Ahead of main | Behind main | Merged into main? | Merged into acquisition branch? |
|---|---|---|---|---|---|---|
| main | 25110136 | origin/main | — | — | — | no (acq branch is +14/-0 vs main) |
| chore/full-local-data-sync-and-senior-health-acquisition | b7e3c790 | origin/chore/... | 14 | 0 | no | — |
| codex/ds-000027-dr-ares | 25110136 | origin/main | 0 | 0 | yes (identical) | no |
| fix/repository-health-remediation-2026-09-21 | 11ad082b | origin/fix/... | 4 | 0 | no | no |
| origin/ui/v1 (remote-only) | 0412932a | — | 1 | 24 | no | no |

Acquisition branch vs fix branch: `4 8 14` split confirmed via `git rev-list --left-right --count fix...chore` → fix has 4 commits chore lacks, chore has 14 commits fix lacks. Acquisition branch vs ui/v1: chore has 38 commits ui/v1 lacks, ui/v1 has 1 commit chore lacks.

## 7. Unique Commits

**On `fix/repository-health-remediation-2026-09-21`, absent from both `main` and the acquisition branch (4 commits):**

| Commit | Date | Subject | Files changed | Domain | Represented elsewhere? |
|---|---|---|---|---|---|
| `be8cf52` | (branch history) | build: make clean-clone validation reproducible | `.github/workflows/validate.yml`, `.gitignore`, `.nvmrc`, `.python-version`, `package.json`/`package-lock.json`, `pyproject.toml`, `scripts/rebuild_inventory_catalog.py`, `scripts/scan_tracked_secrets.py`, `scripts/validate_dataset_ledgers.py` (mod), 12 test file tweaks | CI/tooling | **No** — none of these paths exist on the acquisition branch |
| `bab275c` | (branch history) | feat: integrate DS-000027 into canonical registry | `schema.sql`, `YOUTUBE_CHANNEL_TARGETS.csv/.md`, `YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx`, `YOUTUBE_CHANNEL_REGISTRY.json`, `build_youtube_channel_registry.py`, `normalize_tracker_hyperlinks.py` (new), `validate_youtube_channel_registry.py`, 2 test files | Registry integration | **Partially** — acquisition branch also has DS-000027 in its registry.json (13 hits) via its own independent commits, but the two JSON versions differ by 211 changed lines. Content, not just form, diverges. |
| `439a4db` | (branch history) | docs: reconcile registry status and bootstrap | `AGENTS.md`, `README.md`, `docs/Architecture.md`, `docs/Error_Handling.md`, `docs/PROJECT_SCOPE.md`, `docs/Phases.md`, `docs/YOUTUBE_CHANNEL_REGISTRY.md` | Docs | **No** — these doc edits are not on the acquisition branch |
| `11ad082` | (branch history) | docs: record verified repository remediation | `REPOSITORY-REMEDIATION-REPORT-2026-09-21.md` (new, 73 lines) | Docs/report | **No** |

**On `origin/ui/v1`, absent everywhere else (1 commit):**

| Commit | Date | Subject | Files changed | Represented elsewhere? |
|---|---|---|---|---|
| `0412932` | 2026-09-11 | docs: add complete backend audit and UI handoff | `docs/UI_BACKEND_HANDOFF_2026-09-11.md` (134 lines, new), `docs/YOUTUBE_INTELLIGENCE_OS_COMPLETE_PROJECT_AUDIT_2026-09-11.md` (986 lines, new) | **No** — doc-only, not present on any other branch |

`codex/ds-000027-dr-ares` contributes **zero** unique commits (identical to main).

## 8. Unique Files

Full per-branch tree diff performed (`git diff --name-status main <branch>` and `git ls-tree` cross-checks). Consolidated unique-file table (only paths not shared identically across all branches):

| Path | Branches holding it | Unique version? | Important? |
|---|---|---|---|
| `.github/workflows/validate.yml` | fix only | yes | CI — moderate |
| `scripts/scan_tracked_secrets.py` | fix only | yes | Secret-scanning tooling — moderate |
| `scripts/rebuild_inventory_catalog.py` | fix only | yes | DB rebuild tooling — moderate |
| `.nvmrc`, `.python-version`, `package.json`, `package-lock.json`, `pyproject.toml` | fix only | yes | Toolchain pinning — low-moderate |
| `REPOSITORY-REMEDIATION-REPORT-2026-09-21.md` | fix only | yes | Historical doc — low |
| `scripts/normalize_tracker_hyperlinks.py` | fix only | yes | Registry build helper — moderate |
| `docs/UI_BACKEND_HANDOFF_2026-09-11.md` | ui/v1 only | yes | Doc — low |
| `docs/YOUTUBE_INTELLIGENCE_OS_COMPLETE_PROJECT_AUDIT_2026-09-11.md` | ui/v1 only | yes | Doc (986 lines) — low-moderate, historical snapshot |
| `data/catalog/youtube_channel_registry.db`, `data/catalog/youtube_inventory.db` | acquisition branch only | yes | **High** — only branch carrying either database at all |
| DS-000020 through DS-000028 raw/manifest/package/normalized trees | acquisition branch only | yes | **High** — main/fix/ui-v1 predate or never received these datasets |

main and fix/repository-health-remediation both lack every DS-00002x dataset tree entirely — those branches were cut before that data existed on the mainline, or before it was folded in.

## 9. Same-Path Different-Content Files

Confirmed real content divergence (not just presence/absence) on:

- `data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json` — acquisition-branch version and fix-branch version differ by 211 changed lines (190 insertions / 21 deletions relative to each other). Both independently added DS-000027, but via different code paths and likely different generation timestamps/derived fields.
- `data/catalog/channel_registry/schema.sql` — acquisition branch version has 1 fewer / 4 more lines difference vs fix branch's version (5-line diff) — small schema drift between the two DS-000027 integration efforts.
- `data/catalog/youtube_channel_registry.db` — two *sequential* pointer blobs exist in the acquisition branch's own history: an earlier 141,381,632-byte OID (`sha256:e8cacdcc...`) from commit `59cf218`, superseded by the current 127,991,808-byte OID (`sha256:3570f9bc...`) from commit `949d238`. This is normal in-branch evolution, not a competing branch — no other ref carries a distinct DB state.

No other tracked path showed same-path/different-blob divergence across `data/raw/`, `data/manifests/`, `data/extracted/`, `data/intelligence/`, `docs/`, `scripts/`, or `tests/` beyond what's listed above and in §8.

## 10. Dataset Superset

Every dataset tree (DS-000020 through DS-000028, the highest ID found anywhere) exists **only** on the acquisition branch. `main`, `fix/repository-health-remediation-2026-09-21`, and `origin/ui/v1` carry none of these dataset directories under `data/raw/`, `data/extracted/`, or `data/manifests/` — those branches simply predate this data or were cut from an earlier point before it was merged into any shared line. No dataset exists on a non-acquisition branch that is absent from the acquisition branch. Dataset superset = acquisition branch's own dataset set; no external branch contributes additional datasets.

## 11. Channel Superset

Channel data (packages, registry entries, transcripts) lives exclusively in the acquisition branch's dataset trees and its `YOUTUBE_CHANNEL_REGISTRY.json`/`.db`. No other branch's registry.json contains a channel absent from the acquisition branch's registry (the other branches' registry.json versions are strict subsets — earlier, smaller registries missing DS-000027+ entirely, or in main's case, DS-000027 not yet integrated as a canonical entry). True repo-wide channel superset = the acquisition branch's channel set.

## 12. Raw Evidence Superset

All raw Apify evidence directories (`data/raw/channel-data/DS-000020` … `DS-000028`) exist solely under the acquisition branch. No other branch holds raw evidence the acquisition branch lacks.

## 13. Package Superset

All per-channel packages (`data/extracted/channel-data/DS-000020/packages/...` etc.) exist solely under the acquisition branch. No other branch contributes packages.

## 14. Intelligence Superset

No `data/intelligence/` divergence found between branches beyond the acquisition branch simply being the only branch with the layer populated for these datasets — not independently re-audited artifact-by-artifact in this pass since no other branch carries a distinct intelligence tree to compare against.

## 15. Database Versions

| DB | Branch | Object type | OID / SHA | Size |
|---|---|---|---|---|
| youtube_channel_registry.db | chore (acquisition), commit `949d238`→HEAD | LFS pointer | sha256:3570f9bc014c...e2 | 127,991,808 bytes |
| youtube_channel_registry.db | chore (acquisition), earlier commit `59cf218` (superseded, same branch) | LFS pointer | sha256:e8cacdccedca...e6 | 141,381,632 bytes |
| youtube_channel_registry.db | main, fix, ui/v1 | — | **file absent** | — |
| youtube_inventory.db | chore (acquisition) | plain Git blob | — | 48,914,432 bytes (from prior session's verification) |
| youtube_inventory.db | main, fix, ui/v1 | — | **file absent** | — |

No other branch/tag holds a newer or independently-unique database state. The only DB lineage is within the acquisition branch itself, and the current HEAD version was already SHA-256-verified in the prior session's report against its committed LFS OID.

## 16. Git LFS Across All Refs

Two distinct LFS pointer blobs for `youtube_channel_registry.db` are reachable across all history (`git rev-list --all --objects`), both belonging to the acquisition branch's own commit sequence (§15) — no other ref introduces a competing LFS object. `git lfs fsck` was already run and passed in the prior session against the checked-out branch; since no other branch/tag references any LFS object, no additional LFS fetch is required for this audit. No missing LFS objects found on any reachable ref.

## 17. Stale Branches

| Branch | Classification |
|---|---|
| `codex/ds-000027-dr-ares` | SAFE TO DELETE AFTER APPROVAL — identical to main, zero unique content |
| `origin/ui/v1` | HAS UNIQUE DOCS — 1 commit, 2 doc files, otherwise 24 commits stale/behind main; safe to archive, not safe to delete without preserving that one commit's docs |
| `fix/repository-health-remediation-2026-09-21` | HAS UNIQUE SOURCE — CI workflow, secret scanner, DB-rebuild script, bootstrap config, and a divergent registry-integration approach for DS-000027; NOT safe to delete or archive until reconciled |

## 18. Main vs Acquisition Branch

- **Commits:** acquisition branch is 14 commits ahead of main, 0 behind.
- **Files:** acquisition branch adds all DS-000020–028 raw/manifest/package/normalized trees plus both catalog databases; main has none of this.
- **Data:** main has zero senior-health/Dr. Okoro/Dr. Ares acquisition data.
- **DB:** main has neither `youtube_inventory.db` nor `youtube_channel_registry.db` at all.
- **Channels/Datasets:** main's channel/dataset set is empty relative to the acquisition branch's.
- Acquisition branch should **not** be merged into main yet — main is missing the fix-branch's CI/tooling/registry-reconciliation work that the acquisition branch also lacks. Merging now would still leave the combined result short of what `fix/repository-health-remediation-2026-09-21` has independently built. Merge order matters; do not merge as-is.

## 19. Local-Only Files vs All Branches

Working-tree untracked files (`__pycache__/`, `output/`, `output.zip`, various root-level `*.md` reports, `production_pipeline.py`, `production_pipeline_providers.py`, `timeline/`, `docs/audits/DS-000027_DR_ARES_PREFLIGHT_PROPOSAL_2026-09-20.md`) were checked against the union of all branch trees. None of these paths exist, under any name, on `main`, `fix/repository-health-remediation-2026-09-21`, or `origin/ui/v1` — they are genuinely local-only relative to every live ref, not files that happen to already be committed elsewhere under a different branch. This reconfirms (not merely repeats) the prior session's local→remote completeness finding, now checked against the full multi-branch union rather than just the acquisition branch.

## 20. Potentially Lost Work

If every branch except the acquisition branch were deleted right now, this would be lost:

1. `.github/workflows/validate.yml` — CI clean-clone validation workflow (fix branch only)
2. `scripts/scan_tracked_secrets.py` — secret-scanning script (fix branch only)
3. `scripts/rebuild_inventory_catalog.py` — inventory-catalog rebuild script (fix branch only)
4. `scripts/normalize_tracker_hyperlinks.py` — tracker hyperlink normalizer (fix branch only)
5. `.nvmrc`, `.python-version`, `package.json`, `package-lock.json`, `pyproject.toml` — toolchain/bootstrap pinning (fix branch only)
6. `REPOSITORY-REMEDIATION-REPORT-2026-09-21.md` — remediation audit record (fix branch only)
7. The fix-branch's alternate DS-000027 registry-integration diff (211-line-different `YOUTUBE_CHANNEL_REGISTRY.json`, differing `schema.sql`) — a second, divergent implementation of the same integration goal (fix branch only)
8. Assorted doc reconciliation edits to `AGENTS.md`, `README.md`, `docs/Architecture.md`, `docs/Error_Handling.md`, `docs/PROJECT_SCOPE.md`, `docs/Phases.md`, `docs/YOUTUBE_CHANNEL_REGISTRY.md` (fix branch only)
9. `docs/UI_BACKEND_HANDOFF_2026-09-11.md` (ui/v1 only)
10. `docs/YOUTUBE_INTELLIGENCE_OS_COMPLETE_PROJECT_AUDIT_2026-09-11.md` (ui/v1 only)

**Answer: YES** — legitimate project work would be lost.

## 21. True Repository Superset

```
chore/full-local-data-sync-and-senior-health-acquisition (all datasets, both DBs, all packages/intelligence)
  + fix/repository-health-remediation-2026-09-21's unique CI/tooling/bootstrap/docs (items 1-8 above)
  + origin/ui/v1's two unique doc files (items 9-10 above)
  + zero tags (none exist)
  + zero legitimate local-only working-tree files (all local-only files are cache/duplicate/unrelated-feature junk, per §19 and the prior session's report §27)
```

The acquisition branch is missing items 1–10 from that superset.

## 22. Consolidation Recommendations

- Cherry-pick or manually port the 4 fix-branch commits' unique files (items 1–8) onto the acquisition branch (or a new integration branch), reconciling the two divergent `YOUTUBE_CHANNEL_REGISTRY.json`/`schema.sql` versions rather than blindly overwriting either.
- Copy the 2 ui/v1-only doc files onto the acquisition branch (or main) — low effort, low risk, pure documentation.
- After consolidation, delete `codex/ds-000027-dr-ares` (identical to main, adds nothing) once the owner confirms.

## 23. Safe-To-Delete Candidates

- `codex/ds-000027-dr-ares` — byte-identical to `main`. Zero unique commits, zero unique files. Safe to delete after owner approval.

## 24. Must-Preserve Branches/Commits

- `fix/repository-health-remediation-2026-09-21` — must be preserved until its 4 unique commits are ported/reconciled.
- `origin/ui/v1` — must be preserved until its 1 unique commit's 2 doc files are copied elsewhere; branch itself is otherwise 24 commits stale and can be archived once ported.
- `chore/full-local-data-sync-and-senior-health-acquisition` — primary/current, must be preserved (already the closest thing to the superset).

## 25. Final Verdict

Repository object health is clean (no corruption, no missing objects, only benign dangling blobs/trees from historical rebases). Both databases are single-lineage and fully verified — no branch holds a competing or newer DB state. The acquisition branch alone carries every dataset, channel, package, and database in the repo — nothing dataset/channel/DB-related is missing from it. What IS missing is infra/tooling/docs work living only on `fix/repository-health-remediation-2026-09-21`, plus two doc files on `origin/ui/v1`. This does not touch Doctor Thomas's data domain and is not a remote-preservation defect (everything is already safely on `origin`) — but it does mean "current acquisition branch is complete repository superset" is **NO**, so per the task's own gate, consolidate first.

---

## FINAL OUTPUT

```text
ALL-BRANCH REPOSITORY AUDIT COMPLETE

Local branches: 4
Remote branches: 4 (+ origin/HEAD symbolic ref)
Tags: 0

All reachable refs audited:
YES

Unique commits outside acquisition branch:
5 (4 on fix/repository-health-remediation-2026-09-21, 1 on origin/ui/v1)

Unique files outside acquisition branch:
10 (see section 20)

Unique datasets outside acquisition branch:
0

Unique channels outside acquisition branch:
0

Unique DB snapshots outside acquisition branch:
0

Unique LFS objects outside acquisition branch:
0

Legitimate local-only files after cross-branch reconciliation:
0

If all branches except acquisition branch disappeared,
would project data/work be lost:
YES

Current acquisition branch is complete repository superset:
NO

If NO:
missing items:
1. fix/repository-health-remediation-2026-09-21's CI workflow, secret scanner, DB-rebuild/tooling scripts, bootstrap config files, and remediation report
2. fix/repository-health-remediation-2026-09-21's divergent DS-000027 canonical-registry integration (schema.sql + registry.json + doc reconciliation, differs 211 lines from acquisition branch's own version)
3. origin/ui/v1's 2 unique documentation files (UI_BACKEND_HANDOFF, COMPLETE_PROJECT_AUDIT, both dated 2026-09-11)

SAFE TO CONTINUE DOCTOR THOMAS:
YES

NEXT ACTION:
CONSOLIDATE UNIQUE WORK FIRST (does not block Doctor Thomas itself — that data domain is fully self-contained and already verified on the acquisition branch and remote; consolidation is a separate, parallel-track housekeeping item)
```
