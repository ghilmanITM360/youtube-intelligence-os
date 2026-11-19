# Stage 3: frameworks applied to the six channels' actual videos (2026-11-19)

Scope: the six fixed channels only. Sample: **172 long-form videos** with public views and a transcript (MonkeyExplains 62 of its 64 public long videos; Paper Billions 6). Shorts and Member Edition items are excluded from text tests. Read-only on the DB; no paid run; nothing committed. Code: `stage3_apply.py`, `stage3_topics.py`, `build_stage3_report.py`; per-video features: `stage3_features.csv`; raw results: `stage3_results.json`, `stage3_topics.json`.

## 1. What "applied" means here (honest scope)

| Source | What it is (authority) | What was applied | How it was encoded |
|---|---|---|---|
| **DS-000011** (17 files) | Creator-education and creative library; creative heuristics, not YouTube facts | 9 of its 17 encoded rules (TR-011-002, -003, -004, -007, -010, -011, -012, -015, -016) that can be tested on text | `data/intelligence/system/youtube-strategy-training-knowledge-2026-09-11.json` and the framework DB rows that point to DS-000011 documents |
| **DS-000018** (63-tab Google Doc) | Third-party creator commentary on the "2026 algorithm"; context, not platform fact (earlier audit: 10 of 33 claims supported, 12 partial, 1 contradicted, 8 lacking primary support, 2 not verifiable; REUSED, not re-run) | Only the claims and recommendations that competitor public data can test: CLM-003, CLM-009, CLM-015, CLM-018, REC-005, REC-006, REC-007, REC-009 | the same JSON (TR-018-*) |
| **YouTube Automation Master Playbook** (556 pp) | Course lessons plus prompts; Part D only is official-source | Principles P01, P04, P06, P07, P08, P09 and the "8+ minute sweet spot" | `00_PROJECT_OVERVIEW/PDF_KNOWLEDGE_MAP.md` principle table (REUSED); title families re-implemented by us as 9 regex proxies (INFERRED, not the PDF's own list of 10) |
| **Framework DB** `data/knowledge/reference_knowledge.db`, framework version **v1** | 33 rules (27 creative heuristics, 1 empirical hypothesis, 2 duplicates, 3 not applicable) | 16 rule rows listed with their source rows in section 6: 10 tested on text, 3 only partly (title-word echo), 3 not tested or not evaluable | `ref_rule` rows; member and locator recorded below |

Limits that apply to everything below: the DS and Playbook source files were NOT re-read page by page in this stage (reading coverage is stated in `01_PROJECT_OVERVIEW/01_KNOWLEDGE_BASE_FORENSIC_ANALYSIS.md`); I applied the rules as already encoded. No CTR, retention or impressions exist, so every test compares public views, expressed as **PI = views / that channel's own long-form median**, which removes channel size. Views depend on age; a second sample limited to videos older than 60 days is reported. About 20 features were tested on 3 samples, so one or two p-values below 0.05 are expected by chance. Paper Billions (11 days old) is excluded from the primary sample. Nothing here shows causation.

## 2. Rule-by-rule results (each row: which framework, which rule, what was measured)

Format of the result column: videos with / without the feature; median PI with vs without; Mann-Whitney p; number of channels where the "with" group has the higher median. Primary sample = 5 channels, 166 videos.

| # | Source and rule | Operationalisation on real videos | Result (primary sample) | Older-than-60-days check | Verdict |
|---|---|---|---|---|---|
| 1 | Playbook P07 "title psychology families"; DS-000011 TR-011-013 | Title matches crisis/collapse/bubble/recession words | 39/127; PI 1.45 vs 0.82; p=0.01; channels agree 4/4 | 30/111; PI 1.21 vs 0.71; p=0.04; channels agree 4/4 | Nominal signal only: 4 of 4 channels agree, but p=0.007 does NOT survive correction for 22 tests (threshold 0.0023) and the family overlaps the AI-bubble and crash topics (review, section 11). HYPOTHESIS |
| 2 | Playbook P07 (other 7 families) | curiosity/threat, explainer, story/person, contrarian, urgency, question, superlative | all p >= 0.19 (e.g. question 12/154; PI 1.40 vs 1.00; p=0.61; channels agree 3/3) | no p < 0.05 | NOT SUPPORTED |
| 3 | Playbook P08, DS-000011 TR-011-011, FR-VC-05 (specificity and numbers) | digit in title; digits or money/percent words in first 60 opening words | title 51/115; PI 0.87 vs 1.02; p=0.62; channels agree 1/5; opening 90/76; PI 1.01 vs 0.93; p=0.49; channels agree 3/5 | title 46/95; PI 0.86 vs 0.87; p=0.96; channels agree 3/5; opening 76/65; PI 0.93 vs 0.82; p=0.59; channels agree 4/5 | NOT SUPPORTED (titles with digits are slightly lower) |
| 4 | Playbook P09 title mistakes (ALL CAPS) | an ALL-CAPS word of 3+ letters | 18/148; PI 0.68 vs 1.00; p=0.19; channels agree 2/5 | 16/125; PI 0.65 vs 0.89; p=0.16; channels agree 1/4 | DIRECTIONAL (caps lower in 2 of 5 channels, not significant) |
| 5 | FR-TITLE-01 and TR-011-004 (key info in first ~55 chars; short title) | title <= 55 characters | 154/12; PI 1.00 vs 1.28; p=0.93; channels agree 2/2 | 131/10; PI 0.87 vs 0.97; p=1.00; channels agree 2/2 | rule is met by 93% of titles, so it cannot discriminate (only 12 exceptions) |
| 6 | Playbook "8+ min sweet spot" (an ad-eligibility rule officially, not a view rule) | duration >= 8 min | 149/17; PI 1.02 vs 0.64; p=0.10; channels agree 3/3 | 124/17; PI 0.93 vs 0.64; p=0.27; channels agree 2/3 | DIRECTIONAL, 3 of 3 channels, only 17 videos under 8 min. Spearman of transcript words vs PI = 0.22 (p=0.004), duration 0.21 (p=0.007): longer videos sit slightly higher within a channel. Confounded by topic |
| 7 | DS-000011 TR-011-002 / FR-HOOK-01 / TR-011-012 (3-step hook, contrarian snapback) | a "but / however / the problem / actually / nobody / never..." marker in the first 120 words | 145/21; PI 0.89 vs 1.55; p=0.04; channels agree 0/5 | 126/15; PI 0.83 vs 1.39; p=0.18; channels agree 0/4 | **PROXY INVALID**: 87% of openings contain such a word, and the few without score higher. A word search cannot detect a snapback; the qualitative reading of the top 8 openings per channel (Stage 2 section 9) is the only real evidence, and it shows fact-then-contradiction at Casual Finance and problem-first at MonkeyExplains/Paper Billions |
| 8 | DS-000011 TR-011-010 / FR-VC-01 (audience pain point; speak to the viewer) | "you/your" in first 75 words | 46/120; PI 1.02 vs 1.00; p=0.85; channels agree 4/5 | 35/106; PI 0.85 vs 0.88; p=0.60; channels agree 2/4 | NOT SUPPORTED |
| 9 | FR-VC-06 (timeliness) and DS-000018 REC-007 (early specific names/dates) | dated reference (year, month, "last week", "days ago", "just") in first 75 words | 56/110; PI 1.39 vs 0.89; p=0.14; channels agree 4/5 | 44/97; PI 1.00 vs 0.86; p=0.58; channels agree 4/5 | DIRECTIONAL (4 of 5 channels); effect fades in the older sample and top videos do not show it (section 7), so it may be recency |
| 10 | DS-000018 REC-007 (names, places early) | 3+ named entities in the first 60 words | 158/8; PI 1.00 vs 0.89; p=0.95; channels agree 0/2 | n/a | 95% comply, cannot discriminate |
| 11 | FR-SEO-01 (title keyword spoken in first ~30 s) | at least half of the title's content words appear in the first 75 words | 28/138; PI 0.71 vs 1.07; p=0.33; channels agree 0/4 | 24/117; PI 0.70 vs 0.98; p=0.54; channels agree 1/4 | NOT SUPPORTED. Only 17% of videos say their title words in the first 30 s; a missing keyword does not lower views here |
| 12 | FR-16C-16 (echo: ending returns to the title/theme) | a title content word appears in the last 150 words | 114/52; PI 1.07 vs 0.84; p=0.08; channels agree 4/5 | 98/43; PI 0.99 vs 0.66; p=0.05; channels agree 3/5 | WEAK, borderline (older sample p<0.05, primary p=0.08, 4 of 5 channels). Needs replication |
| 13 | FR-SCR-05 (CTA and monetisation placement) | subscribe/like/sponsor wording anywhere; in the first 15% | any 100/66; PI 1.00 vs 1.00; p=1.00; channels agree 3/4; early 17/149; PI 1.28 vs 1.00; p=0.52; channels agree 1/2 | n/a | descriptive only; no relation |
| 14 | FR-BT-01, FR-16C-03, TR-011-015 (BUT/THEREFORE, avoid "and then") | per-1000-word rates of but/however/yet vs therefore/because/that's why vs "and then", Spearman with PI | but -0.09 (p=0.25); therefore -0.13 (p=0.08); and-then -0.04 (p=0.59) | n/a | NOT SUPPORTED (no positive relation; a word count is a weak proxy for causal structure) |
| 15 | Playbook P04, DS-000018 CLM-009 (templated repetition vs reusable format) | 8-gram Jaccard overlap of the first 400 words, all pairs within each channel | max pair overlap 0.045; 0 pairs >= 0.25 in any channel | n/a | PASS: no near-duplicate scripts. But 21 of MonkeyExplains' 62 openings start with the literal formula "This is Uncle Don / This is Sam..." (15 + 6), so the format repeats while the content differs, which is the case CLM-009 calls acceptable (a creator claim) |
| 16 | DS-000018 CLM-003 (evergreen: views arrive late) | Spearman of video age vs views per channel (single snapshot) | Casual Finance -0.66 (p<0.001: newer videos have MORE views); Crayon 0.19, MonkeyExplains -0.04, Capital Case -0.40, Monkey Economics -0.23 (all n.s.) | n/a | NOT SUPPORTED in this snapshot; view velocity over time would be needed, and we hold one snapshot |
| 17 | FR-TITLE-03, FR-SCR-03, FR-INTRO-02, FR-16C-04 (title promise delivered, no overpromise) | only the title-word echo (row 12) was computed | see row 12 | n/a | PAYOFF READING NOT DONE at scale (would need reading every script). Not claimed |
| 18 | FR-16C-06 (reset every 20-30 s), FR-INTRO timings, TR-011-005 (first 10 s as packaging) | needs timed transcript, visuals or retention | none | n/a | NOT EVALUABLE (framework DB marks it so); FR-NA-01..03 NOT APPLICABLE |

## 3. Outlier method (Playbook P01) on actual numbers

Playbook rule: outlier ratio = views / subscribers; 5x strong, 10x+ clear outlier, studied best on 1K to 100K-subscriber channels. Applied to current subscribers (261K MonkeyExplains, 440K Casual Finance, 224K Monkey Economics, 319K Crayon, 23.6K Paper Billions, 12K Capital Case):

| Channel | Long videos tested | >= 1x subs | >= 2x | >= 5x | Max | Median ratio |
|---|---:|---:|---:|---:|---:|---:|
| Crayon Capital | 35 | 16 | 9 | 3 | 13.2x | 0.94x |
| MonkeyExplains | 62 | 33 | 12 | 3 | 10.2x | 1.06x |
| Capital Case | 13 | 9 | 9 | 6 | 32.1x | 4.55x |
| Casual Finance | 38 | 23 | 11 | 1 | 5.5x | 1.27x |
| Monkey Economics | 18 | 0 | 0 | 0 | 0.9x | 0.05x |
| Paper Billions | 6 | 5 | 5 | 4 | 137.2x | 30.08x |

Reading: the ratio only produces "outliers" for the two smallest channels (Paper Billions 4 of 6 at >= 5x, Capital Case 6 of 13), where the denominator is tiny. For the large channels it is nearly silent (Casual Finance max 5.5x even for 2.4M views). Monkey Economics has none (long-form median 0.05x of its subscribers), which confirms its audience was gathered by Shorts. So the playbook ratio is **informative only against small channels**, which is what the Playbook itself says; our within-channel PI is the better lens for large channels. Topics where several channels produced winners are the "cross-validated outliers" of Playbook Method 1 (section 5).

## 4. Launch cadence (DS-000018 REC-005 "launch with several linked videos")

| Channel | First public upload | Uploads in first 14 days | in first 30 days | Total held |
|---|---|---:|---:|---:|
| Casual Finance | 2025-07-28 | 1 | 2 | 223 |
| Monkey Economics | 2025-04-23 | 11 | 19 | 60 |
| MonkeyExplains | 2025-05-26 | 4 | 13 | 101 |
| Crayon Capital | 2025-04-22 | 1 | 2 | 35 |
| Paper Billions | 2026-11-06 | 6 | 6 | 6 |
| Capital Case | 2026-02-22 | 2 | 2 | 13 |

Paper Billions (6 in 12 days), Monkey Economics (11 in 14 days) and MonkeyExplains (4 in 14 days) started with several uploads. Casual Finance, Crayon Capital and Capital Case show 1 to 2 uploads in the first 14 days; Monkey Economics (Shorts burst, 11) and MonkeyExplains (4 in 14 days, 13 in 30) also started dense. Caveat: the first date is the first video held in the DB, which may not be the channel's true first upload (Casual Finance reports 222 videos but its DB window starts 2025-07-28). Those three have very different outcomes (Paper Billions 710K median, MonkeyExplains 275K, Monkey Economics long 10K), so launch density alone does not predict results here; the data cannot show cause.

DS-000018 REC-006 (repeatable "show" formats): MonkeyExplains uses "Explained Using Bananas" (19 titles, median 274K) and "... Worse Than You Think" (11, median 431K); Crayon uses "Explained Like You're 5" (21, median 301K, equal to its overall median). Template titles are not worse than the rest, in this set. CLM-018 (Shorts and long-form should be separate channels): Monkey Economics shows Shorts reach did not become long-form reach (913K vs 10K medians); Casual Finance kept both in one channel and its long median is 559K. One counter-example each way; not conclusive.

## 5. Topics: framework findings applied across channels (Playbook P01 cross-validation, P06, DS-000018 REC-004/009)

Keyword clusters over all six channels' titles (INFERRED labels; Stage 4 will curate). PI median is relative to each video's own channel.

| Topic cluster | Channels | Long videos | Shorts | Long views | Median PI | Winners (>=2x) | First covered by |
|---|---:|---:|---:|---:|---:|---:|---|
| AI bubble / OpenAI / Nvidia / Anthropic / big tech | 5 | 28 | 45 | 19,449,302 | 1.56 | 7 | MonkeyExplains 2025-11-26 |
| Crisis history (Depression / 2008 / 1973 / dot-com / WW2 era) | 5 | 13 | 0 | 8,818,988 | 1.65 | 6 | Crayon Capital 2025-04-22 |
| Stock market structure and current crashes | 4 | 11 | 15 | 7,981,504 | 1.24 | 3 | Monkey Economics 2025-05-07 |
| Scams / Wolf of Wall Street / fraud / crypto | 4 | 14 | 16 | 6,920,822 | 0.58 | 1 | Monkey Economics 2025-04-29 |
| China / Xi / Singapore / other countries | 5 | 11 | 9 | 5,208,127 | 1.48 | 3 | MonkeyExplains 2025-08-14 |
| Billionaire and company origin stories | 2 | 12 | 0 | 4,228,279 | 0.78 | 3 | Crayon Capital 2025-06-25 |
| Housing / real estate / mortgage | 2 | 3 | 8 | 3,166,986 | 1.32 | 1 | Monkey Economics 2025-05-01 |
| National debt / US debt / bonds | 3 | 5 | 18 | 2,526,383 | 0.21 | 1 | Monkey Economics 2025-05-20 |
| SpaceX / IPO | 4 | 4 | 7 | 2,398,935 | 1.25 | 1 | Casual Finance 2026-05-21 |
| Iran / Hormuz / war / oil / Venezuela | 5 | 8 | 10 | 1,766,973 | 0.62 | 1 | MonkeyExplains 2025-12-21 |
| Government shutdown / US politics | 2 | 5 | 3 | 1,379,053 | 0.89 | 1 | Monkey Economics 2025-06-27 |
| Epstein / Apestein | 3 | 4 | 0 | 1,111,517 | 1.04 | 1 | MonkeyExplains 2026-02-13 |
| Fed / interest rates / inflation | 3 | 5 | 11 | 1,102,087 | 1.88 | 2 | Monkey Economics 2025-04-25 |
| Tariffs / trade war | 1 | 2 | 4 | 880,448 | 1.6 | 1 | Monkey Economics 2025-04-26 |
| Gold / money system / dollar | 3 | 4 | 5 | 811,929 | 0.64 | 0 | Monkey Economics 2025-05-04 |
| Jobs / careers / wages | 1 | 2 | 3 | 223,689 | 10.92 | 1 | Monkey Economics 2025-05-02 |

Findings (clusters are first-match, so no video is counted twice; rebuilt during the review, section 11): (1) Crisis history (Depression, 2008, 1973, dot-com) has 5 channels, 13 long videos, 6 winners and median PI 1.65x. (2) The AI bubble / OpenAI / Nvidia cluster has the most views (19.4M, 28 long, 7 winners, median 1.56x) and 5 channels compete in it, so Playbook P06 (cover proven topics originally) and REC-009 (net-new information) both flag it as saturated. (3) Fed/rates/inflation has the highest median among multi-video clusters (1.88x) with only 5 long videos. (4) China and other countries (Singapore, Korea, Indonesia, France) has median 1.48x with 3 winners over 11 videos; stock-market structure and current crashes 1.24x with 3 winners. (5) Scams/fraud/crypto (14 long, median 0.58x, 1 winner), Iran/war/oil (0.62x), gold/dollar (0.64x, 0 winners), billionaire/company origin stories (0.78x, 3 winners but 12 videos) and national debt (median 0.21x, one 1.92M hit) are weak clusters. (6) Housing: 2 channels, 3 long videos, 1 winner (Casual Finance 2.42M). Airfares, rent data and jobs-report topics from our earlier shortlist do not appear in any channel's titles; see Stage 4.

## 6. Provenance: framework DB rows used (framework version v1, `data/knowledge/reference_knowledge.db`)

| Rule | Version | Member | Source file | Locator | Class |
|---|---|---|---|---|---|
| FR-TITLE-01 | v1 | RM-8b65784803f2 | YouTube Title Analyzer — Natural Language Prompts (2).pdf | p.3 s.1 ChatGPT | CREATIVE_HEURISTIC |
| FR-SEO-01 | v1 | RM-63c5338e6a9e | 🎯 YouTube Video SEO – COMPLETE CHECKLIST DOCUMENT (1).pdf | p.5 s.7 Title Checklist; p.3 script optimization | CREATIVE_HEURISTIC |
| FR-VC-05 | v1 | RM-2d31bc62bc87 | Viral Checklist.pdf | p.1 item 5 | CREATIVE_HEURISTIC |
| FR-VC-06 | v1 | RM-2d31bc62bc87 | Viral Checklist.pdf | p.1 item 6 | CREATIVE_HEURISTIC |
| FR-HOOK-01 | v1 | RM-4bbe6c6e34b2 | Hook guide.pdf | p.1 "3-Step Hook Formula"; p.2 | CREATIVE_HEURISTIC |
| FR-VC-04 | v1 | RM-2d31bc62bc87 | Viral Checklist.pdf | p.1 item 4 | CREATIVE_HEURISTIC |
| FR-VC-01 | v1 | RM-2d31bc62bc87 | Viral Checklist.pdf | p.1 item 1 | CREATIVE_HEURISTIC |
| FR-16C-16 | v1 | RM-242707556f81 | 📜 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated).pdf | p.5 #16 | CREATIVE_HEURISTIC |
| FR-SCR-05 | v1 | RM-6d9840bbe0ca | Script Analyzer.pdf | p.1 s.1; p.1 s.7 Claude | CREATIVE_HEURISTIC |
| FR-BT-01 | v1 | RM-52235e9459a8 | The Magic of ‘BUT’ and ‘THEREFORE’ in Storytelling.docx (1).pdf | p.1 rows 4 and 7 | CREATIVE_HEURISTIC |
| FR-SCR-03 | v1 | RM-6d9840bbe0ca | Script Analyzer.pdf | p.1 s.1 ChatGPT; s.6 Google AI Studio | CREATIVE_HEURISTIC |
| FR-INTRO-02 | v1 | RM-cb50fe7ec900 | Intro Analyzer Prompts.docx (1).pdf | p.2 s.7 Google AI Studio | CREATIVE_HEURISTIC |
| FR-TITLE-03 | v1 | RM-8b65784803f2 | YouTube Title Analyzer — Natural Language Prompts (2).pdf | p.5 s.6 Google AI Studio | CREATIVE_HEURISTIC |
| FR-16C-06 | v1 | RM-242707556f81 | 📜 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated).pdf | p.4 #6 | EMPIRICAL_HYPOTHESIS |
| FR-16C-13 | v1 | RM-242707556f81 | 📜 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated).pdf | p.5 #13 | CREATIVE_HEURISTIC |
| FR-SCR-01 | v1 | RM-6d9840bbe0ca | Script Analyzer.pdf | p.1 s.1 ChatGPT | CREATIVE_HEURISTIC |

