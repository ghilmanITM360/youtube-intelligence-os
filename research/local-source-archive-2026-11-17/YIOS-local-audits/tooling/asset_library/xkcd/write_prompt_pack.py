#!/usr/bin/env python3
"""P6: write the xkcd-style ORIGINAL-cast prompt pack (text only; no image generation). usage: python3 -I write_prompt_pack.py
Writes <lib>/_channel/PROMPT_PACK/<asset_id>.md + PROMPT_INDEX.csv + README.md. Reference frames cited are ones opened in P2/P3."""
import csv, os
LIB = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif/asset_library"); OUT = f"{LIB}/_channel/PROMPT_PACK"; os.makedirs(OUT, exist_ok=True)
STYLE = ("hand-drawn black monoline ink illustration, one uniform line weight (about 8 px on a 1080 px tall frame), slightly wobbly hand-drawn "
         "line with round line ends, flat fills only (light greys #E4E4E4, #C4C4C4, #848484 where a fill is needed), no gradients, no shading, "
         "no texture, no outline glow; people are faceless stick figures: head = unfilled circle with no eyes and no mouth, torso, arms and legs "
         "are single lines, no hands or feet drawn; objects carry the detail (parts, hatching), people stay minimal")
NIB = ("NIB, the narrator: faceless stick figure, unfilled circle head about 0.37 of total figure height, small round wire glasses drawn on the "
       "front of the head as two little circles joined by a bridge (no eyes behind them), a short scarf knotted at the neck with two short "
       "tails filled flat grey #C4C4C4; torso, arms and legs single black lines")
TARDI = ("TARDI, the channel mascot: a chubby water-bear (tardigrade-like) creature drawn in black monoline ink, plump segmented body, eight stubby "
         "legs with tiny claw marks, small round snout opening, two small dot eyes, flat light-grey #E4E4E4 body fill")
ALPHA = ("Output: transparent PNG with a real alpha channel, no checkerboard pattern, no scenery, no ground shadow, one subject (or the listed set) "
         "only, consistent outline weight. If transparency is not available: solid pure green #00FF00 background, no green anywhere in the subject, "
         "no shadow on the background.")
NEG = ("no text, no letters, no numbers, no logos, no watermark, no faces on stick figures, no hands or fingers, no gradients, no 3D shading, "
       "no cel shading, no colour except the listed fills, no thick-thin calligraphic line variation, no sketchy double lines, no photo realism, "
       "no resemblance to any existing comic or channel character, no real person")
ACCEPT = ("Place side by side with `../model_sheets/MODEL_SHEETS_XKCD_WHATIF.md` §1–2 and the approved anchor image: (1) line weight 7–9 px when the "
          "figure is scaled to a 1080 px frame at the measured narrator size (617 px tall); (2) faceless head, single-line limbs; (3) only listed "
          "fills, no gradient; (4) edge/halo QA: composite over #F8F8F8 and over #0C0C0C, inspect edges at 400%: no white or grey matte halo, no "
          "green fringe (if keyed), closed outlines; (5) no stray text or extra objects; (6) originality: does not look like the source channel's "
          "own characters, mascot or cards.")
