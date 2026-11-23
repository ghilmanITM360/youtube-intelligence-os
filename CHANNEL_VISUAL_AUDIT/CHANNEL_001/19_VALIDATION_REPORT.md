# 19 VALIDATION REPORT — CH001
## Same-video test: 10nEByVLya0 (55.4 s, 1660 frames, silent), numeric metrics at 270x480 gray
| Ver | Content F1 | Caption F1 | Full-slice IoU med/mean | Rows-only IoU med/mean |
|---|---|---|---|---|
| v7 | 0.806 | 0.858 | 0.776 / 0.700 | 0.930 / 0.789 |
| v10 | 0.821 | 0.858 | 0.866 / 0.770 | 0.970 / 0.937 |
| v12 | 0.823 | 0.858 | 0.886 / 0.780 | 0.974 / 0.953 |
| v14 | 0.829 | 0.917 | 0.899 / 0.795 | 0.974 / 0.953 |
Caption ink agreement 0.951; ink density ratio 1.029.
Result: NOT PASSED. No pass thresholds were fixed in advance beyond the rulebook's qualitative checks; frame images were never viewed (tool cannot decode PNG), art fidelity of stand-ins/banknotes/bedroom is partial, audio not aligned. Open: S039, S017 (aliased, saturating), 11 ref-only / 16 rec-only caption events (+-3 frames).
## Novel-scene tests
NS1 (inflation, character) and NS2 (compound growth, chart): rendered 9 s each from original art with the measured grammar. Self-check only, evenly timed placeholder captions. Generalization claim: UNPROVEN.
## Independent review
Not done (requires a subagent the owner has not requested).

## Addendum 2026-11-20 — holdout and novel round 2
- Holdout prediction test executed (file 21): bg/band PASS 2/2, caption FAIL 0/2, pacing FAIL.
- Family-conditional novel scenes NS3/NS4 measured with the reference tools (NOVEL_SCENE_QA.md round 2): structure PASS, pacing FAIL.
- Same-video test remains NOT PASSED; independent review not done.
