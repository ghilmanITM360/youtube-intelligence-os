# Progress log (append-only, newest at the bottom)

Purpose: any Claude or Codex session can resume from here after a limit or compaction. Entries say what exists on disk, not what was intended.

## 2026-11-26: recovery from the owner audit
- Owner settled: voice = timing reference, C06 keep + picture rule, B29b keep, non-scale schematic allowed, research and Codex coordination authorised. Human listen (G1) still NOT PERFORMED.
- Written: `ORIGINAL_BRIEF_COMPLIANCE_AUDIT.md`, `research/REFERENCE_PROTOCOL.md`; decisions recorded in `PRODUCTION_PLAN.md`, `START_HERE.md`, `tools/build_manifest.py`.
- Launched four background research agents (earth+moon, astronaut+reflector, observatory+telescope, optical+stopwatch+diagrams+animation). Output locations: `research/real_world_references/<family>/`, `research/reference_fragments/<family>.json`, `research/asset_research/<FAMILY>_RESEARCH.md`. Not merged or verified yet.
- Network facts: images-api.nasa.gov, svs/science.nasa.gov, ilrs, apo.nmsu, xkcd reachable from the shell; commons.wikimedia.org does not resolve (en.wikipedia API works).
- Wrote `SCIENTIFIC_VISUAL_DESIGN.md` (13 concepts, each with the 7 required fields + muted test).
- Built `tools/animatic.py` + `tools/boards.py`: ANIMATIC V0 (`storyboard/animatic/ANIMATIC_V0_540x960_15fps.mp4`, placeholders, master audio) and 10 scene sheets + 120 panels in `storyboard/panels/`. Inspected as stills only (not watched). Findings in `storyboard/ANIMATIC_V0_NOTES.md`. Stopwatch/pulse slow-motion rule corrected in the manifest rows. Known TODO: re-mux with tail padding (video ends at 92.47 s, audio 92.53 s; intended 94 s with fade).
- Reference agents running; browser video pass by the main session still to do.
- Earth+Moon agent finished: 30 saved refs (16 earth, 14 moon) + 5 link-only, 9 animation examples (3 FRAME_SAMPLED from public-domain SVS videos). I opened one image to spot-check its description: it matched. Applied its conflicts: poles must be repainted (EARTH_001), clouds authored (EARTH_002), MOON_002 is low-albedo but HARD-lit, phase rule (gibbous, lit upper-left; Moon in the ground view = waning gibbous) added to `codex_handoff/PRODUCTION_ART_DIRECTION.md`.
- Main-session browser pass: 2 YouTube videos seek-sampled (SED73, APO documentary), evidence + honest limits in `research/video_analysis/BROWSER_REVIEWS.md`.
- Wrote handoff docs: START_HERE, PRODUCTION_ART_DIRECTION, CHARACTER_CONSISTENCY_GUIDE, RIGGING_REQUIREMENTS, SCIENTIFIC_ACCURACY_REQUIREMENTS, ASSET_ACCEPTANCE_TESTS, ../CODEX_HANDOFF.md; generators `tools/merge_references.py`, `tools/build_handoff.py` (briefs, prompt bible, reference copies), `tools/build_atlas.py`. Briefs regenerate when more fragments land.
- Still running: astronaut+reflector, observatory+telescope, optical+stopwatch+diagrams agents.

## 2026-11-26 astronaut + reflector merged
- astronaut (15 saved) and reflector (13 saved) fragments merged: 63 refs total, 17 animation examples (13 METADATA_ONLY, 4 FRAME_SAMPLED; none newly WATCHED).
- Spot-checked by viewing: AS11-40-5874 (side profile, flat PLSS + antenna: description correct) and AS11-40-5952 (tilted dark-glass array, silver aluminium box, white-bright base: description correct).
- Open conflicts to apply to manifest/briefs: RETRO_002/004 "dark frame" is wrong (silver box, white base, dark glossy glass face); RETRO_000 46 cm vs UCSD 0.45 m; RETRO_001 "behind the PSEP" is viewpoint-dependent; B21 exit ray is parallel but OFFSET, not collinear; B18/ASTRO_010 kneel-and-align has no photo evidence (stylised pose, name no astronaut); suit frames A7L (Apollo 11/14) vs A7LB (16/17, pose and dust only).
- REF-RETRO-013 (SP-214 PDF) is viewed=false: kept as honest WARN.
- Still running: observatory+telescope, optical+stopwatch+diagrams agents.

