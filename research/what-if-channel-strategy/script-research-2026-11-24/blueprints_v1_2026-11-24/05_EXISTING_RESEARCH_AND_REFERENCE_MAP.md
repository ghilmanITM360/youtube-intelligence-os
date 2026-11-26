# 05 — Existing research and reference map (2026-11-24)

For each resource: path/section, what I actually read, its class, and how it affects the blueprints. "Read" means opened and read by me in this task; anything else is stated. Source IDs refer to `03_SOURCE_REGISTER.csv`. SELF-REVIEW throughout: no qualified reviewer has seen any of this.

## A. Combined calendar (SRC-01)
`research/what-if-channel-strategy/COMBINED_30_DAY_CALENDAR_2026-11-24.md` — whole file read. Class: proposed planning baseline (AI + owner synthesis). It is not approval, sign-off or a forecast. Effect: fixes the 10 slots; its own "gates" list (peak vs impact speed, 204-vs-204, Voyager distinct Long, Phobos shape, farthest-human definition, neutron hold) became the non-negotiable checks in 08.

## B. Existing What If archive (`research/xkcd-what-if-research-archive/`)
| Resource | What I read | Class | Effect |
|---|---|---|---|
| `LATEST_RESEARCH_INDEX_2026-11-24.md` (SRC-02) | whole | project index, DRAFT/partial | confirms no expert review, no audience data; unresolved list (drag, neutron, Moon tilt, Phobos tide, Voyager status, Worden) |
| `claude_calendar_review_2026-11-24/CLAUDE_INDEPENDENT_VERDICT.md` (SRC-03) | whole | Claude SELF-REVIEW | recommends changing 5 of the 10 slots; the locked calendar is kept, differences recorded in 09 |
| `claude_calendar_review_2026-11-24/SCIENCE_AND_SOURCE_CHECK.csv` (SRC-04) | whole (18 rows) | AI + own computation | provided starting numbers; two corrections found: S11's arXiv link is Li & Batygin 2014, not Lissauer et al.; sets C/D drag values are unsourced assumptions |
| `codex_calendar_review_2026-11-24/CODEX_INDEPENDENT_VERDICT.md`, `SCIENCE_CHECKS.csv` (SRC-05/06) | whole | Codex (different tool, not expert review) | conditional Voyager reply Long; "do not lock exact peak"; "Phobos shape/rotation gate" |
| other folders in the archive (topic/cadence audits, 60-day plans, 83-script analysis, knowledge-base draft, rule evidence ledger, forensics) | **only listed** by the index; not read in this task | — | NOT CHECKED here. The 83-transcript study, knowledge-base draft and rule evidence ledger were not re-read; their conclusions reach me only through the verdicts above |

Also read: `productions/unreasonably-exact-01-free-fall/FACT_CHECK.md` (SRC-07, claims table whole). It uses one fitted drag number (calibrated to the Stratos peak), so its 204 km/h is not independent; I recomputed with the paper's own inputs (08 §1). I did not re-read the SCRIPT, NARRATION_NOTES or the Day 2 draft.

## C. Reference knowledge (creator heuristics only; none is a platform fact)
| Resource | What I read | Class | Effect |
|---|---|---|---|
| `data/knowledge/reference_knowledge.db` `ref_rule` (SRC-11) | 33 rule lines listed; used FR-16C-03 (cause & effect), FR-16C-05 (throughline), FR-16C-13 (plain language), FR-BT-01 (BUT/THEREFORE), FR-HOOK-01 (hook), FR-SCR-04, FR-TITLE-03/04 (promise/payoff) | rule_class CREATIVE_HEURISTIC | each blueprint's beats are written as cause -> consequence ("THEREFORE/BUT"), with one throughline question, and a title-promise check. Not claimed as retention or CTR evidence |
| DS-000011 "The Magic of BUT and THEREFORE" PDF (SRC-10) | all 3 pages | creator heuristic (AI-paraphrased) | same as above |
| DS-000011 "Hook guide" PDF (SRC-10) | pp.1-2 only (first ~70 lines of 58 pages) | creator heuristic | 3-step hook idea (context, pattern break, snapback) used loosely in section F |
| DS-000011 Packaging SOP, Viral Checklist, Script/Intro analyzers | **not opened** this task (only the ref_rule extracts of them) | — | NOT CHECKED |
| DS-000018 "2026 Algorithm Update" (SRC-12) | manifest header only | unverified creator claims | NOT USED as evidence |
| YouTube Automation Master Playbook; global-youtube-knowledge other folders | **not located/opened** (DS-000031 folder exists; not read) | — | NOT CHECKED |
| `what if data .pdf` in Downloads (SRC-13) | first ~60 lines | unrelated persona prompt | NOT USED |

