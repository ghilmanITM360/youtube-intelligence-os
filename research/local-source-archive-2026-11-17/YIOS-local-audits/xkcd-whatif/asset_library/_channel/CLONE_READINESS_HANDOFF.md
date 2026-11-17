# xkcd's What If? — clone-readiness pass, final handoff (2026-11-08T18:04:39Z)
Session: Claude Code (claude-opus-5-5), second account, same Mac. Lock `~/YIOS-local-audits/xkcd-whatif/.xkcd_writer_lock` acquired ~17:45Z, released at the end of this run.
Usage: start 5h 2% / weekly 13% (17:44Z); see end line for the final read.

## Done (all LOCAL ONLY under this folder; nothing published; repo untouched)
| Phase | Deliverable | Key result |
|---|---|---|
| P1 | STATE_SNAPSHOT.md, XKCD_COVERAGE_AUDIT.md, coverage_by_video.csv | 44 videos (24 long/20 Shorts), 5,458 states, pts 5,458 OK, SHA 3/3; 44/44 VISUAL_ANALYSIS_PARTIAL; ~24 long + 11 Shorts independent |
| P2 | category_index.csv, review_sheets/ (10 sheets + VIEWING_NOTES.md), CATEGORY_AUDIT.md | 240/2,755 clusters viewed (8.7%), 44/44 videos; graphics_ui ~96% pure, environments = background type |
| P3 | model_sheets/MODEL_SHEETS_XKCD_WHATIF.md + CSVs + 3 viewed sheets | narrator template pixel-identical in 18/24 long openings; canvas #F9F9F9; stroke ≈8 px@1080; POP_ON 38%/CUT 23%; BUSY vs CALM lists; ASR pace flat |
| P4 | motion_windows/ (13 windows) + MOTION_WINDOWS.md | dissolve linear 6 f; pops/pose 1 f; 0/13 overshoot; camera moves 9–12 f blurred, eased |
| P5 | HUMANCRAFT_ALIGNMENT.md | layer/rig plan, motion mapping, proof spec, scorecard; ffmpeg no drawtext; no Remotion/HyperFrames CLI/Blender |
| P6 | PROMPT_PACK/ (17 files + index) | original NIB narrator, TARDI mascot, teal brand; text only |
Per-phase handoffs: P1–P6_HANDOFF.md. Hashes: SHA256SUMS (per-phase blocks). Tools: ~/YIOS-local-audits/tooling/asset_library/xkcd/ (CF originals untouched).

## Not done / blocked
- Audio: BLOCKED_CAPABILITY (no listening); no CT_SCAN_COMPLETE, no AV sign-off, no status changed.
- No asset generation, no renderer install, no test render, no blind test, no publishing (all need owner go-ahead).
- Second reader for the viewing pass; keyword re-tune; title-card frame not opened; >2 motion windows per class; Shorts motion windows.
- Text indexes could be published to research/xkcd-whatif-visual-forensics only on owner go-ahead (xk_publish.py guards, allowlist, no images).

## Next exact operation (owner decision)
Choose the image model and approve generating CHR-001 (NIB anchor); in parallel decide whether to allow a renderer test (e.g. Python/PIL + ffmpeg overlay/xfade, no install) for the 5–12 s silent motion proof.
Final usage read: {"five_hour": 0.23, "five_hour_reset": 1794177000, "seven_day": 0.15, "seven_day_reset": 1794747600, "overage": false, "read_utc": "2026-11-08T18:04:47.412989Z"}
