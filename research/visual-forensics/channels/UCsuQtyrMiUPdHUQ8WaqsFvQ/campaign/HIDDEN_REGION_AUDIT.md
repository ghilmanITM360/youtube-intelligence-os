# Hidden-region audit v2 (checkpoint J, primary reviewer, session 85559743)
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
