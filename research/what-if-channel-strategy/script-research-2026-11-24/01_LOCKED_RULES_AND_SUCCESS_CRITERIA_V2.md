# 01 — Locked rules and success criteria V2

## Locked rules
- Lead Claude reads raw transcripts and the full Playbook personally. Sub-agents may only help with searches, calculations, independent checks. Their reading never sets `lead_claude_personally_read=YES`.
- Never claim 100% unless it happened. Unreadable pages/files are listed individually.
- Keep slots/order/format unchanged. Slot 05 may narrow "a moon" to Phobos (already decided). Slot 10 stays; distinct-angle option is separate.
- Claim statuses allowed: SOURCE_CHECKED, CALCULATED_SELF_REVIEW, ASSUMPTION, HYPOTHESIS, UNRESOLVED, EXPERT_REVIEW_NEEDED, TIME_SENSITIVE_RECHECK, REMOVED. Video statuses: DRAFT_READY_FOR_OWNER_REVIEW / DRAFT_WITH_OPEN_SCIENCE / CONDITIONAL_DRAFT.
- Seven lenses = Claude self-review. No fake expert, listener, audience or independent sign-off.
- No copying of xkcd/Munroe wording, jokes, art, sequence. No forced CTA/joke/cliffhanger.
- Existing Day 1 v3 (`productions/unreasonably-exact-01-free-fall/`) and Day 2 draft are read-only; both versions preserved.
- Git: branch `research/what-if-channel-strategy-2026-11-18` (live remote tip e9790e1a at start, no claim refs found). Normal push only. No PR, no merge, no force, no media/secrets. Untracked workbook `research/consolidation/XKCD_WHATIF_COMPLETE_DATA_WORKBOOK_2026-11-24.xlsx` (35.7 MB) is NOT part of this task: do not add it.
- Slop gate: scripts that belong under `productions/` need the gate; these V2 scripts live under research/, gate run manually via `scripts/check_slop_risk.py` and verdict reported (proxy only).

## Success criteria
1. 83 (or actual) transcripts: ledger rows with personally-read=YES only after a real read.
2. Playbook 556 pages all read, page log 556 rows, weak pages visually checked.
3. 10 findings each have a status and a fix in actual narration.
4. 10 V2 folders × 6 files; Slot 01/02 full text in final chat.
5. Pushed, remote blob IDs equal local, read-back done.
6. Final report in Roman Urdu with honest limits.