ROOT = "~/YIOS-local-audits/xkcd-whatif/asset_library/_clone_assets"
A = [  # asset_id, name, category, purpose, refs, locks, items, framing, prompt_body, extra
 ("CHR-001", "NIB narrator anchor sheet", "characters", "Identity anchor for every later character prompt; attach the approved PNG to all later requests.",
  "xk_long_typography tiles 2/11/14/20 (lecture frames s3oLIDaElaE G0001, 2LSyizrk8-0 G0003, p2M8Y0z9Rl0 G0001, IdlQsjq5vKo G0004); figure_measure_check.jpg (18 long openings)",
  [STYLE, NIB], "front view standing neutral, 3/4 view standing neutral (only these two; no back view needed)", "two figures side by side, full body, 16:9 canvas, figures 60% of frame height",
  "Character model sheet of an ORIGINAL narrator. Draw NIB twice side by side: (a) front view, standing, arms relaxed slightly away from the body; (b) three-quarter view facing right, same pose. Keep proportions identical in both: head diameter 0.37 of total height, torso 0.25, legs 0.38.", ""),
 ("CHR-002", "NIB pose strip A (lecture poses)", "characters", "Pose library for 1-frame POSE_SWAP and lecture openings.",
  "xk_long_characters 13 (JqFSGkFPipM G0007), 14 (lLlwvmu1ZeA G0062); characters_modifier_kit 5/10 (9VG0yqq_PHM G0009/G0008)",
  [STYLE, NIB], "1 holding a blank sheet of paper in front of the chest; 2 pointing to the right with a straight arm; 3 one hand at chin, thinking; 4 both arms raised; 5 shrugging", "five poses in one row, equal scale, feet on one invisible baseline",
  "Pose strip of NIB (attach anchor CHR-001). Five poses in one horizontal row, same size, same proportions as the anchor: holding a blank paper sheet, pointing right, hand on chin, both arms raised, shrugging.", "One pose strip per request."),
 ("CHR-003", "NIB pose strip B (action poses)", "characters", "Action and situation poses.",
  "xk_long_characters 21 (oTzW-mTQd5w G0058 climber), 17 (JcXpCyPc2Xw G0012); xk_short_characters 3/18/21 (desk + chair)",
  [STYLE, NIB], "1 walking; 2 running; 3 sitting on an office chair typing at a desk (desk drawn separately, chair included); 4 falling backwards; 5 climbing a rope", "five poses in one row, equal scale",
  "Pose strip of NIB (attach anchor CHR-001). Five poses in one row, identical proportions: walking, running, seated on an office chair with both arms forward as if typing, falling backwards, climbing a vertical rope.", "One pose strip per request."),
 ("CHR-004", "Modifier kit (separate layers)", "characters", "Identity modifiers that sit on the base stick rig as separate layers (channel identity comes only from modifiers).",
  "characters_modifier_kit.jpg 2/8/11/12/13/17/21/24; xk_long_characters 10/22/24",
  [STYLE], "long ponytail, short bob hair, messy bun, frizzy shocked hair, knit beanie, wide-brim sun hat, construction hard hat, headphones, sunglasses", "nine items in a 3x3 grid, each centred on an empty unfilled circle head guide drawn in light grey #C4C4C4",
  "Nine separate hair and headwear pieces for a faceless circle-head stick figure, each drawn on its own light-grey guide circle so it can be cut out: long ponytail, short bob, messy bun, frizzy shocked hair with zigzag lines, knit beanie, wide-brim sun hat, hard hat, headphones, sunglasses. Black monoline, flat dark fill #1C1C1C for hair masses.", "≤9 objects per request."),
 ("CHR-005", "Supporting cast set", "characters", "Recurring generic cast: the question asker and crowd extras (original, not the source's named figures).",
  "xk_short_characters 3/18/21 (asker at desk); xk_long_characters 2 (crowd line-up p2M8Y0z9Rl0 G0050), 24",
  [STYLE], "ASKER (beanie + desk + computer, seated); 6 crowd extras each with one different modifier from CHR-004", "seven figures in one row on one baseline",
  "Seven faceless stick figures in one row, same proportions as NIB but without glasses or scarf: first one seated at a small desk with a boxy computer monitor and an office chair, wearing a knit beanie; then six standing extras, each with exactly one modifier: ponytail, bob hair, hard hat, sun hat, headphones, messy bun.", ""),
 ("CHR-006", "TARDI mascot sheet", "characters", "Original channel mascot for title/end cards and occasional gags (replaces the source's silhouette mascot).",
  "title_end_cards.jpg 3/5/7/8 (structure only: a mascot sits left on the end card)",
  [STYLE, TARDI], "front 3/4 view neutral; side view walking; sitting holding a tiny magnifying glass", "three views in one row",
  "Original mascot model sheet: TARDI in three views in one row: three-quarter front view standing, side view mid-step, sitting and holding a tiny magnifying glass. Same size and proportions in all three.", "Mascot may have dot eyes (animals carry more detail than people in this style)."),
 ("ENV-001", "Whiteboard and lecture set pieces", "environments", "The lecture-frame set: empty wall board that receives subject drawings, plus the question card box shape.",
  "xk_long_props 11/15/24 (board with ledge); xk_long_typography 2/11/14/20 (question box + board)",
  [STYLE], "1 empty wide wall whiteboard: thin black rectangle with a short marker ledge along the bottom right holding two tiny markers; 2 empty rounded rectangle card, flat light-grey #E4E4E4 fill, no outline", "two items side by side",
  "Two separate set pieces on one sheet: (1) an empty wide wall whiteboard drawn as a thin black monoline rectangle, aspect about 16:10, with a short ledge along the bottom edge on the right holding two tiny marker pens; (2) an empty rounded-rectangle card with flat light-grey fill and no outline, aspect about 3:1, for a question to be typeset on later.", "Card text is added later as an editable serif text layer, never generated."),
 ("ENV-002", "Space plate", "environments", "Dark background family (16% of clusters): black space with a grey planet limb.",
  "xk_long_environments 3/7 (qu8nx1qUwEU G0042/G0036), 1 (2LSyizrk8-0 G0024), 6 (starfield)",
  [STYLE.replace("people are faceless", "any people are faceless")], "single plate", "full-bleed 16:9 background plate, 1920x1080",
  "Full-bleed background plate: flat black #0C0C0C space with a few tiny white dots for stars; the curved limb of a planet across the bottom third, flat mid-grey #545454 land shapes on flat grey #343434, flat white irregular cloud blobs; thin white monoline outline on the limb. No glow, no gradient.", "Background plate: NOT transparent. Soft glows (sun, beams) are added later as separate blurred layers."),
 ("ENV-003", "Night and dusk plates", "environments", "Grey night scene and flat dusk colour field with black ground silhouette.",
  "xk_long_environments 12/13 (9VG0yqq_PHM G0120/G0132), 4 (BO8rOs05v48 G0098); xk_short_environments 5/21",
  [STYLE.replace("no gradients, ", "a smooth vertical gradient is allowed ONLY on the dusk sky, ")], "1 grey night plate; 2 dusk plate", "two full-bleed 16:9 plates, one per request",
  "Plate 1: full-bleed flat mid-grey #8C8C8C night scene, a black silhouette tree line along the bottom, a small flat ground strip, sparse light-grey snow specks. Plate 2: full-bleed dusk scene, smooth vertical colour field from #3C4C8C at top to #E0A060 near the horizon, flat black ground silhouette with a low hill along the bottom quarter.",
  "Exception to the no-gradient rule: dusk/night plates are the measured counterexample (style bible rule 4). One plate per request. Vignette added in compositing."),
 ("ENV-004", "Map plate style test", "environments", "Map family: grey ocean, pale cyan shelf, cream land, green vegetation.",
  "xk_long_environments 2/10/14/21/24 (WH4g1ptJ-70 maps); palette_full_bleed_scenes_chromatic.csv",
  [STYLE], "one invented continent shape (NOT a real-world map)", "full-bleed 16:9 plate",
  "Full-bleed map plate of an INVENTED island continent: flat grey ocean #C8C8C8, a pale cyan #BCECF4 shallow-shelf band hugging the coast, land in flat cream #ECECB4 with patches of flat green #6CBC6C, small hand-drawn chevron mountain marks, two dashed horizontal latitude lines across the whole plate, black monoline coastline.", "Place names are added later as editable hand-print text layers."),
 ("PRP-001", "Science props A", "props", "Detailed science objects (objects carry the detail).",
  "xk_long_props 18 (BnGqPxnQh9A G0086 rover), 17 (rocket), 23 (2LSyizrk8-0 G0130 telescope), 5 (satellites)",
  [STYLE], "space telescope, small satellite, six-wheeled planetary rover, tall rocket, radio dish, seismograph drum", "six objects in a 3x2 grid, same line weight",
  "Six separate ORIGINAL-design science objects in a 3x2 grid, each detailed with parts and light hatching, black monoline with flat grey fills: a space telescope tube with solar panels, a small boxy satellite with antennas, a six-wheeled rover with a robot arm, a tall multi-stage rocket, a radio dish on a stand, a seismograph drum with a pen arm.", "≤9 objects per request."),
 ("PRP-002", "Everyday props B", "props", "Household and city objects for absurd-scale gags.",
  "xk_long_props 2 (9VG0yqq_PHM G0040 fridge/microwave/toaster), 9 (car), 13 (ship), 16 (banana/pizza); xk_short_props 11 (building)",
  [STYLE], "toaster, fridge, microwave, small car, container ship, two-storey house, round tree, desk lamp, stack of books", "nine objects in a 3x3 grid",
  "Nine separate everyday objects in a 3x3 grid, black monoline with flat grey fills and moderate detail: a toaster, a tall fridge, a microwave oven, a small hatchback car, a long container ship with stacked containers, a two-storey house, a round deciduous tree, an angled desk lamp, a stack of three books.", "≤9 objects per request."),
 ("GFX-001", "Diagram kit", "graphics_ui", "Reusable diagram parts: rulers, axes, flowchart boxes, leader lines, cutaway style sample.",
  "xk_long_graphics_ui 3 (axes), 8 (cross-section), 13/20 (process chain), 14 (cutaway); xk_short_graphics_ui 8/9 (flowchart), 24 (vertical ruler)",
  [STYLE], "vertical ruler with ticks; empty chart axes (L shape); three outlined flowchart boxes with arrows; ground cross-section strip with stipple soil and black rock; circled-icon chain of four circles with arrows", "five items on one sheet, spaced apart",
  "Five separate diagram parts on one sheet: a tall vertical ruler with major and minor tick marks (no numbers); empty chart axes in an L shape with small arrowheads; three empty outlined boxes joined by arrows; a horizontal ground cross-section strip with dotted stipple soil on top and solid black rock below; four empty circles in a row joined by arrows.", "Numbers and labels are editable text layers, never generated."),
 ("GFX-002", "Red annotation marks", "graphics_ui", "The red marker system as stroke references (build final marks as vector paths for write-on).",
  "xk_long_graphics_ui 3 (red ellipse), 18 (red hatching); xk_short_graphics_ui 19 (red strike); xk_long_props 8 (ellipse around WIND)",
  ["red #D0404F monoline marker strokes, same weight as the ink line, slightly wobbly, round ends, no fill"], "ellipse loop, arrow, straight strike-through, zigzag scribble, underline, X mark, dashed limit line", "seven marks in a row on transparent",
  "Seven separate red hand-drawn annotation marks in a row: an open ellipse loop slightly overlapping at the join, a curved arrow, a straight strike-through line, a dense zigzag scribble, a slightly wavy underline, an X mark, a dashed straight line.", "Used as tracing references; final marks should be vector paths so they can write on at ~0.2 stroke/frame."),
 ("TYP-001", "Typography (no image generation)", "typography", "Font choices and text styles; all text is editable layers.",
  "xk_long_typography 2/11/14/20 (serif question card), 6/7/18 (caps headings), 15 (black timer banner); xk_short_props_typo_uncat 13/15 (Shorts sans card)",
  [], "hand-print caps (headings, labels, speech); serif (question card, footnotes); sans for Shorts question card; white caps on black banner", "n/a",
  "DO NOT generate text as images. Choose an ORIGINAL near font: a rounded monoline hand-print caps font for labels (do not use fonts made to imitate the source creator's handwriting), a book serif (Georgia / PT Serif class) for question cards and footnotes, a plain sans for the Shorts card. Render each word as its own layer.", "Owner already allowed a near font."),
 ("BRD-001", "Logo and channel name", "typography", "New brand: name, logo lockup, title card and end card (replaces source title/end cards).",
  "title_end_cards.jpg 3/5/7/8 (structure only: full-frame colour card, mascot left, content centre, credits right)",
  [STYLE, TARDI], "logo lockup: TARDI peeking over a hand-drawn rounded speech-box; title card plate; end card plate", "logo 1:1; cards 16:9",
  "Logo artwork only (lettering added later in the chosen font): TARDI the water bear peeking over the top edge of an empty hand-drawn rounded box, black monoline on a flat deep-teal #1F6F78 square. Second request: 16:9 end-card plate, flat deep-teal #1F6F78 full frame, TARDI drawn in white monoline at the left third, empty space in the centre for book/link tiles and on the right for a credits column.",
  "Brand colour is teal, not the source's full-frame red; red stays only as the annotation colour. Channel name: owner to choose (placeholders: 'Absurd Scale', 'Unlikely Physics', 'What Would Happen'); check trademark/availability before use."),
 ("SHT-001", "Shorts narrator variant", "characters", "9:16 layout: white-outline narrator on a black lower area under a map panel.",
  "xk_short_environments 6/13/17/22 (aMshLs0YCTQ white figure on black)",
  [STYLE.replace("black monoline ink", "WHITE monoline ink"), NIB.replace("black lines", "white lines")], "standing neutral; pointing up", "two poses in one row on solid black",
  "NIB drawn in WHITE monoline ink on a solid black #0C0C0C background (attach anchor CHR-001): standing neutral and pointing upward. Same proportions as the anchor; scarf fill mid-grey #848484.", "Background black is part of the asset here (no transparency needed)."),
]
idx = []
for aid, name, catg, purpose, refs, locks, items, framing, body, extra in A:
    path = f"{ROOT}/{catg}/{aid}/"; is_img = aid != "TYP-001"
    lock_txt = "\n".join(f"- {l}" for l in locks) if locks else "- n/a (fonts, not images)"
    prompt = (f"{body} Locks: " + " ".join(f"{l}." for l in locks)
              + (" " + ALPHA if is_img and catg not in ("environments",) and aid not in ("SHT-001",) else "") + f" Avoid: {NEG}.") if is_img else body
    md = f"""# {aid} — {name}
- **Category:** {catg}
- **Target storage path:** `{path}` (originals + approved PNGs; keep every generation, never overwrite)
- **Purpose:** {purpose}
- **Reference frames (opened in P2/P3, structure reference only, never copied):** {refs}
- **Locked descriptors (repeat verbatim in every request):**
{lock_txt}
- **Required poses / modifiers / items:** {items}
- **Framing:** {framing}
- **Rules:** character sheet and anchor first; one pose strip per request; at most ~9 objects per request; every later prompt repeats the same locks and attaches the same approved anchor image. {extra}

## ChatGPT image-generation prompt
```
{prompt}
```

## Negative prompt
```
{NEG if is_img else 'n/a'}
```

## Acceptance check
{ACCEPT if is_img else 'Render a test line of each font at 1080p next to the model-sheet references; check legibility at 320 px width; confirm the licence allows video use.'}

Status: PROMPT ONLY. Image generation needs owner approval and an owner-chosen image model. Labels: style locks are INFERRED from MEASURED/OBSERVED evidence in `../model_sheets/MODEL_SHEETS_XKCD_WHATIF.md`; character and brand designs are ORIGINAL proposals.
"""
    open(f"{OUT}/{aid}.md", "w").write(md)
    idx.append(dict(asset_id=aid, name=name, category=catg, target_path=path, file=f"PROMPT_PACK/{aid}.md", reference_frames=refs, image_generation=is_img, status="PROMPT_ONLY_NOT_GENERATED"))
with open(f"{OUT}/PROMPT_INDEX.csv", "w", newline="") as f: w = csv.DictWriter(f, list(idx[0])); w.writeheader(); w.writerows(idx)
open(f"{OUT}/README.md", "w").write(f"""# Prompt pack — original channel in the xkcd-style SYSTEM (P6, text only)
{len(idx)} asset families, index `PROMPT_INDEX.csv`. Order: CHR-001 anchor → CHR-002/003 pose strips → CHR-004/005 kit and cast → CHR-006 mascot → ENV → PRP → GFX → TYP (fonts) → BRD → SHT.
Originality: same style system (line, fills, faceless stick rig, red annotation, layouts, rhythm); NEW narrator (NIB: round glasses + two-tail scarf), NEW mascot (TARDI the water bear), NEW brand colour (teal #1F6F78) and name. The source channel's lecture-frame drawing, mascot silhouette, red title/end cards, book covers, credits and names are not to be copied. No real person's likeness.
Text is never generated inside images: all words are editable layers (HumanCraft guide p.12, 13).
Plain colour plates (off-white #F8F8F8 canvas, black #0C0C0C) need no image model: make them as flat fills.
Nothing here has been generated. Generation needs owner approval.
""")
print(len(idx), "files")
