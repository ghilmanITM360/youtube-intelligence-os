# Slot 07 V3: final package manifest (2026-11-26)

Every item the owner listed in the consolidation directive (§2), and where it is. All paths are relative to this folder. SHA-256 values for every file are in `qa/FINAL_MANIFEST_SHA256.txt` (1,605 files, regenerated 2026-11-26 after the move and the documentation updates).

| Required item | Location | sha256 (first 16) / notes |
|---|---|---|
| Clean final MP4: publication candidate | `FINAL_MASTERS/UE_SLOT07_LUNAR_LASER_RANGING_V03_FINAL_RIGHTS_CLEAR.mp4` | `29602f9bfd97c654`, 126.7 MB |
| Clean final MP4: music-inclusive review master | `FINAL_MASTERS/UE_SLOT07_LUNAR_LASER_RANGING_V03_FINAL_MUSIC_REVIEW.mp4` | `8b2675bf405b10b7` (**private review**: music rights unverified) |
| Captioned final MP4 | `FINAL_MASTERS/UE_SLOT07_LUNAR_LASER_RANGING_V03_CAPTIONS_RIGHTS_CLEAR.mp4` / `..._CAPTIONS_MUSIC_REVIEW.mp4` | `ce58ebbc79801648` / `9ce3348dfb782e38` |
| SRT subtitles | `FINAL_MASTERS/UE_SLOT07_LUNAR_LASER_RANGING_V03.srt` | `262a1fa6b0ea92a1`, 49 cues |
| Ungraded picture (no audio) | `renders/roughcut_v3/SLOT07_V3_clean.mp4` | 2,880 frames; the rebuild check compares against this |
| Original approved narration | `narration/raw_v2/SLOT07_NARRATION_V2_RAW.wav` (read-only) | `3800dfce3668e75b`, 95.39 s; transcript `narration/NARRATION_TRANSCRIPT.md`; word times `narration/WORD_TIMESTAMPS.json` |
| Background music: as supplied | `audio/music/Small_Variables.mp3` | `f781c977d23ef71e` (also `../../06-audio-library/music/Small_Variables/Small_Variables_ORIGINAL.mp3`) |
| Background music: edited production version | `renders/roughcut_v3/stems/stem_02_music_small_variables_UNVERIFIED_RIGHTS.wav` | `01d3dd8e21e8409d`. Four bars repeated, seam at 55.58 s, 29-point automation (`renders/roughcut_v3/MUSIC_AUTOMATION_MAP.csv`) |
| Separate audio stems | `renders/roughcut_v3/stems/` | 01 narration, 02 music, 03 ambience, 04 mechanical, 05 scientific illustrative, 06 character Foley, 07 final master, alt rights-clear pad (48 kHz WAV) |
| Editable animation source | `animation/` (`roughcut.py` V3 assembler, `proofs/` scenes, `uemotion/` engine, `render_proofs.py`, `selftest.py`) | V2 sources kept as `*.bak_v2`; `roughcut_v2.py` |
| Codex-generated artwork | `codex_handoff/runs/<RUN>/` (single-deliverable runs, each with `codex.log` + `NOTES.md`), `codex_handoff/deliveries/batch*/` (early multi-asset batches), `codex_handoff/runs/_rejected/` | see `ASSET_GENERATION_FAILURE_ROOT_CAUSE_AUDIT.md` |
| Character and object rigs | `assets/rigs/observatory/RIG_002_observatory.json`, `assets/rigs/astronaut/RIG_003_astronaut_arms.json`, `assets/rigs/astronaut_retro/`, `assets/retro/retro_array_instances.json` | rig code: `animation/proofs/obs_rig.py`, `p05.py`, `p06.py` |
| Scientific research and models | `SCIENTIFIC_RESEARCH.md`, `SCIENTIFIC_CLAIMS_LEDGER.csv`, `SCIENTIFIC_VISUAL_DESIGN.md`, `SCIENTIFIC_COMPREHENSION_QA.md`, `research/` | The model is code: `animation/selftest.py` and the proof asserts (P08, P11, P12, P13). `scientific_model/` is an **empty folder** (never filled) |
| Asset provenance | `ASSET_GENERATION_TRACKER.csv`, `codex_handoff/references/*/REFERENCE_INDEX.md`, `research/REFERENCE_MANIFEST.csv`, `SFX_LICENCE_MANIFEST.csv`, `renders/roughcut_v3/SOUND_DESIGN_CUE_SHEET.csv` | `MASTER_ASSET_MANIFEST.csv` was never updated after planning, so it shows every asset as PLANNED. Use the tracker and `../../11-production-management/REUSABLE_ASSET_INDEX.csv` instead |
| Production QA | `renders/roughcut_v3/FINAL_PRODUCTION_QA.md`, `OWNER_SCREENSHOT_DEFECT_AUDIT_V3.md`, `OPENING_RETENTION_AUDIT.md`, `V2_V3_COMPARISON.md`, `qa/DEFECT_REGISTER.csv`, `renders/proofs/*/PROOF_REPORT.md` | |
| Rebuild instructions | `REBUILD_INSTRUCTIONS.md` | the non-destructive rebuild check passed on 2026-11-26 |
| Owner decision | `OWNER_ACCEPTANCE_RECORD.md` | visual acceptance, recorded separately from listening and licence |

**Self-contained check (2026-11-26).** All of these passed after the project moved to `07-video-productions/`:
- the 95 MP4 checksums in the workspace match their pre-move values;
- the rebuild check opened no file outside the project except the Python environment and the two macOS fonts;
- `animation/selftest.py` passes;
- `render_proofs.py --selftest` passes.
