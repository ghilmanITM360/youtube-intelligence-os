# Chronofold — Channel Forensic Report

Channel #064 of 69 · investigation tier 3 (data-availability order, not a quality rank) · research date 2026-11-12 · source DB `finance_economics_complete.db` sha256 fa6fd1b2…d20 (branch data/finance-economics-complete-2026-11-11 @933f236e).

Evidence labels used: **VERIFIED** (directly in DB / public page), **INFERRED** (derived from DB text by rule or analyst reading), **HYPOTHESIS** (plausible, untested), **UNKNOWN**. Public view counts do not reveal CTR, retention or traffic sources; none of those are claimed.

**Key conclusion:** INSUFFICIENT DATA: two country-history videos — **"The ENTIRE History of Afghanistan in 15 Minutes" (425k, Sep 2026)** and "…Switzerland in 15 Minutes" (1.8k, Oct) — no transcripts, no metadata beyond titles/views; only a subject contrast can be noted (conflict-famous country vs stable country).

## 1. Channel identity and positioning
UNKNOWN beyond titles (no description, subscribers or transcripts in DB). Format: "The ENTIRE History of [Country] in 15 Minutes" (same template family as Built On You).

## 2. Database inventory and coverage
- Channel ID `UCN87LLx0N_ZZ9BZBegN1WXA` · handle nan · https://www.youtube.com/channel/UCN87LLx0N_ZZ9BZBegN1WXA
- Registered sub-niche: nan · subscribers: n/a · availability: AVAILABLE nan
- Description: nan
- Videos in DB 2 (long 2, Shorts 0); views 2; transcripts 0 (0%); thumbnail images 2 (100%); FULL metadata 100%; PI-classified long 0
- Dates 2026-09-05 → 2026-10-17; median views 213,479; p90 382,859; max 425,204
- Titles whose word-set also appears on another channel: 0 (0%)

Per-video field status (AVAILABLE / MISSING / UNVERIFIED / NOT APPLICABLE) is in `VIDEO_INVENTORY.csv`. Note: the source DB was capped at ~100 newest uploads per channel for most channels, so this is not the full lifetime library.

## 3. Complete video catalogue
All 2 videos in the database (also `VIDEO_INVENTORY.csv`). PI = views ÷ median of 15 nearest-in-time uploads (same channel & format); blank PI = not classifiable (too new/too few comparables).

