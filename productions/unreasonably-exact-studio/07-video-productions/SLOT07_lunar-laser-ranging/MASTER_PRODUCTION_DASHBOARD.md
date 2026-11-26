# MASTER PRODUCTION DASHBOARD (GENERATED; the one source of truth)

Generated 2026-11-26 15:36 by `python3 tools/build_dashboard.py` from files on disk and `qa/work_items.csv`, `qa/asset_status_overrides.csv`, `qa/proof_register.csv`. **Edit those, not this file.** Other documents (START_HERE, PRODUCTION_PLAN, PROGRESS_LOG, ORIGINAL_BRIEF_COMPLIANCE_AUDIT, CODEX_HANDOFF) carry no status tables: they point here.

## Measured facts (counted by the script)

| Fact | Value |
|---|---|
| Files in project tree | 1624 |
| Reference manifest entries | 173 (astronaut 28, diagrams 12, earth 28, moon 21, observatory 23, optical 22, reflector 14, stopwatch 11, telescope 14) |
| ...with a local file | 150 |
| ...marked viewed (opened) | 149 viewed, 24 not viewed |
| Animation examples | 25 (FRAME_SAMPLED 6, METADATA_ONLY 19) |
| Planned production assets (non-group) | 68 (Codex 34, Claude 34) |
| Codex briefs on disk | 34 |
| Generated production artwork files (Codex deliveries, PNG) | 27 |
| Validated rigs | 0 |
| Proofs with an MP4 on disk | 16 of 13 |
| Asset generation_status | CANDIDATE 11, N/A 4, PLANNED 52, RESEARCHED 1 |

## Completed (20)

| ID | Area | Item | Evidence | Next executable task |
|---|---|---|---|---|
| W01 | narration | Transcript; word/phrase/sentence times; pauses: OFFICIAL V2 take 95.39 s (SHA 3800dfce...); V1 92.53 s kept in narration/v1_historical | narration/NARRATION_TRANSCRIPT.md ; narration/WORD_TIMESTAMPS.json ; narration/raw_v2/SHA256.txt | human listen (W19) |
| W02 | narration | 40-beat map and narration-to-visual map rebuilt on V2 (drift up to +3.7 s vs V1) | narration/NARRATION_BEAT_MAP.csv ; narration/NARRATION_TO_VISUAL_MAP.csv | validate real visual events against rendered frames in the full film |
| W03 | science | Claims ledger: 13 claims all closed | SCIENTIFIC_CLAIMS_LEDGER.csv ; SCIENTIFIC_RESEARCH.md | none |
| W04 | planning | Text storyboard + 120 panels + 10 scene sheets (placeholder composition) | storyboard/FULL_VISUAL_STORYBOARD.md ; storyboard/panels/S01_the_question.png | replaced for look by look-dev and animatic V1 |
| W05 | planning | Asset manifest (79 rows: 68 assets + 11 groups) and dependency graph | MASTER_ASSET_MANIFEST.csv ; ASSET_DEPENDENCY_GRAPH.md | keep in sync via tools/build_manifest.py |
| W06 | standards | MASTER_STANDARDS_CROSSWALK.md mapping both guides to actions and evidence | MASTER_STANDARDS_CROSSWALK.md | none |
| W07 | handoff | 34 Codex briefs regenerated with 16 mandatory fields and assembly diagrams | codex_handoff/individual_asset_briefs/ASTRO_001_HELMET.md ; codex_handoff/ASSEMBLY_DIAGRAMS.md | re-run tools/build_handoff.py after reference merge |
| W10 | research | Professional animation study: 18 segments (9 frame-sampled via ffmpeg; 9 browser seek-sampled; 3 audio-level rows; none watched end to end; no audio heard) | research/video_analysis/PROFESSIONAL_ANIMATION_STUDY.md ; research/video_analysis/SEGMENTS_STUDIED.csv | fold the 15 STYLE_BIBLE rules into look-dev and the cut |
| W15 | codex | Codex contacted via CLI (GUI computer-use unavailable) and Batch 0 run | codex_handoff/deliveries/batch0/ARTWORK_QA.md | Batch 0b running |
| W21 | human | Owner approves art: owner visual acceptance of the V3 film (2026-11-26, chat). Covers the art as seen in V3, not every asset for every future use | OWNER_ACCEPTANCE_RECORD.md | none for Slot 07 |
| W27 | pipeline | Calibration decisions: native generation ~1254 px; sprite instancing instead of 100 identical objects; large maps from public-domain NASA sources | qa/BATCH0_REVIEW.md | apply to Earth/Moon briefs before Batch 1 |
| W28 | research | Reference gap closure: 37 new entries (35 viewed images) merged; 173 refs total; 8 exact duplicates removed from the active handoff; GAP_AUDIT 116 rows (63 COVERED / 44 PARTIAL / 9 GAP); .tmp fragments resolved | research/asset_research/GAP_AUDIT.csv ; research/REFERENCE_MANIFEST.csv ; research/redundant_refs.csv | 9 gaps remain open (kneel/align photo; clean poles; dome-opening sequence; histogram figures) listed in GAP_CLOSURE_REPORT.md |
| W30 | narration | New narration V2 ingested: checksum, decode, comparison (same 245 words), DP aligner fix | narration/NARRATION_TRANSCRIPT.md ; tools/align_slot07.py | none |
| W31 | codex | Root-cause audit of Batches 0-2 + new single-deliverable protocol (effort high, -i refs, view_image evidence) | ASSET_GENERATION_FAILURE_ROOT_CAUSE_AUDIT.md | apply rules R11-R14 in every brief |
| W33 | pipeline | Bug fixed in shared canvas.blit_image (uninitialised memory around bitmaps); regression check in selftest | animation/uemotion/canvas.py ; animation/selftest.py | none |
| W34 | assets | Claude procedural cloud layer REJECTED (visual + role); replaced by Claude composite of Codex tiles | assets/earth/earth_clouds_codexcomp_4096x2048_report.json | none |
| W35 | opening | Three opening treatments rendered (A/B/C) and A selected | renders/proofs/OPEN/OPENING_SELECTION.md | owner G2 review of the opening |
| W37 | qa | Shot-by-shot visual explanation audit (40 beats) + defect register | SHOT_BY_SHOT_VISUAL_EXPLANATION_AUDIT.csv ; qa/DEFECT_REGISTER.csv | fix D06-D09 |
| W38 | art | Visual consistency sheet; style question resolved by the owner accepting the V3 look (painterly-clean realistic) | OWNER_ACCEPTANCE_RECORD.md | none |
| W39 | edit | V3 film (96.000 s, 2880 frames): opening, 0:59 redesign, disclosures, music mix; designated the OWNER-SELECTED FINAL PRODUCTION VERSION (no V4) | renders/roughcut_v3/FINAL_PRODUCTION_QA.md ; OWNER_ACCEPTANCE_RECORD.md | none |