Retrieval method: rows read directly from `ref_rule` and `ref_source_member` (read-only). Each rule's class is a creative heuristic unless shown; none is a platform fact. These validators are structural: only a reader can mark a rule semantically reviewed, and this stage did not do that.

## 7. Applied to actual videos (top two long videos of each channel)

yes/no per feature computed from the video's title and transcript. Columns: title <= 55 chars; crisis-family title; digit in title; numbers in the opening; dated opening; title keyword spoken early; closing echo; CTA in the first 15%; duration >= 8 min.

| Channel | Video | Views | PI | <=55 | crisis | digit | open nums | dated | kw early | echo | early CTA | >=8m |
|---|---|---:|---:|---|---|---|---|---|---|---|---|---|
| MonkeyExplains | [Why Hasn't The AI Bubble Popped (Yet)?](https://www.youtube.com/watch?v=7rtn4doHIuY) | 2,660,895 | 9.6x | yes | yes | no | no | no | no | no | yes | yes |
| MonkeyExplains | [The US National Debt Crisis Explained with Bananas](https://www.youtube.com/watch?v=bz0OGtrkjv0) | 1,920,233 | 6.9x | yes | yes | no | yes | no | yes | yes | no | no |
| Casual Finance | [The New American Housing Crisis Has Landed](https://www.youtube.com/watch?v=Uumnx2Fo6cE) | 2,422,378 | 4.3x | yes | yes | no | yes | yes | no | yes | no | yes |
| Casual Finance | [Brace For Impact.](https://www.youtube.com/watch?v=5umJ63d3rzQ) | 2,038,798 | 3.6x | yes | no | no | no | no | no | no | no | yes |
| Monkey Economics | [Stop Being Good at Your Job...](https://www.youtube.com/watch?v=GkJCXwm7Ous) | 211,692 | 20.7x | yes | no | no | no | no | no | yes | no | yes |
| Monkey Economics | [Monkey Economics - How to Start a Business](https://www.youtube.com/watch?v=QZdM9DlrMTE) | 43,845 | 4.3x | yes | no | no | yes | no | yes | yes | no | no |
| Crayon Capital | [The Wolf of Wall Street Scam Explained Like You're 5](https://www.youtube.com/watch?v=HawmGu7oNrc) | 4,219,017 | 14.0x | yes | no | yes | yes | no | no | yes | no | yes |
| Crayon Capital | [The Great Depression Explained Like You’re 5](https://www.youtube.com/watch?v=LuEcoqizj0o) | 2,762,821 | 9.2x | yes | yes | yes | yes | no | yes | yes | no | yes |
| Paper Billions | [How a Chinese Spy Got Inside Nvidia](https://www.youtube.com/watch?v=_MG4v3foET8) | 3,237,543 | 4.6x | yes | no | no | no | no | yes | yes | no | yes |
| Paper Billions | [Why Nvidia Would Fail Without Jensen Huang](https://www.youtube.com/watch?v=Vy1m4ZXNzpo) | 1,350,908 | 1.9x | yes | no | no | no | yes | no | yes | no | yes |
| Capital Case | [Rockefeller Explained in 10 Minutes](https://www.youtube.com/watch?v=sGtEBUIppYc) | 385,205 | 7.1x | yes | no | yes | yes | no | no | yes | no | yes |
| Capital Case | [How the Great Depression Actually Happened (The Fatal Decisions)](https://www.youtube.com/watch?v=CAsim5HC-uI) | 294,004 | 5.4x | no | yes | no | yes | no | no | yes | no | yes |

Reading (counts from the table, 12 videos, against the base rate in all 172 videos): crisis-family title 5 of 12 (42%, base 23%); closing echo 10 of 12 (83%, base 69%); title keyword spoken early 4 of 12 (33%, base 17%); dated opening only 2 of 12 (17%, base 33%); digit in title 4 of 12 (33%, base 31%); duration >= 8 min 10 of 12 (base 90%). So the top videos over-represent the crisis title and the closing echo, and do NOT over-represent dated openings, which weakens row 9. 12 videos are too few for any rule to be called a cause.

## 8. Findings and which framework produced each

| ID | Finding | Produced by | Label |
|---|---|---|---|
| F1 | Crisis/collapse/bubble titles have higher PI in 4 of 4 testable channels (1.45x vs 0.82x) | Playbook P07 family test on real titles | HYPOTHESIS: p=0.007 fails multiple-test correction; topic-confounded |
| F2 | Numbers in titles do not help; digit titles are slightly lower | Playbook P08, TR-011-011, FR-VC-05 | INFERRED |
| F3 | A "contrarian snapback" word search cannot detect hooks; the proxy fires on 87% of videos | TR-011-002, FR-HOOK-01 | proxy invalid; use reading |
| F4 | Dated openings trend higher (4 of 5 channels) but the effect vanishes in older videos and the top 12 videos under-represent them (2 of 12) | FR-VC-06, REC-007 | HYPOTHESIS, weak |
| F5 | Only 17% of videos speak the title keyword in the first ~30 s; no penalty | FR-SEO-01 | INFERRED |
| F6 | Ending that returns to the title's words trends higher | FR-16C-16 | HYPOTHESIS, borderline |
| F7 | No near-duplicate scripts anywhere; MonkeyExplains reuses a literal opener in 21 of 62 videos | Playbook P04, CLM-009 | VERIFIED text overlap |
| F8 | The outlier ratio flags only the two smallest channels; within-channel PI is the better lens for large ones | Playbook P01 | INFERRED |
| F9 | Cross-channel topic table (first-match clusters): crisis history and AI bubble strongest, AI bubble most saturated, rates/inflation and China/other-countries high median with few videos | Playbook P01/P06, REC-009 | INFERRED |
| F10 | Three channels launched with several uploads in 14 days (Paper Billions 6, Monkey Economics 11, MonkeyExplains 4) with very different outcomes; late-view (evergreen) growth is not visible in a single snapshot | REC-005, CLM-003 | UNKNOWN causal |

## 11. Review of this report (done 2026-11-19, after first publication)

| # | Issue found | Check | Result and fix |
|---|---|---|---|
| R1 | Crisis-title signal was labelled "only repeatable signal" | Benjamini-Hochberg and Bonferroni over the 22 primary tests | Smallest p=0.0071 vs threshold 0.0023: **not significant after correction**. Label downgraded to HYPOTHESIS (rows 1, F1) |
| R2 | Could the signal be a topic effect? | 39 crisis-family titles in the 5 channels: 19 sit in the Crashes category, 13 in AI bubble. Within AI: 1.56x vs 0.87x (13/13). Within Crashes only 2 titles lack the words, so it cannot be tested. Excluding both categories: 3.24x vs 0.82x, n=7, p=0.03 unadjusted | Unresolved: topic and wording are entangled, and the category regex itself contains "bubble"/"crash" (circular). Not usable as a rule |
| R3 | Topic clusters double-counted videos (an AI crash video counted in "AI" and "crises"; "debt" included an AI debt video; "war" included WW2) | Printed cluster membership | Clusters rebuilt with first-match priority (`stage3_topics.py`); section 5 and F9 text replaced. Changes: crisis history 1.71x to 1.65x, AI views 21.1M to 19.4M, national-debt median 0.60x to 0.21x |
| R4 | Launch cadence text said only Paper Billions launched with a batch | Table in section 4 | Already corrected: Monkey Economics and MonkeyExplains also started dense |
| R5 | Counts and provenance | Rule counts re-derived (27 creative, 1 empirical, 2 duplicate, 3 not applicable); framework rows re-read from `ref_rule` | Corrected from 29 to 27 |
| R6 | Proxies are crude (regex title families are ours, not the PDF's ten; hook "snapback" cannot be found by word search) | Reviewed | Already labelled INFERRED/PROXY INVALID. No rule was adopted |
| R7 | Sample scope | MonkeyExplains tested 62 of 64 public long (2 lack transcripts); Paper Billions only in the 'all' sample | Stated; does not change conclusions |

Net result of the review: the Stage 3 conclusion "no framework rule reliably separates winners" stands; the one positive signal is downgraded from "repeatable" to "nominal".

## 9. Implications for our channel (HYPOTHESIS, to be tested on our own Studio data)

1. Do not adopt any rule as a gate. In this sample, no framework heuristic reliably separates high from low views, which matches the earlier finding (Phase E) that title features did not separate winners.
2. Cheap, compatible choices: crisis/risk framing only when the data supports it; a dated, specific opening; a closing that returns to the title's question. All three are consistent with the evidence above and with the framework DB; none is proved.
3. Avoid the hook trope shared by MonkeyExplains and Paper Billions ("This is X, and he has a huge problem") and the AI-bubble cluster unless a data angle is original.
4. Keep the Part D measurement plan: test titles and thumbnails with YouTube's A/B tool, long-form only, from video 1.

## 10. Not done in Stage 3
- No page-by-page re-read of DS-000011, DS-000018 or the Playbook; no semantic review of rules.
- No payoff/overpromise reading across all scripts; no visual or retention tests (no data).
- DS-000018's platform-mechanism claims (CLM-001, -002, -004, -006 to -008, -010 to -014, -016, -017) cannot be tested on competitor public data; their status stays as in the 2026-09-04 primary validation.
