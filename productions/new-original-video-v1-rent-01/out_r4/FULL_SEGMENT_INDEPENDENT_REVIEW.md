# Independent review: V1_RENT_R4_0-75s.mp4 (corrected 75 s segment)

## Verdict: PASS WITH FIXES

The build follows the long-form grammar (white canvas, one host, one focal subject per beat, hard cuts, stepped pop-ins, drawn flat bars, red scribble annotation, hand-lettered type) and fixes every P1/P2 from the 16.5 s proof review. The data layer is correct and honest. Two kinds of visible defects remain; neither needs a re-block, only a font/annotation tweak: (a) the headline brush face makes "7" read as "1", so 2.7% reads "2.1%" and 7.7% reads "1.1%"; (b) red circles slice through numerals and, at 59.4-63.7 s, run into the source tag; the derived-value note shows tofu boxes instead of minus signs.

## P1 / P2 list (smallest fix)
### P1
1. **Digit "7" in the wide brush face (Marker Felt Wide) reads as "1".** Frames: 4.5-5.4 (2.8% ok), 8.5-12.0 s "2.7%" reads "2.1%" (b04_10.05, zoom4); 14.3-16.5 s same; 46.4-49.3 s "7.7%" reads "1.1%" with no circle (zoom3). The narration says 2.7% and 7.7%; the picture reads 2.1% and 1.1%, and the next label says "about 1.7%". On a phone this is a probable misread of two of the five key figures. Fix: draw the numerals with the 'hand' (Marker Felt thin) face, which has a crossbar on 7 (the "12 months" label uses it and reads fine), or add a visible crossbar and re-check 2.7%, 7.7% and the "3%" at 16.95 s.

### P2
2. **Red circles cut through glyphs instead of enclosing them.** 47.3-49.3 s the ellipse over 7.7% is offset and the left stroke and the "%" poke out; 54.3-55.8 s over 25.9% the ellipse cuts the "2" and "%"; 61.3-63.7 s over 35.3% it cuts "3" and "%". Same class as the earlier strike-through finding, softer. Fix: centre the ellipse on the glyph box and set rx/ry about 1.25x the text half-width/height (circ(...) args at lines for beats 18, 20, 22 of tools/v1r4_render.py), or move the circle to a separate underline.
3. **61.3-63.7 s: the red ellipse over "35.3%" overlaps the source tag line "Source: BLS, CPI release Oct 14, 2026, Table 1" (text collision, zoom2).** Number sits at y=850, tag at about y=1010. Fix: raise the Shelter group (bracket 610, label 685, number 850) by about 100 px, or push the source tag down.
4. **58.0-59.4 s: derived note shows tofu boxes.** "(about 1.7%, derived: 35.3 [box] 7.7 [box] 25.9)": the U+2212 minus is missing from the font. The label that must mark the 1.7% as DERIVED is half unreadable (the word "derived" and "about 1.7%" are readable, so the claim is still labelled). Fix: use an ASCII hyphen "-" or write "35.3 minus 7.7 minus 25.9".
5. **14.3-17.9 s (two beats) show 2.8% and 2.7% with no source tag**, and 16.95 s "about 3%" is unsourced; 3.1-5.4 s also drops the Zillow tag (not needed there). Rule 4.8 says every drawn figure carries the source and date. The tag existed in beat 4 and vanishes for the repeat. Fix: keep the two-line source tag from 8.2 s through 17.9 s (add `*source(...)` to beats 6 and 7).
6. **Word-to-visual sync, over the 0.2 s tolerance (worst first):**

