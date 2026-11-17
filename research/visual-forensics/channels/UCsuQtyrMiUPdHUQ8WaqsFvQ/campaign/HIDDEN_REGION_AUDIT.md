# Hidden-region audit v2 (checkpoint J, primary reviewer, session 85559743)
Read the checkpoint K addendum at the end first. It retracts one J limit line and widens what was opened. The J text below is kept as written.
Supersedes nothing: frames/sheets, sheet_index.csv and campaign/band_review stay as they were. Script pe_sheets.py painted a 22 px label over each tile (bottom 8.1% landscape, 4.6% portrait) and a 3 px border around it.

## Which finding classes could be affected
| Class | Risk from hidden region | Result |
|---|---|---|
| On-screen text | HIGH: last lines of lists can sit low | 1 hit, RmTdnXHbI8s G0008/G0009 "pervy neighbour" |
| Captions | HIGH if burned in low | none found |
| CTA / subscribe prompts | HIGH: usually low in frame | none found |
| End cards | MEDIUM: last frames | none found; last-frame tiles are included |
| Object details | MEDIUM: feet, hands, hems, props | present and consistent with existing descriptions; no new event |
| Boundaries (element entry at frame edge) | LOW: 3 px border hides first edge pixels | 3 ring-only tiles; 1 correction, xBJ6suQSt98 G0092 onset one frame earlier |

## Method
- scripts/pe_sheets_v2.py: same tiles as sheet_index.csv, label above image, gutter outside it, 100% of frame visible. Output frames/sheets_v2 for all 15 videos and RT_P1 attempt 6 (local JPGs, not published). pe_sheets.py unchanged.
- scripts/pe_hidden_audit.py: every distinct sheet tile frame, HOLD end, D4 first/mid/last and ACTIVITY, from native frames. Status per tile in campaign/hidden_audit/hidden_tiles.csv.
- Opened once by primary: STRIP_01-05 (91 new bands + 11 portrait lower 23% slices that band_review had cropped away), FAINT_01 (10 flagged after a second pass for faint marks and light content on dark bands), ring-only tiles at native frame.

## Per-video coverage
| Video | Tiles | ACTIVITY tiles | Empty | Reviewed earlier (v1) | Opened now | Numeric dup, not opened | Faint opened | Ring-only | Corrections |
|---|---|---|---|---|---|---|---|---|---|
| 3AsDdMQr_nQ | 96 | 50 | 74 | 11 | 6 | 5 | 0 | 0 | none |
| 5gSIU30yiVs | 33 | 14 | 33 | 0 | 0 | 0 | 0 | 0 | none |
| 6YHva7Me2ls | 211 | 111 | 181 | 15 | 2 | 13 | 3 | 0 | none |
| C_jSOXP_XWY | 15 | 7 | 15 | 0 | 0 | 0 | 0 | 0 | none |
| DekaeZPzTAQ | 256 | 133 | 217 | 18 | 8 | 13 | 3 | 0 | none |
| IUur04eOd4A | 73 | 41 | 60 | 4 | 7 | 2 | 0 | 0 | none |
| KyBWJPaF1KI | 349 | 192 | 329 | 9 | 8 | 3 | 2 | 2 | none |
| Nv4xJ_NsFdo | 93 | 46 | 84 | 5 | 3 | 1 | 0 | 0 | none |
| RM_KBLDLsnQ | 213 | 130 | 133 | 36 | 15 | 29 | 0 | 0 | none |
| RmTdnXHbI8s | 202 | 104 | 142 | 29 | 15 | 16 | 0 | 0 | G0008, G0009 text: "pervy neighbour" added |
| W8AVd7RhTME | 51 | 24 | 49 | 1 | 1 | 0 | 0 | 0 | none |
| f1vIzsTFrp4 | 32 | 18 | 25 | 1 | 2 | 4 | 0 | 0 | none |
| qB_EKkMyuUE | 210 | 107 | 170 | 18 | 15 | 7 | 1 | 0 | none |
| uIG2U_1xynQ | 92 | 48 | 90 | 1 | 1 | 0 | 1 | 0 | none |
| xBJ6suQSt98 | 176 | 92 | 140 | 18 | 8 | 10 | 0 | 1 | G0092 onset f2520 -> f2519 |
| TOTAL | 2102 | 1117 | 1742 | 166 | 91 | 103 | 10 | 3 | 2 videos |

