# DS-000022 Lucas Grant Transcript Corrective Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Independently verify DS-000021/DS-000022 Git state, investigate ten Lucas Grant transcript placeholders, recover only supported data through targeted Apify inputs, update affected derived artifacts, validate, commit, push, and verify `origin/main`.

**Architecture:** Keep supplied DS-000022 source artifacts immutable. Store any new Apify run output in a run-specific raw directory, merge recovered values into the canonical Lucas Grant workbook and transcript ZIP by video ID, and update manifest/checksum evidence from final files. Preserve all other channel packages byte-for-byte.

**Tech Stack:** Git, Python 3, `openpyxl`, ZIP/JSON/CSV standard libraries, browser automation, Apify `streamers/youtube-scraper`.

**Spec:** User request dated 2026-09-13 in this task.

## Global Constraints

- Work in `/Users/ghilmankhan/workprojects/youtube-intelligence-os` on authorized `main`.
- Never modify immutable raw source evidence.
- Scrape only ten affected Lucas Grant video URLs.
- Never persist credentials, cookies, signed download URLs, or Apify tokens.
- Keep 95 Lucas Grant rows and 732 unique DS-000022 video IDs.
- Push only scoped, validated changes; never force-push.

---

### Task 1: Git and repository audit

**Files:**
- Inspect: Git index, history, remote refs, DS-000020, DS-000021, DS-000022 paths

**Interfaces:**
- Consumes: repository HEAD and `origin/main`
- Produces: recorded before-state SHA and scoped-diff evidence

- [ ] Run required status, diff, log, and remote-SHA commands.
- [ ] Prove whether worktree edits exist or UI history alone reported edits.
- [ ] Compare DS-000020 and DS-000021 content with their original commits.
- [ ] Reconcile DS-000022 manifest paths with physical, tracked, and remote files.

### Task 2: Placeholder and prior-evidence investigation

**Files:**
- Inspect: `data/extracted/channel-data/DS-000022/packages/lucas-grant/LucasGrant_Master_Data.xlsx`
- Inspect: `data/extracted/channel-data/DS-000022/packages/lucas-grant/LucasGrant_Transcripts_95_Videos.zip`
- Inspect: `data/extracted/channel-data/DS-000022/DS-000022_PACKAGE_VALIDATION_REPORT.md`
- Inspect: `data/manifests/DS-000022.md`

**Interfaces:**
- Consumes: workbook rows, transcript members, source-package declarations
- Produces: ten-video evidence table and verified status of claimed prior scrapes

- [ ] Extract ten zero-word placeholder records and exact placeholder bodies.
- [ ] Search all repository evidence for Actor run IDs, dataset IDs, dates, and raw outputs.
- [ ] Open every canonical URL and record availability, redirects, and caption/transcript controls.

### Task 3: Targeted Apify recovery

**Files:**
- Create when run occurs: `data/raw/channel-data/DS-000022/apify-transcript-recovery/<RUN_ID>/input.json`
- Create when run occurs: `data/raw/channel-data/DS-000022/apify-transcript-recovery/<RUN_ID>/run.json`
- Create when run occurs: `data/raw/channel-data/DS-000022/apify-transcript-recovery/<RUN_ID>/dataset_raw.json`
- Create when run occurs: `data/extracted/channel-data/DS-000022/recovery/<RUN_ID>/recovery_clean.json`
- Create when run occurs: `data/extracted/channel-data/DS-000022/recovery/<RUN_ID>/recovery_results.csv`

**Interfaces:**
- Consumes: ten verified canonical video URLs and live Actor input schema
- Produces: immutable raw evidence plus video-ID-keyed clean results

- [ ] Inspect current Actor schema and event-pricing display.
- [ ] Configure exactly ten URLs with supported video-detail and transcript options.
- [ ] Run once, monitor terminal status, and save sanitized metadata and complete dataset output.
- [ ] Retry once only if first input is proven incomplete.

### Task 4: Recovery merge and script audit

**Files:**
- Modify only if recovery succeeds: `data/extracted/channel-data/DS-000022/packages/lucas-grant/LucasGrant_Master_Data.xlsx`
- Modify only if recovery succeeds: `data/extracted/channel-data/DS-000022/packages/lucas-grant/LucasGrant_Transcripts_95_Videos.zip`
- Inspect: `scripts/.generate_ds22_manifests_tmp.py`
- Test/modify only when needed: `tests/test_validate_supplied_channel_packages.py`
- Modify only when needed: `scripts/validate_supplied_channel_packages.py`

**Interfaces:**
- Consumes: recovery results and current canonical package
- Produces: 95-row workbook/ZIP with recovered transcript data or per-video verified placeholders

- [ ] If code behavior changes, write and run a failing regression test first.
- [ ] Merge by exact video ID and rebuild ZIP deterministically.
- [ ] Recalculate workbook values and scan for formula errors.
- [ ] Determine hidden script status from filesystem, index, history, and references; keep no temporary artifact.

### Task 5: Manifests, lineage, and validation

**Files:**
- Modify: `data/manifests/DS-000022.md`
- Modify: `data/manifests/DS-000022_FILES.csv`
- Modify: `data/manifests/DS-000022_SOURCE_ARTIFACTS.csv` only if source lineage changes
- Modify: `data/extracted/channel-data/DS-000022/DS-000022_PACKAGE_VALIDATION_REPORT.md`
- Create: `data/extracted/channel-data/DS-000022/DS-000022_LUCAS_TRANSCRIPT_RECOVERY_REPORT.md`

**Interfaces:**
- Consumes: final package files and immutable run evidence
- Produces: final checksums, lineage, reconciliation, and video-level limitations

- [ ] Recompute every changed artifact size and SHA-256.
- [ ] Validate seven workbooks, seven ZIPs, 732 unique IDs, overlaps, formulas, hyperlinks, and manifest paths.
- [ ] Render affected workbook sheets and inspect visually.
- [ ] Run DS-000022-specific tests, then repository-wide tests; separate environment failures.

### Task 6: Scoped commit, push, and remote verification

**Files:**
- Stage only task paths found changed by verification

**Interfaces:**
- Consumes: verified working tree
- Produces: focused commit(s) on synchronized `origin/main`

- [ ] Scan staged data for credentials and hosting-size limits.
- [ ] Run `git diff --cached --check` and inspect staged stats.
- [ ] Commit recovery evidence/package corrections and any justified script cleanup separately.
- [ ] Push without force and prove local HEAD, `origin/main`, and remote SHA match.
- [ ] Confirm final worktree status and tracked artifact list.
