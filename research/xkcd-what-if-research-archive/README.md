# xkcd What If? research archive (non-image backup)

Created 2026-11-23T12:06:01Z. Base commit: `cf2dbb2c80804710f004109c5ff23d5fdadf3e76` (origin/main at creation). This branch holds a **backup copy of the text, data, code and report files** of the xkcd What If? research done on Machine B on 2026-11-23, plus earlier What If audit files. **Images, video and audio are not stored** (their paths, sizes and SHA-256 are in `EXCLUDED_FILES.csv`).

## Status (read this before using anything here)
**Research IN PROGRESS. DRAFT. NOT complete and NOT independently validated.** The folder name `...complete-forensics` repeats the directive's title; it is not a completion claim.

| Review kind | Status |
|---|---|
| Machine measurement (ffprobe, detectors, ASR) | done for 88 of 92 listed videos (4 media files unavailable) |
| Same-model self-review (Claude, one coder) | most coding: 156 boundary reviews, 125 + 160 style frames, 10 claims + 51 episode rows, tranche A scene coding |
| Partial independent review (Codex, a different tool) | two documents: `codex_independent_review_2026-11-23/` (findings F01 to F14, reproduced SC02, SC03, SC05, E09g only) and `codex_readiness_review_2026-11-23/` (production readiness, checks of operative text); neither listened to audio or has expert standing |
| Human listening | **0** (`heard_by` is empty in all 4439 rows of `09_LISTENING_REVIEW_PACK.csv`, 0 rows filled) |
| Expert or domain reviewer | **0** |
| Original MP4 playback by a reviewer | none recorded |

Do not read any count below as verified scenes, retention evidence or channel-wide rates.

## Counts and where they come from (source file, as of 2026-11-23)
| Quantity | Value | Source |
|---|---|---|
| Inventory rows (videos listed) | 92 (88 media files present, 4 missing) | `forensics_2026-11-23/03_CHANNEL_MASTER_INVENTORY.csv` |
| Audit-layer detector shots (44 videos) | 719 detector shots, **not** verified scenes | `forensics_2026-11-23/ledgers_measured/ALL_SHOT_LEDGER.csv` |
| Audit-layer detector events | 2,160, machine detections, not interpreted | `forensics_2026-11-23/ledgers_measured/ALL_EVENT_LEDGER.csv` |
| Campaign-layer shots (44 other videos) | 718 shots, 2,708 events (ledgers live in the repo under `research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/`, not copied) | `forensics_2026-11-23/13_FINAL_REPORT.md` |
| Boundary review sample | 156 shots, same-model, stratified and clustered; descriptive only | `forensics_2026-11-23/review_sample/REVIEWED_SAMPLE.csv`, `14_SAMPLE_DESIGN_ANALYSIS.json` |
| Literal scene coding (Phase 6.4, owner decision) | 260 of 1,437 ledger shots coded (tranche A), 1,177 not coded (B 594, C 583); 3 stills per shot, same-model | `forensics_2026-11-23/phase15_scene_coding/PROGRESS.md`, `A_ten_SCENE_CODING.csv` |
| Style frames | 125 purpose-selected frames (+160 episode frames) | `forensics_2026-11-23/06_STYLE_MEASUREMENTS_125.csv` |
| Science rows | 11 rows in `07_SCIENCE_CLAIM_CHECKS.csv` (SC01 to SC10 plus SC03B rework); 51 episode rows | `forensics_2026-11-23/07_*` |
| Rule ledger | 23 rules (K01 to K23), draft, operative text revised 2026-11-23 | `forensics_2026-11-23/knowledge_base_draft/RULE_EVIDENCE_LEDGER.csv` |
| Listening items | 16 priority + 9 additions, none listened | `09_LISTENING_PRIORITY_ITEMS.csv`, `14_LISTENING_PACK_ADDITIONS.csv` |

The 563 (unreviewed shots of the 719) and 1,177 (uncoded shots of 1,437) remainders belong to different schemes and must not be added. A detector shot is not a verified scene.

## Latest corrections and where they live
- Reconciliation of the Codex review and the external audit: `forensics_2026-11-23/14_RECONCILIATION_CODEX_AND_EXTERNAL_AUDIT_2026-11-23.md` and the final report v4 `forensics_2026-11-23/13_FINAL_REPORT.md`.
- Operative rule text revised (old text kept in column `rule_text_prior_v3`): `knowledge_base_draft/RULE_EVIDENCE_LEDGER.csv`; pre-edit copies of every edited file: `versions_before_reconcile_2026-11-23/`.
- Science: SC02 now QUALIFIED, SC03 OPEN, E09g wording discrepancy (about 1,900 to 2,250 times, not 2x) recorded in `07_SCIENCE_CLAIM_CHECKS.csv`, `07e_EPISODE_CLAIM_CHECKS.csv`.
- Nothing in this archive was rewritten to hide history: older versions are kept (`*_v1_*`, `*_v2prelight_*`, `versions_before_reconcile_2026-11-23/`).

