# CapCut Rebuild — what_if_earths_water_suddenly_disappear

## 1. Project setup
- CANVAS / ASPECT RATIO: 16:9 landscape
- RESOLUTION: 1920x1080
- FPS: 24
- TOTAL DURATION: 183.792s (4411 frames)
- BACKGROUND: white (default for all diagram shots except S02/S18 red cards and S06–S09/S15 dark/space panels)
- MASTER AUDIO: AU01 (undifferentiated narration+music mix), placed on A1 for the full runtime
- GLOBAL FONT/TEXT SYSTEM: one bold sans-serif family at 3 weights — T01 (question-card), T02 (bold caption/exclamation), T03 (small measurement/chemistry label). Reference `../02_analysis/ASSET_MANIFEST.csv` for exact usage per shot.
- GLOBAL COLOR RULE: black line-art on white/gray by default; red reserved for the title card, credits card, the S14 heat gradient, and the S15 engulfment rays — never used elsewhere.
- GLOBAL EFFECTS: none beyond opacity fades at the S06/S07 gray-fade transition and the S10 seaplane→jar-diagram dissolve.

## 2. Media import checklist
Characters: C01–C06 · Environments: E01–E09 · Objects: O01–O08 · Graphics: G01–G14 · Text systems: T01–T03 · Audio: AU01. Full descriptions in `../02_analysis/ASSET_MANIFEST.csv`.

## 3. Shot builds

### S01 — 00:00.000–00:08.292 (F01.0→F01.1→F01.2→F01.3)
MEDIA: C01, E01, G01, T01, O01
TRACK STACK: V3 text/Q-card (G01,T01) — V2 chalkboard content (O01) — V1 background (E01) + C01
INITIAL COMPOSITION: E01 fills frame; C01 stands left third holding paper; G01 Q-card box top-left; blackboard area blank.
BUILD: 1) Place E01 full-frame. 2) Place C01 left third. 3) Overlay G01+T01 Q-card, hold from 0s. 4) At 2s (f48) reveal O01 sailboat inside blackboard region (opacity 0→100 or draw-on mask). 5) At 4s (f96) reveal fish graphic below waterline. 6) At 6s (f144) swap O01 to capsized pose with motion-line overlay (A03).
KEYFRAMES: 00:02.000 — O01 opacity 0→100 (APPROXIMATE). 00:04.000 — fish graphic opacity 0→100. 00:06.000 — O01 replaced by capsized variant.
TOOLS: overlay, opacity, cutout, text.
TEXT: Q-card wording per `TIMELINE.csv` F01.0 description, top-left, small.
TRANSITION: none in; hard CUT out to S02.
AUDIO SYNC: continuous narration (UNKNOWN exact words — see `05_audio/AUDIO_MAP.md`).
END STATE: F01.3.

### S02 — 00:08.292–00:10.292 (F02.0)
MEDIA: G02
TRACK STACK: V1 full-frame graphic
INITIAL COMPOSITION: G02 title card fills frame, centered logo+wordmark.
BUILD: 1) Cut to full-frame G02, hold 2s.
KEYFRAMES: none (static hold).
TOOLS: overlay.
TEXT: "what if?" / "THE VIDEO SERIES" baked into G02.
TRANSITION: hard CUT in and out.
AUDIO SYNC: measured near-silence gap 9.48–10.35s falls within this card (see `05_audio/AUDIO_MAP.md`) — likely a brief narration pause.
END STATE: F02.0.

### S03 — 00:10.292–00:17.375 (F03.0→F03.1→F03.2)
MEDIA: E02, C02, C03, O02, G03, T02
TRACK STACK: V3 text/graphic overlay (G03,T02) — V2 characters (C02,C03) + O02 — V1 background E02
INITIAL COMPOSITION: E02 palm-beach background; C02 on sand; C03 with O02 on water.
BUILD: 1) Place E02, C02, C03+O02. 2) At ~2s (f295) swap water-area fill to solid black + T02 "VACUUM" label (G03). 3) At ~4s (f343) revert fill to normal water, remove G03/T02.
KEYFRAMES: 00:02.000 — water fill opacity swap to G03 (APPROXIMATE). 00:04.000 — G03 removed, normal water restored.
TOOLS: mask, opacity, text.
TEXT: "VACUUM" bold caption, centered over the blacked-out water area.
TRANSITION: hard CUT in and out.
AUDIO SYNC: continuous narration.
END STATE: F03.2.

