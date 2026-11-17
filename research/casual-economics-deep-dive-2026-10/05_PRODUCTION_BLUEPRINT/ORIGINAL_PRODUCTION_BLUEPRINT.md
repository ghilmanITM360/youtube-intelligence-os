# Original Economics Explainer — Production Blueprint

Purpose: let an AI-assisted team build an **original** 10–16 minute economics explainer using the general techniques observed in Casual Economics (see `03_CHANNEL_DNA/CHANNEL_PRODUCTION_DNA.md`), **without** copying its characters, frames, artwork, thumbnails or brand. Research and specification only — no assets, video or animation project are created here.

Animation approach: static original illustrations, split into layers, moved with ordinary keyframes (position, scale, rotation, opacity, masks, trim paths, numeric counters, layer swaps). Text-to-video is not needed. Custom drawing is needed for pose and expression variants and for one-off metaphor illustrations (§4).

## 0. Originality guardrails (mandatory)

- Do not trace, recolour or "restyle" any Casual Economics frame, character, thumbnail or environment. Do not reproduce its host characters, its end-card layout, its colour combination plus logo, or its name.
- The traits worth borrowing are general genre conventions: simple characters on detailed backgrounds, cream chart cards, black year cards, literal metaphors. Create a **distinct visual identity**. Change at least: head shape (e.g. oval or square-ish instead of round), eye style, line weight, palette, typography family, chart colours and the host design.
- Real logos, seals, photographs and archival images need their own licence or fair-use review. Prefer drawn generic symbols ("central bank building") over real seals.
- Dramatized dialogue must be labelled internally as fiction and must not be presented as quotation. Real quotations need a cited source.

## 1. Pipeline

`Research → Script → Storyboard → Character/Asset Library → Layered Scenes → Keyframe Animation → Audio Sync → Editing → QA`

| Stage | Inputs | Output | Gate |
|---|---|---|---|
| 1. Research | Topic, 3–6 primary/academic sources, data series (FRED, IMF, World Bank, central banks, national statistics) | Claim sheet: every number with source, series ID, unit, date range, retrieval date | Every on-screen number has a row; superlatives are qualified |
| 2. Script | Claim sheet | ~150 words/min narration (≈1,800–2,400 words for 12–16 min), plus `[VISUAL]` cues per sentence | One visual proposition per sentence; hook ≤30 s ends in a question |
| 3. Storyboard | Script | Shot list: scene ID, plate, characters + pose IDs, props, overlay text, motion recipe, approx. duration | Each sentence mapped; reuse plan for each plate listed |
| 4. Character/asset library | Storyboard needs | Layered source files (§3–4) | Style sheet approved; consistency checklist passes |
| 5. Layered scenes | Library | Composed scene files with named layers | Layer order follows §5 |
| 6. Keyframe animation | Scenes + recipes (§6) | Animated comps | Motion timings fall within §6 ranges |
| 7. Audio sync | Voice recording, music, SFX | Timed narration; visual change points within ~0.2 s of the stressed word (target, not an observed channel value) | Word-level alignment checked by ear |
| 8. Editing | Comps + audio | Assembled cut | A new visual state every 1–4 s; text cards held long enough to read twice |
| 9. QA | Cut | QA sheet (§8) | All checks pass |

## 2. Script and story templates

**Acts (based on the 11-video pattern):**
1. Cold open (0–30 s): a contrast ("richest → breadline") or a magnitude ("worst crash in 60 years"), then an explicit question.
2. Rewind (chronology reset device) and setup (30–120 s).
3. Mechanism build (main body): 3–6 chapters, each ends with a 2–4 item list or a feedback loop diagram.
4. Peak event: dated cards and numbers.
5. Consequences: human scale (jobs, homes) shown with figures.
6. Response and lessons: numbered list plus a present-day parallel.
7. Close: callback to opening images, a viewer question, a pointer to the next video.

