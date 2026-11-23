# Independent review: V1_RENT_R4_PROOF_0-16.5s.mp4

## Verdict: PASS WITH FIXES (scale to 75 s only after the P1 and P2 fixes below)

The proof clearly adopts the long-form grammar (white canvas, one rig, hard cuts, drawn bars, hand lettering, red annotation) and is a large improvement on the failed 75 s baseline (beige room, photoreal-style character). It is not a design-system failure. One visual defect (the strike-through over 2.8%) would be read by a viewer as a data error, and a few timing and legibility items need fixing before scale-up.

## Evidence
- Decode: h264 1920x1080, 30 fps, 495 frames, 16.500 s; AAC mono 48 kHz, 16.500 s. Audio mean -19.3 dB, identical to take2 wav over the same 16.5 s (same track, no drift check beyond equal duration/level).
- Frames: 2 fps sheets and beat frames in /private/tmp/claude-501/proof_review/ (f/, p/, sheet_1-3.jpg, p/phone.jpg 640 px view).
- Playback (decoded 320x180 per-frame diff): only 67 of 495 frames differ from their predecessor (about 86% exactly still frames; reference 84-96%). Hard cuts (diff above 15) at 3.13, 5.43, 8.13, 12.00, 14.33 s. Beats: 3.1, 2.3, 2.7, 3.9, 2.3, plus the last 2.2 s, all within the 2-4 s rule. Everything else is 2-4 frame stepped pop-ins (0.5, 1.43, 3.13-3.5, 3.93-4.0, 5.43-5.8, 8.13-8.3, 9.83-9.9, 12.9, 13.7, 15.0). No idle bob, no continuous motion, no easing, no lip movement. This matches L5/L7/L8 and rule 4.5.

## Narration sync (t2_words_merged.json)
| On screen | Time | Word | Delta |
|---|---|---|---|
| Title "Rent inflation" | 0.57 | "rent" at 3.11 | 2.5 s early (title, acceptable as topic header) |
| "12 months to September 2026" | 1.47 | "September" 0.68 | 0.8 s late |
| Chart beat cut, axis/label | 3.13 / ~3.4 | "rent index" 3.11-3.47 | OK |
| BLS bar | 3.93-4.0 | "rose" 3.92 | OK |
| 2.8% label | ~4.4 | "2.8%" 4.28 | 0.1 s late, OK |
| Red circle on 2.8% | ~4.8-5.1 | emphasis | OK |
| Cut to Zillow | 5.43 | "Zillow's" 5.47 | OK |
| "typical market rent" label | 5.73-5.8 | "typical" 7.33 | 1.5 s early |
| Zillow bar grows, 2.7% | 8.23-8.5 | "rose 2.7%" 8.21 / 8.51 | OK |
| "the same 12 months" | 9.83 | "same" 9.82 | OK |
| Cut to "Two measures" | 12.00 | "Two" 11.96 | OK |
| "Two sources" | ~12.9 | "two" 12.95 | OK |
| Cut to chart with approx-equal sign | 14.33 | "almost" 14.32 | OK |
| "almost the same answer" label | 15.0 | "almost the same answer" 14.32-15.16 | OK |
Most items land within 0.2 s. Outliers: Zillow label (early), subtitle (late).

Numbers: 2.8% BLS and 2.7% Zillow are correct. Bar heights are drawn to one scale from a zero baseline (2.8 vs 2.7 look nearly equal, which is honest and supports the line). Source tags carry dates (Oct 14 2026 Table 1; Oct 6 2026 Zillow). Intermediate value risk: the Zillow bar grows in 3 steps (8.23-8.30) and for about 0.1 s a shorter bar, about 60% of final, is on screen without a label. Nothing numeric is mis-stated; no rolling counter is used. Label wording "typical rent" vs narration "typical market rent" is acceptable.

