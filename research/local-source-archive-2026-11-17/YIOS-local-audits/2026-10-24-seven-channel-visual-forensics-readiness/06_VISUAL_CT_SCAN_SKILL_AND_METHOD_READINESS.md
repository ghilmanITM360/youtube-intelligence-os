# 06 — Visual CT Scan skill and method readiness (Machine A)

## A. Kit location and read-only validation (nothing installed, nothing modified)
| Item | Result |
|---|---|
| Preserved candidate | `/Users/ghilmankhan/workprojects/yios-visual-forensics-install-candidate-2026-10-24/` (43 files) — untouched; only read and `shasum -c` |
| Extracted kit | `/Users/ghilmankhan/Downloads/videos in mp3/YIOS_Visual_Forensics_Intelligence_Kit_v1.0/` (inside "videos in mp3"; 21 .md, 4 .json, 3 .csv, 4 .txt, 1 .py) |
| Kit zip | `.../videos in mp3/YIOS_Visual_Forensics_Intelligence_Kit_v1.0.zip` sha256 `a89de050…cff` = candidate `kit-originals/…zip` (identical). No copy in top-level `~/Downloads`. |
| `SKILL.md` | present; frontmatter `name: visual-ct-scan`; sha256 `d308d87d0e1144e2b8a6f234847104856e9fac561d9f4dc63ea0ae263b4868e7` |
| 14 reference modules | 01…14 present (evidence authority, workflow/modes, temporal ingestion, art direction, motion/camera, editing/story, audio sync, attention, reconstruction, script brain, channel DNA, improvements, completion gates, source traceability) |
| 7 templates | AUDIO_ALIGNMENT_COLUMNS.csv, COVERAGE_AND_QUALITY_GATES_TEMPLATE.json, RECONSTRUCTION_BLUEPRINT_TEMPLATE.md, SCENE_ANALYSIS_TEMPLATE.md, SHOT_LEDGER_COLUMNS.csv, SOURCE_MANIFEST_TEMPLATE.json, VISUAL_EVENT_LEDGER_COLUMNS.csv — all non-empty, JSON/CSV parse |
| 4 original master prompts | `source-prompts/01…04_*_ORIGINAL.txt`; byte counts 27,886 / 13,615 / 44,738 / 33,898; all four sha256 match `SOURCE_PROMPT_MANIFEST.json` |
| `validate_kit.py` (extracted kit) | **PASS** (4 prompts hash-verified, 14 refs, 7 templates, 0 errors) |
| `validate_candidate.py` on `repo-overlay` | **PASS** (frontmatter, no dead links, all six modes, CLAUDE.md pointer, index link) |
| Candidate `SHA256SUMS` | all entries OK (0 failures) |
| `routing_demo.py` | PASS — "CT scan"→CT_SCAN; "deeper visual analysis"/"scene by scene"/"visual forensics"→DEEP; "frame-by-frame"→CT_SCAN; "motion reconstruction"→+RECONSTRUCTION; "channel visual DNA"→+CHANNEL_DNA |
| Integration/examples | `SKILL_INVOCATION_EXAMPLES.md`, `INSTALL_README.md`, `MASTER_INSTALL_PROMPT_FOR_CLAUDE.md`, `integration/CLAUDE_MD_INSERT.md` present |

**Important limits.** (1) The routing demo is a *static parse* of a table in SKILL.md; it is **not proof that Claude Code will auto-activate the skill live**. (2) `visual-ct-scan` is **not installed on Machine A** (not in `~/.claude/skills`, not in the repo `.claude/`); Machine B's personal installation is not available here. (3) Per the owner, it must not be installed or published now. Reliable use for the next video = explicitly read `SKILL.md` and all 14 references (+7 templates) from the candidate's `repo-overlay/.claude/skills/visual-ct-scan/` at session start of that audit (references are ~52 KB total), then follow its mode rules. Target modes DEEP, CT_SCAN, RECONSTRUCTION, CHANNEL_DNA all exist in SKILL.md (plus INVENTORY, STRUCTURAL).

## B. Methodology gap assessment against the validated skill
Legend: ✅ supported now · ◐ partially · ❌ not available. "Evidence today" = what exists on Machine A.

