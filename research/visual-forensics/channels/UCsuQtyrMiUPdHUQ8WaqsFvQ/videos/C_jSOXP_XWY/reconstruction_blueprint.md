# Reconstruction blueprint — C_jSOXP_XWY (source sha ac77a0b04110)

Two uses, kept separate: (A) **evidence-matched reconstruction test** of this source's observable output (internal QA only; source artwork, script, voice and branding remain the creator's and are not reusable assets); (B) **original transfer** — the same mechanics applied to a NEW topic, new drawings and new script (see the channel production manual).

## Global tokens (MEASURED unless marked)
- Aspect 9:16 1080x1920, 50/1 fps CFR.
- Canvas background exact #FCFCFC; top quantised bins #F0F0F0, #101010, #F0F010, #D0D0D0, #B0B0B0; yellow in 6/8 holds (mean share 2.14%); red in 0/8 holds; any saturated colour in 8/8 holds. Mean settled dark-ink coverage 8.7% (max 12.5%).
- Line art and character specifics: see review/*/observations.md, review/*/asset_inventory.csv and review/native_art_review.md (OBSERVED). Exact stroke width, typeface, software, layer structure: UNAVAILABLE.

## Per-state prompts (derived from reviewed descriptions; ESTIMATED layout)

| State | Source interval (s) | Image prompt (reconstruction) | Motion into next state | Must stay static | Negative |
|---|---|---|---|---|---|
| VS001 (G0001) | 0.0–1.82 | 9:16 1080x1920, canvas/lighting as described (video background mode #FCFCFC), drawn state: White background. Black title text 'A CAVEMAN' / 'EXPLAINS' at top and 'CAPITALISM' at bottom. Centre: caveman in yellow leopard-spot tunic wearing black sunglasses, arms crossed, scowling bearded face, standing. | POSE_SWAP at 1.82s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS002 (G0003) | 1.84–2.56 | 9:16 1080x1920, canvas/lighting as described (video background mode #FCFCFC), drawn state: Caveman without sunglasses holding two small stick-items in left hand and a padlock-shaped object in right hand; neutral face. Title text unchanged. | POSE_SWAP at 2.56s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS003 (G0005) | 2.58–3.4 | 9:16 1080x1920, canvas/lighting as described (video background mode #FCFCFC), drawn state: Caveman with foot on block holding US-style flag on pole, squinting frown. Title text 'A CAVEMAN EXPLAINS' / 'CAPITALISM' unchanged. | SCENE_SWAP at 3.4s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS004 (G0007) | 3.42–6.02 | 9:16 1080x1920, canvas/lighting as described (video background mode #FCFCFC), drawn state: Same drawing as final tile of G0006: laughing caveman with round glasses, hands raised, coil device with spark lines at right. | SCENE_SWAP at 6.02s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS005 (G0009) | 6.04–6.94 | 9:16 1080x1920, canvas/lighting as described (video background mode #FCFCFC), drawn state: Caveman seated in A-frame tent with bowl, frowning; sign reads 'WILL HUNT FOR FIRE'. | SCENE_SWAP at 6.94s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS006 (G0011) | 6.96–8.98 | 9:16 1080x1920, canvas/lighting as described (video background mode #FCFCFC), drawn state: Same worried caveman with glasses, standing, sweat marks, mouth open; drawn smaller within frame than in G0010 first tile (size differs, may be tile scaling; held state). Yellow tunic present. | POSE_SWAP at 8.98s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS007 (G0013) | 9.0–10.24 | 9:16 1080x1920, canvas/lighting as described (video background mode #FCFCFC), drawn state: Sad naked caveman with solid black oval hole in belly, eyes closed, arms hanging. | POP_ON_OBJECT at 10.24s over 1 frame(s) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |
| VS008 (G0015) | 10.26–11.78 | 9:16 1080x1920, canvas/lighting as described (video background mode #FCFCFC), drawn state: Sad naked caveman with black belly hole containing small white ghost-like spirit with grumpy face and curled tail. Last frame of the clip. | end of video (hold) | all elements not named in the next event | no elements, colours, gradients or effects not described for this state; no extra props or text; no camera shake |

## Editor construction (OBSERVED grammar → steps)
1. Build each composition as separate layers: canvas, character pose drawing(s), props, text (one possible route; source layers are UNAVAILABLE).
2. Cuts = replace whole composition on the same canvas (hard cut, 0 frames).
3. Pops/pose swaps = visibility on a single frame; moves = translate/scale over the measured frame count; dissolves = cross-fade over the measured frame count. Use the measured duration of each event from visual_event_ledger.csv.
4. Align each event onset to the narration word that names the element (ASR_UNCERTIFIED in source; verify by listening in production).

## QA
- Frame-compare each state against its source tile at native resolution (internal test only).
- Onset tolerance target: ±2 frames of source event onset (MEASURED source values in visual_event_ledger.csv).
- Legibility at 320 px width; numbers on screen must equal narrated numbers.
- Listening/AV pass requires a human listener (source analysis has none).