## Limits
- Band review is OBSERVED at strip scale (960 px wide). Handwriting smaller than that could be missed, though none is suspected.
- DUP tiles (103) matched an already reviewed band of the same video within mean abs diff 4 on a 240x24 thumbnail. Not opened.
- EMPTY tiles (1742) were checked numerically only. 10 were opened after the second pass; 1732 have no pixels under the thresholds.
- Original reviewers did not re-review these frames, so their semantic readings were not repeated. Corrections go through review/primary_corrections.csv with raw annotations intact.
- Frames that were never tiles are outside this audit. Partially viewed activities are handled separately in campaign/gap_review.

## Checkpoint K addendum (acceptance reconciliation)
Script scripts/pe_hidden_recount.py re-decoded every tile from the source; results in campaign/hidden_audit/recount_tiles.csv and recount_summary.json. RECOUNT_01-07.jpg (local) opened once by the primary.

### Retraction
J line "1732 have no pixels under the thresholds" was wrong. 13 tiles flagged by the faint pass were dropped by its de-duplication and never opened, and 60 EMPTY tiles in total held a connected mark of at least 12 px that no pass opened, up to 26,315 px. J also said DUP tiles matched a reviewed band; mean difference under 4 on a 240x24 thumbnail did hold, but the largest local 8x8 block difference reached 143.42 of 255, so local content could differ.

### Categories
Status is exclusive and sums to the total: EMPTY 1742 + COVERED_V1 166 + TO_REVIEW 91 + DUP 103 = 2102.
These overlap the status and are not added: faint-pass 10 (all inside EMPTY), portrait lower-slice 11 (inside COVERED_V1), ring-only 3 (inside EMPTY).
EMPTY by reason: 1693 under 0.2% content, 49 over 95% content (full dark or full ink).

### Thresholds and provenance
Band metric from pe_band_audit: gray under 90 or saturation over 80; EMPTY outside 0.002 to 0.95. Faint pass: over 0.2% pixels gray under 235 on bright bands, gray over 150 on dark bands. Recount mark: connected group of at least 12 px differing by at least 60 from the band median. These are analyst-chosen values, not calibrated on labelled text. KyBWJPaF1KI f4038 shows the weakness: tops of lettering on parchment sat under the first threshold.

### Coverage after K
| State | Tiles |
|---|---|
| Opened by a reviewer (model): v1 166, J 91 + faint 10, K DUP 103 + residual 60 | 430 |
| Numeric only, no mark of 12 px or more | 1672 (1667 no connected mark at all, 5 with a mark under 12 px) |
| Total tile frames | 2102 of 66995 decoded frames; last frame is a tile in 15/15 videos |

| Video | Tiles | DUP opened at K | Residual opened at K | Numeric only |
|---|---|---|---|---|
| 3AsDdMQr_nQ | 96 | 5 | 0 | 74 |
| 5gSIU30yiVs | 33 | 0 | 0 | 33 |
| 6YHva7Me2ls | 211 | 13 | 11 | 167 |
| C_jSOXP_XWY | 15 | 0 | 0 | 15 |
| DekaeZPzTAQ | 256 | 13 | 5 | 209 |
| IUur04eOd4A | 73 | 2 | 0 | 60 |
| KyBWJPaF1KI | 349 | 3 | 16 | 311 |
| Nv4xJ_NsFdo | 93 | 1 | 0 | 84 |
| RM_KBLDLsnQ | 213 | 29 | 5 | 128 |
| RmTdnXHbI8s | 202 | 16 | 2 | 140 |
| W8AVd7RhTME | 51 | 0 | 0 | 49 |
| f1vIzsTFrp4 | 32 | 4 | 0 | 25 |
| qB_EKkMyuUE | 210 | 7 | 13 | 156 |
| uIG2U_1xynQ | 92 | 0 | 4 | 85 |
| xBJ6suQSt98 | 176 | 10 | 4 | 136 |

### Result, scoped
In the hidden regions reviewed, no CTA, caption or end card was found. This is not a universal claim about the videos: frames that were never tiles are not in this audit, and 1672 tiles were checked numerically only. Hold interiors are measured static against their tile; ACTIVITY in-betweens were viewed in strips at small scale. Text smaller or fainter than the thresholds could still be missed.
K opened bands show cut-off hands, feet, hems, tree parts, background textures and photos. Native checks: 6YHva7Me2ls f997 marks are grass tufts, qB_EKkMyuUE f5561 blue is the puddle under the frozen caveman, xBJ6suQSt98 f4623 is the red X tip.
Correction: KyBWJPaF1KI G0120 said the second poster line was partly clipped. Native f4038 shows "SCREAM IF FOUND" whole; the clip came from the sheet label. Traced in review/primary_corrections.csv. Original annotations unchanged. Finding classes affected: on-screen text 2 hits in total (RmTdnXHbI8s G0008/G0009, this one).
