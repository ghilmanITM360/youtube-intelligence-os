# Independent QA: A) V1_RENT_R4_0-75s_v3.mp4 and B) V1_RENT_R5_75-122s.mp4

Reviewer working files: /private/tmp/claude-501/qa_r5/ (contact sheets A1-A4, B1-B4, crops). No production file edited, nothing rendered.

## Verdicts
- **A (R4 v3, 0-75 s): PASS WITH FIXES.** All seven claimed revisions verified. No data or narration contradiction. Two P2 visual defects remain (one new regression).
- **B (R5, 75-122.3 s): PASS WITH FIXES.** Facts match the BLS factsheet; sync is good except one 0.83 s late numeral. Method is followable but has three P2 items (misleading 5-of-12 sample picture, flashing month stepper that never reaches June, dead white frame).

## (1) Technical
| Check | A | B |
|---|---|---|
| ffprobe | h264 1920x1080 30 fps, 2250 frames, 75.000 s; AAC mono 48 kHz 75.000 s | h264 1920x1080 30 fps, 1419 frames, 47.300 s; AAC mono 48 kHz 47.300 s |
| Full decode (`-f null`) | no errors | no errors |
| SHA-256 vs .sha256 file | f1a786a5...80f0e MATCHES | 4bf34522...13651 MATCHES |
| Audio vs Take 2 slice | PCM 3,600,000 samples = slice 0-75 s; relative RMS error 0.53% (AAC loss only), sample-aligned | 2,270,400 samples = slice 75-122.3 s; rel. RMS error 0.54%, aligned |
| Audio md5 | 9920006e... identical to R3 baseline audio (same AAC stream); raw-WAV md5 cannot match after AAC, so the aligned-difference test above is the evidence | efbcec5a... (AAC re-encode, 0.3 s fade-out at end) |
| Ending | cut at 75.0, S016 starts 75.14 (clean) | silence detected 46.93-47.30 (= 121.93-122.30); ends before S029 (122.72). Clean |
Baseline R3 out/V1_RENT_segment_0-75s_take2.mp4 sha256 = a40bbccc147368b49c7af10060c537225f4f6c1c1d25fb8e83ec8ba74577516c: UNCHANGED (verified).
Note: B starts 0.14 s before S016 speech; A/B seam is continuous (A ends 75.0, B starts 75.0).

## Verification of the claimed A revisions
| Revision | Result |
|---|---|
| Open-licence fonts (Patrick Hand / Caveat Brush) | VERIFIED visually. Marker Felt removed. Source tags still Helvetica (licence note admits this; not cleared) |
| 7 vs 1 (previous P1) | FIXED. 2.7%, 7.7%, 1.7%, 1/3 read correctly at 640 px; the 7 has a crossbar and looks like a "T-hook" glyph but cannot be mistaken for 1 |
| Seven tiles at 38.0-39.9 -> CPI document + "Rent" tag | VERIFIED, no "1/7" implication. **Regression: "one piece of it" collides with the document** (see P2-A1) |
| Slope line 71.4-75 removed | VERIFIED (72.0-74.8 text and host only) |
| Circles | 2.8%, 7.7%, 25.9%, 35.3% now enclose the numerals (no slicing). 35.3% ring touches the word "Shelter" (P3) |
| Tofu minus / derived note | FIXED: "(about 1.7%, derived: 35.3 minus 7.7 minus 25.9)" legible; 50 px text (4.6%, under the 5% label rule) |
| Source tag on 14.3-17.9 | FIXED (present on both beats) |
| Previously late/early words (MEASURES 29.8, ruler 29.85, Not a 64.5, ? 31.5, one piece 38.3) | all within 0.1 s of ASR |

