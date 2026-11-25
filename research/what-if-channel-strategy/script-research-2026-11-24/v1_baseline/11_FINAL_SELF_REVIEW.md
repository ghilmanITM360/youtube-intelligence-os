# 11 — Final self-review (2026-11-24)

**This is a self-review by the model that wrote the scripts.** Structural checks, calculation re-runs and source reading are not science sign-off, expert review, editorial review or permission to publish. No human listener, expert, editor or other AI system reviewed anything.

## 1. Directive section 12 checklist
| # | Check | Result | Evidence / limit |
|---|---|---|---|
| 1 | Exactly 10 complete scripts, 4 Long + 6 Short | **Yes** | `videos/*/SCRIPT.md`; Long 01, 04, 06, 08; Short 02, 03, 05, 07, 09, 10; validator `scripts/validate_package.py` |
| 2 | Each script has opening, explanation, answer | **Yes (by reading)** | beats files map each; last paragraph states the answer |
| 3 | Title promise vs script | **Yes** | table in `10_CROSS_VIDEO_CONSISTENCY_CHECK.md`; slot 04 needs the "Around a Tiny World" title; slot 06 needs the repair-framed title |
| 4 | Every spoken number and material claim checked against its fact-check | **Done by reading, not automated** | 96 ledger rows (`08_MASTER_CLAIM_LEDGER.csv`); I corrected at least nine numeric/factual slips found this way (Eustace; 20 s vs 25 s; <0.1% vs <0.2%; "seventeen ten-thousandths"; 190 vs 204 km/h; "below 200"; etc.) — a miss is still possible |
| 5 | Contradictions between paired videos | **None found** | `10_CROSS_VIDEO_CONSISTENCY_CHECK.md` |
| 6 | Previous audit findings reconciled | **Yes: A–I** | `03_BLUEPRINT_AUDIT_RECONCILIATION.md/.csv`: 3 CONFIRMED, 1 CONFIRMED with qualification, 5 QUALIFIED, 0 disagreed, 0 STILL OPEN as findings (open items remain inside them) |
| 7 | Transcript and resource coverage matches claims | **Yes** | 83/83 transcripts FULL (read by four reader sub-agents; lead read their notes, not raw text); 68 resource rows, with FULL/SELECTED/INDEX_ONLY/SKIM depths stated; unread items listed in 12 §D |
| 8 | Originality and prior art | **Screened + disclosed** | 5-gram overlap ≤ 0.7% vs the 83 transcripts, ≤ 2.3% vs existing Day 1/2, ≤ 6.2% between new scripts; prior-art disclosures (Little Planet, Loneliest Human, Steak Drop, V018) in packaging/status; a human must still judge structural imitation |
| 9 | Repository script-quality / framework checks | **Slop gate run: 10/10 WARN (R7 "no images" only), 0 FAIL, no R1–R6 finding** | `work/slop_gate_results.txt`; manual checklist C1–C5 still for a human; the content-plan framework check (`--framework-plan`) was not run: it needs a plan.json, and these are scripts, not content plans |
| 10 | Structure checks vs real science/editorial review | **Distinguished** | the validator and gate are structural proxies; "PASS/WARN" is not "will not be detected" |
| 11 | No fabricated tests, feedback or sign-off | **Honoured** | none claimed |