**Sentence-to-visual rule:** each sentence gets exactly one new visual proposition: a number, an icon, a pose change, a label or a chart step. Do not show two new ideas at once.

**Humour:** use absurd true numbers (verified) plus a sight gag. Avoid jokes that stereotype nationalities or that mock real private people.

## 3. Character system

**Base body (one per art style; define on a turnaround sheet):**
- Head: about 45–55% of figure height, simple primitive shape. Eyes: two shapes with a highlight. Mouth: one stroke.
- Hands: simple mitts. Torso: one rectangle-ish jacket shape with lapel/tie lines. Legs: two thin strokes, with feet as small ovals.
- Line: one consistent outline weight at 1080p (e.g. 6–8 px). Flat fills plus one shadow tone.

**Identity kit (swappable layers):** hair (10–15 shapes), glasses (3), facial hair (4), hats (8 period/role hats), outfit colours (palette of 12), badges/props in hand.

**Required pose library per recurring character (custom drawn):** neutral front, ¾ left/right, pointing, both hands raised (panic), hands on head, shrug, holding object (generic hand slot), walking A/B (two frames), sitting at desk. **Expression library:** neutral, happy, worried, panic grimace, angry, bored/closed eyes, surprised. A dialogue scene usually needs 3–5 swaps.

**Consistency rules:** fixed head size per shot scale (close, medium, wide); identity accessory always visible; colour of outfit never changes within a video unless story-motivated; eye level and line weight constant; one-off reaction drawings must match the base proportions.

