# What If? book: audit, index and uses (2026-11-14)

Labels: OBSERVED = measured from files this session. INFERRED = my reading. UNKNOWN = not checked.
Rule kept: index holds references, factual notes and our own summaries. No book text beyond the short question lines is copied. Raw originals were not modified.

## 1. What is actually in `/Users/ghilmankhan/workprojects/what if book`

| Item | OBSERVED |
|---|---|
| Source PDF | `Randall-Munroe-What-If__...Houghton-Mifflin-Harcourt-2014.pdf`, 321 pages, 11.3 MB, SHA-256 `0f43b5f0…2023`. Google Books scan, no text layer (`text_pages: 0`). |
| Edition | 2014 Houghton Mifflin Harcourt, **from the filename**. PDF metadata gives only title "What If?" and author. No copyright page was read, so the edition is **filename-supported, not page-verified**. |
| Page offset | pdf page = printed page + 15 in all 91 records (pdf 16 = printed 1). |
| `WhatIf_Complete_Extraction/` | 91 questions, 321 page OCR files, 330 extracted figures, 91 per-question JSON, 91 transcription md, channel-vs-book match CSV, xlsx/json/pdf database. |
| `XKCD_What_If_Titles_and_Full_Scripts.xlsx` | Channel titles plus scripts. SHA-256 `0906f8b9…2dcc`. Source of the channel match. |
| `tools/` | extraction and build scripts, early/middle/late review JSON. Not modified. |
| `04_FIGURES_AND_DIAGRAMS/middle` (top level) | earlier figure working copy. Not re-audited. |
| `05_SCIENTIFIC_DATA/` | **empty**. |

## 2. Verified counts

- 91 question records, 91 unique IDs, **91 unique question texts**. Sections 57 main, 27 Weird, 7 Short-Answer (matches the coverage report).
- Per-question JSON agrees with the master CSV on page range and question text (0 diffs).
- All 91 transcription files exist. Page ranges are valid and monotone, pdf p.16–305.
- Explanation depth: 40 structured, 12 short notes, 39 none (32 early records plus 7 Weird). Coverage report said 52 detailed: matches 40 + 12.

## 3. Discrepancies (book vs existing extracts)

1. The master CSV shows 59 non-empty "detailed explanation" cells, but 7 Weird rows contain a 2-character placeholder. Real detail = 52. The index tiers fix this.
2. WI-0058, WI-0059 and WI-0060 share "Orbital Speed" at pdf 202–206. This is one chapter with three reader questions, not a duplicate. 91 questions therefore map to fewer chapters.
3. 32 early-section records have no independent explanation notes (the extraction's own unresolved list).
4. Figures: 330 extracted, 329 unique hashes (one duplicate). Question-to-figure mapping is empty for the records I sampled (WI-0010, WI-0033, WI-0086). Figures are not yet usable for storyboards.
5. All OCR is unproofread. Quote, equation, unit or figure use needs a page-image check first.
6. Edition: see section 1, filename-based only. The comparison report itself says overlap does not prove the team used the printed book rather than the website.
7. Channel match: 39 videos match 31 distinct book questions (20 question-answer, 11 excerpt or compilation). 3 videos have no transcript; one (video 89) is title-only probable.

## 4. Index files

- `BOOK_INDEX.csv`: 91 rows with pdf and printed pages, transcription and record paths, detail tier, inferred mechanism tags, channel videos, originality status.
- `book_index.sqlite`: FTS5 over title, question, summary, principles, assumptions, tags.
- `search_book.py`: `python3 -I search_book.py 'drop OR fall'` gives ID, pages, tier, originality.
- `BOOK_SOURCE_REGISTRY.json`: edition note, PDF hash, key file hashes, counts.
- `ORIGINALITY_ROOM.csv`: the 60 questions not on the channel, each with a keyword near-match check against channel titles (heuristic only).
- Rebuild with `build_book_index.py`. Mechanism tags are my keyword heuristic, labelled INFERRED.

## 5. What the book is good for, with examples

**A. Question development.** Hypotheticals are defined by one impossible input plus one measurable output. WI-0033 (pdf 122–126): the mechanism is compressive heating above about Mach 2 plus drag. That mechanism supports new questions the book does not ask, for example "How fast must a falling object go before its surface warms?". This is a candidate only: nothing is verified, and it must be checked against the channel and the book before use.

**B. Script development (WI-0086 Raindrop, pdf 289–292).** Structure only, in our words:
assumption (all moisture becomes one sphere) → first consequence (the sphere exists, over 1 km wide) → escalation (it falls, picks up speed) → surprise (impact pressure beyond the deep ocean) → payoff (scoured ground, floods downstream). Our narration must be written fresh around our own object.

**C. Science verification.** WI-0086 recomputed here: 100 km × 100 km × 6 cm = 0.6 km³ = 600 million tonnes (book number reproduced). Sphere diameter ≈ 1.05 km (reproduced). Fall from 2 km with no drag: 20.2 s, 198 m/s; the book gives ~20 s and >200 m/s, so it matches. The book's ~90 m/s at 10 s is below the drag-free 98 m/s, which is consistent with air drag (INFERRED). WI-0033: the book states Baumgartner reached Mach 1 near 30 km. A search confirms about 39 km jump height and Mach 1.25 peak. The 30 km figure was **not** independently confirmed. Where our scenario differs (a bowling ball on a trampoline is not a free-fall-to-impact question), reuse only the free-fall and energy ideas.

**D. Storyboard development (original sequences).**
- *WI-0086, pdf 290–292:* (1) a wide pale sky with one dot of cloud, a small ruler beside it reading "2 km". (2) the dot swells into a grey ball bigger than the ruler, hard cut. (3) the ball drops past three tick marks; a red speed number steps up beside it, one pop per tick. (4) cut to ground level, flat line, ball touches, everything beside it becomes ring-shaped streaks outward. (5) final frame: the ring labelled with distance. Physical consequence is always visible as a label or ring.
- *WI-0033, pdf 123–125:* (1) a steak on a platform at the top of a tall vertical scale. (2) step the platform down the scale in four pop-ons (39, 70, 100, 250 km). (3) at each stop show the steak with a different outside colour and a cut-open cross-section beside it. (4) final: cross-section with raw centre. Each beat swaps the cross-section, so the audience reads "outside changes, inside does not".

**E. Originality.** `ORIGINALITY_ROOM.csv`: 60 book questions are not on the channel by title or script match; 39 of them also have no keyword overlap with any channel title. Two possible near cases flagged for a human: WI-0047 Everybody Out vs `oBWqlxDd8sU` (human population), WI-0062 Free Fall vs shorts with "place/earth" words (probably noise). 30 of the 60 are structured-tier (best starting pool): WI-0033, 0034, 0035, 0039, 0041, 0044, 0045, 0046, 0047, 0051, 0052, 0053, 0056, 0057, 0058, 0060, 0061, 0062, 0065, 0068, 0069, 0071, 0076, 0079, 0080, 0081, 0083, 0086, 0087, 0088 (only 0047 and 0062 have a keyword near hit). This is a keyword title match, so premise-level duplicates inside video scripts are UNKNOWN.

Limit: the channel adapts book chapters, so using the same chapters is not original. Our pilot (bowling ball on a trampoline) has **no** matching book question (searched drop/fall/jump/bounce/spring/trampoline).