## Known stale or contradictory wording (left as is; NOT rewritten here)
Reported by the Codex readiness review and confirmed by text search on the source files at creation time:
| Where | Stale statement | Latest position |
|---|---|---|
| `forensics_2026-11-23/12_CODEX_CLAUDE_WORKFLOW.md` line 24; `forensics_2026-11-23/knowledge_base_draft/WHAT_IF_SCRIPT_TO_VIDEO_PLAYBOOK.md` line 5 (and the older `*_v2prelight_*` copies) | "narration from 0 s" | rule K06 and hypothesis H2: audio energy near 0 s is measured, speech onset is UNVERIFIED (the Whisper 0.00 s is an artefact); no listening |
| `forensics_2026-11-23/knowledge_base_draft/WHAT_IF_SCIENTIFIC_ANIMATION_GRAMMAR.md` line 5 | "Observed changes are mostly pop-ons, scene swaps and write-ons (K16)" | K16: camera-like moves occur, frequency unmeasured |
| `forensics_2026-11-23/07_SCIENCE_CLAIM_CHECKS.md`, `07e_TEN_EPISODE_PHYSICS_STUDIES.md` | earlier category counts and an earlier 2023-benchmark E09g paragraph precede the corrected text | read the reconcile columns in the CSVs and the addenda |

Read the latest qualified statement, not the first numeric summary.

## Layout
`forensics_2026-11-23/` primary research folder (paths relative to the original folder are preserved) | `codex_independent_review_2026-11-23/` | `codex_readiness_review_2026-11-23/` | `inputs/` original master directive and external audit | `earlier_audits_2026-11-17/` (83-script audit with transcripts; single-video CT scan, text only) | `earlier_preserved_evidence_2026-10-21/` | `archive_tools/` scripts that built this archive | `MANIFEST.csv`, `MANIFEST.json`, `EXCLUDED_FILES.csv`, `DEDUP_MAP.csv`, `EXTERNAL_LOCATIONS_AND_DECISIONS.csv`, `REPO_EXISTING_WHATIF_PATHS_ON_ORIGIN_MAIN.csv`, `REPO_WHATIF_FILES_ONLY_ON_OTHER_BRANCH.csv`, `verify_manifest.py`.

## Included
1071 source files (30.8 MB) copied byte for byte, plus generated archive files (listed in MANIFEST with status GENERATED).
| Category | Files |
|---|---|
| dataset_csv | 488 |
| dataset_json | 310 |
| feed_snapshot_xml | 1 |
| numpy_array | 2 |
| report_or_doc_markdown | 108 |
| script_python | 72 |
| transcript_or_text | 90 |

| Source group | Files |
|---|---|
| codex_independent_review | 4 |
| codex_readiness_review | 1 |
| earlier_83_script_audit | 92 |
| earlier_single_video_ct_scan | 23 |
| external_audit_input | 1 |
| main_forensics_audit | 940 |
| original_master_directive | 1 |
| preserved_what_if_forensic_evidence | 9 |

## Excluded (full list with SHA-256 in `EXCLUDED_FILES.csv`)
| Reason | Files | Size |
|---|---|---|
| audio | 4 | 162.6 MB |
| dependency_install_log | 1 | 0.0 MB |
| image | 6233 | 540.5 MB |
| repo_gitignore_rule_*.log | 8 | 0.0 MB |
Also not listed file by file: 15,520 files of a Python virtual environment (`.venv-demucs`), and one `.pyc`. Frame images are described by the CSV and JSON metadata that are included (`phase15_scene_coding/*.csv`, `07*_SAMPLE_FRAMES.csv`, ledgers). The 88 source MP4s, the book PDF and its parts, and other unrelated Downloads items are excluded (`EXTERNAL_LOCATIONS_AND_DECISIONS.csv`). Eight `*.log` files are excluded because the repository `.gitignore` ignores `*.log` (line 31); they are build logs only.

## Deduplication
Two files are byte-identical to files already on origin/main and were not copied (mapping in `DEDUP_MAP.csv`). 12 groups of internal exact duplicates are kept on purpose (version and provenance copies) and listed there.

## Unavailable or not done
Listening, expert review, Machine A data, source-article correspondence, book-art comparison, scene coding of tranches B and C, 2,160 event interpretations, any original video or asset.

## Rights and privacy notes
The GitHub repository is **public**. The archive includes transcripts and ASR text of third-party (xkcd) videos as research data; the same transcripts are already tracked on origin/main under `research/what-if-scripts/`. No secrets were found by a pattern scan of included text (API keys, tokens, private keys, passwords, e-mail addresses). Local paths contain the Machine B user name, as many existing repo documents do. No xkcd art, book pages or audio are stored.

## Verify
`python3 -I research/xkcd-what-if-research-archive/verify_manifest.py` recomputes SHA-256 and size for every file listed in `MANIFEST.csv` and reports unlisted files.


## Addendum 2026-11-24 (Machine A): later What If research added
Start at `LATEST_RESEARCH_INDEX_2026-11-24.md` (folders, Claude vs Codex, calendar differences, open science issues, exclusions) and `LATEST_MANIFEST_2026-11-24.csv` (source path, destination, size, SHA-256, status). New folders: `topic_cadence_deep_audit_2026-11-23/`, `claude_calendar_review_2026-11-24/`, `codex_calendar_review_2026-11-24/`, `codex_topic_order_audit_2026-11-23/`, `codex_cadence_topic_order_2026-11-23/`, `forensics_logs_supplement_2026-11-23/`. All DRAFT / self- or Codex-reviewed; no expert review, no listening, no owner approval of any proposed calendar. The counts above (1071 files, etc.) describe the original 2026-11-23 archive only; `MANIFEST.csv` now also lists the added files, `MANIFEST.json` carries an `addendum_2026-11-24` key.
