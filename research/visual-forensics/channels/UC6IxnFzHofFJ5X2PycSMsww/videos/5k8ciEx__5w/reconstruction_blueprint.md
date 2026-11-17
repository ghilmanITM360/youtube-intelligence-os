# Reconstruction blueprint — 5k8ciEx__5w (source sha 05fce38976a3)

Two uses, kept separate: (A) **evidence-matched reconstruction test** of this source's observable output (internal QA only; source artwork, script, voice and branding remain the creator's and are not reusable assets); (B) **original transfer** — the same mechanics applied to a NEW topic, new drawings and new script (see the channel production manual).

## Global tokens (MEASURED unless marked)
- Aspect 9:16 1080x1920, 24/1 fps CFR.
- Canvas background exact #FDFDFD; top quantised bins #F0F0F0, #101010, #D0D0D0, #707070, #505050; red accent in 1/10 holds; any saturated colour in 1/10 holds. Mean settled ink coverage 1.4% (max 2.1%).
- Line art: hand-drawn strokes (black on light canvases, white on dark scenes where present - see state descriptions); stick figures minimal, objects detailed (channel-typical, OBSERVED in reviewed videos). Exact brush/stroke width in px, typeface, software: UNAVAILABLE.
- Lettering: hand-lettered all-caps for titles/labels (OBSERVED). Footnotes may use a small serif text block (OBSERVED where present).

## Per-state prompts (derived from reviewed descriptions; ESTIMATED layout)

| State | Source interval (s) | Image prompt (reconstruction) | Motion into next state | Must stay static | Negative |
|---|---|---|---|---|---|
| VS001 (G0001) | 0.0–1.4167 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Portrait white canvas; single black-ink stick figure (round head, no face, right arm raised bent) at left-middle. Nothing else. | POP_ON_OBJECT at 1.4167s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS002 (G0003) | 1.4583–5.4584 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Stick figure left, globe with roped bow right; no text. | SCENE_SWAP at 5.4583s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS003 (G0005) | 5.5–8.2917 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Rope across width on stakes; hair-bob stick figure left, crouched figure right gripping rope. Same as G0004. | SCENE_SWAP at 8.2917s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS004 (G0007) | 8.3333–12.4584 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Rope straight across mid-canvas on posts; hair-bob figure left (hand on hip) and plain-head standing figure right. No labels. | POP_ON_LABEL at 12.4583s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS005 (G0009) | 12.5–14.5 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Rope scene with label '6.28m' and curved arrow at the hair-bob figure; other figure at right. Encoding artifact flagged at frame 336 only. | SCENE_SWAP at 14.5s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS006 (G0011) | 14.5417–15.125 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Globe with outer grey circular arrow labelled 'C' at top; letter 'C' at right in black. Layout appears slightly shifted vs G0010 tile (globe a little smaller/higher) UNRESOLVED whether this is a camera adjustment or tile scaling. | WRITE_ON_TYPE at 15.125s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS007 (G0013) | 15.1667–16.2917 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Globe with C arrow ring and radius arrow 'r'; right text 'C = 2πr'. | POP_ON_LABEL at 16.2917s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS008 (G0015) | 16.3333–18.1667 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Globe diagram; right text 'C = 2π(r+1)'. | WRITE_ON_TYPE at 18.1667s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS009 (G0017) | 18.2083–19.2917 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Two-line formula 'C = 2π(r+1)' / '= 2πr + 2π' beside globe diagram. | POP_ON_LABEL at 19.2917s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS010 (G0019) | 19.3333–20.875 | 9:16 1080x1920, canvas/lighting as described (video background mode #FDFDFD), hand-drawn line art: Globe with C ring and radius r; formula lines 'C = 2π(r+1)' / '= 2πr + 2π' in black and red '~6.28'. | end of video (hold) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |

## Editor construction (OBSERVED grammar → steps)
1. Build each composition as separate layers: canvas, persistent anchors (e.g., ruler/axis), object drawings, labels, red marks.
2. Cuts = replace whole composition on the same canvas (hard cut, 0 frames).
3. Pops = layer visibility on a single frame; write-ons = stroke/mask reveal in reading order over the measured frame count; dissolves = cross-fade over the measured frame count; camera = translate/scale the anchor layer group.
4. Align each event onset to the narration word that names the element (ASR_UNCERTIFIED in source; verify by listening in production).

## QA
- Frame-compare each state against its source tile at native resolution (internal test only).
- Onset tolerance target: ±2 frames of source event onset (MEASURED source values in visual_event_ledger.csv).
- Legibility at 320 px width; numbers on screen must equal narrated numbers.
- Listening/AV pass requires a human listener (source analysis has none).
