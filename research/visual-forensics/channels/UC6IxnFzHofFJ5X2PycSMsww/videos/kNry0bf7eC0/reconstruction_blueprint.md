# Reconstruction blueprint — kNry0bf7eC0 (source sha cb6eb61dd038)

Two uses, kept separate: (A) **evidence-matched reconstruction test** of this source's observable output (internal QA only; source artwork, script, voice and branding remain the creator's and are not reusable assets); (B) **original transfer** — the same mechanics applied to a NEW topic, new drawings and new script (see the channel production manual).

## Global tokens (MEASURED unless marked)
- Aspect 9:16 1080x1920, 24/1 fps CFR.
- Canvas background exact #4C4C4C; top quantised bins #505050, #707070, #909090, #D0D0D0, #B0B0B0; red accent in 0/9 holds; any saturated colour in 0/9 holds. Mean settled ink coverage 83.2% (max 98.4%).
- Line art: hand-drawn strokes (black on light canvases, white on dark scenes where present - see state descriptions); stick figures minimal, objects detailed (channel-typical, OBSERVED in reviewed videos). Exact brush/stroke width in px, typeface, software: UNAVAILABLE.
- Lettering: hand-lettered all-caps for titles/labels (OBSERVED). Footnotes may use a small serif text block (OBSERVED where present).

## Per-state prompts (derived from reviewed descriptions; ESTIMATED layout)

| State | Source interval (s) | Image prompt (reconstruction) | Motion into next state | Must stay static | Negative |
|---|---|---|---|---|---|
| VS001 (G0001) | 0.0–1.625 | 9:16 1080x1920, canvas/lighting as described (video background mode #4C4C4C), hand-drawn line art: Mid-grey canvas with grain; tilted black-ink solar panel on a thin pole (upper-middle) with a small lamp on a side arm (middle-left) casting a soft white glow. No text. No character. | UNRESOLVED_MINOR_CHANGE at 1.625s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS002 (G0003) | 1.6667–3.25 | 9:16 1080x1920, canvas/lighting as described (video background mode #4C4C4C), hand-drawn line art: Same composition as G0001: clean panel with grid cells, pole, lamp with white glow; no text. | STATE_SWAP_DAMAGE at 3.25s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS003 (G0005) | 3.2917–6.3334 | 9:16 1080x1920, canvas/lighting as described (video background mode #4C4C4C), hand-drawn line art: Panel now has dark smudges/cobweb marks upper area; pole and lamp with glow unchanged; no text. | STATE_SWAP_DAMAGE at 6.3333s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS004 (G0007) | 6.375–9.0 | 9:16 1080x1920, canvas/lighting as described (video background mode #4C4C4C), hand-drawn line art: Panel with heavy dark grime; pole shows dark streaked corrosion; lamp still glowing; no text. | SCENE_SWAP at 9.0s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS005 (G0009) | 9.0417–11.875 | 9:16 1080x1920, canvas/lighting as described (video background mode #4C4C4C), hand-drawn line art: Wide roadside scene: lamp light cone, 'HELP' box on pole, road, sign at left, spiky plant, ground glow; no '~100 YEARS' label. | POP_ON_LABEL at 11.875s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS006 (G0011) | 11.9167–15.3334 | 9:16 1080x1920, canvas/lighting as described (video background mode #4C4C4C), hand-drawn line art: Scene shifted/reframed with panel and pole right of centre and label '~100 YEARS' upper-right; sign at left edge; light cone and road; slight framing differs from G0009 tiles (INFERRED camera drift during hold). Scale differs from G0010 tile. | RAIN_ON at 15.3333s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS007 (G0013) | 15.375–18.4584 | 9:16 1080x1920, canvas/lighting as described (video background mode #4C4C4C), hand-drawn line art: Rain streaks across scene with '~100 YEARS' label, panel, lamp, HELP box, road, sign, plant. | SCENE_SWAP_BRIGHT at 18.4583s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS008 (G0015) | 18.5–23.4167 | 9:16 1080x1920, canvas/lighting as described (video background mode #4C4C4C), hand-drawn line art: Light background; hanging lamp with small rays at top; panel pole with lamp (dotted rays) and HELP box; grass tuft at base. | DARKEN_WITH_LIGHT_CONE at 23.4167s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS009 (G0017) | 23.4583–25.25 | 9:16 1080x1920, canvas/lighting as described (video background mode #4C4C4C), hand-drawn line art: Dark grey scene; hanging lamp at top (dark), solar panel pole with lit lamp casting cone onto ground glow, HELP box, grass at base; no text. | end of video (hold) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |

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
