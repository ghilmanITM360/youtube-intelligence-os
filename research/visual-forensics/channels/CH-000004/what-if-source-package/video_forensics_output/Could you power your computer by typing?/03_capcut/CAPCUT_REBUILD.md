# WAY 1 — CapCut reconstruction

## Project setup

- Canvas/aspect: 9:16 portrait. Resolution: 1080 × 1920. FPS: 24. Length: 2,419 frames (01:40.792 rounded).
- Background: E01 matched off-white; E02 for S12. Master audio: none in supplied source; leave A1/A2 empty.
- Global text system: T01. Original font UNKNOWN; source-derived/traced lettering gives the closest match. Editable native text is an approximation, matched by width, baseline and stroke weight.
- Global color: source-matched off-white, black and muted red. Global effects: NONE. Apply G14 only at its listed events.
- Import source as a temporary alignment/reference track, then hide it for export. Import the saved representative PNGs and the overlays specified in the manifest. Rebuilding still artwork and masks is the deliverable method; merely exporting the source video is not a reconstruction.

## Media to import

The following IDs are defined once in [ASSET_MANIFEST.csv](../02_analysis/ASSET_MANIFEST.csv). Import the indicated formats and variants. Source-aligned full-frame PNGs are easiest to register; when cropping a local overlay, preserve its original source position. Background and a stationary illustration can share one plate. Only changing components need separate tracks.

| Asset | Required import |
|---|---|
| E01 | SHAPE / PNG |
| E02 | PNG |
| E03 | GENERATED_IMAGE / PNG |
| C01 | PNG |
| C02 | PNG variants |
| C03 | PNG variants |
| C04 | PNG |
| C05 | PNG variants |
| O01 | PNG / full-frame still |
| O02 | PNG variants |
| O03 | PNG |
| O04 | PNG / full-frame still |
| O05 | PNG / SCREENSHOT |
| O06 | PNG |
| O07 | PNG / SCREENSHOT |
| O08 | PNG / full-frame still |
| O09 | PNG variants |
| O10 | PNG |
| O11 | PNG / full-frame still |
| O12 | PNG variants |
| O13 | PNG variants |
| O14 | PNG / SCREENSHOT |
| O15 | PNG variants |
| G01 | PNG variants / TEXT |
| G02 | PNG |
| G03 | PNG / TEXT |
| G04 | PNG / TEXT |
| G05 | PNG / SHAPE |
| G06 | PNG |
| G07 | PNG strips / SHAPE |
| G08 | PNG / TEXT |
| G09 | PNG / TEXT |
| G10 | PNG / TEXT |
| G11 | PNG / TEXT |
| G12 | PNG / TEXT |
| G13 | PNG / TEXT |
| G14 | PNG / SHAPE / MASK |
| G15 | PNG / TEXT |
| G16 | PNG / TEXT |
| T01 | TEXT / transparent PNG strips |

## Frame-accurate assembly rules

1. Set still duration by frame count, not a rounded decimal drag. All times below are global. Use timeline row boundaries for exact clip lengths. Hard cuts get zero transition duration.
2. Register every full-frame source-aligned plate at 100% scale, center (0,0), zero rotation. When artwork is recreated at different bounds, match the evidence overlay at 50% opacity, then remove the alignment overlay. Positions/crop matches are APPROXIMATE until verified against the reference.
3. For a state replacement, split at the A-ID IN frame and start the new PNG/overlay at full opacity. Do not interpolate position or add stock entrance animation. The one-frame event interval records the change; keep its result until the next applicable event.
4. For reveals, animate a hard mask or crop over fixed artwork. A moving cover matching the background is an alternative when that version cannot keyframe a mask. For complex curves, a short sequence of traced progression PNGs gives tighter control inside CapCut.
5. For S07 use separate black text strips and red stroke layers. Preserve source baselines and line breaks; do not allow auto-wrapping or automatic caption layout. Per-frame x extents are available in the evidence CSV. Do not confuse a wipe through letters with a new hand-writing animation.
6. End with a held image on frame 2418. Export MP4/H.264, 1080×1920, 24 fps, no added audio. Check that the export contains 2,419 frames.

