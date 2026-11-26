# Codex: start here (Slot 07 "Lunar Laser Ranging", from Claude, 2026-11-26)

You are making **illustrated assets and textures** for a 94-second vertical science short about timing a laser pulse to the Moon and back. Claude draws every graphic, rig and animation in code. You draw the *real objects* so that they can be moved apart and animated. This folder is everything you need.

## Read in this order (about 15 minutes)
1. `PRODUCTION_ART_DIRECTION.md`: the look, the one sun direction, the palette, what you never draw.
2. `ASSET_ACCEPTANCE_TESTS.md`: how your work will be judged; run the automated ones yourself first (`tools/validate_asset.py`).
3. `RIGGING_REQUIREMENTS.md`: what must move, which layers must exist, overlap and pivot rules.
4. `SCIENTIFIC_ACCURACY_REQUIREMENTS.md`: facts your art must respect and things it must never imply.
5. `CHARACTER_CONSISTENCY_GUIDE.md`: the astronaut (only needed for Batch 5).
6. `MASTER_ASSET_PROMPT_BIBLE.md`: how prompts are structured plus the master prompt per family.
7. Your batch: `individual_asset_briefs/<ASSET_ID>.md` (one per asset; 16 required sections each, with **local reference image paths**; `ASSEMBLY_DIAGRAMS.md` shows how compound assets fit together).
8. `MASTER_ASSET_MANIFEST.csv`: every asset, parent, canvas, dependencies, status.
9. `CODEX_HANDOFF.md`: ownership, batches, evidence you must save.

## Read the two master guides (required)
`guides/UNREASONABLY_EXACT_MASTER_ANIMATION_PRODUCTION_PLAYBOOK.md` (sections 7-8: the asset request, validation, naming, manifests, handoff protocol) and `guides/HumanCraft_MASTER_Animation_Director_V4.md` (part I sections 2-6 and part II section 6: asset-first production, layers, clean plates, overscan, the decisive 2.5D test). Where a guide marks a standard PROPOSED or UNVERIFIED, treat it as a proposal to test (for example the alpha >= 245 threshold: report what your generator actually produces).

## What you must do before drawing anything
For each asset family you are about to start: open the saved images in `references/<family>/`, then **do your own research** (web, photographs, animation examples) to verify Claude's notes, find missing perspectives, and record disagreements. Save anything you add in `references_codex/<family>/` with its URL and licence. Write what you found in `deliveries/<batch>/RESEARCH_NOTES.md`. Do not rely on Claude's prompts blindly: Claude's research is a starting direction, not a ruling.

## Calibration lessons from Batch 0 (read before sizing anything)
- Your generator's native size is about 1254 px. Where a brief says 3000-4096 px, deliver at NATIVE size, state it, and label any larger export `resampled`. Claude upscales or rebuilds large maps from public-domain sources.
- Do not ask the generator for many identical objects or for "layers". Generate the plate without the objects and ONE sprite of the object separately; Claude instances and assembles in code.
- Keep research deep: open references at full size and crop to detail, open every reference you cite (including SVGs), save at least a few new lawful references per batch with source URL and licence.

## Rules that matter most
- Work **one batch at a time**, in the order in `CODEX_HANDOFF.md`. Stop at the end of each batch for review.
- Deliver only into `deliveries/<batch>/`. Never edit anything else, never overwrite an earlier delivery.
- Every layer of one pose or view: **same canvas, same pixel positions** as the master.
- No text, numerals, arrows, rays, beams, flares, dials, or diagrams in any art.
- Label honestly: `candidate` until Claude's tests pass; `blocked` when your own QA fails; never `approved`.
- Record a line in `CODEX_PROGRESS.csv` after every asset (`asset_id,batch,state,files,date,notes`). That file is yours alone.
- If an instruction is wrong or impossible (e.g. the reference contradicts the brief), say so in `ARTWORK_QA.md` rather than guessing.

## Folder map
```
codex_handoff/
  START_HERE.md                      <- you are here
  PRODUCTION_ART_DIRECTION.md  ASSET_ACCEPTANCE_TESTS.md  RIGGING_REQUIREMENTS.md
  SCIENTIFIC_ACCURACY_REQUIREMENTS.md  CHARACTER_CONSISTENCY_GUIDE.md  MASTER_ASSET_PROMPT_BIBLE.md
  MASTER_ASSET_MANIFEST.csv
  references/<family>/               <- Claude's saved reference images (+ REFERENCE_INDEX.md per family)
  individual_asset_briefs/           <- one brief per asset
  tools/validate_asset.py            <- alpha/canvas/component checks (numpy, Pillow, scipy)
  deliveries/<batch>/                <- yours (create it)
  references_codex/<family>/         <- yours (create it)
  CODEX_PROGRESS.csv                 <- yours
```

## Context in one paragraph
The narration (92.5 s) says: a laser pulse leaves a telescope, crosses to a reflector on the Moon left by Apollo astronauts, returns in about 2.56 s, almost no light comes back, a few photons per pulse are counted over many pulses, and distance = (round-trip time x speed of light) / 2. The animatic that uses your assets is `ANIMATIC_V1_REFERENCE_INFORMED.mp4`, and the illustrated placement boards are in `placement_boards/`. Look at both to see where each asset appears and how big.
