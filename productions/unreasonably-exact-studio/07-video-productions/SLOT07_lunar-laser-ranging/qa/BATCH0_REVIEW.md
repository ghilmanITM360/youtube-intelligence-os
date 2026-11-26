# Batch 0 review (RETRO_002_CUBE_ARRAY calibration): Claude, 2026-11-26

Reviewed: the actual files in `codex_handoff/deliveries/batch0/`. SHA-256 list verified (all 10 files OK). Opened the contact sheet and looked at the image. The 4096 files and the macro were not viewed individually at full size (only validator numbers and the contact sheet).

## What Codex delivered
- One generated composite, **1254x1254 native** RGBA with real transparency (alpha 0-255), two exports resampled to 4096x4096 (front, and a 3x3 crop). No separated frame/faces layers.
- Self-reported **BLOCKED** (honest): A1 native canvas, A3 RGB under zero alpha (3 px native, 6,566 resampled), A6 panel touches the bottom edge, A8 native size below request, B1-B3/B9 not performable without layers.

## What I see (observed)
A clean 10 x 10 grid, 100 round recesses in a brushed-silver panel, dark blue-grey glass with a three-facet Y in each face, consistent upper-left light, no text, no baked rays. Count by eye: 10 rows of 10. It reads well at phone size.
Problems: every face is a pixel-identical-looking sprite with a sphere highlight (looks stamped; the Mercedes-like Y is very prominent); panel too perfect/polished against the matte Apollo photographs; bottom edge cropped; orthographic front is an inferred view (no photo is a true front view).

## Codex research quality (checked against its notes)
Thin: it viewed thumbnails only, did not open the three SVG references, downloaded nothing new, asked no extra perspective questions. It was honest about this. Batch 0b requires deeper research (full-size crops, at least three new saved references with licence).

## Calibration findings that change the pipeline (decisions)
1. **The generator's native size is about 1254 px.** Briefs that demand 3000-4096 px canvases cannot be met natively. Decision: asks are rewritten for native generation (<= ~1500 px per image); larger exports are labelled `resampled` and Claude upscales only where blur is acceptable. Textures that need 4096x2048 (Earth, Moon globe) will start from public-domain NASA maps (SVS / Blue Marble class, licence verified) with Codex or Claude repainting only what is wrong (poles, cloud layer), instead of asking an image generator for a 4096 map.
2. **Do not ask a generator for 100 identical objects.** Decision: Codex delivers (a) an empty frame plate with 100 recesses (b) a single face-disc sprite plus 3 slight variants; Claude instances the discs in code on the exact grid. This gives exact count, exact registration (B9) and reusable faces for the cutaway match.
3. **One generation = one composite.** Layer decomposition is requested as separate focused generations (plate without objects, sprite alone), not as "give me layers".
4. Alpha: the generator gives genuine transparency but with a few RGB-under-zero-alpha pixels; Claude cleans these (logged "repaired by Claude" with hashes).

Status of the asset: `blocked` (Codex's own), art `candidate/reference_only`. Not integrated. Next: Batch 0b with the revised brief.
