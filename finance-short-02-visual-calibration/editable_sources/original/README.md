# Original artwork sources

Four static review SVGs and their top-level PNG exports; independent host variants, four finance props, arrow/highlight and the expense-income element are editable SVG paths/text with transparent PNG companions. Individual face, eyes, mouth, arms and held-paper groups are separable. This is artwork, not a rig or animation library.

Two built-in imagegen concepts are retained as HOST_CONCEPT_v1/v2.png. V1 was too shaded and mascot-like; one imagegen correction reduced body detail but retained unwanted shading. Final review art is an original flat SVG redraw of that original character concept, with new hand-authored geometry. No competitor illustration was traced or embedded in original assets. SVG faces and props have actual editable paths, not a raster-only wrapper.

`draw_calibration.py` authors this small static SVG set; `render_previews.cjs` rasterizes it using preinstalled Sharp. No frame seeking, animation interpolation, video or keyframe code. Independent PNG layer exports preserve alpha. Do not treat the complete asset plan as already produced.

Rebuild static previews from canonical checkout:

```sh
/Users/ghilmankhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 finance-short-02-visual-calibration/editable_sources/original/draw_calibration.py
NODE_PATH=/Users/ghilmankhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules /Users/ghilmankhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node finance-short-02-visual-calibration/editable_sources/original/render_previews.cjs
```

These runtime paths are Laptop B-specific. On another PC use existing Python3, Node and Sharp; no install was performed here. SVG geometry and source pixels are portable, but Chalkboard is macOS-dependent: choose an available approved replacement and review typography. PNG previews are fixed review output. The government crop stays under references; HERO_03.svg embeds its untouched pixels for portable rendering with an independent highlight group. Keep the package local because reference/QA files contain third-party material.

Approved script is preserved verbatim in APPROVED_NARRATION.txt. All CSV time ranges are provisional; no MP3 is needed for this phase. Stop before any bulk illustrations or animation until visual direction is approved.


## V2 current sources

Current HERO/host/prop SVGs revised from original V1 source, preserving host identity; old files in editable_sources/prior_v1. draw_calibration.py exports static art and assigns editor IDs; render_previews.cjs exports PNG; render_v2_review.cjs builds current owner-reference comparison and mobile QA. Existing render_qa.cjs and historical QA files belong to V1. LAYER_REGISTER.csv contains actual top-level layers, normalized anchors/paint order/contact notes. Remaining storyboard assets are plans. Source evidence is separate under ARTICLE_EVIDENCE; crops are embedded unchanged for portable SVG previews, not manually reconstructed text. Current original hero source can be edited without competitor artwork.
