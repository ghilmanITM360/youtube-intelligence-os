# 03 — Technical ingestion, PTS, shot/event detection and temporal completeness

## Technical source profile

Record: source SHA256 bytes and path; filesize; ffprobe  version; container/duration/start time; video resolution/aspect/pixel format/codec; rational avg_frame_rate and r_frame_rate; video `time_base`; number of decoded frames if counted; keyframes; CFR/VFR assessment; source PTS/DTS anomalies; audio stream channels/sample rate/delay; title/thumbnail IDs; source registry mapping. Do not infer exact frame number as `seconds*30` on VFR material.

Recommended read-only probes (use `-show_frames` in bounded intervals; this can be expensive):

```bash
ffprobe -v error -show_streams -show_format -of json "$SRC"
ffprobe -v error -select_streams v:0 -show_frames -show_entries frame=best_effort_timestamp_time,pkt_duration_time,pict_type,key_frame -of json "$SRC"  # only for bounded/deep validation; large output
```

`ffprobe -read_intervals` may seek to nearby positions, not perfectly; anchor and verify actual returned source timestamps.

## State taxonomy

- `SHOT_CUT`: verified discontinuous edit; fade/wipe/dissolve are time ranges, not always one frame.
- `INTRA_SHOT_STATE`: composition, subject, expression or prop state changes while shot remains continuous.
- `CAMERA`: pan, tilt, digital zoom, dolly simulation, parallax, handheld-like drift (distinguish subject movement).
- `GRAPHIC/TEXT`: graphic enters/updates/leaves, number updates, kinetic type, chart bar/arrow.
- `CHARACTER`: pose swap, facial expression, contact, blink, gesture, weight-shift, silhouette.
- `LIGHT/COLOR/EFFECT`: palette switch, flash, blur, particles, lighting change, compositing effect.
- `AUDIO_CUE`: audible speech/music/SFX beat and synchronized visual state.
- `STATIC_HOLD`: deliberate continuation with no material state change (state durations matter).

## Candidate detection is NOT a true cut list

PySceneDetect ContentDetector uses HSV frame differences, AdaptiveDetector normalizes motion; both can mislabel rapid zoom as cuts and miss pose swaps. Run candidate detector for indexing; manually confirm before counting cuts/minute. Analyze frame-difference heatmaps, per-region changes, feature tracking or optical flow if installed/needed; no installation solely for speculative enhancement.

Example reported YIOS failure: one stepped zoom produced 8 false cuts, only about 5/15 Primitive pose changes detected. Include regression clips or reviewer notes, not a global promise about sensitivity.

## Full timeline coverage contract

- Video beginning and end inspected, every playback interval accounted for.
- One row per verified shot/state interval; no unexplained gaps or overlaps except explicitly parallel event tracks.
- Every meaningful candidate event resolved to `verified`, `rejected`, `uncertain`; uncertain means partial.
- For tiny overlays/gestures, inspect native consecutive frames until first/last source PTS confidently bracketed; state precision at actual PTS, not imaginary `00:00.000` timestamps.
- Preserve two layers: SHOT boundaries and independent overlapping EVENT intervals; a shot can contain 20 moving events without 20 cuts.
- Record time-source (frame PTS, file timebase, contact-sheet sample, model ASR, approximate visual estimate).
- Countable shot statistics only after verified boundary inventory; disclose coverage fraction.

## Example event (illustrative only)

`video=EXAMPLE; shot=S001; event=E014; type=TEXT_ENTER; onset_pts=4.233; offset_pts=5.067; source_frame_on=127; evidence=frames_0126_0129.jpg; status=MEASURED; confidence=HIGH; note=left-center value label slides from off-frame and holds.` These numbers are invented illustration, not observed YIOS data.

## Motion tracking cautions

Direct rendered camera motion may be mathematically indistinguishable from 2D scaling or object translation without source project. Describe visible pixel transformation separately from the likely implementation. Interpolated extraction frames are NOT original evidence; optical-flow trajectories are approximations; fixed lens focal length and exact easing curves require measurements/source files.