## 2026-11-26 observatory + telescope merged
- observatory 16 saved + 4 link-only (Wikimedia 429s), telescope 10 saved + 3 link-only; both fragments merged. Two ESO time-lapses FRAME_SAMPLED, others METADATA_ONLY.
- Conflicts to apply: TEL_002 draw order (40) vs OBS_002_DOME (40) / OBS_006_DOME_SLIT (41): telescope would paint over dome shell unless masked; TEL_002 "fork arms" -> "two pylons"; TEL_003 head-on primary has no photo (centre box hides it); B23/TEL_004 return path is simplified (real path folds via M3 to axis receiver); B02/B04 beam stays a symbol; 3.5 m enclosure form unresolved -> generic dome with two bi-parting leaves, not APO's building; evidence tags OBS_001/003/004/006, TEL_001/002/004 -> SEEN; OBS_007 stays GAP.
- Still running: optical+stopwatch+diagrams agent (fragments optical.json.tmp / stopwatch.json.tmp present).
- Applied observatory/telescope/astronaut/reflector conflicts to tools/asset_data.py (backup: research/asset_data.py.bak_pre_conflicts): RETRO frame wording, 46 cm vs 0.45 m, PSEP/array wording, TEL_002 "two pylons", telescope draw order 35/36 behind dome shell (40), TEL_003/TEL_004 simplification notes, OBS_002 generic-dome decision, ASTRO_010 stylised-kneel note; evidence tags OBS_001/003/006 and TEL_001/002/004 -> SEEN. build_beat_maps + build_manifest re-run: 79 rows, unused 0, cycles 0, stale 0.
- Merged references now 96 (observatory 16+4 link-only, telescope 10+3). Remaining: optical+stopwatch+diagrams agent.

## 2026-11-26 master recovery pass (both guides applied)
- Read HumanCraft V4 part I in full and the UE playbook sections used for handoff/QA; wrote `MASTER_STANDARDS_CROSSWALK.md` (areas, gates, checks; UE PROPOSED items are listed as tests).
- Single source of truth: `MASTER_PRODUCTION_DASHBOARD.md` is GENERATED by `tools/build_dashboard.py` from `qa/work_items.csv`, `qa/asset_status_overrides.csv`, `qa/proof_register.csv`; START_HERE, PRODUCTION_PLAN, CODEX_HANDOFF rewritten to point there; ORIGINAL_BRIEF_COMPLIANCE_AUDIT marked historic snapshot. `ASSET_GENERATION_TRACKER.csv` and `ANIMATION_PROOF_REGISTER.md` are generated too; `CODEX_PROGRESS.csv` (root) = Claude-verified log, `codex_handoff/CODEX_PROGRESS.csv` = Codex self-report.
- Briefs: `tools/brief_data.py` (per-asset geometry, states, layer tables, overlap, limits, filenames) + rewritten `tools/build_handoff.py` -> 34 briefs with 16 sections; `codex_handoff/ASSEMBLY_DIAGRAMS.md`, `guides/` (both master guides), `placement_boards/`; audit in `qa/handoff_audit.txt` (flags VISION_CARD link until look-dev finishes).
- Measured: ASTRO_001 now has tagged references (REF-ASTRO-001/002 full-body; a helmet/visor close-up is still a gap, being researched).
- Launched four background workers: reference gap-fill, professional animation video study, procedural library + code proofs, look-dev + animatic V1. Not merged yet.
- Codex: GUI computer-use tool not available in this session; contacted Codex through its CLI (`codex exec`, workspace codex_handoff/, Batch 0 = RETRO_002_CUBE_ARRAY calibration). Result NOT reviewed yet.
- Python env for production: `~/.venvs/uepipe/bin/python` (Pillow, numpy, scipy, cv2).

## 2026-11-26 later: Batch 0 / 0b reviewed, references merged
- Codex Batch 0 (RETRO_002): self-reported BLOCKED; hashes verified, image viewed; `qa/BATCH0_REVIEW.md` records findings and 3 pipeline decisions (native ~1254 px; sprite instancing; PD NASA bases for big maps).
- Batch 0b: plate with 100 measured recesses + 3 face discs + native macro, all self-reported blocked. `tools/assemble_retro_array.py` assembled 100 instances on the measured centres (panel squared, y-scale recorded): `assets/retro/retro_array_assembled_1254.png` viewed; method works; asset stays `candidate`.
- Reference gap pass merged (`merge_references.py` with venv python): 173 refs; 8 exact duplicates dropped from the active handoff via `research/redundant_refs.csv`; handoff now only viewed, non-duplicate refs (133 copies). 9 gaps remain open (see research/asset_research/GAP_CLOSURE_REPORT.md).
- Professional animation study finished (18 segments; none watched end to end).
- Running: Codex Batch 1 (cloud tiles, atmosphere slice layers, pole patches; log /private/tmp/claude-501/codex_batch1.log), Earth/Moon texture + P01/P02 worker, procedural library worker, look-dev + animatic V1 worker.
- Next executable: review Batch 1 files when done; merge worker outputs; view proof frames; rebuild handoff once VISION_CARD exists (audit currently flags the missing link).

