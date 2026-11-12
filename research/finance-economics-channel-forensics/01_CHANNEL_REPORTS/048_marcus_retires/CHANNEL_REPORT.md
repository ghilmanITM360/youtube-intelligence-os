# Marcus Retires — Channel Forensic Report

Channel #048 of 69 · investigation tier 2 (data-availability order, not a quality rank) · research date 2026-11-12 · source DB `finance_economics_complete.db` sha256 fa6fd1b2…d20 (branch data/finance-economics-complete-2026-11-11 @933f236e).

Evidence labels used: **VERIFIED** (directly in DB / public page), **INFERRED** (derived from DB text by rule or analyst reading), **HYPOTHESIS** (plausible, untested), **UNKNOWN**. Public view counts do not reveal CTR, retention or traffic sources; none of those are claimed.

**Key conclusion:** Five-week-old senior-benefits channel (7.5k subs, ~26 uploads/month) that **re-used the network's proven concepts**: the bank-amount and direct-deposit-rules concepts still broke out (244k and 142k), but its "7 Things IRS Can't Take From You" (the 4th-5th appearance of that concept, 7 Oct) drew 242 views, Medicare open-enrolment drew 93, and a "UK Pensioners" title on a US-script video drew 303 — late, saturated or mislocalised copies fail; 7 near-duplicate scripts.

## 1. Channel identity and positioning
Photoreal presenter (senior-benefits network style, 100% face thumbnails); handle @MarcusRetires. Primary sub-niche: senior banking/Social Security/Medicare rules (US). Launched Oct 2026 (VERIFIED dates).

