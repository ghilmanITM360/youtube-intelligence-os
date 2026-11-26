# Phase 15 scene-coding codebook (literal Phase 6.4, owner decision 2026-11-23)
Unit = one ledger shot (hard-cut span, machine boundary; a boundary may be a false cut). Coder = a same-model subagent: SELF-REVIEW, not independent. Evidence = 3 stills per shot (start+0.2 s, middle, end-0.2 s) and provisional ASR text (NOT listened to, may contain errors; units like petawatt/terawatt may be garbled).
Every answer <= 25 words. Prefix INFERRED: on anything that is interpretation of intent (q4, q9 partly, q14). Never claim motion that the three stills do not show; if they are identical write NOT_ASSESSABLE_STILLS for q5.
Fields (JSON keys):
- video_id, shot_id (copy exactly)
- boundary_check: TRUE_CUT | FALSE_PROGRESSIVE | BORDERLINE (is the start of this shot a real scene change versus the same scene changing continuously? judge from the previous cell where visible)
- q2_seen: what the viewer sees (subjects, setting, text on screen)
- q3_concept: the concept being explained
- q4_why_visual: INFERRED: why this visual was chosen for this narration
- q5_moves: what visibly changes between the three stills (or NOT_ASSESSABLE_STILLS)
- q6_fixed: what stays fixed
- q7_simplified: what is intentionally simplified or omitted
- q8_quantity: scientific quantity shown or spoken (with number and unit as drawn) or NONE
- q9_causality: how cause and effect is conveyed (sequence, arrow, before/after, label, none)
- q10_next_change: what changes from this shot into the NEXT cell (or END for the last shot of the video)
- q11_effect: HUMOR | SUSPENSE | SURPRISE | CLARITY | MIXED | NONE plus <= 6 words why
- q12_muted: YES | PARTLY | NO plus <= 10 words (can the shot be understood with the sound off?)
- q13_accuracy: SCHEMATIC | ILLUSTRATIVE | LABELLED_TO_SCALE | UNCLEAR plus <= 8 words (this is about how it is drawn, NOT a physics check)
- q14_technique: INFERRED: a general technique a new original production could use (not the source artwork itself)
- text_on_screen: visible words/numbers verbatim (or NONE)
- narration_check: OK | GARBLED_ASR | MISMATCH_WITH_SCREEN (say what)
- confidence: HIGH | MEDIUM | LOW
q1 (narration) is taken from the context CSV (asr_text) and is not coded again.
