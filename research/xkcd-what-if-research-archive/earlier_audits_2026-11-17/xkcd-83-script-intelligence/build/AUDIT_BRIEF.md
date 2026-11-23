# Script audit brief (xkcd "What If?" channel, transcript-only)

You audit YouTube scripts from TRANSCRIPT TEXT ONLY. You are not summarizing topics; you are reverse-engineering how each script is built. Read each assigned file in `transcripts/` fully (Read tool), then write one JSON file per video to `audits/<VID>.json` (e.g. `audits/V007.json`). Finish every assigned video; never write an audit for a transcript you did not read.

## Hard rules
- Transcripts have NO timestamps. Never invent time intervals, views, CTR, retention, visuals, music, edits, demographics. Audience effects are hypotheses: word them "may", "plausibly".
- Every field ending in `quote` must be an EXACT, case-sensitive, contiguous substring of the text after `TRANSCRIPT:` in the file (copy it; no ellipses, no paraphrase, no fixing typos, keep curly quotes/dashes as in the file). Keep quotes 4–30 words. A script will machine-check every quote; a non-matching quote fails the audit.
- Some captions are `auto_generated` (ASR, no punctuation, possible mis-hearings e.g. "[Music]"). Say so in `caveats` and lower confidence.
- Do not invent a CTA. If the transcript has none, `cta_present: false`.
- Shorts marked with a parent are EXCERPTS of a longer video in your batch. Audit them fully but compactly, and fill `excerpt_delta` by comparing against the parent transcript.
- Derive findings from the text. Do not force a category; use `OTHER:<name>` when the vocab does not fit.
- Plain English, concise: most string fields 1–2 sentences.

## JSON schema (all keys required; use null / [] when not supported)
```
{
 "vid": "V007", "youtube_id": "...", "title": "...", "format": "video|shorts", "parent_vid": null,
 "caption_type": "user_generated|auto_generated",
 "A_identity": {"core_topic","content_category","audience_inferred","primary_question","promise","style","pov"},
 "B_hook": {"opening_quote","hook_tags":[..],"construction","first_curiosity_trigger","conflict_or_contradiction","withheld","audience_expectation","promise_strength":"Strong|Medium|Weak","promise_strength_reason","opening_to_payoff","why_may_hold","weaknesses"},
 "C_opening_beats": [{"beat":1,"quote","info_introduced","question_active","unresolved","curiosity":"up|flat|down"}],   // 3-5 beats covering roughly the first 80-100 words; beats, not seconds
 "D_spine": {"stages":[{"stage":"Hook|Setup|Question|Tension|Escalation|Explanation|Reveal|Payoff|Conclusion","quote","summary","link_to_next"}],"inciting_question","central_problem","turning_points":[..],"climax","resolution"},
 "E_loops": {"loops":[{"id":"A","opening_quote","question","maintained_by","escalates":true,"partial_answer","resolution_quote":null,"status":"closed|partial|abandoned","replaced_by":null}],"loop_map":"A opens -> ..."},
 "F_mechanics": [{"technique","quote","construction","function","possible_audience_response","reuse"}],   // 4-8 strongest; fewer for very short shorts
 "G_emotion": {"mechanisms":[{"emotion","trigger_quote"}],"progression","strongest_beat_quote","emotion_information_relation"},
 "H_pacing": {"sentence_style","density","sequencing","transition_quotes":[..],"setup_to_payoff","slow_sections","redundancy","weaknesses","tempo":"Fast|Moderate|Slow|Variable","tempo_evidence"},
 "I_payoffs": [{"level":"micro|mini|major|reversal|ultimate","question_answered","quote","setup_amount","complete":true,"opens_new_question","fulfils_promise"}],
 "J_ending": {"closing_quote","ending_tags":[..],"final_insight","cta_present":false,"cta_quote":null,"cta_type":null,"earned":"yes|partly|no","earned_reason"},
 "K_assessment": {"strengths":[3],"improvements":[0-3],"distinctive_technique","biggest_risk","lesson"},   // strengths = observations; improvements = suggestions
 "L_formula": ["step 1", "..."],   // 4-8 steps derived from THIS script
 "lenses": {"architect","surgeon","viral","critic","curiosity","platform","integrator","tradeoffs"},   // one distinct finding each, no repetition; viral = most quotable line and why; platform = search-language in opening, standalone/Shorts-able segment
 "framework_rules": [{"rule_id","status":"MET|PARTLY|NOT_MET|EXCEPTION","evidence_quote","note"}],   // exactly these 8 rules, see below
 "matrix_row": {"topic","hook_type","narrative_structure","curiosity_mechanism","emotional_arc","key_payoff","cta","distinctive_technique","confidence":"High|Medium|Low|Speculative"},   // each <= 15 words
 "tags": {"structure_tag":"...","mechanics_tags":[..],"emotion_tags":[..],"answer_position":"FIRST_100_WORDS|MIDDLE|END|NEVER","number_density":"High|Medium|Low"},
 "excerpt_delta": null,   // shorts with parent: {"parent_segment":"where in parent it comes from","opening_change","ending_change","dropped","standalone_ok":"yes|partly|no","reason"}
 "confidence": "High|Medium|Low", "caveats": "..."
}
```