### S04 — 00:17.375–00:26.792 (F04.0→F04.1→F04.2)
MEDIA: E03, O04
TRACK STACK: V2 exposed-seafloor overlay (animated mask) — V1 background E03 + O04
INITIAL COMPOSITION: E03 cliff/water-tower backdrop; light stippled seafloor texture at the waterline.
BUILD: 1) Place E03+O04. 2) Animate seafloor-texture mask expanding downward across ~9s (A06). 3) At ~6s (f566) add C04 figure standing on exposed ground.
KEYFRAMES: 00:00.000→00:09.000 — seafloor mask height 10%→90% of lower frame (APPROXIMATE, continuous). 00:06.000 — C04 opacity 0→100.
TOOLS: mask, keyframes, overlay.
TEXT: none.
TRANSITION: hard CUT in and out.
AUDIO SYNC: continuous narration.
END STATE: F04.2.
FIDELITY LIMITATION: exact mask expansion curve is APPROXIMATE (2-second-interval sampling only).

### S05 — 00:26.792–00:39.625 (F05.0→F05.1→F05.2→F05.3→F05.4)
MEDIA: E02, C02, C03, O02, O03, G04, T03
TRACK STACK: V3 timer/scale overlay (G04,T03) — V2 debris+boats (O03,O02) + characters — V1 background E02
INITIAL COMPOSITION: same E02 beach as S03; normal beach with figures.
BUILD: 1) Re-place E02+C02+C03+O02. 2) At ~4s (f715) fade in O03 debris scatter. 3) At ~9s (f787) add more O03 instances. 4) At ~14s (f857) fade in G04 "1 SECOND" + "5m" scale bar; animate O02 position downward (sinking). 5) Continue O02 descent to shot end.
KEYFRAMES: 00:04.000 — O03 opacity 0→100. 00:14.000 — G04 opacity 0→100; O02 position Y +0→+40px (APPROXIMATE). 00:14.000→00:18.000 — O02 position Y continues downward.
TOOLS: overlay, position keyframes, text.
TEXT: "1 SECOND" timer, "5m" scale label.
TRANSITION: hard CUT in and out.
AUDIO SYNC: measured near-silence gap at 32.4–32.6s falls within F05.1/F05.2 (debris population).
END STATE: F05.4.

### S06 — 00:39.625–00:58.750 (F06.0→F06.1→F06.2)
MEDIA: E04, G04, T03, O05
TRACK STACK: V2 timer/depth overlay (G04,T03) — V1 background E04 + O05 fleet
INITIAL COMPOSITION: cross-section backdrop, "~6 SECONDS" label, shallow depth scale, ships sinking along slope.
BUILD: 1) Place E04+G04+T03+O05. 2) Animate O05 fleet growing/descending across ~12s (A12). 3) At ~14s (f1201) swap depth-scale labels to -1000/-2000/-3000m (T03 text swap). 4) At shot end (~f1395) fade to solid gray full-frame (A13).
KEYFRAMES: 00:00.000→00:12.000 — O05 fleet position Y increasing, count increasing (APPROXIMATE). 00:14.000 — T03 depth labels swapped. 00:18.000→00:19.125 — full-frame opacity fade to solid gray.
TOOLS: position keyframes, text swap, opacity fade.
TEXT: "~6 SECONDS" timer, depth-scale numbers.
TRANSITION: hard CUT in; FADE out (measured near-silence gap at 58.7–58.9s coincides almost exactly with this fade, corroborating it).
AUDIO SYNC: near-silence gap 58.744–58.921s at the fade-out.
END STATE: F06.2.

