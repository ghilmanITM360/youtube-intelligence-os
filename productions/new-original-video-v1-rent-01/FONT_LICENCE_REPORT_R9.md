# Font licence report, R9 (2026-11-21)
Every font in the render path (single loader `font()` in tools/v1r4_render.py) is SIL Open Font License 1.1. Checked from the actual files: embedded name-table licence strings (name IDs 13 and 14) and licence texts kept beside the files.
| Use | File (v1r4_assets/fonts_ofl/) | Licence evidence | SHA-256 |
|---|---|---|---|
| Labels ("hand") | patrickhand_PatrickHand-Regular.ttf | name table: OFL 1.1, http://scripts.sil.org/OFL; Copyright 2012 Patrick Wagesreiter; patrickhand_OFL.txt | 0f173b3e...ad0fc |
| Display words and, in R9, numerals | caveatbrush_CaveatBrush-Regular.ttf | name table OFL 1.1; Copyright 2015 Google Inc.; caveatbrush_OFL.txt | e565bd7b...f6f282 |
| Source tags (R9; was Apple Helvetica) | atkinsonhyperlegible_AtkinsonHyperlegible-Regular.ttf | name table OFL 1.1; Copyright 2020 Braille Institute of America; atkinsonhyperlegible_OFL.txt; fetched from github.com/google/fonts ofl/atkinsonhyperlegible | 7fb917c8...97669 |
| Not used | kalam_Kalam-Bold.ttf (tested only); Apple Marker Felt, Chalkboard SE, Helvetica (removed from R9 path; R7/R8 baselines used Helvetica for tags) | - | - |
Full hashes: `v1r4_assets/fonts_ofl/SHA256.txt` (verified with `shasum -a 256 -c`). OFL permits embedding in video; keep the licence texts with the project; fonts are not sold alone. Characters used outside the Latin text (arrow, not-equal) are drawn or covered by these fonts; the one missing-glyph case found (arrow in Caveat Brush) was replaced by a drawn arrow. Practical check, not legal advice.
