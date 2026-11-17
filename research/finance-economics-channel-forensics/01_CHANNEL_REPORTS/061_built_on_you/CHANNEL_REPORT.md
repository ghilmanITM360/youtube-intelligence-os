# Built On You — Channel Forensic Report

Channel #061 of 69 · investigation tier 3 (data-availability order, not a quality rank) · research date 2026-11-12 · source DB `finance_economics_complete.db` sha256 fa6fd1b2…d20 (branch data/finance-economics-complete-2026-11-11 @933f236e).

Evidence labels used: **VERIFIED** (directly in DB / public page), **INFERRED** (derived from DB text by rule or analyst reading), **HYPOTHESIS** (plausible, untested), **UNKNOWN**. Public view counts do not reveal CTR, retention or traffic sources; none of those are claimed.

**Key conclusion:** Five-week-old company-history channel (15.4k subs, 10 videos, too new/few for PI): **"The ENTIRE History of [mega-brand] in 20 Minutes"** — Amazon (431k), Toyota (242k), Costco (188k), Walmart (135k), Microsoft (113k) — while Nike, Tesla, Nintendo and Samsung got 2-38k and a format break ("The Rise and Fall of Blockbuster in 10 Minutes", 3k) flopped. Within one fixed template, *which brand* decides views.

## 1. Channel identity and positioning
Description (VERIFIED): "Built On You tells the complete history of the world's biggest companies in a single sitting". Faceless documentary; ~20 min. Audience: business-curious general viewers.

## 2. Database inventory and coverage
- Channel ID `UC8p5EKG8jlsL2R2bvr2fZ3g` · handle @BuiltonYou · https://www.youtube.com/channel/UC8p5EKG8jlsL2R2bvr2fZ3g
- Registered sub-niche: company histories · subscribers: 15,400 · availability: AVAILABLE nan
- Description: Every company is built on something. A shortage. A habit. A gamble. Most of the time, it is built on you.  Built On You tells the complete history of the world's biggest companies in a single sitting, from the founder's first strange idea to the empire, the scandals and the market cap they carry today. Amazon, IKEA, Walmart, McDonald's, Stripe, Coca-Cola, Nike, Toyota and more, told in order, with…
- Videos in DB 10 (long 10, Shorts 0); views 10; transcripts 10 (100%); thumbnail images 10 (100%); FULL metadata 100%; PI-classified long 0
- Dates 2026-10-04 → 2026-11-10; median views 75,261; p90 260,433; max 430,614
- Cadence: 8.2 uploads/month over 1.2 months; median gap 3.0 d; max gap 8 d; weekday mode Tuesday
- Duration (min): median 20.0; p10 17.1; p90 21.0; first-third median 20.0 vs last-third 17.9
- Titles whose word-set also appears on another channel: 0 (0%)

Per-video field status (AVAILABLE / MISSING / UNVERIFIED / NOT APPLICABLE) is in `VIDEO_INVENTORY.csv`. Note: the source DB was capped at ~100 newest uploads per channel for most channels, so this is not the full lifetime library.

## 3. Complete video catalogue
All 10 videos in the database (also `VIDEO_INVENTORY.csv`). PI = views ÷ median of 15 nearest-in-time uploads (same channel & format); blank PI = not classifiable (too new/too few comparables).