## (2) Numbers and claims vs registers
**A:** 2.8% (BLS), 2.7% (Zillow), 7.7%, 25.9%, 35.3%, derived 1.7% (labelled), Aug 2026 weights, about 1/3: all equal register values; bar and pie geometry proportional (pie final wedge about 127 deg earlier measured; bar 7.7/25.9/1.7 segments read correctly). No unsupported figure, nothing after 75 s. Remaining soft points: "= housing" for Shelter is narration wording (Shelter is not all housing); "about 3%" is narration rounding, not labelled derived. Orange now means "Rent" (bar, tag) and also "Shelter" (pie wedge 66.7-70.3): colour semantics drift (P3). Olive = BLS rent index and owners' equivalent rent (carried P3).

**B vs BLS factsheet (re-fetched today):**
| On screen | Support |
|---|---|
| 12 houses, 5 blue (sample) | Concept supported ("a small number (usually 5)... per segment"). 5 of 12 = 42% shows a large share; no on-screen "illustration" label. Misleading by scale: **P2** |
| "every 6 months" | exact quote |
| LEASE "fixes the rent for a term" | page: "locked in place for a given lease term"; causal "because" is the narration's, indirect. OK |
| Six panels; Panel 1 Jan/Jul; Panel 2 Feb/Aug; "and so on" | exact quotes; "etc." |
| Stepper Jan..May = Panel 1..5 | months 3-6 not stated by the page ("etc."); consistent extrapolation, register marks D. Acceptable but the visual states it as fact |
| 1/6 each month | derived (6 panels, one per month); register D |
| "monthly change = sixth root of ratio" | page: "sixth root of this relative is the 1-month change". Strictly the root gives a relative (about 1.00x), not a percent change. Narration says "monthly change"; on screen consistent with narration. P3: say "relative" or add "(1 + change)" if an example is ever shown |
| ratio = today's avg rent in panel / avg rent same units 6 months earlier | as narrated (the page calls it a relative); OK |
| chain Jan-Feb-Mar-Apr -> "the index" | page: index(t) = index(t-1) x relative. Boxes are months, not the changes; arrow leaves from the Feb/Mar gap. Concept right, picture loose (P3) |
No unsupported number, nothing from S029+, no example figures. Panel schedule, one-sixth, sixth-root formula, ratio definition and chain do not contradict narration.

## (3) Word-to-visual sync (ASR t2_words_merged.json, tolerance 0.2 s; visual times from the build code and confirmed by frame-change detection)
**A (about 80 pop-ins checked): no item over 0.3 s except:**
| t (s) | Visual | Word | Delta |
|---|---|---|---|
| 67.9 | "of the inflation index" | "inflation" 66.98 | +0.9 (label trails; acceptable as a subtitle line) |
| 19.2 | rent bill | "rent... bigger" 18.71-19.87 | +0.5 (no unique word) |
| 66.7-68.0 | pie wedge grows 6% -> 25% -> 35% under a finished "about 1/3" label | "about a third" 66.58 | ~0.7 s of mismatched wedge (P3) |
| 16.95 | "about 3%" | "3%" 17.35 | -0.4 numeral, "about" on time (carried) |
**B (about 45 pop-ins): worst offenders**
| t (s) | Visual | Word | Delta |
|---|---|---|---|
| 101.5 | "1/6" | "one-sixth" 100.67 | **+0.83 (P2)**; "of the sample" 101.6 vs "of" 101.23 +0.37 |
| 119.5-119.8 | Jan chip and "monthly changes, chained" | "monthly" 119.22 / "changes" 119.50 | +0.3 to +0.6 |
| 107.9 | "ratio" | "ratio" 108.13 | -0.23 |
| 77.8 | "how it measures rent" | "how" 77.60 | +0.2 |
Everything else within 0.15 s (method 75.3, houses, sample, price 85.4, every 6 months 86.2, lease 87.4/87.9/88.9, panels 91.2-92.4, January 94.5, July 95.8, February 97.2, August 98.0, arithmetic 104.3, formula 105.9-107.0, fraction bar 110.6, six months earlier 113.0, sixth root 114.8, six-month 115.4, one-month 116.9, index 121.4).

