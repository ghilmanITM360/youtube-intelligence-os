# Title DNA — Casually Finance

All 206 snapshot titles were processed programmatically; Shorts are the priority. Performance = the playbook's age- and format-matched ratio and tier (`VIDEO_PERFORMANCE.csv`, branch `fb1e56d`, Oct 11 snapshot). 170 Shorts are aged (≥7 days); the aged-Shorts median ratio is 1.02. Feature rules are keyword/regex heuristics, features overlap, and medians are exploratory, not significance tests. A title association never proves the title caused the views (no CTR or impressions are available). This extends, rather than repeats, the playbook's all-format `TITLE_THUMBNAIL_PLAYBOOK.md`.

## Shape

- Shorts titles: **median 8 words (IQR 6–10), 45 characters**. Long-form is identical (8 words, 45 chars).
- **Title Case** is dominant. A lowercase "meme grammar" exists but is rare and weak in Shorts: "if united states so rich... why we all so poor?" 0.44×, "if ai so good... why everyone selling?" 0.50×, "if recession... why economic data good?" 1.19×, "the \*magic\* behind ai debt" 1.02× (n=4, median 0.77). It works once in long-form ("if war bad... why stocks go up?" 2.69×).
- Declarations far outnumber questions. Only 17 Shorts start with "What" or end in "?" (median 0.95).
- Shouted caps are rare and early ("The REAL Reason…", "WTF Is Happening…", "BROKEN").

## Feature associations (aged Shorts)

| Feature (regex) | n | Median ratio | Without | Top/Breakout count | Below/Under count | Label |
|---|---:|---:|---:|---:|---:|---|
| WHY/HOW explainer opening | 25 | **1.37** | 1.00 | 6 | 7 | PERFORMANCE_ASSOCIATION |
| Reversal / state change ("…Not Anymore", "Coming to an End", "Has Started") | 11 | 1.27 | 1.00 | 3 | 2 | PERFORMANCE_ASSOCIATION (small n) |
| Terminal period ("…Itself.") | 46 | 1.27 | 0.97 | 7 | 10 | PERFORMANCE_ASSOCIATION |
| Ellipsis ("…", "...") | 54 | 1.25 | 0.95 | 7 | 14 | PERFORMANCE_ASSOCIATION |
| America/US/government as subject | 28 | 1.20 | 0.98 | 7 | 8 | PERFORMANCE_ASSOCIATION |
| Negative-stakes word (broke, crisis, trap, fail…) | 35 | 1.19 | 1.01 | 6 | 11 | weak |
| Number ($, %, count) | 24 | 1.15 | 1.01 | 3 | 7 | weak |
| Parenthetical qualifier "(Actually)", "(Quietly)", "(Mathematically)" | 25 | 1.02 | 1.02 | 4 | 8 | neutral |
| Nobody/Everyone crowd framing | 24 | 0.98 | 1.03 | 6 | 8 | neutral |
| What/question | 17 | 0.95 | 1.02 | 3 | 8 | neutral-to-weak |
| You/your second person | 22 | **0.80** | 1.07 | 4 | 11 | weak |
| "If You Don't Understand X, You Don't Understand Y" | 6 | **0.78** | 1.03 | 0 | 3 | weak |
| "The REAL X" | 8 | **0.62** | 1.03 | 1 | 5 | weak |

## Recurring formulas, with strong and weak examples

| Formula | Strong (ratio) | Weak (ratio) | Read |
|---|---|---|---|
| **Why + subject + state** | turJ6VMfUjI "Why You (Mathematically) Need Inflation" 14.98; rSa2aziEsAI "Why Japan's Economy Is Awful" 11.85; SYSUh-oow6M "Why Being a Millionaire Doesn't Impress Anyone..." 6.10 | Tc-TUvGnMDI "Why a Record Stock Market Only Makes (Some) People Rich" 0.61; uzPl-GZRrRA "Why Gen Z and Millennials Can't Catch Up" 0.75 | 2 of the 3 highest-ratio Shorts. Strong cases name **one macro mechanism**; weak cases are broad inequality framings |
| **Era / state-change declaration** | Qof71Ef-3EU "The Cheap Money Era Is Coming to an End" 19.03 (top Short); ji2qFfcgSB4 "Everything We Know About Debt Is Changing" 3.20 | ojylN8STqeQ "The REAL Reason Investing Is Changing" 0.44 | Works with a concrete financial object (money, debt); weak when vague |
| **Subject… + twist** (ellipsis) | 6S3PzAUFnXQ "America's Debt Hasn't Broken... Yet" 5.11; JsK53moCyZA "The SpaceX IPO Nobody Can (Actually) Explain..." 7.83 | UAZwkrxS9RA "The Ugly Truth About Bitcoin…" 0.22; jXo9t3t4Wus "The Harder We Fight Inflation... The Worse It Gets." 0.34 | The ellipsis is common in winners and losers alike; the subject matters more |
| **Number-led fact** | RB5zVghPor8 "78% of The Government's Money Goes to Just 5 Things" 3.48; VcyCHhn9WB4 "$1.65 Trillion of Hidden AI Debt" 2.66 | cat9MQyNr8g "50% of America Owns Just 1% of the Stock Market" 0.44; zyQfmErwBNU "The $1.65 Trillion AI Shadow Debt Explained In 97 Seconds" 0.53 | Same $1.65T number scored 2.66 and 0.53: **number alone does not explain outcome** |
| **Contradiction pair** | CFrVTZBYa3Q "You're Celebrating Stocks, They're Heading For The Exits." 4.84 | -Yccxvjk76A "Wall Street's Economy Isn't Your Economy." 0.71 | |
| **Instructional "If you don't understand…"** | — (best: 9OX7I4KH6RA 1.09) | RP0t4UVZNTY "If You Don't Understand Reserve Currency Status…" **0.20 (lowest Short)** | Consistently weak |

