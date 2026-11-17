# Sarah Rickshaw — Channel Forensic Report

Channel #060 of 69 · investigation tier 3 (data-availability order, not a quality rank) · research date 2026-11-12 · source DB `finance_economics_complete.db` sha256 fa6fd1b2…d20 (branch data/finance-economics-complete-2026-11-11 @933f236e).

Evidence labels used: **VERIFIED** (directly in DB / public page), **INFERRED** (derived from DB text by rule or analyst reading), **HYPOTHESIS** (plausible, untested), **UNKNOWN**. Public view counts do not reveal CTR, retention or traffic sources; none of those are claimed.

**Key conclusion:** Two-week-old senior-benefits network channel (Oct 2026, 12 videos, 8 near-duplicate flags) whose winners reproduce other channels' scripts nearly word-for-word — **"Every Senior Should Check These 7 Benefits for January 2027" (277k) opens with Mark Calloway's exact "$117 more every single month… $1,404 more over the year without filling out a single form"; "Never Keep More Than This in the Bank After 65" (72k) opens with Housing's exact garnishment paragraph** — while Medicare-deadline and spouse-death videos flop (~500-970 views).

## 1. Channel identity and positioning
Network presenter style; handle @SarahRickshaw; registered "Medicare / Social Security for seniors". Audience: US 62+.

