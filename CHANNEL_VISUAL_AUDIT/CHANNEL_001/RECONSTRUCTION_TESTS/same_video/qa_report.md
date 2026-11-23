# Same-video reconstruction QA: CasuallyFinance 10nEByVLya0 (rulebook sec. 19)
Reference: ~/workprojects/videos in mp3/CasuallyFinance/The IPO Boom Is the Danger Sign [10nEByVLya0].mp4, 55.40 s, 1080x1920, 30 fps, 1,662 frames. Timing sources: visual_states.csv (61 states), caption_event_ledger.csv (190 events), local ASR (whisper small.en word times, ASR_UNCERTIFIED; no human listening). Audio was not mixed into the render; the render is silent.
Reconstruction: `render_10nEByVLya0.py` (PIL primitives, original art, 2x supersampled band, 1,660 frames). No source pixels are read. Outputs: `../../RENDERED_OUTPUTS/recreation_10nEByVLya0_v1.mp4`, `_v2.mp4`.

## Objective metrics (compare_metrics.py, 270x480 grey, whole video)
| Metric | v1 | v2 |
|---|---:|---:|
| Content-change event F1 (tol 2 frames) | 0.777 | 0.779 |
| Caption-change event F1 (tol 2 frames) | 0.622 | 0.855 |
| Caption ink presence agreement | 0.849 | 0.916 |
| Content bbox IoU median | 0.615 | 0.602 |
Content timing is reproduced well because it is driven by the measured state boundaries; this is expected, not proof of understanding. Caption event timing improved after using the measured caption event frames. Shape fidelity (bbox IoU about 0.6) is mediocre and did not improve; the figure redraw in v2 was not better.

## Visual review (22 shot mid-frames, side-by-side sheets in comparison/)
Layout, canvas colour, caption band position, question-mark row, dollar/bubble, timeline arrows, calendar and speech-bubble placement are close. Large mismatches remain: see visual_error_log.csv (E1-E10). Biggest: stand-in art for all third-party media, stick-man proportions, bedroom/newborn scenes, Earth and candlestick chart.

## Verdict for this gate: NOT PASSED (v2)
Reasons: significant visible mismatches in about half of the shots; third-party regions unmatched by design; only objective frame-metrics and my own visual review, no independent review; silent render; v2 not re-inspected after the figure redraw regressed. Next: measure proportions, fix E2/E3/E4/E6, re-render v3, re-run metrics.

## v3 addendum (2026-11-20) — gate still NOT PASSED
Changes: black-hair stick man rebuilt from pixel measurements on ref f525 (E2 partial); caption block repositioned and word-reveal layout (E6 partial). Render: `render_10nEByVLya0_v3.py` -> `RENDERED_OUTPUTS/recreation_10nEByVLya0_v3.mp4` (1,660 frames). Metrics (`comparison/metrics_v3.json`): content event F1 0.779, caption event F1 0.855, content bbox IoU median 0.602 (v2 0.602) — no metric gain; the figure fix is visible in the crop `comparison/crop_f525_ref_vs_v3.png` but not in these aggregate metrics.
New finding E12: caption layout in the ref is not centred per chunk and shows longer accumulating text; recon captions are too short in 13 of 21 ref frames. Rule fit failed (fit_caption_blocks.py). E3, E4, E7, E8, E9 not touched in v3.

## v4 addendum (2026-11-20) — gate still NOT PASSED
Caption chunk rule read from the 22 ref frames (text read visually, widths measured): a chunk starts after a punctuation-ended ASR word; words appear left-to-right; the full chunk is centred (x~531); wrap at ~800 px, max 2 lines, then a new chunk. Implemented in `render_10nEByVLya0_v4.py` -> `RENDERED_OUTPUTS/recreation_10nEByVLya0_v4.mp4`. Caption ink vs ref at 22 frames: median |left-edge error| 215 -> 28 px, median |width error| 194 -> 41 px (v3 -> v4); 20/22 within 60 px. Metrics (`comparison/metrics_v4.json`): content bbox IoU median 0.602 -> 0.685, caption event F1 0.858, content event F1 0.780, caption ink agreement 0.916. E12 largely resolved; E5 wording (ASR vs shown text) still unverified. Not fixed: E3, E4, E7, E8, E9, E1. No independent review; render still silent.

