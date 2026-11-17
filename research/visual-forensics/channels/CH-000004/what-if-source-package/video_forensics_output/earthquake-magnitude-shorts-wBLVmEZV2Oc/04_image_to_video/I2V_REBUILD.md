# I2V REBUILD — earthquake-magnitude-shorts-wBLVmEZV2Oc

Reference: IMAGE_PROMPTS.md (IMG01-08), ANIMATION_PROMPTS.md (A02,A06+A07,A09,A16,A23,A25). This file sequences them per shot/state and covers final assembly. Text/graphic overlays not baked into source images are added here (CLEAN PLATE / TEXT OVERLAY specs already given in IMAGE_PROMPTS.md for IMG02).

## S01 — 00:00.00-04.60 (F01.0-F01.2)
STATE CHAIN: F01.0 → A02 → F01.2
SOURCE IMAGE: IMG01
IMAGE ACTION: Generate.
I2V PASS: A02
EXPECTED RESULT: F01.2 (seismograph malfunctioning)
TEXT/GRAPHICS OVERLAY: T01 title text + red strike-through shape, added in final assembly (not baked into IMG01)
AUDIO: narration lines 1-2
CUT TO: F01.3

## S01 — 00:05.00-08.00 (F01.3-F01.4)
STATE CHAIN: F01.3 → (static hold) → F01.4
SOURCE IMAGE: IMG02
IMAGE ACTION: Generate.
ANIMATION REQUIRED: NO — hold the image for 3.0s; only the red-circle annotation changes (add via overlay, see COMPOSITE)
TEXT/GRAPHICS OVERLAY: headline/SMS/dialogue text per IMG02's CLEAN PLATE spec; red circle shape fades in at local 1.00s (=6.00s absolute) over the "8"
COMPOSITE: circle overlay is a separate small transparent element, positioned over the numeral in the LIVE-box speech bubble
AUDIO: narration lines 3-5 (gag)
CUT TO: F01.5

## S01 — 00:08.50-18.10 (F01.5-F01.9)
STATE CHAIN: F01.5 → A06+A07 → F01.7 → (hold) → A08 → F01.8 → A09 → F01.9
SOURCE IMAGE: IMG03
IMAGE ACTION: Generate.
I2V PASS: A06+A07 (ruler grows), then A09 (scribble vibrates)
EXPECTED RESULT: F01.9 (bare ruler with red scribble)
ADDITIONAL INDEPENDENT PASSES: none — growth and scribble are on the same isolated ruler element, safe to keep as one element's sequential passes
TEXT/GRAPHICS OVERLAY: T01 title fades in/out at start/mid (A08), T02 caption paragraph fades in mid-growth then out (A08) — both added in final assembly since IMG03 has TEXT BAKED: NO
AUDIO: narration reads the logarithmic-scale fact during the 13.60-15.60s hold
CUT TO: F01.10

## S01 — 00:18.50-27.00 (F01.10-F01.12)
STATE CHAIN: F01.10 → A11 → F01.11 → A12 → F01.12
SOURCE IMAGE: IMG04
IMAGE ACTION: Generate.
ANIMATION REQUIRED: NO for the globe itself (optionally loop A25 in background) — epicenter marks, date labels, and the LIVE box are all overlay additions, not I2V motion
TEXT/GRAPHICS OVERLAY: T01 "MAGNITUDE 9" + T02 date labels fade in at A11 (21.50s); G01+C01+T02 (NASA LIVE box, using IMG08 frame + pose-sheet figure 2) fades in at A12 (23.50s)
COMPOSITE: LIVE box composited bottom-right, ~1/4 frame size
AUDIO: narration states the magnitude, then the real-world examples, then the North-Pole-shift trivia
CUT TO: F01.13

## S01 — 00:27.50-32.00 (F01.13-F01.14)
STATE CHAIN: F01.13 → A14 → F01.14
SOURCE IMAGE: IMG06
IMAGE ACTION: Generate.
ANIMATION REQUIRED: NO — hold image; "3500 KM" label is a text/arrow overlay added at A14 (30.50s)
TEXT/GRAPHICS OVERLAY: T01 "MAGNITUDE 10" (persistent from cut); T02 "3500 KM" + arrow shape fades in at 30.50s
AUDIO: narration gives the magnitude-10 rupture-length fact
CUT TO: F01.15

