# Explainer/ELI5 cluster re-analysis vs YouTube Automation Master Playbook (2026-11-12)
Owner request: re-analyse Econ in a Nutshell, Casual Finance, Primate Economics, Crayon Capital, MonkeyExplains, Economics Explained, Capital Case, PENNY, Paper Billions (the list also had one blank entry; not analysed). Matrix: `EXPLAINER_CLUSTER_PDF_MATRIX_2026-11-12.csv`. Per-channel evidence: `01_CHANNEL_REPORTS/<NNN>_*/CHANNEL_REPORT.md`. Raw data for PENNY/Paper Billions: `APIFY_SPOT_SCRAPES_2026-11-12.csv`.

## Tally of the 22 PDF principles (existing scorecard, 7 channels)
| Channel | Tier | Median long views | Max | FOLLOWED | PARTIAL | NOT |
|---|---|---|---|---|---|---|
| Primate Economics | SUCCESSFUL | 449k | 15.7M (Short) | 8 | 6 | 7 |
| Crayon Capital | SUCCESSFUL | 250k | 4.2M | 9 | 8 | 5 |
| Casual Finance | SUCCESSFUL | 485k | 2.35M | 7 | 9 | 6 |
| MonkeyExplains | SUCCESSFUL | 348k | 1.92M | 7 | 9 | 6 |
| Economics Explained | SUCCESSFUL | 546k | 1.5M | 8 | 6 | 6 |
| Capital Case | SUCCESSFUL (low) | 54k | 380k | 10 | 3 | 8 |
| Econ in a Nutshell | UNDERPERFORMING | 4.8k | 1.04M | 11 | 6 | 2 |

## What the PDF re-check shows (VERIFIED from the scorecard; reading INFERRED)
1. **Playbook score does not predict success.** Econ in a Nutshell follows the most principles (11) and is the weakest (median 4.8k). Primate has 7 NOT FOLLOWED and the biggest hit. Following craft rules is necessary-ish, not sufficient. P21 (topic is the main lever) is the principle that separates them.
2. **All 7 follow P11 (one-idea thumbnail) and P19 (length), and all fail or only partly meet P14 (curiosity loop before 30 s) and P17 (second-person)**: 6 of 7 are NOT FOLLOWED on P13 (why-should-I-care) and all 7 on P14. These explainers win on subject + format, not on the PDF's hook mechanics. This matches the study-wide finding that hooks are near-universal and don't differentiate.
3. **P05 (format arbitrage) is the one principle tied to the biggest wins**: Primate (banana allegory), Crayon, MonkeyExplains, Casual Finance FOLLOWED; Capital Case and Econ in a Nutshell NOT; Economics Explained NOT. 
4. **P01 outlier exploitation fails inside this cluster**: Primate, Casual Finance, Capital Case NOT FOLLOWED (they did not repeat their outlier topic); only Economics Explained FOLLOWED.
5. **P08 title engine**: Primate, Casual Finance, MonkeyExplains, Economics Explained NOT FOLLOWED yet still reach 350-550k medians, so title mechanics are weaker than topic/format here.

## PENNY (@pennyexplainsfinance) - 13 of 18 videos, LOW CONFIDENCE
Evidence VERIFIED (public views, snapshot 2026-11-12, 1-27 days old). No transcripts/thumbnails: P10-P18, P22 NOT TESTABLE.
- P21 topic lever: **FOLLOWED in the bad sense** - "Who Does America Owe $40 Trillion? (ELI5)" 1,151,039 views = 76% of the 13-video total (1.52M); the same-topic follow-up "Is America's $40T Debt a Ponzi Scheme?" 13,568 (85x lower).
- P01: one outlier (>=10x median ~13k); repeat of its topic did not repeat the result -> NOT FOLLOWED / contradicted by the data.
- P03/P05: ELI5 format (a Primate/Crayon/Monkey-style format, so a late entrant, not an originator); also a "Real Math" decision video (Renting vs Buying 44k, perennial decision) - format variety PARTIALLY FOLLOWED.
- P08: 6/13 titles carry a $ amount or number (Google $500B, 20 Years, $40T x2, 1 Cent) - PARTIALLY FOLLOWED.
- P19: durations 6:29-17:03, all but one above 8 min; views don't track length.
- P20: ~13 long videos in 27 days (about 3 a week) - cadence high; the 5 missing videos of 18 unresolved.
- Conclusion: topic-driven single hit; not yet a repeatable model.

## Paper Billions (@PaperBillionsTV) - 3 of 3 videos, VERY LOW CONFIDENCE
- 9.65k subs, 2.67M total views, 2 videos at 1.10M and 1.47M within 2-4 days; IPO video 98k.
- P21: the two hits are current-event money stories (Nvidia spy, market crash); P06/P07: news-hook + story title ("How a Chinese Spy Got Inside Nvidia"). P08: all 3 titles name a subject + stake ($80 Billion, Nvidia). P09 no generic subjects.
- Risk: calendar/news topics decay (study finding: trend-dependent concepts); n=3 gives no pattern. Only 6 days of life.

## Cross-cluster conclusion
- Common winning ingredient across the 9: **a famous/big-number subject presented as simple allegory or story** (banana debt, Wolf of Wall Street ELI5, $40T debt, Nvidia spy) with a one-idea thumbnail; the unique PDF mechanics (hooks, loops) are not what separates them.
- Repeatability is weak: Primate (hit-driven Shorts), PENNY ($40T), Econ in a Nutshell (money laundering 1.04M vs median 4.8k) show single outliers. Casual Finance, Economics Explained, MonkeyExplains and Crayon show the highest floors (medians 250-550k) - the strongest models to study for repeatability.
- Not used: CTR, retention, Google Trends, comments. No transcripts for PENNY/Paper Billions.
