# 02: Asset plan & image prompts (for Codex)

You do **not** generate images yourself. You plan every visual, decide how each is made, and write a prompt file the user hands to **Codex**. Codex generates the images into a folder and the user puts that folder back in `work/02_assets/generated/`.

## 1. First decide HOW each visual is made: `02_assets/asset_plan.md`

For every visual beat in the EDL, choose the cheapest method that still looks hand-made. In priority order:

| Method | Use for | Why |
|---|---|---|
| **T: Typography only** | key words, numbers, chapter titles, questions | the cleanest premium look; zero AI risk |
| **C: Code-drawn** (SVG / canvas / Three.js, made by you in HyperFrames) | diagrams, arteries filling and blocking, blood-sugar graphs, the insulin "key and lock", icons, arrows, counters, the light-3D heart | anatomy logic stays correct; it animates perfectly; it looks like After Effects shape layers |
| **R: User's reference / sound / existing footage** | anything in `input/references/` | already approved by the user |
| **G: Generated still** (this file) | real-life situation shots, objects, textures, background plates | gives the "real world" feeling the hooks need |

Write a table: `Beat # | Timecode | What the viewer must understand | Method (T/C/R/G) | Asset IDs | Animation idea (keyframes/mask)`.

**Rule:** anatomy and medical mechanisms are **C (code-drawn)**, not G. AI images often draw anatomy wrong, and a wrong heart in a cardiologist's video destroys trust.

## 2. How many prompts

Roughly **one G-asset per 8–12 s of narrator or overlay time**, plus plates and textures. That is usually 20–40 for a 5–8 min video, 50–100 for 15 min+. For each important asset write **2 variations** (`a` / `b`) so the user can choose.

## 3. The style lock (put this block at the top of `asset_prompts.md`; every prompt inherits it)

Choose the style that matches the direction approved at GATE 0. Default ("Clinical Calm", see `03_EDIT_SPEC.md` §2):

```
STYLE LOCK (apply to every image):
Editorial photography look, natural soft window light, muted warm-neutral palette
(off-white, warm grey, deep navy, one accent of clinical red #D64545 only where noted).
Shallow depth of field, 50mm lens feel, subtle film grain, realistic textures,
uncluttered composition with generous negative space for typography.
NO text, NO letters, NO logos, NO watermarks, NO brand names, NO medical gore,
NO glossy CGI, NO plastic skin, NO oversaturated colours, NO futuristic holograms.
People: never a clear face. Show hands, silhouettes, backs, over-the-shoulder,
or faces cropped/out of focus. Pakistani / South-Asian everyday settings
(homes, stairs, streets, kitchen, clinic waiting area), modest clothing.
```

Why no clear faces: AI faces are the #1 thing that makes a video "feel AI", and invented realistic people next to a real doctor can mislead viewers.

## 4. Prompt format (exactly this, so Codex can batch it)

The file starts with instructions for Codex:

```markdown
# Asset prompts: Dr. Rehan explainer
## Instructions for Codex
- Generate one image per prompt block below, in order.
- Save each with the exact file name given, into the folder `generated/`.
- Use the size and background stated in each block. For "transparent", output PNG with alpha.
- Prepend the STYLE LOCK to every prompt.
- Do not add text to images. If a generation fails, retry once, then log it in `generated/_failed.txt`.
- When done, write `generated/_index.md` listing each file and its prompt ID.

## STYLE LOCK
(…)
```

Then one block per asset:

```markdown
### G07a: stairs_breathless_a.png
- Size: 2048×1152 (16:9)  |  Background: full scene
- Used in: H01 cold open, 0:02–0:06. Slow push-in + mask reveal from the left.
- Layers needed: yes → also generate G07a_fg.png (person only, transparent) and G07a_bg.png (empty stairs)
- Prompt: A middle-aged South-Asian man seen from behind, one hand on the railing
  of a narrow concrete staircase in a Karachi apartment building, pausing mid-climb,
  slightly bent forward, late-afternoon light through a stairwell window, dust in the
  light beam, his face not visible.
- Avoid: visible face, text on walls, dramatic horror lighting.
```

## 5. Asset types to include (as the script needs them)

1. **Situation plates (16:9 and 9:16 versions)** for hooks and re-hooks: stairs, a family dinner with sweets, a chai cup and a mithai box, a man rubbing his left arm, an elderly hand holding a glucometer, a clinic waiting room, a pharmacy shelf (no brands), a morning walk in a park.
2. **Layer-split plates for 2.5D parallax**: the same scene as foreground (transparent), midground and background. Ask for these on the 4–6 most important shots only.
3. **Hero objects on transparent background** for masks and pop-ins: glucometer, insulin pen, stethoscope, ECG paper strip, sugar cubes, a salt shaker, a pill organiser, an apple, a walking shoe.
4. **Textures**: paper, card stock, frosted glass, soft fabric. Use these as backgrounds behind typography, 4096 px, seamless if possible.
5. **Vertical (9:16) versions** of every plate used in Version B. Recompose them; don't just ask for a crop.

Do **not** request: hearts, arteries, blood cells, organs (code-draw these), Dr. Rehan himself, any real person, logos, charts with numbers.

## 6. Sound plan: `02_assets/sound_plan.md`

List every sound need and its source:
- From `input/references/` (the user's sounds): map each file to its use.
- Generic SFX (whoosh, soft click, paper slide, pop, heartbeat, ECG beep, riser, low hit): free sources with a clear licence (Freesound CC0, Pixabay, YouTube Audio Library), or synthesised in code (Lemo-Opuscar's `core/audio/sfx.py` approach). Record every source and licence for `CREDITS.md`.
- Music bed: calm, minimal, documentary piano/pads/soft pulse, around 80–100 BPM, no vocals. The music must leave room for the voice. Note one moment where the music changes (e.g. it drops out before the key medical point).

## 7. GATE 2 message to the user

Tell them, in Roman Urdu: how many prompts there are and the exact folder name to return (`generated/`), that the MP3s must be named by ID in `work/03_narration_audio/`, which IDs are missing so far, and that you will start the edit as soon as both arrive.
