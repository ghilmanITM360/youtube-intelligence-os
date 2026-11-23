# CH001 CasuallyFinance — branch ledger (R28.3)
Branch: visual-audit/casual-finance | base/HEAD: 72afd88f (full: git rev-parse HEAD) | worktree: /Users/ghilmankhan/workprojects/visual-audit-worktrees/casually-finance
Created 2026-11-20 with owner approval ("Yes, create it"). Files copied (not moved) from main checkout; nothing committed or pushed.
MP4 source (outside Git, read-only): ~/workprojects/videos in mp3/CasuallyFinance/ (216 files, 215 unique sha)
Deep-analysed: 15 | selected next: 4 | holdout: 2 | deferred: 189 (+6 duplicates) | saturation: NOT evaluated | GO: FAILED (62/100 provisional self-score, same-video gate not passed; v6 + novel prototypes done, no independent review)
Canonical live ledger for this channel: ../AUDIT_PROGRESS.md in this worktree. Main-checkout copy is now a stale mirror; edit only here.
Done: 54 ID-less files profiled and deduped (210 unique content). Next: fix E2/E3/E4/E6; render v3; second novel-scene test.

- v10 rendered: recreation_10nEByVLya0_v10.mp4, metrics_v10.json (rows-only IoU mean 0.937). GO FAILED.

- v11: E32/E33 fixed; rows-only IoU mean 0.944; next S039, S010, S036, S057.

- v12: E34-E36 fixed; rows-only IoU mean 0.953; next S039 banknotes, S017.

- v13: E37 PARTIAL, metrics flat (0.953). Bbox-level fixes saturating; next: caption chunking E5/E12, audio timing, selected-video deep analysis, rulebook files 14/15/17-20.

- v14: E38 caption mapping fixed; caption F1 0.917, full-slice mean 0.795.

## Rulebook files
14, 15, 17, 18, 19, 20 written (2026-11-20). Honest re-score 49/100 (replaces provisional 62). Verdict NO-GO.

- 2026-11-20 T1 multi-video numeric pass (4 selected + 2 holdouts): see CHANNEL_001/21_MULTI_VIDEO_EVIDENCE.md. Holdout prediction: bg/band PASS 2/2, caption rule FAIL 0/2, cut-rate FAIL. Not deep analysis; register deep_analysis_done unchanged. Nothing committed.
- 2026-11-20 T2 numeric state extraction for 6 videos (states_*.csv, file 21). State rate 0.5-1.4/s; 3132dfa8 continuous-motion family. Accent column defective. Not deep analysis.
- 2026-11-20 OCR caption check: bottom captions in 10nE+1eTw only; 33NV/xdF8/zLv none (file 21). Caption rule family-conditional.
- 2026-11-20 novel round 2 (NS3 uncaptioned, NS4 captioned) measured with reference tools: structure PASS, pacing FAIL; score 51/100, NO-GO.
- 2026-11-20 pacing retune: NS4 state rate PASS (0.69 s), NS3 FAIL (2.67 s); cuts metric deprecated, states/s is the pacing parameter.
- 2026-11-20 NS3 retuned to 2.18 s/state (near-pass). Score 51/100, NO-GO.
- 2026-11-20 T3 per-state measurements for 33NVvWsGt9k: panel-fill family (green/orange panels, in-art dialogue text). Score 52/100, NO-GO.
- 2026-11-20 T3 per-state data for zLv, xdF8, 3132dfa8 (file 21): >=3 families. Score 53/100, NO-GO.
- 2026-11-20 NS5 family-B panel-fill render: state rate 1.87 s PASS (metric-tuned), no bottom caption PASS. Score 54/100, NO-GO.
- 2026-11-20 progress audit + gate.py (one-command family gate). NS5 credit withdrawn (panel area 10x ref). Score 53/100, NO-GO. See ../AUDIT_PROGRESS.md.
- 2026-11-20 NS5 dark share fixed (0.23 PASS; dark boxes were the cause). NS6 family-C render: pacing PASS by construction, dark share FAIL (0.52 vs 0.42). Score stays 53/100, NO-GO.
- 2026-11-20 audio_sync.py: family B state boundaries align with speech pauses (33NV 0.62 vs 0.28 chance within 0.2 s), family A do not. NS6 dark-share tuning stopped (0.26 vs 0.42). Score 53/100 unchanged, NO-GO.
- 2026-11-20 onset_sync.py: word-onset hypothesis for family A unsupported (within noise). Timing rule status written to 14. Score 53/100 NO-GO.
- 2026-11-20 pixel_iou.py/shot_f1.py: v14 strict pixel F1 median 0.879 (dil1), 0.798 (dil0) vs bbox IoU 0.974: old metric overstated. v15 banknote hypothesis refuted. Score 53/100 NO-GO.
- 2026-11-20 VISUAL QA unlocked (JPEG via Read). v16-v19: SH005 0.62->0.74, SH020 0.68->0.76, SH016 0.74->0.87, SH011 ->0.9, SH022 0.74->0.78; whole-video dil1 median 0.902. E4b/E8b/E39b/E40/E41/E42 logged. Visual inspection ALSO showed NS5 (rectangles vs ref illustrated props) and NS6 (random card montage vs ref one-subject scenes + hand-lettered captions) do NOT match; PASS credits void. Score unchanged 53/100 NO-GO.
- 2026-11-20 render_novel5.py: NS5_v2/NS6_v2 built from viewed refs (one-subject beat grammar). NS5_v2 grammar partial pass; NS6_v2 pacing 1.2 vs 0.79 s/state FAIL. Old NS5/NS6 credit void. VISUAL_QA/ holds sheets. 14 + 21 + 18 updated. Score 53/100 NO-GO.
- 2026-11-20 method audit answered (graphics = Pillow code, stand-ins, candles.json = ref-pixel geometry). Independent vision review #1 run (6/16/2 on v19; NS5 FAIL). v20 dup mask (E42b), v21-23 OCR captions + Comic regular 57 (median F1 0.902->0.95, min 0.83), v25 bedroom rebuilt. Score 53 NO-GO. Nothing committed.