### S07 — 00:58.750–01:04.375 (F07.0)
MEDIA: E04, G04, T03, O05, G07
TRACK STACK: V2 bracket/footnote overlay (G04,G07,T03) — V1 background E04 + O05
INITIAL COMPOSITION: gray water-column panel, "-1000/-2000/-3000m" scale, "~600 SECONDS" bracket on the right, two ships at bottom, small footnote caption below.
BUILD: 1) Fade in from S06's gray hold. 2) Hold static composition for full shot duration.
KEYFRAMES: none (static hold after fade-in).
TOOLS: opacity fade, text.
TEXT: "~600 SECONDS" bracket label; footnote "*THE TWO HALVES DID NOT SINK SIMULTANEOUSLY".
TRANSITION: FADE in (continuation of S06's fade); hard CUT out.
AUDIO SYNC: continuous narration.
END STATE: F07.0.

### S08 — 01:04.375–01:09.208 (F08.0)
MEDIA: E04, G04, T03, O05, G07 (reuse S07 media, add second panel)
TRACK STACK: same as S07, plus V2b second panel overlay
INITIAL COMPOSITION: S07's panel plus a new narrower panel on the right with its own "~30 SECONDS" bracket and a single ship already at the bottom.
BUILD: 1) Keep S07 panel in place. 2) Slide/reveal second panel in from the right with its own bracket+ship.
KEYFRAMES: 00:00.000 — second panel opacity/position reveal (APPROXIMATE).
TOOLS: overlay, position, text.
TEXT: "~30 SECONDS" bracket label.
TRANSITION: hard CUT in and out.
AUDIO SYNC: continuous narration.
END STATE: F08.0.

### S09 — 01:09.208–01:18.333 (F09.0→F09.1)
MEDIA: G04, T03
TRACK STACK: V1 diagram (zoom-out transform)
INITIAL COMPOSITION: dual-panel comparison begins zooming/scaling out.
BUILD: 1) Cut to zoom-out start. 2) Scale/reposition diagram elements outward over ~4.5s to reveal the full trench profile (A14). 3) Add "MARIANA TRENCH" label and deep depth-scale (-2000 to -10,000m) as the zoom completes.
KEYFRAMES: 00:00.000 — diagram scale 100%. 00:04.500 — diagram scale ~40% (zoomed out), full trench visible (APPROXIMATE).
TOOLS: scale keyframes, text.
TEXT: "~60 SECONDS", "MARIANA TRENCH", deep depth-scale numbers.
TRANSITION: hard CUT in and out.
AUDIO SYNC: continuous narration.
END STATE: F09.1.

### S10 — 01:18.333–01:47.458 (F10.0→F10.1→F10.2→F10.3→F10.4→F10.5)
MEDIA: O06, G04, G05, O07, G06
TRACK STACK: V3 caption overlay (G06) — V2 jar-diagram graphics (G05,O07) / seaplane (O06) — V1 background (fading cross-section, then blank)
INITIAL COMPOSITION: seaplane flying near sea-level line, faint cross-section beneath.
BUILD: 1) Place O06 seaplane, animate left-to-right flight path continuously. 2) At ~4s (f1968) fade out remaining cross-section background (A15). 3) At ~8s (f2064) fade in 3-jar insert graphic (G05+O07). 4) At ~12s (f2160) swap to dominant 4-jar row with G06 "GASP!" caption. 5) At ~16s (f2256) cascade additional jar rows/captions ("WHEEZE!"). 6) At ~20s (f2400) animate jar water fill to empty/black in each jar.
KEYFRAMES: 00:00.000→00:29.125 — O06 position X moving steadily left-to-right (looped or single pass, APPROXIMATE). 00:04.000 — background opacity fade to 0. 00:08.000 — jar-insert opacity 0→100. 00:12.000 — jar-row swap. 00:16.000–00:20.000 — jar water-level keyframes descending to empty.
TOOLS: position keyframes, opacity, mask (water level), text.
TEXT: "GASP!", "WHEEZE!" captions per jar.
TRANSITION: hard CUT in; hard CUT out.
AUDIO SYNC: continuous narration describing marine-life consequences.
END STATE: F10.5.
FIDELITY LIMITATION: the seaplane/jar-diagram interleave (F10.0–F10.3) was resolved from 2-second-interval sampling only (no scdet cut detected in this 29s span); exact insert timing is APPROXIMATE.

