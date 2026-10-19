# Forensic review — Qof71Ef-3EU "The Cheap Money Era Is Coming to an End"

Status: `VISUAL_FORENSICS_COMPLETE_AUDIO_LISTENING_BLOCKED` (single reviewer, no independent QA). See `QA.json` (all machine checks pass).

## Source
`The-Cheap-Money-SnapYT.App.mp4` (`CFSRC-037`), SHA256 `273fd644...97e3`, H.264/AAC, 360x640, 30 fps, 2,049 frames (decoded 2,049 = ffprobe 2,049), 68.352 s. Public snapshot: Short uploaded 2026-09-08, 375,765 views. Only a 360p copy exists locally; this was previously selected (Oct-12) and blocked as `MISSING_LOCAL`. Identity = title+duration match (not cryptographic).

## What was done (five passes)
- **A** Narrative: 69 overview frames at 1 fps over the full duration, then 35 scenes.
- **B** Automated: every native frame decoded at 180x320; change detection split into header (y 0.20-0.30), stage (0.30-0.665) and caption (0.665-0.80) bands: 47 stage events, 226 caption change frames, header changed in 0 frames.
- **C** Fine: native-resolution sheets with the frame before, each active frame, the frame after and a hold frame for all 47 auto events; consecutive frames for the bag run cycle; numerical tracking for the zoom, pointer and highlight events.
- **D** Audio: whole track measured (RMS, 18 pauses >=0.25 s, spectrogram) plus Whisper small.en. **Not listened to.**
- **E** Chronology: scene timeline covers frames 0-2,048 contiguously; every stage-active frame lies inside an authored event; the check found one mislocated cut (S07 start f347 -> f339) which was corrected. I did not play the video back; static holds are verified by zero stage change, not by viewing each frame.

## Findings
**Layout (`DIRECTLY_OBSERVED`).** A two-line headline sits at y 0.206-0.294 for the entire video with zero pixel change. The stage occupies y 0.30-0.665 on a white canvas; captions sit at y ~0.69-0.77 and end at f1884 (62.8 s): the last 5.5 s of speech (three sentences) carry no captions.

**Cutting (`MEASURED`).** 33 hard cuts (29.0/min), 35 scenes, median scene 1.72 s. Every cut replaces the whole stage in one frame with no fade or blend (1.7k-16k of ~21k stage pixels change at cut frames). One cut passes through a blank stage frame (f87). Additive builds use single-frame pops: 14 `POP_IN` and 4 `OVERLAY_POP` events, with no visible scale or fade tween at 30 fps sampling.

**Native cadence (`MEASURED`).** 52 of 55 isolated duplicate frames in motion segments fall on frame indices divisible by 5, spaced exactly 5 frames apart (44 times): a 24 fps timeline conformed to 30 fps by repeating every fifth frame (`PLAUSIBLE_HYPOTHESIS` that the project was authored at 24 fps; the long-form videos are mostly 24 fps). Author at 24 fps and expect 30 fps delivery to repeat frames.

**Continuous motion (`MEASURED`).**
- ME014 push-in on OECD Fig 1.8: scale 1.00 -> 1.43 over 1.7 s (tracker 1.434, independent ink-bbox height ratio 1.401) with a leftward drift; speed ~constant for ~20 frames then decays; best named curve ease-out quad (RMSE 0.057) but not a clean fit.
- ME045 push-in on Fig 1.20: scale 1.00 -> 1.52 over 0.87 s, **linear** (RMSE 0.018); warping the first frame by the estimated transform cut residual MSE from 1,964 to 354.
- ME010 red arrow: x 0.479 -> 0.840 of frame width over 2.43 s, **linear** (RMSE 0.007), 0.151 widths/s, tracking the blue line (y +0.021).
- ME012 strip reveal: one front sweeps x 0.04 -> 0.96 in 64 frames (0.0146 w/frame) and extends the chart lines as it passes.
- ME041/ME042 highlighter: orange area grows ~3.1 px/frame over 12 and 15 frames.
- ME017-ME019: the FRED chart's hover cursor/tooltip steps along the series (`DIRECTLY_OBSERVED`); that it is a recorded browser interaction is a `PLAUSIBLE_HYPOTHESIS`.
- ME031: three bag characters change limb poses on every source frame while translating; one exits left and re-enters (loop). Rig pose-swaps, hand-drawn frames or a generated clip cannot be distinguished here.

**Expression swaps (`DIRECTLY_OBSERVED`).** ME004 (US-map eyes wide -> half-lidded, f163) and the Earth's eyes at f951 swap in one frame; bodies unchanged.

**Captions (`MEASURED`).** 214 word-appearance events in 37 chunks (median 5 words, p10 3, p90 9, max 14 in two-line chunks); each word appears whole in one frame. Aligned to ASR onsets: median +33 ms (1 frame), p10 -27 ms, p90 +133 ms, 79.7 % within +-100 ms (ASR uncertainty ~100 ms). The count is lower than the 244 ASR tokens because the closing sentences are uncaptioned.

**Narration sync (`MEASURED`).** Median hard cut precedes the nearest ASR word onset by 87 ms; 10 of 33 cuts land within 120 ms of the end of a >=0.25 s pause. Visuals lead or meet the spoken word; none lag it by more than ~12 ms at the 90th percentile.

**Audio (`MEASURED`, not listened).** 77 % of 50-ms windows are voiced; 18 pauses of 0.25-0.35 s; pauses sit ~20 dB below speech. The spectrogram shows speech striations and no sustained tonal bed. No SFX transient distinguishable from speech onsets was found (cut-time spectral flux median 2.96 vs 1.87 at random times, confounded by speech onsets). Presence of music or SFX is therefore `NOT_DETECTED`, not `ABSENT`.

## Motion-method classification (this video only)
Frame-weighted (each frame to its most complex active event): static hold 83.0 %, plausibly conventional keyframe/compositing 11.4 %, recorded screen capture 3.1 %, more complex continuous animation 2.5 %, possible generated/video-based 0.0 % identified, indeterminate counted inside the 2.5 %. Of the 17 % of screen time with any motion: conventional ~67 %, screen recording ~18 %, complex/indeterminate ~15 %. Event counts: 63 events, 54 of them one-frame (cuts, pops, swaps), 9 with duration. This is one video; it neither supports nor refutes the owner's 70-80 / 10-20 hypothesis channel-wide.

## Uncertainties
360p source limits line-weight and sub-10-px motion measurement; sub-8-px stage changes (129 frames) are not classified; ME017-ME019 mechanism unknown; ME031 method unknown; authoring tools unknown; the header/title mismatch is unexplained; no independent reviewer; no listening.
