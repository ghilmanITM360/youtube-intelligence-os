# CAPCUT REBUILD — earthquake-magnitude-shorts-wBLVmEZV2Oc

Reference: TIMELINE.csv (timing/content per state), ASSET_MANIFEST.csv (every asset ID), MOTION_EVENTS.csv (every A-ID). This file only adds CapCut-specific build steps — it does not repeat descriptions already in those files.

## PROJECT SETUP
- CANVAS / ASPECT RATIO: 9:16
- RESOLUTION: 1080x1920
- FPS: 24
- TOTAL DURATION: 65.96s (round timeline to 66s)
- BACKGROUND: solid white (#FFFFFF), set as canvas color for the whole project (no background clip needed)
- MASTER AUDIO: AU01 narration (write/record new lines per state, see AUDIO_MAP.md) + optional AU02 music bed, low volume, ducked under narration
- GLOBAL FONT/TEXT SYSTEM: one bold hand-drawn/marker-style caps font for T01 (titles), same family at smaller regular weight for T02 (captions) — pick one CapCut font (e.g. "Permanent Marker" or similar bundled font) and reuse for both via size/weight variation only
- GLOBAL COLOR RULE: black line art + grey flat fills on white canvas; red reserved only for annotation/alert marks (strike-throughs, circles, epicenter rings, scribbles) — never used elsewhere
- GLOBAL EFFECTS: none (no filters, no LUTs, no vignette observed)

## MEDIA TO IMPORT
Reference ASSET_MANIFEST.csv for full descriptions. Import as transparent PNGs unless noted:
T01, T02 (built as CapCut text layers, not images), E01, O01, O02, G01 (one frame, reused 3x), C01 (4 pose variants), E02 (ruler — build as CapCut shapes+text, not an image, so it can be keyframed), E03 (4 damage-state PNGs, or 1 base + 3 additive overlay PNGs), O05, O03, O04 (2 density variants), AU01, AU02.

## SHOT BUILD
Single shot (S01) end-to-end — this project is one continuous canvas with layers cutting in/out, not multiple video clips. Build it as one long timeline with clip/image layers trimmed to each state's IN/OUT.

### F01.0-F01.2 — Intro gag (0.00-4.60s)
TRACK STACK: V2 T01 title text | V1 E01 seismograph
BUILD:
1. Place T01 text "RICHTER SCALE" 0.00-1.60s.
2. At 1.60s, duplicate the text clip; apply CapCut's "Strikethrough"-style effect or overlay a thin red rectangle shape animated left-to-right (position keyframe, 1.60s→2.10s) across the text to fake a strike-through.
3. Add second T01 text "\"MOMENT MAGNITUDE\" SCALE" below, opacity keyframe 0%→100% from 1.80s-2.30s.
4. Place E01 clip 0.00-4.60s. If E01 is a static PNG, add a short looping "shake" via position keyframes (small random X/Y jitter, amplitude ~5px) starting 1.60s; if E01 is a pre-animated video clip with the ink-scribble baked in, just trim it to 2.60-4.60s for that portion.
KEYFRAMES: 00:01.600 — red strike shape opacity 0→100 / 00:02.100 — strike hold / 00:01.800 — T01 line2 opacity 0→100 (APPROXIMATE timings)
TOOLS: keyframes, opacity, shape overlay, position (jitter)
TRANSITION: none in (video start) / hard CUT out at 4.60s
AUDIO SYNC: narration line 1 starts 0.00s; line 2 ("well actually, it's the moment magnitude scale") starts ~1.60s
END STATE: F01.2
FIDELITY LIMITATION: CapCut has no native "hand-drawn scribble" brush; fastest approximation is a pre-rendered PNG/video asset for E01 with the scribble baked in, animated only via position keyframes in CapCut.

### F01.3-F01.4 — Newspaper / phone / LIVE box gag (5.00-8.00s)
TRACK STACK: V3 G01+C01+T02 (LIVE box) | V2 O02 (phone) | V1 O01 (newspaper)
BUILD:
1. Cut all V1/V2 (F01.0-2 layers) at 4.60s; new layers in at 5.00s (0.4s hard black-frame gap or straight cut — OBSERVED as instant cut, treat as a straight cut with no transition).
2. Place O01 top third, O02 bottom-left third, G01+C01+T02 bottom-right third, all in 5.00-8.00s.
3. At 6.00s, add a small red circle/ellipse shape (stroke only, no fill) over the "8" inside the LIVE box text, opacity 0→100 keyframe 6.00-6.40s.
KEYFRAMES: 00:06.000 — circle shape opacity 0→100, scale 0→100 (APPROXIMATE)
TOOLS: cutout, position, opacity, shape, keyframes
TRANSITION IN: CUT / TRANSITION OUT: CUT (8.50s)
AUDIO SYNC: narration reads the three gag lines in sequence, punchline emphasis at 6.00s
END STATE: F01.4

### F01.5-F01.9 — The real scale + the fact (8.50-18.10s)
TRACK STACK: V2 T01/T02 text | V1 E02 ruler (built from shapes: one vertical line + repeated small tick-mark lines + number text layers)
BUILD:
1. Build E02 as a CapCut compound: 1 vertical line shape + a stack of short horizontal tick shapes + text numbers, grouped.
2. 8.50-9.00s: short ruler (scale Y ~30%).
3. 9.00-12.50s: keyframe the group's Y-scale from ~30%→70%, and swap in numbered tick text at 12.50s (or reveal a pre-built "numbered" version via opacity crossfade).
4. 13.00-13.60s: continue Y-scale keyframe 70%→100%; simultaneously bring in T02 caption text block (opacity 0→100), replacing an earlier shorter placeholder caption if you built one, or simply have the caption appear once at 13.60s if you skip the intermediate wording change (LOW fidelity cost, OBSERVED difference is minor).
5. 14.60-15.60s: T01 + T02 opacity 100→0.
6. 16.00-17.50s: overlay a red scribble PNG/shape group over the ruler's mid-section, with a fast opacity flicker or small looped jitter to fake vibration, then opacity 100→0 at 17.50-18.10s.
KEYFRAMES: 00:09.000 ruler scaleY 30%→70% (out 12.500) / 00:13.000 ruler scaleY 70%→100% (out 13.600) / 00:14.600 T01+T02 opacity 100→0 (out 15.600) / 00:16.000 scribble opacity 0→100 (out 16.400), jitter loop 16.400-17.400, opacity 100→0 (out 17.500) — all APPROXIMATE
TOOLS: shape, text, keyframes, opacity, scale
TRANSITION: fades throughout, no hard cuts inside this block
AUDIO SYNC: caption fact line reads during 13.60-15.60s hold
END STATE: F01.9
FIDELITY LIMITATION: exact ruler growth easing curve is unmeasurable at 0.5s sampling — use CapCut's default "ease-out" keyframe curve as a reasonable approximation.

### F01.10-F01.22 — Magnitude escalation ladder (18.50-65.96s)
TRACK STACK (constant from here on): V4 G01+C01+T02 (LIVE boxes, when present) | V3 illustration layer (E03 globe / O03 slabs / O04 debris, one at a time) | V2 T01/T02 text | V1 E02 ruler (persistent, never removed)
BUILD PATTERN (repeats per magnitude step — see TIMELINE.csv for each state's exact IN/OUT and content):
1. At each hard-cut boundary (A10, A13, A15, A18, A21, A22 — full list in MOTION_EVENTS.csv), cut V2 text to the new "MAGNITUDE N" label and swap the V3 illustration clip; these are straight cuts, no transition.
2. Within a held state, additive elements (epicenter marks+dates at A11, LIVE box at A12/A19-equivalent, "3500 KM" label at A14, distressed figure at A17, debris at A20) are simple opacity 0→100 fades, ~0.3-0.4s, no position movement needed.
3. For F01.16 (Magnitude 15's crack+spiky-border growth, 37.00-45.00s): build E03's damage overlay as 2-3 PNG stages (crack only → half-spiky → full-spiky) and crossfade between them rather than trying to keyframe a organic shape growth — fastest CapCut-native approximation.
4. For F01.22's finale (59.00-65.96s): start with the same O04 debris PNG used at F01.20, then crossfade in a second "more fragments" O04 variant at ~63.50s to sell the escalation, ending on that frame (video source ends here — decide your own out-point/loop if publishing new content).
5. For A24 (ruler's subtle upward reframe near the end): optionally add a slow position keyframe on E02 (Y position drifting up a few px from 48.50s to the end) — this is a LOW-fidelity-risk optional touch, skip if not visible enough to matter.
KEYFRAMES: see MOTION_EVENTS.csv IN/OUT columns per A-ID — apply the same opacity-fade or straight-cut pattern noted above for each
TOOLS: cutout, opacity, keyframes, crossfade, position (optional for A24)
TRANSITION: hard CUTs between magnitude steps, opacity fades for additions within a step
AUDIO SYNC: each "MAGNITUDE N" cut should land on a narration beat/number callout; LIVE-box gags get a deadpan-delivery narration line
END STATE: F01.22 (video end)

## GLOBAL NOTE ON G01 (LIVE box)
Build G01 once as a reusable overlay (black rounded-rect frame + "LIVE" tag, transparent center). Duplicate the clip 3x on V4 at F01.3-4, F01.12, F01.21, swapping only the C01 pose and T02 caption text inside each instance.
