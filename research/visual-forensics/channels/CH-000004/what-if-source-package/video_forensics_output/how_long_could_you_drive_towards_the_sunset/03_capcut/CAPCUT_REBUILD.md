# WAY 1 — CapCut Rebuild

Reference `02_analysis/TIMELINE.csv`, `ASSET_MANIFEST.csv`, and `MOTION_EVENTS.csv` for full descriptions; this file gives build actions only, citing asset/motion IDs rather than repeating descriptions.

## Project setup
- CANVAS / ASPECT RATIO: 9:16 vertical (480x854 source; recommend building at 1080x1920 and matching crop).
- RESOLUTION: 1080x1920 (or 480x854 to match source 1:1).
- FPS: 24.
- TOTAL DURATION: 129.875s (3117 frames at 24fps).
- BACKGROUND: varies per shot — see MEDIA per shot below (white canvas, chalkboard, vignette, painterly plates, maps).
- MASTER AUDIO: AU01 (single full-mix track) on A1, placed at 00:00.000, untouched — do not split narration/music, no verified separation exists.
- GLOBAL FONT/TEXT SYSTEM: one consistent white, rounded/hand-lettered sans-serif style for every caption instance of T01-T04.
- GLOBAL COLOR RULE: red is reserved exclusively for rejection marks (X), directional arrows, and callout labels; green is reserved for confirmation checks; do not use either color elsewhere.
- GLOBAL EFFECTS: none — every shot uses a static locked camera; do not add camera moves, zooms, or particle effects anywhere in this rebuild.

### Media to import
E01 chalkboard BG · C01 stick-figure PNG · G14 chalk-globe PNG · G01 yellow-circle shape · G02 grey-circle shape · G03 horizon-line shape · G04 mountain-silhouette shape · G05 flashlight-rig PNG · G06 2D globe PNG · G07 3D wireframe-globe PNG · G08 car-icon shape · G09 snow-tractor PNG · E02 polar-dusk-sky BG · C03 seals PNG · E03 mountain-ridge silhouette · G10 hatchback-car PNG · G11 map-inset PNG · G12 legend-icon PNG · E04 coastline-map BG · E05 office-desk BG · G13 PyEphem-icon PNG · E06 church-silhouette PNG · E07 painterly-sunset BG · C02 camera-crew-silhouette PNG · T01-T04 native CapCut text layers · AU01 narration/music WAV.

---

## S01 — 00:00.000-00:05.833
SOURCE STATES: F01.0 → F01.1
MEDIA: E01, C01, G14
TRACK STACK: V2 — G14 chalk-globe overlay · V1 — E01 chalkboard BG + C01 figure
INITIAL COMPOSITION: E01 fills frame; G14 centered-left on the board; C01 lower-left, full height.
BUILD: Import E01 as background; place G14 on V2; place C01 on V1 foreground.
KEYFRAMES (APPROXIMATE — redraw-style motion, not literal position keyframes):
00:00.000 — G14 static, minimal motion-line detail (A01 start).
00:01.000-00:05.833 — G14 rotation simulated via a short crossfade/replace between 2-3 redrawn frames of the globe with an added rotation arrow (A01).
TOOLS: crop, overlay, opacity (for the redraw crossfade), text (none this shot).
TEXT: none.
TRANSITION: CUT out to S02.
AUDIO SYNC: AU01 continuous from 00:00.000; no isolated cue identified.
END STATE: F01.1.
FIDELITY LIMITATION: the source globe "spin" is a hand-drawn redraw, not a true 3D rotation — reproduce with a 2-3 frame crossfade (A01) rather than a rotation keyframe for best fidelity.

