# Revision 1 Self-Audit

PASS / CONCERN / FAIL per item. No numerical scores. Not an argument that the
revision is good — an attempt to say where it is weak.

## Process integrity

| Item | Verdict | Note |
|---|---|---|
| Blind first pass preserved unmodified | **PASS** | All 18 locked SHA-256 hashes verified before the review began and again after it finished. Every one matches `FIRST_PASS_LOCK.md`. |
| Nothing written inside the frozen release | **PASS** | Read-only access only. `validate_brain.py` re-run after this revision: PASS, zero failures. |
| All revision output confined to `revision_1/` | **PASS** | 18 new files. No first-pass file was touched. |
| v1.0.0 metadata inconsistency not fixed in place | **PASS** | Recorded in `RELEASE_METADATA_ISSUE.md` and scoped to a future v1.0.1. |
| Script unaltered | **PASS** | 130 words, verbatim, hash unchanged. No rewriting, no hook improvement, no added narration. |
| No blind-test contamination | **PASS** | No xkcd or "what if" videos, screenshots, thumbnails or style references were browsed. No web search of any kind was performed during this revision. All grammar came from the frozen brain's canonical rows. |
| Web research limited to its permitted purpose | **PASS** | None performed in this revision. The first pass's single domain-restricted medical search is carried forward as a guardrail only and is labelled as such wherever it influences a decision. |
| Corpus baseline recomputed from canonical rows, not prose | **PASS** | `CORPUS_DENSITY_BASELINE.md` is built from `01_master_data/*.csv`. Prose DNA summaries were used for cross-reference only. |
| No arbitrary target count set | **PASS** | No count was decided in advance. Two items were kept *against* the first pass's own cut suggestions; the counts fell out of the audit. |
| Every state and every motion reviewed individually | **PASS** | `STATE_REVIEW.csv` 22 rows, `MOTION_REVIEW.csv` 17 rows. Full coverage, all required columns. |
| Referential integrity across revised outputs | **PASS** | Cross-checked state→shot, state→base image, state→asset, state→motion, motion→shot, motion→source/target state, base image→state, shot→state/motion counts, text→asset/state. `FK/ORPHAN ERRORS = 0`. Shot word counts total 130. |

## Grammar conformance

| Item | Verdict | Note |
|---|---|---|
| Camera locked everywhere | **PASS** | Zero moves. Every well-formed `CAMERA_STATE` row across 581 states is LOCKED/STATIC family. |
| Hard cuts only | **PASS** | Four boundaries, all hard. Zero fades, matching 186 measured corpus boundaries. |
| One-frame change dominance | **PASS** | 14 of 15 motions are one frame; the fifteenth is four frames. The corpus's most common portrait SPEED value is literally `ONE-FRAME CHANGE`. |
| Word-onset anchoring | **PASS** | All 19 anchors are word onsets. No offset padding added, correctly — the measured median offset of 37 ms is inside one frame. |
| Strike duration | **PASS** (was CONCERN) | Retimed to 4 frames against a measured corpus range of 0.125–0.208s. |
| Curved arrows treated as the corpus treats them | **PASS** (was FAIL) | Group reveals, not traced paths. |
| Asset format grammar | **PASS** | One opaque full-frame environment; every character, object and graphic a transparent PNG overlay; all text native editor layers. |
| Asset TYPE vocabulary | **PASS** (was CONCERN) | Five invented type names replaced with the corpus's own. |
| No generated text | **PASS** | Not one image prompt asks for a letter. Every prompt carries an explicit "Do NOT include … any text". |
| Base image economy | **PASS** | Five plates for 20 states, 3–5 states per plate. |
| Motion restraint | **PASS** | Five states have no motion. The longest single moment is a 4.3s ESTIMATED locked hold with nothing moving. |
| No copying of training scenes | **PASS** | No composition reproduces a corpus shot. The transfer is of rules, not images. |
| No absolute timestamps | **PASS** | Every timing value carries ESTIMATED and derives from one stated rate. No estimate is mixed with a measured value, because no measured values exist yet. |
| **Cross-shot base image reuse** | **CONCERN** | Still zero. Each of the five plates serves one shot only. Reuse happens at asset level — the mug in four shots, Dr. Rehan in three, the heart in two — which is defensible, since the five compositions genuinely differ. But a reviewer could reasonably argue SH01 and SH03 should share a plate, and the revision did not revisit that call. |
| **Per-shot reveal rate in SH01 and SH05** | **CONCERN** | SH01 runs an estimated 1.16 states/sec and SH05 0.82, against a portrait p90 of 0.67. Both are driven by the script's own word density and every state fires on a distinct concept word, so no cut was made. This is the most likely point of reasonable disagreement in the plan. |

