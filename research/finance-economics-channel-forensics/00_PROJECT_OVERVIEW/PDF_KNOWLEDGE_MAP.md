# PDF Knowledge Map — the JUDGE

**Source A:** `YouTube_Automation_Complete_Master_Playbook.pdf` (user-supplied, ~/Downloads), 556 pages, A4, compiled 11 Nov 2026, sha256 `c630c24bc189ac39558387109bc865df71a9b52a1dea70accc971daf1624576d`. Not modified; not copied into the repo.

## 1. Actual structure (from the PDF's own Contents, pp.1-2)

| Part | Section | PDF pages |
|---|---|---|
| A — Course lessons & topic selection | Module 2.1 The Outlier Concept | 6-9 |
| | Module 2.2 Niche vs Format vs Template | 11-16 |
| | Module 2.3 Format Arbitrage | 18-22 |
| | Module 2.4 Niche Bending | 24-26 |
| | Module 2.7 Competitor Research Deep Dive | 28-31 |
| | Topic Selection Masterclass intro + Method 1 Outlier Transplant | 33-37 |
| | Method 2 Title Template Injection | 39-42 |
| | Method 3 Cross-Niche Format Snatch | 44-46 |
| | Method 4 Demand/Supply Gap Scan | 48-50 |
| B — Standalone references | 100 YouTube Title Formats Complete Playbook | 52-70 |
| | Topic Validation Prompt (Topic Opportunity Validator) | 72-80 |
| C — 20-document archive | Niche Research Keyword Generator | 82-95 |
| | Niche Bending Validation Prompt | 97-109 |
| | Format Arbitrage Validation Prompt | 111-120 |
| | Topic Repackage Plugin | 122-127 |
| | Title Psychology Breakdown Prompt | 128-133 |
| | Outlier Act Structure Analysis / Act Structure Analysis Prompt | 134-155 |
| | Script Writing Engine | 156-262 |
| | Engagement Techniques Playbook (18 techniques) | 263-284 |
| | AI Scriptwriting Workflow Prompt Guide | 286-317 |
| | Faceless YouTube Scriptwriting Masterclass (23 chapters) | 318-352 |
| | Master Faceless Script Audit | 353-393 |
| | Write-a-New-Script-from-Reverse-Engineered-Format prompt | 394-410 |
| | Prompt to add emotions in VO | 411-424 |
| | Explainer storyboard director (image-prompt pipeline) | 425-439 |
| | Celebrities compilation niche | 440-490 |
| | Practical Month setup + Niche Research Template | 491-531 |
| | Chats for script writing; prompt/document links | 532-553 |
| D — Independent web research (11 Nov 2026, official YouTube sources) | Additional Web Research | 554-556 |

Source caveats stated inside the PDF itself: several course pages are screenshot transcriptions with missing passages (e.g. Method 2 lists 9 of 10 title formats; Method 3 case study cut off; Lesson numbering inconsistent 2.3/2.4/2.5); Method 4 supply threshold is 50K+ in step 2 but 10K+ in the summary. Part D explicitly says the course numbers (10x outlier, 20+ outliers, 50+ topics, A/B/C/D supply grades) are **working heuristics, not official YouTube thresholds**.

## 2. Reading coverage (honest)

Text was extracted with `pdftotext` (page-tagged) on 2026-11-12.
- **Read in full:** pp.1-108 (all of Part A, Part B, Keyword Generator, Niche-Bending Validation up to its verdicts), pp.263-284 (Engagement Techniques Playbook), pp.318-352 (Faceless Scriptwriting Masterclass, incl. Ch.1 six zones, explainer/analysis script types, Ch.19 metadata rules, Ch.22 retention heat map, Ch.23 checklist), pp.425-439 (Explainer storyboard), pp.554-556 (Part D).
- **Read at outline/rule level (headings + rule lines, not every sentence):** pp.109-262 (Format-Arbitrage validator, Repackage plugin, Title psychology prompt, Act-structure prompts, Script Writing Engine), pp.285-317, pp.353-424, pp.440-553. These are predominantly reusable *prompt templates and production workflows*; their evaluative rules duplicate the principles below (outlier ratio, payoff test, celebrity-power test, topic inventory, act structure, hook/stakes/loops). No principle in this study is attributed to a page that was not read.

## 3. Principles converted into evaluation criteria (used in every channel report §16)