## (4) Visual grammar vs doc 22
Common: canvas #FDFDFD, one focal subject per beat, hard cuts, stepped pop-ins, red scribble annotation, no idle motion, host head swaps at beat cuts. Still-frame share: A 2249 frames, change clusters about 75; B similar (14 hard cuts in 47 s, about 22 per 75 s: inside the 17-35 band).
**A defects:** collision at 38.0-39.9; stray red dash left of "Rent" tag at 38.2-38.5 (arrow draw-on start, reads as a mark); room beat 4.6 s (rule 1-3 s); three host scales (0.34/0.46/0.50) and identical point pose (placeholder); thick green torso (placeholder).
**B defects:**
- 82.4-82.9: at the cut into "a sample" five houses are absent (7 grey houses, 5 holes) until the blue ones pop in at 82.9-83.4. Reads as houses vanishing, not "turning blue" (P3).
- 99.5-99.9: 0.4 s completely blank frame (source tag only) before the stepper (P2).
- 99.9-101.4: month stepper changes state every 0.35 s (Jan, Feb, Mar, Apr, May); it is cut at 101.4 so June/Panel 6 never appears, and each state is held only 10 frames: strobing, not "every month" (P2). "Panel k" inside the boxes is 44 px (4.1%, under the 5% label rule): hard to read at 640 px.
- 108-109: the radical's overbar runs through the top of "ratio" (text crossed by the vinculum) (P2).
- 112.0: the denominator reads "average rent, same units," with a dangling comma until "6 months earlier" arrives at 113.0 (P3).
- 94.0 tiny "priced" mid-pop at about 40% scale (3-frame pop, intended; P3 only because it reads as a tiny label).
- 92.4 "PANELS" sits close to the source tag line (no overlap).
- Host appears in 5 of 15 beats (smile, neutral, smirk; down/point/shrug poses): variety is thin but within the rig.

**Phone legibility at 640 px:** titles, bars, numerals fine; 7 vs 1 and 2.7 vs 2.1 resolve in Patrick Hand (the earlier misread is gone). Source tags (Helvetica 44 px, about 11 px tall at 640) are readable but small. B "Panel k" in stepper and A derived note are the smallest text.

## (5) Educational clarity of B
A viewer can follow the sequence: sample -> priced every 6 months (lease) -> six panels -> one panel a month -> ratio -> sixth root -> chain. Gaps: (a) nothing ties a specific panel's 6-month ratio to that month's index move (panel rotation and the formula are shown in separate scenes); (b) no worked numbers, so "sixth root turns six-month change into one-month change" is asserted, not shown; (c) "monthly change" and "ratio" are two boxes with no visual link to the "6-month change" box; (d) the sample picture implies a large sample share. Fix with the smallest additions: one line "same panel, one month at a time" and a not-to-scale tag.

## (6) Originality
Generic flat icons (houses, lease, boxes), original host (curly hair, green vest, navy legs); nothing traces the reference. Fonts OFL. Source-tag font is Apple Helvetica (not cleared, noted by the project). No concern.

## (7) Editorial pacing
A: room beat 17.9-22.5 s (4.6 s) carries three reveals (bubble 17.9, bill 19.2, "?" 20.4), is the single scene plate and matches a 21-word sentence; acceptable but 1.5 s over the guide, and the lowest-energy stretch; P3 (trim to about 3 s only if the cut can follow the narration). B: 15 beats, mean 3.15 s, min 1.9 (stepper), max 5.3 (ratio definition, 3 stacked reveals, fine). First 4.9 s is host-only plus a title: OK as an opener.

## (8) Fonts
Patrick Hand body/numerals and Caveat Brush display: legible, consistent, open-licence. Caveat Brush red words (YOU, WEIGHTS, arithmetic) read at 640 px. Small sizes: A derived note 50 px; B "Panel k" 44 px; "priced" and "Feb" labels fine.