## 2026-11-26 11:00-11:45: V2 narration, role correction, Codex protocol, P01/P02/P05
- New official narration V2 (95.39 s, SHA-256 3800dfce...): copied read-only to `narration/raw_v2/`; same 245 words as V1; aligner fixed (DP word-to-run assignment); beat maps rebuilt; V1 timing archived in `narration/v1_historical/`; transcript + drift table in `narration/NARRATION_TRANSCRIPT.md`.
- Proof timing: `NAR.v1(t)` word-edge warp for hand-set V1 cues; P08 equal slow factor re-solved (leg 2 anchored on its arrival). P07-P13 re-rendered on V2; 51/51 checks PASS. Animatic V1 retimed by inverse warp to `storyboard/animatic/ANIMATIC_V1_RETIMED_V2_TAKE.mp4` (V1 file kept).
- Role correction applied: Claude stopped making illustrated artwork; the Claude procedural cloud layer was rejected and replaced by a Claude composite of Codex tiles. NASA/LROC maps are sourced imagery (not Claude illustration).
- `ASSET_GENERATION_FAILURE_ROOT_CAUSE_AUDIT.md`: 10 root causes (no reference ever reached the generator; effort low; independent views; overloaded runs; wrong tilt in OUR brief, ...) + 4 lessons from the new runs. New protocol: one deliverable per run, effort high, refs via `-i`, `view_image` evidence in the log, Claude measures. Bundled Codex CLI path recorded (PATH `codex` is an older build).
- Codex runs: B3M lunar master, B4M observatory master, B5M astronaut master, R2a retro side (23.6 deg), B5L arm layers, B1c cyclones = candidates; R2b (regressed tilt) and B5L2 (no transparency) rejected into `codex_handoff/runs/_rejected/`. B4L observatory layers running at the time of writing.
- New proofs: P01 (Earth rotation/lighting, 6/6 PASS), P02 (Earth-Moon parallax on the opening line, PASS), P05 (astronaut arm rig v1: 4 PASS / 1 FAIL near-shoulder gap). P13 now uses Codex lunar plate + registered Codex array, panel lean, vector face at deep zoom.
- Fixed shared bug: `canvas.blit_image` wrote uninitialised memory around bitmaps (selftest regression added).
- Review method for all moving proofs this session: decoded frame sequences (`tools/filmstrip.py`, 12 frames + per-frame difference curve). Nothing was watched in real time; no audio heard. Human gates G1/G2/art/final remain open.
- Evidence-backed tracker: `qa/asset_tracker.csv`. Dashboard regenerated.

## 2026-11-26 (afternoon): premium continuation: opening, rigs, full rough cut

### Opening
- Three opening treatments were rendered as real 9.7 s clips with narration (`renders/proofs/OPEN/`).
- A (ground-level cinematic) was selected; the reasons and scores are in `OPENING_SELECTION.md`. It became P03.

### Observatory rig
- Built RIG_002 (`animation/proofs/obs_rig.py`, `assets/rigs/observatory/`) from Codex runs B4P, B4L and B4L2.
  - The shutter opens from its centre line.
  - The telescope is clipped to the slit and slews without overshoot.
- P04: 7/7 checks pass.

### Astronaut
- P05 shoulder gap fixed by shoulder skinning (rig v2). The v1 cap was removed. 5/5 checks pass.
- P06 is new: the astronaut sets the reflector down.
  - Uses Codex B5P (one composition) and its layer cut B5PA/B5PR.
  - Grip solved per frame; ballistic lunar dust.
  - Claude composited the 10x10 cube array onto the panel.
  - 6/6 checks pass.

### P13 strobe
- The push now starts 0.75 s earlier and uses smoothstep plus rack focus.
- Per-frame zoom fell from 26 % to 8.3 %. Max frame difference fell from 35.2 to 27.7; what remains is the full-frame push itself.

### Rough cut and sound
- Gap scenes for B05, B12-B16, B22-B25, B30-B32 and B37-B39 are in `animation/proofs/gaps.py`. All numbers come from the claims ledger (C01-C12).
- ROUGH CUT V1: `animation/roughcut.py` assembles the full 96 s film from the proofs and gap scenes with rendered crossfades and global captions.
- Sound V1 (`tools/sound_design.py`) is procedurally synthesised, so it is rights-clear.
  - Air sounds play only at the observatory; space is silent.
  - The bed is ducked 9 dB under the narration and sits 24.5 LU below it.