| On screen | Pops | Spoken word | Delta |
|---|---|---|---|
| "MEASURES" (red) | 29.20 | "measures" 29.83 | 0.63 s early |
| "Not a" | 64.00 | "not" 64.57 | 0.57 s early |
| ruler icon | 29.40 | "measures" 29.83 | 0.43 s early |
| "?" in dashed box | 31.90 | "out" 31.46 | 0.44 s late |
| "one piece of the CPI" | 38.70 | "piece" 38.28 | 0.42 s late |
| "about 3%" (numeral) | 16.95 | "3%" 17.35 | 0.40 s early ("about" 16.86 is on time) |
| "whole CPI = 100%" | 43.00 | no matching word ("the item called" 43.54) | unanchored |
| title "Rent inflation" | 0.50 | "rent" 3.11 | header, acceptable |
Fix: MEASURES 29.20 to 29.80, ruler 29.40 to 29.85, "Not a" 64.0 to 64.55, "?" 31.9 to 31.5.
Everything else is within 0.2 s (checked each of about 80 pop times against t2_words_merged.json): BLS bar 3.9 vs "rose" 3.92; 2.8% 4.3 vs 4.28; Zillow 5.5 vs 5.47; typical market rent 7.3 vs 7.33; Zillow bar 8.2 vs "rose" 8.21; 2.7% 8.5 vs 8.51; same 12 months 9.8 vs 9.82; Two measures 12.1; two sources 12.85 vs 12.95; 7.7% 46.4 vs 46.42; 25.9% 53.4 vs 53.5; Shelter 59.6 vs 59.53; 35.3% 60.3 vs 60.26; about 1/3 66.8 vs 66.58; = housing 69.0 vs 69.08; slowly 71.2 vs 71.28.

## Status of previous proof defects
| Proof item | Status in this build |
|---|---|
| P1 strike-through over 2.8%/2.7% | FIXED. A bracket now sits above the numerals (10.1-12.0 s), nothing touches glyphs. |
| P2 source tags too small | FIXED. 44 px (4.1% of height, was 2.7%); legible in 640 px view. Beat 2 tag is centred under the chart rather than bottom-left (P3). |
| P2 "typical market rent" 1.5 s early | FIXED (7.3 s vs "typical" 7.33). |
| P2 Zillow bar grows through unlabelled heights | FIXED. Bar pops at final height at 8.23 s (static mode). |
| P2 subtitle 0.8 s late | FIXED (0.9 s vs "September" 0.68; 0.22 s, borderline). |
| P2 label sizes under 5% | FIXED. Bar labels 64 px (5.9%), red note 60 px (5.6%); smallest label 50 px (4.6%, the derived note) and 54-58 px elsewhere. |
| P3 host scale jump | NOT FIXED. Now three scales: 0.46 (hero beats), 0.34 (chart/side beats), 0.50 (room). |
| P3 thick green torso | NOT FIXED (placeholder). |
| P3 only 2 heads | FIXED in system terms: 5 heads seen (neutral, smirk, smile, worried, surprised); poses 3 (down, point, shrug). Point pose is identical every time (stiff). |

## (1) Decode, format, audio sync
- Stream: h264 1920x1080, 30 fps, yuv420p, bt709 tv range; 2250 frames, 75.000 s. AAC mono 48 kHz, 75.000 s, mean -18.7 dB, peak -1.0 dB.
- Full decode with ffmpeg `-f null`: no errors.
- SHA-256 d1221e05...a26... matches out_r4/V1_RENT_R4_0-75s.sha256 (d1221e050ce526d15f0007921c7b96f92efd017e765a72a1a36f8bb1e826f25d).
- Audio PCM md5 (48 kHz mono) is identical to the R3 baseline's audio (9920006e9318376d664d441cc89deba7), so sync is the same Take 2 track by construction; no A/V offset introduced (start_time 0 for both streams).
- Frame-level: 305 of 2249 frames differ from predecessor, so 86.4% exactly still (reference 84-96%). No single-frame blips, no idle motion; longest still run 2.1 s. The only continuous-looking change is the stepped pie draw-on (66.7-68.0, 6 steps), plus stepped circle/underline draw-ons. No rolling counters; every number pops at its final value.
- 26 beats, 25 hard cuts, beat length 1.4-5.0 s, mean 2.9 s. Beats 17-22 (the weights bar) keep the same chart and add one object per beat, so those cuts are almost invisible (a progressive build, not a hard cut).

## (7) R3 baseline
out/V1_RENT_segment_0-75s_take2.mp4 sha256 = a40bbccc147368b49c7af10060c537225f4f6c1c1d25fb8e83ec8ba74577516c: UNCHANGED (matches the expected hash).