| ID | Principle (PDF location) | Criterion applied to a channel | Evidence used (this dataset) | Testability |
|---|---|---|---|---|
| P01 | Outlier concept & transplant (2.1 pp.6-9; M1 pp.34-35) | Does the channel produce outliers vs its own baseline, and does it *exploit* them (repeat the winning topic soon after)? | PI (views ÷ median of 15 nearest uploads); topic of next 10 uploads after each ≥2x video vs base rate | Partial (observes behaviour, not the creator's research) |
| P02 | Niche = audience + persistent interest (2.2 p.11) | Coherent audience; videos feel like one channel | top-2 topic share; explicit audience markers in titles; analyst reading | Testable |
| P03 | Many formats inside one niche (2.2 pp.12-13) | ≥3 formats in regular use | title-format mix | Testable (title proxy) |
| P04 | Avoid repetitive/mass-produced content (2.2 p.13; Masterclass p.351; Part D §7) | Distinct substance per video | near-duplicate script (8-gram Jaccard ≥0.25 on first 400 words); repeated title word-sets | Testable |
| P05 | Format arbitrage / niche bending (2.3-2.4) | Does the channel use a format/niche combination that is novel for finance? | Analyst judgement only | Mostly NOT TESTABLE (needs launch-time landscape) |
| P06 | Competitor research; cover proven topics originally (2.7 pp.28-30) | Topic overlap with other channels; who published first | cross-channel title word-set overlap + first-publisher | Partial |
| P07 | Title template injection / 100 formats (pp.39-40, 52-64) | Use of the 10 title psychology families, and whether it helps | regex match to families; median PI with vs without | Testable (correlation only) |
| P08 | Five-part title engine: subject, situation, trigger, tension, promise (p.53, p.66) | Specific subject + stakes | number/$/named entity in title; PI contrast | Testable (proxy) |
| P09 | 12 title mistakes (p.68; Masterclass p.345) | Avoid ALL CAPS, vague openers, two promises | caps-word count, vague openers, double questions | Testable |
| P10 | Title + thumbnail = one promise, thumbnail adds a clue (p.66, p.68 #11) | Thumbnail text complements, not repeats, title | OCR overlap of thumbnail words with title | Testable (OCR-limited) |
| P11 | Thumbnail teardown: colour, text, faces, focal point, consistency (p.28) | One clear idea, few words, consistent identity | OCR word count, face detection, analyst view of montages | Testable (montage) |
| P12 | Opening hook in first 3-5 s (pp.265, 320) | Question / shock stat / contradiction / story drop / direct challenge; no greeting | first ~13-75 transcript words | Testable (untimed approximation) |
| P13 | Stakes frame 5-15 s (p.320, p.283) | Early “why should I care” tied to viewer money/safety | stakes / why-it-matters lexicon in opening | Testable (proxy) |
| P14 | Open loop before 30 s (p.320, p.350) | Explicit loop/promise phrase early | loop/promise lexicon in first ~150 words | Testable (proxy) |
| P15 | Micro-cliffhangers / bridging teases (pp.267, 272) | Bridges at transitions | bridge-phrase density | Testable (proxy) |
| P16 | Authority & credibility drops (p.273) | Precise numbers, named sources | data/citation density; institutions named | Testable (proxy) |
| P17 | Direct address (p.271) | Second person | you/your density | Testable |
| P18 | Future pacing & CTA placement (pp.280-284) | Next-video tease at the end; CTA after payoff | tease lexicon in last ~60 words; CTA in final 10% | Testable (proxy) |
| P19 | 8+ min sweet spot (p.19) vs Part D §8 (8 min = mid-roll rule only) | Length and its relation to performance | median length; Spearman(duration, PI) | Testable |
| P20 | Posting cadence & dead periods (p.29) | Consistency and pauses | median gap, gap CV, longest pause | Testable |
| P21 | Topic selection IS the production (p.33) | Does topic explain more performance spread than title format? | ratio of best/worst median PI across topics vs across title formats | Testable (within channel) |
| P22 | Content must deliver the title promise (p.40, p.68 #12, p.345) | Opening confirms promise | share of title keywords spoken in first ~150 words | Testable (proxy) |

**Principles extracted but NOT testable with this dataset** (stated, never faked): demand/supply gap scoring from YouTube search (M4 pp.48-50) — no search-result data; comment-section intelligence (p.29) — no comment text; CTR/AVD validation of arbitrage and bends (pp.19, 25) — no Studio data; VidIQ/TubeBuddy/Social Blade growth inflections (pp.7, 29) — not collected; A/B title tests (Part D §5); retention heat-map dips (Masterclass Ch.22, Part D §6); voice-over emotion and visual production prompts (pp.411-439); celebrity-power and payoff tests from validation prompts are applied qualitatively only where relevant.

## 4. How verdicts are assigned
`03_principles.py` computes the evidence string and a **draft** verdict with fixed thresholds (documented in code). Analysts override drafts in `_analysis/<channel>.md` (section `pdf`) when reading the transcripts/thumbnails shows the proxy is wrong — overrides are shown in the report's “Analyst note” column. Verdict scale: FOLLOWED · PARTIALLY FOLLOWED · NOT FOLLOWED · CONTRADICTED BY EVIDENCE (the channel does the opposite and still wins, or the principle predicts the wrong direction inside the channel) · NOT TESTABLE · INSUFFICIENT DATA.
