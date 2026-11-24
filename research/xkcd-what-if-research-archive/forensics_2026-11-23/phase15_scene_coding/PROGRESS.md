# Phase 15 progress: literal Phase 6.4 scene coding (owner decision 2026-11-23)
Honest status; all coding is SAME-MODEL SUBAGENT SELF-REVIEW from 3 stills per shot and provisional ASR (not listened). Not independent. Motion (q5) is only what three stills show.

| Tranche | Scope | Shots | Coded | Status |
|---|---|---|---|---|
| A | ten directive episodes (5 audit layer, 5 campaign layer) | 260 | **260** | done, validated (`A_ten_SCENE_CODING.csv`) |
| B | remaining audit-layer videos (39) | 594 | 0 | cells built (`B_audit_context.csv`), not coded |
| C | remaining campaign-layer videos (39) | 583 | 0 | cells being built, not coded |
| total | | 1,437 | 260 (18.1%) | |

## Tranche A: validation and findings
- Validator `scripts/phase15_validate.py`: 10 of 10 files valid; object counts and shot IDs equal the context CSV; no empty fields.
- Spot-check by the main session (6 shots of gp5G1QG6cXc SH007 to SH012 viewed against their coded rows): all six consistent with the stills; small wording differences only. A larger audit of accuracy was NOT done.
- Agreement with the main session's earlier 156-shot review on boundary type: 20 of 21 overlapping shots agree (the one disagreement: earlier FALSE_PROGRESSIVE, now TRUE_CUT).
- Counts (260 shots, descriptive, not channel rates): boundary TRUE_CUT 222, BORDERLINE 24, FALSE_PROGRESSIVE 14 (10 of them in gp5G1QG6cXc and 4 in 3EI08o-IGYk, the two videos coded by the first agent; the other agents recorded none, so strictness differed between agents and the false-boundary rate here is NOT comparable to the earlier 24%); confidence HIGH 137, MEDIUM 112, LOW 11; q5 NOT_ASSESSABLE_STILLS 70 (27%); narration OK 250, GARBLED_ASR 6, MISMATCH_WITH_SCREEN 4; q12 muted-understandable YES 186, PARTLY 74, NO 0; q13 drawn as SCHEMATIC 134, ILLUSTRATIVE 98, LABELLED_TO_SCALE 28; q11 effect CLARITY 104, HUMOR 77, MIXED 23, SUSPENSE 20, NONE 19, SURPRISE 17.
- Known weaknesses: later shots of several videos are terser (agents' own reports); the audit-layer narration (5 videos) was truncated at about 240 characters in the context CSV (fixed in `scripts/phase15_cells.py` for tranche B; tranche A not re-run); 54 s to 105 s shots are sampled by only 3 stills; q4 and q14 are INFERRED intent, not observation.
- Cost note: tranche A (4 agents, about 527k agent tokens) moved the 5-hour usage window from 52% to 66% and weekly from 22% to 25%.

## Next
Tranche B in batches of about 260 shots per usage window; then C; re-code of the 156 earlier shots is subsumed by B/C (they are inside those videos). After each tranche: validate, spot-check at least 5% of shots against sheets, write counts here.
