# Ten-script final review V2 (2026-11-24)

**This review is by the model that wrote the scripts (Claude self-review).** No expert, human listener, editor or independent AI reviewed anything. Structural checks and re-run calculations are not science sign-off or publication approval. WebFetch/sub-agent reads of web pages are summaries, not verbatim lead reading.

## Table

| Slot | Day | Format | Title | Words | Runtime estimate | Status | Main remaining issue |
|---|---|---|---|---|---|---|---|
| 01 | 1 | Long | Falling From 100 km vs 1 km: Which One Hits the Ground Faster? | 706 | 4:41–5:06 | DRAFT_WITH_OPEN_SCIENCE | Drag range and constant drag shape to Mach ~3 are model assumptions that need an aerodynamics review. |
| 02 | 4 | Short | Why Does a High-Altitude Skydiver Slow Down Without a Parachute? | 158 | 1:05–1:11 | DRAFT_WITH_OPEN_SCIENCE | Drag range at 10 km needs an aerodynamics check; numbers are model values. |
| 03 | 7 | Short | Why Does a Radio Signal Take a Whole Day to Reach Voyager 1? | 142 | 0:58–1:03 | DRAFT_READY_FOR_OWNER_REVIEW | NASA distance and wording must be rechecked on release day. |
| 04 | 10 | Long | Could One Sideways Jump Put You in Orbit Around a Tiny World? | 635 | 4:10–4:34 | DRAFT_WITH_OPEN_SCIENCE | Take-off speed is an assumption; the toy world is not a real asteroid. |
| 05 | 13 | Short | Could You Jump Off Phobos and Never Come Back? | 180 | 1:11–1:18 | CONDITIONAL_DRAFT | No primary source for Phobos's local escape-speed range; secondary values conflict. |
| 06 | 16 | Long | How Do You Fix a Spacecraft When Every Reply Takes Two Days? | 610 | 3:58–4:20 | DRAFT_WITH_OPEN_SCIENCE | Paragraph 10 is time-sensitive and may be out of date by release. |
| 07 | 19 | Short | How Long Does a Laser Take to Reach the Moon and Back? | 170 | 1:06–1:12 | DRAFT_READY_FOR_OWNER_REVIEW | Only part of Murphy 2013 was read; no average detected-photon figure exists in what was read. |
| 08 | 22 | Long | What Would Happen to the Ocean If the Moon Vanished? | 680 | 4:24–4:48 | DRAFT_WITH_OPEN_SCIENCE | No ocean model of a Moonless Earth or decay time was found; the answer is partly 'not known'. |
| 09 | 25 | Short | Would Earth Still Have Tides Without the Moon? | 185 | 1:12–1:18 | DRAFT_READY_FOR_OWNER_REVIEW | Oceanographer confirmation of the last paragraph is pending. |
| 10 | 28 | Short | How Far Has a Human Been From Every Other Person? | 180 | 1:10–1:16 | DRAFT_READY_FOR_OWNER_REVIEW | Munroe overlap (owner decision) and unsourced geometry. |

Runtime = 2.5–2.75 words/second plus 1.5 s per paragraph break. Estimates only; recording and listening are still required. Shorts run longer than the 60 s editorial target; YouTube allows up to 3 minutes.

## Claim ledger counts (84 claims)
ASSUMPTION: 9, CALCULATED_SELF_REVIEW: 30, EXPERT_REVIEW_NEEDED: 1, HYPOTHESIS: 1, SOURCE_CHECKED: 33, TIME_SENSITIVE_RECHECK: 6, UNRESOLVED: 4

## Checks run
- Structure: 10 folders × 6 V2 files built by `work/build_v2.py` (asserts allowed statuses and that every beat cites an existing claim).
- Banned-phrase scan (stock openings, CTA words, AI phrases): none in spoken text.
- Residual-phrase scan for the ten criticised statements: none in spoken text (`work/residual_phrase_scan.txt`; hits are only 'removed from v1' notes).
- 5-gram overlap: `work/overlap_check_output.txt`.
- Repository AI-slop gate (`scripts/check_slop_risk.py`): all ten WARN on R7 only (no image files; none were created). No FAIL. This is a proxy, not proof that content will not be detected; manual checklist C1–C5 is for a human.
- Models re-run: `work/models/` (fall, orbit/Phobos/light-day arithmetic).

## Findings F1–F10
See `INDEPENDENT_AUDIT_RECONCILIATION_V2.md`: 8 CONFIRMED (F1, F2, F3, F4, F6, F8, F9, F10; F6 was already corrected in v1 and rechecked) and 2 QUALIFIED (F5, F7); all were fixed in the narration; none was disagreed with. Residual open items per finding are listed there.

## Honest weaknesses
- Slot 01 and slot 08 are dense; a listener test is needed.
- Slot 05 is conditional: its real-world part rests on secondary sources.
- Slots 03/06/10 depend on NASA/Guinness wording that must be rechecked on production day.
- Slot 08 has no tide-height or decay-time number because none was found.
- All figures from the fall model are model values; heating, real drag changes with Mach number and head-down postures are not established.
- The Munroe overlap in slot 10 remains the owner's decision.
- Humour is minimal by design; a human editor may want to add or remove dry lines.

## What was not done
No audio, image, animation, thumbnail, upload or publication. The owner-approved Day 1 v3 and Day 2 draft were not modified (sha256 0455e37d… and 128ce572…).
