# 13 Final report v2: xkcd What If? complete forensics (rewritten 2026-11-23 after the continuation from checkpoint 15)

**Status: NOT a finished research system.** 4 of 14 phases are COMPLETE, 10 are PARTIAL, 0 are NOT STARTED (criterion: COMPLETE only when every substantive requirement of the original directive is met, within self-review). Reviews are machine analysis or one-model self-review; **there is no human review and no independent review of any kind.** Repo untouched: branch `research/what-if-channel-strategy-2026-11-18`, HEAD `9eb4f5ab`, no commits, no branch switches, nothing pushed or merged, no media modified. The v1 report is kept as `13_FINAL_REPORT_v1_2026-11-23T1152.md`; earlier conclusions that changed are listed in section G.

## Phase 0 to 13 status against the original directive
| Phase | Requirement | Done (evidence) | Status | Remaining and limits |
|---|---|---|---|---|
| 0 | workspace safety | `00_PHASE0_WORKSPACE_STATE.md` (+ addendum: coordination records read, no What If claim refs); tree clean, 2 worktrees untouched | COMPLETE | self-review; Finance writer rules do not cover What If, noted |
| 1 | audit existing strategy | `01_*` (25 claims; C02 and C17 updated 2026-11-23) | COMPLETE | self-review |
| 2 | audit repository, 83 scripts | `02_*`, 83 of 83 audits verified; transcript gap statements corrected | COMPLETE | prose of audits not re-judged |
| 3 | other local folders, 16 attributes per file | 10 folders concluded; `02_WHAT_IF_RELATED_FILE_REGISTER.csv` now has all attributes | PARTIAL | the new attributes are rule-derived from path, category and sha256, not file-by-file inspection; 1,371 candidate rows |
| 4 | verified channel inventory | live recount 92 = 46 long + 46 Shorts (`live_channel_ids_2026-11-23.json`); inventory v2 with aspect ratio, dates, audio, legal status | PARTIAL | article correspondence 0 verified (22 title candidates, 22 weak, 48 unknown); unlisted videos cannot be excluded |
| 5 | script reconciliation, playbook | `05_*`, `05_PHASE5_VERIFICATION.md`, `05_RULE_EVIDENCE_LINKS.csv`, era split | COMPLETE | stability check, not a pre-registered holdout; corrections: no CTA 41/43, length by era |
| 6 | real visual forensics (6.1 to 6.5) | coverage matrix; style on 125 frames; 108 shots viewed; pacing by definition; machine CT scan of 88 videos; 1 video deep-viewed | PARTIAL | 611 of 719 shots and 2,160 events not interpreted; style sample not random; no book-art comparison; motion not assessed except the pilot |
| 7 | science and physics layer | 125 frames coded; 10 spoken claims recomputed | PARTIAL | the 10 directive episodes not studied one by one; constants partly not fetched; not expert review |
| 8 | asset recipes and contracts | `08_*` (schema, 10 scene breakdowns, method rule) | PARTIAL | design proposals only; nothing built or tested |
| 9 | narration, editing, sound | machine alignment (4,439 segments) and loudness (88); listening pack | PARTIAL | **listening BLOCKED**; no human-verified timing; music and effects unexamined |
| 10 | validation and holdouts | H1 to H9 (`10_*`) | PARTIAL | independent QA UNAVAILABLE; no per-topic-family test |
| 11 | canonical knowledge base | `knowledge_base_draft/`: 14 documents + 23-rule ledger | PARTIAL | draft inside the audit folder, not published; limits above carry into every rule |
| 12 | Codex + Claude workflow | `12_CODEX_CLAUDE_WORKFLOW.md` v2 | PARTIAL | design only, not run by two agents; no tool tested |
| 13 | final report A to F | this file | PARTIAL | the report exists; the research it reports is not finished |

## A. Existing research audit (`research/what-if-channel-strategy/`, branch-only)
Detail: `01_*`. 25 claims: VERIFIED 11, MEASURED 3, OBSERVED 3, INFERRED 3, UNVERIFIED 3, CONTRADICTED 1 (2026 long durations are 2:42 to 4:38, not 2:43 to 3:33), SUPERSEDED 1 (C17, later re-rated PARTIAL: the 7.77 s shot median is valid only as a Brain shot median, see `06_PACING_CORRECTION.md`). C02 updated: 83 catalog transcripts, 5 provisional ASR, 4 without media. Qualified: "no CTA" holds for wording only (a red book-promo end card closes 44 of 44 long videos). Useful for production: catalog numbers, IP boundary, honest labelling. Not usable: any xkcd visual statement beyond the 14-video Brain.

## B. Local data discovery
Detail: `02_DUPLICATES_AND_PROVENANCE.md`, `02_LOCAL_WORKSPACE_INVENTORY.csv`, `02_WHAT_IF_RELATED_FILE_REGISTER.csv`, `02_MEDIA_AND_TRANSCRIPT_AVAILABILITY.md` (all corrected). Key facts: library `YIOS-Media-Library/xkcd Channel/` holds 88 MP4s (hash equal to the census for 88 of 88, 0 duplicate hashes); the older Brain source folder holds 14 MP4 encodes (0 of 14 hash-equal; same logical videos); 3 competitor MP4s; 1,371 What If-related candidate files across 7 of the 10 audited folders; offline-map-audits excluded. Missing: 4 videos, Machine A data, SRC01/SRC02 registry IDs (candidates `rGZ6TsXvi8E`, `TIDHee_Q5Gk`; owner decision).

