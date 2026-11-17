# HumanCraft Video Studio V2 guide, applied to the Casual Finance clone (2026-11-08, LOCAL ONLY)

Source: `~/Downloads/HumanCraft_Video_Studio_V2_Complete_Guide.pdf` (35 pages, read in full). What it changes in our plan, and what it does not.

## What the guide says that matters here
- The goal is human-crafted animation: editable layered assets, authored keyframes, masks, camera, verified moving renders. Text-to-video and image-to-video are OFF by default as the source of shot motion. AI stills (art, mattes, clean plates) are allowed only if approved. (PDF p.3-5, 18-19, Part IV.)
- No skill is mandatory; pick a real, tested renderer (Remotion, Blender, Fusion, After Effects, CapCut/FFmpeg) and prove it with a tiny render first. If no renderer works, deliver assets and a blocker note and do NOT claim a video. (PDF p.1, 10, 17-18.)
- Narration/audio is the timing authority; transcript timestamps are suggestions until checked. A reference's visual grammar is learned, not copied (STYLE_BIBLE, REFERENCE_BREAKDOWN, ANIMATION_GRAMMAR, FEEDBACK_MEMORY). (PDF p.8-11.)
- Process: style proof (one still) -> moving 5-12 s proof with real narration -> review against the 10-dimension scorecard (find worst 3 issues) -> fix -> chapters -> whole-video rhythm pass. Do not call a scene complete without a working render. (PDF p.12, 16.)

## Fit with what we already built
| Guide requirement | Our status |
|---|---|
| Reference breakdown with SEEN vs INFERRED labels | Done in style (MEASURED/OBSERVED/ESTIMATED/INFERRED) in `model_sheets/MODEL_SHEETS_CASUAL_FINANCE.md` |
| Style bible | One-page v0.1 in the model sheets, 8 rules, with counterexamples |
| Honest reference intake (list what was actually seen) | 168 of 3,945 clusters viewed (`CATEGORY_AUDIT.md`); the rest rule-tagged |
| Shot grammar / motion grammar | Entering-class stats and rhythm per video are MEASURED; true motion curves and easing are NOT measured yet (one frame per state) |
| Sound grammar | UNAVAILABLE (audio blocked, ASR-only) |
| Original assets, not a clone of the creator | Style system only; characters/logo/name must be original |

## How the clone should be BUILT under this guide (design, not yet tested)
INFERRED from the sheets: Casual Finance visuals are layered cut-outs on white plus occasional flat-colour scene plates, so they suit the guide's "illustration and character craft" and "typography-led editorial" modes, not generated video. A stick-figure channel is easy to author with real layers.
- **Stick-figure rig:** head disc (peach fill + outline), face layer swap set (eyes/mouth: neutral, smile, grin, worried, panic, angry, asleep, shock), torso line, 2 arm lines + hook hand, 2 leg lines, hair/hat/glasses/clothes modifier layers, held-prop layer. Pivot points at neck, shoulders, hips. Poses are drawn swaps (matches the 230 POSE states), not constant wobble.
- **Props and anthropomorphic icons:** one transparent PNG/SVG per asset (money bag, banknote, oil barrel, coin, map with eyes layer, chalkboard + frame, newspaper, red arrow/circle/X). AI stills allowed only with the owner's approval; then segment, clean edges, keep originals.
- **Scene plates (Layer B):** separate sky/ground/foreground/furniture/character layers; the guide asks for clean plates behind any layer that moves.
- **Text:** editable text layers (hand font + serif + chalk style), red marker marks as vector strokes with a draw-on.
- **Motion library (candidate mapping, INFERRED, to be tested):** CUT -> hard cut (#59); POP_IN -> scale/opacity pop with small overshoot (#37, #43, #46 stagger); POSE -> pose-to-pose swap on ones/twos (#66, #54); ZOOM_IN -> push-in on a layer (#04); DRAWON -> trim-path write-on (#85); TEXT_TYPE -> typewriter (#78); MICRO -> small idle/follow-through (#44). The guide asks for 1-4 primary mechanisms per shot and says intentional restraint reads as professional.

## Gaps this exposes (not done)
1. **Motion curves are unmeasured.** We hold one frame per state. To copy HOW things pop in (duration, overshoot, easing) we need a few short frame-by-frame windows per class (about 10-30 frames each). Cheap and targeted; propose after the owner agrees.
2. **Renderer not verified.** Present on this Mac: ffmpeg, Node/npm, CapCut.app, a `remotion-best-practices` skill. NOT checked: whether a Remotion project/package works, no Blender, no ImageMagick. Per the guide, a tiny test render must pass before any "video" claim.
3. **Audio** remains BLOCKED; narration-driven timing cannot be verified against the originals.
4. **Stills generation** needs an owner-chosen image model and explicit approval (guide: stills allowed only if approved).
5. Step 5 held-out test, scorecard review and FEEDBACK_MEMORY loop come after a renderer works.