## Controlled vocab (multi-select where a list; add OTHER:<name> if needed)
- hook_tags: READER_QUESTION_ATTRIBUTION, COLD_QUESTION, IMMEDIATE_SHORT_ANSWER, DEADPAN_DOOM_VERDICT, ANSWER_WITH_TWIST, PREMISE_REFRAME, ASSUMPTION_SETTING, SUPERLATIVE_CLAIM, TEASE_LATER, CALLBACK_TO_PRIOR_VIDEO, DIRECT_ADDRESS_TO_ASKER, IDIOM_LITERALIZED, ABSURD_CONSEQUENCE, AUTHORITY, CONTRADICTION, MYSTERY, STORY, PROBLEM, PROMISE, EMOTIONAL, UNEXPECTED_FACT, DIRECT_CHALLENGE, SHOCK
- structure_tag (one): ESCALATION_LADDER (keeps scaling the premise up/down), CONSEQUENCE_TIMELINE (what happens next, step by step), ELIMINATION_SEARCH (candidates ruled out until the answer), ANSWER_FIRST_THEN_EXPLAIN, PREMISE_REFINEMENT (re-interprets the question in successive versions), FEASIBILITY_CALCULATION (can it work? run the numbers), CONCEPT_EXPLAINER, COMPILATION
- mechanics_tags: MINI_HOOK, CLIFFHANGER, DELAYED_REVEAL, QUESTION_STACKING, INFORMATION_GAP, FORESHADOWING, CALLBACK, CONTRAST, REVERSAL, SURPRISE, CONCRETE_EXAMPLE, ANALOGY, SCALE_COMPARISON, NARRATIVE_RESET, PROMISE_AND_PROOF, AUDIENCE_QUESTION, STRATEGIC_REPETITION, UNDERSTATEMENT, DEADPAN_HUMOR, EXPERT_OR_SOURCE_CITATION, SELF_CORRECTION, SECOND_PERSON_IMMERSION, PRECISE_NUMBER
- emotion_tags: CURIOSITY, AWE, SURPRISE, CONCERN, FEAR, HOPE, EMPATHY, HUMOR, RELIEF, INSPIRATION, SATISFACTION, SUSPENSE
- ending_tags: DEADPAN_PUNCHLINE, CALLBACK_TO_OPENING, CALLBACK_TO_ASKER, UNDERSTATEMENT, MOCK_PRACTICAL_ADVICE, AWE_IMAGE, ONE_LINE_MORAL, DIRECT_ANSWER_RESTATED, OPEN_ENDED, FINAL_ESCALATION, TRUNCATED_TRANSCRIPT, SUBSCRIBE_CTA, COMMENT_CTA, NEXT_VIDEO_CTA, PRODUCT_CTA

## framework_rules: assess exactly these (creative heuristics from the repo reference framework v1, NOT platform facts)
- FR-HOOK-01: hook = lean context -> scroll-stop beat -> contrarian snapback
- FR-INTRO-03: where the intro over-explains vs under-explains
- FR-SCR-01: narrative spine setup -> tension -> resolution
- FR-SCR-06: curiosity gaps planted, delayed, layered
- FR-BT-01: beats linked by BUT / THEREFORE rather than flat "and then"
- FR-16C-07: opens new loops before closing old ones
- FR-16C-13: complex ideas in plain language
- FR-16C-16: ending echoes the opening question/theme

## When done
Reply with only: the list of VIDs written, and any transcript you could not read. No summaries.