| # | date | title | min | views | PI | class | topic | title format | transcript |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-04 | [The ENTIRE History of Amazon in 20 Minutes](https://www.youtube.com/watch?v=jOo8wSIeGus) | 20.0 | 430,614 |  | NOT_CLASSIFIED | company_business_case | statement_other | Y |
| 2 | 2026-10-06 | [The ENTIRE History of Walmart in 19 Minutes](https://www.youtube.com/watch?v=EtNH4mzw7AM) | 19.1 | 135,316 |  | NOT_CLASSIFIED | company_business_case | statement_other | Y |
| 3 | 2026-10-09 | [The ENTIRE History of Nintendo in 21 Minutes](https://www.youtube.com/watch?v=N6_TsQ655m8) | 21.4 | 12,780 |  | NOT_CLASSIFIED | money_history | statement_other | Y |
| 4 | 2026-10-13 | [The ENTIRE History of Toyota in 20 Minutes](https://www.youtube.com/watch?v=bOc-RUVrLSo) | 20.6 | 241,524 |  | NOT_CLASSIFIED | money_history | statement_other | Y |
| 5 | 2026-10-16 | [The ENTIRE History of Microsoft in 21 Minutes](https://www.youtube.com/watch?v=8oGSERdqoUI) | 20.9 | 112,692 |  | NOT_CLASSIFIED | money_history | statement_other | Y |
| 6 | 2026-10-20 | [The ENTIRE History of Costco in 19 Minutes](https://www.youtube.com/watch?v=AwxcZVfJUSA) | 19.1 | 188,468 |  | NOT_CLASSIFIED | company_business_case | statement_other | Y |
| 7 | 2026-10-23 | [The ENTIRE History of Tesla in 20 Minutes](https://www.youtube.com/watch?v=z3loXgkzRHM) | 20.1 | 27,422 |  | NOT_CLASSIFIED | company_business_case | statement_other | Y |
| 8 | 2026-10-27 | [The ENTIRE History of Nike in 20 Minutes](https://www.youtube.com/watch?v=luLV78wnSro) | 20.2 | 37,830 |  | NOT_CLASSIFIED | company_business_case | statement_other | Y |
| 9 | 2026-11-05 | [The  Rise and Fall of Blockbuster in 10 Minutes](https://www.youtube.com/watch?v=WXbSOqIODUs) | 10.4 | 3,085 |  | NOT_CLASSIFIED | macro_economy | rise_fall_case | Y |
| 10 | 2026-11-10 | [The ENTIRE History of Samsung in 18 Minutes!](https://www.youtube.com/watch?v=F1USlAvAC_s) | 17.9 | 1,828 |  | NOT_CLASSIFIED | money_history | statement_other | Y |

## 4. Topic and sub-niche map
| topic | n | long | median views | median PI | succ/breakout | under | first | last |
|---|---|---|---|---|---|---|---|---|
| company_business_case | 5 | 5 | 135,316 | n/a | 0 | 0 | 2026-10-04 | 2026-10-27 |
| money_history | 4 | 4 | 62,736 | n/a | 0 | 0 | 2026-10-09 | 2026-11-10 |
| macro_economy | 1 | 1 | 3,085 | n/a | 0 | 0 | 2026-11-05 | 2026-11-05 |

Title-format mix (INFERRED tags): statement_other: n=9.0, medPI=n/a · rise_fall_case: n=1.0, medPI=n/a

Mega-brand histories only. PI unavailable (fewer than 12 dated comparables) — raw views used, age not controlled (all within 5 weeks).

## 5. Winning video analysis
**The ENTIRE History of Amazon in 20 Minutes** (431k), **…Toyota** (242k), **…Costco** (188k), **…Walmart** (135k), **…Microsoft** (113k). Everyday-use American retail/tech giants lead (Amazon, Costco, Walmart — the same subjects winning on Business Decoded, Robin MBA, Brimm).

### Evidence: top-PI long-form videos


## 6. Underperforming video analysis
**…Samsung in 18 Minutes!** (1.8k, newest — age confound), **The Rise and Fall of Blockbuster in 10 Minutes** (3.1k, template break + nostalgia subject heavily covered), **…Nintendo** (12.8k), **…Tesla** (27k), **…Nike** (38k).

### Evidence: bottom-PI long-form videos


## 7. Successful vs failed comparison
Template identical; spread 1.8k→431k by brand (age partly confounds the newest two). Retail giants viewers use weekly > enthusiast brands (Nintendo, Tesla) in this audience (HYPOTHESIS).

_Too few classified videos for a contrast._



## 8. Topic discovery and research sources
Company histories; no links.

Institutions named in transcripts/descriptions (rule-based; 'Academic / research study' matches generic words like “study/research” and is low-confidence): Academic / research study 8, Company filings / earnings 7, News outlets 2, Congress / legislation 1
Description link domains: link.amazon 3, commons.wikimedia.org 2, builtonyou.github.io 1
Per-video source map: `SOURCE_MAP.csv`.

## 9. Trend behaviour
Evergreen.

## 10. Thumbnail strategy
Not inspected.

## 11. Title strategy
"The ENTIRE History of [X] in [N] Minutes" — PDF format 045 ("The Entire History of [X]") + time promise (089).

## 12. Hook and introduction strategy
Not analysed in depth (small sample).

## 13. Script and storytelling strategy
~20 min chronological.

## 14. Audience engagement model
UNKNOWN.

## 15. Upload and publishing strategy
~2/week since Oct 2026.

## 16. PDF principle evaluation
Judge: *YouTube Automation – Complete Master Playbook* (556 pp., sha256 c630c24b…576d). Supporting authority: global-youtube-knowledge (DS-000011/18/31) — see `00_PROJECT_OVERVIEW/GLOBAL_KNOWLEDGE_MAP.md`. Automated evidence uses text proxies; verdict = analyst override where noted, else rule-based draft.

| ID | PDF principle (location) | What the PDF says | Evidence from channel (automated, incl. winners vs rest where testable) | Verdict | Analyst note |
|---|---|---|---|---|---|
| P01 | Module 2.1 Outlier Concept, pp.6-9; Method 1 Outlier Transplant, pp.34-35 | Find videos that beat the channel norm (5-10x strong, 10x+ clear outlier) and treat their TOPIC as proven demand; build the calendar from validated outliers. | only 0 PI-classified long-form videos | **INSUFFICIENT DATA** | too young. |
| P02 | Module 2.2 Niche vs Format vs Template, p.11 | A niche is an audience + persistent interest + monetisation path, not a topic; every video should feel like it belongs to the same channel. | top-2 topics (company_business_case, money_history) = 90% of uploads; explicit audience marker in 0% of titles | **FOLLOWED** |  |
| P03 | Module 2.2, pp.12-13 | One niche can carry many formats; add formats to grow without changing niche. | 2 title-format types each ≥10% of uploads (statement_other 90%, rise_fall_case 10%) | **PARTIALLY FOLLOWED** |  |
| P04 | Module 2.2 p.13; Masterclass Ch.23 p.351; Web research §7 p.555 | Avoid repetitive/mass-produced uploads; rotating templates alone is not enough — each video needs distinct substance (inauthentic-content policy). | near-duplicate-script flag on 0% of videos; repeated title word-sets within channel 0% | **FOLLOWED** |  |
| P05 | Module 2.3 Format Arbitrage pp.18-20; Module 2.4 Niche Bending pp.24-26 | Win by transplanting a proven format into a niche that lacks it, or by combining two overlapping niches. | requires historical competitor-format landscape at launch; analyst note in report if a bend is visible | **NOT TESTABLE** |  |
| P06 | Module 2.7 Competitor Research pp.28-30; Method 1 p.34 | Study competitors’ top videos, titles, thumbnails, cadence and comments; cover proven topics with original content. | 0% of titles share a word-set with another channel; this channel published first on 0 of 0 | **NOT FOLLOWED** |  |
| P07 | Method 2 Title Template Injection pp.39-40; 100 Title Formats pp.52-64 | Inject niche topics into proven title psychology families (mystery, downfall, contradiction, revelation, practical, conflict…), but the content must deliver. | 100% of titles match a 100-format family | **FOLLOWED** | PDF title families 045 + 089 combined. |
| P08 | 100 Title Formats p.53 (five-part engine), p.66 scorecard | A strong title names a recognisable subject, a situation, a trigger, a tension and a concrete promise/stakes. | 100% of titles carry a number/$/named entity | **FOLLOWED** |  |
| P09 | 100 Title Formats p.68 (12 mistakes); Masterclass Ch.19 p.345 | Avoid generic subjects, two promises, vague “this/they” openers, ALL CAPS overuse, overstated certainty. | titles with ≥3 ALL-CAPS words 0%; vague 'this/they' opener 0%; double-question 0% | **FOLLOWED** |  |
| P10 | 100 Title Formats p.66 (title+thumbnail one promise), p.68 #11 | Thumbnail should add a complementary clue, not repeat the title. | OCR thumbnail text found on 80%; median share of thumbnail words repeated from title 1.00 | **NOT FOLLOWED** |  |
| P11 | Module 2.7 Thumbnail Teardown p.28 (supporting: DS-000011 Packaging SOP) | Study colour, text amount, faces/expressions, focal object, contrast and template consistency; one clear idea. | thumbnail images 100%; median OCR words 2.5 (OCR undercounts stylised text); face/character detected 90% (cartoon faces often missed) | **FOLLOWED** |  |
| P12 | Engagement Playbook §1 p.265; Masterclass Zone 1 p.320 | The first ~3-5 seconds must create curiosity: question, shock stat, contradiction, mystery, story drop, direct challenge. | opening ~75 words contain question/number/contradiction/story/you-hook in 60%; greeting/channel-intro opening 0% | **PARTIALLY FOLLOWED** |  |
| P13 | Masterclass Zone 2 p.320; Engagement §18 p.283 | Within ~5-15 s answer “why should I care?” — connect to the viewer’s money, safety or identity. | explicit stakes/why-it-matters language early in 30% | **PARTIALLY FOLLOWED** |  |
| P14 | Masterclass Zone 3 p.320; Ch.23 p.350 | Open at least one curiosity loop before ~30 s and keep it open. | explicit open-loop/promise phrase in first ~150 words of 40% | **PARTIALLY FOLLOWED** |  |
| P15 | Engagement §2 & §7 pp.267, 272 | Use bridging teases / micro-cliffhangers at segment transitions to prevent drop-off. | bridge/cliffhanger phrases per 100 words (median) 0.032 | **PARTIALLY FOLLOWED** |  |
| P16 | Engagement §8 p.273 | Precise numbers, dates, named sources and expert quotes signal research and keep sceptical viewers. | data/citation terms per 100 words 0.82; videos naming an institution/source 80% | **PARTIALLY FOLLOWED** |  |
| P17 | Engagement §6 p.271 | Second-person address makes the viewer a participant (“if you own…”, “imagine you…”). | 'you/your' per 100 words (median) 0.79 | **NOT FOLLOWED** |  |
| P18 | Engagement §15-16 pp.280-281; Deployment p.284 | Close loops, then future-pace to a next video; strongest CTA right after a payoff, not only at the end. | next-video tease in final ~60 words 0%; any CTA in final 10% 80% | **PARTIALLY FOLLOWED** |  |
| P19 | Module 2.3 p.19 (8+ min sweet spot); Web research §8 p.555 | Course: formats should fill 8+ minutes; appendix: 8 min is a mid-roll eligibility rule, length should follow the story. | median long-form length 20.0 min — 8+ min is an ad-eligibility rule, not a success rule (PDF p555) | **FOLLOWED** |  |
| P20 | Module 2.7 Posting cadence p.29 | Check upload frequency, consistency, dead periods and growth inflection points. | median gap 3.0 d, gap CV 0.56, longest pause 8 d | **FOLLOWED** |  |
| P21 | Topic Selection Masterclass intro p.33 | “A bad video on the right topic will outperform a great video on the wrong topic” — topic selection is the main lever. | 0 classified long-form | **FOLLOWED** | subject (brand) decides within a fixed template. |
| P22 | Method 2 warning p.40; 100 Formats p.68 #12; Masterclass Ch.19 p.345 | Title gets the click, content keeps the viewer: the opening must confirm and the video must deliver the title’s promise. | median share of title keywords that appear in the first ~150 spoken words 0.25 | **NOT FOLLOWED** |  |

## 17. Strengths and weaknesses
Clean scalable template; strong subject choices early. Weaknesses: template break; enthusiast brands weaker.

## 18. Replicable working model
**"Entire History of a Brand You Use"**.

## 19. What to copy
Template + everyday mega-brands first.

## 20. What not to copy
Breaking the template; niche-enthusiast brands early.

## 21. Missing evidence and limitations
10 videos, 5 weeks, no PI; thumbnails not inspected.

- Not available from this dataset for any channel: CTR, impressions, retention curves, traffic sources, subscriber growth history, comments text. Hook timings are word-position estimates (untimed transcripts).

## 22. Final channel diagnosis
Promising template; subject choice drives results. Lesson: **lead with brands viewers use every week.**
"If I wanted a channel like this, I would study the Amazon and Costco videos and keep the 'Entire History in 20 Minutes' template on everyday mega-brands."
