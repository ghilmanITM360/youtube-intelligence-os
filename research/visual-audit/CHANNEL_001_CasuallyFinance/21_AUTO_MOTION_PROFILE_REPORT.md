# Automatic motion profile, all CasuallyFinance videos (2026-11-20)
Tool: `tools/auto_diff_series.py` (ffmpeg decode, 240 px grey, fraction of pixels changed by >16/255 between frames). Output: `21_AUTO_MOTION_PROFILE_ALL_VIDEOS.csv`, one row per distinct video ID (162 IDs from the 216 files; duplicate files share an ID). MEASURED for pixel change; no human or frame review.

## Calibration (what the number means)
- A first threshold (25% of pixels), taken from the long videos, gave 0 events for most Shorts because Short frames change only a few percent. It was wrong for Shorts and was dropped.
- Threshold 2% of pixels, checked against the 15 ledger videos (4 Shorts, 11 long): correlation with ledger shots per minute 0.78 (n=15). The auto event count is about 1.9x the ledger shot count, because pop-ins and pose changes count as events but are not new shots.
- So `change_events_per_min` is a rough editing-pace index. It is NOT a shot count. 15 videos, mostly long, is a thin check for 139 Shorts.

## Result
| Group | n | change events/min (p10 / median / p90) | still frames (median) |
|---|---:|---|---:|
| Short | 139 | 18.5 / 34.1 / 70.4 | 85.6% |
| Long | 24 | 19.5 / 38.6 / 46.3 | 87.9% |

Reading: pace is similar between Shorts and long videos, and about 86-88% of frames are fully still (matches the earlier finding that the style is mostly static with brief changes). The Short spread is wide (18-70 events/min), so Shorts are not one uniform style; the 4 ledger Shorts cannot say why.

Not covered: shot boundaries, asset types, text, design system for the 143 videos with no ledger. Score unchanged at 59/100.
