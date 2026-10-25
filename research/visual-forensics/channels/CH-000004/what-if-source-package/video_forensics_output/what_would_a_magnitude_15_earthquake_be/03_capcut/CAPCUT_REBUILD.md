# CapCut Rebuild — what_would_a_magnitude_15_earthquake_be

## Project setup
CANVAS / ASPECT RATIO: 16:9 landscape
RESOLUTION: 1280x720
FPS: 24
TOTAL DURATION: 00:03:05.29 (4447 frames)
BACKGROUND: Off-white (#F5F5F0 approx.) for all illustration shots; solid deep red for the bumper (S02) and credits (S16)
MASTER AUDIO: Single narration/music mix track (AU01), placed on A1 for the full runtime
GLOBAL FONT/TEXT SYSTEM: Bold rounded sans-serif for "MAGNITUDE ##" headlines and most captions (T01/T03); looser hand-lettered comic font for onomatopoeia (T02)
GLOBAL COLOR RULE: Black line art on off-white by default; red reserved for the bumper/credits background and hand-scribble emphasis marks (strike-through, tick marks, epicenter rings)
GLOBAL EFFECTS IF ANY: None — no filters, LUTs, vignettes, or camera-shake effects were measured anywhere in the source

MEDIA TO IMPORT: See `../02_analysis/ASSET_MANIFEST.csv` for the full list (C01-C05 characters, E01-E06 environments, O01-O17 objects, G01-G07 graphics, T01-T03 text systems, AU01 audio). Reference IDs below rather than re-describing each asset.

---

### S01 00:00.000–00:16.917
SOURCE STATES: F01.0 → F01.1 → F01.2 → F01.3
MEDIA: C01, E01, O01, G01, G03, T01, T03
TRACK STACK:
V3 — "MAGNITUDE ##" text label / caption box (G01)
V2 — NYC skyline illustration (E01/O01), swappable damage-state layers
V1 — host figure (C01)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Caption box top-left over host figure; skyline illustration fills the right two-thirds of frame, gear icon top-right.
BUILD:
1. Place the caption-box text layer (G01/T03) and set it to fade in over ~0.5s at 00:00.000.
2. Import the host figure PNG (C01) at frame-left; keep static for the whole shot.
3. Import the base NYC-skyline PNG (E01/O01, intact buildings) on V2.
4. Add a "MAGNITUDE" text layer above the skyline; type the number "15", cut to "25" at 00:08.000.
5. At 00:12.000, cross this same skyline layer with a second skyline PNG variant showing explosion+rubble (or use a short built-in "shatter/explode" overlay effect), holding the rubble frame until 00:16.917.
KEYFRAMES: None besides simple opacity fades on the caption box and label swaps (instant, no interpolation).
TOOLS: Text layer, opacity keyframe, overlay/replace image, cut.
TEXT: Caption box body copy exactly as in `TIMELINE.csv` F01.0; "MAGNITUDE 15" then "MAGNITUDE 25" headline, centered above the skyline, large bold font.
TRANSITION: Fade-in at video open; hard cut out at 00:16.917.
AUDIO SYNC: Narration presumed to read the intro question aloud; no measured silence gap in this range.
END STATE: F01.3
FIDELITY LIMITATION: The brief single-frame "MAGNITUDE 0" flicker observed at ~00:00:07 in the source is treated as a rendering artifact and is not reproduced.

### S02 00:16.917–00:18.917
SOURCE STATES: F02.0
MEDIA: G02
TRACK STACK:
V1 — bumper card image/video (G02)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Full-frame static red bumper card.
BUILD: Import the bumper still (or reuse the identical clip from any other video in this project's library, since it is unchanged) and hold for the full 2.0s.
KEYFRAMES: None (static hold).
TOOLS: None beyond placing the clip.
TEXT: Baked into the bumper image ("xkcd's what if? THE VIDEO SERIES").
TRANSITION: Hard cut in/out.
AUDIO SYNC: None distinct measured.
END STATE: F02.0

### S03 00:18.917–00:24.042
SOURCE STATES: F03.0 → F03.1
MEDIA: O04, G06, T01
TRACK STACK:
V2 — headline text + strike-through/shake overlay
V1 — seismograph illustration (O04)
A1 — narration/music (AU01)
INITIAL COMPOSITION: "RICHTER SCALE" headline over the seismograph device, centered.
BUILD:
1. Place the seismograph PNG (O04), static, for the full shot.
2. Add "RICHTER SCALE" text layer above it.
3. At 00:22.000, add a red scribble/strike-through overlay (freehand draw tool or a pre-made "strike" PNG) across that text, and fade in a second text layer reading "MOMENT MAGNITUDE SCALE" above it.
4. Simultaneously add a small shake-lines overlay (G06) around the seismograph.
KEYFRAMES: Opacity fade-in on the new headline (~0.3s); no position keyframes.
TOOLS: Text layer, draw/overlay, opacity.
TEXT: "RICHTER SCALE" (struck through); "MOMENT MAGNITUDE SCALE" (in quotes).
TRANSITION: Hard cut in/out.
AUDIO SYNC: None distinct measured.
END STATE: F03.1

### S04 00:24.042–00:27.458
SOURCE STATES: F04.0
MEDIA: O02, O03, C02, T02, T03
TRACK STACK:
V3 — LIVE TV inset (C02) at frame-right
V2 — newspaper (O02) center, phone alert (O03) at frame-left
V1 — background (off-white)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Three-panel composite: phone alert left, newspaper center, LIVE TV inset right.
BUILD: Place all three overlay PNGs in their fixed positions; hold static for the full 3.4s shot. No reveal animation needed (composite appears as a single cut).
KEYFRAMES: None.
TOOLS: Overlay/image placement only.
TEXT: Newspaper headline "3.5 EARTHQUAKE STRIKES FEAR IN OHIO CORN FIELD"; phone alert "SMALL DOG WAS FRIGHTENED BY 4.8 EARTHQUAKE" / "WE MUST STOP THIS AT THE SOURCE!"; TV captions "IT'S AT LEAST AN 8 ON THE RICHTER SCALE!" / "UHM, ACTUALLY...".
TRANSITION: Hard cut in/out.
AUDIO SYNC: None distinct measured.
END STATE: F04.0

### S05 00:27.458–00:46.250
SOURCE STATES: F05.0 → F05.1 → F05.2 → F05.3 → F05.4
MEDIA: O05, E03, C02, T01, T03
TRACK STACK:
V3 — epicenter labels / LIVE TV inset
V2 — globe (E03)
V1 — ruler (O05)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Blank ruler at frame-left, 0-10 range.
BUILD:
1. Place the ruler PNG (O05) at frame-left; keyframe its height/scale to grow taller at 00:32.000 (relabel to 0-15).
2. At 00:36.000, overlay red scribble tick marks near the 10-15 region (draw tool or pre-made overlay).
3. At 00:38.000, fade in "MAGNITUDE 9" text and the Asia-facing globe PNG (E03) beside the ruler.
4. At 00:43.000, overlay two red epicenter-ring PNGs with date-label text on the globe, and fade in the LIVE TV inset (C02) at lower-right with its fact-box caption.
KEYFRAMES: Scale/height keyframe on the ruler (00:27.458→00:32.000); opacity fades on each subsequent reveal.
TOOLS: Scale keyframe, overlay/draw, text layer, opacity.
TEXT: "MOMENT MAGNITUDE SCALE"; small logarithmic-scale note (illegible at delivery resolution — reproduce approximate wording or omit); "MAGNITUDE 9"; "MARCH 2011 9.0-9.1"; "9.1-9.3 DECEMBER 2004"; TV caption "THE NORTH POLE SHIFTED 2.5 CM, DECREASING THE LENGTH OF A DAY BY 268 MICROSECONDS".
TRANSITION: Hard cut in/out.
AUDIO SYNC: None distinct measured.
END STATE: F05.4

### S06 00:46.250–01:06.667
SOURCE STATES: F06.0 → F06.1 → F06.2 → F06.3
MEDIA: O06, E03, O05, G04, G05, C01, T01
TRACK STACK:
V3 — debris ring / host + thought bubble
V2 — globe or tectonic diagram (E03/O06)
V1 — ruler (O05)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Ruler at left; tectonic block diagram center-right, "MAGNITUDE 10" headline.
BUILD:
1. Hold the tectonic-diagram composition until 00:51.000, then swap (hard replace) to the plain Americas-facing globe PNG, headline "MAGNITUDE 11".
2. At 00:56.000, crossfade/overlay crack-line texture onto the globe and begin fading in small debris-fragment PNGs around its edge (headline "MAGNITUDE 15").
3. By 01:00.000, complete the debris ring (all fragment PNGs at full opacity, arranged in a circle) and fade in the host figure (C01) with a "PHEW!" thought-bubble graphic (G05) at frame-right.
KEYFRAMES: Opacity fade-in on each debris fragment (staggered ~0.1s apart for a "forming" look); no position keyframes on the globe itself.
TOOLS: Image swap, overlay, opacity, text layer.
TEXT: "MAGNITUDE 10" / "MAGNITUDE 11" / "MAGNITUDE 15"; "PHEW!".
TRANSITION: Hard cut in/out.
AUDIO SYNC: Two measured near-silence gaps (61.4s, 65.2s) fall inside this shot — align any planned narration beat/pause there if re-recording.
END STATE: F06.3

### S07 01:06.667–01:14.583
SOURCE STATES: F07.0 → F07.1
MEDIA: C02, T01, T03
TRACK STACK:
V2 — LIVE TV inset (C02)
V1 — headline/fact text
A1 — narration/music (AU01)
INITIAL COMPOSITION: "MAGNITUDE 18" headline with "10^32 JOULES = BYE BYE EARTH" sub-text, centered, no illustrated object.
BUILD: Place the two text layers; at 01:10.000 fade in the LIVE TV inset (C02) with its caption below the existing text.
KEYFRAMES: Opacity fade-in on the TV inset (~0.5s).
TOOLS: Text layer, overlay, opacity.
TEXT: "MAGNITUDE 18"; "10^32 JOULES = BYE BYE EARTH"; TV caption "A SUSPECTED MAGNITUDE 18 QUAKE HAS DESTROYED ALL SEISMOMETERS ON THE PLANET."
TRANSITION: Hard cut in/out.
AUDIO SYNC: None distinct measured.
END STATE: F07.1

### S08 01:14.583–01:17.625
SOURCE STATES: F08.0
MEDIA: E03, G04, C01, G05, T01
TRACK STACK:
V2 — host + "PHEW!" bubble (small, edge of frame)
V1 — fragmented-Earth close-up (E03/G04)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Close-up of Earth broken into large jagged fragments, held loosely together, centered.
BUILD: Place the fragmented-Earth PNG; hold static for the full 3.0s. No motion needed.
KEYFRAMES: None.
TOOLS: Image placement only.
TEXT: "MAGNITUDE 18".
TRANSITION: Hard cut in/out.
AUDIO SYNC: None distinct measured.
END STATE: F08.0

### S09 01:17.625–01:23.292
SOURCE STATES: F09.0 → F09.1
MEDIA: E03, G04, G03, T01
TRACK STACK:
V1 — Earth fragments (E03/G04)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Same fragmented-Earth cluster as S08, "MAGNITUDE >18" headline.
BUILD: Keyframe each fragment's position outward from center over the full 5.7s, ending fully dispersed in a radial pattern filling the frame; add short motion-streak overlays trailing each fragment for the last ~2s.
KEYFRAMES: Position keyframes per fragment, 01:17.625 (clustered) → 01:23.292 (dispersed); stagger slightly per fragment for a natural burst.
TOOLS: Position keyframe, scale (fragments may grow slightly as they approach camera), motion-streak overlay.
TEXT: "MAGNITUDE >18".
TRANSITION: Hard cut in/out.
AUDIO SYNC: None distinct measured.
END STATE: F09.1

### S10 01:23.292–01:32.750
SOURCE STATES: F10.0 → F10.1 → F10.2
MEDIA: O07, O08, T01
TRACK STACK:
V1 — sun/magnetar object (O07/O08)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Plain sun circle with a spiky outline, centered, "MAGNITUDE 24" headline.
BUILD:
1. Hold the spiky-sun state briefly, then crossfade its surface to a banded/striped texture overlay by 01:27.000.
2. Continue crossfading the banded texture to a dense dotted texture, then scale/morph it down into a small dark core with a radiating field-line overlay (O08) fading in, complete by 01:32.750.
KEYFRAMES: Crossfade opacity between texture overlays; scale-down keyframe on the object as it becomes the magnetar core.
TOOLS: Crossfade, scale keyframe, overlay.
TEXT: "MAGNITUDE 24"; "*SUNQUAKE" sub-caption (brief, early in this shot).
TRANSITION: Hard cut in/out.
AUDIO SYNC: One measured near-silence gap (84.6s) falls near the texture-morph boundary.
END STATE: F10.2
FIDELITY LIMITATION: The exact sub-second timing of the sunquake→banded→magnetar progression is LIKELY (1fps-sampled), not frame-exact.

### S11 01:32.750–01:37.083
SOURCE STATES: F11.0
MEDIA: O08, T02, T03
TRACK STACK:
V1 — magnetar (O08)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Full-frame magnetar, dark core with radiating field lines, "KERTHUMP" burst text, "SGR 1806-20" label.
BUILD: Loop/pulse the field-line overlay's opacity and slight scale outward on a ~1s cycle for the full 4.3s, synced to the "KERTHUMP" text appearing once near shot start.
KEYFRAMES: Opacity/scale pulse keyframes, repeating.
TOOLS: Opacity keyframe, scale keyframe, text layer.
TEXT: "KERTHUMP"; "SGR 1806-20".
TRANSITION: Hard cut in/out (out boundary APPROXIMATE — see `TIMELINE.csv` notes).
AUDIO SYNC: None distinct measured.
END STATE: F11.0

### S12 01:37.083–02:05.958
SOURCE STATES: F12.0 → F12.1 → F12.2 → F12.3 → F12.4 → F12.5 → F12.6
MEDIA: O08, O07, G03, C01, E04, O09, E06, T01, T03
TRACK STACK:
V3 — thought bubble / explosion overlay
V2 — sun, host figure, or truck+house (swaps per state)
V1 — background (off-white or ground plane)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Magnetar carrying over briefly from S11.
BUILD:
1. At 01:39.000, hard-swap the magnetar to a plain sun labeled "MAGNITUDE 25".
2. At 01:41.000, trigger an explosion-burst overlay (G03) on the sun and fade in the host figure with speech text "PLEASE DON'T!".
3. At 01:43.000, hard-swap to the calm host figure alone, centered.
4. At 02:00.000, fade in a thought-bubble graphic (G05) with a small house inside it beside the host's head.
5. At 02:03.000, swap the bubble's content to the small truck+10m-drop preview.
6. At 02:05.000, hard-swap the whole frame to the full-scale "MAGNITUDE 1" truck-and-house demonstration (no bubble outline, no host figure).
KEYFRAMES: Opacity fades on each reveal; no position keyframes until the final full-scale swap.
TOOLS: Image swap, overlay, opacity, text layer.
TEXT: "MAGNITUDE 25"; "PLEASE DON'T!"; "MAGNITUDE 1".
TRANSITION: Hard cut in; hard cut out.
AUDIO SYNC: Three measured near-silence gaps (106.9s, 108.6s, 111.1s) fall inside this shot's host/thought-bubble section; one gap (125.6s) falls almost exactly at this shot's end.
END STATE: F12.6
FIDELITY LIMITATION: This shot's start boundary (F12.0, carried over from the magnetar) is an APPROXIMATE attribution — the measured cut at 92.75s does not correspond to an obvious visual swap at 1fps sampling resolution.

### S13 02:05.958–02:12.583
SOURCE STATES: F13.0 → F13.1
MEDIA: O09, E04, G06, G04, T01
TRACK STACK:
V1 — truck+house, then debris wall
A1 — narration/music (AU01)
INITIAL COMPOSITION: Truck suspended above house, "MAGNITUDE 1" headline.
BUILD:
1. Keyframe the truck's position downward to ground level over ~1s, then add shake/motion-line overlays (G06) to truck and house.
2. At 02:08.000, hard-swap the whole frame to the "MAGNITUDE 0" debris-wall graphic (G04) with tumbling particle figures.
KEYFRAMES: Position keyframe on the truck (drop); opacity on the shake overlay.
TOOLS: Position keyframe, overlay, image swap.
TEXT: "MAGNITUDE 1"; "MAGNITUDE 0".
TRANSITION: Hard cut in/out.
AUDIO SYNC: None distinct measured.
END STATE: F13.1

### S14 02:12.583–02:50.958
SOURCE STATES: F14.0 → F14.1 → F14.2 → F14.3 → F14.4 → F14.5 → F14.6 → F14.7 → F14.8
MEDIA: E05, C01, C03, O10, O11, C04, O12, O13, O14, O15, O16, C05, T01, T02, T03
TRACK STACK:
V1 — per-state illustration (swaps every ~3-6s)
A1 — narration/music (AU01)
INITIAL COMPOSITION: Tree with a leaf mid-fall, "MAGNITUDE -1" headline.
BUILD: This shot is nine sequential hard-swap segments on a single video track. For each, place the state's illustration, add its headline text, and any onomatopoeia text, holding for the durations below (see `TIMELINE.csv` for exact frame ranges):
1. 02:12.583 "MAGNITUDE -1": tree scene; keyframe the leaf's position downward with a slight side-to-side sway over the state's duration.
2. 02:17.000 "MAGNITUDE -2": filing-cabinet scene; keyframe the cat's position falling off the cabinet ("WHUMP" text appears on impact).
3. 02:21.000 "MAGNITUDE -3": trash-can scene; keyframe the cat's position tumbling into the can ("CRASH" text; add speech text "I DESERVE THAT.").
4. 02:24.750 "MAGNITUDE -4": dog, static, no keyframes ("PLINK" text).
5. 02:28.000 "MAGNITUDE -5": desk/computer scene, static, no keyframes ("CLICK" text).
6. 02:32.400 "MAGNITUDE -6": laptop scene, static, no keyframes.
7. 02:35.292 "MAGNITUDE -7": feather scene; keyframe the feather's position falling slowly with a gentle rock.
8. 02:38.417 "MAGNITUDE -8": hourglass scene; loop a sand-particle-flow overlay/animation for the state's duration.
9. 02:44.292 "MAGNITUDE -15" (render this headline in gray, dimmer than the others): table+mouse scene; a barely-visible single-frame twitch on the mouse is optional and easy to skip without noticeable fidelity loss.
KEYFRAMES: Position keyframes on the leaf, cat (x2), and feather; opacity/particle-loop on the hourglass sand.
TOOLS: Position keyframe, opacity, particle/looping overlay, text layer, hard cut between each of the 9 segments.
TEXT: "MAGNITUDE -1" through "MAGNITUDE -15"; "WHUMP"; "CRASH"; "I DESERVE THAT."; "PLINK"; "CLICK".
TRANSITION: Hard cut in; hard cuts between every internal state; hard cut out.
AUDIO SYNC: Two measured near-silence gaps (144.5s, 147.8s) fall near the -4/-5 boundary; one gap (158.2s) falls almost exactly at the -7/-8 boundary.
END STATE: F14.8

### S15 02:50.958–02:55.292
SOURCE STATES: F15.0 → F15.1
MEDIA: E05, C01, E06, E04, O17
TRACK STACK:
V1 — black card, then ending vignette
A1 — narration/music (AU01)
INITIAL COMPOSITION: Full black frame.
BUILD: Hold solid black for ~1s, then hard-cut/wipe to the outdoor vignette (tree, seated host figure, distant hillside house, rock/path); add two bird shapes with a position keyframe moving left-to-right across the upper-right sky over the remaining ~3.3s.
KEYFRAMES: Position keyframe on the two bird shapes only.
TOOLS: Solid color clip, wipe/cut transition, position keyframe.
TEXT: None.
TRANSITION: Hard cut in; hard cut out to credits.
AUDIO SYNC: Narration is LIKELY ending around here — most of this shot and all of S16 fall within the extended near-silence region (173.8-185.3s).
END STATE: F15.1

### S16 02:55.292–03:05.292
SOURCE STATES: F16.0
MEDIA: G07
TRACK STACK:
V1 — credits card (G07)
A1 — narration/music (AU01), likely silent/music-only here
INITIAL COMPOSITION: Full-frame static red credits card.
BUILD: Import the credits still (or reuse the identical clip from any other video in this project's library, since it is unchanged) and hold for the full ~10s to the end of the video.
KEYFRAMES: None (static hold).
TOOLS: None beyond placing the clip.
TEXT: Baked into the credits image (crew names, book titles, copyright).
TRANSITION: Hard cut in; end of video.
AUDIO SYNC: Extended near-silence measured through this entire shot.
END STATE: F16.0