## v5 addendum (2026-11-20)
Render: RENDERED_OUTPUTS/recreation_10nEByVLya0_v5.mp4 (1660 frames, silent). Changes, all from measured ref crops (original art, no source pixels):
- E3: brown man re-measured (f345/f270): head rx80, scribbled hair cap, asymmetric arms; slides 525->232 over S014; Earth lands f312-319 at (700,965) r222 (timing error found: v4 showed Earth too early).
- E4: years now Menlo-like monoline (~95 px).
- E7: bedroom (SH013) and swaddle close-up (SH014) redrawn from measured layout; portrait is a generic original face (E1 stand-in).
- E8: 119 candle bodies extracted from ref f1212 (extract_candles.py -> candles.json) and drawn in own style; arrow path, "90%" label and worried face repositioned from measurements.
- E9: burning Earth redrawn (centre (528,980) r368, spiral eyes, flames alternate every 10 frames).
Metrics v4 -> v5: content bbox IoU median 0.685 -> 0.728 (mean 0.617 -> 0.664); content event F1 0.78 -> 0.776 (flat); caption unchanged (0.858 / 0.916); ink density ratio 0.946.
Gate: still NOT PASSED. Remaining: E1 stand-ins, E2 residual, E5 wording, bedroom clutter (bubble/pillows), SH006/SH007/SH016-17/SH021 not re-inspected, no audio timing, no independent review, second novel-scene test not run.

## v6 addendum (2026-11-20)
- Rebuilt SH001-SH003 and SH006 from connected-component measurements of reference frames (E14-E17). v5 scrolled the ? row ~7x too fast (15.5 vs 2.3 px/frame); fixed. Render: RENDERED_OUTPUTS/recreation_10nEByVLya0_v6.mp4 (render_10nEByVLya0_v6.py).
- Metrics v5 -> v6 (comparison/metrics_v6.json): content event F1 0.776 -> 0.794; caption F1 0.858 (unchanged); bbox IoU median 0.728 -> 0.730 (mean 0.664 -> 0.673); ink-density ratio 0.946 -> 0.983.
- Gate status: NOT PASSED. Third-party stand-ins (E1), SH007 fire clip, bedroom clutter (E7), SH017 last-frame arrow, audio timing, independent review still open. Gains are small; the metrics are coarse (270x480 gray), so they do not prove visual equivalence.

## v7 addendum (2026-11-20)
- Redrew SH021 (table page, yellow sweep, check, skyline, bubble), fixed SH007 label position and bedroom overflow (E18-E20). Render: RENDERED_OUTPUTS/recreation_10nEByVLya0_v7.mp4 (render_10nEByVLya0_v7.py).
- Metrics v6 -> v7 (comparison/metrics_v7.json): bbox IoU median 0.730 -> 0.770 (mean 0.673 -> 0.700); content event F1 0.794 -> 0.763 (events 427 -> 499, a worse result: the linear page slide creates change events the reference does not have); caption F1 0.858 and ink agreement 0.916 unchanged; ink ratio 0.98.
- Mixed result: geometry better, event timing worse. Next try: make the page slide discrete (ref event timing) and re-measure. Gate still NOT PASSED.

### v7 final (page slide re-timed to ref: static to f1537, ease-out slide f1538-1549)
Metrics: content event F1 0.806 (435 vs 466 events), bbox IoU median 0.776 / mean 0.700, caption F1 0.858, caption ink agreement 0.916, ink ratio 0.98. Supersedes the 0.763 reading above; E18 now FIXED for timing. Gate still NOT PASSED (E1 stand-ins, SH017 arrow, audio, no independent review).