## C. Repository audit
Branch and status as above. The strategy folder exists only on this branch (not on `origin/main`); `research/what-if-scripts` (83 audits, 41 files) and the campaign `research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww` (manuals v0.1 to v0.7, 44 per-video ledgers) are on `main`. Transcript coverage 83 catalog + 5 ASR; media 88 of 92.

## D. Visual forensic report
- **Coverage (logical IDs, `03_CORPUS_COMPLETENESS_REPORT.md`):** DEEP_VISUAL 1 (visual-only), TARGETED 43, STRUCTURAL 44, UNAVAILABLE 4. Machine-measured: 88 of 88 (every frame, CT machine stage). Sampled and viewed: 125 science frames (82 videos), 108 shots (44 videos), 1,632 residual runs (88 videos). Kept as three separate statuses.
- **Editing rhythm:** see `06_PACING_CORRECTION.md`: event gap about 2.1 s and 22 events per minute replicate across 44 + 44 disjoint videos; shot median 8.4 s (campaign) vs 6.7 s (audit detector); about 93% of frames are holds.
- **Character construction and style:** `06_STYLE_ANALYSIS_PHASE62.md`: ring head, line body (height 3.5 x head), thin line about 6 px, achromatic palette, red accent in 31% of frames, negative space 0.66 and 0.77.
- **Motion grammar:** pop-ons, scene swaps and write-ons dominate (campaign labels); pan and zoom over a map background appears in one Short (inferred from stills); the pilot shows one-frame pops and typed text.
- **Scientific-diagram treatment:** `07_*`: spoken number on screen in 53 of 105 quantity moments; label is the commonest device; schematic, not to scale.
- **2D / 2.5D / 3D evidence:** none of the viewed frames shows perspective or 3D; no claim about hidden software.
- **Narration alignment:** machine only (56% vs 33 to 37% chance); listening blocked.
- **Long vs Shorts:** 38 of 40 Shorts are re-cuts; portrait recomposition; stroke 5.7 vs 6.3 px; negative space 0.77 vs 0.66.
- **Holdout validation:** `10_*`. **Independent QA: none.**

## E. Production intelligence readiness
| Element | State |
|---|---|
| Reusable original character and art system | recipe drafted (`08_ORIGINAL_ASSET_RECIPES.md`); no asset built |
| Asset design recipes and contracts | schema + 10 scene breakdowns, untested |
| Science-animation techniques | method-selection table (hypothesis) |
| Physics accuracy gates | process proven on 10 claims; 0 discrepant; lightning "two days" OPEN (definitions/original source required) |
| Script-to-scene playbook | `05_MASTER_SCRIPT_PLAYBOOK.md` v0.2 and KB draft |
| Codex/Claude workflow | design draft, untested |
| **Unclosed blockers** | listening (no audio tool); no independent or other-family reviewer; Machine A data; SRC01/SRC02 registry decision (owner); publishing the KB needs owner approval and, if a branch is wanted, an approved branch/worktree |
Knowledge-base readiness: **DRAFT usable as a research reference with the limits listed; not production-ready as a validated system.**

## F. Proof of work (all counts recomputed in this folder; no estimates)
| Item | Count |
|---|---|
| Videos inventoried | 92 (46 long, 46 Shorts), live recount 2026-11-23 |
| Videos with complete media | 88 (44 long, 44 Shorts) |
| Videos with transcripts | 83 catalog (untimed); 88 with local provisional ASR; any transcript 88 of 92 |
| Videos deeply visually examined | **1** (`9VG0yqq_PHM`, visual only, one coder, no audio) |
| Shots measured | 718 campaign rows (44 videos) + 719 audit rows (44 videos) = 1,437 rows, different detectors, disjoint videos |
| Measured visual events | 2,160 audit events (plus the campaign's own event ledgers); 74 small additions viewed; 313,650 frames machine-differenced |
| Shots viewed and coded | 108 (of 719 audit shots) |
| Visual states recorded with interpretation | pilot 109 event rows; 108 shots; 125 science frames; none of the 2,160 events |
| Audio alignments validated by listening | **0** (4,439 segments machine-aligned, provisional) |
| Science claims checked | 10 recomputed, same-model self-review (4 consistent, 3 caveat, 1 qualified, 1 open, 1 not verified; v1 "1 discrepant" withdrawn after re-check) |
| Independent reviews completed | **0** |

Review kinds: **machine analysis** (probe, ASR, ledgers, CT scan, pacing, style masks, alignment, loudness, claim arithmetic); **self-review by one model** (all viewing and coding, all documents); **human review: none; independent review: none.**

## G. Conclusions that changed in this continuation (history kept in `_v1_` files)
1. Live recount done: 92 confirmed (v1: not done). 2. ASR exists for 88, not 64; any transcript 88 of 92 (v1: 86). 3. DEEP_VISUAL is 1 visual-only video (v1: 0). 4. "7.77 and 8.44 are the same quantity" withdrawn: different units, samples, detectors. 5. No CTA: 41 of 43 (v1 playbook: 38). 6. Long script length differs by era (825 vs 632 words). 7. Boundary strength is a weak filter (64% vs 89%), not unusable. 8. Phase 3 register had 7 columns; now all directive attributes (rule-derived).

## Not done or unavailable
Listening and sync; interpretation of 611 shots and 2,160 events; faint-layer (1,585 long, 204 Short) and sub-15 px changes; the ten directive physics episodes in depth; book-illustration comparison; article correspondence; independent review; Machine A data; owner decisions (strategy pacing line, SRC01/SRC02, publishing).
