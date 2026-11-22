# Motion windows v2 (2026-11-20): 341 windows, 15 videos
Up to 8 events per class per video; 34-frame windows; metric = share of pixels changing >16/255 between frames. Raw: `11_MOTION_WINDOWS.csv`. Script: `tools/measure_motion_windows.py`.

| Class | Windows | Videos | Median frames moving (p25-p75) |
|---|---:|---:|---|
| POP_IN | 120 | 15 | 2 (1-3) |
| POSE | 88 | 15 | 1 (1-2) |
| TEXT_SWAP | 55 | 7 | 1 (1-1) |
| ZOOM_IN | 29 | 7 | 1 (1-1): mostly cut plus tiny scale; true zooms are rare |
| POP_OUT | 17 | 4 | 2 (1-2) |
| SLIDE_IN | 10 | 3 | 15.5 (12-30) |
| TEXT_TYPE | 9 | 2 | 2 (1-6) |
| PAN | 5 | 1 | 31 (all in one Short) |
| RISE_IN | 3 | 1 | 15 (14-16) |
| DRAWON | 4 | 2 | 4 (4-8) |
| HOP_IN | 1 | 1 | 9 |

Easing fit (15 usable windows only; candidates linear, ease-out, ease-in, smoothstep on cumulative change or scale): linear 9, ease-out 4, smoothstep 2. Conclusion (MEASURED, small sample): the channel is mostly one-frame events; the few timed moves are mostly linear. No overshoot/follow-through was detected. Keyframe values are NOT recovered.

Limits: pixel change is not keyframe data; cut-adjacent windows are inflated; rare classes (PAN, RISE_IN, TEXT_TYPE, DRAWON) come from 1-3 videos each, so not generalisable.