## 2. Database inventory and coverage
- Channel ID `UCn2nfMN6I-ozJikqW-zk_6A` · handle @SarahRickshaw · https://www.youtube.com/channel/UCn2nfMN6I-ozJikqW-zk_6A
- Registered sub-niche: Medicare / Social Security for seniors · subscribers: 1,950 · availability: AVAILABLE nan
- Description: Welcome to Sarah Rickshaw! 💰  Your personal finance, investment advice, saving, budgeting, and economics blog.  A place where you will find answers to your money questions, plus guidance on making the best financial decisions for your future.  And a place to learn more about different ways to grow your money and create lasting wealth.  Subscribe to my blog to get simple financial tips and guidance…
- Videos in DB 12 (long 12, Shorts 0); views 12; transcripts 12 (100%); thumbnail images 12 (100%); FULL metadata 100%; PI-classified long 12
- Dates 2026-10-12 → 2026-10-26; median views 4,869; p90 69,816; max 276,511
- Cadence: 12.0 uploads/month over 1.0 months; median gap 1.0 d; max gap 2 d; weekday mode Monday
- Duration (min): median 18.4; p10 12.0; p90 25.5; first-third median 15.6 vs last-third 20.8
- Spearman(gap-before-upload, PI) = -0.07; Spearman(duration, PI) = 0.45; median PI first third 1.76 vs last third 0.35
- PI classes (long): Underperforming 6, Breakout 4, Successful 2; near-duplicate-script flags 8
- Titles whose word-set also appears on another channel: 0 (0%)
- **Every Senior Should Check These 7 Benefits for January 2027** — [06XLtP1gyM0](https://www.youtube.com/watch?v=06XLtP1gyM0) · 2026-10-19 · 18.65 min · 276,511 views · PI 93.45 (Breakout) · senior_perks_discounts/list_countdown · face=True · thumb text: “JANUARY/2027/SENIORS”
- **Never Keep More Than This in the Bank After 65 — Most Seniors Don’t Know** — [NXbwK51_1n8](https://www.youtube.com/watch?v=NXbwK51_1n8) · 2026-10-22 · 19.50 min · 72,315 views · PI 24.44 (Breakout) · banking_cash/warning_mistake · face=True · thumb text: “THEY/CAN/AN/THIS/AMOUNT.”
- **Born Before 1967? 4 Social Security Changes Coming for You in 2027** — [u8uufIVsWoc](https://www.youtube.com/watch?v=u8uufIVsWoc) · 2026-10-16 · 21.82 min · 47,324 views · PI 15.99 (Breakout) · social_security/news_change_update · face=True · thumb text: “BORN/OUP”
- **Medicare Is Canceling Plans for 2027 — Check Your Mail NOW** — [yyVM5uYVAeg](https://www.youtube.com/watch?v=yyVM5uYVAeg) · 2026-10-20 · 18.02 min · 500 views · PI 0.07 (Underperforming) · medicare_health_costs/news_change_update · face=True · thumb text: “MEDICARE/<j”
- **Every Senior on Medicare Should Check This Before October 15** — [FPka3UI5u8o](https://www.youtube.com/watch?v=FPka3UI5u8o) · 2026-10-14 · 7.52 min · 754 views · PI 0.11 (Underperforming) · medicare_health_costs/statement_other · face=True · thumb text: “THIS”
- **If Your Spouse Dies, What Happens to the Money in Your Joint Bank Account?** — [HEgn2UneFKk](https://www.youtube.com/watch?v=HEgn2UneFKk) · 2026-10-13 · 14.42 min · 967 views · PI 0.14 (Underperforming) · banking_cash/question · face=True · thumb text: “**/JOINT/BANK/RECOUNT/THESE/THINGS/HAPPEN”

Per-video field status (AVAILABLE / MISSING / UNVERIFIED / NOT APPLICABLE) is in `VIDEO_INVENTORY.csv`. Note: the source DB was capped at ~100 newest uploads per channel for most channels, so this is not the full lifetime library.

## 3. Complete video catalogue
All 12 videos in the database (also `VIDEO_INVENTORY.csv`). PI = views ÷ median of 15 nearest-in-time uploads (same channel & format); blank PI = not classifiable (too new/too few comparables).

| # | date | title | min | views | PI | class | topic | title format | transcript |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-12 | [Seniors 65+: You Could Be Overpaying These 5 Bills Every Month](https://www.youtube.com/watch?v=dJ0IX32h1fk) | 18.1 | 31,989 | 10.81 | Breakout | social_security | statement_other | Y |
| 2 | 2026-10-13 | [If Your Spouse Dies, What Happens to the Money in Your Joint Bank Account?](https://www.youtube.com/watch?v=HEgn2UneFKk) | 14.4 | 967 | 0.14 | Underperforming | banking_cash | question | Y |
| 3 | 2026-10-14 | [Every Senior on Medicare Should Check This Before October 15](https://www.youtube.com/watch?v=FPka3UI5u8o) | 7.5 | 754 | 0.11 | Underperforming | medicare_health_costs | statement_other | Y |
| 4 | 2026-10-15 | [Every Senior Should Check These 6 Things Before October Is Over](https://www.youtube.com/watch?v=2khKtIjjx7s) | 16.8 | 9,984 | 3.37 | Successful | social_security | list_countdown | Y |
| 5 | 2026-10-16 | [Born Before 1967? 4 Social Security Changes Coming for You in 2027](https://www.youtube.com/watch?v=u8uufIVsWoc) | 21.8 | 47,324 | 15.99 | Breakout | social_security | news_change_update | Y |
| 6 | 2026-10-17 | [Every Senior Should Do These 7 Things in November — Or Pay More in 2027](https://www.youtube.com/watch?v=-TLkYTBt_-A) | 26.0 | 6,779 | 2.29 | Successful | medicare_health_costs | list_countdown | Y |
| 7 | 2026-10-19 | [Every Senior Should Check These 7 Benefits for January 2027](https://www.youtube.com/watch?v=06XLtP1gyM0) | 18.6 | 276,511 | 93.45 | Breakout | senior_perks_discounts | list_countdown | Y |
| 8 | 2026-10-20 | [Medicare Is Canceling Plans for 2027 — Check Your Mail NOW](https://www.youtube.com/watch?v=yyVM5uYVAeg) | 18.0 | 500 | 0.07 | Underperforming | medicare_health_costs | news_change_update | Y |
| 9 | 2026-10-21 | [Every Senior Should Check Their Cash Before November 1 — Don’t Miss This](https://www.youtube.com/watch?v=guUp240aJKk) | 22.0 | 1,826 | 0.27 | Underperforming | banking_cash | statement_other | Y |
| 10 | 2026-10-22 | [Never Keep More Than This in the Bank After 65 — Most Seniors Don’t Know](https://www.youtube.com/watch?v=NXbwK51_1n8) | 19.5 | 72,315 | 24.44 | Breakout | banking_cash | warning_mistake | Y |
| 11 | 2026-10-23 | [Seniors: 10 New Social Security Limits for 2027 You Need to Know](https://www.youtube.com/watch?v=v1SfK6v_WEE) | 25.9 | 2,959 | 0.44 | Underperforming | social_security | news_change_update | Y |
| 12 | 2026-10-26 | [BIG Medicare Changes Are Coming in 2027 — Seniors Need to Know This](https://www.youtube.com/watch?v=IEtKlIzICbc) | 11.7 | 1,022 | 0.15 | Underperforming | medicare_health_costs | news_change_update | Y |

## 4. Topic and sub-niche map
| topic | n | long | median views | median PI | succ/breakout | under | first | last |
|---|---|---|---|---|---|---|---|---|
| medicare_health_costs | 4 | 4 | 888 | 0.13 | 1 | 3 | 2026-10-14 | 2026-10-26 |
| social_security | 4 | 4 | 20,986 | 7.09 | 3 | 1 | 2026-10-12 | 2026-10-23 |
| banking_cash | 3 | 3 | 1,826 | 0.27 | 1 | 2 | 2026-10-13 | 2026-10-22 |
| senior_perks_discounts | 1 | 1 | 276,511 | 93.45 | 1 | 0 | 2026-10-19 | 2026-10-19 |

Title-format mix (INFERRED tags): news_change_update: n=4.0, medPI=0.29 · list_countdown: n=3.0, medPI=3.37 · statement_other: n=3.0, medPI=0.27 · question: n=1.0, medPI=0.14 · warning_mistake: n=1.0, medPI=24.44

Senior perks/benefits (PI 93), banking (24), Social Security (16) win; Medicare (0.07-0.11) fails.

## 5. Winning video analysis
1. **Every Senior Should Check These 7 Benefits for January 2027** (06XLtP1gyM0, 277k, PI 93.5): verbatim hook of Mark Calloway's Pfm1t6xd88A (17 Oct, 295k) two days later (VERIFIED identical sentences).
2. **Never Keep More Than This in the Bank After 65 — Most Seniors Don't Know** (NXbwK51_1n8, 72k, PI 24.4): verbatim opening of Housing's NXhhbwvx3Fg (10 Oct).
3. **Born Before 1967? 4 Social Security Changes Coming for You in 2027** (u8uufIVsWoc, 47k, PI 16): birth-year grouping.

### Evidence: top-PI long-form videos
- **Every Senior Should Check These 7 Benefits for January 2027** — [06XLtP1gyM0](https://www.youtube.com/watch?v=06XLtP1gyM0) · 2026-10-19 · 18.65 min · 276,511 views · PI 93.45 (Breakout) · senior_perks_discounts/list_countdown · face=True · thumb text: “JANUARY/2027/SENIORS”
  - 0-30s: “Starting in January, the average retired couple on Social Security will get $117 more every single month. That is $1,404 more over the year without filling out a single form. And believe it or not, that is the smallest piece of good news coming for your money this January. For the last few months, almost everything you have heard about retirement money has been bad news. Prices going up, Medicare plans being dropped, warnings …”
  - end: “Six, if your income and savings are very low, apply for SSI even if you own your home. Seven, if your income is under about $1,800 a month, apply for a Medicare Savings Program. It can put about $2,400 a year back in you…” · sources: Social Security Administration (SSA); IRS; Congress / legislation; Trustees report; Company filings / earnings
- **Never Keep More Than This in the Bank After 65 — Most Seniors Don’t Know** — [NXbwK51_1n8](https://www.youtube.com/watch?v=NXbwK51_1n8) · 2026-10-22 · 19.50 min · 72,315 views · PI 24.44 (Breakout) · banking_cash/warning_mistake · face=True · thumb text: “THEY/CAN/AN/THIS/AMOUNT.”
  - 0-30s: “If a debt collector wins a court judgment against you, federal law automatically protects only about 2 months of your social security sitting in your bank account, and every dollar above that line can be frozen within 2 business days of the bank getting the order. Not your whole balance, not your life savings. 2 months. And that is just one of the lines. There are seven of them. Seven amounts that once your bank”
  - end: “property site. Seven, open every letter that says your bank is merging and check your coverage with the FDIC. If a a order ever hits your account, call a local legal aid office right away. And to check your deposit insur…” · sources: Social Security Administration (SSA); IRS; CBO / Treasury; VA
- **Born Before 1967? 4 Social Security Changes Coming for You in 2027** — [u8uufIVsWoc](https://www.youtube.com/watch?v=u8uufIVsWoc) · 2026-10-16 · 21.82 min · 47,324 views · PI 15.99 (Breakout) · social_security/news_change_update · face=True · thumb text: “BORN/OUP”
  - 0-30s: “Find your birth year on the screen right now because starting in January, the rules for your Social Security, your Medicare, and your taxes split into four groups. And the only thing that decides your group is the year you were born. Two people can do exactly the same thing next year. Same income, same choice, same paperwork. One of them pays nothing, the other pays a penalty every month for the rest of their”
  - end: “were born in 1962, mark your Medicare window on the calendar today. And if Cobra is your plan, call Social Security about part B before you do anything else. And every group, check your drug plan before the 7th of Decemb…” · sources: Social Security Administration (SSA); IRS; CMS / Medicare.gov; Congress / legislation; Trustees report; Company filings / earnings

## 6. Underperforming video analysis
**Medicare Is Canceling Plans for 2027 — Check Your Mail NOW** (yyVM5uYVAeg, 500), **Every Senior on Medicare Should Check This Before October 15** (FPka3UI5u8o, 754), **If Your Spouse Dies, What Happens to the Money in Your Joint Bank Account?** (HEgn2UneFKk, 967 — Walter Canada's/Lana's concept).

### Evidence: bottom-PI long-form videos
- **Medicare Is Canceling Plans for 2027 — Check Your Mail NOW** — [yyVM5uYVAeg](https://www.youtube.com/watch?v=yyVM5uYVAeg) · 2026-10-20 · 18.02 min · 500 views · PI 0.07 (Underperforming) · medicare_health_costs/news_change_update · face=True · thumb text: “MEDICARE/<j”
  - 0-30s: “At this very moment, one diagnostic code entered into your medical record can give private insurers grounds to restrict your access to health care without broad network limits. And before December 7th, as many as 5 million older Americans may learn that their current health plan is being discontinued. Over the next 15 minutes, we'll look at ways to help protect you or your parents from unexpected medical bills that could reach…”
  - end: “or even your grandparents navigate this marketing blitz and celebrity commercials alone during this Medicare open enrollment season. This weekend, check their mail for a annual notice of change or a cancellation letter. …” · sources: CMS / Medicare.gov; Congress / legislation; Company filings / earnings; News outlets; Academic / research study
- **Every Senior on Medicare Should Check This Before October 15** — [FPka3UI5u8o](https://www.youtube.com/watch?v=FPka3UI5u8o) · 2026-10-14 · 7.52 min · 754 views · PI 0.11 (Underperforming) · medicare_health_costs/statement_other · face=True · thumb text: “THIS”
  - 0-30s: “If you're on Medicare, there's a date eight days from now that most people will walk straight past October 15th. It's the day open enrollment begins, and it's also the deadline for a letter from an old employer or union that quietly decides whether you could be paying a penalty for as long as you're on Medicare. At the same time, the drug cost numbers for 2027 are already locked in, and they all moved”
  - end: “Medicare number. If someone does, hang up. Call back only on a number you looked up yourself. Let me recap. The drug cap goes from 2 in state to 2,000. Your fixed income might not be heads up number. Hmm, it's education,…” · sources: Social Security Administration (SSA); CMS / Medicare.gov
- **If Your Spouse Dies, What Happens to the Money in Your Joint Bank Account?** — [HEgn2UneFKk](https://www.youtube.com/watch?v=HEgn2UneFKk) · 2026-10-13 · 14.42 min · 967 views · PI 0.14 (Underperforming) · banking_cash/question · face=True · thumb text: “**/JOINT/BANK/RECOUNT/THESE/THINGS/HAPPEN”
  - 0-30s: “The first time you walk into a bank after losing your husband or your wife, you are going to be asked for a piece of paper and you are going to be asked questions about an account the two of you used together for years. Here is what almost nobody tells you before that day arrives. What happens to that money was decided a long time ago by a few words on a form that”
  - end: “kindest thing you can do for a friend who is grieving is to hand them clear answers so they do not have to figure it all out alone. And if you want more videos like this every week in plain English, subscribe to the chan…”

## 7. Successful vs failed comparison
Copied scripts both won and lost; Medicare topics lost on every network channel tested (Nia, Mark Calloway, Lana, Marcus, Housing, Sarah) — a consistent cross-channel failure topic.

| feature | upper half | lower half |
|---|---|---|
| t_number | 100% | 83% |
| t_dollar | 0% | 0% |
| t_question | 17% | 17% |
| t_you | 33% | 50% |
| t_fear_risk | 17% | 0% |
| t_urgency | 67% | 83% |
| t_secret_truth | 0% | 0% |
| t_named_entity | 17% | 67% |
| t_caps_word | 0% | 33% |
| t_year | 50% | 50% |
| h_first_sentence_q | 0% | 0% |
| h_you_in_30s | 100% | 100% |
| h_number_30s | 67% | 83% |
| h_dollar_30s | 17% | 50% |
| h_stakes_30s | 0% | 17% |
| h_contrarian_30s | 17% | 50% |
| h_open_loop_30s | 17% | 50% |
| h_promise_30s | 33% | 50% |
| h_story_open | 0% | 0% |
| h_greeting_open | 0% | 0% |
| h_first_person_30s | 17% | 17% |
| s_cta_end | 50% | 83% |
| tx_words (median) | 3,780 | 3,062 |
| s_num_density (median) | 3.16 | 3.67 |
| s_q_density (median) | 0.08 | 0.14 |
| s_but_density (median) | 0.36 | 0.28 |
| s_example_density (median) | 0.05 | 0.03 |
| s_data_density (median) | 1.26 | 1.51 |
| s_loop_density (median) | 0.01 | 0.00 |
| s_you_density (median) | 4.61 | 3.64 |
| s_wpm (median) | 204 | 204 |
| h_title_overlap_150 (median) | 0.32 | 0.49 |
| i_promise_pos (median) | 121 | 176 |
| t_len (median) | 64.50 | 65.50 |
| th_text_words (median) | 3.00 | 3.50 |
| th_colorfulness (median) | 95.19 | 92.09 |
| thumbnail has face | 100% | 100% |



## 8. Topic discovery and research sources
Network scripts; real rules (Social Security garnishment protection; COLA).

Institutions named in transcripts/descriptions (rule-based; 'Academic / research study' matches generic words like “study/research” and is low-confidence): IRS 8, Social Security Administration (SSA) 7, CMS / Medicare.gov 7, Congress / legislation 5, Trustees report 5, Company filings / earnings 5, CBO / Treasury 4, News outlets 2, Academic / research study 2, Federal Reserve 1
Description link domains: none
Per-video source map: `SOURCE_MAP.csv`.

## 9. Trend behaviour
Calendar (January 2027 changes) framing helps.

## 10. Thumbnail strategy
Montage not inspected.

## 11. Title strategy
Network formulas.

## 12. Hook and introduction strategy
Copied verbatim from sister channels (VERIFIED for two).

## 13. Script and storytelling strategy
7-22 min; 8 of 12 near-duplicate flags.

## 14. Audience engagement model
Benefit/protection anxiety.

## 15. Upload and publishing strategy
12 videos in two weeks.

## 16. PDF principle evaluation
Judge: *YouTube Automation – Complete Master Playbook* (556 pp., sha256 c630c24b…576d). Supporting authority: global-youtube-knowledge (DS-000011/18/31) — see `00_PROJECT_OVERVIEW/GLOBAL_KNOWLEDGE_MAP.md`. Automated evidence uses text proxies; verdict = analyst override where noted, else rule-based draft.

| ID | PDF principle (location) | What the PDF says | Evidence from channel (automated, incl. winners vs rest where testable) | Verdict | Analyst note |
|---|---|---|---|---|---|
| P01 | Module 2.1 Outlier Concept, pp.6-9; Method 1 Outlier Transplant, pp.34-35 | Find videos that beat the channel norm (5-10x strong, 10x+ clear outlier) and treat their TOPIC as proven demand; build the calendar from validated outliers. | 4 long-form ≥5x and 4 ≥10x own baseline; after 5 winners, next-10 uploads repeat the winner's topic 21% vs base rate 28% | **NOT FOLLOWED** |  |
| P02 | Module 2.2 Niche vs Format vs Template, p.11 | A niche is an audience + persistent interest + monetisation path, not a topic; every video should feel like it belongs to the same channel. | top-2 topics (social_security, medicare_health_costs) = 67% of uploads; explicit audience marker in 75% of titles | **FOLLOWED** |  |
| P03 | Module 2.2, pp.12-13 | One niche can carry many formats; add formats to grow without changing niche. | 3 title-format types each ≥10% of uploads (news_change_update 33%, statement_other 25%, list_countdown 25%, question 8%) | **FOLLOWED** |  |
| P04 | Module 2.2 p.13; Masterclass Ch.23 p.351; Web research §7 p.555 | Avoid repetitive/mass-produced uploads; rotating templates alone is not enough — each video needs distinct substance (inauthentic-content policy). | near-duplicate-script flag on 67% of videos; repeated title word-sets within channel 0% | **CONTRADICTED BY EVIDENCE** | 67% near-duplicate scripts, cross-channel copying. |
| P05 | Module 2.3 Format Arbitrage pp.18-20; Module 2.4 Niche Bending pp.24-26 | Win by transplanting a proven format into a niche that lacks it, or by combining two overlapping niches. | requires historical competitor-format landscape at launch; analyst note in report if a bend is visible | **NOT TESTABLE** |  |
| P06 | Module 2.7 Competitor Research pp.28-30; Method 1 p.34 | Study competitors’ top videos, titles, thumbnails, cadence and comments; cover proven topics with original content. | 0% of titles share a word-set with another channel; this channel published first on 0 of 0 | **CONTRADICTED BY EVIDENCE** | wholesale copying; results lottery-like. |
| P07 | Method 2 Title Template Injection pp.39-40; 100 Title Formats pp.52-64 | Inject niche topics into proven title psychology families (mystery, downfall, contradiction, revelation, practical, conflict…), but the content must deliver. | 0% of titles match a 100-format family | **NOT FOLLOWED** |  |
| P08 | 100 Title Formats p.53 (five-part engine), p.66 scorecard | A strong title names a recognisable subject, a situation, a trigger, a tension and a concrete promise/stakes. | 92% of titles carry a number/$/named entity | **FOLLOWED** |  |
| P09 | 100 Title Formats p.68 (12 mistakes); Masterclass Ch.19 p.345 | Avoid generic subjects, two promises, vague “this/they” openers, ALL CAPS overuse, overstated certainty. | titles with ≥3 ALL-CAPS words 0%; vague 'this/they' opener 0%; double-question 0% | **FOLLOWED** |  |
| P10 | 100 Title Formats p.66 (title+thumbnail one promise), p.68 #11 | Thumbnail should add a complementary clue, not repeat the title. | OCR thumbnail text found on 100%; median share of thumbnail words repeated from title 0.29 | **FOLLOWED** |  |
| P11 | Module 2.7 Thumbnail Teardown p.28 (supporting: DS-000011 Packaging SOP) | Study colour, text amount, faces/expressions, focal object, contrast and template consistency; one clear idea. | thumbnail images 100%; median OCR words 3.0 (OCR undercounts stylised text); face/character detected 100% (cartoon faces often missed) | **FOLLOWED** |  |
| P12 | Engagement Playbook §1 p.265; Masterclass Zone 1 p.320 | The first ~3-5 seconds must create curiosity: question, shock stat, contradiction, mystery, story drop, direct challenge. | opening ~75 words contain question/number/contradiction/story/you-hook in 83%; greeting/channel-intro opening 0% | **FOLLOWED** |  |
| P13 | Masterclass Zone 2 p.320; Engagement §18 p.283 | Within ~5-15 s answer “why should I care?” — connect to the viewer’s money, safety or identity. | explicit stakes/why-it-matters language early in 8% | **NOT FOLLOWED** |  |
| P14 | Masterclass Zone 3 p.320; Ch.23 p.350 | Open at least one curiosity loop before ~30 s and keep it open. | explicit open-loop/promise phrase in first ~150 words of 33% | **PARTIALLY FOLLOWED** |  |
| P15 | Engagement §2 & §7 pp.267, 272 | Use bridging teases / micro-cliffhangers at segment transitions to prevent drop-off. | bridge/cliffhanger phrases per 100 words (median) 0.000 | **NOT FOLLOWED** |  |
| P16 | Engagement §8 p.273 | Precise numbers, dates, named sources and expert quotes signal research and keep sceptical viewers. | data/citation terms per 100 words 1.38; videos naming an institution/source 92% | **FOLLOWED** |  |
| P17 | Engagement §6 p.271 | Second-person address makes the viewer a participant (“if you own…”, “imagine you…”). | 'you/your' per 100 words (median) 4.51 | **FOLLOWED** |  |
| P18 | Engagement §15-16 pp.280-281; Deployment p.284 | Close loops, then future-pace to a next video; strongest CTA right after a payoff, not only at the end. | next-video tease in final ~60 words 17%; any CTA in final 10% 67% | **PARTIALLY FOLLOWED** |  |
| P19 | Module 2.3 p.19 (8+ min sweet spot); Web research §8 p.555 | Course: formats should fill 8+ minutes; appendix: 8 min is a mid-roll eligibility rule, length should follow the story. | median long-form length 18.4 min; Spearman(duration, PI) 0.45 — 8+ min is an ad-eligibility rule, not a success rule (PDF p555) | **FOLLOWED** |  |
| P20 | Module 2.7 Posting cadence p.29 | Check upload frequency, consistency, dead periods and growth inflection points. | median gap 1.0 d, gap CV 0.92, longest pause 2 d | **FOLLOWED** |  |
| P21 | Topic Selection Masterclass intro p.33 | “A bad video on the right topic will outperform a great video on the wrong topic” — topic selection is the main lever. | spread of median PI across topics 54.14x (best social_security) vs across title formats 12.53x (best list_countdown) | **FOLLOWED** |  |
| P22 | Method 2 warning p.40; 100 Formats p.68 #12; Masterclass Ch.19 p.345 | Title gets the click, content keeps the viewer: the opening must confirm and the video must deliver the title’s promise. | median share of title keywords that appear in the first ~150 spoken words 0.38 | **PARTIALLY FOLLOWED** |  |

## 17. Strengths and weaknesses
None original. Weaknesses: copied scripts (policy risk), Medicare topics.

## 18. Replicable working model
Not a model — network duplication evidence.

## 19. What to copy
Nothing; study the originals instead.

## 20. What not to copy
Script copying; Medicare deadline videos in this network style.

## 21. Missing evidence and limitations
Two weeks; montage not inspected.

- Not available from this dataset for any channel: CTR, impressions, retention curves, traffic sources, subscriber growth history, comments text. Hook timings are word-position estimates (untimed transcripts).

## 22. Final channel diagnosis
1) Copied network scripts; some won on distribution. 2-13) As Housing (051): duplication produces fragile, lottery-like outcomes and policy risk. Lesson: **identical scripts across channels are not a strategy anyone should copy.**
"I would not replicate this channel; the originals (Mark Calloway Pfm1t6xd88A, Housing NXhhbwvx3Fg) show the topics, and the lesson is to write original, verified scripts."
