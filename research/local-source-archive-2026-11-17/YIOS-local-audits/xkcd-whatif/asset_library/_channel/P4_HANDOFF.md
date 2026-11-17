# P4 handoff — motion windows (xkcd clone-readiness)
- Done: 13 windows in `motion_windows/<class>_<video>_<seg>/` (window.csv/json, strip.jpg, f_*.jpg), summary `motion_windows/MOTION_WINDOWS.md`. Tool `tooling/asset_library/xkcd/motion_window.py` (SHA check, bounded select, PTS check).
- MEASURED: dissolve = linear 6 f (2/2 + the dissolved pose swap); pop-on and pose swap 1 f, no overshoot; write-on ≈ constant speed; camera moves 9–12 f, blurred, eased; 0/13 overshoot. Disk after: 64 GiB free; 26 MB used.
- NOT done: >2 windows per class; Shorts windows; title-card animation; per-letter timing beyond 2 examples.
- Next exact operation: P5 HumanCraft alignment (re-check node/ffmpeg/drawtext; no installs).
