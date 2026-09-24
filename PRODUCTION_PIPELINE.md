# Voiceover production pipeline

Run from repository root. Requirements: Python with OpenAI Whisper installed, ffmpeg and ffprobe. Whisper word timestamps are model alignments, not independently verified phoneme timing. Review `transcript/words.csv` against audio before final edit. The provided written script informs scene planning; audio transcript controls timing.

```bash
python3 production_pipeline.py prepare path/to/voiceover.mp3 --script path/to/script.txt --output output/project-name
python3 production_pipeline.py validate output/project-name
python3 production_pipeline.py status output/project-name
```

Set `PRODUCTION_BRAIN` to a different read-only production brain directory if needed. The default is a sibling directory named `video data of what if/production_intelligence_brain`. Existing evidence is read only. The current planner uses deterministic lexical rules; confidence is limited and visual choices require editorial review. Image prompts are generated automatically. Place generated PNGs at the exact paths in `ASSET_REGISTRY.json`, then run `validate` again. Give `capcut/CHATGPT_WORK_CAPCUT_PROMPT.md` and the package folder to ChatGPT Work for GUI editing. No CapCut project file internals are modified.

Timeline schema version 1.0 contains source media, scenes, shots, tracks, assets, audio, captions, motions, keyframes, transitions, and sync events. CapCut actions schema version 1.0 contains ordered operations with timestamps and targets. `qc/validation.json` records structural checks and missing assets. Production grammar priors (locked camera and hard cuts) are cited from the corpus. Original colors and imagery are project decisions. SFX and music are not inferred from the corpus.
