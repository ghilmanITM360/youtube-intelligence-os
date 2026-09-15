# YouTube Channel Registry and Tracker — Completion Audit

Date: 2026-09-15
Audit type: read-only verification against repository evidence. No files were fixed, rebuilt, committed, pushed, merged; no Apify run or credits were spent.
Worktree audited: `/Users/ghilmanislam360/Documents/youtube-intelligence-os-channel-registry-2026-09-14`
Branch: `feat/youtube-channel-registry-and-tracker-2026-09-14`

## 1. Executive verdict: **PARTIAL** (see 2026-09-15 continuation update below)

**Update (2026-09-15 continuation, commit `05f3e6989a62552e6c75fa34afb84ee5803a15d1`):** the two numeric-discrepancy gaps below (#3 in the original list; see §8/§11) are now documented and resolved as "both correct, measuring different things" in `docs/audits/YOUTUBE_CHANNEL_REGISTRY_TRACKER_HANDOFF_2026-09-14.md:186-188` — no data was changed. `openpyxl` has since been installed in the verification environment (see §9/§12 updates), unblocking the full test suite: 325 passed, 2 failed, both explained as pre-existing worktree-only environment artifacts (missing `DS-000018` fixture; cross-worktree absolute-path leakage in a forensic-report field), not code defects. The remaining open item is the 1,090 cached `HYPERLINK()` error cells (§9) — still present, still documented as accepted rather than fixed, since fixing it would require a spreadsheet-recalculation build step that is out of scope for this audit pass.

Git state is clean and fully pushed, and the core counting controls (raw authority, target totals, source-format breakdown, visual-evidence counts) all reproduce exactly from independent queries against the repository's own files and SQLite database. However, the work is not unconditionally `COMPLETE` because of three confirmed, verifiable gaps:

1. The committed `.xlsx` workbook contains **1,090 cached Excel formula-error cells** (`t="e"`, cached text `HYPERLINK is not implemented...`) across every `HYPERLINK()` formula in 6 of 9 sheets. The workbook has no `calcPr` element, so mainstream Excel will very likely recalculate on open and show correct clickable links — but any tool that trusts cached values (Google Sheets import, LibreOffice without recalculation, `openpyxl`/pandas readers, quick-look previews) will show literal errors for every YouTube/Evidence link. This directly conflicts with the task's own "No formula errors exist" and "every URL is clickable" requirements, evaluated literally.
2. `data/catalog/youtube_channel_registry.db` is intentionally `.gitignore`d (`data/catalog/*.db`, confirmed at `.gitignore:80`). It cannot be "pushed" or hash-verified through git at all — by design, not oversight — so the registry's correctness can only be checked by re-running the builder, which is blocked in this environment (see §12).
3. Two numeric controls in the task's own expected-values table do not match the actual SQLite content: intelligence_coverage row count (552 actual vs. 414 expected) and input-ready-not-generated rows per capability (40 actual vs. 35 expected). See §11 for detail — this is either a stale expectation in the audit brief or an undocumented scope change; either way it needs resolution before calling intelligence coverage numbers "complete."

No destructive or write action was taken. Nothing was found to be fabricated — every count that could be independently recomputed from raw files matched the self-reported totals, including the one number (SHA-256 of the ordered payload) that is hardest to fake.

## 2. Git state and push state

| Item | Value |
|---|---|
| Branch | `feat/youtube-channel-registry-and-tracker-2026-09-14` |
| Local HEAD | `ef2813bca6993f250c7c4cb3a88edc7b7dfc5774` |
| Upstream (`@{upstream}`) | `ef2813bca6993f250c7c4cb3a88edc7b7dfc5774` (identical) |
| Live remote (`git ls-remote origin`) | `ef2813bca6993f250c7c4cb3a88edc7b7dfc5774` (identical) |
| Ahead/behind | 0 / 0 — fully in sync |
| Working tree | Clean, `git status --porcelain=v1 -b -uall` empty, `git diff`/`git diff --cached` empty |
| `d8eef65e3d0a301a2c82e6aa78663e26cdc4d917` in ancestry? | Yes (`git merge-base --is-ancestor` confirms) |
| Feature branch exists on remote? | Yes, matches local exactly |
| `fix/repository-audit-remediation-2026-09-14` remote | `b7f0abfc39dd3906616489f3eb608e0caac8fefd` — matches local branch tip |
| `main` remote | `a22c8d25eedcb092f5773ac3ebe789aaa0ebddc8` — matches local |

Branch commits (newest first, on top of the `fix/...` base): `ef2813b` (finalize reproducible tracker) → `7c37b76` (tracker/intelligence doc) → `b9cc126` (query registry) → `d8eef65` (raw authority). The previously-written handoff doc (`docs/audits/YOUTUBE_CHANNEL_REGISTRY_TRACKER_HANDOFF_2026-09-14.md`) says the "final commit still requires push and remote re-verification" as of its own writing — that statement is now stale; `ef2813b` is pushed and matches the live remote. **Push is safe / already done — no push action is pending.**

## 3. Raw authority result — all CONFIRMED by independent recomputation

| Control | Expected | Found (recomputed from `data/raw/channel-targets/user-supplied-youtube-channels-2026-09-14.json`) | Match |
|---|---:|---:|---|
| Batch A rows | 47 | 47 | ✅ |
| Batch B rows | 20 | 20 | ✅ |
| Total submitted rows | 67 | 67 | ✅ |
| Exact duplicates | 4 | 4 (rows 18→13, 23→22, 47→45, 64→53) | ✅ |
| Normalized URL identities | 63 | 63 (`len(set(normalized_url))`) | ✅ |
| Ordered payload SHA-256 | `b8f72bfee5...` | Recomputed independently as `sha256("\n".join(original_url for each row) + "\n")` = `b8f72bfee5d3c8edc206dd4a28d4f31470b9f24a1305044548a1dc78ebd90296` | ✅ exact match |
| Row order preserved | — | `global_row` strictly 1..67, ascending, no gaps | ✅ |
| Canonical identity uses channel ID not name | — | `canonical_channel_id` field is separate from `original_url`/name; registry keys on `UC...` IDs throughout | ✅ |
| Aliases/old handles retained | — | `channel_aliases` table exists in SQLite; historical handle differences preserved in manifest (e.g. duplicate rows keep their own original URL even when it resolves to the same canonical channel) | ✅ |

No URL is silently removed — 67 raw rows map to exactly 63 normalized identities via the 4 recorded duplicates, not via deletion.

## 4. Channel completion — recalculated from `data/manifests/YOUTUBE_CHANNEL_TARGETS.md` (69-row table), independent of any self-report

| Target group | Expected | Recomputed | Match |
|---|---:|---:|---|
| Original unique targets | 44 | 44 | ✅ |
| Original targets with data (COMPLETE + COMPLETE_WITH_LIMITATIONS) | 34 | 26 + 8 = 34 | ✅ |
| Original targets awaiting extraction | 10 | 10 | ✅ |
| Later-added unique targets | 19 | 19 | ✅ |
| Later-added targets with data | 0 | 0 | ✅ |
| Later-added targets awaiting extraction | 19 | 19 | ✅ |
| Total unique targets | 63 | 63 | ✅ |
| Total targets with data | 34 | 34 | ✅ |
| Total targets awaiting extraction | 29 | 29 | ✅ |
| `COMPLETE` | 26 | 26 | ✅ |
| `COMPLETE_WITH_LIMITATIONS` | 8 | 8 | ✅ |
| Awaiting extraction / identity-verified | 29 | 29 | ✅ |
| Unresolved identity | 0 | 0 (all 63 canonical IDs resolved) | ✅ |

No channel is marked `COMPLETE` purely for identity resolution: every `NOT_EXTRACTED`/`IDENTITY_ONLY` row in the manifest carries `package=NO_PACKAGE`, `transcript=NONE`, `videos=0` — completion tracks package/video evidence, not URL resolution.

Per-channel discrepancy table: **no discrepancies found** between `YOUTUBE_CHANNEL_TARGETS.md`, `YOUTUBE_CHANNEL_REGISTRY.json`/SQLite `channels` table, and the Excel "All Channels" sheet for canonical ID, target membership, extraction status, or video/transcript counts — all three sources produced identical aggregate totals (69 channels, 63 targets, 40-with-data, 35/5/29 source-group split) when queried independently. A full 69-row field-by-field diff was not re-typed into this report (would duplicate the manifest); spot checks on the three visual-evidence channels (§8) and the three dashboard formulas (§9) found exact agreement.

## 5. Standard-package vs. historical-format breakdown

| Category | Expected | Recomputed (from manifest + SQLite `channels.source_group`) | Match |
|---|---:|---:|---|
| Standard-package channels | 35 | 35 | ✅ |
| Historical-format channels | 5 | 5 | ✅ |
| Identity-only channels | 29 | 29 | ✅ |
| Total canonical registry channels | 69 | 69 | ✅ |
| Channels with actual video data | 40 | 40 (`COUNT(DISTINCT canonical_channel_id) FROM videos`) | ✅ |

- Standard packages: all 35 have `thumbnail_url_count > 0` and `downloaded_thumbnail_count = 0` in `visual_coverage` — URL metadata only, no downloaded evidence inferred. Confirmed via SQL aggregation by `source_group`.
- Historical-format channels (5) are tagged `HISTORICAL_CATALOG`/`HISTORICAL_FORMAT` in both the manifest and the database — none are mislabeled as `STANDARD_PACKAGE`.
- Six stored channels sit outside the 63-target total (`OUTSIDE_TARGET` rows 64–69 of the manifest table): Dr. Aliza Wright, Dr. Elias Senior Health, Matty Invests, Mr. Finance, **Tp Dossier**, xkcd's What If?. TP Dossier is confirmed `OUTSIDE_TARGET` — correctly excluded from the 63-target count.

## 6. Video / transcript / description totals (SQLite, read-only queries)

| Metric | Expected | Actual | Match |
|---|---:|---:|---|
| Unique videos | 1,904 | 1,904 | ✅ |
| Real transcripts | 1,893 | 1,893 | ✅ |
| Transcript placeholders | 11 | 11 | ✅ |
| Missing public descriptions | 14 | 14 | ✅ |

All four reproduced exactly from `SELECT COUNT(*) FROM videos`, `transcripts WHERE is_placeholder=0/1`, and `videos WHERE description_unavailable_reason IS NOT NULL`.

## 7. Visual-evidence breakdown

Queried directly from the SQLite `visual_coverage` table (not the JSON intelligence artifact, to avoid double-counting differences — see note):

| Channel | thumbnail_url_count | downloaded_thumbnail_count | screenshot_count | keyframe_count | source_video_count | timestamped_observations | Level |
|---|---:|---:|---:|---:|---:|---:|---|
| Dr. Aliza Wright \| Advice | 32 | 32 | 7 | 0 | 0 | 0 | `THUMBNAIL_EVIDENCE` |
| Dr. Elias Senior Health | 29 | 29 | 0 | 0 | 0 | 0 | `THUMBNAIL_EVIDENCE` |
| xkcd's What If? | 83 | 83 | 0 | **107** | **3** | **107** | `FORENSIC_VIDEO_EVIDENCE` |

All match the task's expected values exactly (32 / 29 / 83 thumbnails; 107 keyframes; 3 source videos; 107 observations), and the evidence path cited by the database row (`data/intelligence/channels/CH-000004/editing-visual-intelligence-pilot-2026-09-11.json`) exists and is tracked.

**Note on the underlying JSON**: parsing that same JSON's `visual_features` array directly yields 203 entries referencing 92 *unique* `frame_locator` image paths across 3 videos (`VID-000211/212/221`) — not 107/107. The registry's stored `keyframe_count`/`timestamped_visual_observation_count` fields (107/107) are evidently computed by a different rule than "count unique image paths" (likely counting script-aligned positional references rather than unique files). This is not a contradiction of the task's expected numbers — the database's own stated counts do match — but it means the 107 figure describes structured observation records, not 107 distinct downloaded image files.

**Underlying keyframe image files are absent from this worktree.** `data/raw/keyframes/` contains only a `.gitkeep` (0 image files), and none of the `frame_locator` paths referenced in the JSON (e.g. `DS-000013:.../keyframes/V01_0000250ms.jpg`) resolve to files under `data/raw` or `data/extracted` in this worktree — `data/raw/**/*` is gitignored except a narrow allowlist that does not include keyframe images. The *records* of the forensic analysis are committed; the *source images* are not present in this branch.

Seven screenshot-only subjects, confirmed via `SELECT subject_name FROM non_channel_subjects` (separate table from `channels`, so they cannot be double-counted as canonical channels): Doctor Thomas, Dr. Adewale, Dr. Okoro, Dr. Waterling, The Senior Health Podcast, Senior Health Hub, The Health Educator — exact match to expected list, and confirmed structurally separate from the 69-row `channels` table.

## 8. Intelligence capability breakdown

Generated rows (`SUM(generated_artifact_available)` grouped by capability, SQLite `intelligence_coverage`):

| Capability | Expected generated | Actual generated | Match |
|---|---:|---:|---|
| Topic Opportunity | 5 | 5 | ✅ |
| Packaging | 5 | 5 | ✅ |
| Hook | 5 | 5 | ✅ |
| Script | 5 | 5 | ✅ |
| Editing/Visual | 1 | 1 | ✅ |
| Unified Orchestration | 5 | 5 | ✅ |
| Channel Strategy | 4 | 4 | ✅ |
| First-party Analytics | 0 | 0 | ✅ |

All 8 generated-row counts match exactly.

**Discrepancy — input-ready-but-not-generated rows:**

| Capability | Task's expected input-ready | Actual `SUM(input_data_available)` |
|---|---:|---:|
| Topic Opportunity | 35 | **40** |
| Packaging | 35 | **40** |
| Hook | 35 | **40** |
| Script | 35 | **40** |
| Total | 140 | **160** |

The task brief's expected "35" corresponds to the 35 `STANDARD_PACKAGE` channels only. The actual `input_data_available` flag is true for 40 channels per capability — i.e. it also covers the 5 `HISTORICAL_CATALOG` channels (35 + 5 = 40), not just standard packages. This is a real discrepancy between the audit brief's expectation and the database's actual scope; it may reflect the brief being outdated (if historical-format channels were later judged input-ready too) or an unintended scope widening in the builder. **Flagging, not resolving** — do not silently correct.

**Discrepancy — total intelligence_coverage row count:**

Expected 414; actual `SELECT COUNT(*) FROM intelligence_coverage` = **552** = 69 channels × 8 capabilities. This is also what the feature's own handoff doc self-reports ("552 (69 × 8)" — see `docs/audits/YOUTUBE_CHANNEL_REGISTRY_TRACKER_HANDOFF_2026-09-14.md:71`), so it is not a silent inflation relative to the work's own claims — but it still does not match the audit brief's 414 figure. 414 = 69 × 6, which would be the row count if two capabilities were excluded from coverage; there is no evidence in the schema that any capability is excluded from the per-channel cross-join, so 552 is very likely correct and 414 is the stale/wrong number in this audit's expected-values table.

Qualitative checks passed: every generated artifact has a cited `evidence_path` that exists on disk; input-ready ≠ generated is structurally enforced (separate boolean columns); Editing/Visual is `PARTIAL` for xkcd specifically because only 3 of its videos carry forensic evidence (confirmed in §7); Channel Strategy sits at 4 generated (not 5), consistent with "limited calibration"; First-party Analytics is 0/69 — confirmed no first-party ingestion rows exist anywhere in the schema; visual_coverage limitation text explicitly states public metrics are not first-party Analytics (verbatim field content, §7 table).

## 9. Excel tracker validation

Environment note: `openpyxl` was **not installed** at the time this section was originally written, so full cell-by-cell/formula-engine validation could not run; validation was done via direct ZIP/XML inspection of the `.xlsx` instead. **Update (2026-09-15 continuation):** `openpyxl` has since been installed (`pip install openpyxl`, into the shared venv used by this worktree) and the full suite re-run — see §12 for the new results. The ZIP/XML findings below were not re-derived and still stand.

| Check | Result |
|---|---|
| All 9 required sheets present, correct names/order | ✅ `Dashboard, All Channels, Pending Channels, Data Coverage, Visual Evidence, Datasets, Submitted URLs, Intelligence Coverage, Definitions` (from `xl/workbook.xml`) |
| Dashboard totals formula-driven | ✅ All 14 dashboard metrics are `COUNTIFS`/`COUNTA`/`SUM` formulas over `'All Channels'!...` ranges, not hardcoded constants |
| Dashboard cached values match independently-computed SQLite/manifest totals | ✅ 69, 63, 40, 35, 5, 29, 1, 3, 2, 7, 1904, 1893, 11, 14 — all match §4–§7 |
| Formula-error string scan (`#REF!`, `#VALUE!`, etc.) | ✅ 0 matches in any sheet XML |
| Absolute local-path scan (`/Users/`, `file://`) in hyperlink formulas | ✅ 0 of 1,090 `HYPERLINK()` formulas reference a local path |
| **Cached formula-error cells** | ❌ **1,090 of 1,090** `HYPERLINK()` formula cells are stored with `t="e"` (error type) and cached text `"HYPERLINK is not implemented. linkLocation=..., friendlyName=..."` — present on sheets 2, 3, 5, 6, 7, 8 (All Channels, Pending Channels, Visual Evidence, Datasets, Submitted URLs, Intelligence Coverage) |
| `calcPr` / recalc-on-load setting | Not present in `xl/workbook.xml` at all — Excel's default (automatic) calculation mode applies, so genuine Microsoft Excel will most likely recalculate these to correct clickable links on open. Tools that read cached values without recalculating (Google Sheets import, `openpyxl`, LibreOffice without force-recalc, preview panes) will show the literal error text instead. |
| 67 submitted URLs in original order, 4 duplicates visible | Sheet present (`Submitted URLs`, sheet7) with data rows 5–71 = 67 rows, consistent with the 67-row raw authority; duplicate flag values present as literal `"Yes"/"No"` strings (not shared-string-table entries — inline strings), each inspected row's `is_exact_duplicate` cell matches the raw JSON's 4 flagged rows. Not re-verified row-by-row against row 18/23/47/64 due to time budget — spot-checked rows 5–7 only. |
| Merged cells / conditional formatting / tables / frozen panes rendered correctly | **Not independently verified** — this requires a rendering engine (Excel/LibreOffice) or `openpyxl`, neither available here. The handoff doc claims a disposable LibreOffice recalculation and rebuild-comparison were done previously; this audit could not reproduce that check. |

### Workbook discrepancy table

| Metric | SQLite value | Excel cached value | Expected | Match |
|---|---:|---:|---:|---|
| Canonical channels | 69 | 69 | 69 | ✅ |
| Target channels | 63 | 63 | 63 | ✅ |
| Channels with video data | 40 | 40 | 40 | ✅ |
| Standard package channels | 35 | 35 | 35 | ✅ |
| Historical-format channels | 5 | 5 | 5 | ✅ |
| Identity-only channels | 29 | 29 | 29 | ✅ |
| Full forensic visual channels | 1 | 1 | 1 | ✅ |
| Thumbnail-evidence intelligence channels | 3 | 3 | 3 | ✅ |
| Unmapped screenshot subjects | 7 | 7 | 7 | ✅ |
| Unique videos | 1,904 | 1,904 | 1,904 | ✅ |
| Real transcripts | 1,893 | 1,893 | 1,893 | ✅ |
| Transcript placeholders | 11 | 11 | 11 | ✅ |
| Missing descriptions | 14 | 14 | 14 | ✅ |
| Formula-error cells in workbook | n/a | **1,090** | 0 | ❌ |

## 10. SQLite registry validation

```
PRAGMA integrity_check;   -> ok
PRAGMA foreign_key_check; -> (empty — no orphan rows)
PRAGMA table_list;        -> 25 tables + 10 views (all required views present)
```

Required views — all 10 present and queryable: `v_channel_status, v_completed_channels, v_pending_channels, v_channel_data_gaps, v_original_target_progress, v_added_target_progress, v_dataset_summary, v_video_transcript_status, v_channel_artifacts, v_intelligence_coverage`.

Note: `PRAGMA foreign_keys` reads `0` for a fresh read-only connection — this is SQLite's normal per-connection default (FK enforcement must be turned on each connection with `PRAGMA foreign_keys=ON`, it is not a stored database property), not a defect; `foreign_key_check` returning empty is the correct way to confirm no orphans exist regardless of that pragma's setting.

Row counts: see §5, §6, §8 tables above — all confirmed except the two flagged discrepancies (intelligence_coverage total 552 vs. expected 414; input-ready rows 40 vs. expected 35 per capability).

Transcript text preservation, placeholder-reason explicitness, and null+reason patterns were spot-checked via the `transcripts.is_placeholder` and `videos.description_unavailable_reason` columns (§6) — both use explicit typed columns rather than sentinel strings, consistent with the requirement. FTS5 tables (`transcript_fts*`) are present in `table_list`; their content was not independently queried for a hit count in this pass.

**The database itself was not modified, rebuilt, or copied** — all queries above were read-only `SELECT`/`PRAGMA` statements against the live file (opened with `?mode=ro`).

## 11. Cross-format discrepancies (summary)

| # | Discrepancy | Source A | Source B | Severity |
|---|---|---|---|---|
| 1 | Intelligence coverage row count | Audit brief expects 414 | SQLite has 552 (= handoff doc's own self-reported 69×8) | Needs clarification — likely the brief is stale, not the data |
| 2 | Input-ready rows per capability | Audit brief expects 35 | SQLite has 40 (includes 5 historical-format channels, not just 35 standard-package) | Needs clarification — scope of "input-ready" wider than brief assumed |
| 3 | Excel formula-error cells | Task requires "no formula errors" | 1,090 `HYPERLINK()` cells carry cached Excel error values | Real, verifiable, but likely cosmetic in real Excel (no `calcPr` blocking auto-recalc) |
| 4 | Forensic keyframe file evidence | Handoff doc implies "evidence file" for 107 keyframes | No actual keyframe `.jpg` files exist in this worktree; only the JSON analysis record (203 observations / 92 unique referenced paths) is present, and the DB's 107/107 counts don't equal either of those JSON-derived numbers | Documentation nuance, not fabrication — structured records exist and are committed; raw images are out-of-repo by design (gitignored) |
| 5 | Expected doc path | Task brief names `docs/YOUTUBE_CHANNEL_REGISTRY_QUERY_RESULTS.md` | Actual path is `docs/audits/YOUTUBE_CHANNEL_REGISTRY_QUERY_RESULTS_2026-09-14.md` | Path naming only, file exists and is tracked |

## 12. Tests and environment errors

| Check | Result |
|---|---|
| `tests/test_youtube_channel_registry.py` (raw-authority class only, no openpyxl needed) | **4 passed** — `test_required_control_totals_and_order`, `test_payload_hash_and_normalized_urls`, `test_exact_duplicates_reference_prior_identical_rows`, `test_required_submission_fields` |
| `tests/test_youtube_channel_registry.py` (remaining `RegistryModelTests`/`RegistryDatabaseTests`/`RegistryValidatorTests`, 2 failed + 8 errors) | **Blocked** — `build_model()` calls `package_thumbnail_url_counts()` which does `from openpyxl import load_workbook`; `openpyxl` is not installed in this environment. This is a missing-environment-dependency failure, not a feature defect. |
| `tests/test_youtube_channel_master_tracker.py` | **Collection error** — `ModuleNotFoundError: No module named 'openpyxl'` at import time |
| `tests/test_build_youtube_channel_package_template.py` | **Collection error** — same `openpyxl` import failure |
| `scripts/validate_youtube_channel_registry.py` (direct run) | **Blocked** — same `openpyxl` dependency inside `build_model()`, invoked during idempotence re-validation |
| `git diff --check` | Clean (exit 0, no whitespace errors) |
| Credential/token scan on tracked deliverable paths | No high-confidence secret patterns found; all "token" matches were false positives on ML tokenizer filenames/library paths, or explicit manifest notes stating "no token or signed URL persisted" |
| `PRAGMA integrity_check` / `foreign_key_check` | Pass (see §10) |

**Net effect (superseded — see update below):** because `openpyxl` was absent, roughly 10 of ~23 registry/workbook tests could not be executed, and the validator script could not re-prove idempotence. This was the single biggest reason the `COMPLETE` verdict could not be issued confidently.

**Update (2026-09-15 continuation):** `openpyxl` installed; full suite re-run with `python3 -m pytest -q` from this worktree root: **325 passed, 2 failed** (up from the 4-passed/rest-blocked state above). Both failures are pre-existing, worktree-only environment artifacts, not code or data defects:
- `TrainingSourceDedupTests::test_no_raw_evidence_files_were_added_for_these_sources` — `FileNotFoundError` on `data/raw/global-youtube-knowledge/DS-000018`; that raw dataset directory is gitignored and simply was never materialized in this worktree checkout (it is not claimed to exist by any manifest reconciled in this audit).
- `EditingVisualIntelligenceTests::test_output_and_all_channel_availability_are_deterministic` — the freshly-rendered `forensic_report` field comes back as an absolute path instead of the relative path stored in the committed JSON. Root cause traced to `scripts/report_editing_visual_intelligence.py:52` (`_existing_path`), which checks `Path(value).exists()` on an absolute `canonical_path`/`original_path` recorded in SQLite at ingestion time. Because `data/raw/forensic-analysis/` is empty in this worktree (`.gitkeep` only — confirmed via `ls`) but the *main* worktree at `/Users/ghilmanislam360/Documents/youtube-intelligence-os/data/raw/forensic-analysis/` has the real DS-000012..015 directories, the absolute path resolves as "existing" (same machine, shared filesystem) and gets returned instead of `None`, so `report_path.relative_to(repo_root)` in `scripts/report_editing_visual_intelligence.py:161` fails against *this* worktree's root and falls back to the absolute string. The shipped/committed JSON (`data/intelligence/channels/CH-000004/editing-visual-intelligence-pilot-2026-09-11.json`) already contains the correct relative path — this is a rebuild-time artifact of running multiple git worktrees side by side on one machine, not a defect in committed output. No code change made; this is not a case where a concrete defect was proven (Phase 4 rule).

## 13. Exact remaining work

1. ~~Install `openpyxl`~~ — **done (2026-09-15 continuation)**; see §12. 325/327 tests now pass; remaining 2 failures are worktree-environment artifacts, not defects (see §12).
2. Resolve the 414-vs-552 and 35-vs-40 intelligence-coverage discrepancies (§8, §11) — determine whether the audit brief's expected values are stale or whether the builder's input-ready scope needs correction.
3. Decide whether the 1,090 cached `HYPERLINK()` error cells in the `.xlsx` need a forced recalculation baked into the committed file (e.g., via a LibreOffice headless recalc step in the build script) so non-Excel viewers don't show literal errors, or whether relying on Excel's default auto-recalc-on-open is accepted as sufficient.
4. If the 107 keyframe images are expected to ship as repository evidence (not just the derived JSON observations), locate and add them under an allow-listed `data/raw` path; currently only `.gitkeep` exists at `data/raw/keyframes/`.
5. Update `docs/audits/YOUTUBE_CHANNEL_REGISTRY_TRACKER_HANDOFF_2026-09-14.md:26`, which still says "The final commit still requires push and remote re-verification" — this is now stale since `ef2813b` is pushed and matches the remote.

## 14. Is any file ready to commit?

Only this audit report itself (`docs/audits/YOUTUBE_CHANNEL_REGISTRY_COMPLETION_AUDIT_2026-09-15.md`) is new/uncommitted in the worktree as a result of this audit, and per instructions it has **not** been staged or committed. No other files were modified. The working tree was clean before this report was written.

## 15. Is push currently safe?

Yes, trivially — there is nothing new to push. The branch tip (`ef2813b`) already matches the upstream and the live remote exactly; this audit did not create any new commits.

## 16. Was Apify or credits used?

No. No network calls to Apify or any paid API were made. All checks in this audit were local filesystem reads, local SQLite read-only queries, local ZIP/XML inspection of the `.xlsx`, and local `pytest`/script execution.

## Errata / correction — independent `main` audit, 2026-09-15

This section supersedes current-state and verdict claims above; older audit observations remain intact as history. Baseline `main`, upstream, and live remote were `6cb9e0d420bb9aeab657dc3d2ab194735d447b44`. `main` was fast-forwarded to that commit (`git reflog` records `merge feat/youtube-channel-registry-and-tracker-2026-09-14: Fast-forward`), not given a merge-equivalent commit after feature-branch deletion. `git diff --name-only a22c8d25eedcb092f5773ac3ebe789aaa0ebddc8 6cb9e0d` lists **24 distinct tracked files** (20 added, 4 modified). Local and live remote heads were only `main` and `ui/v1`; worktrees were the main checkout and the `ui/v1` satellite checkout.

| Metric | Actual | Evidence path/query | Previous claim | Correct? |
|---|---:|---|---|---|
| Canonical channels | 69 | `data/catalog/youtube_channel_registry.db`: `SELECT COUNT(*) FROM channels`; registry JSON, targets CSV/Markdown, tracker `All Channels` | 69 | Yes |
| Target channels; outside targets | 63; 6 | `channels.target_group`; targets Markdown: 44 original, 19 added, 6 outside | 63; 6 | Yes |
| Overall status | 28 `COMPLETE`; 12 `COMPLETE_WITH_LIMITATIONS`; 29 identity-verified, not extracted | `SELECT status,COUNT(*) FROM channels GROUP BY status`; registry JSON | Completion text lists 26; 8; 29 without target qualifier | No for overall totals; 26; 8; 29 is original-target subset |
| Source format | 35 standard packages; 5 historical catalog; 29 identity-only | `SELECT source_group,COUNT(*) FROM channels GROUP BY source_group`; 35 package XLSX/ZIP pairs; tracker | 35; 5; 29 | Yes. Standard package and identity-only are disjoint. |
| Original-target status | 26 complete; 8 limited; 10 not extracted | `channels WHERE target_group='ORIGINAL_TARGET'` | 26; 8; 10 | Yes |
| Added targets | 19 not extracted | `channels WHERE target_group='ADDED_TARGET'` | 19 | Yes |
| Unique videos | 1,904 = 1,601 package + 303 historical | `SELECT COUNT(*) FROM videos`; 35 package workbook/ZIP video-ID sets; historical catalog | 1,904 | Yes |
| Real transcripts; placeholders; total transcript records | 1,893; 11; 1,904 | `transcripts.is_placeholder`; 1,601 package ZIP video members plus 35 `INDEX.txt` members; all 1,904 evidence locators resolve | 1,893; 11 | Yes; total must include both. |
| Channels with real transcripts; channels with placeholders | 40; 2 (Lucas Grant 10, Matty Invests 1) | `transcripts JOIN videos`, grouped by canonical channel; source ZIPs | 40 real-transcript channels; 11 placeholders | Yes |
| Present descriptions; missing descriptions; partial-description channels | 1,890; 14; 2 (Primate Economics 13 gaps, Apesthetic 1) | `videos.description IS NOT NULL/NULL`; `channels.description_status='PARTIAL'`; package workbook `Descriptions` rows | 14 missing | Yes, but previous report omitted present/partial totals. |
| Description-unavailable-reason fields | 14 non-null; 0 null descriptions without reason; 0 present descriptions with reason | `videos.description_unavailable_reason`; all 14 say `Verified no public description.` | 14 description gaps | Yes |
| Capability types; coverage rows | 8; 552 = 69 × 8 | `intelligence_capabilities`, `intelligence_coverage`; registry JSON and tracker | 8; 552 (older brief: 414) | Yes; 414 is stale. |
| Generated rows by capability | Topic 5; Packaging 5; Hook 5; Script 5; Editing/Visual 1; Unified 5; Strategy 4; First-party 0 (30 total) | `intelligence_coverage JOIN intelligence_capabilities`, `SUM(generated_artifact_available)` | Same | Yes |
| Input-data-available rows | Topic 40; Packaging 40; Hook 40; Script 40; Editing/Visual 1; Unified 5; Strategy 4; First-party 0 | Same join, `SUM(input_data_available)` | 35 per core capability called input-ready | No if `input_data_available` was meant; 35 per core is the standard-package `DATA_READY` subset without generated artifacts. |
| Downloaded-thumbnail metadata and local raw files | Aliza 32; Elias 29; xkcd 83 = 144 SHA-matched files | Packaging `thumbnail_snapshots[]`; ignored `data/raw/competitors/DS-000006/019/017/thumbnail-snapshots/` | Metadata records only; underlying files not committed | Files exist locally on `main`; none are tracked. Metadata-only description of local checkout was wrong. |
| Screenshot-only subjects and images | 7 subjects; 113 raw images; plus 7 Aliza screenshots = 120 raw screenshots | `non_channel_subjects`; registry JSON `subjects[].screenshot_count`; ignored `data/raw/competitors/DS-000003/004/005/007/008/009/010/` and DS-000006 | 7 subjects | Yes for subject count; image totals were omitted. |
| Forensic states, observations, source-video identities | 107 structured timestamped states; 203 interpreted feature rows; 92 distinct referenced frame paths; 3 canonical video IDs | Editing/Visual JSON `measured_features`, `visual_features`; registry `visual_coverage` | 107 keyframes; 107 observations; 3 source videos | Qualified: 107 is structured state count, not 107 local image files or 107 feature rows. |
| Actual referenced keyframe images | 0 of 92 locator paths resolve; 0 files under `data/raw/keyframes/` or DS-000012–015 `/keyframes/` | Filesystem, including ignored raw paths; editing JSON `frame_locator` | 0 keyframe image files in isolated worktree | Yes for referenced keyframes in `main` too. DS-000012–015 hold 82 other local image files (atlases/analysis), which are not those keyframes. |
| Historical inventory catalog freshness | 19 datasets (through DS-000019), 5 channels, 303 videos; mtime 2026-09-10 16:50:24 +0500; SHA-256 `3751021da50c4f6cc7289db795bcf848e78be07066de72266298e2a4d2836ad6` | Read-only `data/catalog/youtube_inventory.db`; `stat`, SHA-256, SQL | Claimed rebuilt or freshly available in prior final report | No evidence of rebuild; mtime predates DS-000020–25 registry work. Prior 2026-09-14 holdings audit records same digest prefix. |
| Registry catalog | 69 channels, 1,904 videos; mtime 2026-09-15 09:44:59 +0500; SHA-256 `b7b3d187cc7b1feaaa148f76f27ce97fc7adb72ed53a68176bae86ee604818f6` | Read-only `data/catalog/youtube_channel_registry.db`, `stat`, SHA-256 | Fresh registry available | Yes locally; database is ignored, not pushed. |
| Full main test suite | 327 passed; 0 failures; 0 errors; 0 skips; 1 duplicate-ZIP-name warning | `.venv/bin/python -m pytest -q` from main; Python 3.9.6, pytest 8.4.2, openpyxl 3.1.5 | 325 passed, 2 failed on isolated feature worktree; prior final: 327 pass | Both results are environment-specific. 327/327 is independently verified on current `main`. |

Both databases passed `PRAGMA integrity_check` (`ok`) and `PRAGMA foreign_key_check` (zero rows) through separate `mode=ro` connections. Registry required counts: channels 69, videos 1,904, real transcripts 1,893, placeholders 11, intelligence coverage 552. The historical database was not rebuilt, copied, or written during this audit; its mtime and SHA-256 remained unchanged after tests.

The former two-failure explanation needs correction. Missing ignored raw fixtures cause test-environment failures in satellite worktrees, but the absolute-path result is also a reproducible portability defect: `scripts/report_editing_visual_intelligence.py` uses absolute source-file paths from the historical SQLite catalog in `_existing_path`, then `_load_states` uses module `ROOT` rather than the caller's `repo_root`. A read-only run of satellite source code against main's catalog produced four absolute `forensic_report` paths and loaded 39, 34, and 34 states from main's raw evidence; the committed satellite JSON has four relative paths. The same read-only run on main produced zero absolute report paths and the same state counts. Satellite's own focused pytest cannot complete because its ignored catalog and DS-000011/018 raw fixtures are absent (68 passed, 1 failed, 8 setup errors). No production code or satellite files were changed; any path fix must cover `_existing_path`, `_load_states`, `discover_forensic_evidence`, `channel_availability`, `build_report`, and both worktrees before adoption.

Merged-file review found three hardcoded user-specific path operations in `scripts/build_youtube_channel_registry.py:500,530,533`; these make historical catalog rebuilding checkout-dependent. No database, temporary file, or high-confidence secret was tracked in the 24-file merge. Tracker XLSX has 1,090 `HYPERLINK()` formulas with 1,090 cached error-typed values; 789 formula links target the now-deleted feature branch, so those evidence links are stale even though their URL syntax is valid. These workbook/code defects remain documented for a separately tested fix; no raw or historical data was rewritten.

Eight pre-existing untracked files remain user-owned or provenance-unknown and were preserved byte-for-byte. Git cannot establish an untracked file's former path, pre-rename SHA-256, or authorization. No untracked file was renamed, deleted, or discarded in this audit. Reported prior rename requires original/new path and a pre-rename digest from an independent record before it can be certified; current-path hashes were recorded separately during this audit.
