# Style & Character Guide: Calf Pain / PAD Short

Machine-readable tokens: `project/STYLE_TOKENS.json` (the code imports it, so it's the single source of truth).

## Reference evidence (read-only YIOS research, ~6 min timebox)
| Source | What was taken |
|---|---|
| `casually-finance/2026-10-12/04_PRODUCTION_DNA/VISUAL_DNA.md` | White field, irregular thick black contour, round peach heads, dot eyes, sparse flat props; green = good, red = warning; one relationship per screen |
| `MOTION_DNA.md` (label counts) | CUT dominant; POP_IN, TEXT_REVEAL, additive BUILD, HIGHLIGHT, ZOOM_IN, POSE/FACE_CHANGE |
| `SHORTS_DNA.md` | Claim at ~0 s with no greeting; short caption chunks; additive diagrams; one bounded payoff |
| Source frames: 0ll9rEtoRrs 4.9–6.1 s (M0004) | **REVEAL_MOVE**: element enters progressively from the frame edge → Dr. Rahim's entrances (4.3 s, 40.0 s, 45.9 s) and the pointing hand (7.35 s) |
| 0ll9rEtoRrs 29.0–29.75 s (M0020) | **POP_IN_THEN_SCALE** → "Dr. Rahim" tag (4.74 s), "EARLY WARNING SIGN" stamp (35.22 s) |
| -X6YzlY_8tM 30.2–32.8 s (M0047) | **CUT_THEN_ZOOM_IN** → calf close-up (5.9 s), muscle shot (13.62 s), doctor medium shots (25.5 s, 32.9 s) |
| rSa2aziEsAI Short (1 frame / 6 s) | Outlined handwritten captions with the key word in red; personified objects (→ personified calf muscle) |
| Casual Economics `3tVMjRRXQIg` reconstruction (secondary) | Map/landmark + photo-footage montage. Photo footage **not** used: original vector art only, for medical credibility |

Nothing was copied: no source character, logo, illustration or scene is reproduced.

## Visual system
- **Paper** `#FFFFFF`, **ink** `#161616`, 7 px round-joined contours; a subtle animated "line boil" (fractal-noise displacement, seed steps every 4 frames) keeps the static art alive.
- **Semantic colour:** red `#E23B3B` = pain/warning, green `#2FA55A` = relief, amber `#F09A24` = caution/early signal, blue `#2F86DE` = oxygen, yellow `#F4CF57` = plaque.
- **Type:** Kalam 700 (bundled via `@fontsource/kalam`, so it works offline). Captions use a paper fill over a heavy ink outline, with the key word in a semantic colour. Text stays between y 230 and 1480 (Shorts safe zone).

## Characters (one rig, `project/src/rig.tsx`)
Both characters are the same parametric SVG skeleton: 2-bone legs and arms with forward kinematics plus 2-bone IK reach, a tilting head, posable hands (`fist / point / open / up / thumb`), a procedural walk cycle, auto-grounding and seat blending. They differ only in their `Look` record, so geometry, outline and proportions stay identical in every shot.

| | **Patient** (fictional) | **Dr. Rahim** (fictional; no likeness was supplied) |
|---|---|---|
| Silhouette | Messy brown fringe + back tuft, mustard tee, navy shorts (calves visible), white sneakers | Neat black side-part, round glasses, moustache + short beard, long white coat, teal scrubs, stethoscope, charcoal trousers |
| Skin | `#EDBE93` | `#B98159` |
| Views used | Side (walk, clutch, sit, rub, point), front (body map) | Front (wave, point, explain, present, hand-on-chin), side (crouch with magnifier) |
| Expressions | neutral, discomfort, pain, relief, concern, worried, understanding, surprised | happy, talk (lip-sync from the narration's loudness envelope), serious, concerned |

## Four environments (built once, reused)
1. **Park** (`env.tsx` `Park`): sidewalk, hedge, trees, lamps, one bench at a fixed world x. Used in S1, S2, S3, S6 and S10 (dusk tint).
2. **Clinic** (`Clinic`): wall, window, plant, whiteboard whose panels hold mini versions of the same patient. Used in S8, S9 and S13.
3. **Anatomy** (`anatomy.tsx` `LegCutaway`): the patient's lower leg with tibia, calf muscle and artery. Plaque, blood-cell flow and O₂ delivery are parameters. Also supplies the cross-section, gauge, personified muscle and the magnifier-lens callback.
4. **Risk map** (`BodyMap` + `ArteryTree`): the front-view patient with an artery overlay linking legs → heart → neck/brain. Used in S7b and S12.

## Medical wording rules applied
- Claudication = exertional calf pain that eases with rest; "not every cramp is PAD" is stated on screen.
- Rest pain is labelled "may signal severe blood-flow loss" and "persistent pain at rest → seek prompt medical assessment". The screen never asserts a CLTI diagnosis.
- Cardiovascular risk is shown only as direction (↑) with heart and brain icons. No statistics are given.
