# Reconstruction blueprint v2 — sFTRRdHqZIQ (closure v1; rv1 blueprint unchanged)
Use A = internal evidence-matched test only (source art, script, voice, names and branding are not reusable). Use B = ORIGINAL transfer: new subject and drawings, PROMPT_PACK_v2 locks and original branding; never the source logo, title lockup, creator name or recurring characters.
Global: 1080x1920, 24 fps CFR, 1766 f. DARK_FIELD #0C0C0C with sparse white dot stars for space states, white monoline; LINE_ART near-white canvas for EARTH/grinder/skin states; persistent white title chip `WHY SPACE IS WARM` (black caps on white box, top centre) with sub-chip `PART 1`/`PART 2`; grey Earth limb (light-grey land, mid-grey sea) with dashed white atmosphere line, pale blue tint on it from VS015 (only colour).

| State | Frames | Enter (event @frame, length) | Image prompt (rv1 description verified on native/half-scale view; corrections applied) |
|---|---|---|---|
| VS001 | 0–74 | first frame | Black canvas with a few faint white stars; white label box 'WHY SPACE IS WARM' at top; text 'SPACE' upper-middle above a white-outline stick figure with a double-circle head (helmet). Lower half empty black. |
| VS002 | 82–107 | WIPE_IN_PANEL @f75, 7 f | Split screen: upper half = VS001 (space, helmeted white stick figure under `SPACE`); lower half = white panel with `EARTH` label, tree, faceless stick figure, squirrel and chair on stippled air-dot texture |
| VS003 | 109–137 | POP_ON_ARROWS @f108, 1 f | Split as VS002; Earth half adds many small black curved heat arrows around tree, figure, squirrel and chair |
| VS004 | 139–200 | POP_ON_LABEL+POP_ON_ARROWS @f138, 1 f | VS003 + sub-chip `ANSWER: RADIANT HEAT` under the title; ring of small white outward arrows and two `?` marks around the space figure |
| VS005 | 202–275 | SCENE_SWAP @f201, 1 f | Black space upper, grey Europe limb lower with white dashed atmosphere arc; title 'WHY SPACE IS WARM' only. |
| VS006 | 277–338 | POP_ON_LABEL @f276, 1 f | Title plus 'PART 1' label; empty space above Earth limb. |
| VS007 | 342–372 | WRITE_ON_TYPE @f339, 3 f | Formula 'T = 2/(3k_B) · KE average' mid-canvas, title, 'PART 1', Earth limb. |
| VS008 | 374–507 | POP_ON_OBJECT @f373, 1 f | Formula, five spark particles with arc trails over limb. Encoder artifact frame 417 noted. |
| VS009 | 509–578 | POP_ON_OBJECT+POP_ON_LABEL @f508, 1 f | VS008 + small white tumbling astronaut at left with hand-lettered caption `THIS IS THE HOTTEST PLACE I'VE EVER GOTTEN FROSTBITE` |
| VS010 | 580–647 | SCENE_SWAP @f579, 1 f | White canvas: goggled adult at grinder on bench, small child at left; no sparks. |
| VS011 | 649–812 | POP_ON_OBJECT @f648, 1 f | Grinder scene with sparks; encoder artifacts frames 721 and 801 noted. |
| VS012 | 814–958 | POP_ON_LABEL @f813, 1 f | Grinder scene with sparks and '~2000°F (1100°C)' label with leader line. |
| VS013 | 960–999 | SCENE_SWAP @f959, 1 f | Near-white canvas; horizontal curved line (skin surface) with caption `PAPA MUNROE'S SKIN` below (source-specific name: never reuse); one spark dot with a zigzag trail above |
| VS014 | 1001–1067 | STATE_SWAP_SPARK_TO_WISP @f1000, 1 f | Same skin line + caption; spark replaced by a dot at the line with a thin wavy smoke wisp |
| VS015 | 1069–1308 | SCENE_SWAP @f1068, 1 f | Submarine with smooth white body and three sparks with trails, title, Earth limb. Sparks and sub unchanged. |
| VS016 | 1315–1338 | SPARKS_FADE_OUT+FILL_TEXTURE_SWAP @f1309, 6 f | Hatched submarine alone, no sparks or arrows; title and Earth limb. |
| VS017 | 1340–1392 | POP_ON_ARROWS @f1339, 1 f | Submarine with outward arrows all round. |
| VS018 | 1394–1455 | POP_ON_LABEL @f1393, 1 f | Title, 'PART 2', submarine with outward arrows, Earth limb. Encoder artifact frame 1401 noted. |
| VS019 | 1457–1519 | POP_ON_OBJECT_SWAP_ARROWS @f1456, 1 f | Submarine with fan at right and wind lines; title and 'PART 2'. |
| VS020 | 1521–1568 | POP_OFF_OBJECT @f1520, 1 f | Hatched submarine alone; title, 'PART 2', Earth limb. |
| VS021 | 1570–1657 | POP_ON_ARROWS @f1569, 1 f | Hatched submarine with a ring of small wavy (radiant-heat squiggle) arrows above and below; title + PART 2; Earth limb |
| VS022 | 1659–1732 | SCENE_SWAP @f1658, 1 f | No Earth, no title: tilted white-grey space capsule wearing a grey knit pom-pom hat and grey scarf, motion trail lines |
| VS023 | 1734–1765 | STATE_SWAP_REMOVE_CLOTHING @f1733, 1 f | VS022 with hat and scarf removed; bare capsule, same pose and trails |

Motion: 1-frame pops/cuts except: G0002 f75–81 lower-panel PUSH-IN from the left, linear ~154 px/frame (edge x 153→1079 over 7 f, no easing, content travels with the panel); G0012 f339–341 left-to-right formula write-on in 3 frames (`T=` → `T=2/3k_B·KE_(` → full); G0030 f1309–1314 6-frame cross-dissolve (sparks fade out while submarine fill changes plain→hatched). No camera moves (hold-pair shift <= 0.03 px).
Continuity: title chip fixed position in all space states; PART chip changes 1→2 at f1393; Earth limb drawing identical across SH space shots; submarine stays at one position, only overlays change; capsule pose identical VS022→VS023.
QA: (1) use A frame compare per state at native res; (2) every onset within ±1 frame of the ledger; (3) pops change on exactly 1 frame, multi-frame events match the measured curve (activity_curves.csv); (4) holds still (<0.1% changed px excluding grain); (5) all text exactly as transcribed in CLOSURE.md and legible at 320 px width; (6) use B originality check.
Not done: per-video render test (not required by contract v1).
