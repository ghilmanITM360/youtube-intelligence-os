# Resume here — Casually Finance editing forensics

State (2026-10-20): Phase 1 gate PASSED. 17 of 48 local videos (all Shorts) have validated per-video forensics (depth A/B/C, listening blocked, single reviewer); preliminary channel DNA, recipes, asset spec and handoff exist (n=10-12 snapshot, era split refreshed at n=14). 31 videos remain (15 uncovered Shorts + 16 prior-covered videos incl. all 10 long-form). Latest: xrNPr3YrWdw (banded, depth B). Do not claim 100 %.

1. Read `SOURCE_DISCOVERY_REPORT.md`, then `STATUS.json` (`queue_uncovered_by_views`, `videos_in_progress`).
2. Worktree: `/Users/ghilmankhan/workprojects/yio-cf-editing-forensics`, branch `research/casually-finance-editing-forensics` (from `main@08e71926`). Do not touch the main checkout (`research/finance-economics-intelligence`, PR #36).
3. Source media stays in `/Users/ghilmankhan/Downloads/CasuallyFinance` (read-only). Verify SHA256 against `SOURCE_MEDIA_INVENTORY.csv` before work on a new machine.
4. Prior research is read from Git, not from the working tree: `codex/casually-finance-forensic-research@043b85bf`, `origin/research/casually-finance-success-playbook@fb1e56d0`, `origin/research/casually-finance-video-inventory@1adfdeb9`. Fetch them if absent.
5. Frame dumps live outside Git in `../yio-cf-editing-forensics-local-evidence/`; every script is deterministic and regenerates them from the source MP4.
6. Never mix Casual Economics or What If evidence into Casually Finance records. Direct audio listening is unavailable to the agent: report measured signal and ASR only.
7. Check live usage first (5-hour, weekly). Stop expensive work near 90 % / 95 %, commit, update this file.

8. Per-video procedure and script order are in `STATUS.json` -> `pipeline`. Next video: first entry of `queue_uncovered_by_views`. Use `python3 -E` (not `-I`) for scripts that import numpy/PIL/whisper.
9. In `bands.json` set `"auto_cuts": true` to have `build_video_tables.py` generate hard-cut events from scene boundaries (scene-centric authoring); author only non-cut events by hand.

10. After adding videos: run `scripts/aggregate_channel.py` and `scripts/update_registers.py`, then refresh the numbers quoted in `CHANNEL_EDITING_DNA.md`, `OBSERVATIONS_VS_HYPOTHESES.md`, `SOUND_DESIGN_SPEC.md`.
11. Decode must use `-fps_mode passthrough` (fixed). Videos whose AUTO_SUMMARY frames differ from inventory frames must be re-extracted before authoring (`STATUS.json` `redo_after_decode_fix`).

12. Fast authoring: `scripts/prep_banded.sh <id>` or `scripts/prep_full.sh <id>`, then a per-video `videos/<id>/review/author_review.py` using `scripts/author_lib.py` (see `videos/UJEqqBpH18k/review/author_review.py`).
