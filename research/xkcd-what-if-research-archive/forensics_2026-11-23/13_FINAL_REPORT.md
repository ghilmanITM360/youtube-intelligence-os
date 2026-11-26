# 13 Final report v4: xkcd What If? complete forensics (v3 kept as `versions_before_reconcile_2026-11-23/13_FINAL_REPORT.md`; v4 written 2026-11-23 after reconciling the Codex independent review and the supplied external audit)

**Status: NOT a finished or independently validated research system. IN PROGRESS: the folder name says "complete forensics" because that was the directive's title, not a completion claim.** Against the directive (`Pasted text(20261123-055514).txt`, 973 lines, SHA-256 `e38230526627e27b49c0f09c44dcac2cdba63fbcfe773c0f7370607d72668dc7`): 4 of 14 phases COMPLETE (0, 1, 2, 5; self-reviewed), 10 PARTIAL, 0 NOT STARTED (COMPLETE only when every substantive requirement is met at the stated review level). Review kinds: machine analysis; same-model self-review; **one partial independent review by a different tool (Codex, 2026-11-23: no expert, no listening, no video played, sample-only checks)**; human review none; listening none. Repo state at the last check (2026-11-23 about 11:2x UTC): branch `research/what-if-channel-strategy-2026-11-18`, HEAD `a0c0391c5d45ab7c2443fc054f2e22d7747f8261`; three untracked What If planning files from another session are not mine; this work made no git writes, no branch switch, no commit, no push, no media change. Earlier versions: `_v1_`, `_v2_`, `versions_before_reconcile_2026-11-23/`.

## Phase 0 to 13 status against the directive (detail and criteria: `14_RECONCILIATION_CODEX_AND_EXTERNAL_AUDIT_2026-11-23.md` section 4)
| Phase | Done (evidence) | Status | Remaining and limits |
|---|---|---|---|
| 0 | `00_PHASE0_WORKSPACE_STATE.md`; repo rechecked after Codex noted HEAD movement | COMPLETE | self-review; output path is the existing `Documents/YIOS-local-audits/<date>-...` pattern, not the directive's `~/YIOS-local-audits/...` suggestion |
| 1 | `01_*` (25 claims) | COMPLETE | self-review; Codex did not audit it |
| 2 | `02_*`, 83 of 83 audits verified | COMPLETE | self-review; audit prose not re-judged |
| 3 | 10 folders; register with all attributes | PARTIAL | attributes rule-derived from path and hash, not per-file inspection |
| 4 | live recount 92 (46 + 46); inventory v2; 88 SHA-256 recomputed 2026-11-23 (88 match) | PARTIAL | article correspondence 0 verified; unlisted videos cannot be excluded; 14 older encodes not byte-compared |
| 5 | `05_*` | COMPLETE | stability check, not a preregistered holdout; not independently checked |
| 6 | 6.1 coverage matrix; 6.2 style (125 + 160 frames); 6.3 motion: 16 dense sequences + pilot; 6.5 pacing; 156 shots viewed | PARTIAL | **6.4 "every scene" NOT met** (`14_COVERAGE_PLAN_AND_SCOPE.md`); 563 shots and 2,160 events uninterpreted; no book comparison |
| 7 | 10 claims (v3 counts 4/2/2/1/1/0) + ten episodes (51 rows, TARGETED_VISUAL) | PARTIAL | same-model arithmetic; Codex re-derived SC02, SC03, SC05, E09g only; no expert; M-coded constants not fetched |
| 8 | `08_*` recipes, schema, 10 scenes | PARTIAL | proposals only, untested |
| 9 | machine alignment, loudness, silence; 25 listening items prepared | PARTIAL (blocked) | listening 0; ASR provisional |
| 10 | H1 to H9 reclassified (`10_*`); topic-family stability check preregistered, 20 of 20 judged cells pass | PARTIAL | not independent holdouts; no listener-validated sync; independent QA only the partial Codex review |
| 11 | `knowledge_base_draft/`: 14 documents + 23-rule ledger; operative text of 22 rules revised (K06, K10, K11, K16, K20, K22 ...) | PARTIAL | draft inside the audit folder; not published |
| 12 | `12_CODEX_CLAUDE_WORKFLOW.md` + review-loop addendum | PARTIAL | design only |
| 13 | this report | PARTIAL | the research it reports is unfinished |

