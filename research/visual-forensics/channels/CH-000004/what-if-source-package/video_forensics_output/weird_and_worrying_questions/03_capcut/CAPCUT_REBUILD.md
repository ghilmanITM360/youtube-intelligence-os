# WAY 1 — CapCut Reconstruction — weird_and_worrying_questions

This entire video is **one locked-camera shot (S01)**; there are no camera cuts to rebuild. All 27 visual states are built as layer/keyframe changes on a single canvas. Reference `../02_analysis/TIMELINE.csv` (SHOT_ID/STATE_ID) and `../02_analysis/MOTION_EVENTS.csv` (MOTION_ID) instead of repeating descriptions here.

## CapCut project setup
- CANVAS / ASPECT RATIO: 9:16
- RESOLUTION: 1080x1920
- FPS: 24
- TOTAL DURATION: 00:47.458 (1139 frames)
- BACKGROUND: solid white (E01), full duration
- MASTER AUDIO: AU01, single continuous track from 00:00.000
- GLOBAL FONT/TEXT SYSTEM: two text styles reused throughout — T01 (Q-card: gray rounded-rectangle shape, sentence-case body text, smaller bold "— Name" line) and T02 (bold all-caps hand-drawn-style font, selective underline for emphasis)
- GLOBAL COLOR RULE: black line art on white; red fill reserved for the thermometer mercury (G03) only
- GLOBAL EFFECTS: none (no filters, LUTs, or transitions beyond hard cuts/fades on individual layers)

## Media to import
Reference `../02_analysis/ASSET_MANIFEST.csv` for full detail. Import checklist:
- C01 — narrator stick-figure PNG (base + drinking + exasperated pose variants)
- C02 — detective/mirrors-aside character PNG
- O01 — desk/monitor/keyboard PNG
- O02 — coffee mug PNG (in-hand + thrown variants)
- G01 — thought-bubble outline PNG
- G02 — teeth PNG (intact + shattered variants)
- G03 — thermometer PNG (mercury-high + mercury-low variants)
- G04 — steaming mug (bubble illustration) PNG
- G05 — ring/beam/sunburst composite PNG
- G06 — standing figure (bubble) PNG
- G07 — volcano PNG (static + erupting variants)
- G08 — reactor building PNG (intact + meltdown variants)
- G09 — "ANTIMATTER →" label PNG or native text
- G10 — award plaque PNG (heading-only + with caption line variants, or build caption as an overlay)
- G11 — crying figure PNG (puddle-growth variants)
- AU01 — full-mix audio WAV/AAC

## S01 — 00:00.000–00:47.458 (entire video)
SOURCE STATES: F01.0 → F01.26 (all 27 states; see `../02_analysis/TIMELINE.csv`)

TRACK STACK:
- V5 — Q-card / caption text overlays (T01, T02)
- V4 — thought-bubble contents (G02–G11, per-gag)
- V3 — thought-bubble outline (G01)
- V2 — C01 (+ C02 for its one appearance) and physical props (O02)
- V1 — desk/monitor (O01) over background (E01)

INITIAL COMPOSITION: E01 fills the canvas; O01 (desk) is placed lower-right, fixed for the entire duration; C01 sits at the desk holding O02 (mug) in hand.

BUILD (sequential, by joke segment — every motion ID A01–A25 is cited):

**Segment 1 — Shelby / cold teeth (00:00.000–00:08.875, F01.0–F01.7)**
1. 00:00.000 — Place T01 card #1 (Shelby's question) top-left. END STATE: F01.0.
2. 00:01.000 — Add G01 (bubble) + G02 intact-teeth PNG inside it (A01). END STATE: F01.1.
3. 00:02.000 — Add G03 thermometer, mercury-high variant, beside teeth (A02). END STATE: F01.2.
4. 00:03.000–00:04.000 — Keyframe G03's mercury layer: crop/mask animates from high to low fill (A03, opacity/scale keyframes on the mercury sub-layer). END STATE: F01.3.
5. 00:04.000 — Swap G02 to its shattered variant (A04, hard cut, no crossfade). END STATE: F01.4.
6. 00:05.000 — Add G04 steaming-mug PNG to the right of the bubble (A05, opacity fade-in 0.2s). END STATE: F01.5.
7. 00:06.000 — Keyframe O02 (physical mug) position from C01's hand to off-frame upper-left over ~0.3s (A06, position keyframes + motion-blur optional); swap C01 to reaction-pose variant. END STATE: F01.6.
8. 00:08.875 — Clear V4/V5 (bubble contents + Q-card) to blank; hold O02 hidden from here on (A07, opacity 100%→0% cut). END STATE: F01.7. FIDELITY LIMITATION: A03's exact mercury-drop timing is APPROXIMATE (1s-sampling derived).