| # | date | title | min | views | PI | class | topic | title format | transcript |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-05 | [The ENTIRE History of Afghanistan in 15 Minutes](https://www.youtube.com/watch?v=nB3WRMupmW4) | 15.0 | 425,204 |  | NOT_CLASSIFIED | money_history | statement_other | N |
| 2 | 2026-10-17 | [The ENTIRE History of Switzerland in 15 Minutes](https://www.youtube.com/watch?v=-2_MAElCGCc) | 15.0 | 1,754 |  | NOT_CLASSIFIED | money_history | statement_other | N |

## 4. Topic and sub-niche map
| topic | n | long | median views | median PI | succ/breakout | under | first | last |
|---|---|---|---|---|---|---|---|---|
| money_history | 2 | 2 | 213,479 | n/a | 0 | 0 | 2026-09-05 | 2026-10-17 |

Title-format mix (INFERRED tags): statement_other: n=2.0, medPI=n/a

Country histories (off the finance core).

## 5. Winning video analysis
Afghanistan (425k) — globally newsworthy history.

### Evidence: top-PI long-form videos


## 6. Underperforming video analysis
Switzerland (1.8k) — lower curiosity; also newer (age confound).

### Evidence: bottom-PI long-form videos


## 7. Successful vs failed comparison
n=2 — no conclusions beyond subject salience (HYPOTHESIS).

_Too few classified videos for a contrast._



## 8. Topic discovery and research sources
NOT AVAILABLE (no transcripts).

Institutions named in transcripts/descriptions (rule-based; 'Academic / research study' matches generic words like “study/research” and is low-confidence): none detected
Description link domains: none
Per-video source map: `SOURCE_MAP.csv`.

## 9. Trend behaviour
UNKNOWN.

## 10. Thumbnail strategy
2 images exist; not inspected.

## 11. Title strategy
"The ENTIRE History of [X] in N Minutes".

## 12. Hook and introduction strategy
NOT AVAILABLE (no transcripts).

## 13. Script and storytelling strategy
NOT AVAILABLE.

## 14. Audience engagement model
UNKNOWN.

## 15. Upload and publishing strategy
2 uploads.

## 16. PDF principle evaluation
Judge: *YouTube Automation – Complete Master Playbook* (556 pp., sha256 c630c24b…576d). Supporting authority: global-youtube-knowledge (DS-000011/18/31) — see `00_PROJECT_OVERVIEW/GLOBAL_KNOWLEDGE_MAP.md`. Automated evidence uses text proxies; verdict = analyst override where noted, else rule-based draft.

| ID | PDF principle (location) | What the PDF says | Evidence from channel (automated, incl. winners vs rest where testable) | Verdict | Analyst note |
|---|---|---|---|---|---|
| P01 | Module 2.1 Outlier Concept, pp.6-9; Method 1 Outlier Transplant, pp.34-35 | Find videos that beat the channel norm (5-10x strong, 10x+ clear outlier) and treat their TOPIC as proven demand; build the calendar from validated outliers. | only 0 PI-classified long-form videos | **INSUFFICIENT DATA** | only 2 videos; all other principles INSUFFICIENT DATA or NOT TESTABLE (no transcripts). |
| P02 | Module 2.2 Niche vs Format vs Template, p.11 | A niche is an audience + persistent interest + monetisation path, not a topic; every video should feel like it belongs to the same channel. | top-2 topics (money_history) = 100% of uploads; explicit audience marker in 0% of titles | **FOLLOWED** |  |
| P03 | Module 2.2, pp.12-13 | One niche can carry many formats; add formats to grow without changing niche. | 1 title-format types each ≥10% of uploads (statement_other 100%) | **NOT FOLLOWED** |  |
| P04 | Module 2.2 p.13; Masterclass Ch.23 p.351; Web research §7 p.555 | Avoid repetitive/mass-produced uploads; rotating templates alone is not enough — each video needs distinct substance (inauthentic-content policy). | near-duplicate-script flag on 0% of videos; repeated title word-sets within channel 0% | **FOLLOWED** |  |
| P05 | Module 2.3 Format Arbitrage pp.18-20; Module 2.4 Niche Bending pp.24-26 | Win by transplanting a proven format into a niche that lacks it, or by combining two overlapping niches. | requires historical competitor-format landscape at launch; analyst note in report if a bend is visible | **NOT TESTABLE** |  |
| P06 | Module 2.7 Competitor Research pp.28-30; Method 1 p.34 | Study competitors’ top videos, titles, thumbnails, cadence and comments; cover proven topics with original content. | 0% of titles share a word-set with another channel; this channel published first on 0 of 0 | **NOT FOLLOWED** |  |
| P07 | Method 2 Title Template Injection pp.39-40; 100 Title Formats pp.52-64 | Inject niche topics into proven title psychology families (mystery, downfall, contradiction, revelation, practical, conflict…), but the content must deliver. | 100% of titles match a 100-format family | **FOLLOWED** |  |
| P08 | 100 Title Formats p.53 (five-part engine), p.66 scorecard | A strong title names a recognisable subject, a situation, a trigger, a tension and a concrete promise/stakes. | 100% of titles carry a number/$/named entity | **FOLLOWED** |  |
| P09 | 100 Title Formats p.68 (12 mistakes); Masterclass Ch.19 p.345 | Avoid generic subjects, two promises, vague “this/they” openers, ALL CAPS overuse, overstated certainty. | titles with ≥3 ALL-CAPS words 0%; vague 'this/they' opener 0%; double-question 0% | **FOLLOWED** |  |
| P10 | 100 Title Formats p.66 (title+thumbnail one promise), p.68 #11 | Thumbnail should add a complementary clue, not repeat the title. | OCR thumbnail text found on 100%; median share of thumbnail words repeated from title 0.50 | **PARTIALLY FOLLOWED** |  |
| P11 | Module 2.7 Thumbnail Teardown p.28 (supporting: DS-000011 Packaging SOP) | Study colour, text amount, faces/expressions, focal object, contrast and template consistency; one clear idea. | thumbnail images 100%; median OCR words 4.0 (OCR undercounts stylised text); face/character detected 0% (cartoon faces often missed) | **FOLLOWED** |  |
| P12 | Engagement Playbook §1 p.265; Masterclass Zone 1 p.320 | The first ~3-5 seconds must create curiosity: question, shock stat, contradiction, mystery, story drop, direct challenge. | only 0 transcripts | **INSUFFICIENT DATA** |  |
| P13 | Masterclass Zone 2 p.320; Engagement §18 p.283 | Within ~5-15 s answer “why should I care?” — connect to the viewer’s money, safety or identity. | only 0 transcripts | **INSUFFICIENT DATA** |  |
| P14 | Masterclass Zone 3 p.320; Ch.23 p.350 | Open at least one curiosity loop before ~30 s and keep it open. | only 0 transcripts | **INSUFFICIENT DATA** |  |
| P15 | Engagement §2 & §7 pp.267, 272 | Use bridging teases / micro-cliffhangers at segment transitions to prevent drop-off. | only 0 transcripts | **INSUFFICIENT DATA** |  |
| P16 | Engagement §8 p.273 | Precise numbers, dates, named sources and expert quotes signal research and keep sceptical viewers. | only 0 transcripts | **INSUFFICIENT DATA** |  |
| P17 | Engagement §6 p.271 | Second-person address makes the viewer a participant (“if you own…”, “imagine you…”). | only 0 transcripts | **INSUFFICIENT DATA** |  |
| P18 | Engagement §15-16 pp.280-281; Deployment p.284 | Close loops, then future-pace to a next video; strongest CTA right after a payoff, not only at the end. | only 0 transcripts | **INSUFFICIENT DATA** |  |
| P19 | Module 2.3 p.19 (8+ min sweet spot); Web research §8 p.555 | Course: formats should fill 8+ minutes; appendix: 8 min is a mid-roll eligibility rule, length should follow the story. | median long-form length 15.0 min — 8+ min is an ad-eligibility rule, not a success rule (PDF p555) | **FOLLOWED** |  |
| P20 | Module 2.7 Posting cadence p.29 | Check upload frequency, consistency, dead periods and growth inflection points. | 1 dated gaps | **INSUFFICIENT DATA** |  |
| P21 | Topic Selection Masterclass intro p.33 | “A bad video on the right topic will outperform a great video on the wrong topic” — topic selection is the main lever. | 0 classified long-form | **INSUFFICIENT DATA** |  |
| P22 | Method 2 warning p.40; 100 Formats p.68 #12; Masterclass Ch.19 p.345 | Title gets the click, content keeps the viewer: the opening must confirm and the video must deliver the title’s promise. | median share of title keywords that appear in the first ~150 spoken words n/a | **INSUFFICIENT DATA** |  |

## 17. Strengths and weaknesses
Template shared with successful history channels.

## 18. Replicable working model
INSUFFICIENT DATA.

## 19. What to copy
Only the template observation.

## 20. What not to copy
Drawing conclusions from 2 videos.

## 21. Missing evidence and limitations
2 videos, 0 transcripts, no metadata.

- Not available from this dataset for any channel: CTR, impressions, retention curves, traffic sources, subscriber growth history, comments text. Hook timings are word-position estimates (untimed transcripts).

## 22. Final channel diagnosis
Documented exception: not enough evidence for a channel model.
"With two videos and no transcripts, there is no evidence-based model to replicate here."
