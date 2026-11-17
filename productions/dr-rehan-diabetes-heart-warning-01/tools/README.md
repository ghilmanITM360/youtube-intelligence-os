# Static build / delivery tools

`build_assets.py S01` (through S08, sequentially) writes original vector assets for that scene and updates manifests/storyboards. It is an illustration-authoring file, not an animation SDK. Editing SVG directly is supported; do not rerun its scene builder afterwards unless you also reconcile the authoring source, because the generator is authoritative for regeneration.

`export.mjs` renders authored SVGs through Sharp. Existing PNGs are delivered; no generation service is required. Dependency: Sharp 0.34.x-compatible API, Node 22+; Python 3.9+ and Pillow 11.x for review/validation. Runtime used in this session is recorded in BUILD_ENVIRONMENT.json. The environment's Arial font was used; install an appropriately licensed Arial or choose/review a substitute on another machine. No font file is redistributed.

From the production directory:

```sh
python3 tools/build_assets.py S01
SHARP_MODULE=/absolute/path/to/node_modules/sharp node tools/export.mjs
python3 tools/review.py S01
python3 tools/finalize.py
python3 tools/validate.py
```

Repeat only the scene being corrected. `review.py` refreshes its review sheet and the full contact sheet; `finalize.py` updates derived metadata/part register/content hashes, not artwork. SOURCE_MANIFEST.json excludes itself by definition. Run finalization after any deliverable edit. Native sources and delivered exports are portable even without these optional regeneration dependencies. No new dependencies were installed in the repository.