## Medical guardrails

| Item | Verdict | Note |
|---|---|---|
| No overclaim on the energy-drink comparison | **PASS** | One muted-red triangle over one object. No skull, death icon, exploding heart, flatline, poison mark, red emergency field or colour wash anywhere. |
| No new medical claims in visuals | **PASS** (strengthened) | No numbers, thresholds, doses, millilitres, cup counts, diagnoses, disease labels or ECG tracings. The gauge icon was removed precisely because a needle-on-dial implies a reading and a tick implies a threshold. |
| Coffee not depicted as universally good or bad | **PASS** | The plan's structure is the argument: install the binary, mark it wrong, delete it, replace it with body-response-in-context. |
| Response arcs carry no measurement | **PASS** | Unlabelled, uncalibrated, no scale, no trace. They count; they do not measure. |
| Dr. Rehan is not a likeness | **PASS** | Simplified stick figure with three cues. No photorealism, no facial identity, no coat or stethoscope. |
| Energy drink unbranded | **PASS** | Blank sides, no logo or lettering; the prompt states it must not resemble any real product. |
| Guardrail decisions labelled separately from brain decisions | **PASS** | Every guardrail-driven choice is marked `MEDICAL GUARDRAIL (not brain-derived)` in the CSVs and called out in the plan's guardrail section. |

## Evidence quality

| Item | Verdict | Note |
|---|---|---|
| **No CTA precedent anywhere in the corpus** | **CONCERN** | Confirmed by direct lookup: none of the 14 source videos ends on a call to action. R05.4 and M15 are therefore grammar transfers with no evidenced content, and their confidence stays MEDIUM. The script demands a CTA, so it cannot simply be dropped. |
| **The doctor / patient / consultation staging is unprecedented** | **CONCERN** | No corpus video is medical or interpersonal in this way. The stick-figure construction and one-frame character entry are precedented; the situation is not. |
| **The three-item factor list edges toward an infographic template** | **CONCERN** | Three outlined plates with a connector spine and text is the plan's most template-like layout, and removing the gauge icon did not change that. Corpus boxed-heading and caption-plate layouts are the nearest precedent and they are not a strong match. The alternative — drop the remaining two icons for symmetry and make it three text plates — would be *more* template-like, not less, which is why it was not applied. |
| Response arcs as a body-reading metaphor | **CONCERN** | Invented for this script. No corpus analogue for "a reading at a body". The mechanism (countable repetition of a small mark) is precedented; the meaning is not. |
| Stimulation strokes as a caffeine metaphor | **PASS** | Countable repetition of an identical mark is directly the corpus's quantity idiom, and the two/four grouping does the comparison without a number. |
| Caution triangle | **PASS** (was CONCERN) | Precedent located in three videos. The muted-red colour remains a stated departure from the corpus's black. |

## Honesty checks

| Item | Verdict | Note |
|---|---|---|
| First-pass errors named rather than quietly fixed | **PASS** | Six corrected claims tabulated in `REVISION_1_CHANGELOG.md`, including one where the first pass's own self-audit reasoning was wrong (its density comparator) and two where its suggested cuts were rejected. |
| Changes attributed to evidence, not preference | **PASS** | Every KEEP/MERGE/REMOVE/MODIFY row carries a `BRAIN_EVIDENCE` value pointing at canonical rows or a labelled guardrail. |
| Reviewer's alternatives stated where a judgement call was made | **PASS** | The all-text-plates alternative for SH05, the SH01/SH03 shared-plate question, and the consistency mitigations for the five plates and the mug are all named and left unapplied. |
| Not claiming success | **PASS** | No statement anywhere that the brain generalises. That conclusion is the human reviewer's, on this evidence. |
| Residual risks stated | **PASS** | Five listed in `EXECUTABILITY_CHECK.md`, including two — generation consistency across five plates, and the mug at four scales — that have no applied mitigation. |

## No FAIL verdicts

The two first-pass items that would have earned FAIL — the curved path-following
draws, which had no deterministic implementation, and the two-identical-figures
generation dependency — are both resolved. The remaining weaknesses are the six
CONCERNs above, four of which are evidence-availability problems that no
revision of this plan can fix: the corpus contains no medical video, no
consultation, no body-reading metaphor and no CTA. Those four are properties of
the test, not defects in the plan, and they are exactly what a
different-niche generalisation test is supposed to expose.
