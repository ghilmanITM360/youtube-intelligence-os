# v4 feature screen — protocol (written before any screen output; LOCAL ONLY)
Purpose: locate feature-present clips for the two UNTESTED v3 changes (MAP_FILL C2; merged multi-move camera instance M1) in the 11 remaining unused local Shorts, by measurement + a quick look, not by title.
**Exposure disclosure:** this screen opens frames of all 11 Shorts. After it, none of them is a blind held-out for any *other* rule; they are usable only for the feature-specific tests frozen afterwards (FROZEN_RULES_v4_feature.md).
Screen (tool `tooling/asset_library/xkcd/v4_screen.py`, 4 fps sampling at 1/4 scale):
- SAT: fraction of pixels with HSV S >= 0.35 and V >= 0.30 per sample; candidate MAP window = run of samples with SAT >= 0.15.
- SHIFT: phase-correlation translation between consecutive samples (response >= 0.3, |shift| >= 2 px at 1/4 scale); candidate SCROLL = >= 2 such shifts within 3.0 s with no hard cut (mean abs diff spike) between them.
- Then one contact image per candidate window is viewed and labelled MAP_FILL / TINT / GREY / OTHER and STRIP_SCROLL / SINGLE_PAN / OTHER.
Excluded from positive evidence regardless: grey maps, single moves, Shorts whose parent long is in a used set (parent check by census title + caption overlap where available).