## A. Existing research audit (`research/what-if-channel-strategy/`, branch-only)
Detail: `01_*`. 25 claims: VERIFIED 11, MEASURED 3, OBSERVED 3, INFERRED 3, UNVERIFIED 3, CONTRADICTED 1 (2026 long durations are 2:42 to 4:38, not 2:43 to 3:33), SUPERSEDED 1 (C17, later re-rated PARTIAL: the 7.77 s shot median is valid only as a Brain shot median, see `06_PACING_CORRECTION.md`). C02 updated: 83 catalog transcripts, 5 provisional ASR, 4 without media. Qualified: "no CTA" holds for wording only (a red book-promo end card closes 44 of 44 long videos). Useful for production: catalog numbers, IP boundary, honest labelling. Not usable: any xkcd visual statement beyond the 14-video Brain.

## B. Local data discovery
Detail: `02_DUPLICATES_AND_PROVENANCE.md`, `02_LOCAL_WORKSPACE_INVENTORY.csv`, `02_WHAT_IF_RELATED_FILE_REGISTER.csv`, `02_MEDIA_AND_TRANSCRIPT_AVAILABILITY.md` (all corrected). Key facts: library `YIOS-Media-Library/xkcd Channel/` holds 88 MP4s (hash equal to the census for 88 of 88, 0 duplicate hashes); the older Brain source folder holds 14 MP4 encodes (0 of 14 hash-equal; same logical videos); 3 competitor MP4s; 1,371 What If-related candidate files across 7 of the 10 audited folders; offline-map-audits excluded. Missing: 4 videos, Machine A data, SRC01/SRC02 registry IDs (candidates `rGZ6TsXvi8E`, `TIDHee_Q5Gk`; owner decision).

## C. Repository audit
Branch and status as above. The strategy folder exists only on this branch (not on `origin/main`); `research/what-if-scripts` (83 audits, 41 files) and the campaign `research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww` (manuals v0.1 to v0.7, 44 per-video ledgers) are on `main`. Transcript coverage 83 catalog + 5 ASR; media 88 of 92.

## D. Visual forensic report
- **Coverage (logical IDs, `03_CORPUS_COMPLETENESS_REPORT.md`):** DEEP_VISUAL 1 (visual-only), TARGETED 43, STRUCTURAL 44, UNAVAILABLE 4. Machine-measured: 88 of 88 (every frame, CT machine stage). Sampled and viewed: 125 science frames (82 videos), 156 shots (44 videos), 1,632 residual runs (88 videos). Kept as three separate statuses.
- **Editing rhythm:** see `06_PACING_CORRECTION.md`: event gap about 2.1 s and 22 events per minute replicate across 44 + 44 disjoint videos; shot median 8.4 s (campaign) vs 6.7 s (audit detector); about 93% of frames are holds.
- **Character construction and style:** `06_STYLE_ANALYSIS_PHASE62.md`, `11_RULE_AUDIT_2026-11-23.csv`: ring head, line body (height about 3.5 x head, n=28), thin line about 6 px, mostly achromatic palette with a red accent in 31% of 125 frames; **exceptions**: 20 of 160 further frames have more than 5% chromatic pixels (9 in the rotated-world episode); other characters (child, reporter, helmeted figure, cat) exist beyond the base figure; negative space 0.66 and 0.77.
- **Motion grammar:** pop-ons, scene swaps and write-ons dominate (earlier campaign labels, not re-verified); camera-like moves exist: 15 of the 16 shots flagged from stills were **confirmed in 9-frame sequences at 0.25 s steps** (map pan/zoom with motion blur 8, wide-composition slide 1, film-strip scroll 1, diagram transition with a blurred smear and swinging-chain overlay 3, continuous scale-down through nested drawings 2; 1 was a hard cut); their frequency across the channel is unmeasured; the pilot shows one-frame pops and typed text.
- **Scientific-diagram treatment:** `07_*`: spoken number on screen in 53 of 105 quantity moments; label is the commonest device; schematic, not to scale.
- **2D / 2.5D / 3D evidence:** no 3D rendering was observed in stills or in 16 short sequences (depth cues were 2D pan, zoom, blur, scale-down); no multi-plane parallax identified; the absence of 3D or parallax channel-wide is NOT established; some hand-drawn perspective objects and gradients or glows exist; no claim about hidden software.
- **Narration alignment:** machine only (56% vs 33 to 37% chance); listening blocked.
- **Long vs Shorts:** 38 of 40 Shorts are re-cuts; portrait recomposition; stroke 5.7 vs 6.3 px; negative space 0.77 vs 0.66.
- **Holdout validation:** `10_*` (reclassified: most tests are stability checks); topic-family stability check passed 20 of 20 judged cells. **Independent QA: one partial review by a different tool; no expert; no validation of the visual coding.**

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
| Shots viewed and coded | 156 of 719 audit shots (23.1% of the 675 with a boundary); 16 of them also as 9-frame sequences; **descriptive counts of a stratified, clustered, non-random sample, not channel rates** |
| Visual states recorded with interpretation | pilot 109 event rows; 156 shots; 125 science frames; 160 ten-episode frames; none of the 2,160 events |
| Audio alignments validated by listening | **0** (4,439 segments machine-aligned, provisional; 25 items prepared for a listener) |
| Science claims checked | 10 recomputed (v3: 4 consistent, 2 caveat, 2 qualified [SC02, SC05], 1 open [SC03], 1 not verified; v1 "1 discrepant" withdrawn) plus 51 rows over the ten directive episodes (19 consistent, 13 caveat, 8 qualified, 7 not verified, 2 supplementary, 1 open, 1 discrepant as stated), all same-model self-review |
| Independent reviews completed | **1 partial** (Codex, different tool; scope: counts, 5 rule verdicts, 4 science rows, 4 contact sheets; no expert, no listening); validation by an independent reviewer of the visual coding or the rules: **0** |

