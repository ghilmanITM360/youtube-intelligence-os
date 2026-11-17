# Forensic review — 44ggG2I6JPY "The REAL Reason Everyone Is Panicking"

Status: `VISUAL_FORENSICS_COMPLETE_AT_DEPTH_B_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). Machine checks: all pass (`QA.json`).

## Source (MEASURED)
`The REAL Reason Everyone Is Panicking.mp4` (`CFSRC-032`), SHA256 `987f49cd...deb9e`, H.264/AAC, 720x1280, 30.0 fps, 3025 frames (decoded = ffprobe), 100.924 s. SHORT uploaded 2026-09-02, 47,329 views at the 2026-10-19 snapshot. Identity = title+duration match (not cryptographic). 

## Depth
DEPTH_C (cut-delimited scenes authored from a 2 s full-duration overview and the compact event sheets for events SE003-SE132; events not individually classified are kept as UNRESOLVED_CHANGE rows; caption words and sub-0.8% changes counted only). Audio: whole track measured (76 % voiced, 30 pauses >=0.25 s, 23 of them within 120 ms of a visual event) plus Whisper small.en; **not listened to**. Scenes are contiguous over frames 0-3024.

## Measured statistics
- 29 scenes (median 2.83 s, p10 1.37, p90 5.07, longest 15.23); 28 hard cuts (16.65/min); 81 events (48.16/min), 61 of them one-frame.
- Operations: UNRESOLVED_CHANGE 41, HARD_CUT_REPLACE 28, POP_IN 6, CAMERA_SCROLL_ZOOM 2, SCALE_TWEEN 1, TEXT_WRITE_ON 1, OVERLAY_POP 1, SLIDE_IN 1.
- Frame-weighted: static hold 92.0 %, plausibly conventional keyframe/compositing 5.6 %, screen recording 0.0 %, complex continuous animation 0.0 %, change of undetermined method 2.4 %; generated/video-based: none identified.
- Hard cuts relative to the nearest ASR word onset: median -27 ms (p10 -200, p90 53; negative = visual first; ASR uncertainty ~100 ms).
- Cadence: 24 fps timeline conformed to 30 fps by repeating every 5th frame (MEASURED: 19 of 29 duplicates share one phase mod 5; 5-frame gaps 18).

## Findings
- **Decode correction.** The first decode inserted one duplicate frame near f100 (3,026 vs 3,025 native frames) because ffmpeg's default frame-rate mode normalised an irregular timestamp; the pipeline now decodes with `-fps_mode passthrough` and this video was re-analysed; all frame numbers in the tables are native (`MEASURED`, QA check `decoded_frames_equal_ffprobe_frames`).
- **Layout.** 720p source. A two-line burned-in title ('the world's safest market is breaking') is present only for the first 6 s (f0-188), unlike the full-duration headline of `Qof71Ef-3EU` and `DEgQTSsSX9U`; after that the frame is full-bleed with hand-lettered captions (`DIRECTLY_OBSERVED`).
- **Sparse white compositions.** Scene changes replace small objects on white, so only ~7 % of the frame changes at a cut (versus 25-60 % on screenshot-heavy Shorts); the per-video cut/pop thresholds are therefore relative (`MEASURED`).
- **Meme and brand imagery.** A meme photograph ('Coincidence?' then 'I THINK NOT!', zoomed), the Avengers logo and the OECD logo carry jokes and authority beats; rights status unverified.
- **Reuse across videos.** The pension card with green check, bond tags, '?' circle, detective figure, blackboard presenter and the Earth with eyes recur from `DEgQTSsSX9U` and `Qof71Ef-3EU`; this video is a re-edit of the pension theme with 6 added country charts (`DIRECTLY_OBSERVED`).
- **No screen recording or generated motion identified.**

## Uncertainties (DEPTH_C)
41 detected changes (chart appearances, small slides, caption-chunk growth) are kept as UNRESOLVED_CHANGE rows and not classified; of the three event sheets only the first two were viewed; caption timing not measured; creator tools unknown; no listening; single reviewer.
