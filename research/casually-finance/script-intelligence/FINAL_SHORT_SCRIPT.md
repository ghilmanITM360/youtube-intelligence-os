# Final Short — original script for owner approval

**Title:** Why Raising Rates Costs the Fed Money
**Topic:** The Fed's own rate-hike bill. Its deferred asset stopped shrinking after the Sept 16, 2026 hike (TOPIC_RESEARCH rank 1, score 93/100).
**Status:** draft for approval. Facts are current to the H.4.1 release of **2026-10-08** (week ended Oct 7). **Re-check H.4.1 on publish day** (next releases Oct 15 and Oct 22; FOMC Oct 28). If the weekly series stops rising, rewrite S12.

## Narration (complete)

> The Fed raised rates in September to fight inflation. One of the first bills to go up was its own.
>
> Banks park about $3 trillion at the Fed, and it pays them interest at a rate that moves the moment the Fed moves. But the Fed earns mostly from bonds, many bought in 2020 and 2021, when 10-year yields averaged under 1.5%. Those don't reset.
>
> That's how a central bank loses money. Starting in 2022, losses piled into a hole that hit $245 billion this year. Until it's filled, the Fed's usual payments to the Treasury stay on hold. In 2021, that was $107 billion.
>
> This year, the Fed started climbing out, until progress stalled near $233 billion, then came the hike. A quarter point on $3 trillion is roughly $7.5 billion a year. Since then, the hole has grown three weeks straight.
>
> It won't break the Fed. But every hike now pushes back the day the Treasury gets paid again. The Fed meets again October 28th.

## Length and timing

- **Word count: 167** as written (numerals count as one word, matching how the corpus WPM was measured from Whisper tokens). About 191 words if every number is spoken in full ("two hundred forty-five billion dollars").
- **Estimated duration: ~52.5 s** at 191 wpm, the median narration pace of the channel's six transcribed Shorts (observed range 187–213 wpm). Range: **47.0 s** at 213 wpm to **58.9 s** at a slower 170 wpm.
- Why ~52 s and not 60+: the brief caps the Short at 59 s. The channel's recent Shorts run longer (Aug–Oct median 67.5 s), but its proven complete-mechanism Shorts sit at 61–69 s on ~210–230 ASR words. Our 167 words deliver one mechanism at the same density, with headroom for a slower read.

| Section | Sentences | Words | Time @191 wpm |
|---|---|---:|---|
| Hook: paradox | S01–S02 | 20 | 0.0–6.3 s |
| Mechanism | S03–S05 | 45 | 6.3–20.4 s |
| Stakes and size | S06–S09 | 40 | 20.4–33.0 s |
| Turn: dated evidence | S10–S12 | 38 | 33.0–44.9 s |
| Payoff + forward date | S13–S15 | 24 | 44.9–52.5 s |

## Evidence for every material claim

Labels: VERIFIED (primary source fetched 2026-10-14), PARTIAL (supported, with a stated gap), CALCULATION (our arithmetic on verified inputs), INTERPRETATION (derived reasoning, conditional). Source IDs refer to SOURCE_REGISTER.csv.