## 2. Results
| slot | day | format | recommended title | words | est. narration | status | biggest issue |
|---|---|---|---|---|---|---|---|
| 01 | 1 | Long | Falling From 100 km vs 1 km: Which One Hits the Ground Faster? | 696 | 4:45 | DRAFT_WITH_OPEN_SCIENCE | Drag range and constant-Cd extrapolation to Mach ~3 (EXPERT_REVIEW_NEEDED, V01-C07, C10). |
| 02 | 4 | Short | Why Does a High-Altitude Skydiver Slow Down Without a Parachute? | 137 | 1:00 | DRAFT_WITH_OPEN_SCIENCE | Drag range (V02-C02, C04). |
| 03 | 7 | Short | Why Does a Radio Signal Take a Whole Day to Reach Voyager 1? | 134 | 0:57 | DRAFT_READY_FOR_OWNER_REVIEW | NASA wording and current speed must be rechecked on release day (V03-C03, C06). |
| 04 | 10 | Long | Could One Sideways Jump Put You in Orbit Around a Tiny World? | 639 | 4:18 | DRAFT_WITH_OPEN_SCIENCE | Jump speed is an assumption (V04-C07, C08). |
| 05 | 13 | Short | Could You Jump Off Phobos and Never Come Back? | 149 | 1:03 | CONDITIONAL_DRAFT | Shape/spin/Mars effects not modelled (V05-C04, C05, C08). |
| 06 | 16 | Long | How Do You Fix a Spacecraft When Every Reply Takes Two Days? | 619 | 4:09 | DRAFT_WITH_OPEN_SCIENCE | 2026 outage status: TIME_SENSITIVE_RECHECK (V06-C10, C11). |
| 07 | 19 | Short | How Long Does a Laser Take to Reach the Moon and Back? | 154 | 1:03 | DRAFT_READY_FOR_OWNER_REVIEW | Extraction-level reading of the APOLLO paper; Murphy 2013 not read (V07-C07, C08). |
| 08 | 22 | Long | What Would Happen to the Ocean If the Moon Vanished? | 566 | 3:45 | DRAFT_WITH_OPEN_SCIENCE | Ocean response, decay time and local timing (EXPERT_REVIEW_NEEDED/UNRESOLVED: V08-C04, C05, C08, C10). |
| 09 | 25 | Short | Would Earth Still Have Tides Without the Moon? | 147 | 1:00 | DRAFT_READY_FOR_OWNER_REVIEW | Last paragraph (many coasts still have two highs and lows) needs oceanographer confirmation (V09-C06). |
| 10 | 28 | Short | How Far Has a Human Been From Every Other Person? | 153 | 1:03 | DRAFT_READY_FOR_OWNER_REVIEW | Editorial: exact question overlap with Munroe's "Loneliest Human" (owner decision). |

Status meaning: DRAFT_READY_FOR_OWNER_REVIEW (4: 03, 07, 09, 10), DRAFT_WITH_OPEN_SCIENCE (5: 01, 02, 04, 06, 08), CONDITIONAL_DRAFT (1: 05). None is "publication-ready".

## 3. What the structural tools did and did not check
- `validate_package.py`: required files; 10 folders × 6 files; claim IDs cited in beats/fact-checks/Sources exist; ledger statuses are in the permitted set; calendar order/days/format; coverage 83 FULL (43 long, 40 shorts); findings A–I present; no CTA words or claim-ID brackets in the spoken text; no "SCIENCE VERIFIED / READY FOR PUBLICATION / independently verified" statements. **It does not check physics, wording quality or imitation.**
- `overlap_check.py`: 5-gram overlap only.
- `finding_checks.py`: re-runs the model arithmetic behind findings A, B, E–I; model assumptions are the weakest link (constant drag, recalled density above 86 km, uniform airless sphere, sphere + Hill sim for Phobos).

## 4. Honest weaknesses
- Slot 01 (≈ 4:45) is at the top of the 3–5 minute band; its caveat paragraphs are dense. Slot 06 depends on NASA text read through a fetch-tool summary; its 2026 paragraphs will need a rewrite if status changes.
- Shorts estimate 57–63 s at 2.7 words/s; recordings may exceed 60 s.
- Humor is intentionally sparse (a few dry lines); a human editor may want more or less.
- The seven lenses were run by one model in one session; their "strengths" are subjective.
- Slot 05 and 08 contain statements that only a domain expert can validate (V05-C04/C05, V08-C04/C08/C10).
- Slot 10's narration includes "probably on the far side … roughly 120 km up", which is our geometry, flagged as an estimate, not Guinness's method.
- Several statements rest on search snippets (Eustace, Karman line, Voyager speed/launch year, Apollo 15 orbit height); each is marked SNIPPET_ONLY in the ledger.

## 5. What was not done (by directive or constraint)
No audio, thumbnail, image, video, animation, upload, commit or push. The existing Day 1/Day 2 productions, the combined calendar file, and the repository were not modified (HEAD `e9790e1a`; `git status` shows only the pre-existing untracked workbook).