## v8 addendum (2026-11-20)
- Added a supplementary metric (rows y<1272 only) because caption ascenders bleed into the original content slice (ref and recon differ in caption line count at some frames). compare_metrics.py now reports both.
- v8 fixes E21/E22 (Blackstone/portraits/search card/logo slide-out) plus yacht money-bag positions. Render: recreation_10nEByVLya0_v8.mp4.
- Metrics v7 -> v8: bbox IoU median 0.776 -> 0.798 (mean 0.700 -> 0.727); no-caption-rows IoU median 0.930 -> 0.939, mean 0.789 -> 0.867; content event F1 0.806 -> 0.811; caption F1 0.858, ink agreement 0.916, ink ratio 0.988. Gate still NOT PASSED.

## v9 addendum (2026-11-20)
- Article scene (E23) re-laid from measurements. Render: recreation_10nEByVLya0_v9.mp4 (render_10nEByVLya0_v9.py).
- Metrics v8 -> v9: no-caption-rows IoU median 0.939 -> 0.954, mean 0.867 -> 0.882; full-slice IoU median 0.798, mean 0.727 -> 0.736; content event F1 0.811; caption F1 0.858; ink ratio 1.01. Gate still NOT PASSED.

## v10 addendum (E24-E31)
Metrics v10 (270x480 gray): content F1 0.821, caption F1 0.858, full-slice IoU median 0.866 / mean 0.770, no-caption-rows IoU median 0.970 / mean 0.937, ink ratio 1.034, caption ink agreement 0.916.
v9 -> v10: rows-only mean 0.882 -> 0.937, full-slice mean 0.736 -> 0.770.
Fixes: timeline scroll (S041/S042, S017), Earth cut-in, logo exit, candle labels, banknote spread, portrait text column, red tile layout. All numeric (bbox/column-run) verification only; frames not viewed.
Worst remaining (rank): S002 ? circles entry 0.84, S039 0.88, S010 bubble 0.90, S036 0.81, S057 0.82, S035 news page 0.55.
Gate status: same-video gate NOT passed; no independent review; GO FAILED (provisional 62/100).

## v11 addendum
E32 (S002 entry) and E33 (S035 page) fixed. Rows-only IoU mean 0.944 (v10 0.937), full-slice mean 0.774 (0.770), content F1 0.822 (0.821), caption F1 0.858 unchanged. Numeric verification only. GO still FAILED, provisional 62/100.

## v12 addendum
E34-E36 fixed. Rows-only IoU mean 0.953 (v11 0.944), full-slice mean 0.780, content F1 0.823, caption F1 0.858. Numeric only. Worst now S039 (0.88), S010, S017. GO still FAILED, provisional 62/100.

## v13 addendum
E37 patched (PARTIAL). No metric change: rows-only IoU mean 0.953, full-slice mean 0.779, content F1 0.823, caption F1 0.858. S039 and S017 (aliased timeline) are at the limit of bbox-level fixes; remaining gap needs per-note art measurement. GO still FAILED, provisional 62/100.

## v14 addendum
E38 caption event mapping fixed. Caption F1 0.917 (v13 0.858), caption ink agreement 0.951 (0.916), full-slice IoU mean 0.795 (0.779), content F1 0.829 (0.823), rows-only mean 0.953. Remaining caption residual: 11 ref-only / 16 rec-only events, mostly +-3 frame offsets. Numeric only. GO still FAILED, provisional 62/100.

