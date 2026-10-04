# Package audit protocol (title + thumbnail as one unit)

A package audit is run only for videos whose thumbnail audit is already verified (audited and passed QA). The reviewer reads the **title**, opens the **native thumbnail image**, and has the thumbnail audit row and the (QA-corrected) blind title audit row as context. **Views, performance classes, percentiles and ranks are withheld** so the judgement cannot be anchored by outcomes.

`EXPERT_PACKAGING_DIAGNOSTIC_SCORE` (0-100) is an analyst's diagnostic of how well title and thumbnail work together. It is **not** a CTR prediction, expected-views estimate, virality score or algorithm score. `TITLE_SCORE` (ANALYST_TITLE_DIAGNOSTIC_SCORE), `THUMBNAIL_SCORE` (EXPERT_VISUAL_DIAGNOSTIC_SCORE), `PACKAGE_SCORE` (this) and `PERFORMANCE_CLASS` are four separate fields. Do not average the first two to get the package score: the package score must reflect the interaction (what one adds to the other). Content is not checked: `content_promise_verified` is always `NOT_CHECKED`.

Thumbnails marked `CURRENT_PUBLIC_ONLY` are the creative visible today, not proof of what viewers saw when old views were earned.

## Row fields (one JSON object per package, same order as input)
- `Package_ID`, `Video_ID`, `Thumbnail_ID`, `seq`, `batch_id`
- `title_says` (<=20 words: what the title alone communicates), `thumbnail_says` (<=20 words: what the image alone communicates, text + visual)
- `shared_information`, `title_only_information`, `thumbnail_only_information` (<=20 words each; "NONE" allowed)
- `unanswered_question` (<=16 words, the open question the package creates, or "NONE"), `package_promise` (<=20 words), `viewer_expectation` (<=20 words: what a viewer would expect to get after clicking)
- `relationships`: non-empty list from `COMPLEMENTARY, REINFORCING, REDUNDANT, CURIOSITY_GAP, THUMBNAIL_EXTENDS_TITLE, TITLE_EXPLAINS_THUMBNAIL, CONTRADICTORY, THUMBNAIL_OVERPROMISE, TITLE_OVERPROMISE, DISCONNECTED, UNCLEAR`; `primary_relationship` must be one of them. Multiple labels only when justified; do not force one.
- Y/N judgements: `thumbnail_repeats_title`, `thumbnail_adds_curiosity`, `title_explains_what_thumbnail_cannot`, `image_reveals_answer_too_early`, `unnecessary_duplication`, `contradiction`, `thumbnail_escalates_beyond_title`, `title_escalates_beyond_thumbnail`
- `one_second_comprehension` YES/PARTIAL/NO (would a phone viewer grasp the topic in about a second), `credible` YES/PARTIAL/NO, `misleading_risk` LOW/MEDIUM/HIGH (packaging only), `fits_target_audience` YES/PARTIAL/NO
- Scores (integers; `score_100` = exact sum): `title_clarity` 0-10, `title_curiosity_specificity` 0-10, `thumbnail_visual_proposition` 0-10, `thumbnail_hierarchy` 0-10, `title_thumbnail_complementarity` 0-15, `one_second_comprehension_score` 0-10, `curiosity_gap` 0-10, `credibility` 0-10, `mobile_viability` 0-5, `distinctiveness` 0-5, `promise_alignment` 0-5
- `strongest_element`, `weakest_element` (<=20 words each), `improvement` (ONE testable package-level edit, <=24 words; a hypothesis)
- `medical_package_label`: `NOT_HEALTH / MEDICAL_PACKAGING_SAFE / NEEDS_CONTEXT / MISLEADING_RISK / UNRESOLVED` (title + thumbnail together; never CONTRADICTED_BY_CONTENT because content is not read)
- `medical_escalation`: `NONE / TITLE_MODERATE_THUMBNAIL_EXTREME / TITLE_EXTREME_THUMBNAIL_NEUTRAL / BOTH_EXTREME / BOTH_MODERATE` (NONE for non-health); `content_verification_queue`: `Y/N` (Y when the package makes a diagnosis, cure, reversal or fear claim that content would need to support)
- `confidence` HIGH/MEDIUM/LOW; `content_promise_verified` = `NOT_CHECKED`; `evidence_labels` = "title_says,thumbnail_says=DATA; relationships and scores=INFERENCE; improvement=HYPOTHESIS"; `qa_status` = `NOT_SAMPLED`

## Rules
- Every sentence must refer to this package's actual words and imagery. No boilerplate; wording must differ between rows; no repeated `improvement`.
- Use the full range. 40-60% of a component's max is ordinary; 80%+ needs a reason visible in the package; <30% needs a visible defect.
- A package where the thumbnail merely repeats the title scores low on `title_thumbnail_complementarity` and `curiosity_gap` even if both halves are individually good.
- `one_second_comprehension` YES requires that the topic survives at 160x90 (use the thumbnail audit's `mobile_readability_160` as evidence, but judge the package).
- `thumbnail_escalates_beyond_title` / `title_escalates_beyond_thumbnail` mean one half makes a bigger claim than the other; `THUMBNAIL_OVERPROMISE` / `TITLE_OVERPROMISE` mean the bigger claim is hard to credit.
- Do not state that a package causes clicks, views or retention.
