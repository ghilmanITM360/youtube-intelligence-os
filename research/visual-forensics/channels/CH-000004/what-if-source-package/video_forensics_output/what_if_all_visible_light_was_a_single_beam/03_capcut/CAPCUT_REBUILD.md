# WAY 1 — CapCut Rebuild

Reference `02_analysis/TIMELINE.csv`, `02_analysis/ASSET_MANIFEST.csv`, `02_analysis/MOTION_EVENTS.csv`, `05_audio/AUDIO_MAP.md` for canonical facts; this file gives only the CapCut build actions. Import `AU01` (the original audio track, or a re-recorded/licensed replacement — see NOTE below) onto A1 for the full project length before building any shot.

**NOTE on audio:** no transcript exists (see `05_audio/AUDIO_MAP.md`). Every AUDIO SYNC line below cues off the five *measured* silence gaps and off "continuous mixed audio" generically — do not attempt to cut on specific words.

## S01 — 0:00.000–0:06.567
SOURCE STATES: F01.0 → F01.1 → F01.2
MEDIA: E01, C01, G01, G02, G03, T01
TRACK STACK: V1 chalkboard background (E01) · V2 stick figure (C01) · V3 sun icon (G01) + earth icon (G02) · V4 beam/cone (G03) · V5 text (T01)
INITIAL COMPOSITION: E01 full-frame; C01 lower-third, centered; G01 upper-left; G02 mid-right; T01 top-right of G02.
BUILD:
1. Place E01 on V1 for the full shot duration; place C01 on V2, static.
2. Place G01/G02 on V3, static; add T01 on V5 reading "UN-SUN-SPECTING EARTH".
3. At 0:02.000 cut V4 in: draw/overlay a widening cone from G01 to G02 (opacity 0→100 over ~6 frames); swap T01 text to "UNINHABITABLE EARTH" at the same timestamp.
4. At 0:04.000 animate the cone (V4) narrowing to a thin line via a mask/scale keyframe; add a small "1m" bracket text element next to G02.
KEYFRAMES: V4 opacity 0→100 at 0:02.000 (A01); V4 width scale 100%→20% between 0:04.000 and 0:04.200 (A02, fastest defensible interpretation of a same-second reveal).
TEXT: "UN-SUN-SPECTING EARTH" (0:00.000-0:02.000) → "UNINHABITABLE EARTH" (0:02.000-0:06.567) → "1m" bracket label appears 0:04.000.
TRANSITION IN: hard cut (video start). TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio under the whole shot; no measured silence in this range.
END STATE: F01.2.

## S02 — 0:06.600–0:15.900
SOURCE STATES: F02.0 → F02.1 → F02.2
MEDIA: E02, C02, T02, G03, G04
TRACK STACK: V1 black starfield (E02) · V2 body silhouette (C02) · V3 beam band (G03) · V4 scattered letters (T02) · V5 particle glyphs (G04)
INITIAL COMPOSITION: E02 full-frame; C02 centered.
BUILD:
1. Cut to E02+C02 at 0:06.600.
2. At ~0:07.000, cross-fade/replace C02 with T02 (letters positioned per source: top cluster spells "DNA"/"FATTY ACIDS", bottom cluster "MITOSIS"/"CELLULOSE"/"BLOOD"); bring in V3's horizontal beam band across the vertical middle, opacity 0→100.
3. From ~0:11.000, fade in G04's small red particle/squiggle glyphs at low opacity, increasing in count/opacity to 0:15.900.
KEYFRAMES: V3 opacity 0→100 at 0:07.000 (A03); V5 (G04) opacity 0→100 ramping 0:11.000-0:15.900 (A04).
TEXT: molecule-name letters are baked into T02's image asset (TEXT BAKED = YES for this one asset only — see IMAGE_PROMPTS.md), not overlay text, because they are treated as scattered particle glyphs rather than a caption.
TRANSITION IN: hard cut. TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F02.2.
FIDELITY LIMITATION: exact letter positions/rotations are approximated from the reference; do not add extra letters or particles beyond what §02_analysis/TIMELINE.csv describes.

