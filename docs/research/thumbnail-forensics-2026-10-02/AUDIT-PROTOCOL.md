# Thumbnail audit protocol (B002+)

Every audited thumbnail gets one JSON row after the reviewer has opened the **native image**, the **320x180** render and the **160x90** render (batch sheets). Rows are image-specific: sentences must name things actually visible in that image. Boilerplate that could be pasted onto another thumbnail is a defect.

## Evidence rules
- Facts = what is visible (text, objects, colours, layout). Interpretation fields are labelled analyst judgement. Never state that a thumbnail causes clicks, views or retention.
- Never identify a real person from appearance. A name printed on the image may be quoted as visible text only.
- Only say an image looks AI-generated or composited when a concrete artefact is visible (extra fingers, melted text, inconsistent shadows, mismatched lighting). Smooth rendering alone is not evidence.
- `scan` is `ANALYST_VISUAL_HEURISTIC` – never eye-tracking.
- Content fulfilment (does the video deliver the thumbnail promise?) is `NOT_CHECKED` unless transcript/content was actually read.
- Current-public thumbnails (`CURRENT_PUBLIC_ONLY`) are not evidence about what the creative was when old views were earned.
- Objective features supplied in the batch input are measurements/proxies. Do not copy them as psychology.

## Fields
Narrative (one to three specific sentences each, no padding):
- `text` – exact visible words, top-to-bottom, separated by " / "; badge/logo text in brackets; `NONE` if no text.
- `scene` (A) – people/faces/expression/gaze/gesture, objects, symbols, medical visuals, background, arrows, comparison elements, visual story.
- `composition` (C) – primary and secondary focal point, subject scale, cropping, negative space, hierarchy, symmetry/thirds, diagonal/leading lines, arrow role, separation, clutter.
- `typography` (D) – word count and hierarchy, placement, contrast, density, what survives at 160x90, redundancy with the title, information the title lacks.
- `colors` (E) – dominant/accent palette, saturation/brightness/contrast, subject separation, semantic colour use.
- `psychology` (F) – visible expression, gaze, pose and authority/trust/fear/hope/urgency/vulnerability cues. Visible signals only.
- `partnership` (G) – title promise vs thumbnail promise, duplicated vs added information, unanswered question, escalation, contradiction, reveal-too-much risk.
- `scan` (H) – likely scan order, prefixed `ANALYST_VISUAL_HEURISTIC:`.
- `art` (I) – perspective, lighting, cutout/compositing quality, realism, anatomy/object coherence, artefacts (only with evidence), background complexity, mobile survival.
- `strength`, `weakness`, `bottleneck` (J) – one specific line each.
- `action` (J) – ONE concrete corrective action (a testable change, not a platitude). Labelled hypothesis.
- `counterexample` – a Thumbnail_ID / Seq from this batch that does the opposite well or badly, with why; or `NONE_IN_BATCH`.
- `mechanism` – prose for B; `mechanism_primary` – one enum value; `mechanism_secondary` – free text or "".

Structured tags (enums validated by `validate_audit_batch.py`): `word_count`, `people_count_visible`, `face_visible` Y/N, `face_scale` NONE/SMALL/MEDIUM/LARGE, `expression_label` (short free text or NONE), `hero_object` (short free text or NONE), `arrow_present`, `before_after`, `numbers_in_text`, `age_marker`, `warning_color_used` (Y/N), `text_density` NONE/LOW/MEDIUM/HIGH, `mobile_readability_160` PASS/PARTIAL/FAIL, `hierarchy_clear` Y/N, `background_complexity` LOW/MEDIUM/HIGH, `art_style` PHOTO/ILLUSTRATED_CARTOON/STICK_FIGURE/THREE_D_RENDER/AI_STYLE_ILLUSTRATION/SCREENSHOT_OR_DOCUMENT/MIXED/OTHER, `title_relation` DUPLICATES/COMPLEMENTS/ESCALATES/CONTRADICTS/UNRELATED, `reveal_too_much_risk` LOW/MEDIUM/HIGH, `confidence` HIGH/MEDIUM/LOW.

Health safety: `medical_label` NOT_HEALTH / MEDICAL_PACKAGING_SAFE / NEEDS_CONTEXT / MISLEADING_RISK / CONTRADICTED_BY_CONTENT / UNRESOLVED; `medical_flags` list from INSTANT_CURE, REVERSAL, DIAGNOSIS, MEDICATION_AMBIGUITY, UNSUPPORTED_TREATMENT, FEAR_EXAGGERATION, MISLEADING_SYMPTOM_IMAGERY, CREDENTIAL_AMBIGUITY, TITLE_THUMBNAIL_CONTRADICTION (empty list if none); `medical_notes` one sentence (or ""). Use `NOT_HEALTH` for non-medical topics. Content contradiction cannot be asserted without content evidence; use `NEEDS_CONTEXT`/`UNRESOLVED`.

`content_promise_verified`: `NOT_CHECKED` unless content evidence was read. `evidence_labels`: `text,scene=DATA; diagnostic fields and scores=INFERENCE; proposed changes=HYPOTHESIS`.

## EXPERT_VISUAL_DIAGNOSTIC_SCORE (not a CTR prediction)
Integer components, `score_100` = their exact sum:
`story_score` 0-15 (clear visual proposition) · `psychological_hook_score` 0-15 · `title_partnership_score` 0-15 · `hierarchy_score` 0-10 · `mobile_readability_score` 0-10 · `composition_score` 0-10 · `emotion_subject_alignment_score` 0-10 · `credibility_score` 0-10 · `distinctiveness_score` 0-5.
Use the full range. Typical scale: a component at 40-60% of its maximum is ordinary; 80%+ must be earned by a visible reason; <30% requires a visible defect. Do not give every thumbnail similar totals. `credibility_score` rates visible production/claim plausibility cues, not factual truth.