## Scorecard
| Item | A | B |
|---|---|---|
| Background | MATCHES (room beat long) | MATCHES |
| Body structure | PARTIAL (placeholder rig, thick torso, 3 scales) | PARTIAL (same rig) |
| Head / expressions | ACCEPTABLE ORIGINAL ADAPTATION | ACCEPTABLE ORIGINAL ADAPTATION (few appearances) |
| Poses | PARTIAL (point pose identical every time) | PARTIAL |
| Stroke / colour | ACCEPTABLE ORIGINAL ADAPTATION (orange/olive reused for two meanings) | ACCEPTABLE ORIGINAL ADAPTATION |
| Financial / educational graphics | ACCEPTABLE ORIGINAL ADAPTATION (bars, pie; pie wedge grows under finished label) | PARTIAL (sample picture misleading, stepper strobes, formula overstrike) |
| Typography | ACCEPTABLE ORIGINAL ADAPTATION | ACCEPTABLE ORIGINAL ADAPTATION (small Panel labels) |
| Motion / editing | MATCHES | ACCEPTABLE ORIGINAL ADAPTATION (blank 0.4 s, strobing stepper) |
| Source readability | ACCEPTABLE ORIGINAL ADAPTATION (small at 640) | same |
| Narration sync | MATCHES | MATCHES except 1/6 (+0.83) |
| Factual accuracy | MATCHES | MATCHES (illustrative sample not labelled) |
| Originality | MATCHES | MATCHES |
| Overall | PASS WITH FIXES | PASS WITH FIXES |

## Defects ranked
### A
**P1:** none.
**P2**
1. A-P2-1, 38.0-39.9: "one piece of it" starts at the document's lower-right border and is clipped/touched by it (frames 38.5, 39.5). Smallest fix: move the text right about 80 px or down 40 px (txt at x 1300, y 700 in beat 15 of tools/v1r4_render.py line 247).
2. A-P2-2, 38.2-38.5: stray red dash left of the Rent tag (arrow draw-on first step shown before the arrow exists). Smallest fix: start the arrow at full length of its first step beyond the tag, or delay `arrow(...,38.5)` start so the first step is not an isolated dot.
**P3:** pie wedge 6%/25% shown under a finished "about 1/3" (delay label to 67.6 or draw wedge in one step); 35.3% ring touches "Shelter"; orange used for Rent and Shelter; room beat 4.6 s; host scales/torso/point pose (final art); derived note 50 px; source tags Helvetica.

### B
**P1:** none.
**P2**
1. 99.5-101.4 month stepper: 0.4 s blank lead-in, 0.35 s per month (strobe), stops at May, small "Panel k" text. Smallest fix: start stepper at 99.7, 0.5 s per step, show all six (or three steps and "...") or slow it to hold 0.7 s; enlarge "Panel k" to at least 54 px.
2. 101.5 "1/6" +0.83 s after "one-sixth" (100.67). Smallest fix: cut to the 1/6 beat at 100.6 and pop "1/6" at 100.7, "gets a new price" at 102.2.
3. 84.0 "5 of 12 houses blue" implies a large sample share. Smallest fix: add a small red/grey tag "illustration, not to scale" in the beat, or show 1-2 blue among about 40 houses.
4. 108-109 sixth-root bar runs through "ratio". Smallest fix: lower "ratio" (y 480 -> 520) or raise the bar by 40 px.
**P3:** houses vanish at the cut to "a sample" (draw the 5 pick houses grey from the cut, then recolour); dangling comma at 112.0; chain boxes are months not changes and arrow leaves the Feb/Mar gap; Jan chip 0.3 s after "monthly"; "monthly change" should be "relative" if a number is ever shown; no worked example for the sixth root; "ratio" 0.23 s early.

## What final Codex art must fix (host rig is a placeholder)
Torso thickness (about 5% of figure height vs 1.6-2.5% in rule), single consistent host scale (now 0.34/0.46/0.50), more than one pointing pose and arm variety, richer head set, shoe/hand detail; the room plate in the outline grammar; none of these are data issues.

## Not verified
Not played in real time at phone size (checked 640 px frames); legal font clearance beyond the project's note; BLS page quotes via a summarising fetch, not raw HTML.
