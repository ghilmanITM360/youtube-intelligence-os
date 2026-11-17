# DATA_INVENTORY — xkcd's What If? replication audit (2026-11-14)
Built by read-only inspection. No raw file modified. Paths are real; sizes from `du`.

| # | Resource | Path | Type / size | Source | Verification | Relevance |
|---|---|---|---|---|---|---|
| 1 | Reference videos, set A (88 files = 44 long + 44 Shorts) | `~/Downloads/videos in mp3/xkcd Channel/` | MP4, 532 MB | public download | census: 88 of 91 channel videos local; SHA-256 recorded in census (100/100 OK) | PRIMARY evidence. 3 videos have no local file (alkJ7xScBiw, NxVdO7M2YdM, XwJAbyn5uGY) |
| 2 | Reference videos, set B (14 files, 12 are re-downloads of set A) | `~/workprojects/video data of what if/videos/` | MP4, 158 MB | public download (YTDown) | ffprobe + md5: same video, same audio; 2 pairs 1080p vs 720p | REDUNDANT, not independent. The other 2 files (sunset, visible-light beam) were not part of the 12-pair check; their relation to set A is not verified here |
| 3 | Per-video ingest workspaces (70 videos) | `~/YIOS-local-audits/xkcd-whatif/videos/<id>/` | frames, tables, ASR, loudness, 6.3 GB | derived | 44 have quality_gate.json, all VISUAL_ANALYSIS_PARTIAL | decoded-frame measurements and state ledgers |
| 4 | Census | `.../census/census.csv` (+summary) | 91 rows | public player metadata, 2026-11-04 | live page 2026-11-14: still 91 videos, 1.38M subs | public facts |
| 5 | Visual state library | `.../asset_library/` | 5,458 state frames of 44 videos, 1.1 GB | extracted from set A | pts 5,458 OK, SHA verified | still frames, NOT motion |
| 6 | Channel model sheets / motion windows | `asset_library/_channel/model_sheets`, `motion_windows` | CSV+JPG, 13 windows | measured | viewed 3 sheets, 2 strips | style rules, motion grammar |
| 7 | Visual closure ledger | `asset_library/_channel/ct_closure/` | 29 rows | closure contract v1 (visual-only) | per-video gates | strongest per-video status |
| 8 | Deep-VF rules v1-v4 + held-out v7-v9 | `asset_library/_channel/deep_vf/` | MD/CSV | frozen rules | v8 32/34 holds; v9 untested features | generalization evidence |
| 9 | Silent proof renders | `deep_vf/proof_v1_attempt3/` | 2 MP4 (16:9, 9:16), 8 s | Python/PIL + ffmpeg | machine checks PASS; P8/P9 human review PENDING | only rendered recreation test |
| 10 | Animatics RT1-RT4 | `reconstruction/` | 11 MB | Python/ffmpeg | RT2/RT3/RT4 PASS rhythm/grammar, silent | grammar proof, not craft proof |
| 11 | Prompt packs v1, v2 | `asset_library/_channel/PROMPT_PACK*` | text only | authored | no image ever generated | original NIB narrator / TARDI mascot design text |
| 12 | Older 14-video corpus + "brain" | `~/workprojects/video data of what if/` (production_intelligence_brain, video_forensics_output 499 MB) | 7,864 words, 604 sentences, 581 states, 200 shots, 438 motions | Sep 2026 analysis | validator passes; channel identity was unresolved then | overlaps set A (same 14 videos, same channel): NOT independent of rows 1-3 |
| 13 | Failed CapCut chair test | `.../chair_test_v2_review/FAILED_VIDEO_VISUAL_AUDIT.md` | MD + evidence | owner export 0921.mp4 | REJECTED PROTOTYPE | the only earlier recreation attempt, it failed |
| 14 | Book source | `~/workprojects/what if book/` | PDF + 91-question extraction, 241 MB | Randall Munroe, Houghton Mifflin 2014 | extraction QA folder | script source material. Copyrighted: do not reuse text |
| 15 | Tools | ffmpeg 9.0.1 (no drawtext), node 24, python venv with PIL+OpenCV, whisper-cli | n/a | checked 2026-11-14 | `which` | blender, remotion, yt-dlp, manim, ImageMagick NOT installed |

Not found anywhere: audio listening records, sound-effect/music libraries, a generated original character, a rig, any 3D asset, CapCut/AE project files of the source channel.
Duplicate rule applied (AGENTS rule 9): rows 1 and 2 are one dataset; row 12 is the same 14 videos as part of row 1; row 5 is derived from row 1; Shorts that are narration excerpts of long videos (9 in library, 7 more with parents outside) are partly the same drawings re-laid out. Independent visual sample: about 24 long + 11 Shorts (campaign audit, 2026-11-08).