| # | Sentence | Claim | Status | Source(s) |
|---|---|---|---|---|
| S01 | The Fed raised rates in September to fight inflation. | Sep 16, 2026: target range +¼ pt to 3.75–4.00%; statement cites elevated inflation and the 2% goal | VERIFIED | SR-W01 |
| S02 | One of the first bills to go up was its own. | IORB rose 3.65% → 3.90%, effective Sep 17, the day after the decision | VERIFIED (framing: "bill" = interest expense) | SR-W02, SR-W03 |
| S03 | Banks park about $3 trillion at the Fed, and it pays them interest at a rate that moves the moment the Fed moves. | Reserve balances $3.022T (Oct 7, 2026); interest is paid at IORB, which is reset with each decision | VERIFIED (one-day effective lag simplified) | SR-W04, SR-W02 |
| S04 | But the Fed earns mostly from bonds, many bought in 2020 and 2021, when 10-year yields averaged under 1.5%. | Securities are ~96% of Fed assets ($6.374T of $6.657T, Mar 25, 2026); holdings rose $3.87T → $8.49T from Q1 2020 to Q2 2022; 10-year yield averaged 0.89% (2020) and 1.45% (2021) | PARTIAL: the share of *current* holdings dating from 2020–21 was not verified, so "many" is used rather than "most" | SR-W07, SR-W09, SR-W10 |
| S05 | Those don't reset. | Fixed-coupon Treasuries and agency MBS pay their original coupon until maturity | VERIFIED as a simplification (the small FRN and TIPS holdings behave differently) | general instrument terms |
| S06 | That's how a central bank loses money. | A deferred asset arises when earnings do not cover costs | VERIFIED (H.4.1 footnote) | SR-W04 |
| S07 | Starting in 2022, losses piled into a hole that hit $245 billion this year. | Deferred asset first negative Sep 2022; monthly average peaked at −$245.4B (Feb 2026); the Fed reported $244B on Mar 25, 2026 | VERIFIED | SR-W06, SR-W07 |
| S08 | Until it's filled, the Fed's usual payments to the Treasury stay on hold. | The deferred asset is "the amount of net earnings the Reserve Banks must realize before remittances to the Treasury resume" | VERIFIED (nuance: a few individual Reserve Banks remitted in isolated weeks, hence "usual") | SR-W04, SR-W07 |
| S09 | In 2021, that was $107 billion. | 2021 remittances to the Treasury: $107.4B (preliminary, unaudited release) | VERIFIED | SR-W08 |
| S10 | This year, the Fed started climbing out, until progress stalled near $233 billion, then came the hike. | Weekly level −$238.4B (Jun 3) → −$233.0B (Aug 5) → −$232.751B (Sep 16), roughly flat Aug–mid-Sep | VERIFIED | SR-W06 |
| S11 | A quarter point on $3 trillion is roughly $7.5 billion a year. | 0.25% × $3.022T = $7.56B/yr extra interest on reserves alone (excludes ~$0.33T ON RRP, which adds ~$0.8B; assumes constant balances) | CALCULATION | SR-W02, SR-W04 |
| S12 | Since then, the hole has grown three weeks straight. | Weekly levels −$232.999B (Sep 23), −$233.139B (Sep 30), −$233.587B (Oct 7): +$0.836B in three weeks | VERIFIED sequence. Causation is plausible but not proven: weekly data is noisy (it also rose on Aug 26) | SR-W06, SR-W04 |
| S13 | It won't break the Fed. | The Fed says negative net income and the deferred asset "do not affect" its ability to conduct policy or meet obligations | VERIFIED | SR-W07 |
| S14 | But every hike now pushes back the day the Treasury gets paid again. | Higher IORB → higher interest expense → slower paydown of the deferred asset → later resumption of remittances | INTERPRETATION (all else equal; a hike also lifts some Fed income on new bill purchases and repo, but interest-bearing reserves + RRP (~$3.36T) far exceed that) | SR-W04, SR-W02 |
| S15 | The Fed meets again October 28th. | FOMC meeting Oct 27–28, 2026; the statement is released on the 28th | VERIFIED | SR-W05 |

No invented numbers. Every figure traces to a primary Federal Reserve, FRED (H.4.1 source) or Treasury page dated in SOURCE_REGISTER.csv. Secondary commentary (First Trust) was **not** used for any scripted number.

## Deliberately avoided (inaccurate or dramatic framings)

- "The Fed is broke / insolvent / bankrupt": false. Its losses do not impair operations (S13 says so).
- "Taxpayers pay the Fed's losses": no appropriation occurs. The real effect is forgone remittances (S08, S14).
- "The hike caused the hole to grow": stated as a sequence, not as sole causation (S10–S12).
- "The Fed sends the Treasury nothing": isolated Reserve Bank remittances occurred, so "usual payments… on hold" is used.

## Comparison with the observed Short structures (SCRIPT_DNA §B)

| Dimension | Channel evidence | This script |
|---|---|---|
| Hook | Contradiction stated in sentence one; topic named by 3–10 s | Paradox (rate hike raises the Fed's own bill); topic named at ~3 s |
| Time to mechanism | 5/6 Shorts by 7.5 s | 6.3 s |
| Structure | S1 (rSa2aziEsAI): paradox → mechanism → trap reveal → close. S2 (6S3PzAUFnXQ): mechanism → official numbers → dated turning point | Hybrid S1 + S2: paradox → mechanism → reveal and size → dated turn → payoff with a forward date. The "armchair objection" beat is dropped because it is a Japan-Short signature |
| Mechanism count | One per Short | One (floating liability vs fixed-rate assets) |
| Rhythm | Long chained sentences broken by ≤7-word punchlines (5/6 Shorts) | 23-word and 19-word chains followed by "Those don't reset." (3 words); 5 sentences of ≤7 words |
| Number density | 15–55% of sentences contain a number | 7 of 15 (47%) |
| Pace | 187–213 wpm | written to 191 wpm |
| Ending | 3/6 complete answer, 2/6 open loop, no CTA | Complete answer, then a dated forward cue (Oct 28) as a light open loop. No CTA |
| Stakes | National/systemic in 5/6 | National (Treasury payments; the Fed's fight against inflation) |

Originality check (2026-10-14): 5-gram overlap with all 16 transcripts and all 206 titles/descriptions = 1 generic phrase ("in 2020 and 2021 when"); 4-gram overlaps are generic ("the fed raised rates"). No signature line is reused ("It is an invoice", "It can't do both", "the answer is you", "financial monster", the oxygen metaphor).

## Out of scope (stopped here by instruction)

No thumbnail, visuals, storyboard, voiceover, animation or video. Waiting for owner approval.
