# V1 Rent storyboard v1 (narration of record: take 2, 416.9 s)
Timing source: audio/take2/t2_sentences_timed.tsv (ASR, +/-0.1 s). 1920x1080, 30 fps. Character = original fictional male renter (approved art: v1_ch_master_front / p1 neutral / p3 bill; see CHARACTER_SPEC below). Real screenshots only where the source was read: BLS (captured later), Zillow Oct report (owner manual capture). Anything else = labelled "visualization".
Source tags: every number gets "Source, report date". Unverified = no number on screen.

| Seq | Time (s) | Sentences | Narration idea | Visual | Evidence | Chart/Highlight | Status |
|---|---|---|---|---|---|---|---|
| A hook | 0.0-31.8 | S001-S006 | 2.8% BLS vs 2.7% Zillow, why rent feels bigger | the renter at a table with a rent bill; two bars side by side 2.8 / 2.7; question mark | BLS Table 1 (Sep 2026), Zillow Sep report | highlight 2.8 row in BLS screenshot; bars = visualization | C-01 V, C-02 B |
| B1 CPI | 32.9-39.2 | S007-S008 | BLS publishes CPI, rent is one piece | Basket icon grid, rent tile lit | BLS CPI release 2026-10-14 | none | V |
| B2 weights | 39.9-74.3 | S009-S015 | 7.7 / 25.9 / 35.3 percent weights | Stacked bar of CPI, shelter 35.3 split rent 7.7 + OER 25.9 + other | BLS Table 1 relative importance Aug 2026 | highlight 3 rows on screenshot; stacked bar | C-03..05 V |
| C method | 75.1-121.8 | S016-S028 | sample, 6 months, six panels, sixth root | Calendar with 6 panels (Jan/Jul, Feb/Aug...), formula card (ratio)^(1/6), chain arrows; hypothetical example "100 -> 103 over six months = about 0.49 percent a month" labelled HYPOTHETICAL | BLS factsheet owners-equivalent-rent-and-rent | highlight "panels", "sixth root" lines on screenshot | C-07..09 V |
| C2 UNVERIFIED | 122.7-139.9 | S029-S032 | "July 2024 new rule", half percent shifts | the renter + plain text card, no numbers, no source tag | none | none | X C-24,25 |
| D1 UNVERIFIED | 140.7-163.8 | S033-S038 | Zillow Sept 2024 $2,157 / $2,101 | Plain card "Zillow series (figures unverified)". Do not chart. | none | none | X C-26. Owner should cut or re-record |
| E1 high vs fast | 164.8-197.3 | S039-S046 | level vs change, speed vs distance | Car speedometer vs odometer metaphor with the renter; no data | none | metaphor | n/a |
| D2 UNVERIFIED | 198.2-228.9 | S047-S053 | understated? academic teams, match | the renter magnifier on empty folder, "no evidence found" tone, no claims on screen | none | none | X C-27..29 |
| F0 UNVERIFIED | 229.8-254.6 | S054-S060 | rule list, disclaimer | Three-question text card (text only) | none | none | n/a (questions), disclaimer ok |
| C3 | 255.1-278.1 | S061-S064 | vacancy/age adjustment, fixed homes | Row of homes with 6 steps, "fixed set of homes" | BLS factsheet | highlight vacancy and age-bias lines | C-10,11 V |
| D3 Zillow | 278.8-299.9 | S065-S069 | Oct 2026 $1,913, 2.9%, Sep 2.7% | Zillow Oct report screenshot, highlight $1,913 and 2.9%; label "$1,859 implied (1,913/1.029)" | Zillow Oct report 2026-11-12 | highlight; do not plot Sep $1,932 with Oct $1,913 | C-12,14 V; C-13 D; C-15 B |
| E2 level vs change | 300.8-330.1 | S070-S077 | Zillow = level + change, BLS = change only | Two-column card "Level / Change"; the renter looks at bill | BLS, Zillow | none | V |
| D4 what we checked | 330.6-387.5 | S078-S090 | no evidence it lags; 2.8 vs 2.7; Oct +0.2 vs flat; no Oct 12-month BLS | Three numbered cards; BLS Nov release screenshot with the "did not collect Oct 2025" note highlighted | BLS cpi_11102026, notice 12m-changes-202610 | highlight the note | C-16..19 V |
| F close | 388.1-416.4 | S091-S099 | three questions, own lease, disclaimer, sources | Three question cards, the renter closes laptop, end card with source list | all | none | V; S099 "every number carries a source tag" only true if X blocks show no numbers |

## Per-beat standard fields (applied to every row above)
Transitions: hard cut or 6-frame dissolve between sequences, no flashy effects. Typography: one sans family, numbers 96 px bold, labels 36 px, source tags 24 px bottom-left. Audio: voice only, optional soft pad at -28 LUFS under; no music claim from reference. Sound: none from third parties.

## CHARACTER_SPEC (original, not Casual Finance; updated 2026-11-21 by owner direction: male renter replaces "Mara")
Fictional early-30s American male renter, no name. Side-parted dark curls, warm skin, olive overshirt, cream tee, dark jeans, white sneakers. Approved art (independent review, `codex_art/qa/INDEPENDENT_REVIEW_V1_RENT.md`): CH-MASTER = CH-P1 neutral (open-arm explaining), CH-P3 holding a blank bill, BG-ROOM, BG-TABLE; registered in `v1_assets/`. Style as delivered: ink outline with soft shading (more detail than the flat reference; accepted at review).
Available: front view only, closed mouth only (no lip sync), bill baked into the P3 sprite (cannot move or carry text). Not yet made: thinking, pointing, relieved poses, mouth-open variants, 3/4 views, separable bill/hand layers. Pose rows elsewhere in this file that name those poses stay open until drawn; use P1/P3 swaps meanwhile.

## Representative test segment
0.0-74.3 s (A + B1 + B2): contains character (P1,P3 swaps), original source-labelled charts (no screenshots captured), two charts (2.8/2.7 bars, shelter stack), exact audio sync. Render 1920x1080 30 fps to out/test_segment_A_B.mp4, then QA.

## Open issues
1. Blocks C2, D1, D2 hold unverified claims. Owner: cut 122.7-139.9, 140.7-163.8 and 198.2-228.9 or re-record with sourced figures.
2. S099 claim "every number carries a source tag" conflicts with them.
3. Zillow screenshots need owner capture (403).