## 2026-11-20 Hybrid production system (PRODUCTION_SYSTEM/)
- Reconciled: git = visual-audit/casual-finance, everything untracked, nothing committed. Kit `visual-ct-scan` installed in ~/.claude/skills; zip validate_kit.py = PASS (4 prompt hashes, 14 refs, 7 templates); installed copy is a superset (SKILL.md differs slightly). Methodology only; no kit file writes outside this worktree.
- Tools: TOOL_DECISION_MATRIX.md. Tested: Pillow engine, ffmpeg, HyperFrames (init+render PoC, 10 s 1080p in 8 s). Others NOT inspected; opuscar licence unclear; 3D/MotionClone/shorts skipped.
- Built: export_assets.py (14 transparent PNGs, code-drawn LEVEL-3, asset_registry.json), render_scene.py (JSON spec -> MP4; presets cut/pop/fade/slide, keyframes, pose switch, conveyor, reveal, counter/bars/arrow, camera, motion_fps 24, caption full-chunk layout, validator; md5-reproducible).
- Same-video proof: specs/same_video_SH001_002.json (ref f0-153). Viewed ref vs render at 6 frames: row geometry/timing and captions match; chart + money-bag art clearly weaker (need Codex assets). SH002 entry times are estimates.
- Original test ES1 (specs/original_ES1.json, productions/cf-visual-system-tests/ES1_EMERGENCY_FUND_SCRIPT.md, slop gate WARN R1/R7 only): 14.5 s, 5 shots, 435 frames. Pipeline works; art is still code-drawn.
- Codex: ASSET_INVENTORY.csv + ASSET_PROMPTS_BATCH1_FOR_CODEX.md (8 asset groups). NO images generated; import_assets.py ready to validate them.
- Score unchanged 53/100 NO-GO.
- 2026-11-20 Independent review 2: v25 11 PASS/10 PARTIAL/1 FAIL; spec renderer layout PASS, art PARTIAL; ES1 prototype-grade. Score 53 NO-GO.

## Asset pipeline repair (2026-11-21, engineering only; score unchanged 53/100 NO-GO)
- Importer bug FIXED: blanket 25% bbox rule removed. `PRODUCTION_SYSTEM/pipeline.py` + `asset_schema.json` = type-aware validation (illustration/head/rig_arm/torso/legs/earth_*), anchors, variants, duplicate IDs, clip detection, metadata (`staging_meta.json`). `import_assets.py` is now a validate-only shim.
- Workflow: staging -> `pipeline.py validate` (dry run) -> `review` (independent, bound to file SHA-256) -> `approve` (all-or-nothing, backup, atomic swap) -> `asset_registry.json`; `rollback`, `verify`. Renderer resolves `asset:<id>` / `asset:<family>/<variant>` (approved/legacy only, `render_scale` honoured); plain paths still work (ES1 render md5 unchanged).
- Tests: `python3 -W ignore -m unittest discover -s tests` = 38 OK (1 expected failure = real defect: `rig_arm_right_up` exits top canvas edge; `char_body_up` same cause).
- Real staging (31 PNGs, `reports/validation_2026-11-21.json`): 29 technical PASS, 2 FAIL (clipping). Thin limbs/torso/legs now accepted. 0 approved assets; production registry untouched (14 legacy).
- Engineering PASS on rig previews != art approval. Independent visual review: see VISUAL_QA.
- Independent review (blind, opus subagent, 2026-11-21): qcircle PASS (only one approved+registered; note: my own frame check found it font-like vs reference, so treat as weak PASS, rollback available); chart PARTIAL (colour/line weight/ratio); bags PARTIAL (colour, $); dollar FAIL (double bar, teal outline, bubble); rig PARTIAL (up-arm clipped, pose arms 40-50% short, hips pose wrong, left_up==left_point identical, hip seam); Earth FAIL (continent map, no white eyes/clouds, flame ring vs two side flames, face jumps between variants). Reviews in PRODUCTION_SYSTEM/reviews/.

