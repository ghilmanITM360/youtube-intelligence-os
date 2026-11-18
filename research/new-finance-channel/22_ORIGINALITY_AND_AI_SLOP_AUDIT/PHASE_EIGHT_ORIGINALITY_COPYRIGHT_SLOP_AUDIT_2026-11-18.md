# Phase Eight: originality, copyright and AI-slop audit (master "Phase Eight"), 2026-11-18

Status: audit of the concepts and formats we have, not of scripts (none exist). This is a risk assessment, not legal advice. Labels: VERIFIED / PAPER_FACT / OUR_INFERENCE / HYPOTHESIS / UNKNOWN. No AI tool is declared a violation by itself; risk is judged by originality, transformation, sourcing and the official policy text.

## 1. Frameworks located and used
| Framework | What it is | Used here for |
|---|---|---|
| `docs/policies/AI-SLOP-RISK-RULES.md` + `scripts/check_slop_risk.py` | Our gate: R1 to R7 automatic checks, manual checklist C1 to C5; derived from one 4-page Google paper (PAPER_FACT F1 to F6) | Section 4 and 5 mapping |
| Official YouTube pages, fetched 2026-11-18 (Phase A): 1311392 (monetization: inauthentic, reused content), 14328491 (altered or synthetic content disclosure), 16391400, 6175006, 7628154, 9314355 | Platform policy | Section 3 |
| `data/knowledge/reference_knowledge.db` framework | Rule classes, mandatory for content plans | Not queried in this pass; any real content plan must pass `run_youtube_intelligence.py --framework-plan` (structural check only) |
Limit: the paper's strongest signals (account infrastructure, API use, upload timing) cannot be seen in a script. The gate is a proxy; a PASS never means "will not be detected".

## 2. A. Inspiration versus copying (by element)
| Element | Acceptable transformation (our rule) | Copyright or policy risk | Our status |
|---|---|---|---|
| Topic | Same subject is fine; subjects are not owned | none by itself; high overlap raises look-alike risk | rent and airfares are public-data subjects |
| Concept | Reuse the idea "explain a price" with our own mechanism and sources | low | Concept 1 + 2 |
| Title | Own wording; no title identical or near-identical to a competitor's | reusing a competitor's exact title is the R2 FAIL; Senior Health work found a network sharing titles word for word | candidate titles checked: highest word overlap with any of 3,832 DB titles is 0.36 (warn level is 0.8); lexical, DB only, not the whole of YouTube |
| Thumbnail | Own layout, own palette, real data chart; no round-head cartoon, no animal cast | copying a thumbnail composition or character is look-alike risk and R7 (dHash) FAIL | briefs only; no image exists yet; R7 cannot be run |
| Script structure | Learn the pattern (fact, contradiction, mechanism); write from our own research | reproducing a competitor's structure beat for beat, or paraphrasing a transcript, is R1 and "reused content" | no script exists; R1 untested |
| Visual presentation | Real charts with source and date; own flat style | cloned templates across a channel are the "mass-produced" signal | design decided in branding phase |
| Editing | Pace and cuts are techniques, not protectable | none, but frame-level editing analysis is NA in our data | not analysed |
Never recommended and never to be done: downloading a competitor video and publishing it with small changes; re-voicing or spinning a competitor script; using their characters or thumbnails; adding noise to pass a threshold (the rules call this itself a violation).

## 3. Policy position (VERIFIED from the pages read in Phase A, not re-read today beyond Phase A)
1. Repetitive or mass-produced content is "inauthentic" and not monetizable; channel-level review. Reused content needs significant original commentary or transformation.
2. AI-generated personas presenting as human experts who give financial advice are not monetizable.
3. Content that only reads out text from websites or news feeds is not monetizable.
4. Realistic altered or synthetic content must be disclosed; non-realistic visuals, script help and own-voice cloning do not need it. Disclosure alone does not limit reach or monetization.
Copyright: thumbnails, footage and music of others are copyrighted; charts we build from public data (BLS, IATA) are factual data, but the exact layout of someone else's chart is not ours. Licensing for stock, music and fonts is UNKNOWN until the production workflow phase.