CapCut capability references: [official desktop keyframe help](https://www.capcut.com/help/keyframes-in-capcut-pc) supports position/scale/opacity controls; [official editing guide](https://www.capcut.com/resource/how-to-use-capcut) covers masks. These establish available reconstruction controls, not the original production software. UI wording can differ by version.

## S01 — 00:00.000–00:04.500

SOURCE STATES: F01.0 → F01.1 → F01.2

MEDIA: E01, C01, C02, O01, G01, T01

TRACK STACK: V3 G01; V2 C01/C02/O01 board scene (one fixed plate allowed); V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F01.0 evidence](../01_evidence/frames/f0000_00000.000s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.

| Event | Global change interval | CapCut action |
|---|---|---|
| A01 | 00:01.292–00:01.333 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A02 | 00:02.875–00:02.917 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |

KEYFRAMES: NONE; state changes are clip/overlay boundaries.
TOOLS: overlay, split/trim, crop/mask
TEXT: Exact wording and placement are canonical in the S01 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Start directly on first drawing. Hard cut to S02 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F01.2.

## S02 — 00:04.500–00:07.625

SOURCE STATES: F02.0 → F02.1 → F02.2

MEDIA: E01, O02, O03, T01

TRACK STACK: V3 TAP/leader and probe; V2 O02 key-state plate; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F02.0 evidence](../01_evidence/frames/f0108_00004.500s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. The probe does not descend smoothly: use the hover variant, then the pressed contact plate. Replace the dome as well as the cap; a mere downward translation would retain the wrong geometry.

| Event | Global change interval | CapCut action |
|---|---|---|
| A03 | 00:05.667–00:05.708 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A04 | 00:06.500–00:06.542 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |

KEYFRAMES: NONE; state changes are clip/overlay boundaries.
TOOLS: overlay, split/trim, crop/mask
TEXT: Exact wording and placement are canonical in the S02 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S03 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F02.2.

## S03 — 00:07.625–00:10.375

SOURCE STATES: F03.0

MEDIA: E01, C02, O04, G02

TRACK STACK: V2 fixed C02/O04/G02 plate; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F03.0 evidence](../01_evidence/frames/f0183_00007.625s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.

ANIMATION REQUIRED: NO. Hold the source plate for this whole shot.

KEYFRAMES: NONE; state changes are clip/overlay boundaries.
TOOLS: still image, trim
TEXT: Exact wording and placement are canonical in the S03 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S04 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F03.0.

## S04 — 00:10.375–00:19.292

SOURCE STATES: F04.0 → F04.1 → F04.2

MEDIA: E01, O05, G03, T01

TRACK STACK: V3 G03 annotation groups; V2 O05; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F04.0 evidence](../01_evidence/frames/f0249_00010.375s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. Keep keyboard/paper angle fixed. Annotation subgroups are coupled onset events. The research-paper body is squiggle artwork, not text to invent.

| Event | Global change interval | CapCut action |
|---|---|---|
| A05 | 00:14.250–00:14.292 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A06 | 00:16.417–00:16.458 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |

KEYFRAMES: NONE; state changes are clip/overlay boundaries.
TOOLS: overlay, split/trim, crop/mask
TEXT: Exact wording and placement are canonical in the S04 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S05 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F04.2.

## S05 — 00:19.292–00:30.042

SOURCE STATES: F05.0 → F05.1 → F05.2 → F05.3

MEDIA: E01, C05, O06, G04, G05, T01

TRACK STACK: V4 G04 title/captions; V3 C05 and G05 replacement region; V2 O06; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F05.0 evidence](../01_evidence/frames/f0463_00019.292s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. Use the actual second squirrel region at the final replacement. Do not turn the caption’s upward arrow into a visible hop.

| Event | Global change interval | CapCut action |
|---|---|---|
| A07 | 00:21.125–00:21.167 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A08 | 00:24.083–00:24.125 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A09 | 00:27.667–00:27.708 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |

KEYFRAMES: NONE; state changes are clip/overlay boundaries.
TOOLS: overlay, split/trim, crop/mask
TEXT: Exact wording and placement are canonical in the S05 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S06 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F05.3.

## S06 — 00:30.042–00:35.833

SOURCE STATES: F06.0 → F06.1 → F06.2 → F06.3 → F06.4

MEDIA: E01, O07, G06, T01

TRACK STACK: V4 G06 arrows; V3 headline; V2 O07 with page text and lower label; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F06.0 evidence](../01_evidence/frames/f0721_00030.042s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. For exact book body, retain the evidence crop. Recreated tiny text will alter the picture. Masks reveal red arrows; no book opening/page movement.

| Event | Global change interval | CapCut action |
|---|---|---|
| A10 | 00:31.125–00:31.417 | Place exact headline artwork at its reference box; animate a hard rectangular reveal mask horizontally for 7 frames, fully visible on f753. |
| A11 | 00:31.750–00:32.042 | Overlay traced red-arrow PNG. Reveal it in the observed order with short crop/mask segments; use saved adjacent frames for the final 7-frame progression. |

KEYFRAMES: Only mask extent for the reveal events above.
TOOLS: overlay, split/trim, crop/mask, text or traced text PNG
TEXT: Exact wording and placement are canonical in the S06 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S07 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F06.4.

FIDELITY LIMITATION: Dense page lettering requires source-derived art for an exact match.

## S07 — 00:35.833–00:43.542

SOURCE STATES: F07.0 → F07.1 → F07.2 → F07.3 → F07.4 → F07.5 → F07.6 → F07.7 → F07.8 → F07.9 → F07.10 → F07.11 → F07.12 → F07.13 → F07.14 → F07.15 → F07.16 → F07.17 → F07.18 → F07.19 → F07.20 → F07.21 → F07.22 → F07.23 → F07.24 → F07.25 → F07.26 → F07.27 → F07.28 → F07.29 → F07.30 → F07.31 → F07.32 → F07.33 → F07.34 → F07.35 → F07.36 → F07.37 → F07.38 → F07.39 → F07.40 → F07.41 → F07.42

MEDIA: E01, T01, G07

TRACK STACK: V3 G07 separate red stroke strips; V2 separate black T01 word/line strips; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F07.0 evidence](../01_evidence/frames/f0860_00035.833s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. Use the final source plate for alignment only. Split black wording into the sequential chunks named in the motion map; a single mask on the entire final plate would reveal red strikes too soon. Black and red need independent tracks on overlapping frames. Y bands and per-frame extents in text_reveal_measurements.csv are in original 1080×1920 source pixels.

| Event | Global change interval | CapCut action |
|---|---|---|
| A12 | 00:35.833–00:36.250 | Use separate black artwork strip for line 1; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A13 | 00:36.250–00:36.375 | Use separate red artwork strip for line 1; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A14 | 00:36.375–00:36.500 | Use separate black artwork strip for line 1; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A15 | 00:36.542–00:36.667 | Use separate red artwork strip for line 1; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A16 | 00:36.667–00:36.917 | Use separate black artwork strip for line 1; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A17 | 00:36.917–00:37.125 | Use separate black artwork strip for line 2; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A18 | 00:37.167–00:37.292 | Use separate red artwork strip for line 2; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A19 | 00:37.292–00:37.667 | Use separate black artwork strip for line 2; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A20 | 00:37.667–00:37.792 | Use separate red artwork strip for line 2; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A21 | 00:37.792–00:38.250 | Use separate black artwork strip for line 2; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A22 | 00:38.250–00:38.458 | Use separate red artwork strip for line 2; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A23 | 00:38.458–00:38.917 | Use separate black artwork strip for line 3; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A24 | 00:39.208–00:39.708 | Use separate black artwork strip for line 4; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A25 | 00:39.708–00:40.333 | Use separate black artwork strip for line 5; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A26 | 00:41.208–00:41.542 | Use separate black artwork strip for line 6; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A27 | 00:41.500–00:41.667 | Use separate red artwork strip for line 6; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A28 | 00:41.667–00:41.958 | Use separate black artwork strip for line 7; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A29 | 00:41.917–00:42.125 | Use separate red artwork strip for line 7; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A30 | 00:42.083–00:42.375 | Use separate black artwork strip for line 8; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A31 | 00:42.375–00:42.583 | Use separate red artwork strip for line 8; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A32 | 00:42.542–00:42.833 | Use separate black artwork strip for line 9; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A33 | 00:42.833–00:43.000 | Use separate red artwork strip for line 9; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A34 | 00:43.000–00:43.292 | Use separate black artwork strip for line 10; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |
| A35 | 00:43.250–00:43.458 | Use separate red artwork strip for line 10; rectangular mask progresses left-to-right. Match per-frame extent in text_reveal_measurements.csv; leave all completed strips on screen. |

KEYFRAMES: Only mask extent for the reveal events above.
TOOLS: overlay, split/trim, crop/mask, text or traced text PNG
TEXT: Exact wording and placement are canonical in the S07 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S08 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F07.42.

FIDELITY LIMITATION: Native text/font and a generic typewriter preset will not reproduce exact glyphs and stroke timing; use the measured strips/masks.

## S08 — 00:43.542–00:56.917

SOURCE STATES: F08.0 → F08.1 → F08.2 → F08.3 → F08.4 → F08.5 → F08.6 → F08.7

MEDIA: E01, C02, O08, O09, O10, G08, T01

TRACK STACK: V4 G08 labels/arrows; V3 O09 count variants and O10; V2 C02/O08 fixed plate; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F08.0 evidence](../01_evidence/frames/f1045_00043.542s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. Keep all book variants resting on the same tabletop. The one-to-two-to-three progression has no slide/bounce. Ten books appear as a single replacement, not seven individually falling books.

| Event | Global change interval | CapCut action |
|---|---|---|
| A36 | 00:46.167–00:46.208 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A37 | 00:47.750–00:47.792 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A38 | 00:49.208–00:49.250 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A39 | 00:49.375–00:49.417 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A40 | 00:50.125–00:50.167 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A41 | 00:51.708–00:51.750 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A42 | 00:53.917–00:53.958 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |

KEYFRAMES: NONE; state changes are clip/overlay boundaries.
TOOLS: overlay, split/trim, crop/mask
TEXT: Exact wording and placement are canonical in the S08 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S09 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F08.7.

## S09 — 00:56.917–01:06.792

SOURCE STATES: F09.0 → F09.1 → F09.2 → F09.3

MEDIA: E01, C02, O11, O12, O13, G09, T01

TRACK STACK: V4 G09 labels; V3 O12 cable/plug and C02/O13 pose patch; V2 O11 and starting C02; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F09.0 evidence](../01_evidence/frames/f1366_00056.917s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. A local replacement must erase old arm/head lines before the new reading pose is placed. Use a source-matched opaque patch or clean base beneath transparent pose. Retain cable, laptop and right-hand book.

| Event | Global change interval | CapCut action |
|---|---|---|
| A43 | 00:58.250–00:58.292 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A44 | 01:00.875–01:00.917 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A45 | 01:02.417–01:02.458 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |

KEYFRAMES: NONE; state changes are clip/overlay boundaries.
TOOLS: overlay, split/trim, crop/mask
TEXT: Exact wording and placement are canonical in the S09 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S10 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F09.3.

## S10 — 01:06.792–01:10.583

SOURCE STATES: F10.0 → F10.1

MEDIA: E01, O14, C02, O15, G10, G11, T01

TRACK STACK: V3 G11/C02/O15 lower callout; V2 O14/G10 calendar group; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F10.0 evidence](../01_evidence/frames/f1603_00066.792s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. The lower callout appears as a full group. No typing-hand animation is observed.

| Event | Global change interval | CapCut action |
|---|---|---|
| A46 | 01:09.042–01:09.083 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |

KEYFRAMES: NONE; state changes are clip/overlay boundaries.
TOOLS: overlay, split/trim, crop/mask
TEXT: Exact wording and placement are canonical in the S10 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S11 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F10.1.

FIDELITY LIMITATION: Tiny calendar dates/year cannot be verified as prose; preserve the source calendar crop.

## S11 — 01:10.583–01:31.125

SOURCE STATES: F11.0 → F11.1 → F11.2 → F11.3 → F11.4 → F11.5 → F11.6 → F11.7 → F11.8 → F11.9 → F11.10 → F11.11 → F11.12 → F11.13

MEDIA: E01, C03, O15, G01, G12, G13, G14, T01

TRACK STACK: V6 G14 dark/light treatment; V5 headline G13; V4 G01 cloud variants; V3 C03 pose; V2 O15/G12; V1 E01. Keep G12 above any background words crossing its clear band. A1/A2 empty.

INITIAL COMPOSITION: Register [F11.0 evidence](../01_evidence/frames/f1694_00070.583s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. Keep cloud increments separate and persistent, including the small additions during the dark hold. Use an opaque registered patch or clean base for the pose swap so old arms do not remain. The monitor light is stationary; do not add flicker.

| Event | Global change interval | CapCut action |
|---|---|---|
| A47 | 01:14.667–01:14.875 | Use the completed cloud as a separate layer; expand a hard mask from the middle to its reference bounds over 5 frames. |
| A48 | 01:17.708–01:17.875 | Separate exact headline PNG from new cloud PNG. Expand hard masks over both for 4 frames; match saved f1865–1868. |
| A49 | 01:20.000–01:20.042 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A50 | 01:21.250–01:21.292 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A51 | 01:22.042–01:22.292 | Place dark treatment above artwork: black overlay APPROX 82% opacity plus bright duplicate below/inside feathered oval mask centered on face/monitor. Start 0% on f1968; reach matched dark treatment on f1974. Keep geometry locked. |
| A52 | 01:23.292–01:23.333 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A53 | 01:23.500–01:23.542 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A54 | 01:25.458–01:25.708 | Hold dark composite through f2050; reduce its opacity to 0% on f2056. Match inverse of entry; no zoom. |
| A55 | 01:27.250–01:27.292 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |

KEYFRAMES: Only mask extent for the reveal events above; G14 opacity at f1968/1974 and f2050/2056.
TOOLS: overlay, split/trim, crop/mask, opacity keyframes and feathered mask, text or traced text PNG
TEXT: Exact wording and placement are canonical in the S11 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S12 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F11.13.

FIDELITY LIMITATION: A feathered oval plus opacity is an approximation to the source light falloff. Match dark endpoint against saved evidence; original effect settings are UNKNOWN.

## S12 — 01:31.125–01:35.667

SOURCE STATES: F12.0 → F12.1 → F12.2 → F12.3

MEDIA: E02, C02, O01, O12, O13, G01, G15, G14

TRACK STACK: V5 G15 label/book ticks; V4 G01 and O13 icon; V3 O12/G14 cable/light patch; V2 C02/O01; V1 E02. A1/A2 empty.

INITIAL COMPOSITION: Register [F12.0 evidence](../01_evidence/frames/f2187_00091.125s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. The cable and light pool appear instantly together; do not fade the light on. The book icon stays suspended without rotation/travel after onset.

| Event | Global change interval | CapCut action |
|---|---|---|
| A56 | 01:31.500–01:31.542 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A57 | 01:33.750–01:33.792 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |
| A58 | 01:34.542–01:34.583 | At the event IN frame, start the indicated overlay or replace its local still; hold unchanged. Use no entrance animation or interpolated transform. |

KEYFRAMES: NONE; state changes are clip/overlay boundaries.
TOOLS: overlay, split/trim, crop/mask
TEXT: Exact wording and placement are canonical in the S12 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hard cut to S13 at shot OUT.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F12.3.

## S13 — 01:35.667–01:40.792

SOURCE STATES: F13.0 → F13.1 → F13.2

MEDIA: E01, E03, C02, C04, O13, G16, T01

TRACK STACK: V3 G16 caption; V2 E03/C02/C04/O13 fixed outdoor plate; V1 E01. A1/A2 empty.

INITIAL COMPOSITION: Register [F13.0 evidence](../01_evidence/frames/f2296_00095.667s.png) full-frame at 100%, centered. Exact composition is the corresponding TIMELINE row; do not add a reframing keyframe.

BUILD:
1. Trim the base plate to this shot’s canonical duration. Separate the changing media onto the listed overlay tracks.
2. Apply the event operations below in order; keep each completed layer visible unless that event explicitly replaces it.
3. Hold the entire outdoor drawing still, including the runner, leaves and grass. Reveal both caption lines together, not one after another.

| Event | Global change interval | CapCut action |
|---|---|---|
| A59 | 01:37.167–01:37.458 | Use exact two-line caption artwork. One hard vertical reveal mask uncovers both lines together for 7 frames; fully visible f2338. |

KEYFRAMES: Only mask extent for the reveal events above.
TOOLS: overlay, split/trim, crop/mask, text or traced text PNG
TEXT: Exact wording and placement are canonical in the S13 rows of TIMELINE.csv; T01 applies. Use saved source lettering/crops for exact shape. Text in unchanged assets stays fixed; the event table governs every change.
TRANSITION: Hard cut in on shot IN. Hold to end of file; no exit fade.
AUDIO SYNC: Visual cues only; see AUDIO_MAP.md. No source sound is present.
END STATE: F13.2.

## Completion check

Compare exported frame counts and cut positions with TIMELINE.csv. Inspect every A-ID first/last frame, especially two-book duration, overlapping S07 strokes, dark-hold cloud additions and instant pose changes. Confirm zero added camera motion. This is a complete manual build specification; no CapCut project or final export is claimed to have been produced.
