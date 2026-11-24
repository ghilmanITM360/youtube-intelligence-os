# 05 Existing plan and prior-audit reconciliation (Phase 0) — status: PARTIAL (see end)
Prepared 2026-11-23 PKT. Labels: [OBS]=I opened/recomputed it now; [REP]=reported by an existing file; [INF]=my inference.

## 1. The three original files
- [OBS] CSV vs XLSX "Calendar" sheet compared cell-by-cell: 31x19 cells, **0 differences**. Other XLSX sheets (Month grid, Longs (10), Notes) read; Longs+Notes agree with CSV. "Charts" sheet = embedded images, not inspected.
- [OBS] PDF (7 pp) read in full as rendered pages. Its tables agree with the CSV (10 longs, 13 Shorts, scores, statuses).
- [OBS] Counts: 30 rows = **10 Long, 13 Short, 5 Rest (D7,12,17,21,24), 2 Evaluation (D14,D30)**. L4's "23 video slots, 10 long incl. conditional Day 29, 13 Shorts" **matches**. PDF says "25 dated rows" — it excludes the five rest rows (30-5); not a discrepancy. Day-29 is a "winner slot" with no topic. Notes sheet: "L 3, S 2, T 2, R 1, Q 1, winner 1" = 10.
- [OBS] Score formula 5D+3G+5F+3C+2V+2P recomputed for all 22 scored slots: **0 mismatches** (ORIGINAL_CALENDAR_AUDIT.csv). Weekdays match dates for all 30 rows. Excerpts inherit the parent's score (not independent evidence).
- [REP] Provenance: owner approved the *calendar* 2026-11-18; only the Day-1 script v3 is approved (2026-11-19). Sources named: branch research/what-if-channel-strategy-2026-11-18 (files 03, 05, 06, topic_scores). Branch exists locally and as origin/…; **not yet read by me** (to do, via `git show`, no checkout).
- [INF] **Stale status:** Day 1 = today 2026-11-23 and the file itself says no record the Day-1 video exists. The calendar's dates (Nov 23–Dec 22) are therefore already unachievable as written; the plan must be re-based (L18: keep as history, propose re-based dates).
- [INF] **Capacity mismatch:** 23 videos/30 days (10 longs) is roughly one long every 3 days. No document gives actual production capacity. Prior audit 2 sizes this at ~18–32 h per long (an estimate, unsourced) — so the original cadence implies far more than any competitor-level workload for a new, unlaunched channel (see cadence deliverable).

## 2. Prior audit 1 (~/Downloads/UNREASONABLY_EXACT_TOPIC_AUDIT_2026-11-23/, written 19:51–19:53 PKT)
[OBS] opened: START_HERE.md, TOPIC_SELECTION_AND_ORDER_REPORT.md (first 150 lines), EXISTING_CALENDAR_TOPIC_AUDIT.csv (23 rows, all columns). [Not yet opened: evidence register, competitor audit, book crosswalk, knowledge audit, limitations, next-steps, NEXT_60_DAYS xlsx content.]
Its claims: proposed 60-day window Dec 7 2026–Feb 4 2027; keep higher-fall first; Voyager added; hold neutron pellet + slow light; replace last-light, small plane, steak, raindrop; Day 29 → optional readiness reserve.
Independent check: its fall table reproduces ([OBS] my own RK4 + US-1976 atmosphere: ground 204.0 / 204.3 km/h for 1 km / 100 km; sensitivity 186–229 km/h; peak 3,620 km/h from 100 km; raw/science_recompute_output.txt). Caveat: drag input CdA/m=0.00505 m²/kg is shared with the prior audit, so this validates arithmetic/integration, not the drag value.
Neutron: 0.7 cm³×2.7e17–1e18 kg/m³ = 189–700 million t [OBS]; prior audit's "~190 million" lower bound is only true for the assumed lowest density.

## 3. Prior audit 2 (~/Downloads/UNREASONABLY_EXACT_CADENCE_AND_TOPIC_ORDER_2026-11-23/, 20:42–20:52 PKT) — NOT named in the prompt
Found by listing Downloads. Author session unknown; no running session in the app's list. [OBS] 22 channels, 1,443 inventory rows; rows use *relative ages* ("7mo ago") — many have no exact publish time; counts are labelled "lower bound/partial". 60-day plan: Dec 7 → Feb 4; **6 longs + 8 Shorts (4 excerpt, 4 standalone), 42 production/rest days, 3 review days, 1 reserve** (counts [OBS] from PROPOSED_60_DAY_ORDER.csv). Order: D1 WIB-36 fall (Dec 7), D8 Voyager (ALT-01), D18 kettle, D29 tiny-planet orbit (WIB-17), D40 Moon tides (ALT-03), D51 Mars helicopter (ALT-02).
The prompt's remembered order "fall, Voyager, orbit jump, astronaut records, Moon tides, alien detectability, Mars rotor" corresponds to audit 1's workbook; audit 2 differs (kettle inserted, astronaut→Short, alien parked). So the two prior proposals already disagree.

## 4. Disagreements between the two prior audits (from the CSVs) [OBS]
| Slot | Audit 1 | Audit 2 |
|---|---|---|
| D5/D9 NEW-06 Moon | KEEP WITH REVISED PACKAGING (long) / MOVE (excerpt) | REPLACE / REPLACE |
| D25/D28 WIB-52 loneliest | KEEP WITH REVISED PACKAGING / MOVE | REPLACE / REPLACE |
| D8/D10 WIB-22 aliens | MOVE | MOVE LATER (parked pending instrument premise) |
| D15/D19 WIB-17 orbit | MOVE | MOVE LATER (to Day 29 of new plan) |
| Day 29 | NEEDS MORE DATA | NEEDS MORE DATA |
Note: audit 2 re-adds a Moon-tide long (ALT-03) while marking NEW-06 REPLACE — i.e. "replace" there means retitle, so the labels are not comparable across audits. To be resolved in Phase 6 with evidence.

## 5. Plan lineage table
| Plan | Window | Longs | Shorts | Status |
|---|---|---|---|---|
| Original approved calendar | 2026-11-23→12-22 (30 d) | 10 (1 conditional) | 13 | owner-approved 2026-11-18 (calendar only); stale at Day 1 |
| Prior proposal 1 (workbook) | 2026-12-07→2027-02-04 | see xlsx (not yet counted) | see xlsx | proposal, no approval |
| Prior proposal 2 | same window | 6 | 8 | proposal, no approval |
| This audit | Phase 7 | pending | pending | proposal |

## 6. Not yet done in Phase 0 (L16)
- Read strategy branch files (topic bank, 03/05/06, scores), prior science checks, Codex/Claude audits, book extracts, source registers.
- Open audit-1 evidence register/limitations/xlsx; count prior proposal 1 items.
- Search other worktrees (xkcd-what-if worktree at cf2dbb2c, ~/workprojects/"video data of what if") for topic banks.
Status: **PARTIAL**.