## S02 — 00:05.833-00:11.792
SOURCE STATES: F02.0 → F02.1 → F02.2
MEDIA: G01, G02, G03, T03 (X/check marks as simple graphic overlays, not text)
TRACK STACK: V2 — growing circle chain + marks · V1 — white BG + G03 horizon line
INITIAL COMPOSITION: G03 horizon line spans the frame at mid-height; chain builds left-to-right above/on it.
BUILD: Place G03; then add G01/G02 instances one at a time along the line per TIMELINE state boundaries.
KEYFRAMES:
00:05.833 — first G01 + X mark appears (A02 start).
00:07.333-00:09.792 — additional G01/G02 pairs + X/check marks appear sequentially (A02).
00:09.833-00:11.750 — chain extends to 6-7 elements with final marks (A03).
TOOLS: overlay, position (per new element), text/shape for X and check marks.
TEXT: none (marks are simple drawn shapes, not text).
TRANSITION: CUT in from S01; CUT out to S03.
AUDIO SYNC: AU01 continuous; no isolated cue identified.
END STATE: F02.2.
FIDELITY LIMITATION: none significant.

## S03 — 00:11.792-00:13.833
SOURCE STATES: F03.0 → F03.1
MEDIA: E07, C02, T01
TRACK STACK: V2 — T01 captions · V1 — E07 BG + C02 silhouettes
INITIAL COMPOSITION: E07 full-frame; C02 pair lower-left; sun disc right-of-center on the horizon.
BUILD: Place E07 and C02; add T01 "NOT A SUNSET" caption at shot-in.
KEYFRAMES:
00:11.792 — "NOT A SUNSET" caption visible (shot start).
00:12.792 — second T01 line "NOT TOUCHING THE HORIZON (YET)" + pointer arrow fades in (A04).
TOOLS: text, opacity (fade-in), overlay (arrow graphic).
TEXT: "NOT A SUNSET" (top, centered); "NOT TOUCHING THE HORIZON (YET)" (lower-right, with pointer arrow to the sun).
TRANSITION: CUT in from S02; CUT out to S04.
AUDIO SYNC: AU01 continuous.
END STATE: F03.1.
FIDELITY LIMITATION: none significant.

## S04 — 00:13.833-00:31.417
SOURCE STATES: F04.0 → F04.1 → F04.2 → F04.3 → F04.4 → F04.5 → F04.6
MEDIA: G01, G02, G03, G04, G05
TRACK STACK: V2 — reveal graphics (X marks, G05, crack gag, mountain roll) · V1 — white BG + G03/G04
INITIAL COMPOSITION: G03 horizon line at mid-height; elements build/change on top of it across this long shot.
BUILD (sequential, per state boundary in TIMELINE.csv):
00:13.833 — G01/G02 pair settles on horizon line, then X mark appears (A05).
00:16.000 — G05 flashlight-rig appears, held, then redrawn once more (A06).
00:18.000 — fresh G01/G02 chain builds; first crack-gag callout appears on one circle (A07).
00:21.000 — second crack gag + X mark; layout resets to a plain G01/G02 pair (A08).
00:25.000 — G04 mountain silhouette appears; G01 rolls/bounces across the peaks; final X mark + G02 rolls away (A09).
TOOLS: overlay, opacity, position (per redraw), text/shape for X marks and the "BRWWAAK" sound-effect lettering.
TEXT: "BRWWAAK" (hand-lettered sound-effect callout, appears twice at the crack-gag beats).
TRANSITION: CUT in from S03; CUT out to S05.
AUDIO SYNC: measured near-silence gap at 25.062s-25.172s (see `05_audio/AUDIO_MAP.md`) falls at the F04.5→F04.6 boundary, right as the mountain-roll beat (A09) begins.
END STATE: F04.6.
FIDELITY LIMITATION: A09's mountain-roll bounce is reconstructed as a short sequence of redrawn positions (multi-exposure look in the source), not a smooth physics-accurate bounce; treat as APPROXIMATE.

