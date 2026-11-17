# CapCut Rebuild

Reference `02_analysis/TIMELINE.csv`, `ASSET_MANIFEST.csv`, `MOTION_EVENTS.csv` for IDs. Descriptions are not repeated here.

## Project setup
- CANVAS / ASPECT RATIO: 9:16
- RESOLUTION: 1080x1920
- FPS: 24
- TOTAL DURATION: 00:00.000–01:23.333
- BACKGROUND: off-white (S01) → fully covered by E01 (S02), no letterboxing
- MASTER AUDIO: AU01, one continuous clip, full length, placed on A1
- GLOBAL FONT/TEXT SYSTEM: T01 = a bold/rounded serif for the title card; G02 city labels = a casual hand-lettered font (CapCut's "Marker"/"Handwriting" preset family is the closest built-in match — POSSIBLE, not confirmed)
- GLOBAL COLOR RULE: grayscale board scene (S01) vs. full climate-palette map (S02) — no color grade/LUT beyond the source asset colors
- GLOBAL EFFECTS: none (no filters, no vignette, no grain observed)

## Media to import
- T01 — title card (text box + rounded-rect background shape, built natively in CapCut, no import needed)
- C01 — stick-figure narrator PNG
- O01 — single globe PNG
- O02 — two-globes-plus-arrow PNG (or two separate globe PNGs + CapCut arrow shape)
- E01 — master map JPG/PNG (must be wide enough that the S02 crop window never runs out of image — see FIDELITY LIMITATION below)
- G02 — one city-pin dot PNG (reused), 20x native CapCut text labels
- G03 — red circle annotation PNG (or drawn live with CapCut's shape/brush tool)
- G04 — landscape vignette sticker PNG
- G05 — dialogue vignette sticker PNG
- AU01 — full-length audio/music+VO track

## Shot build

### S01 — 00:00.000–00:04.420
SOURCE STATES: F01.0 → F01.1
MEDIA: T01, C01, O01, O02
TRACK STACK:
- V3 — T01 (title card)
- V2 — O01/O02 (board content, swapped at the internal state change)
- V1 — C01 (narrator) composited over the off-white background (or the background is V0/canvas color)
- A1 — AU01

INITIAL COMPOSITION: T01 centered top ~1/3 of frame; board (O01) centered middle third; C01 bottom third, left-of-center.
BUILD:
1. Add AU01 to A1, full length.
2. Add T01 text box, position top-third, duration 0:00–0:04.42 (holds unchanged the whole shot).
3. Add C01 PNG to V1, same duration, static, no keyframes (APPROVED: no motion observed).
4. Add O01 to V2, 0:00–~0:02.00 (APPROXIMATE cut point — verify against your own copy of the source before locking).
5. Cut V2 to O02 at ~0:02.00, hold to 0:04.42.
KEYFRAMES: none — every element in S01 is a static hold (confirms MOTION_EVENTS A01 as a straight replace, not a tween).
TOOLS: text tool (rounded background), cutout/PNG overlay, cut (no transition effect — it's a straight replace within the same locked shot).
TEXT: "What would the world's largest cities be like / if the land masses were rotated by 90 degrees?" — two centered lines, black serif, gray rounded card, position top-third, unchanged for the full 4.42s.
TRANSITION: hard cut out at 4.42s into S02.
AUDIO SYNC: none confirmed (wording unknown) beyond the silence dip at 4.13s — optionally add a short whoosh SFX there if you have one; it is not a verified original asset.
END STATE: F01.1.

### S02 — 00:04.420–00:83.333 (single continuous "shot", built as ONE crop-and-pan move over E01)
SOURCE STATES: F02.0 → F02.1 → F02.2 → F02.3 → F02.4 → F02.5 → F02.6 → F02.7 → F02.8
MEDIA: E01, G02 (x20), G03, G04, G05
TRACK STACK:
- V4 — G03 / G04 / G05 (timed overlays, only on-screen for their own window)
- V3 — G02 dots+labels (20 separate clips/keyframed groups, each appearing at its own timestamp and then holding to the end of the video)
- V2 — E01 (the one large map image/video, scaled up and keyframed for position+scale to simulate the pan)
- A1 — AU01 continues (already placed in S01's build, unbroken)

INITIAL COMPOSITION: Import E01 at a scale large enough that the 1080x1920 frame is always a small crop of it (e.g. import at 3x–4x canvas size, exact scale depends on your source art's real pixel dimensions — mark APPROXIMATE). Set its first keyframe to frame the Mexico City area (per F02.0's literal description).
BUILD:
1. Place E01 on V2, full 4.42–83.333s duration.
2. Turn on position/scale keyframes on E01. Because CapCut keyframes are the only real path to a "pan across a giant image" in this tool, treat each MOTION_EVENTS PAN row (A03–A10) as one pair of keyframes (start-of-burst / end-of-burst), holding position flat between bursts (the HOLD states in TIMELINE.csv):
KEYFRAMES (position values are APPROXIMATE — set by eye against your own copy of E01, using each state's literal description as the target framing; do not treat these as measured pixel coordinates):
```
00:04.420 — E01 position/scale: frame = F02.0 (Mexico City / North America)
00:08.800 — A03 burst start
00:09.300 — A03 burst end, position/scale: frame = F02.1 (Australia/Jakarta)      [HOLD to 18.00]
00:18.000 — A04 burst start
00:18.500 — A04 burst end, position/scale: frame = F02.2 (Asia/Europe/Africa)      [HOLD to 25.60]
00:25.600 — A05 burst start
00:26.100 — A05 burst end, position/scale: frame = F02.3 (+ Seoul/Osaka/Tokyo/Moscow/Cairo/London/NYC/LA)  [HOLD to 35.40]
00:35.400 — A06 burst start
00:35.900 — A06 burst end, position/scale: frame = F02.4 (reframe, red circle gone)  [HOLD to 41.90]
00:41.900 — A07 burst start
00:42.400 — A07 burst end, position/scale: frame = F02.5 (Cairo/Nile push-in)      [HOLD to 47.90]
00:47.900 — A08 slow-pan start (NO blur — animate this one as a smooth linear/eased keyframe move, not a fast burst)
00:55.000 — A08 slow-pan end, position/scale: frame = mid-point (Cairo/Nile ↔ São Paulo)
00:65.300 — A08 slow-pan effectively complete, position/scale: frame = F02.6 (wide Asia/Europe/Africa/N.America)
00:65.300 — A09 burst start
00:65.800 — A09 burst end, position/scale: frame = F02.7 (reframe)                [HOLD to 72.40]
00:72.400 — A10 burst start
00:72.900 — A10 burst end, position/scale: frame = F02.8 (Moscow/Cairo/London/NYC quadrant) [HOLD to 83.333]
```
4. For each fast-pan burst (A03,A04,A05,A06,A07,A09,A10): add Speed-ramp or a short "Zoom/Blur" transition-style motion blur (CapCut's built-in "Blur" transition, or a Directional Blur effect clip, ~0.3–0.5s) so the burst reads as a fast blurred pan rather than an instant camera snap — this is the one fidelity-limited step, see below.
5. Add each G02 dot+label pair on V3 at its own appearance point per TIMELINE.csv / MOTION_EVENTS.csv (R01/R02/R05), then let it hold (opacity 100%, no further keyframes) through the rest of the video once added.
6. Add G03 on V4, 0:30.00–0:35.40 only (matches its observed on/off window).
7. Add G04 on V4, ~0:44.50–~0:55.00 (its own clip, parented/keyframed to track the same position deltas as E01's pan during that window, since it is map-anchored — see FIDELITY LIMITATION).
8. Add G05 on V4, ~0:76.00–0:83.333.
TOOLS: keyframes, position, scale, crop, mask (if you need to hard-crop E01's edges), opacity (for G02 pop-ins), blur/speed-ramp transition.
TEXT: 20x G02 city names — exact spellings and order of first appearance: Mexico City, Jakarta, Kolkata, Delhi, Hong Kong, Mumbai, Karachi, Manila, Shanghai, Seoul, Osaka, Tokyo, Beijing, Moscow, Cairo, London, New York City, Los Angeles, São Paulo, Buenos Aires.
TRANSITION IN: whip-zoom blur from S01 (A02).
TRANSITION OUT: none — video ends on the F02.8 hold.
AUDIO SYNC: AU01 continues unbroken from S01; no further confirmed sync points beyond the one silence dip already placed at the S01/S02 boundary.
END STATE: F02.8 (final frame of the file).

FIDELITY LIMITATION: CapCut cannot natively "walk a virtual camera along a fixed-position sticker" — G04/G05 tracking the map pan (CAMERA_SUBJECT_COUPLED, motion A08) must be hand-keyframed to move in lockstep with E01's own keyframes rather than being a single automatic parent/child relationship (CapCut has no true parenting). Closest method: keyframe G04/G05's position with the same deltas you used for E01 in that time window.