### S11 — 01:47.458–01:54.333 (F11.0→F11.1)
MEDIA: E05, C05, O08
TRACK STACK: V2 characters+boat (C05,O08) — V1 background E05
INITIAL COMPOSITION: household rooftop/sink scene, rowboat resting on dry ground beside the house.
BUILD: 1) Place E05+C05+O08. 2) At ~9s (f2688) animate C05 departing figure + dog walking to O08 and pushing off rightward off-frame (A20).
KEYFRAMES: 00:09.000→00:11.375 — C05(departing)+O08 position X moving right toward frame edge (APPROXIMATE).
TOOLS: position keyframes.
TEXT: none.
TRANSITION: hard CUT in and out.
AUDIO SYNC: continuous narration.
END STATE: F11.1.

### S12 — 01:54.333–02:16.792 (F12.0→F12.1→F12.2→F12.3→F12.4→F12.5)
MEDIA: E06, G08, G09, G10, G07
TRACK STACK: V3 CO2/footnote overlay (G10,G07) — V2 rain/fire graphics (G08,G09) — V1 background E06
INITIAL COMPOSITION: hillside silhouette under dark rain clouds, rain falling.
BUILD: 1) Place E06+G08, animate rain lines falling continuously (persistent loop, A21) for ~8s. 2) At ~8s (f2928) stop rain, begin vegetation-drying color/line change (A22). 3) At ~14s (f3024) ignite small flame (G09, A23). 4) At ~18s (f3096) spread fire across full hillside width (A24). 5) At ~22s (f3192) add G10 CO2 text cascade rising from fire + G07 footnote note box (A25).
KEYFRAMES: 00:00.000→00:08.000 — rain-line loop (persistent). 00:08.000 — rain opacity→0, vegetation texture swap. 00:14.000 — flame opacity 0→100 (small). 00:18.000→00:21.000 — flame scale/width increasing to full hillside. 00:22.000 — CO2 text opacity 0→100 (repeated instances), footnote box opacity 0→100.
TOOLS: opacity, position/scale keyframes, text, mask.
TEXT: "NOTE: WATER HAS A VERY COMPLEX IMPACT ON GLOBAL WARMING..." footnote box; "CO2" repeated text.
TRANSITION: hard CUT in and out.
AUDIO SYNC: continuous narration.
END STATE: F12.5.

### S13 — 02:16.792–02:23.583 (F13.0→F13.1)
MEDIA: C01, E01, G11, T01, T02
TRACK STACK: V2 tombstone+caption (G11,T01,T02) — V1 background E01 + C01
INITIAL COMPOSITION: host beside blackboard, tombstone graphic reading "RIP / ALL LIFE ON EARTH / THANKS JOANNA".
BUILD: 1) Cut to E01+C01+G11. 2) At ~5.4s (f3374) add handwritten "WORSE? FOR WHO?" T02 caption beside the tombstone (A26).
KEYFRAMES: 00:05.400 — T02 caption opacity 0→100.
TOOLS: overlay, text.
TEXT: tombstone text baked in G11; "WORSE? FOR WHO?" as a separate T02 layer.
TRANSITION: hard CUT in and out.
AUDIO SYNC: near-silence gap at 140.99–141.23s falls near the caption reveal.
END STATE: F13.1.