## S03 — 0:15.900–0:22.000
SOURCE STATES: F03.0 → F03.1 → F03.2
MEDIA: E02, G05, G02, T03
TRACK STACK: V1 black starfield (E02) · V2 radial glow (G05) · V3 earth icon (G02) · V4 text (T03)
INITIAL COMPOSITION: G05 centered.
BUILD:
1. Cut to E02+G05 at 0:15.900.
2. At 0:17.000 fade in G02 (bottom) + "~1.5·10^22 J/day" caption.
3. At 0:20.000 fade in "~3.8·10^26 J/second" caption (top) + disclaimer paragraph.
KEYFRAMES: V3/caption opacity 0→100 at 0:17.000 (A05); second caption group opacity 0→100 at 0:20.000 (A06).
TEXT: "~1.5·10^22 J/day" (from 0:17.000); "~3.8·10^26 J/second" + disclaimer paragraph (from 0:20.000).
TRANSITION IN: hard cut. TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F03.2.

## S04 — 0:22.000–0:40.500
SOURCE STATES: F04.0 → F04.1 → F04.2 → F04.3
MEDIA: E03, G03, G07, T04, G08
TRACK STACK: V1 cross-section background (E03) · V2 beam (G03) · V3 plasma dome (G07) · V4 labels (T04) · V5 cracks/debris (G08)
INITIAL COMPOSITION: beam descends center-top onto the arc's apex.
BUILD:
1. Cut to E03+G03 at 0:22.000; small red glow at contact point; "MILLIONS OF DEGREES..." label already visible.
2. 0:23.500 grow V3 (dome) to small semicircle labeled "PLASMA" (scale keyframe).
3. 0:25.500-0:36.500 continue growing V3 to full size with spike/ray texture; bring in "X-RAYS" and "MORE PLASMA" labels on V4 (staggered fade-ins); hold final size/labels static for the remainder of this static-hold window.
4. 0:36.500 begin V5: black crack lines spreading from the contact point (mask reveal), reaching full-frame-width red saturation by 0:40.500.
KEYFRAMES: V3 scale small→medium at 0:23.500-0:25.500 (A07); V3 scale medium→full + V4 label opacity 0:25.500-0:36.500 (A08); V5 crack-mask reveal 0:36.500-0:40.500 (A09); background tint (V1) shifts grey→red/pink over the same window.
TEXT: "MILLIONS OF DEGREES (FAHRENHEIT, CELSIUS, RANKINE, OR KELVIN — IT DOESN'T REALLY MATTER)" from 0:22.000; "PLASMA" from 0:23.500; "X-RAYS", "MORE PLASMA" by 0:25.500.
TRANSITION IN: hard cut. TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F04.3.

## S05 — 0:40.500–0:49.800
SOURCE STATES: F05.0 → F05.1
MEDIA: E02, G03, G09, T05
TRACK STACK: V1 black bg (E02) · V2 beam (G03) · V3 Earth globe (G09) · V4 text/arrows (T05)
INITIAL COMPOSITION: globe centered, beam hitting top pole.
BUILD:
1. Cut in at 0:40.500 with "RIP" arrow (top) and "SAFE?" arrow (bottom).
2. At 0:45.500 swap "SAFE?" text to red "NOT SAFE!" and fade in the small icon element next to the bottom arrow.
KEYFRAMES: text/icon opacity or color-swap keyframe at 0:45.500 (A10).
TEXT: "RIP" (constant); "SAFE?" (0:40.500-0:45.500) → "NOT SAFE!" (0:45.500-0:49.800).
TRANSITION IN: hard cut. TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F05.1.
FIDELITY LIMITATION: the small icon near "NOT SAFE!" is illegible at source resolution; recreate as a small generic reaction glyph and flag as approximate, or omit if precision is required.