## S05 — 00:31.417-00:42.917
SOURCE STATES: F05.0 → F05.1 → F05.2
MEDIA: G06, T03
TRACK STACK: V2 — labels/arrows · V1 — G06 globe on dark vignette BG
INITIAL COMPOSITION: G06 centered; "SUNSET ZONE" label + dashed line already present at shot-in.
BUILD: Place G06; reveal callouts in sequence.
KEYFRAMES:
00:31.417 — G06 + "SUNSET ZONE" label visible (shot start).
00:35.417 — first "1000 km/h" arrow+label appears, then a second (A10).
00:39.583 — larger sweeping arrow + "OH NO!" caption appears (A11).
TOOLS: text, overlay (arrows), opacity.
TEXT: "SUNSET ZONE", "1000 km/h" (x2), "OH NO!".
TRANSITION: CUT in from S04; CUT out to S06.
AUDIO SYNC: AU01 continuous; no isolated cue identified.
END STATE: F05.2.
FIDELITY LIMITATION: none significant.

## S06 — 00:42.917-00:49.875
SOURCE STATES: F06.0 → F06.1 → F06.2
MEDIA: G07, G08
TRACK STACK: V2 — arrows + G08 icon · V1 — G07 wireframe globe
INITIAL COMPOSITION: G07 angled to emphasize the pole; "SUNSET ZONE" dashed line + first arrow present at shot-in.
BUILD: Place G07; reveal arrows one at a time, then the vehicle icon.
KEYFRAMES:
00:42.917 — G07 + 1 arrow visible (shot start).
00:44.917-00:47.875 — three more arrows appear at progressively lower latitudes (A12).
00:47.917 — G08 vehicle icon appears near the pole (A13).
TOOLS: overlay, opacity, position (icon placement).
TEXT: "SUNSET ZONE" (carried over from shot-in).
TRANSITION: CUT in from S05; CUT out to S07.
AUDIO SYNC: AU01 continuous.
END STATE: F06.2.
FIDELITY LIMITATION: none significant.

## S07 — 00:49.875-00:53.000
SOURCE STATES: F07.0 (static — no animation)
MEDIA: E02, G09, C03, T02
TRACK STACK: V2 — T02 caption · V1 — E02 BG + G09 + C03
INITIAL COMPOSITION: E02 full-frame gradient; G09 right, C03 foreground lower-left; sun disc left on horizon; "NORTH POLE, 90°N" caption top-left.
BUILD: Place E02, G09, C03; add T02 caption; hold for full shot duration.
KEYFRAMES: none — ANIMATION REQUIRED: NO, hold the composed frame for the measured duration.
TOOLS: text, overlay only (no keyframes needed).
TEXT: "NORTH POLE, 90°N".
TRANSITION: CUT in from S06; CUT out to S08 (LIKELY DISSOLVE — see S08 fidelity note).
AUDIO SYNC: AU01 continuous.
END STATE: F07.0.
FIDELITY LIMITATION: none significant.

## S08 — 00:53.000-01:08.417
SOURCE STATES: F08.0 → F08.1 → F08.2 → F08.3 → F08.4 → F08.5
MEDIA: E02, E03, G10, T02, T03, G11
TRACK STACK: V3 — captions/map inset · V2 — G10 car · V1 — E02 BG + E03 ridge
INITIAL COMPOSITION: E02 gradient with E03 ridge silhouette at horizon; G10 parked right; sun left on horizon; "LONGYEARBYEN, 78°N" caption top-left at shot-in.
BUILD: Place backgrounds and car; reveal captions/inset in sequence.
KEYFRAMES:
00:53.000 — T02 caption visible (shot start; LIKELY a dissolve from S07 — cross-fade the two background plates over ~0.3-0.5s if reproducing this transition, otherwise a plain cut is an acceptable simplification).
00:55.000 — T02 caption fades out (A14).
00:57.000 — "~55 min" caption + arrow appears (A15).
00:59.000 — "WEST" caption replaces it (A16).
01:01.000 — G11 circular map inset appears top-right (A17).
01:04.000 — "355 mph" caption appears (A18).
TOOLS: text, opacity (fades/swaps), overlay (map inset), mask (circular crop for G11).
TEXT: "LONGYEARBYEN, 78°N", "~55 min", "WEST", "355 mph".
TRANSITION: DISSOLVE in from S07 (LIKELY); CUT out to S09.
AUDIO SYNC: AU01 continuous.
END STATE: F08.5.
FIDELITY LIMITATION: the S07→S08 transition type is inferred (LIKELY dissolve) since the automated cut detector did not flag a hard cut despite the visible content change; a plain cut is an acceptable simplification if the dissolve cannot be confirmed.