Review kinds: **machine analysis** (probe, ASR, ledgers, CT scan, pacing, style masks, alignment, loudness, claim arithmetic); **self-review by one model** (all viewing and coding, all documents); **human review: none; independent review: none.**

## G. Conclusions that changed in this continuation (history kept in `_v1_` files)
1. Live recount done: 92 confirmed (v1: not done). 2. ASR exists for 88, not 64; any transcript 88 of 92 (v1: 86). 3. DEEP_VISUAL is 1 visual-only video (v1: 0). 4. "7.77 and 8.44 are the same quantity" withdrawn: different units, samples, detectors. 5. No CTA: 41 of 43 (v1 playbook: 38). 6. Long script length differs by era (825 vs 632 words). 7. Boundary strength is a weak filter (64% vs 89%), not unusable. 8. Phase 3 register had 7 columns; now all directive attributes (rule-derived).

## H. Changes after the independent-audit request (2026-11-23, third pass; history in the `_v1_`, `_v2prelight_` and `_before_v3` files)
1. **The audit file `WHAT_IF_INDEPENDENT_AUDIT.md` named in the request was not found** on this machine (searched Documents, Downloads, Desktop and the session folders; a different project's audit exists). Only its lightning point, as quoted in the request, was addressed; nothing else from it was reconciled.
2. **SC03 lightning**: "DISCREPANT" withdrawn, now OPEN (definitions and original source required). The video's three lines agree with each other at 126 to 132 MJ per strike; the sources give per-flash totals; no source separates delivered, ground or recoverable energy; What If #16 has no figure (`07_SC03_LIGHTNING_REWORK.md`). Sub-check SC03B ("several million years") is an internal tension, not verified.
3. **SC05 magnitude 25** is relation-dependent (the Sun result flips under the USGS rough relation); the 6.9e41 J binding energy used in v1 was not supported and is dropped.
4. **Ten directive episodes**: all ten matched to video IDs and available locally; 51 rows rechecked; one **discrepant as stated** (E09g, "5 petawatts, double the world's electricity" is about 1,500x), which the original article repeats; spoken, captioned and drawn values compared (E01c, E02b, E09a, E07d); auto-caption and ASR unit errors found ("paws", "terowatt", "soil").
5. **23 rules audited**: numbers recomputed from the cited files; K06 corrected (Whisper start 0.00 s is an artefact; audio energy within 0.5 s measured by waveform), K10 exceptions (colour maps and heat scenes), K22 updated to 156 shots; ledger carries `audit_label_2026_11_23`.
6. **Shot review batch 4**: 48 more shots (156 of 719 viewed), true-cut rate 76% (0.69 to 0.82), strength pattern replicated, 16 camera-move inferences, new observations (red title card after the question beat at 9 to 19 s, static ending of a Short, overlays and counters as false-boundary causes).
7. Not changed: no listening, no independent reviewer, no commit, no branch switch, no push, no new video; the knowledge base remains a research draft.

## Not done or unavailable
Listening and sync (see `09_LISTENING_PRIORITY_ITEMS.csv` for the lines that matter most); interpretation of 563 shots and 2,160 events; faint-layer (1,585 long, 204 Short) and sub-15 px changes; deep study of the ten directive episodes (they are sampled and viewed only); the originals of five of the ten episodes (no archive title match); book-illustration comparison; article correspondence; independent review; Machine A data; confirmation of M-coded constants; owner decisions (strategy pacing line, SRC01/SRC02, publishing).


## I. After the Codex review and the external audit (2026-11-23, fourth pass; full table `14_RECONCILIATION_CODEX_AND_EXTERNAL_AUDIT_2026-11-23.md`)
**Accepted (AGREE): F01 (directive now supplied), F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12. Partly accepted: F13 (rules still only partly independently checked), F14 (hashes now 88 of 88; raw campaign ledgers and older encodes not re-verified). Disputed: none. Unresolved: audio-dependent items (K06 speech onset, SC03 and E09g wording as spoken), expert physics review.**
1. **Operative wording fixed.** The `rule` column that a production agent reads now carries sample, selection and limits for 22 of 23 rules (old text kept in `rule_text_prior_v3`); K06 no longer says narration starts at 0 s (audio energy within 0.5 s; speech onset UNVERIFIED); H2 split into four quantities; K10 and K20 carry the exceptions; K16 became "camera-like moves exist, frequency unmeasured".
2. **Shot statistics.** Wilson intervals withdrawn as channel statements; sample counts, design table, post-stratified 78.4% and video-cluster bootstrap 71.9 to 85.1% given as sensitivity only; recall explicitly not inferred.
3. **Science.** SC02 QUALIFIED (5.953 g; self-compression not modelled); SC03 stays OPEN; SC05 toy extrapolation; E09g recorded as an article-and-ASR wording discrepancy (5 PW is about 1,900 to 2,250 times 2012 average world electricity, not 2x; the earlier 1,486x used a 2023 figure); intended correction not inferred; audio not heard.
4. **New work.** 16 motion sequences viewed; 88 hashes recomputed; preregistered topic-family stability check; coverage plan for 6.4 and the remaining shots and events; listening pack of 25 items; Codex/Claude review-loop requirement.
5. **Corrections to my own earlier numbers found on the way:** K11 stroke sample is 94 frames (63 + 31), not 93; Short silhouette exclusions 7, not 8; "21.7% viewed" is 23.1% of shots with a boundary.
6. **Not done:** no listening; no expert; 563 shots and 2,160 events uninterpreted; originals of five of ten episodes not compared; book art not compared; article correspondence 0 verified; M-coded constants not fetched; Machine A data; owner decisions (SRC01/SRC02, publishing, whether 6.4 must be literal).

## Knowledge-base readiness
**Research draft, usable as a research reference with the documented limits. Not independently validated. Not production-ready.**

## J. Literal Phase 6.4 (owner decision 2026-11-23: "Literal chahiye"), progress
Scope: all 1,437 ledger shots (719 audit layer + 718 campaign layer), 14 questions each (`phase15_scene_coding/CODEBOOK.md`). **Done: tranche A = the ten directive episodes, 260 shots (18.1% of scope), same-model subagent self-review from 3 stills per shot, validated by script, 6-shot spot-check consistent, 20 of 21 boundary types agree with the earlier review** (`phase15_scene_coding/A_ten_SCENE_CODING.csv`, `PROGRESS.md`). **Not done: tranche B (594 shots) and C (583 shots).** Phase 6.4 is therefore still NOT MET; the ten-episode study moves from TARGETED_VISUAL sampling to shot-level coding of every shot of those ten episodes, still stills-based, still self-review, still no listening. Counts above in this report that say "156 shots viewed" refer to the earlier review; tranche A adds coded shots (125 + 135) without changing those numbers.