## Correction checkpoint integration (2026-11-21; score unchanged 53/100 NO-GO; nothing committed)
- Schema compat FIXED: `asset_schema.json` now has explicit `rig_versions` v1 (legacy anchors neck 0/shoulder 168/hip 1032) and v2 (corrected: neck 1024,320 / shoulder 1024,454 / hip 1024,1146, measured from torso top y=320, arm roots y~437, legs top y=1145). Contract chosen per asset via `staging_meta.json` `contract` or `validate --contract`; default stays v1. New kind `rig_body` (v2 char_body: height >=50%, content at neck/shoulder/hip anchors; legacy keeps the 20% bbox rule). New families `prop_earth_flame_left/right` (min_contract v2: overlap globe, correct side, extend beyond globe edge); combined `prop_earth_flames` keeps legacy lower-edge rule under v1 and side-union rule under v2. Pose-pair anatomy checks (up must rise >=100px above shoulder, point >=250px reach, hips/down hands below waist). No pixels added, no thresholds relaxed. Registry entries record `contract`; reviews keep history (`reviews/history/`). Validate accepts single PNG files.
- Tests: 62 OK + 1 expected failure (legacy preview defect). New: RigContractV2 (10), CorrectedCharacterRig, IndependentArmPreview, CorrectedEarth. Mutation (v2 shoulder anchor altered) -> 4 failures, restored.
- Technical validation of 26 corrected + 5 heads + master (`reports/validation_2026-11-21_correction.json`): 32/32 PASS, 0 FAIL; only `prop_qcircle` absent from staging (already registered). render_scale for chart/bags/dollar recomputed to keep legacy on-screen width (0.2744/0.1264/0.1494).
- Independent review 2 (blind opus, 33 records bound to SHA, `reviews/` + `reviews/history/`): 9 PASS (master, heads neutral/worried/happy/shocked, body_down, legs, chart, dollar), 5 FAIL (hips body + 2 hips arms, left_up, left_point, earth_face_neutral = 6 FAIL incl. both hips arms), rest PARTIAL (arm shrug/point/up length + brush striation, down arms stray torso sliver, torso cap/collar, sweat head drop, bags fill, Earth ocean/mouths/faceted flames), registered `prop_qcircle` re-reviewed PARTIAL (font-like; kept, no replacement exists).
- Registered now: 10 approved (9 new + qcircle), registry verified, backup in registry_backups/. Rig NOT production-complete (arms/torso unapproved), Earth has 0 approved layers.
- Renders (scratchpad rv2/): approved-subset character (body_down + 4 approved heads via asset: refs), SH001-002 with approved chart+qcircle (bags legacy): chart matches ref, '?' visibly heavier/font-like, bag state/position still differs -> PARTIAL. Earth/rig previews = staging only. 62 tests OK +1 expected failure (legacy preview). Score 53/100 NO-GO.

## Batch 1 final-approval integration (2026-11-21)
- Closure set: 33 PNG hashes match manifest; own v2 validation 33/33 PASS (reports/validation_2026-11-21_closure.json). Technical PASS is not artistic approval.
- Independent review (claude-opus-blind-reviewer-3, hash-bound): 10 unchanged assets reused; 24 changed re-reviewed -> PASS 1 (prop_moneybag_pair), FAIL 6 (char_body_hips, rig_arm_*_hips x2, rig_torso, rig_arm_*_down x2), PARTIAL 17 (body down/point/shrug/up, arms shrug/up/point x6, Earth body/faces/flames x6, prop_qcircle candidate).
- Registered: prop_moneybag_pair (supersedes legacy). Total approved: 11. Question disc kept (candidate PARTIAL; reviewer says clear style improvement but stroke 25% thin, no top curl).
- Renders: SH001-002 (approved assets incl. bag, 154 fr), approved character (105 fr), legacy ES1 (435 fr) all OK. 62 tests OK (1 expected failure). Earth not rendered from approved layers (none approved).
- Defects for Codex: hips arms (hands on pelvis sides, elbows out, no curl hooks); torso (flanges, collar block, hard cut); down arms (stub, sliver, haze); up arms (seam, hands above head); shrug (forearms up); point (no V dip); Earth ocean patches, neutral mouth, sweat spirals, cream flame tone, flames overlap rim; qcircle thicker + top curl. Claude: regenerate truncated M_*.jpg preview strips (Codex-owned packet).
- Score stays 53/100 NO-GO. Nothing committed.