## S09 — 01:08.417-01:14.292
SOURCE STATES: F09.0 → F09.1 → F09.2
MEDIA: C01, G01, G02
TRACK STACK: V2 — inset diagram · V1 — white BG + C01 figures
INITIAL COMPOSITION: single C01 figure centered at shot-in.
BUILD: Add two more C01 copies; then build the small inset diagram top-right.
KEYFRAMES:
01:08.417 — 1 figure visible (shot start).
01:10.417 — two more figures appear; small inset diagram appears (A19).
01:12.417 — inset diagram gains a second circle pair + arrow (A20).
TOOLS: overlay, position (figure placement), text/shape (inset diagram).
TEXT: none.
TRANSITION: CUT in from S08; CUT out to S10.
AUDIO SYNC: AU01 continuous.
END STATE: F09.2.
FIDELITY LIMITATION: none significant.

## S10 — 01:14.292-01:35.583
SOURCE STATES: F10.0 → F10.1 → F10.2 → F10.3 → F10.4
MEDIA: E04, G08, G12, T03
TRACK STACK: V3 — G12 legend icon · V2 — G08 car + labels · V1 — E04 map BG
INITIAL COMPOSITION: E04 fills frame, DAY/NIGHT band already visible at shot-in.
BUILD: Reveal direction labels, then car, then SUNSET gradient + legend icon, then animate car + legend together.
KEYFRAMES:
01:14.292 — E04 + plain DAY/NIGHT band visible (shot start).
01:17.083 — "NW" label+arrows appear, then swap to "SW" (A21).
01:20.542 — G08 car icon appears on the road (A22).
01:24.083 — SUNSET gradient band + G12 legend icon (2 circles) appear (A23).
01:29.083-01:35.583 — G08 advances along the road toward the SUNSET band while G12's circle count increases step by step from 2 to 7 (A24, single continuous ~8.6s pass — use one long position keyframe run for G08 and a matched series of opacity/swap keyframes for G12's circle count).
TOOLS: position (car path), opacity (label swaps, gradient build), keyframes (long continuous pass for A24), overlay (legend icon box).
TEXT: "NW", "SW".
TRANSITION: CUT in from S09; CUT out to S11.
AUDIO SYNC: AU01 continuous.
END STATE: F10.4.
FIDELITY LIMITATION: A24's exact circle-count timing (which of the 5 steps lands on which frame) was approximated from 1fps sampling — treat sub-second placement as APPROXIMATE.

## S11 — 01:35.583-01:44.500
SOURCE STATES: F11.0 → F11.1 → F11.2
MEDIA: E05, G13, G11
TRACK STACK: V2 — G13 icon + map overlay · V1 — E05 desk BG
INITIAL COMPOSITION: E05 desk/chair/laptop; plain map panel above at shot-in.
BUILD: Reveal PyEphem icon, then Arctic Circle overlay on the map panel.
KEYFRAMES:
01:35.583 — E05 + plain map panel visible (shot start).
01:39.583 — "PyEphem" icon + label appears near the laptop (A25).
01:43.333 — "ARCTIC CIRCLE" dashed curve + label appears on the map panel (A26).
TOOLS: overlay, text, opacity.
TEXT: "PyEphem", "ARCTIC CIRCLE".
TRANSITION: CUT in from S10; CUT out to S12.
AUDIO SYNC: AU01 continuous.
END STATE: F11.2.
FIDELITY LIMITATION: none significant.