## 4. B. Originality audit of each shortlisted concept
Questions from the master list, answered for what exists today (HYPOTHESIS where the video does not exist yet).
| Question | V1 Rent | V2 Airfares | V3 Industry test (ports) |
|---|---|---|---|
| Original angle? | yes: two measurement systems (6-month BLS sample vs market asking rents) | partly: BLS fare index vs IATA margin; news-driven | yes, if sourced per video; topic itself not yet validated |
| Developed from independent research? | not yet; primary BLS data read, market series NOT obtained | primary BLS and IATA read; fuel table and fare sample not obtained | none yet |
| Original examples? | needs a real unit-rent worked example from public data | "follow one ticket" needs a real fare sample (the $400 in Phase E was illustrative) | needs real port fee schedules |
| Meaningful added value? | yes if the number comparison is shown with sources | risk of being a read-out | HYPOTHESIS |
| Visuals original or licensed? | to build: charts from BLS data | to build: charts from BLS/IATA | to build |
| Only a rewrite of a competitor video? | no: no DB video answers it; but 8 pipeline copies of the exact angle exist, all tiny | no, but 4 pipeline copies in 3 days | unknown |
| Repetitive template feel? | risk grows if every video is "two numbers disagree" | same | same |
| Human editorial input? | policy default adopted: named human or labelled voice, human checks every number (C5) | same | same |
Verdict: V1 and V2 pass the concept-level originality test only if the video adds a primary-data comparison; neither is safe as a read-out. V3 is untested.

## 5. C. AI-slop risk by format
| Format or practice | Risk (HYPOTHESIS) | Why / mitigation |
|---|---|---|
| Generic AI narration with no named presenter | HIGH | policy item 2 plus R6; use named human or clearly labelled narration |
| Repetitive scripts across videos | MEDIUM to HIGH | R1 and R4 only catch lexical overlap; a fixed "number, contradiction, mechanism" arc is fine, identical sentences are not |
| Reused visual templates | MEDIUM | one colour style is branding; the same animated layout in every video is the signal; vary composition by story |
| Mass-produced animations | HIGH if automated | not planned; no animation pipeline chosen |
| Low-value slideshows (images over voice) | HIGH | avoid; charts must show data |
| Unoriginal or poor research | HIGH in finance (YMYL) | primary sources on screen; C5 human check |
| Misleading financial claims | HIGH | numbers labelled as forecast, sample, estimate; no advice; no "will" for forecasts (corrected in Phase E, "Airlines Will Make" became "Are Forecast to Make") |
| 30-video templated calendar | MEDIUM | whole-channel review; Phase Eleven keeps a short rolling plan |
| Shorts as clones of long videos | MEDIUM | each Short carries one number and one contradiction with its own script |
| Upload cadence in bursts | MEDIUM (F3 pacing) | C1: steady human cadence; no bulk scheduling |
| Several channels run from one account, template or API (cluster) | HIGH | C2: this project must not become a Generation Cluster with the other channels in the repo; separate accounts, tools and scripts |

## 6. Gate readiness
- The gate runs on scripts in `productions/<project>/**/*SCRIPT*.md`. None exists, so it has not been run on any of our content. I did not run it on titles because R2 needs a script's header; the title check above is my own word-overlap pass.
- Manual C1 to C5 for this project: C1 not applicable until upload; C2 owner must confirm separate accounts and tools; C3 only if realistic synthetic visuals are used (not planned); C4 no cloned voice or invented expert; C5 human must check every number before publish.

## 7. Decisions needed from the owner
1. Voice: confirm "named human or clearly labelled narration, no AI expert".
2. Confirm channel separation from the other YIOS channels (C2).
3. Confirm music, font and stock licensing source before production.
