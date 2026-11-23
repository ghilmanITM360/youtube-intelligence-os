# 15 PRODUCTION PIPELINE — CH001 (independent, reproducible; creator's own toolchain UNKNOWN)
## Forensics
Creator software: UNKNOWN (no project files, no disclosure found). Visual inference only (flat vector look, hard cuts, pop-ins) - category VISUAL_INFERENCE, no specific tool claimed.
## Pipeline actually used for the same-video test (verified by execution)
Idea -> ASR words (`audio/10nEByVLya0_small_en.json`) + caption-event ledger -> visual-state CSV (61 states) -> measured geometry (ffmpeg frame extract, bbox/column-run/dark-mass on 270x480 gray) -> original-art draw functions (PIL, SS=2, band y640-1300, bg #FDFDFD) -> per-frame composition -> raw RGB piped to ffmpeg libx264 crf14, 30 fps -> metrics (`compare_metrics.py`) -> error log (E1-E38) -> QA report.
| Step | Input | Output | Gate |
|---|---|---|---|
| State timing | source MP4, ledgers | visual_states.csv | frame ids on every state |
| Geometry | ref frames | numbers in blueprint/DNA files | bbox IoU per state |
| Build | numbers, original art | render_*.py | renders without errors, 1660 frames |
| Render | script | MP4 (silent) | ffmpeg exit 0 |
| QA | ref vs recon | metrics json, rank.py list | worst-state review, logged in error log |
| Release review | all of the above | verdict | needs independent reviewer (NOT done) |
Command: `python3 render_10nEByVLya0_v14.py OUT.mp4 1660` (~90 s). Risks: numeric-only QA (images never viewed); audio not synced; third-party content replaced by labelled stand-ins.
Rights: references and reconstructions with third-party material stay internal; recreations use original art only.
