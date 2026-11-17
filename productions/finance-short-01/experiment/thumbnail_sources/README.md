# Original thumbnail sources

Two vector compositions were authored locally for this experiment and exported through the bundled Sharp renderer. No paid generation, raster image model, competitor artwork, stock image or logo was used. `render.mjs` contains the exact geometry and typography; the SVGs are independently editable source files, not raster images embedded in vector wrappers.

## Files and reproduction

- `thumbnail_A.svg`: conditional-offer hero, recommended.
- `thumbnail_B.svg`: backward-clock alternative.
- `render.mjs`: original authoring geometry and PNG export commands.
- `runtime.json`: verified local runtime/package locations.
- `mobile_review.png`: both designs at 320 and 160 pixels wide.
- `thumbnail_A_crop_4x5.png` and `thumbnail_B_crop_4x5.png`: central 4:5 crop inspection.
- Parent-directory `thumbnail_A.png` and `thumbnail_B.png`: final 2160×3840 PNG exports.

Run from the experiment directory using the Node path in `runtime.json`:

```sh
/Users/ghilmanislam360/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node thumbnail_sources/render.mjs
```

This redraws only these two thumbnail concepts and their QA previews. It does not create a motion composition or a full asset library. Text remains live SVG text; export used the fonts available locally. Recheck line widths if moving the sources to a machine with different fonts. PNGs preserve the reviewed rendering.

## Art direction

Original shopper Remy has a warm-brown angular face, plum curls, solid teal torso and solid articulated hands. The character investigates the offer instead of impersonating a real person or a competitor host. The illustration is intentionally a waist-up cutout. Palette roles are shared between A and B; no brand identity is implied.

A shows the contractual condition in full: “IF PAID IN FULL.” Its “NO INTEREST?” headline is a question, not a real product advertisement. B shows “BACK TO DAY ONE” with an interest receipt and counterclockwise arrow. The receipt is schematic: strokes represent entries without numerical values, dates or a fake bill total.

## Visual review

Both designs were inspected in a contact sheet at 320px and 160px width. The main headline, IF/clock silhouette and shopper remain distinguishable. A's smaller “PAID IN FULL” text is subordinate at 160px; the oversized IF carries the condition. B's interest label is smaller, so its exact subject depends more on the accompanying title. No measured two-second comprehension test or viewer preference study was performed.

The central 4:5 crops retain the full headline and principal relationship. This is a geometry check, not proof of every YouTube surface's crop. The actual owner-account workflow still requires verification before publication. The full 9:16 compositions can be reused as meaningful video frames after the owner approves the script and provides the MP3.

Named groups include `headline`, `remy-shopper`, `head`, `torso`, `arm-point`, `arm-rest`, and the concept-specific offer/clock/receipt. These groups establish editable hero artwork; they are not a finished animation rig. Approval of these stills does not certify animated acting or Casually Finance quality parity.
