# Housing — Channel Forensic Report

Channel #051 of 69 · investigation tier 2 (data-availability order, not a quality rank) · research date 2026-11-12 · source DB `finance_economics_complete.db` sha256 fa6fd1b2…d20 (branch data/finance-economics-complete-2026-11-11 @933f236e).

Evidence labels used: **VERIFIED** (directly in DB / public page), **INFERRED** (derived from DB text by rule or analyst reading), **HYPOTHESIS** (plausible, untested), **UNKNOWN**. Public view counts do not reveal CTR, retention or traffic sources; none of those are claimed.

**Key conclusion:** Senior-benefits network channel launched Sep 2026 (handle @housingusa, 3.7k subs) with extreme bimodality (median 668 views; three videos 97k-185k, PI 167-566) and the **highest near-duplicate rate in the dataset (13 of 24 videos)**; its "5 Types of Debt Relief Seniors Should Know After 65" opens with the *same sentences* as Nia Prescott's 1.13M "bills after 65" video ("There are five bills that the government itself says you may no longer have to pay once you turn 65. Not a smaller amount… The whole bill gone…") and drew 43 views.

## 1. Channel identity and positioning
Photoreal presenter (network style; 100% faces); name "Housing" mismatches the senior-tax content (VERIFIED). Sub-niche: senior banking/IRS/Social Security rules. Audience: US 65+.

