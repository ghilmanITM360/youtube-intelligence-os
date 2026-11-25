# 10 — SELF-REVIEW and open issues (2026-11-24)

**This is SELF-REVIEW by the same model that wrote the blueprints.** No qualified reviewer, human listener, expert or editor has examined any item. A passing structural check or a successful calculation is not science verification and not permission to publish.

## 1. Second-pass checklist (Phase 6)
Legend: ✔ checked and consistent · ◐ partly / with a stated gap · ✘ not satisfied.
| # | Check | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | The question is answered | ✔ | ✔ | ✔ | ✔ | ✔ | ◐ | ✔ | ◐ | ✔ | ✔ |
| 2 | Each step follows from the last | ✔ | ✔ | ✔ | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ |
| 3 | No new physical assumption unstated | ◐ | ✔ | ✔ | ✔ | ◐ | ◐ | ✔ | ◐ | ✔ | ✔ |
| 4 | Numbers/units/ranges consistent | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 5 | Science tied to a visible consequence | ✔ | ✔ | ✔ | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ |
| 6 | Answer doesn't contradict the title | ✔ | ✔ | ✔ | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ |
| 7 | A Short works without its parent | n/a | ✔ | ✔ | n/a | ✔ | n/a | ✔ | n/a | ✔ | ✔ |
| 8 | A Long is not a stretched Short | ✔ | n/a | n/a | ✔ | n/a | ✘/◐ | n/a | ◐ | n/a | n/a |
| 9 | Humor doesn't replace explanation or copy xkcd | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 10 | Every material number has a claim ID | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 11 | No source text copied | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 12 | Limitations/unknowns visible | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 13 | Labelled SELF-REVIEW | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

Notes behind the non-✔ cells:
- **01 (3):** constant drag coefficient to Mach ~3 and a recalled density table above 86 km are stated but are real physical assumptions. **05 (3):** the sphere-plus-Hill model is a physical simplification; the gated beat depends on it. **06 (1,2,5,6):** the "reply" is hypothetical and the real status is unresolved, so the answer to the title is "at least ~48 h, but no reply is promised"; beats 4–6 depend on a snippet-level source and an editorial inference. **06 (8):** likely a stretched Short unless beats 3–6 are sourced. **08 (1,3,8):** the ocean's quantitative response and decay time are not sourced; beats 1–6 stand, the Long is borderline if tilt/spin beats are excluded.
- **Check 4 (numbers):** ledger values were compared to `scripts/output/fall_results.csv` and the calculation stdout by `scripts/validate_outputs.py` (fall numbers) and by reading (others). A mismatch found in the pass was fixed: the first Phobos fall-back range (17–31 min) described only one sphere; the corrected ranges are in 08/ledger/blueprint 05. A world-definition mix in blueprint 04 beat 2 (4 km world's g vs the 3 km worked world) was fixed.

## 2. Automated structural checks
`python3 scripts/validate_outputs.py` checks: required files; CSV parsing and column counts; calendar days 1,4,…,28 and 10 slots in crosswalk and ledger; every claim ID cited in a blueprint exists in the ledger; every SRC id resolves; ledger statuses are in the allowed set and none says VERIFIED; blueprints contain sections A–J, a STATUS line, the phrase SELF-REVIEW and no "SCIENCE VERIFIED / READY FOR PUBLICATION" status; key numbers match the model output. **This is structural only**; its result is printed at the end of this session's run and is not an assessment of the science. (Last run result is recorded in 02_PROGRESS_CHECKPOINT.md.)

## 3. What was NOT done (honest gaps against the directive)
- **Phase 1B:** the 83-transcript script analysis, the knowledge-base draft, the rule evidence ledger, the script-intelligence pilot and the topic/cadence audit CSVs were **not** read; I relied on the two calendar verdicts, both science-check CSVs, the research index and the Day 1 fact-check.
- **Phase 1C:** DS-000011 Packaging SOP, Viral Checklist, analyzers and the Hook guide beyond pp.1–2; DS-000018 content; the YouTube Automation Master Playbook; other global-youtube-knowledge material were not read. Only the `ref_rule` lines, the "But/Therefore" PDF and the first pages of the Hook guide were. None of this is platform fact.
- **Phase 2:** no xkcd video was watched, no audio listened to, no thumbnail reviewed; the channel's own search did not filter (title check against the workbook's 92 registry titles only). Other comparable videos were not reviewed. Randall Munroe's articles were read only via a fetch tool's extraction (68 and 72).
- **Phase 3:** several constants are recalled (G, USSA >86 km table, masses, Voyager speed, Neptune distance); official pages were read via fetch-tool extractions, not as page-by-page reading; Murphy review, 2024 Voyager fix, Apollo 15 orbit, Voyager news seen as snippets only.
- **Book:** read through imperfect OCR; What If? 2 not available.
- **Expert/human review:** none.

## 4. Claims that need an expert or a better source
| Claim IDs | Needs |
|---|---|
| V01-C03/C04/C07/C08, V02-* | aerodynamics/atmospheric-flight reviewer (drag range, hypersonic extrapolation, density table) |
| V05-C05/C06 | planetary dynamicist with a Phobos shape model (sphere + Hill sim is crude) |
| V06-C04 | primary NASA/JPL page for the April 2024 timeline |
| V03-C04, C06 | NASA source for Voyager's speed; Neptune distance |
| V07-C04 | Murphy review and APOLLO papers (photon return rate) |
| V08-C03/C08, V09-C04 | physical oceanographer (response to a changed forcing; decay time; wording) |
| V08-C06/C07 | astronomer; Lissauer 2012 and Laskar papers; a primary source for tidal recession |
| V08-C01 | source for the speed of gravity |
| V10-C02 | Apollo 15 mission report for orbit altitude/apse alignment |
| V04-C09, V05-C07 | biomechanics source for jump and sprint speeds |
| all NASA/Guinness pages | re-open on the release day (status and records change) |

## 5. Other corrections found in earlier project material
- Claude's calendar-review row S11 cites arXiv 1404.7505 for Lissauer et al.; that id is Li & Batygin (2014) (V08-C06). Do not reuse S11.
- The earlier Day 1 fact-check's 204 km/h is a calibrated value (A); it is not independent (V01-C03).
- The NASA 2012 Phobos slide's surface-gravity entry is garbled and inconsistent; unused.
- My own Phobos script first hung (impact-detection bug) and my first orbit "max clear elevation" table was meaningless; both fixed and documented in 08.

## 6. Statements the work does NOT make
No claim of survival, safety or injury; no prediction of views, CTR, retention or ranking; no claim that Voyager 1 is answering; no claim that any calendar position is approved; no claim of expert sign-off; nothing was created for production (no script, voiceover, asset, thumbnail, animation, video, upload, commit or push).
