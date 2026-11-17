# xkcd's What If? — clone-readiness pass, state snapshot (re-verified on disk 2026-11-08T17:47Z)

Session: Claude Code (claude-opus-5-5), second account, same Mac (`/Users/ghilmankhan`). Writer lock `~/YIOS-local-audits/xkcd-whatif/.xkcd_writer_lock` ACQUIRED 2026-11-08 ~17:45Z (label `xkcd-clone-readiness`), after usage check.

## Usage at start (meter: `primitive-education/scripts/pe_usage.sh`, headless rate_limit_event)
- 2026-11-08T17:44:25Z: five-hour 2%, weekly 13%, overage false. Disk 65 GiB free.

## Verified (MEASURED, `tooling/asset_library/xkcd/coverage_audit.py`)
| Check | Result |
|---|---|
| Library videos (`library_manifest.csv`) | 44 (24 LONG_FORM, 20 SHORT by census `format_class`) |
| State rows in all `states_index.csv` | 5,458 |
| State JPGs on disk | 5,458 (= manifest `frames_saved` sum) |
| `pts_check` column | 5,458 OK, 0 MISMATCH |
| Unique frames in `_channel/unique_frames/` | 2,755 |
| SHA-256 spot-check, 3 random rows (seed 20261108) | 3/3 match: `Ny9m2l6h478/states/G0019_f000451_t18.792.jpg` 705171cf…, `YL2VNtus4xk/states/G0060_f001992_t83.000.jpg` 35303f08…, `FkUNHhVbQ1Q/states/G0030_f000695_t28.958.jpg` 8b01fa93… |
| Per-video status (`videos/<id>/quality_gate.json`) | 44/44 VISUAL_ANALYSIS_PARTIAL; ct_scan_complete true 0; full_av_signoff true 0 |
| Kit hashes | packaged SKILL.md b7baff3e…bfd9, installed d308d87d… (same as campaign record) |

## Facts from the handoff, checked or not
- 38/40 caption-available Shorts are narration excerpts: from `campaign/short_long_text_reuse_population.csv` (not recomputed). Within this library: 16/20 Shorts are text excerpts (9 of their parents are in the library), 2 standalone text, 2 have no caption text (parent UNKNOWN).
- "27 videos without local source media": matches 27 `MISSING_SOURCE_HASH` rows in `campaign/knowledge_links_v1_issues.csv` (repo index scope). Census `local_files` shows 88/91 channel videos have a local MP4; 44 are in this library, 20 more (Pop-6 long) were measured only, with no ledger, so they are not in the library.
- 10 videos shared with the repo forensic index have different media hashes: taken from the checkpoint R handoff, not re-verified here. Not merged.
- Census 45 long + 46 Shorts: from `campaign/CAMPAIGN_GOAL_v1.md` (snapshot 2026-11-04), not refetched.