## (2) Numeric accuracy against the claim register
| On screen | Time | Register | Result |
|---|---|---|---|
| 2.8% (BLS rent) | 4.3-5.4, 8.1-17.9 | 2.8%, BLS Oct 14 2026 Table 1 | Correct value; tag present 3.4-5.4 and 8.2-14.3; MISSING 14.3-17.9 (item 5) |
| 2.7% (Zillow) | 8.5-16.5 | 2.7%, Zillow Group Oct 6 2026 | Correct value; reads "2.1%" (P1 item 1) |
| Bar heights | 8.1-16.5 | zero baseline, 120 px per point | 2.8 bar 336 px vs 2.7 bar 324 px. Proportional; honest "almost the same" |
| 7.7% | 46.4-49.3 | 7.728 | Correct, reads "1.1%" (P1) |
| 25.9% | 53.4-55.8 | 25.902 | Correct, readable |
| 35.3% | 60.3-63.7 | 35.323 | Correct |
| about 1.7% "derived" | 58.0-59.4 | 1.693 derived | Value and "derived" label present; formula glyphs broken (item 4) |
| "about 3%" | 16.95-17.9 | narration's own rounding | Not a register item, not labelled derived; narration says it, acceptable (P3) |
| about 1/3 pie, "= housing" | 66.5-70.3 | 35.3% about 1/3, derived | Pie wedge measured about 127 deg (35.3% = 127.2 deg). Source tag gives 35.3%. "Housing" is the narration's wording (shelter is not all housing); not on screen contradicting narration |

Weights bar: bar spans x 360-1560 (1200 px = 100%). By construction and checked in a frame at 63.6 s: rent 92.7 px (7.728%), owners' equivalent rent 310.8 px (25.902%), sliver 20.3 px (1.693%), shelter bracket 424 px (35.323%), ends at x 784. PROPORTIONAL. The title and tag say August 2026 weights. No claims shown after the 75 s mark; no seasonal-adjustment claim; no screenshot of BLS or Zillow; Zillow icon is a generic house plus a blue "Zillow" wordmark (nominative use, not the logo).
Label vs narration contradictions: none found. Minor: 38.0-39.9 s shows 7 equal tiles with Rent as one tile (reads as "1/7"); the next beats correct it to 7.7%. 71.4-75 s draws an unlabelled gently rising line under "rent moves slowly" (decorative, no data, no axes; could be read as a chart).

## (4) Visual grammar vs doc 22 (viewed frames at every beat, mid and end, plus 640 px sheets)
- **L1/R1 canvas:** `#FDFDFD` on 25 of 26 beats. One room plate (17.9-22.5 s, 4.6 s; rule says 1-3 s). The plate is the earlier cream room with a coloured, unoutlined style that differs from the outline grammar; it is the project's own asset. P3: shorten to about 3 s or replace with a drawn room.
- **L11 one focal subject:** met. Each beat is title/chart/icon plus at most the host.
- **L3/R2 host:** head about 0.39 of figure height (reference 0.31-0.38, rule 0.31-0.38), separate head and body layers, white shoes, curly hair. Torso is a thick green rectangle (about 5% of figure height vs rule 2.5%): reads as a vest on sticks. Placeholder; see section 8.
- **L4/L5 expressions:** head swaps at hard moments (worried at 31.5, smirk 13.7). No lip sync. Good.
- **L7/L8 motion:** hard cuts, held frames, stepped 2-5 frame pops, no idle bob. MATCHES.
- **L9 graphics:** hand-wobbled flat bars, drawn axis, red scribble circle/arrow, hand lettering. The reference uses line charts and real screenshots; bars are an adaptation. Colour semantics reuse olive for BLS rent index (2.8%) and for owners' equivalent rent (25.9%) (P3).
- **L10 type:** hand-lettered style at 5-12% of frame height; source tags in a plain sans, 4.1% of height, bottom-left except beat 2 (centred under chart). Red used for emphasis words (DIFFERENT, YOU, WEIGHTS, side detail, slowly) consistently.
- **Phone legibility (640 px sheets):** titles and labels legible; source tags small but readable; the 7 glyph issue is the only legibility failure.
- **Geometry/animation glitches:** no off-screen elements, no clipped text except circles slicing digits (item 2) and the 35.3% circle running through the tag (item 3). Pie draw-on shows interim wedges of 10%, 25% without a label (P3, harmless). Partial scale-pop of labels at 8.2 s (tiny "Zillow typical rent" for 1-2 frames) is the intended 3-frame pop.