## Loop break — reference-first integration (2026-11-21)
- State: 33 candidates (hashes all match method_change/sha256.json), 11 approved registry entries → qcircle superseded with candidate 0869a58c (independent reviewer-4 PASS: disc area-ratio .990, mark .588D/stroke .054D vs ref .577/.06; old mark 17 % too tall/40 % too thick). Flames left/right/composite reviewed PARTIAL (emoji silhouette, ~5 k fringe px, hot orange). Registry verified, 65 tests OK (+1 expected fail).
- SCENE_ASSET_MATRIX.md: 22 shots mapped; **hips is used in SH008/010/012/015 → required**; Earth in SH004/018; Earth spiral-eye face, brown-hair man, calendar icon missing from library. Reference-critical approved 7/16; full library 11/33 IDs registered (10 match current files).
- specs/make_sameVideo_full.py → same_video_full_progress.json (22 shots, 1660 frames, captions from OCR, registry refs only, labelled stand-ins/blocked slates) rendered to RENDERED_OUTPUTS/cf_full22_progress_v3_standins.mp4. Verified: 2/22 shots match (SH001-002).
- Motion evidence: stepped, runs ≤4 frames; SH018 = 2-state whole-Earth boil every 10 frames (no fade/flicker). Hips landmarks measured; rig contract v2 shoulder anchor (16 %) conflicts with SH010 (31 %).
- Score unchanged 53/100 NO-GO. Nothing committed. Codex handoff: PRODUCTION_SYSTEM/CODEX_CRITICAL_HANDOFF.md.


## Geometry correction & rig contract v3 (2026-11-21)
- Landmarks measured on SH004/008/010/012/015 (12+ frames); torso shoulder offset 29 % (v2 said 16 %) -> rig contract v3 added alongside v1/v2 (`asset_schema.json`, pipeline kind/legs/pose-rule support, `tests/test_rig_v3.py`). Hips hands stop at 54-55 % of torso; hips are static within each shot (SH008 = right-arm variant B).
- Found two further spec errors: approved `rig_legs` geometry (601 px tall) does not match the reference legs (~258 px, splayed) and approved `char_head_*` are the brown-haired character, not the black-haired man of SH008-SH022. Reference-critical approved-and-matching assets: 4 (not 7).
- One hips prototype (body+head, A and B) drawn from landmarks; 99.8 %/96.7 % ink agreement within 3 px at 1080x1920 playback scale (`PRODUCTION_SYSTEM/rig_measurements/prototype/sheet.png`); layers pass v3 validation.
- New `CODEX_CRITICAL_HANDOFF.md` (v2; v1 kept as `_v1_superseded`), `THIRD_PARTY_PROVENANCE_REGISTER.csv` (11 shots), SH018 two-state boil + procedural pose overrides in `render_scene.py` (+test), render `RENDERED_OUTPUTS/cf_full22_progress_v4_boil.mp4`. 70 tests OK (1 expected failure). Score stays 53/100, NO-GO; nothing committed; no registry change.

## Complete-sprite route for observed static/stepped shots (2026-11-21, after owner directive "stop rig/Earth perfection loop")
- Whole-figure/state sprites drawn from measured geometry in `PRODUCTION_SYSTEM/shot_sprites/` (hips A/B x expression, SH018 Earth A/B, SH004 man + Earth A/B, calendar, arrow, bare $, SH003 bubble + burst). Not registry assets, not a rig; manifest + hashes in `shot_sprites_manifest.json`. Reusable rig stays a separate milestone.
- Render: `RENDERED_OUTPUTS/cf_full22_progress_v7_sprites.mp4`. Independent review v2 (`shot_sprites/reviews/independent_review_v2.json`): SH003/004/008/010/012/015/017/018 PARTIAL, SH005 FAIL (font + uneven scroll steps). Calendar and arrow sprites PASS; other 11 sprites PARTIAL.
- Known open defects: hips hair solid block (no scribble), year font (thin handwriting not matched), SH003 bubble starts ~5f early/steps, SH004 slide and SH017 scroll easing, Earth shading/outline weight, SH018 eyes ~20% narrow. Caption OCR has >8-frame gaps at ~70 places.
- Also found: approved prop_dollar_sign = in-bubble composite, not the bare $ of SH003. Score unchanged 53/100 NO-GO; nothing committed; registry untouched.