Platform/algorithm "formulas" in those files were not used as facts. Nothing here predicts CTR, retention or views.

## D. Owner-supplied What If? book and workbook
**Book (SRC-08):** `~/Downloads/Randall-Munroe-What-If__-Serious-Scientific-Answers-to-Absurd-Hypothetical-Questions-Houghton-Mifflin-Harcourt-2014.pdf`. PDF metadata: title "What If?", author Randall Munroe, 321 pages, produced by a Google Books converter; edition confirmed from the OCR of the title page and copyright page: Houghton Mifflin Harcourt 2014, © 2014 xkcd Inc., ISBN 978-0-544-27299-6 (hardback) — the first edition of the book (What If? 2 is a different book). It is an image-only scan (no text layer). I OCR'd every page with Apple Vision into my scratchpad (not saved here) and keyword-searched all 321 pages; I then **read in full**: the contents list, "Little Planet" (printed pp.102-106), "Steak Drop" (pp.107-110), "Loneliest Human" (pp.270-272), the start of "Orbital Speed" (pp.187-189), "Free Fall" (p.195-196 start), "High Throw" (p.168-170 start), the Moon/tide passage in "Global Windstorm" (pp.5-6) and parts of "Laser Pointer" (pp.27-34). Printed page = PDF page − 15. OCR is imperfect; no book prose is reproduced in this folder.
Chapter mapping (class per directive):
| Our slot | Book chapter | Class |
|---|---|---|
| 10 Farthest human | Loneliest Human, pp.270-272 | EXACT QUESTION |
| 4 Sideways-jump orbit | Little Planet, pp.102-106 | CLOSE PREMISE |
| 5 Phobos escape | Little Planet (escape-speed rule); Phobos only in a photo caption | BROAD MECHANISM |
| 1, 2 Fall from space / slow-down | Steak Drop pp.107-110; Free Fall p.195-196; Orbital Speed pp.187-190 | BROAD MECHANISM |
| 7 Lunar laser | Laser Pointer pp.27-34 (many lasers at the Moon; not round-trip timing) | BROAD MECHANISM / adjacent |
| 8, 9 Moon and tides | Global Windstorm pp.5-6 (Moon, tides and spin) | BROAD MECHANISM |
| 3, 6 Voyager | no "Voyager" hit in OCR | NOT FOUND in OCR (OCR-limited; not proof of absence) |
What If? 2 and the other book chapters were not available/read. Related xkcd articles opened: what-if.xkcd.com/72 (Loneliest Human) and /68 (Little Planet), via a fetch tool's extraction.

**Workbook (SRC-09):** `research/consolidation/XKCD_WHATIF_COMPLETE_DATA_WORKBOOK_2026-11-24.xlsx` — 318 sheets (README, INDEX, FILE_CATALOG + 315 data sheets); `B.VIDEO_MASTER` has 92 rows. I keyword-searched registry titles (42 hits, none for fall-from-space, Voyager, orbit/little planet, Phobos, Moon vanishing, tides, farthest human). Titles only: the videos' content, thumbnails, audio were not inspected. Related Moon titles found: moon-turned-into-a-black-hole (two versions), Moon made of protons/electrons, pool on the Moon; laser: "What if everyone pointed a laser at the moon?" (JqFSGkFPipM).

**Channel page (SRC-32):** opened @xkcd_whatif in the built-in browser (1.38M subscribers, 92 videos); its topic search did not filter results, so no per-topic channel search was achieved. Nothing was played or listened to; no frame sampled.

## E. The owner's observed What If? approach
Used as an observed creative approach and owner preference, not as a verified xkcd production checklist: (1) strange but understandable question; (2) explicit rules for the hypothetical; (3) real science with intermediate calculations; (4) cause -> consequence -> next question; (5) numbers turned into imaginable comparisons; (6) escalation only where supported; (7) clear answer with qualifications; (8) restrained humor where natural. Every blueprint is organised on it (sections A-J), but this is our interpretation of a style, not a reproduction of anyone's wording, jokes, drawings or beats.

## F. Primary and official sources read (see 03)
NASA Voyager release and blog (Nov 2026), NASA NSSDC Mars and Moon fact sheets, NASA 2012 Phobos slides, Guinness (Worden; Artemis II separation), NASA Artemis II release, NOAA tides page and CO-OPS harmonic constituents (raw data), Guerster & Walter 2017 (Stratos aerodynamics), Li & Batygin 2014 (abstract), NIST (first lunar echo). Snippet-only: Murphy LLR review, the 2024 Voyager fix, Apollo 15 orbit altitudes, Voyager news. Re-open all official pages before any publication.