### Review documents
- `SHOT_BY_SHOT_VISUAL_EXPLANATION_AUDIT.csv`: 40 beats.
- `qa/DEFECT_REGISTER.csv`.
- `qa/art/ART_CONSISTENCY_SHEET_2026-11-26.png`.
- Root-cause audit updated with R15-R17.

### Not done
- No human listening (G1) and no real-time continuous viewing.
- No viewer muted test.
- No art approval or owner acceptance.

## 2026-11-26 (afternoon): V2 premium editorial revision

**Deliverables** (V1 untouched):

- `renders/roughcut_v2/ROUGH_CUT_V2_PREMIUM.mp4` and `ROUGH_CUT_V2_PREMIUM_CAPTIONS.mp4` (1080×1920, 96.000 s)
- `renders/roughcut_v2/ROUGH_CUT_V2.srt`

**Fixes:**

- dome seam (D07), P13 pixelation and blur (D12), new G29 atmosphere scene (D09)
- "A few photons" now shows the three dots (D14); the P06 release completes before the dissolve (D13)
- dots enlarged (D08); badges moved into the safe area (D16)
- caption redesign (D15)
- global grade (D10, partial)
- original synthesised SFX library and V2 mix: −17.4 LUFS, −1.9 dBTP (D06 by sound)

**Records:** correction list, text audit, AI-appearance audit, comprehension QA, final QA and the Roman Urdu report.

**Not done:** real-time viewing, listening, muted-viewer test, owner acceptance.

## 2026-11-26 (evening): V3 retention, clarity, music and polish

**Deliverables:** `renders/roughcut_v3/`, with V1 and V2 untouched.
- `SLOT07_V3_PREMIUM(.mp4|_CAPTIONS.mp4)`: private review mixes containing Small_Variables.mp3, whose rights are **unverified**.
- `SLOT07_V3_RIGHTS_CLEAR_MASTER_NO_MUSIC(...)`, `SLOT07_V3.srt`, `stems/`.
- The audits listed in the V3 brief, plus `PHONE_REVIEW.html`.

**Picture**
- Opening 2–4 s: aim trace, continuous tilt and a charge glow (D20).
- G22 redesigned as a push-in followed by a schematic photon rain with a detector payoff (D21).
- All pill badges replaced by one `DISCLOSURES` table in `roughcut.py` (D24).
- Imagined mirror is now a stand mirror (D17).
- P09/P10 share a detector panel (D19).
- G37 cinematic ending (D18).
- Labels in Comic Neue, formula in a maths face (D22).
- G30 enlarged.

**Sound** (`tools/sound_design_v3.py`)
- 4-bar repeat edit of the music.
- Automation map with 29 points.
- Music sits 21.0 dB under the voice in voiced windows.
- 51 cues (down from 115), retuned to F major.
- −16.4 LUFS / −2.0 dBTP.

**Not done:** listening, real-time viewing, muted test, owner acceptance, music licence (D25).

## 2026-11-26 (late): owner acceptance and consolidation
- Owner directive: V3 is the owner-selected final production version and its visual quality is accepted; there will be no V4. Recorded in `OWNER_ACCEPTANCE_RECORD.md` and in `qa/work_items.csv` (W21, W23, W38 updated; W39–W42 added). Listening (W22), music licence (W41) and the publication checks (W42) stay open.
- The project moved from `unreasonably-exact/lunar-laser-ranging/` to `unreasonably-exact/07-video-productions/SLOT07_lunar-laser-ranging/`. The move was an atomic rename, so no bytes changed and all 95 workspace MP4 checksums match.
- `Small_Variables.mp3` was copied into `audio/music/`. `tools/sound_design_v3.py` now reads it there, which makes the project self-contained.
- Non-destructive rebuild check (`tools/rebuild_check.py`): 19 stills match the locked clean render within 1.38–1.88 /255 (encoding error). The code reads no files outside the project apart from the Python environment and the macOS fonts. Both `selftest.py` and `render_proofs.py --selftest` pass.
- New files: `FINAL_MASTERS/` (hard links with UE_ names), `FINAL_PACKAGE_MANIFEST.md`, `REBUILD_INSTRUCTIONS.md`, `tools/requirements_uepipe.txt`, and `qa/FINAL_MANIFEST_SHA256.txt` (every file).
- Reusable parts were cloned (not moved) into the workspace library: `04-shared-assets/` and `05-animation-engine/`.