## (5) Originality
No resemblance to a specific reference asset. The reference host is a spiky-haired black line stick man with a flesh face; this host has curly dark hair, a green vest, navy legs, white shoes. Red circle/arrow and bar charts are generic devices. The wavy "almost the same" glyph and house icon are generic. Marker Felt and Helvetica are Apple system fonts used in the output: P3 licence check if the final video is published commercially.

## Scorecard
| Item | Rating |
|---|---|
| Background | MATCHES (room plate beat too long, P3) |
| Body structure | PARTIAL (thick torso, three scales; placeholder) |
| Head / expressions | ACCEPTABLE ORIGINAL ADAPTATION (5 heads, swaps at cuts) |
| Poses | ACCEPTABLE ORIGINAL ADAPTATION (3 poses, point pose repeated) |
| Stroke / colour | ACCEPTABLE ORIGINAL ADAPTATION (richer fills than the reference, consistent outline) |
| Financial graphics | ACCEPTABLE ORIGINAL ADAPTATION (bars and weights bar proportional; circle placement defective) |
| Typography | PARTIAL ("7" reads "1" in the brush face; tofu minus signs) |
| Motion / editing | MATCHES |
| Source readability | ACCEPTABLE ORIGINAL ADAPTATION (4.1% height, one collision, two beats without tag) |
| Narration sync | ACCEPTABLE ORIGINAL ADAPTATION (about 80 pops checked; four over 0.4 s) |
| Numeric accuracy | PARTIAL (all values correct; 2.7% and 7.7% misreadable as 2.1% and 1.1%) |
| Originality | MATCHES |
| Overall | ACCEPTABLE ORIGINAL ADAPTATION (verdict PASS WITH FIXES) |

## P3 list
- Room plate 4.6 s with a different painting style (17.9-22.5); shorten or redraw.
- Host scale 0.34 / 0.46 / 0.50; pick two sizes by rule.
- Beat 2 source tag centred rather than bottom-left (3.4-5.4 s).
- Equal-size tiles at 38.0-39.9 s imply equal weights; use one tile with a "?" or a weights row from the start.
- Decorative unlabelled slope at 71.4-75 s; label "illustration" or remove.
- Same olive used for BLS rent and owners' equivalent rent.
- Pie interim wedges unlabelled (66.7-68.0 s).
- Weights bar beats 17-22 do not look like cuts (progressive build); fine, but the storyboard text says hard cuts.
- Marker Felt/Helvetica licence check.

## (8) Host rig (provisional placeholder)
System judgement: the layered rig (separate head and body, 5 heads, 3 poses, anchor file) works, the swaps are clean and the character is stable across all 26 beats; the placement system (feet fixed at the same y, neck x per layout) is sound. Final Codex art must fix: a thin line body (about 2.5% of figure height) in the same stroke as the chart outlines instead of a thick torso; one consistent figure scale; 5+ heads that include worried and flat, plus a sunglasses/aside option; 4+ poses with varied pointing/shrug/hands-on-hips arms and legs (the current point arm is identical in every beat); a stroke weight matching the bar outline; clothing hint only; optional hand-lettered type that reads as drawn (letter-by-letter reveal at 24 fps) instead of whole-word pops; and a drawn (outlined) room plate for the single environment beat.

## Evidence and limits
- Frames: /private/tmp/claude-501/full_review/ (f/ = 52 frames at beat middle and end, sheet_1-7.jpg at 640x360 per frame, zoom1-4.jpg, steps.jpg for pop/draw-on sequences, d.raw 320x180 gray decode used for diffs).
- Reference views: chars_normalized.jpg, SHEET3_charts.jpg, SHEET4_typography_props.jpg (SHEET1 and SHEET5 not opened; INSUFFICIENT EVIDENCE for background/motion comparison beyond doc 22 itself).
- Source of timing: tools/v1r4_render.py t0 values cross-checked against decoded frame diffs (pop frames at 29.23, 29.43, 64.0 and others match the code).
- No percentage scoring used. No production files were edited, nothing rendered or committed.