## v15 + pixel-level metric (2026-11-20) — gate still NOT PASSED
New tools `MULTI_VIDEO_MEASUREMENTS/pixel_iou.py` and `shot_f1.py`: dilated ink-mask precision/recall F1 per frame and per shot (216x384, 6 fps). The earlier bbox IoU (median 0.974 no-caption rows) was saturated and overstated fidelity. v14 at dilation 2 / 1 / 0 (about 10 / 5 / 0 px at 1080 wide): median F1 0.914 / 0.879 / 0.798, mean 0.873 / 0.828 / 0.710, p10 0.769 / 0.686 / 0.476.
Worst shots at dilation 1: SH005 0.62 (year digits E4), SH020 0.68 (candles E8), SH016 0.74, SH022 0.74, SH011 0.74.
v15 hypothesis E39: SH016 excess ink (0.111 vs ref 0.082) comes from banknotes -> halved notes (10->5). Result: SH016 F1 0.74 -> 0.74, precision 0.64 -> 0.65: **hypothesis refuted**, excess ink is elsewhere (article/portrait region, rows 0.34-0.38 vs 0.19-0.26). Not fixable without viewing the frame; numeric-only workflow cannot localise it further. v15 render kept (metrics equal v14). Frame-level visual review and independent review are still required.

## v16-v19 VISUAL-led fixes (2026-11-20 evening) — first round with the pixels actually viewed
Image reading works for JPEG via the Read tool (PNG did not). Tools: `MULTI_VIDEO_MEASUREMENTS/cmp_frames.py` (ref | render | diff overlay JPEG), `contact_sheet.py`.
Process per defect: view ref vs render -> name visible difference -> measure it -> one change -> re-view -> metric as support.
| shot | what was visibly wrong | fix | F1 (dil1, 6 fps) before -> after |
|---|---|---|---|
| SH005 | slashed Menlo zeros, thin butt-cap arrow, uniform 40 px/frame scroll landing late | Courier+stroke digits, 20 px round-cap arrow, 80 px/distinct-frame scroll with 24fps dup pattern, measured arrow gaps | 0.62 -> 0.74 |
| SH020 | big chart labels, eased arrow, small low O-mouth face without hand | 6 px labels, linear arrow, measured face geometry | 0.68 -> 0.76 |
| SH016 | grey-bar article (2x ink), 128 px logo, 7 plain notes | tiny-serif article, 94 px logo, note shower | 0.74 -> 0.87 |
| SH011 | small boat card, 50 px bags | measured photo plate + 3 moneybags + lamp | 0.74 -> ~0.9 |
| SH022 | invented bar-chart/bubble layout | table text, black-hair man, stepped building, round bubble | 0.74 -> 0.78 |
Whole video v15 -> v19 (dil 1): median 0.879 -> 0.902, mean 0.829 -> 0.866, p10 0.687 -> 0.742; worst shot 0.62 -> 0.74.
Honest status: the same-video visual gate is still NOT PASSED. Third-party photos/clips are stand-ins; hand-drawn glyphs and several scribbles are approximations; only 5 of 22 shots were visually re-inspected; the other 17 were last judged by numbers.

## v20-v25 (after independent review #1 + implementation audit) 2026-11-20
- E42b dup-frame mask (v20): 16 segments, not only SH005. F1 effect ~0 (small), motion fidelity only.
- E43/E44 captions from ref OCR + Comic Sans MS regular 57 +1px stroke (v21-v23): whole-video dil1 F1 median 0.902 -> 0.95, mean 0.866 -> 0.948, p10 0.742 -> 0.91, min 0.74 -> 0.83 (SH022). SH003 0.81->0.95 SH004 0.83->0.95 SH005 0.74->0.92 SH020 0.76->0.95 SH016 0.87->0.91.
- LESSON: earlier art-only fixes were scored against caption text from ASR; much of the 'weak shot' F1 gap was captions. Metrics alone had hidden it; found by the independent reviewer.
- E45 bedroom rebuilt (v24-v25) SH013 0.90->0.93.
- Still open: SH022 (0.83, pointing man + row bands), Earth art (shots 5,19), chart art (1,2), shot 10 barcode, building tower; reviewer visual PASS/PARTIAL/FAIL not re-run on v25.
