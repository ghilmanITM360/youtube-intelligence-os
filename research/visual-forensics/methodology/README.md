# Visual CT Scan methodology (snapshot)

`visual-ct-scan-skill-snapshot/` is a copy of the Machine A personal skill `~/.claude/skills/visual-ct-scan/` (SKILL.md, references 01-14, templates) taken 2026-10-24 so Machine B can read the contract. The `source-prompts/` originals are not copied. The installed skill remains authoritative; this snapshot is a reference copy and may drift.

Tooling used by both accepted scans: ffmpeg 9.0.1, ffprobe, Python 3.12 venv with opencv-python-headless 5.0.0.93, scenedetect-headless 0.7.2, numpy, pandas; openai-whisper small.en for provisional ASR. Per-video scripts and validators are stored under each video's `research/` folder (`validate_outputs.py`, `v1_scripts/`, `v2/validate_v2.py`). Validators need the external evidence folder and the source MP4; on a machine without them only the Git-stored reports and ledgers can be read, not re-validated.

Lessons carried into later videos (from Uumnx2Fo6cE): use larger state tiles, a built-in independent second pass, multi-tier sub-threshold event sweeps, bounded native-resolution crops, and chunked reviewer waves with usage checkpoints.