## Judgement
- Background: white (#FDFDFD-class) throughout, no room plate. Matches L1.
- Character system: separate head and body, head about 0.33 of figure height (measured about 200 of 610 px at 4.8 s), three arm poses seen (arms down, shrug, pointing), several head drawings (neutral, smirk), no mouth animation, identity stable across beats. Fits L3/L4/L5. Departures from the reference: the torso is a thick green rectangle (about 5-6% of figure height, reference line body 1.6-2.5%), shoes and curly hair are original and not the reference's spiky hair or bare stick. That is good for originality but the body reads as a "vest on sticks" rather than a line body. The figure also changes scale between beats (full height at 0-3 s and 12-14 s, about 0.6x in chart beats), acceptable but inconsistent.
- Chart grammar: wobble-outlined flat bars, hand-lettered numbers and labels, red scribble circle on the key number, red "approx equal" glyph and red annotation. Matches L9 and rule 4.6 (numbers pop at final value). Reference uses line charts and real screenshots; bars are an acceptable adaptation. The Zillow house plus blue wordmark is a generic icon, not Zillow's logo; fine.
- Typography: brush title and Comic-style labels are large and high contrast. Labels about 3.5-4% of frame height ("Official rent index" about 4%), below the 5% rule but readable at 640 px width. Source tags are about 2.6-2.8% of frame height, below the 3.4% rule; at 640 px (p/phone.jpg) they are barely legible and are a plain face as required.
- Hierarchy: one focal subject per beat, title or chart plus a small host. Strong.
- Originality: no resemblance to a specific reference asset. Reference host is a bare black-line stick man with spiky hair; this one is a coloured, clothed, curly-haired figure. Chart bars use similar red circle device, which is a generic technique. No copied artwork found.
- Animation quality: crisp and appropriately stepped. Draw-on of circle and underline is stepped. Weakness: pop-ins give no sense of hand-drawn lettering, and the stepped timing is 30 fps steps rather than the 24 fps stepping noted for the reference (minor).

## Scorecard
| Item | Rating |
|---|---|
| Background | MATCHES |
| Body structure | PARTIAL (thick torso, scale changes) |
| Head / expressions | ACCEPTABLE ORIGINAL ADAPTATION (only 2 expressions seen in 16.5 s; INSUFFICIENT EVIDENCE for the 5-head set) |
| Poses | ACCEPTABLE ORIGINAL ADAPTATION (3 poses, stiff) |
| Stroke / colour | ACCEPTABLE ORIGINAL ADAPTATION (colour fills are far richer than the reference; outline weight consistent) |
| Financial graphics | ACCEPTABLE ORIGINAL ADAPTATION (defect at 10.2-11.9 s) |
| Typography | ACCEPTABLE ORIGINAL ADAPTATION (labels slightly under the 5% rule) |
| Motion / editing | MATCHES |
| Source readability | PARTIAL (too small on phone) |
| Narration sync | ACCEPTABLE ORIGINAL ADAPTATION (two outliers) |
| Originality | MATCHES |
| Overall | ACCEPTABLE ORIGINAL ADAPTATION |

## Defects
### P1
1. 10.2-11.9 s: a horizontal rule/bracket is drawn through the top of the numerals "2.8%" and "2.7%" (grows from the 2.8% side to about the middle of 2.7%). It reads as a strike-through, i.e. "2.8% deleted". Smallest fix: draw it as an equals sign or a bracket well above the numerals (above the "the same 12 months" caption, or between the two numbers), never overlapping glyphs; or remove it, since the beat already has the caption.
### P2
2. Source tags at about 2.7% of frame height (rule requires 3.4%); two-line tag at 8.5-12 s and 14.3-16.5 s is hard to read at 640 px. Fix: raise font to at least 3.4%, keep bottom-left, widen contrast.
3. 5.73-8.2 s: "typical market rent" label appears 1.5 s before "typical" is spoken. Fix: pop it at about 7.3 s or drop it for the "Zillow" wordmark only.
4. 8.23-8.30 s: Zillow bar grows through shorter, unlabeled heights. Fix: pop the bar at final height at the word (rule 4.6).
5. Subtitle "12 months to September 2026" pops at 1.47 s, 0.8 s after "September". Fix: show at 0.68 s.
6. Chart labels (bar names, "almost the same answer" at about 2.7% height) are under the 5% label rule. Fix: bar names at 5%, the red annotation at least 4%.
### P3
7. Host scale jumps from full height (0-3, 12-14 s) to about 0.6x in chart beats; pick one size or a deliberate two-size rule.
8. Body is a thick green torso; final art should use a thin line body with a clothing hint (rule 4.2).
9. Only two head drawings seen; final art needs the 5-head set including worried/flat; poses are stiff (pointing arm identical at 3.1, 8.1, 14.3 s).
10. Title "Rent inflation" appears 2.5 s before the word "rent"; fine as a header but could be delayed.
11. 5 beats in 16.5 s (about 0.3 cuts/s) is on the slow side of 20-30 per 75 s (this extrapolates to about 23 beats in 75 s, within the guide).

## What final art must improve
A true thin line body with a large head, 5+ head drawings, 4+ arm/leg poses, consistent scale, hand-lettered type that reads as drawn (not pop-in text), and a wobble line that is the same width as the figure outline.

## Notes
- Scope: reviewed the single proof; the other 29 landscape references were not viewed. No percentage scoring used.
- No production files were edited; no renders were made; frames only in /private/tmp/claude-501/proof_review/.
