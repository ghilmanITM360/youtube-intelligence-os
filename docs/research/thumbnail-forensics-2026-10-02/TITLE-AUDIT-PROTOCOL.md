# Title audit protocol (analyst layer)

The analyst reads each title **blind**: only title text, channel name, niche label and format. Views, ranks, performance classes, thumbnails and programmatic labels are deliberately withheld so the judgement cannot be anchored by outcomes.

The result is `ANALYST_TITLE_DIAGNOSTIC_SCORE` (0-100). It is an analyst's diagnostic of title craft. It is **not** a CTR prediction, view prediction, virality score or algorithm score. Content is not checked: `content_promise_verified` is always `NOT_CHECKED`; overpromise is flagged only relative to what the title itself claims.

## Row fields (one JSON object per title, same order as input)
- `Video_ID` (exact), `seq`
- `core_topic` (<=8 words), `exact_promise` (<=16 words, what the title promises the viewer gets), `intended_viewer` (<=8 words, visible from the title only)
- `unanswered_question` (<=14 words, the question the title leaves open, or "NONE")
- `tells_too_much` / `tells_too_little`: `Y`/`N`
- `mechanism_reliance`: list from `FEAR`, `AUTHORITY`, `CURIOSITY`, `URGENCY`, `HOPE`, `SPECIFICITY`, `SOCIAL_PROOF`, `NOVELTY`, `NONE`
- `orientation`: `SEARCH`, `BROWSE`, `MIXED`
- `unnecessary_words`: list of the words/phrases that could be cut (empty list if none)
- `overpromise_risk`: `LOW`/`MEDIUM`/`HIGH`; `overpromise_note`: "" or one short reason (e.g. absolute claim, cure/reversal language, guaranteed outcome)
- `medical_title_flag`: `NOT_HEALTH` / `MEDICAL_PACKAGING_SAFE` / `NEEDS_CONTEXT` / `MISLEADING_RISK` / `UNRESOLVED` (packaging flag from the title alone; never "contradicted" because content is not read)
- `improvement`: ONE testable edit (hypothesis) of <=18 words; make it concrete (new wording), not "be more specific"
- Scores (integers) and `score_100` = exact sum:
  - `clarity_score` 0-20: is the topic and value understood in one read?
  - `specificity_score` 0-15: concrete nouns, numbers, named things, defined audience
  - `curiosity_score` 0-20: open loop or tension the viewer wants closed (without being a bait-and-switch)
  - `promise_strength_score` 0-15: size/desirability of the payoff for the target viewer
  - `credibility_score` 0-15: plausible, not exaggerated, no absolute/miracle claims
  - `audience_fit_score` 0-10: clearly aimed at a defined viewer
  - `concision_score` 0-5: no filler; right length
- `confidence`: `HIGH`/`MEDIUM`/`LOW`
- `qa_status`: `NOT_SAMPLED`

## Rules
- Judge only the title. Do not guess what the video contains. Do not use outside knowledge of how the video performed.
- Use the full range. A component at 40-60% of max is ordinary; 80%+ needs a reason visible in the words; <30% needs a visible defect. Do not give most titles similar totals.
- Wording must differ between rows: no repeated `improvement` text, no boilerplate.
- `credibility_score` rates plausibility of the claim wording, not truth.
- Health titles: flag instant-cure, reversal, "clear arteries", guaranteed prevention, diagnosis-from-symptom, medication ambiguity, unsupported authority or fear exaggeration under `overpromise_note`/`medical_title_flag`.