## S01 — 00:32.50-48.00 (F01.15-F01.17)
STATE CHAIN: F01.15 → A16 → F01.16 → A17 → F01.17
SOURCE IMAGE: IMG04 (F01.15, re-skinned/regenerated facing North America — reuse IMG04's prompt with continent changed) → IMG05 (F01.16-17)
IMAGE ACTION: Generate IMG05 as a distinct image (composition changes materially: crack + full spiky border is a different end-state than IMG04's clean globe, per the UNIQUE IMAGE RULE's "camera/composition changes substantially" trigger).
I2V PASS: A16 (crack + spiky border grows in)
EXPECTED RESULT: F01.16 (fully cracked/spiky globe, held)
ADDITIONAL INDEPENDENT PASSES: none needed for A17 — the distressed stick figure (pose-sheet figure 3) is a simple overlay fade-in, not an I2V motion pass
TEXT/GRAPHICS OVERLAY: T01 "MAGNITUDE 11" then "MAGNITUDE 15" (cut swap at 37.00s); distressed figure composited in at 45.00s
AUDIO: narration escalates tone here — first real sense of danger
CUT TO: F01.18
FIDELITY RISK: F01.15's plain North-America globe and F01.16's damaged version share a base design but are generated as two separate images to give the I2V engine a clean, simple starting frame for the crack/spike animation (avoids asking one pass to both introduce a new continent view AND perform major destructive changes).

## S01 — 00:48.50-51.50 (F01.18-F01.19)
STATE CHAIN: F01.18 → A19 → F01.19
SOURCE IMAGE: none (blank white canvas + title only — no illustration in this state)
IMAGE ACTION: N/A — this is a pure text beat, build directly in final assembly with no generated image.
ANIMATION REQUIRED: NO
TEXT/GRAPHICS OVERLAY: T01 "MAGNITUDE 18" cuts in at 48.50s; T02 "10^32 JOULES = BYE BYE EARTH" writes in at 49.50s
AUDIO: narration delivers the joules figure as the escalation's biggest number yet
CUT TO: F01.20

## S01 — 00:51.50-58.50 (F01.20-F01.21)
STATE CHAIN: F01.20 → A21 → F01.21
SOURCE IMAGE: IMG07 (F01.20), IMG08 (F01.21's LIVE box frame, reused)
IMAGE ACTION: Generate IMG07. Reuse IMG08.
ANIMATION REQUIRED: NO for either — both are static holds; the cut between them is a straight replacement, not a morph
TEXT/GRAPHICS OVERLAY: T01/T02 persist across the cut; LIVE-box caption "A SUSPECTED MAGNITUDE 18 QUAKE HAS DESTROYED ALL SEISMOMETERS ON THE PLANET." + pose-sheet figure 4 (headset) composited into IMG08's frame
AUDIO: narration delivers the deadpan punchline caption verbatim
CUT TO: F01.22

## S01 — 00:59.00-65.96 (F01.22)
STATE CHAIN: F01.21 → A22 → F01.22 → A23 → (video ends)
SOURCE IMAGE: IMG07 (reused from F01.20) + IMG07B overlay
IMAGE ACTION: Reuse IMG07; generate IMG07B (small transparent overlay only, not a full image).
I2V PASS: A23 (extra fragments burst outward)
EXPECTED RESULT: F01.22's final, more-chaotic debris state
TEXT/GRAPHICS OVERLAY: T01 swaps to "MAGNITUDE >18" at the 59.00s cut
AUDIO: narration trails off / ends on the open-ended finale
CUT TO: end of video (source file ends mid-animation at 65.96s — for new content, choose your own out-point or loop back to IMG01 for a Shorts-style loop)

## FINAL ASSEMBLY NOTES (applies across all shots)
- All hard-cut boundaries (A03, A05, A13, A15, A18, A21, A22) are straight cuts between held images/clips — no crossfade, no transition effect (OBSERVED, see VISUAL_DNA.md transition language).
- The ruler (IMG03) is composited as a persistent bottom layer under every state from F01.5 onward; only its own two motions (A06+A07 growth, then A24's subtle late reframe) apply to it — it is not regenerated per shot.
- G01's LIVE-box frame (IMG08) is generated once and reused for all three LIVE-box appearances, swapping only the composited pose-sheet figure and caption text each time.
- No high-risk motion-leakage cases were identified beyond what's already flagged (A16 continent/damage generation split, A25 rotation being unverified) — all other passes are simple, isolated, single-element motions on locked-camera compositions.