## In progress (0)

(none)

## Failed (2)

| ID | Area | Item | Evidence | Next executable task |
|---|---|---|---|---|
| W14 | animatic | ANIMATIC_V0 placeholder kept for timing only; ends before the audio (video 92.47 s vs audio 92.53 s); never approved artistically | storyboard/ANIMATIC_V0_NOTES.md | superseded by V1 |
| W25 | codex | Batch 0 RETRO_002: Codex self-reported BLOCKED (1254 px native; no layers; alpha/edge fails); hashes verified; image viewed; review written | qa/BATCH0_REVIEW.md | Batch 0b with revised method (plate + face sprite + native macro) |

## Blocked (0)

(none)

## Candidate (9)

| ID | Area | Item | Evidence | Next executable task |
|---|---|---|---|---|
| W11 | animation | uemotion library + proofs P07-P13 RETIMED to V2 (NAR.v1 word-edge warp; P08 equal slow factor re-solved); real Earth/Moon textures; P13 on Codex lunar plate + registered Codex array; 51/51 checks PASS; reviewed as decoded frame sequences (not real-time) | renders/proofs/P13/PROOF_REPORT.md ; qa/render_v2c_P08-P13.log | owner watches in real time; P13 push-in strobe (max frame step ~35/255) still open |
| W12 | art direction | Vision card + 3 look-dev treatments (18 panels; stills only) + decision: treatment C hybrid chosen (decision by the look-dev worker; owner has not approved) | look_dev/VISION_CARD.md ; look_dev/LOOKDEV_DECISION.md ; look_dev/panels/comparison_sheet.png | owner approval of the visual language |
| W13 | animatic | ANIMATIC V1 retimed to the V2 take by inverse word-edge warp (new file; V1 file kept) | storyboard/animatic/ANIMATIC_V1_RETIMED_V2_TAKE.mp4 ; tools/animatic_v1.py | owner watches at phone size (G2) |
| W17 | assets | Codex artwork: masters for lunar env (B3M), observatory (B4M), astronaut (B5M); retro side view (R2a); arm layers (B5L); cyclone variants (B1c). 2 rejects (R2b, B5L2) | qa/asset_tracker.csv ; codex_handoff/runs/ | B4L observatory layers review; shoulder cap on tight canvas; lunar prop sprites |
| W18 | rigs | Rigs: RIG_001 globe (P01/P02); RIG_002 observatory (P03/P04 PASS); RIG_003 astronaut v2 shoulder skinning (P05 PASS); astronaut+reflector interaction (P06 PASS) | renders/proofs/P04/PROOF_REPORT.md ; renders/proofs/P05/PROOF_REPORT.md ; renders/proofs/P06/PROOF_REPORT.md | owner art approval; real-time review |
| W26 | codex | Batch 0b RETRO_002: Codex parts (plate with 100 measured recesses; 3 face discs; native macro) all self-reported blocked; hashes verified; contact sheet viewed; Claude assembled 100 instances (assets/retro/) | codex_handoff/deliveries/batch0b/ARTWORK_QA.md ; assets/retro/retro_array_assembled_1254.png | Batch 1 (clouds/atmosphere slice/pole caps); Claude builds Earth/Moon base textures from public-domain NASA maps |
| W29 | codex | Batch 1 delivered (4 cloud tiles; 3 atmosphere-slice layers; 2 polar patches); Codex self-reported blocked (grey relief in cloud alpha; RGB under zero alpha in 8 files; sizes 1672x941/1774x887 exceed ~1500 limit; polar geography uncertified); hashes verified; contact sheet viewed | codex_handoff/deliveries/batch1/ARTWORK_QA.md | Claude: clean alpha and test tiling; register polar patches against NASA base map |
| W32 | animation | P01 Earth rotation/lighting and P02 Earth-Moon parallax rendered on validated textures; all checks PASS | renders/proofs/P01/PROOF_REPORT.md ; renders/proofs/P02/PROOF_REPORT.md | owner real-time review |
| W36 | edit | Full rough cut V1 (96 s) with captions and procedural sound mix | renders/roughcut/ROUGH_CUT_V1_final.mp4 ; renders/roughcut/mix_report.json | human listening + real-time viewing + muted viewer test |