## 2. Database inventory and coverage
- Channel ID `UCW_JmbBR0gsRGIUGRY3WA-Q` · handle @MarcusRetires · https://www.youtube.com/channel/UCW_JmbBR0gsRGIUGRY3WA-Q
- Registered sub-niche: retirement / Social Security / Medicare · subscribers: 7,500 · availability: AVAILABLE nan
- Description: Marcus Retires helps retirees and seniors navigate the confusing world of retirement finances — in plain, simple language.  From Social Security and Medicare to hidden tax rules, 401(k) mistakes, IRA traps, and bills you may no longer need to pay — we break down the topics that can save (or cost) you thousands.  💡 What You'll Learn Here: ✅ Retirement tax rules most people never hear about ✅ Social…
- Videos in DB 29 (long 29, Shorts 0); views 29; transcripts 29 (100%); thumbnail images 29 (100%); FULL metadata 100%; PI-classified long 23
- Dates 2026-10-05 → 2026-11-09; median views 2,098; p90 76,850; max 244,513
- Cadence: 25.9 uploads/month over 1.1 months; median gap 0.5 d; max gap 7 d; weekday mode Monday
- Duration (min): median 18.5; p10 14.3; p90 24.1; first-third median 19.1 vs last-third 17.2
- Spearman(gap-before-upload, PI) = 0.45; Spearman(duration, PI) = -0.02; median PI first third 0.04 vs last third 0.10
- PI classes (long): Underperforming 12, Breakout 6, Successful 3, Average 2; near-duplicate-script flags 7
- Titles whose word-set also appears on another channel: 11 (38%)
- **Never Keep More Than This in the Bank After 65 — Most Seniors Miss These** — [b-oBChjaZo4](https://www.youtube.com/watch?v=b-oBChjaZo4) · 2026-10-22 · 15.03 min · 244,513 views · PI 17.21 (Breakout) · banking_cash/warning_mistake · face=True · thumb text: “THEY/CAN/AKEN/AY/WE/OVER/THIS”
- **6 Places Seniors Should Never Keep Their Cash Before Nov 1** — [5CIZ4R6LiQk](https://www.youtube.com/watch?v=5CIZ4R6LiQk) · 2026-10-09 · 23.62 min · 85,806 views · PI 12.28 (Breakout) · banking_cash/list_countdown · face=True · thumb text: “MOVE/YOUR/CASH/BEFORE/NOV”
- **NEW Bank Rules for Social Security Direct Deposits in 2026 — What Every Retiree Needs to Know** — [MBrPZfSmVo0](https://www.youtube.com/watch?v=MBrPZfSmVo0) · 2026-10-27 · 18.62 min · 142,470 views · PI 10.03 (Breakout) · social_security/news_change_update · face=True · thumb text: “BANKS/FLAGGING/DIRECT/DEPOSITS”
- **The Medicare Decision You Can't Undo — Open Enrollment Ends Dec 7 and Most Seniors Choose Wrong** — [rrQWvS5hwLE](https://www.youtube.com/watch?v=rrQWvS5hwLE) · 2026-10-10 · 17.63 min · 93.00 views · PI 0.01 (Underperforming) · medicare_health_costs/statement_other · face=True · thumb text: “THE/EDICARE/WRONG”
- **7 Things IRS Can’t Take From You — Most Retirees Only Know 1st** — [LPxn5Mq8Sqk](https://www.youtube.com/watch?v=LPxn5Mq8Sqk) · 2026-10-07 · 23.93 min · 242 views · PI 0.02 (Underperforming) · retirement_accounts_tax/list_countdown · face=True · thumb text: “CAN'T/TOUCH/THESE/7-THINGS®/FOR/SENIORS/65+”
- **UK Pensioners: 5 Bills You DON'T Have To Pay After 60 - Exempt By Age** — [KQlnU39MdOQ](https://www.youtube.com/watch?v=KQlnU39MdOQ) · 2026-10-13 · 21.32 min · 303 views · PI 0.02 (Underperforming) · retirement_accounts_tax/warning_mistake · face=True · thumb text: “PENSIONERS/DONT,”

Per-video field status (AVAILABLE / MISSING / UNVERIFIED / NOT APPLICABLE) is in `VIDEO_INVENTORY.csv`. Note: the source DB was capped at ~100 newest uploads per channel for most channels, so this is not the full lifetime library.

## 3. Complete video catalogue
All 29 videos in the database (also `VIDEO_INVENTORY.csv`). PI = views ÷ median of 15 nearest-in-time uploads (same channel & format); blank PI = not classifiable (too new/too few comparables).

| # | date | title | min | views | PI | class | topic | title format | transcript |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-05 | [Stop Paying These 5 Bills After 65 (Nobody Tells You)](https://www.youtube.com/watch?v=t3lEL9Zv7Ks) | 12.5 | 388 | 0.03 | Underperforming | social_security | warning_mistake | Y |
| 2 | 2026-10-06 | [If Your Spouse Dies, These 3 Things Happen to Your Joint Bank Account](https://www.youtube.com/watch?v=wkuU1fN_-Go) | 14.4 | 1,597 | 0.11 | Underperforming | banking_cash | list_countdown | Y |
| 3 | 2026-10-07 | [7 Things IRS Can’t Take From You — Most Retirees Only Know 1st](https://www.youtube.com/watch?v=LPxn5Mq8Sqk) | 23.9 | 242 | 0.02 | Underperforming | retirement_accounts_tax | list_countdown | Y |
| 4 | 2026-10-08 | [Seniors 65+: 5 Bills You're Legally Exempt From — Most Never Stop Paying Them](https://www.youtube.com/watch?v=5ePBe4PL9xY) | 15.3 | 15,162 | 2.17 | Successful | social_security | warning_mistake | Y |
| 5 | 2026-10-09 | [6 Places Seniors Should Never Keep Their Cash Before Nov 1](https://www.youtube.com/watch?v=5CIZ4R6LiQk) | 23.6 | 85,806 | 12.28 | Breakout | banking_cash | list_countdown | Y |
| 6 | 2026-10-10 | [The Medicare Decision You Can't Undo — Open Enrollment Ends Dec 7 and Most Seniors Choose ](https://www.youtube.com/watch?v=rrQWvS5hwLE) | 17.6 | 93 | 0.01 | Underperforming | medicare_health_costs | statement_other | Y |
| 7 | 2026-10-10 | [2027 Social Security COLA: Why Your January Check May Be Smaller Than You Expect!](https://www.youtube.com/watch?v=0_yzbUMKtHM) | 26.5 | 538 | 0.04 | Underperforming | social_security | list_countdown | Y |
| 8 | 2026-10-12 | [Social Security Just Changed 3 Direct Deposit Rules — Do This Before Your Check Disappears](https://www.youtube.com/watch?v=Vk8o9lCtGew) | 19.1 | 19,865 | 2.84 | Successful | social_security | warning_mistake | Y |
| 9 | 2026-10-13 | [UK Pensioners: 5 Bills You DON'T Have To Pay After 60 - Exempt By Age](https://www.youtube.com/watch?v=KQlnU39MdOQ) | 21.3 | 303 | 0.02 | Underperforming | retirement_accounts_tax | warning_mistake | Y |
| 10 | 2026-10-14 | [Every Senior Must Know The Real October Changes Hitting Social Security And Savings Or Los](https://www.youtube.com/watch?v=4ax78GFequQ) | 20.4 | 48,561 | 6.95 | Breakout | social_security | news_change_update | Y |
| 11 | 2026-10-15 | [Born Before 1967? 4 Social Security Changes Hitting Your Birth Year In 2027](https://www.youtube.com/watch?v=9TKIxH6yjgk) | 20.5 | 21,653 | 1.52 | Average | social_security | news_change_update | Y |
| 12 | 2026-10-16 | [Seniors: Move These 7 Assets Before 2027 — The IRS Could Take $45,000](https://www.youtube.com/watch?v=x5G9I1tIvPo) | 29.9 | 38,104 | 5.45 | Breakout | taxes_irs | news_change_update | Y |
| 13 | 2026-10-17 | [If You're Over 60, Aldi Will Give You These 14 Things (If You Ask)](https://www.youtube.com/watch?v=iAM2a3SObjg) | 13.0 | 2,098 | 0.15 | Underperforming | medicare_health_costs | list_countdown | Y |
| 14 | 2026-10-18 | [Seniors: 7 Pieces of Good News for Your Money in January (Most Don't Know)](https://www.youtube.com/watch?v=E_75nb-GHZ0) | 22.1 | 6,990 | 0.49 | Underperforming | social_security | warning_mistake | Y |
| 15 | 2026-10-19 | [Breaking: Social Security Announces 4 Major Changes for 2027](https://www.youtube.com/watch?v=2jWRfKNHmaY) | 19.0 | 70,520 | 4.96 | Successful | social_security | news_change_update | Y |
| 16 | 2026-10-20 | [Never Keep More Than This in One Bank Account After 65 — 7 Rules Most Seniors Miss](https://www.youtube.com/watch?v=dKjz8vkF0hI) | 22.6 | 14,204 | 0.72 | Average | banking_cash | list_countdown | Y |
| 17 | 2026-10-21 | [7 Retirement Assets to Review Before 2027 — Avoid These Costly IRS Mistakes](https://www.youtube.com/watch?v=MXsnofPBQ3E) | 24.5 | 1,985 | 0.10 | Underperforming | retirement_accounts_tax | list_countdown | Y |
| 18 | 2026-10-22 | [Never Keep More Than This in the Bank After 65 — Most Seniors Miss These](https://www.youtube.com/watch?v=b-oBChjaZo4) | 15.0 | 244,513 | 17.21 | Breakout | banking_cash | warning_mistake | Y |
| 19 | 2026-10-23 | [BREAKING: 10 Social Security Changes for 2027 — What Every Retiree Needs to Know!](https://www.youtube.com/watch?v=mK7WKlBjyaM) | 15.8 | 1,477 | 0.07 | Underperforming | social_security | news_change_update | Y |
| 20 | 2026-10-24 | [The 7 Letters Retirees Receive in November That Quietly Change Their 2027 Income (best fit](https://www.youtube.com/watch?v=7-LH8eaUkxw) | 14.6 | 2,000 | 0.10 | Underperforming | retirement_accounts_tax | news_change_update | Y |
| 21 | 2026-10-25 | [Congress Just Passed a Social Security Bill — 3 Retirement Age Changes Explained for Senio](https://www.youtube.com/watch?v=2MuHoggHMGY) | 21.3 | 753 | 0.04 | Underperforming | social_security | news_change_update | Y |
| 22 | 2026-10-26 | [🚨 NEW SSA RULES (Updated October 2026): Seniors Born in the 40s, 50s and 60s Are Affected ](https://www.youtube.com/watch?v=VmpfwwTqhgY) | 17.2 | 74,611 | 5.25 | Breakout | social_security | news_change_update | Y |
| 23 | 2026-10-27 | [NEW Bank Rules for Social Security Direct Deposits in 2026 — What Every Retiree Needs to K](https://www.youtube.com/watch?v=MBrPZfSmVo0) | 18.6 | 142,470 | 10.03 | Breakout | social_security | news_change_update | Y |
| 24 | 2026-10-28 | [5 Simple Ways to Increase Your Social Security Check in 2027 — Most Retirees Miss #5](https://www.youtube.com/watch?v=sgj5OF7cCVg) | 15.6 | 913 |  | NOT_CLASSIFIED | social_security | list_countdown | Y |
| 25 | 2026-11-05 | [7 Things They Can't Take From You After 65 — Not Even the IRS](https://www.youtube.com/watch?v=kDHt7X1cffI) | 15.6 | 387 |  | NOT_CLASSIFIED | taxes_irs | list_countdown | Y |
| 26 | 2026-11-06 | [5 Changes Hiding In Your Medicare Letter (Check Before Dec 7)](https://www.youtube.com/watch?v=XWJfxTwg7x0) | 13.7 | 126 |  | NOT_CLASSIFIED | medicare_health_costs | list_countdown | Y |
| 27 | 2026-11-07 | [Social Security Just Changed for Anyone Born Before 1967 One Group Gets Nothing in January](https://www.youtube.com/watch?v=6ZGsRygrYvo) | 16.1 | 2,843 |  | NOT_CLASSIFIED | social_security | news_change_update | Y |
| 28 | 2026-11-08 | [Social Security Just Changed for Anyone Born Before 1967](https://www.youtube.com/watch?v=nu0VEIbuu-E) | 17.8 | 6,276 |  | NOT_CLASSIFIED | social_security | news_change_update | Y |
| 29 | 2026-11-09 | [Born Before 1967? Social Security Changes for 2027 — 3 Groups Explained](https://www.youtube.com/watch?v=YC-V5cUSM-k) | 18.5 | 113 |  | NOT_CLASSIFIED | social_security | news_change_update | Y |

## 4. Topic and sub-niche map
| topic | n | long | median views | median PI | succ/breakout | under | first | last |
|---|---|---|---|---|---|---|---|---|
| social_security | 16 | 16 | 6,633 | 1.85 | 6 | 5 | 2026-10-05 | 2026-11-09 |
| banking_cash | 4 | 4 | 50,005 | 6.50 | 2 | 1 | 2026-10-06 | 2026-10-22 |
| retirement_accounts_tax | 4 | 4 | 1,144 | 0.06 | 0 | 4 | 2026-10-07 | 2026-10-24 |
| medicare_health_costs | 3 | 3 | 126 | 0.08 | 0 | 2 | 2026-10-10 | 2026-11-06 |
| taxes_irs | 2 | 2 | 19,246 | 5.45 | 1 | 0 | 2026-10-16 | 2026-11-05 |

Title-format mix (INFERRED tags): news_change_update: n=12.0, medPI=4.96 · list_countdown: n=10.0, medPI=0.11 · warning_mistake: n=6.0, medPI=1.33 · statement_other: n=1.0, medPI=0.01

Banking (median PI 6.50) and taxes (5.45) win; Social Security (1.85) mixed; retirement accounts (0.06, 4/4 flops) and Medicare (0.08) fail. News-change titles median 4.96 vs lists 0.11.

## 5. Winning video analysis
1. **Never Keep More Than This in the Bank After 65 — Most Seniors Miss These** (b-oBChjaZo4, 245k, PI 17.2): matched pair "Two retirees, both 68… One… opened his banking app… account frozen" — bank-amount concept (Nick 2025, Robin Jul, Walter Oct).
2. **6 Places Seniors Should Never Keep Their Cash Before Nov 1** (5CIZ4R6LiQk, 86k, PI 12.3): two dates "11 days apart" deadline.
3. **NEW Bank Rules for Social Security Direct Deposits in 2026** (MBrPZfSmVo0, 142k, PI 10): "On June 19th of this year, a rule took effect…" — direct-deposit concept (Lana Jul 31, Nia Aug 5, Walter Oct 12, Marcus Oct 27) — still winning on its fourth/fifth appearance.

### Evidence: top-PI long-form videos
- **Never Keep More Than This in the Bank After 65 — Most Seniors Miss These** — [b-oBChjaZo4](https://www.youtube.com/watch?v=b-oBChjaZo4) · 2026-10-22 · 15.03 min · 244,513 views · PI 17.21 (Breakout) · banking_cash/warning_mistake · face=True · thumb text: “THEY/CAN/AKEN/AY/WE/OVER/THIS”
  - 0-30s: “Two retirees, both 68, both careful with money, both kept everything in one bank. One of them slept fine every night. The other opened his banking app one morning and found his account frozen with nothing he could touch. He had broken no law. He had made no mistake. The difference between them was one number that nobody ever told him to watch. There is a small set of dollar limits sitting in the background”
  - end: “because I'm breaking down more of these rules every week and I'll cover each change as it lands. And type your age in the comments. I read everyone and they decide what I cover next. Until then, keep an eye on your money…” · sources: Social Security Administration (SSA); IRS; CBO / Treasury; VA · desc links: consumerfinance.gov fdic.gov fincen.gov irs.gov marcusretires.com ssa.gov
- **6 Places Seniors Should Never Keep Their Cash Before Nov 1** — [5CIZ4R6LiQk](https://www.youtube.com/watch?v=5CIZ4R6LiQk) · 2026-10-09 · 23.62 min · 85,806 views · PI 12.28 (Breakout) · banking_cash/list_countdown · face=True · thumb text: “MOVE/YOUR/CASH/BEFORE/NOV”
  - 0-30s: “Your money is sitting somewhere right now and whatever that place happens to be paying you, it did not ask your permission to pay you that rate and it will not ask your permission to pay you less. There are two dates coming just 11 days apart and between them almost every interest rate in this country gets reset. The first is the 27th and 28th of October when the Federal Reserve meets and decides”
  - end: “six places right now. And subscribe with the bell turned on because next week I am breaking down exactly what the Fed's decision means for your Social Security check and your Medicare premiums. Until then, keep an eye on…” · sources: Federal Reserve; CBO / Treasury
- **NEW Bank Rules for Social Security Direct Deposits in 2026 — What Every Retiree Needs to Know** — [MBrPZfSmVo0](https://www.youtube.com/watch?v=MBrPZfSmVo0) · 2026-10-27 · 18.62 min · 142,470 views · PI 10.03 (Breakout) · social_security/news_change_update · face=True · thumb text: “BANKS/FLAGGING/DIRECT/DEPOSITS”
  - 0-30s: “On June 19th of this year, a rule took effect that changed how every bank and credit union in America treats the money that comes in. It didn't come from Congress. The president didn't sign it. And it now applies to the account where your social security lands every month. Most people have never heard of it. And almost nobody has connected it to three other things that happened to the federal benefit system this”
  - end: “turned on because when the 2027 Part B premium is announced, I'll be here with the exact subtraction and what it means for your January deposit. And type your age in the comments. I read everyone and they decide what I c…” · sources: Social Security Administration (SSA); CMS / Medicare.gov; Congress / legislation; CBO / Treasury; Trustees report; VA · desc links: consumerfinance.gov marcusretires.com medicare.gov nacha.org ssa.gov

## 6. Underperforming video analysis
- **7 Things IRS Can't Take From You — Most Retirees Only Know 1st** (LPxn5Mq8Sqk, 242 views): typo ("Only Know 1st"), concept already won on Lana/Nia/Mark Calloway (Jul–Sep).
- **The Medicare Decision You Can't Undo — Open Enrollment Ends Dec 7** (rrQWvS5hwLE, 93 views): crowded seasonal Medicare topic.
- **UK Pensioners: 5 Bills You DON'T Have To Pay After 60** (KQlnU39MdOQ, 303): title targets the UK, script says "the average American retiree" (VERIFIED mismatch) — broken localisation.

### Evidence: bottom-PI long-form videos
- **The Medicare Decision You Can't Undo — Open Enrollment Ends Dec 7 and Most Seniors Choose Wrong** — [rrQWvS5hwLE](https://www.youtube.com/watch?v=rrQWvS5hwLE) · 2026-10-10 · 17.63 min · 93.00 views · PI 0.01 (Underperforming) · medicare_health_costs/statement_other · face=True · thumb text: “THE/EDICARE/WRONG”
  - 0-30s: “There is a window that opened on October 15th and it closes on December 7th. And whatever you decide inside that window or whatever you decide by doing nothing at all locks you into a health coverage decision for the entire next year. You cannot undo it in January. You cannot fix it in March. You cannot call Medicare in June and say you made a mistake and you want to switch because by then”
  - end: “the bell icon so you get notified every single time I post a new video. And share this video right now with every person you know who is on Medicare because this deadline does not wait for anyone and you might be the onl…”
- **7 Things IRS Can’t Take From You — Most Retirees Only Know 1st** — [LPxn5Mq8Sqk](https://www.youtube.com/watch?v=LPxn5Mq8Sqk) · 2026-10-07 · 23.93 min · 242 views · PI 0.02 (Underperforming) · retirement_accounts_tax/list_countdown · face=True · thumb text: “CAN'T/TOUCH/THESE/7-THINGS®/FOR/SENIORS/65+”
  - 0-30s: “There's a list of seven things sitting in federal and state law right now that no creditor, no collection agency, no nursing home, and not even a hospital's collections department can legally take from you once you're past 65. Most families never find out this list exists until they've already panicked and made an expensive mistake trying to protect something the law was already protecting for them the whole time. And I'll tel…”
  - end: “because someone you love is quietly worrying about one of these seven things right now. And subscribe with the bell turned on because next week I'm covering the deadline change that affects every retireese's Medicare enr…” · sources: Social Security Administration (SSA); IRS; Congress / legislation; Company filings / earnings; VA
- **UK Pensioners: 5 Bills You DON'T Have To Pay After 60 - Exempt By Age** — [KQlnU39MdOQ](https://www.youtube.com/watch?v=KQlnU39MdOQ) · 2026-10-13 · 21.32 min · 303 views · PI 0.02 (Underperforming) · retirement_accounts_tax/warning_mistake · face=True · thumb text: “PENSIONERS/DONT,”
  - 0-30s: “There are at least five bills the average American retiree is still paying year after year that the law says you may not have to pay at all after a certain birthday. Five of them. And most people keep paying them for years. Not because they owe them, but because no one ever told them a birthday had canceled them. And before I go a single sentence further, I have to clear up the misunderstanding”
  - end: “for no reason on earth. And subscribe with the bell turned on because next week I am covering the bill that starts at 73 instead of ending, the required distribution rule, the penalty for missing it, and the one move tha…” · sources: Social Security Administration (SSA); IRS; DWP / HMRC / gov.uk

## 7. Successful vs failed comparison
Same presenter/style in both halves. Banking-protection concepts survived repeated reuse; the IRS-protection concept and Medicare did not. Sloppiness (typos, mislocalisation) concentrated in flops.

| feature | upper half | lower half |
|---|---|---|
| t_number | 91% | 100% |
| t_dollar | 9% | 0% |
| t_question | 9% | 0% |
| t_you | 27% | 64% |
| t_fear_risk | 45% | 18% |
| t_urgency | 64% | 45% |
| t_secret_truth | 0% | 18% |
| t_named_entity | 55% | 55% |
| t_caps_word | 27% | 18% |
| t_year | 45% | 45% |
| h_first_sentence_q | 0% | 9% |
| h_you_in_30s | 82% | 91% |
| h_number_30s | 82% | 82% |
| h_dollar_30s | 27% | 9% |
| h_stakes_30s | 9% | 27% |
| h_contrarian_30s | 45% | 73% |
| h_open_loop_30s | 27% | 36% |
| h_promise_30s | 45% | 27% |
| h_story_open | 18% | 0% |
| h_greeting_open | 0% | 0% |
| h_first_person_30s | 9% | 27% |
| s_cta_end | 91% | 82% |
| tx_words (median) | 3,940 | 3,577 |
| s_num_density (median) | 1.74 | 1.57 |
| s_q_density (median) | 0.05 | 0.02 |
| s_but_density (median) | 0.30 | 0.24 |
| s_example_density (median) | 0.03 | 0.07 |
| s_data_density (median) | 0.90 | 0.65 |
| s_loop_density (median) | 0.00 | 0.00 |
| s_you_density (median) | 4.23 | 3.78 |
| s_wpm (median) | 194 | 194 |
| h_title_overlap_150 (median) | 0.45 | 0.50 |
| i_promise_pos (median) | 130 | 149 |
| t_len (median) | 77.00 | 75.00 |
| th_text_words (median) | 5.00 | 4.00 |
| th_colorfulness (median) | 84.98 | 85.74 |
| thumbnail has face | 100% | 100% |



## 8. Topic discovery and research sources
Network concepts; rule references (Jun-19 bank rule claim UNVERIFIED). 38% cross-channel title overlap.

Institutions named in transcripts/descriptions (rule-based; 'Academic / research study' matches generic words like “study/research” and is low-confidence): Social Security Administration (SSA) 23, IRS 14, Company filings / earnings 14, Congress / legislation 12, CMS / Medicare.gov 12, CBO / Treasury 10, Trustees report 9, VA 5, BLS / CPI data 5, Academic / research study 3
Description link domains: marcusretires.com 15, ssa.gov 14, medicare.gov 10, consumerfinance.gov 5, irs.gov 5, fdic.gov 3, congress.gov 2, finra.org 1, fincen.gov 1, nacha.org 1
Per-video source map: `SOURCE_MAP.csv`.

## 9. Trend behaviour
Calendar dates ("Before Nov 1") help.

## 10. Thumbnail strategy
Montage not inspected; 100% presenter.

## 11. Title strategy
Network formula ("Never Keep More Than This…", "NEW Bank Rules…", "Most Seniors Miss These").

## 12. Hook and introduction strategy
Matched retirees; dated rule changes.

## 13. Script and storytelling strategy
14-24 min; 7 near-duplicate flags (repetitive-content risk).

## 14. Audience engagement model
Fear of frozen accounts.

## 15. Upload and publishing strategy
~26/month in the first five weeks.

## 16. PDF principle evaluation
Judge: *YouTube Automation – Complete Master Playbook* (556 pp., sha256 c630c24b…576d). Supporting authority: global-youtube-knowledge (DS-000011/18/31) — see `00_PROJECT_OVERVIEW/GLOBAL_KNOWLEDGE_MAP.md`. Automated evidence uses text proxies; verdict = analyst override where noted, else rule-based draft.

| ID | PDF principle (location) | What the PDF says | Evidence from channel (automated, incl. winners vs rest where testable) | Verdict | Analyst note |
|---|---|---|---|---|---|
| P01 | Module 2.1 Outlier Concept, pp.6-9; Method 1 Outlier Transplant, pp.34-35 | Find videos that beat the channel norm (5-10x strong, 10x+ clear outlier) and treat their TOPIC as proven demand; build the calendar from validated outliers. | 6 long-form ≥5x and 3 ≥10x own baseline; after 7 winners, next-10 uploads repeat the winner's topic 26% vs base rate 35% | **NOT FOLLOWED** |  |
| P02 | Module 2.2 Niche vs Format vs Template, p.11 | A niche is an audience + persistent interest + monetisation path, not a topic; every video should feel like it belongs to the same channel. | top-2 topics (social_security, banking_cash) = 69% of uploads; explicit audience marker in 69% of titles | **FOLLOWED** |  |
| P03 | Module 2.2, pp.12-13 | One niche can carry many formats; add formats to grow without changing niche. | 3 title-format types each ≥10% of uploads (news_change_update 41%, list_countdown 34%, warning_mistake 21%, statement_other 3%) | **FOLLOWED** |  |
| P04 | Module 2.2 p.13; Masterclass Ch.23 p.351; Web research §7 p.555 | Avoid repetitive/mass-produced uploads; rotating templates alone is not enough — each video needs distinct substance (inauthentic-content policy). | near-duplicate-script flag on 24% of videos; repeated title word-sets within channel 0% | **CONTRADICTED BY EVIDENCE** | 7 near-duplicate scripts in 29 videos. |
| P05 | Module 2.3 Format Arbitrage pp.18-20; Module 2.4 Niche Bending pp.24-26 | Win by transplanting a proven format into a niche that lacks it, or by combining two overlapping niches. | requires historical competitor-format landscape at launch; analyst note in report if a bend is visible | **NOT TESTABLE** |  |
| P06 | Module 2.7 Competitor Research pp.28-30; Method 1 p.34 | Study competitors’ top videos, titles, thumbnails, cadence and comments; cover proven topics with original content. | 38% of titles share a word-set with another channel; this channel published first on 0 of 11 | **PARTIALLY FOLLOWED** | network concepts transplanted; some still win (banking), some saturated (IRS list). |
| P07 | Method 2 Title Template Injection pp.39-40; 100 Title Formats pp.52-64 | Inject niche topics into proven title psychology families (mystery, downfall, contradiction, revelation, practical, conflict…), but the content must deliver. | 45% of titles match a 100-format family; median PI with 0.07 (n=9) vs without 1.12 (n=14) | **PARTIALLY FOLLOWED** |  |
| P08 | 100 Title Formats p.53 (five-part engine), p.66 scorecard | A strong title names a recognisable subject, a situation, a trigger, a tension and a concrete promise/stakes. | 100% of titles carry a number/$/named entity | **FOLLOWED** |  |
| P09 | 100 Title Formats p.68 (12 mistakes); Masterclass Ch.19 p.345 | Avoid generic subjects, two promises, vague “this/they” openers, ALL CAPS overuse, overstated certainty. | titles with ≥3 ALL-CAPS words 3%; vague 'this/they' opener 0%; double-question 0% | **NOT FOLLOWED** | typos and mislocalised titles. |
| P10 | 100 Title Formats p.66 (title+thumbnail one promise), p.68 #11 | Thumbnail should add a complementary clue, not repeat the title. | OCR thumbnail text found on 97%; median share of thumbnail words repeated from title 0.45 | **PARTIALLY FOLLOWED** |  |
| P11 | Module 2.7 Thumbnail Teardown p.28 (supporting: DS-000011 Packaging SOP) | Study colour, text amount, faces/expressions, focal object, contrast and template consistency; one clear idea. | thumbnail images 100%; median OCR words 4.0 (OCR undercounts stylised text); face/character detected 100% (cartoon faces often missed) | **NOT TESTABLE** | montage not inspected. |
| P12 | Engagement Playbook §1 p.265; Masterclass Zone 1 p.320 | The first ~3-5 seconds must create curiosity: question, shock stat, contradiction, mystery, story drop, direct challenge. | opening ~75 words contain question/number/contradiction/story/you-hook in 90%; greeting/channel-intro opening 0% | **FOLLOWED** |  |
| P13 | Masterclass Zone 2 p.320; Engagement §18 p.283 | Within ~5-15 s answer “why should I care?” — connect to the viewer’s money, safety or identity. | explicit stakes/why-it-matters language early in 21%; median PI with 0.07 vs without 1.12 | **NOT FOLLOWED** |  |
| P14 | Masterclass Zone 3 p.320; Ch.23 p.350 | Open at least one curiosity loop before ~30 s and keep it open. | explicit open-loop/promise phrase in first ~150 words of 38% | **PARTIALLY FOLLOWED** |  |
| P15 | Engagement §2 & §7 pp.267, 272 | Use bridging teases / micro-cliffhangers at segment transitions to prevent drop-off. | bridge/cliffhanger phrases per 100 words (median) 0.000 | **NOT FOLLOWED** |  |
| P16 | Engagement §8 p.273 | Precise numbers, dates, named sources and expert quotes signal research and keep sceptical viewers. | data/citation terms per 100 words 0.96; videos naming an institution/source 90% | **PARTIALLY FOLLOWED** |  |
| P17 | Engagement §6 p.271 | Second-person address makes the viewer a participant (“if you own…”, “imagine you…”). | 'you/your' per 100 words (median) 4.45 | **FOLLOWED** |  |
| P18 | Engagement §15-16 pp.280-281; Deployment p.284 | Close loops, then future-pace to a next video; strongest CTA right after a payoff, not only at the end. | next-video tease in final ~60 words 76%; any CTA in final 10% 90% | **FOLLOWED** |  |
| P19 | Module 2.3 p.19 (8+ min sweet spot); Web research §8 p.555 | Course: formats should fill 8+ minutes; appendix: 8 min is a mid-roll eligibility rule, length should follow the story. | median long-form length 18.5 min; Spearman(duration, PI) -0.02 — 8+ min is an ad-eligibility rule, not a success rule (PDF p555) | **FOLLOWED** |  |
| P20 | Module 2.7 Posting cadence p.29 | Check upload frequency, consistency, dead periods and growth inflection points. | median gap 0.5 d, gap CV 1.80, longest pause 7 d | **PARTIALLY FOLLOWED** |  |
| P21 | Topic Selection Masterclass intro p.33 | “A bad video on the right topic will outperform a great video on the wrong topic” — topic selection is the main lever. | spread of median PI across topics 107.13x (best banking_cash) vs across title formats 44.16x (best news_change_update) | **FOLLOWED** |  |
| P22 | Method 2 warning p.40; 100 Formats p.68 #12; Masterclass Ch.19 p.345 | Title gets the click, content keeps the viewer: the opening must confirm and the video must deliver the title’s promise. | median share of title keywords that appear in the first ~150 spoken words 0.50 | **FOLLOWED** |  |

## 17. Strengths and weaknesses
Fast launch on proven banking concepts. Weaknesses: duplicates, saturated copies, sloppy titles.

## 18. Replicable working model
Network transplant — not recommended as a model beyond "banking-protection concepts can survive reuse".

## 19. What to copy
Matched-pair bank-freeze hooks; real deadlines.

## 20. What not to copy
Re-running saturated concepts; mislocalised titles; duplicate scripts.

## 21. Missing evidence and limitations
Only 5 weeks; montage not inspected.

- Not available from this dataset for any channel: CTR, impressions, retention curves, traffic sources, subscriber growth history, comments text. Hook timings are word-position estimates (untimed transcripts).

## 22. Final channel diagnosis
1) New channel living off the network's concepts; banking ones still work, others are saturated. 2) Advantage: proven concepts. 3) Model: network transplant. 4) Topic: bank/SS rules. 5) Packaging: network presenter. 6) Script: duplicated passages. 7) Interest: frozen-account fear. 8) Failures: saturation, sloppiness. 9) Learn: some concepts saturate, some don't. 10) Don't copy: duplicates. 11) Repeatable: short-term. 12) Reputation: none. 13) Lesson: **a copied concept only works while the audience hasn't seen it many times.**
"If I wanted a channel like this, I would not copy it; I would take only the lesson that banking-protection topics with matched retirees and real deadlines still have demand, and write original scripts."