**Identical-title counterexample.** fo8tcM2_xEw and CtLER-CK1_A share the title "You're About To Buy SpaceX... Whether You Like It Or Not" (case aside), 10 days apart. They scored **2.43× vs 0.58×**, which shows topic-run position and recency matter beyond wording.

## Recent shifts (share of Shorts titles per period)

| Feature | Mar–Apr 2026 (n=36) | May–Jul (n=87) | Aug–Oct (n=50) |
|---|---:|---:|---:|
| America/US subject | 6% | 15% | **30%** |
| Parenthetical qualifier | **31%** | 10% | 10% |
| Why/How opener | 28% | 13% | 8% |
| Ellipsis | 28% | **40%** | 18% |
| Terminal period | 14% | 34% | 22% |
| "The REAL…" | 11% | 1% | 6% |
| Median title words | 7 | 8 | 8.5 |
| Median Short duration | 46.5 s | 45 s | **67.5 s** |

`OBSERVED_PATTERN`: the channel moved away from parenthetical and "REAL" gimmicks toward **plain declarative statements about America and its money/debt**. Shorts also lengthened to ~60–75 s. This tracks the content shift toward bonds, debt and rates (TOPIC_RESEARCH).

## Top and bottom aged Shorts (ratio)

Top: Qof71Ef-3EU 19.03; turJ6VMfUjI 14.98; rSa2aziEsAI 11.85; JsK53moCyZA 7.83; SYSUh-oow6M 6.10; 6S3PzAUFnXQ 5.11; 10nEByVLya0 "The IPO Boom Is the Danger Sign" 5.06; CFrVTZBYa3Q 4.84; RB5zVghPor8 3.48; gUkJbLaqwmM "What Happens When a Market's Priced for Perfection" 3.26.

Bottom: RP0t4UVZNTY 0.20; UAZwkrxS9RA 0.22; yDxPLckhxMI "The Bitcoin Lie Nobody Will Admit" 0.24; jXo9t3t4Wus 0.34; BqE-JSB4W80 "What Do Robo-Advisor's (Actually) Do?" 0.39; H3PRCteue9Y "Your Dollar's Emergency Fund Is (Mostly) Not Spent on Emergencies" 0.40.

`PLAUSIBLE_HYPOTHESIS`: strong titles state **a single consequential macro claim in plain words** (cheap money ending, needing inflation, Japan awful, debt not broken yet). Weak titles lean on a device ("REAL", "Ugly Truth", "If you don't understand") or on niche institutional nouns (robo-advisors, emergency fund, reserve currency status) without a felt stake. Counterexample: "Why the Federal Reserve Can't Fix OUR Problems" (bUY77LwMR6E) is a plain institutional claim that scored only TYPICAL (1.10).

## Title candidates for the selected Short (see FINAL_SHORT_SCRIPT.md)

| # | Candidate | Pattern followed | Fits the script's promise because | Factual / misleading risk | Strong / weak precedent |
|---|---|---|---|---|---|
| 1 | **Why Raising Rates Costs the Fed Money** (7 words, 37 chars) | Why + subject + state (median 1.37, n=25) | The script explains exactly this: the hike raised the rate the Fed pays on ~$3T of reserves, while its bond income does not reset | Low. True as stated: the hike raises interest expense. It does not claim insolvency | Strong: turJ6VMfUjI 14.98, rSa2aziEsAI 11.85 (same reserve-interest mechanism for Japan). Weak: uzPl-GZRrRA 0.75; bUY77LwMR6E (Fed-named "Why") 1.10 |
| 2 | The Fed Is Losing Money Again... | State change + ellipsis | The script's turn: the paydown stalled and the hole grew three weeks running after the hike | **Medium.** "Again" rests on 3 weekly H.4.1 prints (+$0.84B); the trend could reverse, and the title can read as "the Fed is in trouble" | Strong: 6S3PzAUFnXQ 5.11, Qof71Ef-3EU 19.03. Weak: zHekycA0R3E "The Beginning of the End..." 0.69 |
| 3 | The Fed's $233 Billion Hole Just Got Deeper. | Number-led fact + terminal period | Uses the script's central number | **Medium.** "Deeper" is literally true but the change is 0.4%; the number cue implies a bigger move | Strong: RB5zVghPor8 3.48, 0inCzZ4pUzo "The $85 Billion Private Credit Problem." 1.96. Weak: DL7WdIHXAM0 "The $1.28 Trillion Crisis Everyone's Ignoring" 0.99; zyQfmErwBNU 0.53 |

## Final recommended title

### **Why Raising Rates Costs the Fed Money**

Chosen because:

1. It uses the formula behind 2 of the channel's 3 highest-ratio Shorts and the strongest positive association in the Shorts title set.
2. It sits at the recent length norm (7–8 words).
3. It makes **the exact promise the script fulfils**, with no exaggeration.
4. It duplicates no existing title; no Casually Finance title, description or transcript covers the Fed's own losses.

Candidates 2 and 3 are stronger curiosity hooks but carry the overstatement risks noted above. Hold candidate 2 for after the Oct 28 FOMC if the weekly series keeps rising.