## Validated (automated evidence) (2)

| ID | Area | Item | Evidence | Next executable task |
|---|---|---|---|---|
| W08 | handoff | Automated brief path audit (every section-2 path exists; every brief has a tagged reference) | qa/handoff_audit.txt | re-run after reference merge |
| W40 | package | Final package verified self-contained: rebuild check after the 2026-11-26 move (19 frames, mean abs diff 1.38-1.88/255 vs the locked clean render, 0 files opened outside the project except the Python env and macOS fonts); music copied into audio/music/ | qa/REBUILD_CHECK_2026-11-26.json ; REBUILD_INSTRUCTIONS.md ; FINAL_PACKAGE_MANIFEST.md | none |

## Requires human verification (an agent cannot close these) (7)

| ID | Area | Item | Evidence | Next executable task |
|---|---|---|---|---|
| W19 | human | G1 a human listens to the whole narration take against the script | - | owner |
| W20 | human | G2 owner watches the animatic at phone size and approves | - | owner |
| W22 | human | Human listening to the final mix (headphones and phone speaker) | - | owner |
| W23 | human | Real-time playback of the final film and owner acceptance: VISUAL acceptance recorded 2026-11-26 (owner, chat); listening, licence and technical publication checks stay open (W22, W41) | - | owner: listening (W22) and licence (W41) before any publication |
| W24 | human | Comprehension check: picture-only and voice-only lead to the same conclusion | - | owner or a reviewer |
| W41 | rights | Small_Variables.mp3 licence or ownership evidence. Until it exists only the RIGHTS_CLEAR master may be published | - | owner supplies licence/ownership evidence |
| W42 | publication | Publication checks: listening (W22), licence (W41), Shorts-UI caption overlap test on a phone, muted-viewer test (W24), final title/description; nothing uploaded | - | owner |

## Planned / not started (1)

| ID | Area | Item | Evidence | Next executable task |
|---|---|---|---|---|
| W16 | codex | Codex independent reference research per batch | - | required in each batch RESEARCH_NOTES.md |