| Capability required | Status | Evidence / gap / consequence |
|---|---|---|
| Authentic source verification | ✅ | ffprobe + SHA-256 for all 456; 456/456 match Machine B; embedded IDs absent so 65 files remain title+duration identities (file 04) |
| Complete video overview | ✅ | ffmpeg 9.0.1 (videotoolbox decode); 1 fps / scdet / select / tile filters all present |
| Actual scene/shot identification | ◐ | ffmpeg `scdet`/`select` are *candidate generators* only; PySceneDetect and OpenCV are **not installed** (not installed per instruction) → must use ffmpeg + numpy frame-diff; every boundary needs manual frame confirmation |
| Native-timestamp frame refs | ✅ | `ffprobe -show_frames`, `showinfo` PTS, `-fps_mode passthrough` (the CF lesson: decode must use passthrough). VFR check must be run per selected video (only average fps was recorded here) |
| Sub-second text/graphic events, before/during/after motion | ◐ | Technically possible via dense native-frame windows (Pillow+numpy diff + image reading by the reviewing agent); **no OCR** (tesseract missing) so text timing is by visual reading; expensive per video |
| Motion uncertainty / frame-rate limits | ✅ | Source fps 24/30 mostly (50/60 fps for some files); 24→30 conforms exist (CF lesson) → uncertainty must be declared per video |
| Art/illustration, typography, palette, symbols | ◐ | Agent can judge from frames (analysis is interpretive, labelled INFERRED); no automatic palette/typography extractor installed beyond Pillow/numpy; CF scripts `measure_color_area.py`, `layout_profile.py` exist in Git only |
| Kinetic typography, layering, parallax, easing, masking, transitions | ◐ | Needs dense frame windows; easing is explicitly `NOT_ASSESSED` in all prior CF/CE records; signal-derived motion classes are candidates, not facts |
| Hook/story/payoff/numeric graphics/retention hypotheses | ✅ (as hypotheses) | Skill labels attention/retention as hypotheses; **no measured retention, CTR, eye-tracking or creator intent exists** and none may be claimed |
| Audio availability | ✅ | All 454 video files have AAC audio (44.1/48 kHz) |
| ASR / transcription | ◐ | `openai-whisper 20240930` + torch 2.8 in **system python 3.9** with cached models `base.pt`, `small.en.pt` (no download needed). Official transcripts: xkcd 83/83, Primate 28/29, Casual Economics 11/11 (in Git branch); **none for Casually Finance, monke, Primitive Education, Barely Evolved**. Repo `.venv` (py3.12) has Pillow/numpy but no whisper. ASR is `ASR_UNCERTIFIED` |
| Speech-to-visual timing | ◐ | Possible with ASR word times (±100 ms prior CF note) vs frame-exact visual times |
| Music/SFX/silence | ◐ | ffmpeg `silencedetect`/`ebur128` available; classification of music/SFX events is signal-based only |
| Verified listening / AV sign-off | ❌ | The agent cannot hear audio. **FULL_AV_SIGNOFF_COMPLETE requires a human listener** (skill reference 13). 0 videos in any ledger have it |
| Scene-by-scene blueprints, image/animation prompts, asset inventory, design tokens, edit specs, feasibility, improvements | ✅ | Templates exist (RECONSTRUCTION_BLUEPRINT_TEMPLATE, SCENE_ANALYSIS_TEMPLATE, ledgers); prior CF/CE branches contain example blueprints. Reconstruction claims require a viewable source (all 448 video sources are viewable) |
| Original-vs-reconstruction honesty | ✅ | Skill forbids claiming reconstruction without frame evidence |

### Environment (checked read-only, nothing installed)
- ffmpeg/ffprobe 9.0.1 (`/opt/homebrew/bin`), hwaccel `videotoolbox`; filters present: scdet select showinfo tile blackdetect freezedetect silencedetect ebur128 mpdecimate cropdetect thumbnail.
- Python: system `/usr/bin/python3` 3.9.6 → Pillow 11.3.0, numpy 2.0.2, torch 2.8.0, whisper 20240930, openpyxl 3.1.5; `/opt/homebrew/bin/python3.12` has none; repo `.venv` 3.12.14 → Pillow 12.3.0, numpy 2.5.4. **Missing everywhere:** OpenCV, scenedetect, scipy, pandas, tesseract/pytesseract, faster-whisper, librosa, soundfile, mlx-whisper. Consequence: use ffmpeg + numpy/Pillow (the CF forensic scripts did exactly this and require `python3 -E`, not `-I`).
- **CF forensic scripts** (`forensic_features.py`, `layout_profile.py`, `segment_events.py`, `event_sheets.py`, `build_video_tables.py`, `author_lib.py`, etc. — 20 files) live only in Git at `origin/research/casually-finance-editing-forensics@090f84b3`. The worktree `/Users/ghilmankhan/workprojects/yio-cf-editing-forensics` does **not exist** on Machine A, and creating worktrees is forbidden without owner approval. They can be read with `git show`; running them needs an owner-approved external copy.
- Existing evidence: `/Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence/` (38 Short evidence dirs with whisper.json, sheets, spectro) and `/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research/` (38 thumbnail files).
- **Disk: only ~11–12 GB free of 460 GB (98 % used) on the data volume.** This is the main local-capacity risk: no bulk frame dumps; per-video scratch must be capped (<~2 GB, deleted/archived after), evidence stored outside `/tmp`. Claude plan usage is separate: five-hour 10 %, weekly 7 %, context 26 % at last check.

## C. Verdict
Kit: valid and complete; **not installed; live auto-activation unproven**. Tools: sufficient for a rigorous evidence-based DEEP/CT_SCAN of *one video at a time* with ffmpeg + numpy/Pillow + agent frame review, but with real gaps (no OCR, no PySceneDetect/OpenCV, scripts not on disk, human listening impossible, tight disk). → **DEEP_VISUAL_CT_SCAN_PIPELINE_PARTIALLY_READY**.
