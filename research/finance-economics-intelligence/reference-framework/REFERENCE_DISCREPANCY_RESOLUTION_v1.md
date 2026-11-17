# Reference-corpus discrepancy resolution (2026-11-02)

## 30 versus 33 rules
Not a conflict. `ref_rule` holds **33 records: 30 analytical rules + 3 classified `NOT_APPLICABLE`** (FR-NA-01 cinematic energy/texture, FR-NA-02 image/video prompting, FR-NA-03 numeric scoring/hero-journey/named-director overlays). Of the 30 analytical rules by class: **27 CREATIVE_HEURISTIC, 2 DUPLICATED_OR_SUPERSEDED (FR-16C-03, FR-16C-04), 1 EMPIRICAL_HYPOTHESIS (FR-16C-06)**. Earlier text saying "30 rules" counted the analytical ones; "33" counts all records. Counts are unchanged; the report wording now names both.

## 62 versus 63 compilation entries (algorithm compilation)
Checked against the verified ZIP (SHA-256 d2114224…15d), all four renditions.
- **TXT/MD/DOCX contain 63 title-marked videos, not 62.** The v1 constituent index had 62 because entry #62 (lines 41865-42475) swallowed a second video that starts at line 42108 with its own title marker: *How to survive being a small YouTube channel (the TRUTH about growth)*. The DOCX also contains this title once.
- **The XLSX has 63 numbered rows** (sno 1-63 plus one trailing blank row; the earlier "65 rows" counted header and the blank). Row 63 is that same video.
- **Duplicates are real and kept, not collapsed:** XLSX rows 26/38 (identical title, 21,422 vs 21,418 characters) and 51/52 (7,501 vs 7,500 characters, same title); the TXT also repeats 26/38. Three "How to Upload YouTube Shorts Like a PRO" rows (10, 12, 13) have different lengths and are different transcripts.
- **Eight TXT entries (16, 20, 22, 23, 26, 41, 45, 46) have no `Title:` line** (v1 index title empty); titles were filled from the XLSX row of the same number and marked `XLSX_ROW_SAME_NUMBER_(TXT_TITLE_LINE_ABSENT)` in `ALGO_UPDATE_CONSTITUENT_INDEX_v2.json`.
- **Unresolved:** XLSX rows 47-51 align one position later than the TXT segmentation by body-text overlap (row 47 is titled "YouTube Just Made It 10X Easier..." but its text best matches the TXT segment titled "What YouTube Actually Wants in 2026", which has no XLSX title). Which rendition mislabels is not determined; both are preserved, and the XLSX is treated as an overlapping alias, not an independent source.
- **Decision:** the constituent count is **63 title-marked segments (v2 index), of which at least two pairs are duplicates (26/38 and, in the XLSX, 51/52)**. The compilation remains one source, not four. Nothing unique to the XLSX was discarded.

`ref_constituent_video` now has 63 rows; the test asserts 63.

## Extraction gaps (PDF glyphs, images, blank page)
Method: all PDF members except the identical-text alias `Hook (1).pdf` were rendered (130 dpi, 269 pages) and read with the macOS Vision text-recognition framework (compiled Swift helper, scratch only; no network; Tesseract is not needed). Each OCR page was compared word-for-word with the stored text-layer section (`REFERENCE_OCR_CROSSCHECK_v1.csv`, one row per page).
- **Dropped f/fi/ligature glyphs: not confirmed as material.** 269 of 269 pages matched a stored section; words of four letters or more that OCR found but the text layer lacks are 0.0-0.5% per member. Only one page tripped the 8% screen: `Hook guide.pdf` p.20, where the "missing" words are the random characters of a pasted `.mp4` file ID, not content. The earlier "glyphs dropped" worry therefore applies to no stored body text that can be identified by this test; a residual of isolated OCR-versus-layer differences remains in the CSV for any rule that cites a page.
- **`YouTube Title Analyzer` p.6 is genuinely blank** (render is white, OCR empty), not an extraction failure.
- **DOCX/MD images are not substantive.** The compilation DOCX has four images (70, 2,395, 2,898 and 3,690 bytes; OCR returns no text) and the MD has eight 16x16 base64 icons (264-340 characters). The other three DOCX members contain no images. The `PROCESSED_WITH_UNREAD_IMAGES` disposition is therefore resolved as "images inspected: decorative".
- **Still not done:** rule-level extraction from the Hook guide body, Renae, VIDEO EDITING, VEO 3, Nano-Banana, the 117-page algorithm guide, `new YT algorithms updates` and the constituent videos. The corpus is extracted and locator-addressed, not fully interpreted.
