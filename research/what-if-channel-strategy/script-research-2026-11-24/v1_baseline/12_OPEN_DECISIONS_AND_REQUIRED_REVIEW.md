# 12 — Open decisions and required review (2026-11-24)

## A. Owner decisions
1. **Slots 01 and 02 versus the existing Day 1/Day 2 work.** `productions/unreasonably-exact-01-free-fall/` (v3, owner-approved 2026-11-19, ladder from 1 m to 400 km) and `unreasonably-exact-02-slow-before-landing/` (draft v1) are untouched. This package gives alternative drafts built on the locked calendar's own questions (1 km vs 100 km; the slow-down mechanism). Choose: keep v3/Day 2, use ours, or merge. Numbers differ on purpose: v3 prints 204 km/h (calibrated fit) and "about five g"; ours prints ~190 km/h with a 160–200 range and no g value.
2. **Slot 10 overlap with Munroe's "Loneliest Human".** Exact question overlap, disclosed. Our framing differs (nearest-neighbour definition, three record types, 2R+h geometry, Artemis II 2026 contrast). Choose: keep, or reframe with an alternative title. Put the overlap disclosure in the description.
3. **Slot 06 and the live 2026 outage.** Paragraphs 11–12 state NASA's status as of 2026-11-20 posts (checked again 2026-11-24, no later update found). Choose: keep and rewrite on production day, or cut them (Long ≈ 3:15).
4. **Titles.** Recommended titles are in each TITLE_AND_PACKAGING.md; the calendar file was not edited. Slot 05 narrows "a moon" to Phobos.
5. **Lengths.** Longs estimate 3:45–4:45 (owner band 3–5 min). Shorts estimate 57–63 s at 2.7 words/s + 1.5 s per paragraph; trim one sentence if a recording runs long.
6. **Repository placement.** Nothing was saved inside the repo or committed. To use the slop gate's automatic hooks, scripts would have to be moved under `productions/<project>/` with a header block; that is a separate instruction.
7. **On-screen honesty labels** (MEASURED / CALCULATED / MODEL / ASSUMED) are proposed in the framework; confirm before production.

## B. Required expert or human review (none has happened)
| Topic | Claim IDs | Reviewer needed |
|---|---|---|
| Drag range, constant Cd to Mach ~3, density above 86 km, heating | V01-C07, C10, C11, C12, C15; V02-C02..C04 | aerodynamics / atmospheric-flight |
| Toy-orbit statements (circular vs elliptical, tilt) | V04-C05, C09, C11, C12 | physicist |
| Jump and sprint speeds | V04-C07, C08; V05-C03 | biomechanics source |
| Phobos fall-back, escape thresholds, shape/spin/Mars | V05-C04, C05, C08 | planetary dynamicist with shape model |
| Voyager 2024 repair wording | V06-C06, C07, C09 | optional spacecraft engineer; read the 2024-04-04 NASA post |
| Ocean response, decay, local timing, "two highs a day" | V08-C04, C05, C08, C10; V09-C06 | physical oceanographer |
| Tilt / seasons / day length (excluded) | V08-C12, C13 | astronomer; read Lissauer 2012, Laskar |
| Lunar-laser return rates and precision | V07-C07, C08 | LLR instrument expert; read Murphy 2013 |
| Apollo 15 orbit height / alignment | V10-C04 | mission-report check |
| All scripts | — | a human editor / listener for tone, clarity, imitation of Munroe's beats |

## C. Time-sensitive rechecks (do on production day)
- NASA Voyager status, distance, speed and wording (V03-C03, C06; V06-C10, C11, C12).
- Guinness "most isolated" record status and wording (V10-C02); Artemis II records (V10-C06).
- Eustace/Baumgartner/FAI records (V01-C13, C14).
- YouTube Shorts length and view-count rules (not used in the scripts, but affects the ≈60 s target): official pages were read only through a summarising tool.

## D. Not read, or read only partly (honest list)
- 83 xkcd transcripts: read in full by four reader sub-agents; the lead read their notes and summaries, not the raw transcripts. No xkcd video was watched; no audio, picture or thumbnail was inspected.
- DS-000011: 12 creative documents read in full by one sub-agent; SEO checklist, two prompt guides and two algorithm compilations not read (INDEX_ONLY). DS-000011 supplement = DS-000018 (same Google Doc; counted once); only the first/last parts of the 63 tabs were compared programmatically, not read.
- YouTube Automation Master Playbook: found at `/Users/ghilmanislam360/GhilmanProjects/dr rehan videos editing/YouTube_Automation_Complete_Master_Playbook.pdf`; about 10% read (chapters 1-3, 12, 16, 19, 23, Part D). DS-000031: first ~420 lines read in full.
- Existing archive: rule ledger, playbooks, synthesis, count reports read in full; 8 of 83 earlier audits skimmed.
- Munroe book: read through imperfect OCR in an earlier session; What If? 2 not available.
- Murphy 2013 lunar-laser review PDF could not be read by the fetch tool (9 MB); the APOLLO instrument paper was read through a text extraction (figures not seen). Lissauer 2012 and Laskar not read.
- Official web pages were read through a summarising fetch tool, not opened page-by-page in a browser.

## E. Reviews that do not exist
Expert review; human listening/audio review; independent reviews by other AI systems (none were run: the "seven lenses" are Claude self-review lenses); viewer, retention, CTR or audience data; any A/B test of titles or thumbnails.
