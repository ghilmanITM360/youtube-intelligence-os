# 02 — Progress checkpoint

Last updated: 2026-11-24 (after Phase 3 calculations, before writing deliverables).

## Done
- Repo/branch confirmed: `research/what-if-channel-strategy-2026-11-18`; only untracked file is `research/consolidation/XKCD_WHATIF_COMPLETE_DATA_WORKBOOK_2026-11-24.xlsx`. No commit/push/edit to repo.
- 00 directive saved in full; 01 rules saved.
- Calendar, latest research index, Claude + Codex verdicts, both science-check CSVs, Day 1 FACT_CHECK.md read (whole or effectively whole).
- Munroe book: PDF found (`~/Downloads/Randall-Munroe-What-If__...Houghton-Mifflin-Harcourt-2014.pdf`, 321 pages, IMAGE-ONLY scan, no text layer, metadata title "What If?", author Randall Munroe, Google Books converter; OCR of the copyright page confirms HMH 2014, ISBN 978-0-544-27299-6 hardback). I OCR'd all 321 pages with Apple Vision into the SCRATCHPAD (not saved here, not redistributed) and keyword-searched them; I read in full: TOC, Little Planet (PDF 117-121 = printed 102-106), Steak Drop (PDF 122-125 = printed 107-110), Loneliest Human (PDF 285-287 = printed 270-272), Orbital Speed (PDF 202-204 start), Free Fall (PDF 210-211 start), High Throw (183-185 start), Global Windstorm pp. 20-21 (Moon/tide line), Laser Pointer (PDF 42, 48-49 partly). OCR is imperfect. Printed page = PDF page - 15.
- Workbook: 318 sheets; B.VIDEO_MASTER 92 rows. Titles keyword-matched (titles only; not the video content).
- `what if data .pdf` (446 pp) opened first ~60 lines only: an unrelated persona prompt about "YouTube virality"; NOT used as evidence.
- Reference framework: `data/knowledge/reference_knowledge.db` rules read (FR-16C-03/05/13, FR-BT-01, FR-HOOK-01, FR-SCR-04, FR-TITLE-03/04); DS-000011 PDFs "But and Therefore" (3 pp, whole) and "Hook guide" (58 pp, first ~70 lines only); DS-000018 manifest header only. All are creator heuristics (rule class CREATIVE_HEURISTIC), not platform facts.
- Web (WebFetch/WebSearch, access 2026-11-24): NASA Voyager light-day release (read, dated 2026-11-19) and Voyager blog (dated 2026-11-18, page updated 2026-11-20); NASA NSSDC Mars + Moon fact sheets; NASA 2012 Phobos slides (NTRS 20120013420, local pdftotext); Guinness Worden page; Guinness Artemis II "farthest separation" article; NASA Artemis II release; what-if.xkcd.com/72 and /68; NOAA tides02_cause page; NOAA CO-OPS harcon API (raw JSON saved in scripts/data); Li & Batygin arXiv 1404.7505 abstract; Guerster & Walter 2017 PLoS ONE (PMC5720713, extraction); NIST "Moon and back" page; search snippets only: Murphy LLR review, 2024 Voyager FDS fix, Apollo 15 orbit altitudes, Voyager news.
- Browser pane: opened YouTube @xkcd_whatif (1.38M subs, 92 videos); the channel-search query did not apply a filter, so NO per-topic channel search was achieved (NOT CHECKED). Nothing played, nothing listened.
- Scripts written and run (stdlib python): fall_model.py, atmosphere_check.py, orbit_small_world.py, phobos_escape.py (a bug that skipped impact detection was fixed; a first run hung and was killed), light_time_tides_isolation.py, fetch_noaa_harcon.py. Outputs in scripts/output/.

## Key findings so far (self-review, not expert review)
1. Fall: ground speed from >=3 km is height-independent within the model, but its VALUE depends on drag: 164-204 km/h across sets; independent paper inputs (Cd 0.60, A 1.19 m2, m 121.2 kg) give 189 km/h, not 204. Peak check vs Stratos: set B 364.8 vs real 377.1 m/s (-3.3%). Slow-down appears for releases above ~1.7-2 km. Felt load from 100 km ~4.6 g (model, low confidence).
2. Munroe's book already covers: Steak Drop (falling from altitude), Little Planet (escape/orbit speed ~5/3 m/s on a tiny body), Orbital Speed, Loneliest Human (EXACT Short 6 question; also what-if.xkcd.com/72), Laser Pointer (many lasers at Moon). Nothing found for Voyager/Phobos (Phobos only as a photo mention).
3. Short 6: Guinness page = Worden 3,596.4 km (2R+h with h~121.6 km); Munroe 3,585 km (h~110 km). Artemis II (Apr 2026) set distance-from-Earth (406,771 km) and Guinness "farthest separation" (419,656 km) records; neither is isolation.
4. Phobos: point-mass v_esc 11.3 m/s agrees with NASA slide; Hill-model sim says 3 m/s falls back everywhere (17-31 min for the main sphere; 12-155 min across radii), best-direction threshold ~4-6 m/s (sphere model) - HYPOTHESIS needing shape model + expert.
5. Claude's earlier note attributes arXiv 1404.7505 to Lissauer et al.; it is Li & Batygin 2014. Lissauer 2012 still not read.
6. Tides: Sun/Moon tide-force ratio 0.459 (NOAA "about 1:2"); real S2/M2 at 8 NOAA stations 0.15-0.54 => no universal %.

## Final state (2026-11-24)
All deliverables written: 00-10, START_HERE, 10 blueprints, scripts (+outputs, raw NOAA data). `python3 scripts/validate_outputs.py` -> 105 passed, 0 failed (structural only; not a science or originality check).
Statuses: READY FOR OWNER REVIEW: 1,2,3,4,9,10 (10 also NEEDS EDITORIAL DECISION); PARTIAL: 5,6,7,8; BLOCKED: none.
Repo check: `git status` shows only the pre-existing untracked workbook; nothing committed, pushed, or edited in the repo. Calendar file untouched.
Exact next action (if resumed): owner decisions in 04; expert/source items in 10 §4; re-open NASA/Guinness pages before any publication; nothing else pending.
