# CT_SCAN pilot: video 9VG0yqq_PHM (toaster in a freezer), 162.26 s

Status: **CT_SCAN complete for this one video, self-review, one coder.** Every native frame was measured by the machine and (in later passes, see `span_960_1679/SPAN_REPORT.md` and `ALL_FRAMES_VIEW_REPORT.md`) all 3,893 frames were viewed at 192x108 and differenced at full resolution. This report's sections 2 to 3 describe the first pass (104 change windows, 10.5% of frames viewed); two corrections and five added small events are in `ALL_FRAMES_VIEW_REPORT.md` and `visual_event_ledger_ct.csv`. No audio listened. Describes devices; no artwork or script reproduced.

## 1. Source (MEASURED)
- File in the media library, sha256 `1a5c6363860a5c2c90c608602c8c9a9e3a8241238c8d75d0d4c94a16ac6016ac` (`source_manifest.json`), 24 fps constant (one PTS step, 0.04167 s), **3,893 decoded frames**, 162.26 s.
- Why this video: the shortest of the 24 long videos that have a campaign ledger (so the result can be compared with a reviewed ledger).

## 2. What was done to each frame
1. **Every frame** decoded and differenced against the previous one at 256x144 grey (`per_frame_table.csv`: 3,893 rows with PTS, picture type, changed fraction, ink delta, bounding box, cut candidate, state, event id).
2. **Two thresholds:** the frozen ledger rule (pixel change above 24 grey levels, at least 0.04% of pixels) gives 64 strong events; a second, more sensitive layer (change above 2 grey levels, at least 15 pixels, outside strong events) adds 40 faint spans. Together **104 change spans**; every frame belongs to exactly one state interval (HOLD, EVENT or FAINT; `state_intervals.csv`, 189 intervals).
3. **Windows viewed:** for each of the 104 spans, up to 8 native frames (the frame before onset, evenly spaced frames inside, the frame after the end) at 200x112, in 18 sheets (`sheet_01-18.jpg`, 6 spans per sheet, one span per row, order = `events_machine.csv`). 407 distinct frames viewed = 10.5% of all frames; 244 of the 286 frames inside change spans. Coded in `visual_event_ledger_ct.csv`; shots in `shot_ledger_ct.csv`.

## 3. Findings
**Time structure (MEASURED, 3,893 frames):**
- 3,607 frames (92.7%) are holds, 136 (3.5%) are strong-event frames, 150 (3.9%) are faint-change frames. 83 hold intervals: median 36 frames (1.5 s), longest 186 frames (7.75 s).
- Strong events are short: **50 of 64 last one frame**; the longest 14 frames. Inside a change the picture moves on every frame (gaps between changing frames at the sensitive threshold: 184 are 1 frame; the next most common, 2 frames, occurs 8 times), i.e. animation is on ones at 24 fps, not stepped; between changes the picture is still.

**What the changes are (OBSERVED, 104 spans):** 18 object pop-ons, 13 label pop-ons, 7 typed-text write-ons (about one character per frame; a 3-frame label "600 C", a 6-frame sentence), 4 line write-ons (arrows and heat marks growing over 4 to 9 frames), 4 state swaps (toaster fills red, door closes), 5 pose swaps (one frame), 4 progressive red-glow fades (6 to 13 frames), 1 dim-to-grey fade (6 frames), 1 pose cross-dissolve (8 frames), 1 zoom dissolve (8 frames), 11 hard cuts (including the cut to the red series title card and the cut to the end card), 1 scene pop-on, title-card animation spans (5), plus 27 faint spans with no visible change at 200 px (codec shimmer or sub-visible).
- **Written text arrives either as a whole label in one frame or typed on at about one character per frame**; shapes arrive whole in one frame; only glows, dims, dissolves and arrow growth are gradual.
- **The detector at the frozen threshold misses gradual changes:** 13 of 77 visible changes (17%) were found only by the sensitive layer (red-glow fades, arrow growth, a pose dissolve, title-card animation). The measured ledgers for the other 44 videos use the frozen threshold, so their events undercount gradual changes. Not quantified for them.
- **Shot boundaries:** the machine flagged 13 cut candidates: **11 are hard cuts** and 2 are not (an 8-frame zoom dissolve, a 6-frame dim fade). So 85% on this video; shots = 12, median 11.2 s (campaign 9 boundaries). All 9 campaign boundaries match mine (within 2 frames); I see 2 more that are visually clear cuts (frame 672, a white scene to a grey scene; frame 778, the title card to the fridge scene); the campaign may have merged them; not resolved.
- **Against the campaign events (tolerance 3 frames):** campaign 72 events, my visible changes 77, 66 match both ways (recall 92%, precision 86%).
- **Structure of the video:** question card typed in for the first 4 s, a kitchen scene built object by object (toaster, labels, steam), a 3 s red series title card at 30.4 s (cut in, cut out), a temperature axis built label by label, a series of cuts to scenes with one object each, a closing red end card with credits and book covers for the last 10.05 s (starts frame 3653, 152.21 s).

## 4. Limits (do not skip)
- **Superseded:** this first pass viewed 10.5% of frames; the later passes viewed all of them (see top).
- (First-pass note) Not every frame was viewed (10.5%). Unviewed frames are holds at the detector thresholds plus 42 change-span frames between sampled window frames. A change below both thresholds would be missed.
- 200x112 windows: small marks and fine text are below what I can read; those rows carry LOW confidence (`confidence` column).
- One coder, no second reviewer. No audio. Camera motion not assessed (only the zoom dissolve was seen).
- One video. Do not generalize rates to the channel.
- Shot and event classes use my own vocabulary, close to the campaign's; not the same as the campaign's classes.

## 5. Next frame range and recompute
`continuation_handoff.md`. Recompute: `uv run --no-project --with numpy python scripts/ct_pilot.py 9VG0yqq_PHM` then view the sheets and run `python3 scripts/ct_pilot_code.py` (the coding is in the script).
