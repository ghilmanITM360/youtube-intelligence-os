# Targeted evidence forensics (CH001), 2026-11-22

Tool: `tools/window_forensics.py` (native-fps decode of each window; per-frame global diff, yellow-pixel and red-pixel counts; events are measured, then confirmed by viewing contact sheets in `forensics/*_sheet.jpg`). Raw per-frame curves: `forensics/*_frames.csv`, `*_events.json`. Event table with unique document-instance and annotation-event IDs: `forensics/EVIDENCE_EVENTS.csv`. Narration alignment uses the unverified local ASR word timings (the 7uu6qaCGZsY and OC1yu0L7jT4 workspaces do not exist, so those two windows have no narration alignment).
Evidence labels: [M] measured, [O] viewed, [U] unavailable. Sample: 9 annotation events in 6 documents across 5 videos. Nothing here is a channel-wide rate.

## Measurement caveat found
The yellow/red pixel detectors also fire on artwork (red X marks, red arrows, the yellow "$" glyph on drawn banknotes). In the 7uu6 and OC1y windows every "pre-marked" flag was artwork, not a document mark. Document marks are therefore claimed only where a frame was viewed. The earlier "progressive" reading of the yViM 275 s ellipse was wrong: a baseline of 112 red pixels from the "BIG BUSINESS" artwork made the 5%/95% thresholds look gradual; the ellipse is one frame.

## Findings per window
| Window | Document | What happens [M]/[O] |
|---|---|---|
| yViM 204.75-209.96 | CNBC search-result card, $1.28 trillion | Red ellipse appears complete in one frame at 206.667 s (f4960); card was on screen at least 1.9 s earlier; ellipse lands 0.15 s after the spoken "$1"; held to the window end. Instant, not drawn. |
| yViM 275.79-279.08 | Dark AI-summary-style card, 7.1% bankruptcy filings | Red ellipse appears complete in one frame at 277.792 s (f6667), 0.09 s after "7". Matches Codex's f6666 to f6667. "2025" was pre-highlighted by the source UI. |
| Xkk9 74.08-78.125 | EIA chart with 2006 tooltip | Red ellipse around the tooltip, instant at 75.247 s; then a yellow highlight sweeps the "imports 13.71 million barrels per day" row left to right, about linear, 75.33 to 77.33 s (2.0 s), finishing about 0.15 s before "imports" is spoken. Ellipse 0.6 s after "60%" was spoken (it marks the tooltip row for the clause that follows). Two different techniques on one document. |
| 7K99 3.97-6.57 | Google Finance S&P 500 card | Red arrow already present when the window opens (pre-marked comparator); card held 2.6 s; cut at 6.57. |
| DKyJ 403.87-412.0 | Mag-7 article card | Red ellipse around the 36% sentence appears complete in one frame at 407.837 s, 0.04 s before the clause "now make up around 36%..." begins and 1.12 s before "36" is spoken; whole document visible and legible from the window start, no zoom. |
| Im-N3 184-204 | Four documents in 20 s | (a) DVD cover with red X (pop-culture, not transferable), (b) "That's right." text card, (c) MacroMicro chart with 35.45 underline already present, (d) a redrawn article card: empty card with only a title for 2.37 s, then paragraph plus red underline under 41.8% appear together in one frame (199.333 s), 0.21 s before "MAG 7"; replaced at 203.733 s (the narration "And if you swap" starts 203.74) by a larger card with a second paragraph and a second pre-placed underline. Slow ~1-3% scale drift on held cards. |
| 7uu6 146-176 | Mechanism sequence (no document marks) | Text beat card ("Maybe..."), two third-party clips relabelled with a white "Private Credit" sticker (not transferable), character vignette (lender offers money, borrower shrugs), building with red X (avoiding Wall St.), brand-logo cards (Blackstone, Venmo) for identification, chalkboard teacher scene with a numbered step "1. Originate Direct Loan". |
| OC1y 310-340 | Comparison/mechanism (no document marks) | Two numbers side by side ("1%" vs "3.5 - 3.75%") with a red arrow pop-in sequence (1 arrow at 313.4, 6 by 314.0, five staggered steps in about 0.6 s), reused later inside a character's speech bubble as a callback ("The gap" plus arrows); object metaphors (crossed-out crying dollar, yen pile vs dollar, cliff edge, red monster); hard cuts every 2-4 s. |

## Verification of displayed claims
| Claim shown | Result |
|---|---|
| Credit card debt $1.28 trillion, Q4 2025, up $44 billion | Confirmed: NY Fed Household Debt and Credit Report, Q4 2025 (press release 2026-02-10). The card's own article is a CNBC piece I did not open. |
| Business bankruptcy filings 24,737 vs 23,107, +7.1% (year ending Dec 31 2025) | Confirmed against U.S. Courts statistics (arithmetic 24,737/23,107 = +7.05%). The card's "decade-long high" and "slow-burn" statements: unresolved. The dark card's origin (search-AI summary style) unresolved. |
| EIA chart, tooltip 2006 imports 13.71 million barrels per day | Not confirmed (search did not return the table value) [U]. The chart prints its own vintage: Monthly Energy Review Table 3.1, September 2023. |
| S&P 500 6,728.80 on Nov 7, 2025 | Consistent with the displayed Google Finance card; not independently re-fetched. |
| 41.8% of S&P 500 YTD return from Magnificent Seven through Q3 2025; 35.45% market-cap share | Third-party redraw/chart sources (Proactive Advisor Magazine, MacroMicro): unverified. |

## Corrected evidence-animation rules (replace the 4.8 s rule)
1. There is no universal highlight delay. Record these events separately for every document instance: source entry, target legible, mark onset, mark complete, replacement/exit.
2. Observed treatments, in order of frequency here: instant complete red ellipse (4 of 9 events), mark already present on entry (3), instant paragraph-plus-underline reveal (1), progressive yellow sweep (1). Progressive red underline/ellipse drawing was NOT observed in this sample.
3. Timing relative to the spoken number: +0.15 s, +0.09 s (mark lands as the number is said); 0.04 s before the clause start and 1.12 s before the number; 0.21 s before the clause and 1.28 s before the number (mark placed at the clause start); +0.97 s after the number (ellipse placed on the following clause's evidence). So two modes: mark on the number, or mark at the clause start, with a range of about -1.3 to +1.0 s around the number onset. n=5 timed events, ASR-unverified.
4. A yellow sweep duration can track the clause (2.0 s for a 2.1 s clause). 5. Held documents stay 2.6-4.4 s after the mark. 6. A card can enter empty or title-only and receive text plus mark at the clause that quotes it. 7. A replacement card can cut exactly on a clause boundary.
All are priors from a small sample. Our renderer takes onset/complete frames as parameters; set them from the verified narration clause.

## Unmatched or uncertain observations
- D04 and D06 entry frames precede their windows, so onset is unknown. - The Xkk9 yellow row identity was seen at low resolution. - Document entry transitions (cut vs pop) were not captured because entry precedes most windows. - The Bitcoin-thumbnail case (Codex f157) was not re-measured here.