**Host:** design one original explainer host with a unique silhouette (it is your channel's brand). Use it for questions, chalkboard explanations and pauses.

## 4. Asset library structure

```
library/
  characters/<char_id>/{base, poses/, expressions/, accessories/}
  environments/<plate_id>/{bg_far, bg_mid, furniture_front}   # separate layers so characters can sit behind desks
  props/{money/, documents/, buildings/, arrows/, signs/, metaphors/}
  maps/{world, regions/, countries/}  # vector, each country a separate shape for recolouring
  charts/templates/{bar, line, dual_line, pie, area, stat_grid}
  cards/{year_card, title_card, list_banner, quote_card, number_card}
  overlays/{rewind, pause, highlight_band, circle, strike}
  brand/{end_card, lower_third, logo}
```

**Minimum viable library for one 12-minute video:** about 8–12 environment plates (each reused 3–10 times), 6–10 characters (2 recurring with full pose libraries), 40–60 props, 6–10 chart instances from templates, maps for every geography mentioned. These figures are planning estimates from observed reuse (e.g. JPN ~10 recurring plates), not the creator's file counts.

**State variants to prepare in advance:** intact/damaged (car, house, bank), empty/full (money bags, stacks), normal/recoloured (map regions, loan tags), sketch/colour (landmark plates).

**Needs custom drawing (cannot be keyframed from a still):** new poses and expressions, period costumes, one-off metaphors (e.g. a figure covered in bandages, a building with a bubble), crowds with varied figures, environment plates.

## 5. Scene templates (layer order bottom → top)

1. **Character scene:** plate_far → plate_mid → characters → front furniture (desk/counter) → foreground props → caption → overlays.
2. **Concept card:** neutral field (cream, white or black) → icons → arrows → headline → number.
3. **Chart card:** cream field → axes/grid → series (trim path) → annotation (band, line, circle) → value labels → title.
4. **Map card:** black ocean → land shapes (separately colourable) → markers/icons → year/caption.
5. **Split screen:** two clipped panels with a 2–4 px divider; each panel animates on its own.
6. **List banner:** 2–4 full-width bars, each with an icon on the left; bars stack in sequence.
7. **Number punch:** blurred/dimmed scene → huge number (red = loss, green = gain) → subtitle.
8. **Dialogue skit:** fixed plate, 2–3 characters, pose swaps on line changes, optional speech bubble.

## 6. Movement recipes (keyframe operations)

Durations are suggested starting points; the source's exact timing and easing were not measured.

| Recipe | Keyframes | Suggested duration |
|---|---|---|
| Pop-in | opacity 0→100, scale 85→105→100% (ease-out) | 0.2–0.35 s |
| Slide-in | position from off-frame to rest, ease-out; optional 3–5° settle rotation | 0.3–0.5 s |
| Type-on | text reveal by character, linear | 12–25 characters/s |
| Counter | slider 0→N bound to text, ease-out; final value colour change | 0.6–1.2 s |
| Line draw | trim path end 0→100%, ease-in-out; label pops at end | 1–2.5 s |
| Bar grow | scale-Y 0→100% from baseline, staggered 0.05–0.1 s per bar | 0.6–1.2 s total |
| Pie sweep | radial wipe 0→100% | 0.5–0.8 s |
| Strike + correct | stroke trim 0→100% across text, then new text pop | 0.25 + 0.25 s |
| Pose swap | hold keyframe exchange of drawing layers on the word | instant |
| Prop swap (state change) | cut between variants, optional 2-frame white flash or shake | instant |
| Drop | position Y from above, slight overshoot, 2–4 px squash optional | 0.3–0.5 s |
| Bubble rise | position Y up + scale 60→100% + slight wobble rotation ±3° | 1–2 s |
| Accumulate | duplicate layer, offset start 0.08–0.15 s each | per item |
| Fade-to-one | opacity 100→25% on N–1 items, staggered | 0.6–1 s |
| Recolour | fill colour keyframe or crossfade to recoloured duplicate | 0.3–0.6 s |
| Sketch→colour | linear wipe on colour plate above sketch plate | 0.8–1.2 s |
| Camera push | parent scale 100→108–115%, ease-in-out | 2–6 s |
| Whip transition | position + directional blur across 6–10 frames | 0.2–0.35 s |
| Split panel | panel X from off-frame inside clip mask | 0.3–0.5 s |

## 7. Audio sync and editing rules

- Record narration first; cut visuals to narration.
- Place each visual change on the stressed keyword. Numbers appear when the number is spoken, not before.
- Music bed under narration; duck it under dense explanation; change the cue at act boundaries. Use only licensed tracks and credit them.
- SFX (whoosh on slides, pop on icons, cash register for money, thud for drops) are a production choice; their use by the source channel was not verified.
- Hold text cards long enough to read the text twice at normal reading speed.
- Year cards on black separate eras; avoid more than one consecutive black card.

## 8. Quality criteria (QA checklist)

**Factual:** every number on screen matches the claim sheet (value, unit, date, series); charts state source and range; superlatives are qualified; dramatizations are not presented as quotes; distinguish intraday from close values (e.g. Black Thursday) and nominal from real values.
**Visual:** character proportions and accessories are consistent; no copied third-party art; logos and photos are licensed; text is readable at 320×180; no typos (cf. JPN "TECHOLOGY" 804).
**Motion:** no sentence without a visual change for more than ~6 s unless it is a deliberate hold; no two simultaneous new concepts; transitions are consistent.
**Audio:** narration is intelligible over the music; no clipping (peak below −1 dBFS); music credits are present.
**Packaging:** the title promise is delivered in the first 30 s and paid off by the end; the thumbnail headline and focal face read at 160×90.
**Provenance:** the asset licence register and claim sheet ship with the project.

## 9. Thumbnail and title kit (original)

- Headline: 1–3 words naming the event or place, in your own typeface, with a high-contrast outline.
- One large original character with a strong emotion (fear, shock, greed), one central symbol of the mechanism (arrow, cracked emblem, bubble), plus an optional small secondary group.
- Title formulas observed (for adaptation, not copying): "[Event] in N Minutes", "How [Place] Got [Outcome]", "How [X] Actually Happened", "Did [Place] [Achieve Y]?". See `04_PERFORMANCE_RESEARCH/` for evidence on what performed; that evidence is weak.
