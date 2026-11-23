# 18 READINESS SCORECARD — CH001 (self-scored, NOT independently reviewed; diagnostic only)
weighted = max x score/5. Honest re-score after files 14/15/17 written; replaces the earlier provisional 62/100, which over-credited one-video evidence.
| Dimension | Max | Score 0-5 | Points | Evidence / why not higher |
|---|---:|---:|---:|---|
| Representative video and shot coverage | 15 | 2 | 6 | 1 of 15 deep videos measured; 4 selected + 2 holdouts not analysed |
| Visual design system | 15 | 3 | 9 | palette/typography measured on one video |
| Asset reconstruction readiness | 15 | 3 | 9 | original art for core assets; third-party stand-ins, bedroom clutter, banknote art partial |
| Animation reconstruction readiness | 15 | 3 | 9 | timings measured for ~40 states (E24-E38) |
| Camera, depth and lighting | 10 | 2 | 4 | static frame, flat; limited evidence |
| Editing, audio-time alignment, finishing | 10 | 2 | 4 | caption timing matched (F1 0.917); renders silent |
| Visual decision-engine generalization | 10 | 2 | 4 | file 14 from one video |
| Executed independent reproduction validation | 10 | 2 | 4 | same-video rendered (v14) but gate not passed; novel scenes prototype-only; no independent review |
| **TOTAL** | 100 | | **49** | band: 0-59 insufficient |
Uncertainty: +-8. No path to 85 without the 4 selected videos, a second novel-scene round, and an independent reviewer.

## Addendum 2026-11-20 (T1 multi-video pass, file 21)
Score stays **49/100**. Holdout test was executed (first real generalisation evidence): bg/band rules PASS 2/2, caption rule FAIL 0/2, pacing FAIL. Coverage +0 (numeric only, no shot data); decision engine 4 -> 3 (caption and pacing rules were over-generalised); validation 4 -> 5 (a real holdout prediction test now exists). Net 49. Caption/pacing rules in 14/13 are family-conditional hypotheses.

## Addendum 2026-11-20 (novel round 2)
Executed family-conditional novel tests (structure transfers, pacing does not). Decision engine 3 -> 4, validation 5 -> 6. **Total 51/100**, band still insufficient (0-59). Gap to 85: coverage (6/15, no shot-level data for 6 other videos), assets/animation (no new families built), camera and audio (not measured), same-video gate and independent review (not met). 90 cannot be reached by re-scoring; each point needs executed work, and the review gate needs a subagent only the user can request.

## Addendum 2026-11-20 (T3 33NV)
Coverage 6 -> 7 (one more video has per-state measurements and a new panel-fill family identified). Total **52/100**, NO-GO unchanged. The new family has no reconstruction test, so assets/animation are not credited.

## Addendum 2026-11-20 (T3 on 4 more videos)
Coverage 7 -> 8 (per-state data for 6 videos, >=3 families identified, but no shot blueprints/reconstruction for them). Visual design system 9 -> 9 (palette recurrences noted, roles unverified). Total **53/100**, NO-GO. Hard ceiling logic: with families B/C unrebuilt, assets/animation/camera cannot be credited above current.

## Addendum 2026-11-20 (NS5 family B)
Animation 9 -> 9 (proxy only). Validation 6 -> 7 (second family exercised with executed novel render). Total **54/100**, NO-GO. Family C and D untested; metric-tuned results are not independent evidence.

**Correction (gate.py audit):** NS5 +1 credit withdrawn - panel area was ~10x the reference and dark-ink share still FAILS after shrinking. Validation 7 -> 6. **Total 53/100**, NO-GO.

## Addendum 2026-11-20 (visual QA round)
Evidence quality improved, no dimension moves a full point: same-video worst shot F1 0.62 -> 0.74 and median 0.879 -> 0.902 (dil1), but the same-video VISUAL gate is not passed and only 5 of 22 shots were re-inspected by eye. NS5/NS6 credit stays void; NS5_v2/NS6_v2 are grammar-level partials (NS6_v2 pacing fails). Family taxonomy corrected (see 21). Independent visual review still not done (needs a user-requested subagent). **Total 53/100, NO-GO.**

## Addendum 2026-11-20 (v25, independent review #1)
Same-video pixel F1 (dil1,6fps) median 0.95 / min 0.83, BUT independent visual review (on v19) = 6/16/2 PASS/PARTIAL/FAIL and NS tests fail same-channel. Score kept at 53/100 NO-GO: metric rise came from caption text (OCR) and does not equal visual pass; reviewer must re-run on v25 before any increase.
