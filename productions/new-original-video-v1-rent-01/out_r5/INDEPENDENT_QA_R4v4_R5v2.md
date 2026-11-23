# Independent QA: A) V1_RENT_R4_0-75s_v4.mp4 and B) V1_RENT_R5_75-122s_v2.mp4

Reviewer working files: /private/tmp/claude-501/qa_r4v4_r5v2/ (JPEG montages m1-m8, m360, crops). No production file edited, nothing rendered. Method: ffmpeg frame extraction of the actual MP4s, per-frame luma-diff analysis, ffprobe/silencedetect, word timings from audio/take2/t2_words_merged.json, builder files for beat times, one WebFetch of the BLS factsheet.

## Verdicts
- **A (R4 v4, 0-75 s): PASS.** All claimed v4 fixes verified in the rendered frames. No P1, no P2. Six P3 items.
- **B (R5 v2, 75.0-122.3 s): PASS.** All claimed v2 fixes verified. Explanation is faithful to the BLS factsheet. No P1, no P2. Seven P3 items.
- **Critical defects: none** (no P1, no P2 in either video).

## (6) Technical (verified)
| Check | A | B |
|---|---|---|
| SHA-256 | 8501627a...f3a37b MATCHES | a288a438...d5548 MATCHES |
| Stream | h264 1920x1080 30 fps yuv420p, 2250 frames, 75.000 s; AAC mono 48 kHz 75.000 s | h264 1920x1080 30 fps yuv420p, 1419 frames, 47.300 s; AAC mono 48 kHz 47.300 s |
| Duration audio = video | yes (3,600,000 samples = 75.0 s) | yes (2,270,400 samples = 47.3 s) |
| Timestamps | 2250 frames, 0.000-74.967, every dt 0.0333, none non-monotonic | 1419 frames, 0.000-47.267, every dt 0.0333, none non-monotonic |
| Full decode (-f null) | no errors | no errors |
| Colour | range tv, space bt709; transfer/primaries read "unknown" (P3-T1) | same |
| Background | corner pixel decodes to 251 (= #FDFDFD in tv range) | identical 251 |
| Still-frame share (consecutive frames identical) | 86.9 % | 84.1 % |
| Beats / hard cuts | 26 beats, 25 cuts (builder), 15 large luma jumps >9 | 15 beats, 14 cuts (about 22 per 75 s, inside the 17-35 band) |
| Silence | only in gaps between sentences (0.4-1.1 s, at sentence ends); tail silent 74.34-75.0 | gaps 0.4-0.9 s at sentence ends; no gap inside a sentence |
| Blackdetect | no black frames | no black frames |
| Near-empty frames (content area blank, source tag only) | 35.50-35.63 (4 fr), 66.50-66.73 (7 fr) | 87.33-87.43 (3 fr), 90.13-90.33 (6 fr), 93.33-93.50 (5 fr), 100.63-100.73 (3 fr), 114.63-114.83 (6 fr). All at cuts, max 0.23 s; the previous 0.4 s blank lead-in before the stepper is gone (99.5 starts with a lit panel) |
| Audio click check | largest sample step is inside speech (A 40.58 s, B 8.01 s = 83.0 s); head of B starts at -1..-6 LSB, tail of A is zero: no click at the join | |

## (1)+(2) Changed areas verified in the rendered frames
### R4 v4
| Fix | Frames checked | Result |
|---|---|---|
| 38.0-39.9 s: CPI document + Rent tag + arrow + "one piece of it" replaces the seven tiles | 37.97, 38.0, 38.1, 38.2, 38.4, 38.7, 39.5, 39.87 | VERIFIED. Document is the same drawing as the previous beat (clean hard cut, nothing changes at 38.0). Orange Rent tag at right, arrow pointing at the document, "one piece of it" beneath the tag, no collision with the document edge. No "1/7" or tile implication. |
| Previous text collision | 38.4-39.9 | FIXED (text starts about 90 px right of the document edge). |
| Stray arrow dash | 38.7 shows a short red stub at the tag edge | It is the draw-on of the arrow (5-step draw, grows to full arrow by 39.0, full arrow at 39.5). Reads as drawing, not as an isolated mark. Acceptable (see P3-A2). |
| Slope line removed 71.4-75 | 70.33, 71.0, 71.5, 72.4, 72.47, 73.5, 74.5, 74.96 | VERIFIED. Only host + text; nothing drawn after 71.2. |
| OFL fonts, 7 vs 1 | 640 px and 360 px crops: 2.8%, 2.7%, 7.7%, 25.9%, 35.3%, 1.7%, 1/3 | VERIFIED. The 7 has a crossbar and cannot be read as 1; 2.7% vs 2.1% not confusable at 640; at 360 the 2.7% still reads as 2.7. |
| Source tags 44 px | e.g. 8.9, 15.5, 42.0, 61.9, 68.0 | Present on every number beat. Readable at 640; about 5 px high at 360 (unreadable there, P3-A1). |
| Transitions 35.5, 39.93, 41.33, 63.73, 66.5, 70.33, 72.43 | before/after frames | Clean hard cuts. No half-drawn object carried over, no ghost, no flash, no clipped box. |

### R5 v2
| Fix | Frames checked | Result |
|---|---|---|
| Month stepper Jan then Feb 0.5 s each, no blank lead-in | 99.4-100.7 (frames 24.4, 24.6, 24.9, 25.2, 25.6 of the clip) | VERIFIED. Cut at 99.5 lands on a lit "Panel 1 / Jan" immediately; Feb/Panel 2 from 100.1; cut to 1/6 at 100.6. No strobing. Only two months are shown although the narration says "every month" (P3-B1). |
| "1/6" at the spoken word | pop at 100.7 vs "one-sixth" 100.67 | VERIFIED (delta +0.03 s). |
| Sixth-root bar not through "ratio" | 106.8-108.9 (frames 32.0-34.0) | VERIFIED. The overbar sits above "ratio" with clear space; the index "6" in red at its upper left. |
| Sample houses 3 of 12, labelled "illustration, not to scale" | 79.97-84.9 | VERIFIED. Label is present from 80.0 to 84.7 in both house beats. 3 blue of 12 grey; no claim about the real sample size on screen. |
| Dangling comma "average rent, same units," | 112.0-113.0 | Still present until "6 months earlier" arrives at 113.0 (carried P3-B4). |
| Join with R4 | A last frame 74.967 vs B first frame 75.0 | Same host rig, same pose/scale (0.46, down/smile, x 470, feet 1010), same #FDFDFD, same font family. Hard cut with text swap; reads as the next beat. Audio: A tail is silent (74.34-75.0, 0.3 s fade), B starts 0.14 s before "Here" (75.14): no gap, no click. |

## (3) Numerical accuracy
**A (vs SEGMENT_0_75_CLAIM_REGISTER.md C-01..C-05):** 2.8% (BLS Table 1), 2.7% (Zillow), 7.7% (7.728), 25.9% (25.902), 35.3% (35.323), derived "about 1.7%" (35.323-7.728-25.902 = 1.693, labelled "derived" on screen), "August 2026 weights" on the title and on the source tags, "12 months to September 2026", "about 1/3" (derived, 35.3%), dates Oct 14 2026 / Oct 6 2026. All equal the register. Bar heights (2.8 vs 2.7 at 120 px per point) and the weights-bar widths are proportional by construction (7.7/25.9/1.7 segments checked visually in 49.9-61.9 frames). No number from after 75 s. Not supported but not numbers: "about 3%" (narration rounding, not labelled derived), "= housing" for Shelter (narration wording; Shelter is not all housing) - both carried, P3. Not independently re-verified by me against the BLS release or Zillow press release (relied on the register).

**B (vs SEGMENT_75_122_CLAIM_REGISTER.md and the BLS page fetched today):** the only numerals are "6", "6 months", "1/6", "Panel 1-6", "Jan/Feb/Mar/Apr", "6-month", "1-month". Every one is supported by the factsheet or labelled derived by the register. Quotes re-confirmed today: "(usually 5) ... renter-occupied housing units selected to represent each segment"; "collects rent data from each sampled unit every 6 months"; "divides each area's rent sample into six subsamples called panels"; "panel 1 are collected in January and July; panel 2, in February and August, etc."; "Dividing the average pure rent for the current month (t) by the average pure rent from 6 months earlier"; "The sixth root of this relative is the 1-month change"; "index for period t ... multiplying the index for period t-1 by the relative of price change"; "locked in place for a given lease term". Not found in my fetch: the phrase "same units" (screen 112-113 s and narration "the same units six months earlier"). It is narration wording, plausible (a panel is the same units priced six months apart) but I did not see it as a quote: UNVERIFIED as a BLS statement. The factsheet's "average pure rent" (adjusted rent) is simplified to "average rent": acceptable simplification, not flagged by the video.
Register inconsistency: row 99.5-103.6 says "months step Jan..Jun"; the video shows Jan and Feb only (P3-B2, record fix).

## (4) Mobile readability (frames downscaled to 640 and 360 px wide)
| Item | 640 px | 360 px |
|---|---|---|
| 2.8% / 2.7% / 7.7% / 25.9% / 35.3% numerals | clear; 7 vs 1 and 2.7 vs 2.1 resolve | clear |
| Red circles (7.7, 25.9, 35.3) | clear, enclose the numerals, no slicing; 35.3 ring touches "Shelter" text above (carried P3) | clear |
| 1/6, "ratio", "monthly change", "6-month change", "1-month change" | clear | clear |
| Index "6" of the sixth root (about 40 px tall) | readable | about 6-7 px, marginal (P3-B5); the words "sixth root" are spoken and then labelled at 114.8 |
| "Panel k" in stepper (56 px), "Panel 1-6" chips | readable | "Panel 1" tiny, readable only with effort |
| "illustration, not to scale" (50 px grey) | readable | small but legible |
| Source tags (44 px Helvetica, grey) | readable | not readable (about 5 px). Accepted family of P3 (face already accepted). |

## (5) Audio sync (words from t2_words_merged.json; R5 times are absolute full-narration times, clip time + 75.0)
Almost every label is within 0.15 s of its word. Worst items:
| t (s) | Visual | Word | Delta |
|---|---|---|---|
| 99.7 | "every month" label | "every" 99.94 | -0.24 (early, harmless) |
| 107.9 | "ratio" | "ratio" 108.13 (after "this" 107.83) | -0.23 |
| 77.8 | "how it measures rent" | "how" 77.60 | +0.2 |
| 86.2 | "every 6 months" | "every" 85.82, "six" 86.2 | +0.38 vs "every", 0 vs "six" |
| 102.2 | "gets a new price" chip | "gets" 101.93 | +0.27 |
| 100.7 | "1/6" | "one-sixth" 100.67 | +0.03 (was +0.83) |
| 106.8-107.0 | sixth-root bar / index 6 | "sixth" 106.78-107.21 | 0 |
| 38.1/38.2 | Rent tag / "Rent" text | "Rent" 38.0 | +0.1/+0.2 |
| 38.3 / 38.6 | "one piece of it" / arrow | "one piece" 38.01-38.28, "it" 38.72 | +0.02 / -0.1 |
Carried from R4 v3 audit, unchanged and still within tolerance or P3: "about 3%" numeral 16.95 vs "3%" 17.35 (-0.4), rent bill 19.2, pie wedge growth under a finished "about 1/3" label (66.7-67.8).

## (7) Explanation accuracy of the six-panel and sixth-root animations vs BLS
Faithful. Sequence on screen: sample of units -> each priced every 6 months (lease as the reason) -> six panels -> Panel 1 Jan/Jul, Panel 2 Feb/Aug, "and so on" -> stepper Jan=Panel 1, Feb=Panel 2 -> 1/6 of the sample new price each month -> monthly change = sixth root of ratio -> ratio = today's average panel rent / average rent six months earlier -> sixth root turns a 6-month change into a 1-month change -> monthly changes chained into the index.
- Month order correct (Jan before Feb, Panel 1 before Panel 2). Ratio direction correct (current over earlier). Sixth root applied to the six-month ratio, not the other way round; the picture never implies the six-month ratio is itself the monthly change (the 6-month box sits before the arrow and the 1-month box after it). Wording "one-sixth" appears only as "1/6 of the sample gets a new price", not as a one-sixth of a change.
- STATED by BLS: usually 5 units per segment (concept only), 6-month collection, six panels, panel 1 Jan/Jul, panel 2 Feb/Aug, ratio of current to 6-months-earlier average, sixth root = 1-month change, index = previous index times the one-month relative, lease-term rigidity.
- DERIVED (not stated by BLS; correctly marked D in the register): "every month 1/6 of the sample gets a new price" (six panels, one per month); panels 3-6 months (not shown, only Jan and Feb are); the picture of Jan-Feb-Mar-Apr boxes feeding "the index" (the page says index(t) = index(t-1) x one-month relative; the boxes stand for the months/changes); the illustrative 3-of-12 houses (labelled as illustration).
- Precision caveats, all P3 and none misleading to a lay viewer: (a) strictly the sixth root yields a relative (for example 1.004), the on-screen/narration "change" is the BLS-page phrase; (b) the chain boxes are labelled by month, arrow leaves from the Feb/Mar gap (the index depends on all four boxes), loose but not wrong; (c) "same units" is narration, not a BLS quote I could confirm; (d) no worked numeric example, so the root is asserted, not demonstrated (a deliberate choice: no invented numbers).

## (8) Visual consistency between the videos
Same engine and tokens: canvas #FDFDFD, Patrick Hand body / Caveat Brush display, red scribble words (#D82C2C), orange tag (Rent/Panel months/1-month), blue for Zillow/sample/panel 1, grey #E2E2E2 boxes, source tags Helvetica 44 px bottom-left at x 64 (no host) or x 700 (host on the left), host rig scales 0.46/0.34 with the same poses/heads, hard-cut grammar, stepped 24 fps content in a 30 fps file. One mild colour-meaning drift (orange = Rent in A, orange also = month/1-month in B, carried). The two videos sit back to back at 75.0 s without visible or audible seam.

## Findings table
| # | Timestamp | Sev | Evidence | Suggested action |
|---|---|---|---|---|
| P3-A1 | all source tags, esp. 8.2-17.9, 41.3-70.3 | P3 | 44 px Helvetica; unreadable at 360 px wide | accepted; no change |
| P3-A2 | 38.1-38.2 and 38.7-38.9 | P3 | orange tag blank for 0.1 s (3 frames) before "Rent" text; arrow draw-on stub for about 0.3 s | none |
| P3-A3 | 47.8 and 58.5 | P3 | red arrow tails touch the label text ("Rent of primary residence" R; "a few smaller items" few) | none unless a re-render happens anyway |
| P3-A4 | 14.3-16.5 | P3 | two-line source tag sits about 30 px under the "typical rent" label (no overlap) | none |
| P3-A5 | 66.5-66.73 | P3 | 0.23 s empty content frame at the cut into the pie beat | none |
| P3-A6 | carried | P3 | about 3% unlabelled rounding; "= housing"; pie wedge growing under finished label; 35.3 ring touches "Shelter"; room beat 4.6 s; placeholder host (accepted) | none |
| P3-T1 | metadata | P3 | colour transfer/primaries untagged (only bt709 matrix + tv range set) | tag bt709 at next encode |
| P3-B1 | 99.5-100.6 | P3 | stepper shows Jan, Feb only while narration says "every month" | none (owner: no more iterations) |
| P3-B2 | SEGMENT_75_122_CLAIM_REGISTER.md row 99.5-103.6 | P3 (record) | says "Jan..Jun"; video shows Jan, Feb | edit the register text |
| P3-B3 | 97.2 | P3 | "February" text touches both chip borders | none |
| P3-B4 | 112.0-113.0 | P3 | dangling comma until "6 months earlier" | none |
| P3-B5 | 107.0-109.3 | P3 | red index "6" about 6 px at 360 px | none |
| P3-B6 | 82.4-82.9 | P3 | three grey houses absent for 0.5 s at the cut into "a sample", then appear blue | none |
| P3-B7 | 87.33, 90.13-90.33, 93.33, 114.63-114.83 | P3 | 0.1-0.23 s near-empty frames at cuts; "same units" not found as BLS quote | none; consider verifying the phrase on the BLS page |

P1: none. P2: none.

## Not verified
Zillow press release and BLS Table 1 values (relied on the registers); host art originality; lip movement (single closed-mouth pose); playback on actual phones; the phrase "same units" on the BLS page; frame-exact comparison of every R4 beat pop time (spot-checked, not all 80 pop-ins).