**Segment 2 — Mirrors aside + Jeff / new star (00:10.000–00:21.125, F01.8–F01.13)**
9. 00:10.000 — Add C02 PNG entering from right edge + T02 caption ("HOW MANY MIRRORS...") (A08, position/opacity keyframe over ~0.3s). END STATE: F01.8.
10. 00:12.167 — Remove C02 + caption; add T01 card #2 (Jeff) top-left; V4 empty (A09, hard cut). END STATE: F01.9.
11. 00:16.000 — Add G05 composite (ring+beam+sunburst+figures) to V4 (A10, opacity fade-in 0.2s). END STATE: F01.10.
12. 00:17.000 — Swap G05 for G06 (standing figure) (A11, hard cut). END STATE: F01.11.
13. 00:19.000 — Add T02 caption "...MAYBE" beside G06 (A12). END STATE: F01.12.
14. 00:21.125 — Clear V4/V5 to blank (A13, hard cut). END STATE: F01.13. FIDELITY LIMITATION: G05's internal build order (ring → beam → sunburst) is inferred as a single simultaneous reveal; source may build it in finer sub-steps not resolvable at 1s sampling.

**Segment 3 — Tomasz / volcano (00:23.000–00:28.125, F01.14–F01.16)**
15. 00:23.000 — Add T01 card #3 (Tomasz) + G07 static-volcano PNG (A14, simultaneous). END STATE: F01.14.
16. 00:27.000 — Swap G07 to erupting variant (large ash-cloud burst PNG or opacity-crossfade to burst layer) (A15). END STATE: F01.15.
17. 00:28.125 — Clear V4/V5 to blank (A16, hard cut). END STATE: F01.16.

**Segment 4 — AJ / Chernobyl + plaque (00:29.000–00:40.708, F01.17–F01.22)**
18. 00:29.000 — Add T01 card #4 (AJ) + G08 intact reactor-building PNG (A17, simultaneous). END STATE: F01.17.
19. 00:30.000 — Add G09 "ANTIMATTER →" label/arrow beside stack (A18). END STATE: F01.18.
20. (hold, no keyframe needed — F01.19, static)
21. 00:34.000 — Swap G08 to meltdown-burst variant (A19). END STATE: F01.20.
22. 00:34.708 — Clear V4/V5; add G10 plaque PNG (heading only) full-frame on V4 (A20, hard cut). END STATE: F01.21.
23. 00:39.000 — Add T02 caption line ("FOR GOD'S SAKE...") to the plaque; swap C01 to exasperated-pose variant (A21, simultaneous). END STATE: F01.22.

**Segment 5 — Karl / crying (00:40.708–00:47.458, F01.23–F01.26)**
24. 00:40.708 — Clear plaque; add T01 card #5 (Karl) + G11 crying-figure PNG (small puddle) (A22, hard cut). END STATE: F01.23.
25. 00:42.000–00:44.958 — Keyframe G11's puddle sub-layer scale from small to large over ~3s (A23). END STATE: F01.24.
26. 00:45.000 — Clear V4/V5; add T02 caption "...KARL" above C01 (A24, hard cut). END STATE: F01.25.
27. 00:46.000 — Extend T02 caption text to "...KARL, IS EVERYTHING OK?" (A25). END STATE: F01.26 (holds to 00:47.458, end of video).

KEYFRAMES: only listed where an element's position/scale/opacity actually changes (A03 mercury, A06 mug throw, A23 puddle growth); all other transitions are hard cuts/fades between static PNG variants, per the Absolute Fidelity Rule (no invented easing beyond a simple 0.2–0.3s opacity fade where noted).

TOOLS: opacity, position keyframes, scale keyframes, crop/mask (for G03 mercury), cutout/overlay layering, text (native CapCut for T01/T02).

TEXT: exact wording for every T01/T02 instance is given verbatim in `../02_analysis/TIMELINE.csv`'s `LITERAL_FRAME_DESCRIPTION` and `SCRIPT_OR_AUDIO_CUE` columns; reproduce as native CapCut text layers rather than baking into images (see `../04_image_to_video/IMAGE_PROMPTS.md` TEXT BAKED policy).

TRANSITION: hard cuts throughout; the only soft fades observed are the ~0.2–0.3s opacity fade-ins noted above for newly appearing bubble graphics (A01, A02, A05, A08, A10, A12, A18).

AUDIO SYNC: AU01 plays continuously from 00:00.000; the four measured near-silence gaps (see `../05_audio/AUDIO_MAP.md`) fall at ≈34.5s (during the Chernobyl/plaque transition, A19–A20) and ≈45.5–47.3s (during the closing Karl caption beats, A24–A25) — APPROXIMATE sync only, no transcript available.

END STATE: F01.26 (video ends).

FIDELITY LIMITATION: because this is a single continuous canvas rather than discrete camera shots, CapCut reconstruction requires careful layer-visibility sequencing (toggling V4/V5 content per segment) rather than simple shot-to-shot cutting; get the V1–V2 layers (E01/O01/C01) right once and never re-cut them for the whole 47.458s.