### S14 — 02:23.583–02:35.208 (F14.0→F14.1)
MEDIA: E07, G12, T03
TRACK STACK: V2 chemistry annotations (G12 boxes/arrows, T03 formulas) — V1 background E07 (volcano shape) + heat-gradient layer
INITIAL COMPOSITION: volcano cross-section, CO2+H2O box, grayed-out CaSiO3/CaCO3 chemistry boxes, no heat gradient yet.
BUILD: 1) Place E07+G12+T03. 2) Animate a red gradient layer beneath the volcano from 0% to full opacity/saturation across ~7.6s (A27).
KEYFRAMES: 00:00.000 — gradient opacity 0. 00:07.600 — gradient opacity 100 (APPROXIMATE, continuous ramp).
TOOLS: opacity/color keyframes.
TEXT: chemical formulas (CO2+H2O, H2CO3, CaSiO3, CaCO3+CO2) baked in G12.
TRANSITION: hard CUT in and out.
AUDIO SYNC: near-silence gap at 154.86–155.12s falls right at this shot's end.
END STATE: F14.1.

### S15 — 02:35.208–02:46.750 (F15.0→F15.1→F15.2)
MEDIA: C01, E01, E08, G13, T02
TRACK STACK: V2 sun/moon graphic + caption (E08,G13,T02) — V1 background E01 + C01
INITIAL COMPOSITION: host beside blackboard; blackboard shows black space, Sun upper-left, Moon center, "~1,000,000,000 YEARS FROM NOW" label, "BYE!" text.
BUILD: 1) Place E01+C01+E08+G13+T02. 2) Animate red ray/particle intensity around the Sun increasing across ~4s (A28). 3) Fade rays out, leaving Moon alone with a dimmer Sun (A29).
KEYFRAMES: 00:00.000 — ray opacity 0. 00:04.000 — ray opacity 100 (peak). 00:04.000→00:08.500 — ray opacity fades back to 0.
TOOLS: opacity keyframes, text.
TEXT: "~1,000,000,000 YEARS FROM NOW", "BYE!".
TRANSITION: hard CUT in and out.
AUDIO SYNC: continuous narration.
END STATE: F15.2.

### S16 — 02:46.750–02:50.792 (F16.0)
MEDIA: E09, O07
TRACK STACK: V1 background E09 + O07 creatures
INITIAL COMPOSITION: aquarium tank with rocks, two creatures swimming, dashed measurement line at the top of the water.
BUILD: 1) Cut to E09+O07. 2) Loop subtle creature swim-cycle for the shot duration (no material position change observed at 2s sampling; treat as ANIMATION REQUIRED: minimal/idle only).
KEYFRAMES: none required beyond an idle swim loop.
TOOLS: overlay.
TEXT: none.
TRANSITION: hard CUT in and out.
AUDIO SYNC: continuous narration.
END STATE: F16.0.

### S17 — 02:50.792–02:53.792 (F17.0)
MEDIA: E09, O07, C06, T02
TRACK STACK: V2 greeter figure+caption (C06,T02) — V1 background E09+O07
INITIAL COMPOSITION: same tank as S16; a head/figure enters from the right edge with a "Hi!" caption.
BUILD: 1) Keep E09+O07 in place. 2) Cut in C06 at the right edge with T02 "Hi!" caption.
KEYFRAMES: none (single reveal at cut-in).
TOOLS: overlay, text.
TEXT: "Hi!".
TRANSITION: hard CUT in; hard CUT out to credits.
AUDIO SYNC: continuous narration.
END STATE: F17.0.

### S18 — 02:53.792–03:03.792 (F18.0)
MEDIA: G14
TRACK STACK: V1 full-frame graphic
INITIAL COMPOSITION: red credits card — logo, contributor list, book-cover thumbnails, "GET THE BOOKS" text.
BUILD: 1) Cut to full-frame G14. 2) Hold/loop for the remainder of the runtime (~10s).
KEYFRAMES: none (static hold).
TOOLS: overlay.
TEXT: baked into G14.
TRANSITION: hard CUT in; N/A out (video end).
AUDIO SYNC: extensive measured near-silence from ~172–184s (see `05_audio/AUDIO_MAP.md`) — consistent with a music-only or silent credits card.
END STATE: F18.0 (video end).