## S06 — 0:49.800–0:52.600
SOURCE STATES: F06.0 → F06.1
MEDIA: E04, G10, T06
TRACK STACK: V1 dusk background (E04) · V2 tombstone row (G10, multiple instances placed left-to-right) · V3 text (T06)
INITIAL COMPOSITION: leftmost tombstone ("TWILIGHT") framed center.
BUILD:
1. Cut in at 0:49.800.
2. Animate a position keyframe on V1/V2 (or simulate via a wider composite panned by CapCut's position/scale keyframes) moving the frame rightward so the "MOONLIGHT" tombstone is centered by 0:51.000, holding to 0:52.600.
KEYFRAMES: composite X-position moves left→right, 0:49.800-0:51.000 (A11).
TEXT: "RIP / CAUSE OF DEATH: TWILIGHT" (left stone); "RIP / CAUSE OF DEATH: MOONLIGHT" (next stone); a third, partially-framed stone's text is UNCONFIRMED — do not fabricate it.
TRANSITION IN: hard cut. TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F06.1.

## S07 — 0:52.600–0:56.100
SOURCE STATES: F07.0 → F07.1
MEDIA: E02, G11, T07, G08
TRACK STACK: V1 black bg (E02) · V2 twilight sphere (G11) · V3 label (T07) · V4 cracks (G08)
INITIAL COMPOSITION: sphere centered, five arrows raining onto the terminator from above.
BUILD:
1. Cut in at 0:52.600 with arrows + "TWILIGHT" label, no cracks.
2. From 0:53.500, fade/reveal V4 jagged crack marks along the terminator, growing to 0:56.100.
KEYFRAMES: V4 opacity/mask reveal 0:53.500-0:56.100 (A12).
TEXT: "TWILIGHT" (constant).
TRANSITION IN: hard cut. TRANSITION OUT: smooth (leads directly into the S08 ring growth on the same asset).
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F07.1.

## S08 — 0:56.100–1:23.700
SOURCE STATES: F08.0 → F08.1
MEDIA: E02, G11, G12
TRACK STACK: V1 black bg (E02) · V2 twilight sphere (G11, continued from S07) · V3 glowing ring (G12)
INITIAL COMPOSITION: same sphere as S07's end frame.
BUILD:
1. Continue from S07 without a hard cut in the underlying sphere layer.
2. Apply a circular-wipe/mask animation on V3 (the ring) that grows continuously from the two short arcs at the terminator, wrapping further around the sphere over time, closing fully by 1:16.100 (76.0s into the video).
3. Hold the closed ring static from 1:16.100 to 1:23.700.
KEYFRAMES: V3 circular-mask angle 0°→360° (wrap progress, A13), eased LIKELY-linear, 0:56.100-1:16.100 (~19.9s). This is CapCut's closest single-keyframe-group equivalent to the observed continuous wrap; if CapCut's circular mask cannot animate angular sweep directly, approximate with a sequence of pre-rendered ring-arc PNGs cross-faded at roughly 1s intervals.
TEXT: "TWILIGHT" label persists (carried over from S07).
TRANSITION IN: smooth (continues from S07). TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio; a short measured silence (75.226s-75.393s) falls late in the wrap (~0:75.2-0:75.4) — no visual cut occurs there, so no edit action is needed, just be aware narration/music briefly pauses mid-motion.
END STATE: F08.1.
FIDELITY LIMITATION: the wrap's exact angular speed curve (linear vs. eased) is not resolvable from 4s-interval sampling; treat as LIKELY steady/continuous, not exact.

## S09 — 1:23.700–1:30.000
SOURCE STATES: F09.0
MEDIA: E03, G03, G07, G08 (same assets as S04, reused verbatim)
TRACK STACK: same stack as S04 (V1 E03, V2 G03, V3 G07, V5 G08), swapped in fresh.
INITIAL COMPOSITION: identical framing to S04's end state.
BUILD:
1. Hard cut back to the S04 composite (reuse the same layered asset stack — do not regenerate).
2. Add diagonal zigzag red spark/debris line elements (part of G08) radiating from the contact point, static or very slow flicker only.
ANIMATION REQUIRED: NO (static hold once the debris elements are placed — no further growth is evidenced within this shot).
TEXT: none (labels from S04 are not visible in this reused framing per the reference).
TRANSITION IN: hard cut. TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F09.0.

## S10 — 1:30.000–1:31.900
SOURCE STATES: F10.0
MEDIA: E02, G09, G14
TRACK STACK: V1 black bg (E02) · V2 Earth (G09) · V3 Moon icon (G14)
INITIAL COMPOSITION: Earth left-of-center, Moon icon at fixed distance to the right.
BUILD: Cut in at 1:30.000; static composite, no internal motion evidenced.
ANIMATION REQUIRED: NO.
TRANSITION IN: hard cut. TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F10.0.

## S11 — 1:31.900–1:44.500
SOURCE STATES: F11.0 → F11.1 → F11.2 → F11.3
MEDIA: E02, G03, G13, G14, G15
TRACK STACK: V1 black bg (E02) · V2 beam (G03) · V3 simplified Earth outline (G13) · V4 Moon icon (G14) · V5 starburst/ring (G15)
INITIAL COMPOSITION: simplified Earth outline centered, beam hitting its pole, Moon icon fixed at right.
BUILD:
1. Cut in at 1:31.900 (style change from G09 to the plainer G13 — treat as a new source image, not a morph).
2. From 1:36.000, fade in the first thin starburst arrows on V5 radiating from the pole.
3. From 1:39.000, add more arrows; thicken one toward the Moon icon; tint the Moon icon's edge red (color/opacity keyframe on V4).
4. From 1:42.000, animate V5's ring element closing fully around the Earth outline by 1:44.500.
KEYFRAMES: V5 arrow-count/opacity ramp at 1:36.000 (A14); further ramp + V4 Moon-edge red tint at 1:39.000 (A15); V5 ring-mask closure 1:42.000-1:44.500 (A16).
TRANSITION IN: hard cut. TRANSITION OUT: hard cut.
AUDIO SYNC: a measured silence (95.778s-96.079s ≈ 1:35.8-1:36.1) falls right at this shot's F11.0→F11.1 boundary — treat the arrow-reveal keyframe at 1:36.000 as landing just after this pause.
END STATE: F11.3.

## S12 — 1:44.500–1:49.000
SOURCE STATES: F12.0 → F12.1
MEDIA: E02, G05, G03, G14, G16
TRACK STACK: V1 black bg (E02) · V2 glow/beam (G05+G03) · V3 Moon (G14) · V4 trail (G16)
INITIAL COMPOSITION: glow/beam at top; Moon enters from lower-left off-frame.
BUILD:
1. Cut to the wide glow framing at 1:44.500; animate V3+V4 (Moon + trail) moving along a curved path from lower-left toward the beam, position keyframes, arriving at the beam by 1:47.500.
2. At 1:47.500, trigger a red flash/glow element at the contact point (opacity keyframe, quick in/out).
KEYFRAMES: V3/V4 position path 1:44.500-1:47.500 (A17); flash opacity spike at 1:47.500 (A17).
TRANSITION IN: hard cut. TRANSITION OUT: smooth (continues into S13's flight on the same wide framing).
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F12.1.

## S13 — 1:49.000–1:58.000
SOURCE STATES: F13.0 → F13.1
MEDIA: E02, G05, G03, G16, G17
TRACK STACK: same as S12, with V3 asset swapped from G14 (grey Moon) to G17 (cracked/red Moon) at the cut into this shot.
INITIAL COMPOSITION: continues from S12's contact point.
BUILD: Animate V3+V4 (Moon/comet + trail) along a curved path away from the beam, position keyframes from 1:49.000 to 1:58.000, ending at the frame's lower-right/far position.
KEYFRAMES: V3/V4 position path 1:49.000-1:58.000 (single continuous curve; do not add extra bounces or direction changes not evidenced).
TRANSITION IN: smooth (continues from S12). TRANSITION OUT: hard cut.
AUDIO SYNC: two measured silences fall inside this shot — 109.181s-109.345s (≈1:49.2, near the shot's start) and 114.036s-114.285s (≈1:54.0, mid-flight). No visual cut occurs at either; they are pauses during the continuous flight.
END STATE: F13.1.

## S14 — 1:58.000–2:00.000
SOURCE STATES: F14.0
MEDIA: E02, G17
TRACK STACK: V1 black bg (E02) · V2 shattered Moon (G17)
INITIAL COMPOSITION: Moon debris alone, no beam.
BUILD: Hard cut in; static hold, no beam/other elements visible.
ANIMATION REQUIRED: NO.
TRANSITION IN: hard cut. TRANSITION OUT: hard cut.
AUDIO SYNC: continuous mixed audio; no measured silence in this range.
END STATE: F14.0.

## S15 — 2:00.000–2:03.933 (end of video)
SOURCE STATES: F15.0
MEDIA: G10, T06, G17
TRACK STACK: V1 tombstone (G10) · V2 inset emblem (G17, small scale) · V3 text (T06)
INITIAL COMPOSITION: tombstone centered, emblem inset, text below.
BUILD: Hard cut to the final card; hold static to the end of the video. Fade the audio track out under this card (the source measures a 1.284s near-silence from 122.711s to the end).
ANIMATION REQUIRED: NO.
TEXT: "RIP" (on stone) + "WE SHOULDN'T HAVE TURNED THE SUN INTO A LASER".
TRANSITION IN: hard cut. TRANSITION OUT: end of video (export ends here).
AUDIO SYNC: audio fades/quiets from 122.711s to the end (measured); fade the A1 audio clip out over roughly this window.
END STATE: F15.0 (final).

## Completion check
All 15 shots (S01-S15) have a build recipe above; every motion event A01-A18 is referenced by ID or by its underlying keyframe description in its shot's BUILD/KEYFRAMES section; every asset in `ASSET_MANIFEST.csv` is placed on a track in at least one shot.