## S12 — 01:44.500-01:53.458
SOURCE STATES: F12.0 → F12.1
MEDIA: E04, G10, G01, G02, T03
TRACK STACK: V3 — T03 caption · V2 — G10 car · V1 — E04 landmass (side-view treatment)
INITIAL COMPOSITION: E04 landmass along lower frame; G10 upper-left with motion lines; G01/G02 pair ahead of it on the coastline at shot-in.
BUILD: Place elements; reveal caption while car continues advancing.
KEYFRAMES:
01:44.500 — composition visible, no caption (shot start; A27/A28 begin — car already in slow continuous motion).
01:48.667-01:53.458 — "~95 min" caption + bracket fades in (A27) while G10 continues advancing along the coastline (A28, small continuous displacement).
TOOLS: position (car advance), text, opacity.
TEXT: "~95 min".
TRANSITION: CUT in from S11; CUT out to S13.
AUDIO SYNC: AU01 continuous.
END STATE: F12.1.
FIDELITY LIMITATION: A28's car displacement within this shot is small and its exact easing is APPROXIMATE (1fps sampling).

## S13 — 01:53.458-01:55.000
SOURCE STATES: F13.0 → F13.1
MEDIA: E06, C01, G01, G02, G11
TRACK STACK: V2 — caption + map arrow · V1 — E06 church + C01 + circle pair
INITIAL COMPOSITION: E06 left, C01 center, G01/G02 pair right, G11 small map bottom-right (partially cropped) at shot-in.
BUILD: Place elements; reveal caption + map location marker.
KEYFRAMES:
01:53.458 — composition visible, no caption (shot start).
01:54.208 — "~55 min" caption + bracket appears; G11 gains a red arrow/label pointing to the town (A29).
TOOLS: text, overlay, opacity.
TEXT: "~55 min", "LONGYEARBYEN".
TRANSITION: CUT in from S12; CUT out to S14.
AUDIO SYNC: AU01 continuous.
END STATE: F13.1.
FIDELITY LIMITATION: none significant.

## S14 — 01:55.000-02:09.875
SOURCE STATES: F14.0 → F14.1 → F14.2 → F14.3 → F14.4 → F14.5
MEDIA: E07, C02, T04
TRACK STACK: V2 — T04 captions + swirl graphic · V1 — E07 BG + C02 silhouettes
INITIAL COMPOSITION: identical framing to S03 (E07 + C02), no disclaimer captions this time, at shot-in.
BUILD: Reveal swirl motion, then dialogue captions one at a time.
KEYFRAMES:
01:55.000 — E07 + C02 visible, no captions (shot start).
01:58.000-01:59.958 — spiral/swirl motion lines appear around the right-hand figure and persist (A30, PERSISTENT_LOOP-style squiggle — loop a short swirl animation for the remainder of the shot).
02:00.000 — "WHAT ARE YOU DOING?" caption appears (A31).
02:02.000 — "LENGTHENING THE SUNSET" / "PUSHING BACK THE NIGHT" captions appear (A32).
02:05.000 — "GIVING ME A LITTLE MORE TIME" caption appears (A33).
02:08.000 — "HERE WITH YOU." caption appears; hold to end as audio fades (A34).
TOOLS: text, overlay (swirl loop), opacity, audio fade-out (match the measured 128.228s-129.981s fade on A1).
TEXT: "WHAT ARE YOU DOING?", "LENGTHENING THE SUNSET", "PUSHING BACK THE NIGHT", "GIVING ME A LITTLE MORE TIME", "HERE WITH YOU."
TRANSITION: CUT in from S13; END OF VIDEO (fade out, audio only).
AUDIO SYNC: measured fade 128.228s-129.981s under F14.5 — apply an audio fade-out on A1 matching this window.
END STATE: F14.5 (final frame of video).
FIDELITY LIMITATION: A30's swirl is a hand-drawn squiggle motif — reproduce as a small looping line-animation overlay rather than a literal physics-based spin.

## Completion check
All 14 shots (S01-S14) have a build recipe above, and every motion ID A01-A34 is cited at least once inline with its corresponding KEYFRAMES action.