## 2. Database inventory and coverage
- Channel ID `UC3Tzh0Wu1C9s3AI2Oqc8kIA` · handle @housingusa · https://www.youtube.com/channel/UC3Tzh0Wu1C9s3AI2Oqc8kIA
- Registered sub-niche: senior taxes / Social Security / IRS news · subscribers: 3,690 · availability: AVAILABLE nan
- Description: Welcome to HOUSING with Alex Morgan!  We share educational updates on U.S. taxes, IRS news, Social Security, retirement, Medicare, and government programs affecting Americans.  ⚠️ Disclaimer: This channel may use AI-generated presenters. We strive to provide accurate, fact-checked information for educational purposes only. We are not affiliated with the IRS, SSA, or any U.S. government agency. Ple…
- Videos in DB 24 (long 24, Shorts 0); views 24; transcripts 24 (100%); thumbnail images 24 (100%); FULL metadata 100%; PI-classified long 22
- Dates 2026-09-14 → 2026-11-09; median views 668; p90 114,066; max 185,127
- Cadence: 13.0 uploads/month over 1.8 months; median gap 1.0 d; max gap 20 d; weekday mode Monday
- Duration (min): median 22.5; p10 14.4; p90 31.1; first-third median 18.4 vs last-third 23.1
- Spearman(gap-before-upload, PI) = -0.15; Spearman(duration, PI) = 0.58; median PI first third 0.37 vs last third 8.43
- PI classes (long): Underperforming 10, Breakout 8, Successful 2, Average 2; near-duplicate-script flags 13
- Titles whose word-set also appears on another channel: 2 (8%)
- **3 Banking Changes to Watch in 2026 That Could Affect Your Checking Account** — [oPZjqx_6d1g](https://www.youtube.com/watch?v=oPZjqx_6d1g) · 2026-09-17 · 28.17 min · 126,232 views · PI 566.06 (Breakout) · banking_cash/list_countdown · face=True · thumb text: “CHECKING./EW/_R/ULE/($8/IRS”
- **7 Types of Income the IRS May Not Tax After 65 — Most Seniors Miss These** — [hNuWYk9YQsc](https://www.youtube.com/watch?v=hNuWYk9YQsc) · 2026-09-28 · 24.02 min · 96,911 views · PI 289.29 (Breakout) · taxes_irs/list_countdown · face=True · thumb text: “ie/THI</AFTER/AGE/65”
- **Never Keep More Than This in the Bank After 65 — Most Seniors Miss These** — [NXhhbwvx3Fg](https://www.youtube.com/watch?v=NXhhbwvx3Fg) · 2026-10-10 · 23.95 min · 185,127 views · PI 166.63 (Breakout) · banking_cash/warning_mistake · face=True · thumb text: “TAKE/YOUR/LES)/OVER/THIS/AMOUNT”
- **Check Your Mailbox. 600,000 Seniors Are Losing Their Medicare Plan** — [ZEsdKt4Jdws](https://www.youtube.com/watch?v=ZEsdKt4Jdws) · 2026-10-04 · 15.48 min · 335 views · PI 0.08 (Underperforming) · medicare_health_costs/how_to · face=True · thumb text: “SECURITY/AR”
- **Seniors: New Income Eligibility Rules in October 2026 — What to Know if You Were Denied** — [hbtiNALywK8](https://www.youtube.com/watch?v=hbtiNALywK8) · 2026-09-22 · 19.27 min · 35.00 views · PI 0.10 (Underperforming) · budgeting_debt/news_change_update · face=True · thumb text: “SENIORS/penet”
- **5 Types of Debt Relief Seniors Should Know About After Age 65** — [NyCxO-ZkD3k](https://www.youtube.com/watch?v=NyCxO-ZkD3k) · 2026-09-26 · 14.00 min · 43.00 views · PI 0.13 (Underperforming) · budgeting_debt/list_countdown · face=True · thumb text: “SENIORS/CHECK/YOUR/BILLS/Outstanding/KNOW/HAT/YOu”

Per-video field status (AVAILABLE / MISSING / UNVERIFIED / NOT APPLICABLE) is in `VIDEO_INVENTORY.csv`. Note: the source DB was capped at ~100 newest uploads per channel for most channels, so this is not the full lifetime library.

## 3. Complete video catalogue
All 24 videos in the database (also `VIDEO_INVENTORY.csv`). PI = views ÷ median of 15 nearest-in-time uploads (same channel & format); blank PI = not classifiable (too new/too few comparables).

| # | date | title | min | views | PI | class | topic | title format | transcript |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-14 | [Retirees in These 3 States: Tax Breaks You Could Be Missing in 2026](https://www.youtube.com/watch?v=ptog3oAPt9U) | 16.0 | 124 | 0.37 | Underperforming | retirement_accounts_tax | list_countdown | Y |
| 2 | 2026-09-15 | [4 Important Legal Documents Homeowners Should Review Before 2027](https://www.youtube.com/watch?v=Y2GId9tvJyU) | 32.4 | 46 | 0.14 | Underperforming | housing_real_estate | list_countdown | Y |
| 3 | 2026-09-16 | [Federal Reserve Update: What It Could Mean for Your Money and Mortgage Rates](https://www.youtube.com/watch?v=MyMgN02HMM4) | 15.5 | 618 | 2.77 | Successful | housing_real_estate | news_change_update | Y |
| 4 | 2026-09-17 | [3 Banking Changes to Watch in 2026 That Could Affect Your Checking Account](https://www.youtube.com/watch?v=oPZjqx_6d1g) | 28.2 | 126,232 | 566.06 | Breakout | banking_cash | list_countdown | Y |
| 5 | 2026-09-18 | [Seniors: Where to Keep Your Savings Safe This October 2026](https://www.youtube.com/watch?v=Oy2j-pyP0pQ) | 37.9 | 223 | 0.67 | Average | budgeting_debt | news_change_update | Y |
| 6 | 2026-09-19 | [7 Assets Seniors May Be Able to Protect From Creditors and the IRS](https://www.youtube.com/watch?v=Ut1kEnsrbO4) | 17.5 | 45 | 0.13 | Underperforming | taxes_irs | list_countdown | Y |
| 7 | 2026-09-22 | [Seniors: New Income Eligibility Rules in October 2026 — What to Know if You Were Denied](https://www.youtube.com/watch?v=hbtiNALywK8) | 19.3 | 35 | 0.10 | Underperforming | budgeting_debt | news_change_update | Y |
| 8 | 2026-09-23 | [New US Laws Taking Effect in Fall 2026: What They Could Mean for Your Money](https://www.youtube.com/watch?v=0AQU5LHPNnM) | 15.9 | 105 | 0.31 | Underperforming | social_security | news_change_update | Y |
| 9 | 2026-09-26 | [5 Types of Debt Relief Seniors Should Know About After Age 65](https://www.youtube.com/watch?v=NyCxO-ZkD3k) | 14.0 | 43 | 0.13 | Underperforming | budgeting_debt | list_countdown | Y |
| 10 | 2026-09-28 | [7 Types of Income the IRS May Not Tax After 65 — Most Seniors Miss These](https://www.youtube.com/watch?v=hNuWYk9YQsc) | 24.0 | 96,911 | 289.29 | Breakout | taxes_irs | list_countdown | Y |
| 11 | 2026-09-30 | [Seniors: Important Benefit and Tax Updates to Check Before October 2026](https://www.youtube.com/watch?v=xAGP0UqlDwM) | 13.3 | 208 | 0.29 | Underperforming | taxes_irs | news_change_update | Y |
| 12 | 2026-10-02 | [Estate Planning for 2027: 5 Assets Families Should Review Before Passing Them On](https://www.youtube.com/watch?v=fL78IA2FV9o) | 19.7 | 719 | 0.67 | Average | retirement_accounts_tax | news_change_update | Y |
| 13 | 2026-10-04 | [Check Your Mailbox. 600,000 Seniors Are Losing Their Medicare Plan](https://www.youtube.com/watch?v=ZEsdKt4Jdws) | 15.5 | 335 | 0.08 | Underperforming | medicare_health_costs | how_to | Y |
| 14 | 2026-10-06 | [THE IRS JUST SENT MILLIONS A LETTER — Why Most Seniors May Get NOTHING](https://www.youtube.com/watch?v=e403nRaArVM) | 25.5 | 13,698 | 12.33 | Breakout | taxes_irs | news_change_update | Y |
| 15 | 2026-10-08 | [The IRS Treats Age 63 DIFFERENTLY — Most Retirees Discover This Too Late!](https://www.youtube.com/watch?v=RSuR7GF09qo) | 10.4 | 1,077 | 0.27 | Underperforming | retirement_accounts_tax | statement_other | Y |
| 16 | 2026-10-10 | [Never Keep More Than This in the Bank After 65 — Most Seniors Miss These](https://www.youtube.com/watch?v=NXhhbwvx3Fg) | 23.9 | 185,127 | 166.63 | Breakout | banking_cash | warning_mistake | Y |
| 17 | 2026-10-12 | [3 New Rules Quietly Taking Money From Your Check Starting October — Most Seniors Miss Thes](https://www.youtube.com/watch?v=1Sarh9YrP6Y) | 33.6 | 9,877 | 8.89 | Breakout | social_security | list_countdown | Y |
| 18 | 2026-10-14 | [Every Senior Must Open This Before October 30 Or Risk Paying More in 2027](https://www.youtube.com/watch?v=6LmGIF6GssQ) | 23.4 | 3,972 | 3.58 | Successful | medicare_health_costs | news_change_update | Y |
| 19 | 2026-10-15 | [Never Keep More Than This in Cash at Home After 65 — Most Seniors Miss These](https://www.youtube.com/watch?v=GKi1uaic9CY) | 22.6 | 1,111 | 0.28 | Underperforming | banking_cash | warning_mistake | Y |
| 20 | 2026-10-16 | [7 Things the IRS Lets You Do After 70½ — Most Seniors Miss These](https://www.youtube.com/watch?v=7L2oaG3pgig) | 26.7 | 9,361 | 8.43 | Breakout | taxes_irs | list_countdown | Y |
| 21 | 2026-10-18 | [Millions of Seniors Could Lose 22% of Their Social Security Check — Most Seniors Miss Thes](https://www.youtube.com/watch?v=WZ2Rec5ldJ8) | 26.4 | 6,033 | 5.43 | Breakout | social_security | statement_other | Y |
| 22 | 2026-10-18 | [Seniors: Don’t Miss This October 30 Deadline — Most Seniors Miss These](https://www.youtube.com/watch?v=tamw1y1Yd24) | 22.7 | 121,418 | 109.29 | Breakout | housing_real_estate | news_change_update | Y |
| 23 | 2026-11-07 | [🔴 THE FED JUST CHANGED EVERYTHING —  Most Seniors Miss These](https://www.youtube.com/watch?v=MuVOm0TJCc0) | 22.3 | 241 |  | NOT_CLASSIFIED | macro_economy | news_change_update | Y |
| 24 | 2026-11-09 | [IRS Releases 2027 Tax Brackets + Capital Gains Update — Most Seniors Miss These](https://www.youtube.com/watch?v=K7ZeSTydf5U) | 15.3 | 29 |  | NOT_CLASSIFIED | taxes_irs | news_change_update | Y |

## 4. Topic and sub-niche map
| topic | n | long | median views | median PI | succ/breakout | under | first | last |
|---|---|---|---|---|---|---|---|---|
| taxes_irs | 6 | 6 | 4,784 | 8.43 | 3 | 2 | 2026-09-19 | 2026-11-09 |
| banking_cash | 3 | 3 | 126,232 | 167 | 2 | 1 | 2026-09-17 | 2026-10-15 |
| budgeting_debt | 3 | 3 | 43.00 | 0.13 | 0 | 2 | 2026-09-18 | 2026-09-26 |
| housing_real_estate | 3 | 3 | 618 | 2.77 | 2 | 1 | 2026-09-15 | 2026-10-18 |
| retirement_accounts_tax | 3 | 3 | 719 | 0.37 | 0 | 2 | 2026-09-14 | 2026-10-08 |
| social_security | 3 | 3 | 6,033 | 5.43 | 2 | 1 | 2026-09-23 | 2026-10-18 |
| medicare_health_costs | 2 | 2 | 2,154 | 1.83 | 1 | 1 | 2026-10-04 | 2026-10-14 |
| macro_economy | 1 | 1 | 241 | n/a | 0 | 0 | 2026-11-07 | 2026-11-07 |

Title-format mix (INFERRED tags): news_change_update: n=11.0, medPI=0.67 · list_countdown: n=8.0, medPI=4.40 · statement_other: n=2.0, medPI=2.85 · warning_mistake: n=2.0, medPI=83.46 · how_to: n=1.0, medPI=0.08

Banking (median PI 167, n=3), taxes (8.4), Social Security (5.4) win; budgeting/debt relief (0.13), retirement (0.37) fail.

## 5. Winning video analysis
1. **3 Banking Changes to Watch in 2026 That Could Affect Your Checking Account** (oPZjqx_6d1g, 126k, PI 566): "Your bank made three changes… and never called you… a notice inside an envelope that looked like a credit card offer".
2. **7 Types of Income the IRS May Not Tax After 65 — Most Seniors Miss These** (hNuWYk9YQsc, 97k, PI 289, 28 Sep): its hook is near-verbatim Mark Calloway's (14 Sep) — "seven kinds of income… legally not allowed to touch… shield as much as $500,000… in a single afternoon" (VERIFIED identical phrasing). The concept still won here (and flopped on Marcus Retires, 7 Oct).
3. **Never Keep More Than This in the Bank After 65** (NXhhbwvx3Fg, 185k, PI 167): Social Security garnishment protection ("about two months of your social security… protected" — real Treasury rule on 2-month look-back, VERIFIED concept).

### Evidence: top-PI long-form videos
- **3 Banking Changes to Watch in 2026 That Could Affect Your Checking Account** — [oPZjqx_6d1g](https://www.youtube.com/watch?v=oPZjqx_6d1g) · 2026-09-17 · 28.17 min · 126,232 views · PI 566.06 (Breakout) · banking_cash/list_countdown · face=True · thumb text: “CHECKING./EW/_R/ULE/($8/IRS”
  - 0-30s: “Your bank made three changes to your checking account and never called you. They were not required to call you. They sent a notice inside an envelope that looked like a credit card offer, the kind most people throw away without opening and that was considered legally sufficient. So, the changes went into effect. The fees started appearing. The monitoring started running. The holds became possible. And millions of account holde…”
  - end: “the alerts. Organize the documents. Verify the people and designations connected to your accounts. Then keep checking periodically. Because the most expensive banking mistake is often not making one bad transaction, it i…” · sources: Social Security Administration (SSA); IRS; Congress / legislation
- **7 Types of Income the IRS May Not Tax After 65 — Most Seniors Miss These** — [hNuWYk9YQsc](https://www.youtube.com/watch?v=hNuWYk9YQsc) · 2026-09-28 · 24.02 min · 96,911 views · PI 289.29 (Breakout) · taxes_irs/list_countdown · face=True · thumb text: “ie/THI</AFTER/AGE/65”
  - 0-30s: “There are seven kinds of income. The IRS is legally not allowed to touch after the age of 65. And one of them can shield as much as $500,000 from federal tax in a single afternoon. Yet almost every senior in this country knows about only one of the seven and quietly hands the government money that was never entitled to take. Think about that. Not a loophole, not a scheme, not some gray area”
  - end: “give anyway. Most seniors know the one. Starting today, you know all seven. Find your provisional income, draw from the right accounts in the right order, use the home exclusion, make the charitable distribution before y…” · sources: Social Security Administration (SSA); IRS
- **Never Keep More Than This in the Bank After 65 — Most Seniors Miss These** — [NXhhbwvx3Fg](https://www.youtube.com/watch?v=NXhhbwvx3Fg) · 2026-10-10 · 23.95 min · 185,127 views · PI 166.63 (Breakout) · banking_cash/warning_mistake · face=True · thumb text: “TAKE/YOUR/LES)/OVER/THIS/AMOUNT”
  - 0-30s: “If a debt collector wins a court judgment against you, federal law automatically protects only about two months of your social security sitting in your bank account. Every dollar above that line can be frozen within two business days of the bank getting the order, not your whole balance, not your life savings, two months. And that's just one of the lines. There are seven of them. Seven amounts that once your bank balance cross…”
  - end: “every account once a year and search your name on your state's unclaimed property site. Seven, open every letter that says your bank is merging and check your coverage with the FDIC. If a garnishment order ever hits your…” · sources: Social Security Administration (SSA); IRS; CBO / Treasury

## 6. Underperforming video analysis
**Check Your Mailbox. 600,000 Seniors Are Losing Their Medicare Plan** (ZEsdKt4Jdws, 335), **Seniors: New Income Eligibility Rules in October 2026** (hbtiNALywK8, 35 views — SNAP rule topic that won for Robin MBA, 234k), **5 Types of Debt Relief Seniors Should Know About After Age 65** (NyCxO-ZkD3k, 43 views — Nia's script opening re-used).

### Evidence: bottom-PI long-form videos
- **Check Your Mailbox. 600,000 Seniors Are Losing Their Medicare Plan** — [ZEsdKt4Jdws](https://www.youtube.com/watch?v=ZEsdKt4Jdws) · 2026-10-04 · 15.48 min · 335 views · PI 0.08 (Underperforming) · medicare_health_costs/how_to · face=True · thumb text: “SECURITY/AR”
  - 0-30s: “Check your mailbox this week because 600,000 people are about to find out their Medicare plan is gone. Not changed, gone. The letters go out by Friday, October 2nd. And every one of those 600,000 comes from a single company. And here's what worries me. Most people who open that letter will read the first line, see the same company name printed on a brand new plan, and sign it without reading another word. That's”
  - end: “out. And if you truly cannot leave, there's one more lever. If your plan no longer has any doctor in its network who can provide the care you need within a reasonable distance, the plan is supposed to arrange that care o…” · sources: Social Security Administration (SSA); IRS; Trustees report; Academic / research study
- **Seniors: New Income Eligibility Rules in October 2026 — What to Know if You Were Denied** — [hbtiNALywK8](https://www.youtube.com/watch?v=hbtiNALywK8) · 2026-09-22 · 19.27 min · 35.00 views · PI 0.10 (Underperforming) · budgeting_debt/news_change_update · face=True · thumb text: “SENIORS/penet”
  - 0-30s: “If you are 60 or older and somebody once told you your income was too high to qualify for food help, that answer came out of a test that does not apply to your household. That has been true for years. And on the 1st of October, which is days away now, every number sitting behind that answer gets thrown out and replaced. Nobody wrote to you the first time. The second time will be”
  - end: “closes the door forever. The rules are written in numbers, deductions, dates, and procedures. Your job is to make sure the facts of your household actually make it into that calculation. If your state office has never on…” · sources: Social Security Administration (SSA); IRS
- **5 Types of Debt Relief Seniors Should Know About After Age 65** — [NyCxO-ZkD3k](https://www.youtube.com/watch?v=NyCxO-ZkD3k) · 2026-09-26 · 14.00 min · 43.00 views · PI 0.13 (Underperforming) · budgeting_debt/list_countdown · face=True · thumb text: “SENIORS/CHECK/YOUR/BILLS/Outstanding/KNOW/HAT/YOu”
  - 0-30s: “There are five bills that the government itself says you may no longer have to pay once you turn 65. Not a smaller amount, not a discount, shaved off the top. The whole bill gone, wiped away by a rule that already exists and already has your name on it. And here is the part that should make you angry. Nobody whose job it is to collect that money from you has the slightest reason”
  - end: “of reach by a system that was hoping you would never ask. So, ask. And if this video helped you, please share it with one person over 65 you care about and subscribe so you do not miss the next one. Then let yourself fee…” · sources: Social Security Administration (SSA); IRS; Congress / legislation; VA

## 7. Successful vs failed comparison
Same presenter, same network scripts. Outcome looks close to a lottery across copies: identical concepts win on one channel/date and fail on another — strong sign that **distribution (who gets tested first, audience saturation) rather than script quality** decides network copies (HYPOTHESIS; traffic data unavailable).

| feature | upper half | lower half |
|---|---|---|
| t_number | 82% | 100% |
| t_dollar | 0% | 0% |
| t_question | 0% | 0% |
| t_you | 36% | 45% |
| t_fear_risk | 27% | 36% |
| t_urgency | 36% | 55% |
| t_secret_truth | 9% | 0% |
| t_named_entity | 45% | 27% |
| t_caps_word | 27% | 18% |
| t_year | 27% | 55% |
| h_first_sentence_q | 0% | 0% |
| h_you_in_30s | 91% | 73% |
| h_number_30s | 73% | 91% |
| h_dollar_30s | 36% | 36% |
| h_stakes_30s | 0% | 9% |
| h_contrarian_30s | 36% | 45% |
| h_open_loop_30s | 0% | 55% |
| h_promise_30s | 36% | 18% |
| h_story_open | 0% | 9% |
| h_greeting_open | 9% | 0% |
| h_first_person_30s | 0% | 9% |
| s_cta_end | 91% | 45% |
| tx_words (median) | 4,194 | 2,693 |
| s_num_density (median) | 2.14 | 0.99 |
| s_q_density (median) | 0.02 | 0.08 |
| s_but_density (median) | 0.23 | 0.23 |
| s_example_density (median) | 0.05 | 0.04 |
| s_data_density (median) | 1.27 | 0.37 |
| s_loop_density (median) | 0.00 | 0.00 |
| s_you_density (median) | 4.38 | 4.01 |
| s_wpm (median) | 166 | 170 |
| h_title_overlap_150 (median) | 0.38 | 0.22 |
| i_promise_pos (median) | 140 | 164 |
| t_len (median) | 73.00 | 67.00 |
| th_text_words (median) | 5.00 | 4.00 |
| th_colorfulness (median) | 93.30 | 91.70 |
| thumbnail has face | 100% | 100% |



## 8. Topic discovery and research sources
Network scripts; some real rules (garnishment protection, SNAP Oct-1 reset).

Institutions named in transcripts/descriptions (rule-based; 'Academic / research study' matches generic words like “study/research” and is low-confidence): IRS 19, Social Security Administration (SSA) 16, Congress / legislation 9, CBO / Treasury 8, Academic / research study 5, Federal Reserve 2, VA 2, Trustees report 2, Company filings / earnings 1, BLS / CPI data 1
Description link domains: payhip.com 2
Per-video source map: `SOURCE_MAP.csv`.

## 9. Trend behaviour
Network concept waves.

## 10. Thumbnail strategy
Montage not inspected.

## 11. Title strategy
Network formula ("— Most Seniors Miss These").

## 12. Hook and introduction strategy
Copied network openings (VERIFIED for two videos).

## 13. Script and storytelling strategy
14-28 min; 13 near-duplicate flags.

## 14. Audience engagement model
Fear of bank/IRS actions.

## 15. Upload and publishing strategy
~24 videos in 8 weeks.

## 16. PDF principle evaluation
Judge: *YouTube Automation – Complete Master Playbook* (556 pp., sha256 c630c24b…576d). Supporting authority: global-youtube-knowledge (DS-000011/18/31) — see `00_PROJECT_OVERVIEW/GLOBAL_KNOWLEDGE_MAP.md`. Automated evidence uses text proxies; verdict = analyst override where noted, else rule-based draft.

| ID | PDF principle (location) | What the PDF says | Evidence from channel (automated, incl. winners vs rest where testable) | Verdict | Analyst note |
|---|---|---|---|---|---|
| P01 | Module 2.1 Outlier Concept, pp.6-9; Method 1 Outlier Transplant, pp.34-35 | Find videos that beat the channel norm (5-10x strong, 10x+ clear outlier) and treat their TOPIC as proven demand; build the calendar from validated outliers. | 8 long-form ≥5x and 5 ≥10x own baseline; after 6 winners, next-10 uploads repeat the winner's topic 13% vs base rate 17% | **NOT FOLLOWED** |  |
| P02 | Module 2.2 Niche vs Format vs Template, p.11 | A niche is an audience + persistent interest + monetisation path, not a topic; every video should feel like it belongs to the same channel. | top-2 topics (taxes_irs, retirement_accounts_tax) = 38% of uploads; explicit audience marker in 79% of titles | **NOT FOLLOWED** | channel name "Housing" vs senior-tax content. |
| P03 | Module 2.2, pp.12-13 | One niche can carry many formats; add formats to grow without changing niche. | 2 title-format types each ≥10% of uploads (news_change_update 46%, list_countdown 33%, statement_other 8%, warning_mistake 8%) | **PARTIALLY FOLLOWED** |  |
| P04 | Module 2.2 p.13; Masterclass Ch.23 p.351; Web research §7 p.555 | Avoid repetitive/mass-produced uploads; rotating templates alone is not enough — each video needs distinct substance (inauthentic-content policy). | near-duplicate-script flag on 54% of videos; repeated title word-sets within channel 0% | **CONTRADICTED BY EVIDENCE** | 54% of videos flagged near-duplicate, including cross-channel script reuse (inauthentic/reused-content risk, PDF p.555 §7). |
| P05 | Module 2.3 Format Arbitrage pp.18-20; Module 2.4 Niche Bending pp.24-26 | Win by transplanting a proven format into a niche that lacks it, or by combining two overlapping niches. | requires historical competitor-format landscape at launch; analyst note in report if a bend is visible | **NOT TESTABLE** |  |
| P06 | Module 2.7 Competitor Research pp.28-30; Method 1 p.34 | Study competitors’ top videos, titles, thumbnails, cadence and comments; cover proven topics with original content. | 8% of titles share a word-set with another channel; this channel published first on 1 of 2 | **CONTRADICTED BY EVIDENCE** | wholesale script copying produced lottery-like results. |
| P07 | Method 2 Title Template Injection pp.39-40; 100 Title Formats pp.52-64 | Inject niche topics into proven title psychology families (mystery, downfall, contradiction, revelation, practical, conflict…), but the content must deliver. | 33% of titles match a 100-format family; median PI with 4.28 (n=8) vs without 0.67 (n=14) | **PARTIALLY FOLLOWED** |  |
| P08 | 100 Title Formats p.53 (five-part engine), p.66 scorecard | A strong title names a recognisable subject, a situation, a trigger, a tension and a concrete promise/stakes. | 100% of titles carry a number/$/named entity | **FOLLOWED** |  |
| P09 | 100 Title Formats p.68 (12 mistakes); Masterclass Ch.19 p.345 | Avoid generic subjects, two promises, vague “this/they” openers, ALL CAPS overuse, overstated certainty. | titles with ≥3 ALL-CAPS words 8%; vague 'this/they' opener 0%; double-question 0% | **FOLLOWED** |  |
| P10 | 100 Title Formats p.66 (title+thumbnail one promise), p.68 #11 | Thumbnail should add a complementary clue, not repeat the title. | OCR thumbnail text found on 100%; median share of thumbnail words repeated from title 0.25 | **FOLLOWED** |  |
| P11 | Module 2.7 Thumbnail Teardown p.28 (supporting: DS-000011 Packaging SOP) | Study colour, text amount, faces/expressions, focal object, contrast and template consistency; one clear idea. | thumbnail images 100%; median OCR words 5.5 (OCR undercounts stylised text); face/character detected 100% (cartoon faces often missed) | **PARTIALLY FOLLOWED** |  |
| P12 | Engagement Playbook §1 p.265; Masterclass Zone 1 p.320 | The first ~3-5 seconds must create curiosity: question, shock stat, contradiction, mystery, story drop, direct challenge. | opening ~75 words contain question/number/contradiction/story/you-hook in 88%; greeting/channel-intro opening 4% | **FOLLOWED** |  |
| P13 | Masterclass Zone 2 p.320; Engagement §18 p.283 | Within ~5-15 s answer “why should I care?” — connect to the viewer’s money, safety or identity. | explicit stakes/why-it-matters language early in 17% | **NOT FOLLOWED** |  |
| P14 | Masterclass Zone 3 p.320; Ch.23 p.350 | Open at least one curiosity loop before ~30 s and keep it open. | explicit open-loop/promise phrase in first ~150 words of 33% | **PARTIALLY FOLLOWED** |  |
| P15 | Engagement §2 & §7 pp.267, 272 | Use bridging teases / micro-cliffhangers at segment transitions to prevent drop-off. | bridge/cliffhanger phrases per 100 words (median) 0.000 | **NOT FOLLOWED** |  |
| P16 | Engagement §8 p.273 | Precise numbers, dates, named sources and expert quotes signal research and keep sceptical viewers. | data/citation terms per 100 words 0.98; videos naming an institution/source 92% | **PARTIALLY FOLLOWED** |  |
| P17 | Engagement §6 p.271 | Second-person address makes the viewer a participant (“if you own…”, “imagine you…”). | 'you/your' per 100 words (median) 4.13 | **FOLLOWED** |  |
| P18 | Engagement §15-16 pp.280-281; Deployment p.284 | Close loops, then future-pace to a next video; strongest CTA right after a payoff, not only at the end. | next-video tease in final ~60 words 17%; any CTA in final 10% 71% | **PARTIALLY FOLLOWED** |  |
| P19 | Module 2.3 p.19 (8+ min sweet spot); Web research §8 p.555 | Course: formats should fill 8+ minutes; appendix: 8 min is a mid-roll eligibility rule, length should follow the story. | median long-form length 22.5 min; Spearman(duration, PI) 0.58 — 8+ min is an ad-eligibility rule, not a success rule (PDF p555) | **FOLLOWED** |  |
| P20 | Module 2.7 Posting cadence p.29 | Check upload frequency, consistency, dead periods and growth inflection points. | median gap 1.0 d, gap CV 2.05, longest pause 20 d | **NOT FOLLOWED** |  |
| P21 | Topic Selection Masterclass intro p.33 | “A bad video on the right topic will outperform a great video on the wrong topic” — topic selection is the main lever. | spread of median PI across topics 1298.17x (best banking_cash) vs across title formats 6.59x (best list_countdown) | **FOLLOWED** |  |
| P22 | Method 2 warning p.40; 100 Formats p.68 #12; Masterclass Ch.19 p.345 | Title gets the click, content keeps the viewer: the opening must confirm and the video must deliver the title’s promise. | median share of title keywords that appear in the first ~150 spoken words 0.38 | **PARTIALLY FOLLOWED** |  |

## 17. Strengths and weaknesses
Proven network concepts. Weaknesses: duplicated scripts, identity mismatch, policy risk.

## 18. Replicable working model
Not a model to copy — evidence of the network's duplication strategy.

## 19. What to copy
Nothing beyond the underlying real rules.

## 20. What not to copy
Re-using other channels' scripts; mismatched channel names.

## 21. Missing evidence and limitations
Network ownership inferred; montage not inspected.

- Not available from this dataset for any channel: CTR, impressions, retention curves, traffic sources, subscriber growth history, comments text. Hook timings are word-position estimates (untimed transcripts).

## 22. Final channel diagnosis
1) Lottery-like outcomes from copied network scripts. 2) Advantage: none original. 3) Model: script duplication. 4) Topic: senior banking/IRS. 5) Packaging: network presenter. 6) Script: copied openings. 7) Interest: fear of losing benefits. 8) Failures: copies, saturation. 9) Learn: duplication is fragile. 10) Don't copy: any of it. 11) Repeatable: risky. 12) Reputation: none. 13) Lesson: **identical scripts on multiple channels make results a lottery and invite policy action.**
"If I wanted a senior-benefits channel, I would not follow this one; I would study the original Nia Prescott and Mark Calloway entries and write verified, original scripts."
