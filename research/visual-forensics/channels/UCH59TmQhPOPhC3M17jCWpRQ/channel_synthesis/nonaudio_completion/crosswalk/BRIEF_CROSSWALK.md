# Asset crosswalk reviewer brief (Barely Evolved, 3 videos)
Inputs (read only these):
- sheets_local_only/*.jpg — one labelled native thumbnail per state (label = state id + frame). SHEET_INDEX.json maps sheets to states.
- ../../final_audit/CROSS_VIDEO_ASSET_ALIASES.csv (existing families XV-01..04; keep these IDs).
- ../../../2026-11-02-uPQcyookL0Y-deep-ct-scan/tables/o_asset_family_crosswalk_ext.csv (v1 families, keep original family IDs as aliases).
Task: build an inventory of RECURRING visual assets (characters, props, backgrounds/sets, graphic devices) that appear in 2+ states (within one video or across videos).
Rules:
- Only what you can see in the thumbnails. One canonical ID per asset: BE-CHR-###, BE-PRP-###, BE-BKG-###, BE-GFX-###.
- relation per member state: SAME (identical design), VARIANT (same design, changed pose/outfit/scale/colour — describe), UNCERTAIN (cannot tell at thumbnail size — say why). Never merge merely similar assets; if two designs differ in a defining feature (e.g. glasses, hair, outfit, body construction), make separate IDs and list them in a 'distinct_from' column.
- Cite the exact state ids. Do not guess story roles beyond what is drawn.
Output (write to this folder):
1. ASSET_CROSSWALK_v1.csv columns: canonical_id,kind,description,video,state,frame,relation,variant_note,original_alias_ids,distinct_from,confidence
2. ASSET_CROSSWALK_v1_notes.md: under 300 words: counts, uncertain cases, limits (thumbnail 384x216).
Write nothing else; modify no other file. Report under 150 words.
