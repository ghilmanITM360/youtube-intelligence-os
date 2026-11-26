# How the Playbook was (and was not) applied to the ten videos

Evidence class for everything below: **creator guidance**, used only where it agrees with our own rules or with the xkcd transcripts. Page numbers refer to the PDF.

## Applied to all ten scripts
| Playbook guidance | Page(s) | How it is applied |
|---|---|---|
| Title promise = script promise; the last paragraph must answer the title | 40, 66, 68, 170, 248, 355 | Every `FACT_CHECK_V2`/`TEN_SCRIPT_FINAL_REVIEW_V2` has a "title promise check" line. |
| Five-part title engine (subject, situation, trigger, tension, promise) | 53, 156–158 | `TITLE_AND_PACKAGING_V2.md` writes the five parts for each title. |
| Title scorecard with "unsupported claim is a veto" | 66 | Used as a decision aid only (not a CTR predictor); veto applied to absolute words. |
| Qualify "every, only, first, best, last, real reason" | 68 | Titles and narration avoid unqualified absolutes. |
| Fact sheet / claim ledger with source, date, confidence; flag uncertain items | 291–292, 304, 495 | `MASTER_SCIENCE_CLAIM_LEDGER_V2.csv`; time-sensitive items carry a date. |
| "Rewrite cautiously or omit unsupported blueprint claims" | 228 | Used for every sentence in `SCRIPT_SENTENCE_LEVEL_CORRECTIONS.csv`. |
| No stock openings, no AI phrases, vary sentence length, write for the ear, no visible act labels | 230, 233, 236–237, 261, 382–383, 407 | Seventh-lens checks; banned-phrase scan on every script. |
| Clarity for a listener who cannot re-read: few numbers, defined terms | 374 | Spoken numbers limited and rounded; units defined at first use. |
| Open loops must close or the uncertainty be stated | 203, 218 | Each beat sheet has a question table with a resolution column. |
| "Do not withhold simple facts purely to extend the video"; no artificial cliffhanger | 179, 235 | Verdict or limit is stated when the reasoning reaches it; no teaser lines. |
| Word count verified by a tool, not by paragraph count | 242–243 | `wc`-style count in `SCRIPT_V2.md` (spoken text only). |
| Read aloud before trusting runtime | 298, 323 | Runtime is labelled an estimate; real recording is still needed. |
| Short = standalone piece | 307, 423 | Each Short names the premise in sentence one, speaks every number, repeats nothing from its Long. |
| Policy-safe framing: source → information → complexity | 342 | Used for uncertain science statements (Moon/ocean, Phobos, lunar laser). |
| Visuals originate from the explanation; asset rights documented | 303, 497 | Beat sheets describe original diagrams only; no media is stored in the repo. |

## Applied to specific slots
| Slot | Playbook device | Page(s) | Note |
|---|---|---|---|
| 01 Higher Fall | Contrast and comparison, side-by-side numbers; "X vs Y" title family | 59, 274 | Two heights, one set of numbers; contradiction family (p57) honest because the near-equality is a model result. |
| 02 Skydiver slowdown | Explainer: simple layer then precise layer | 328, 335 | Mechanism first, numbers second; no safety claims. |
| 03 Voyager signal | Authority drop: precise number, source, date anchor | 273 | Distance/speed with NASA date; no invented daily-growth figure. |
| 04 Tiny-world orbit | Explainer; "What happens when X is removed" style subtraction | 63, 335 | Toy world labelled as such. |
| 05 Phobos | Mystery/unsolved rule: "never pretend to solve what is unsolved" | 312, 334 | Ending states model result and real uncertainty together. |
| 06 Voyager repair | Documentary/explainer; "Evidence → interpretation" transitions | 239, 326 | Distinct 2024 repair story, dated NASA sources. |
| 07 Lunar laser | Credibility drops; "be specific about instrument" | 273 | Instrument-specific figures only. |
| 08 Moon vanishes | "What happens when X is removed?" title (088); counterfactual labelling | 63, 64 | Separates transient motion, solar forcing and local response. |
| 09 Sun's tides | Misconception → real explanation (only if real) | 328 | No universal fraction. |
| 10 Farthest human | Attribution of records to sources | 330 | Guinness definition cited; geometry labelled as calculation. |

## Deliberately NOT applied
Pattern-interrupt timers (15–30 s, 20–30 s, 30 s); micro-cliffhangers at transitions; false resolution; "viewer qualification" lines; CTA at 50–70%; next-video future pace; hooks that promise secrets; personal-risk stakes ("this could save your life"); numeric "engagement density" and technique counts; 8-minute length target; competitor style mimicry and reference-image storyboard cloning; invented statistics of any kind. Reasons are in `PLAYBOOK_COMPLETE_REVIEW.md` §4.

## Seven analytical lenses and the Playbook's analyzers
The title, intro and script analyzers (pp 128–132, 134–146, 244–261, 353–392) were used as **checklists inside Claude's own self-review**. Their scores are editorial judgments by one model; they are not independent reviews and not predictions of audience behaviour.
