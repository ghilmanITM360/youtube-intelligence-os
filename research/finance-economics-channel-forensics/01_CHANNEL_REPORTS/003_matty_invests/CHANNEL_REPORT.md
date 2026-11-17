# Matty Invests — Channel Forensic Report

Channel #003 of 69 · investigation tier 1 (data-availability order, not a quality rank) · research date 2026-11-12 · source DB `finance_economics_complete.db` sha256 fa6fd1b2…d20 (branch data/finance-economics-complete-2026-11-11 @933f236e).

Evidence labels used: **VERIFIED** (directly in DB / public page), **INFERRED** (derived from DB text by rule or analyst reading), **HYPOTHESIS** (plausible, untested), **UNKNOWN**. Public view counts do not reveal CTR, retention or traffic sources; none of those are claimed.

**Key conclusion:** Clearest niche-pivot case in the dataset: Jan-2026 general budgeting videos for young adults got 171-646 views, then from 31 Jan 2026 the channel switched to **retiree lifestyle & "what retirement with $X looks like"** and produced 15 breakouts (up to 1.08M views, PI 498) — audience choice, not script craft, made the channel.

## 1. Channel identity and positioning
Faceless illustrated host "Matt" ("What's up everyone? Matt here", gR3EWBGXP2c — VERIFIED). Primary sub-niche after the pivot: **retirement reality & retiree lifestyle/psychology for 55-75-year-old Americans** — observational ("Things Wealthy Retirees Stopped Buying", "Things Retirees Stopped Caring About", "Simple Routines Thriving Retirees Practice") plus number-anchored reality checks ("$500,000", "$2 Million", "Average Person Retires With This Much"). 86 of 94 videos are retirement-tagged. Audience (INFERRED): US near-retirees/retirees with 401k + Social Security, worried whether they are "okay". Problem solved: reassurance + social comparison ("Am I doing better or worse than other retirees?"). Differentiation: warm anecdotal storyteller voice (neighbour Steve, old man Ray) rather than an adviser; no source links, no funnel in descriptions.

## 2. Database inventory and coverage
- Channel ID `UCkqzov98m_7niJOXwbRQgBA` · handle nan · https://www.youtube.com/channel/UCkqzov98m_7niJOXwbRQgBA
- Registered sub-niche: retirement finance / retiree lifestyle · subscribers: n/a · availability: AVAILABLE nan
- Description: nan
- Videos in DB 94 (long 94, Shorts 0); views 94; transcripts 93 (99%); thumbnail images 94 (100%); FULL metadata 100%; PI-classified long 94
- Dates 2026-01-24 → 2026-08-22; median views 3,984; p90 31,699; max 1,084,237
- Cadence: 13.4 uploads/month over 6.9 months; median gap 2.0 d; max gap 5 d; weekday mode Saturday
- Duration (min): median 14.2; p10 13.3; p90 15.0; first-third median 14.4 vs last-third 14.1
- Spearman(gap-before-upload, PI) = -0.07; Spearman(duration, PI) = -0.02; median PI first third 0.93 vs last third 0.94
- PI classes (long): Average 41, Underperforming 26, Breakout 15, Successful 12; near-duplicate-script flags 0
- Titles whose word-set also appears on another channel: 3 (3%)
- **7 Things Wealthy Retirees Stopped Buying to Stay Rich** — [5V1gCUvdqMs](https://www.youtube.com/watch?v=5V1gCUvdqMs) · 2026-05-11 · 14.13 min · 1,084,237 views · PI 498.27 (Breakout) · retirement_accounts_tax/list_countdown · face=True · thumb text: “RETIREES/38/WHO/BUY”
- **Why People Get Richer After Retirement** — [7mqI2YgRW1w](https://www.youtube.com/watch?v=7mqI2YgRW1w) · 2026-01-31 · 12.63 min · 223,088 views · PI 76.69 (Breakout) · retirement_accounts_tax/explainer · face=True · thumb text: “RICHER/AFTER”
- **10 Things Retirees Just Stopped Caring About** — [A-lvYmMpGSA](https://www.youtube.com/watch?v=A-lvYmMpGSA) · 2026-07-13 · 13.97 min · 219,096 views · PI 43.21 (Breakout) · retirement_accounts_tax/list_countdown · face=False · thumb text: “WHO/DON’T”
- **What Retirement Looks Like With a $2Million Portfolio** — [6U9jXkpQBzE](https://www.youtube.com/watch?v=6U9jXkpQBzE) · 2026-03-26 · 14.53 min · 146,923 views · PI 35.51 (Breakout) · retirement_accounts_tax/statement_other · face=False · thumb text: “THE/$2M/RETIREMENT/2M/REALITY”
- **If You have Saved $500,000, This is Your Retirement Reality** — [gR3EWBGXP2c](https://www.youtube.com/watch?v=gR3EWBGXP2c) · 2026-02-05 · 14.72 min · 95,382 views · PI 32.79 (Breakout) · retirement_accounts_tax/statement_other · face=True · thumb text: “oy/RETIREMENT”
- **The Average Person Actually Retires With This Much (Not Good)** — [OYOOB6eOong](https://www.youtube.com/watch?v=OYOOB6eOong) · 2026-02-07 · 14.33 min · 71,159 views · PI 24.46 (Breakout) · retirement_accounts_tax/explainer · face=True · thumb text: “AVERAGE/RETIREE/HAS/Weal/THIS”
- **When a Retiree is Considered Wealthy** — [W-cQ90FFbi0](https://www.youtube.com/watch?v=W-cQ90FFbi0) · 2026-04-09 · 13.83 min · 63,942 views · PI 20.99 (Breakout) · retirement_accounts_tax/statement_other · face=False · thumb text: “SIGNS/OF/WEALTHY/or”
- **Simple Routines Thriving Retirees Practice Daily** — [Q1RP8c_9bKs](https://www.youtube.com/watch?v=Q1RP8c_9bKs) · 2026-07-27 · 14.07 min · 122,987 views · PI 13.17 (Breakout) · retirement_accounts_tax/statement_other · face=False · thumb text: “THE/THRIVING”
- **Debt Payoff Vs Investing: The Decision Keeping You Up At Night** — [xn5wQuIpoWQ](https://www.youtube.com/watch?v=xn5wQuIpoWQ) · 2026-01-29 · 13.75 min · 171 views · PI 0.03 (Underperforming) · investing_stocks/comparison · face=True · thumb text: “IGNORE/THE/DEBT?”
- **Why You Are Paying More To Be Lazy (The Convenience Trap)** — [RBGsBXmWkwY](https://www.youtube.com/watch?v=RBGsBXmWkwY) · 2026-01-26 · 15.20 min · 201 views · PI 0.03 (Underperforming) · banking_cash/warning_mistake · face=True · thumb text: “CONVENIENTLY/BROKE”
- **Boring Habits That Will Save You Serious Money** — [vlmT5prI1aQ](https://www.youtube.com/watch?v=vlmT5prI1aQ) · 2026-01-27 · 16.45 min · 346 views · PI 0.05 (Underperforming) · wealth_psychology_habits/statement_other · face=True · thumb text: “BORING/BUT/FY/RICH”
- **The Reverse Budget: Why Your Perfect Budget Fails By Day 3** — [tGz3DaPPdMI](https://www.youtube.com/watch?v=tGz3DaPPdMI) · 2026-01-24 · 14.17 min · 646 views · PI 0.10 (Underperforming) · budgeting_debt/explainer · face=False · thumb text: “LAZY/MAN'S”
- **Sell These 5 Things Before You Retire (Or You'll Regret It)** — [3vOefiaKRzg](https://www.youtube.com/watch?v=3vOefiaKRzg) · 2026-02-03 · 14.62 min · 839 views · PI 0.13 (Underperforming) · retirement_accounts_tax/list_countdown · face=False · thumb text: “SELL/BEFORE/YOU/RETIRE”
- **Age 50 With Zero Retirement Savings (Too Late?)** — [XMPPfELet4w](https://www.youtube.com/watch?v=XMPPfELet4w) · 2026-03-05 · 12.63 min · 878 views · PI 0.21 (Underperforming) · retirement_accounts_tax/question · face=False · thumb text: “00/WITH/NO/3)/RETIREMENT/SAVINGS”
- **4 Social Security Strategies Smart Retired Couples Use (Saves You Money)** — [vHn0KvE_ku0](https://www.youtube.com/watch?v=vHn0KvE_ku0) · 2026-05-16 · 13.18 min · 582 views · PI 0.24 (Underperforming) · social_security/list_countdown · face=False · thumb text: “RETIRED/COUPLES/CLAIMING”
- **How Much You Actually Need To Retire Comfortably** — [Xnr2DD_fwI4](https://www.youtube.com/watch?v=Xnr2DD_fwI4) · 2026-02-02 · 14.98 min · 1,596 views · PI 0.25 (Underperforming) · retirement_accounts_tax/explainer · face=False · thumb text: “YOU/NEED/TO/RETIRE”

Per-video field status (AVAILABLE / MISSING / UNVERIFIED / NOT APPLICABLE) is in `VIDEO_INVENTORY.csv`. Note: the source DB was capped at ~100 newest uploads per channel for most channels, so this is not the full lifetime library.

## 3. Complete video catalogue
All 94 videos in the database (also `VIDEO_INVENTORY.csv`). PI = views ÷ median of 15 nearest-in-time uploads (same channel & format); blank PI = not classifiable (too new/too few comparables).

| # | date | title | min | views | PI | class | topic | title format | transcript |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-01-24 | [The Reverse Budget: Why Your Perfect Budget Fails By Day 3](https://www.youtube.com/watch?v=tGz3DaPPdMI) | 14.2 | 646 | 0.10 | Underperforming | budgeting_debt | explainer | Y |
| 2 | 2026-01-26 | [Why You Are Paying More To Be Lazy (The Convenience Trap)](https://www.youtube.com/watch?v=RBGsBXmWkwY) | 15.2 | 201 | 0.03 | Underperforming | banking_cash | warning_mistake | Y |
| 3 | 2026-01-27 | [Boring Habits That Will Save You Serious Money](https://www.youtube.com/watch?v=vlmT5prI1aQ) | 16.4 | 346 | 0.05 | Underperforming | wealth_psychology_habits | statement_other | Y |
| 4 | 2026-01-29 | [Debt Payoff Vs Investing: The Decision Keeping You Up At Night](https://www.youtube.com/watch?v=xn5wQuIpoWQ) | 13.8 | 171 | 0.03 | Underperforming | investing_stocks | comparison | Y |
| 5 | 2026-01-31 | [Why People Get Richer After Retirement](https://www.youtube.com/watch?v=7mqI2YgRW1w) | 12.6 | 223,088 | 76.69 | Breakout | retirement_accounts_tax | explainer | Y |
| 6 | 2026-02-02 | [How Much You Actually Need To Retire Comfortably](https://www.youtube.com/watch?v=Xnr2DD_fwI4) | 15.0 | 1,596 | 0.25 | Underperforming | retirement_accounts_tax | explainer | Y |
| 7 | 2026-02-03 | [Sell These 5 Things Before You Retire (Or You'll Regret It)](https://www.youtube.com/watch?v=3vOefiaKRzg) | 14.6 | 839 | 0.13 | Underperforming | retirement_accounts_tax | list_countdown | Y |
| 8 | 2026-02-05 | [If You have Saved $500,000, This is Your Retirement Reality](https://www.youtube.com/watch?v=gR3EWBGXP2c) | 14.7 | 95,382 | 32.79 | Breakout | retirement_accounts_tax | statement_other | Y |
| 9 | 2026-02-07 | [The Average Person Actually Retires With This Much (Not Good)](https://www.youtube.com/watch?v=OYOOB6eOong) | 14.3 | 71,159 | 24.46 | Breakout | retirement_accounts_tax | explainer | Y |
| 10 | 2026-02-09 | [Who Has $1M in Retirement Savings? (Fewer Than You Think)](https://www.youtube.com/watch?v=pcXqVMJjCRY) | 14.5 | 34,030 | 10.30 | Breakout | retirement_accounts_tax | question | Y |
| 11 | 2026-02-10 | [If This Is You, Don’t Retire Yet (5 Signs You’re Not Ready)](https://www.youtube.com/watch?v=oOW-26QLMac) | 14.8 | 9,134 | 2.76 | Successful | retirement_accounts_tax | list_countdown | Y |
| 12 | 2026-02-12 | [Why Retirees With $1M End Up With $5M (What Happens)](https://www.youtube.com/watch?v=oBJZxDwKgAU) | 14.4 | 2,909 | 0.32 | Underperforming | retirement_accounts_tax | explainer | N |
| 13 | 2026-02-14 | [The 3 Retirement Net Worth Milestones That Change Everything (Takeoff Points)](https://www.youtube.com/watch?v=-UdMJ-EtLDI) | 14.9 | 20,777 | 3.26 | Successful | retirement_accounts_tax | news_change_update | Y |
| 14 | 2026-02-16 | [Weird Habits Of A Quiet Wealthy Retiree (Not What You Expect)](https://www.youtube.com/watch?v=y3aQC2VsBr4) | 14.3 | 10,322 | 2.30 | Successful | retirement_accounts_tax | statement_other | Y |
| 15 | 2026-02-17 | [The Perfect Age to Retire (Why Wrong Timing Could Cost You Everything)](https://www.youtube.com/watch?v=yW1VMUmjA6I) | 13.5 | 2,090 | 0.33 | Underperforming | retirement_accounts_tax | explainer | Y |
| 16 | 2026-02-19 | [When Your Retirement Contribution Don’t Matter As Much (Crossover Point)](https://www.youtube.com/watch?v=ew7a9DyAc3w) | 15.3 | 6,372 | 1.42 | Average | retirement_accounts_tax | statement_other | Y |
| 17 | 2026-02-23 | [Why Millionaires Are Afraid to Retire (Money Can’t Fix This)](https://www.youtube.com/watch?v=mwEYAZ-B6WE) | 15.0 | 3,304 | 0.52 | Average | retirement_accounts_tax | explainer | Y |
| 18 | 2026-02-26 | [The Worst Retirement Risks Nobody Talks About](https://www.youtube.com/watch?v=tSbLwXj_X1I) | 14.3 | 1,820 | 0.29 | Underperforming | retirement_accounts_tax | statement_other | Y |
| 19 | 2026-02-28 | [The 5 Levels of Retirement Wealth (Which Level Are You?)](https://www.youtube.com/watch?v=GXt3_i-oW0U) | 14.5 | 22,887 | 5.11 | Breakout | retirement_accounts_tax | list_countdown | Y |
| 20 | 2026-03-02 | [What People Have in Retirement Savings (40s vs 50s vs 60s)](https://www.youtube.com/watch?v=MSVYXdwp1rQ) | 15.2 | 4,483 | 1.08 | Average | retirement_accounts_tax | comparison | Y |
| 21 | 2026-03-03 | [Big Purchases Retirees Tend To Regret (Buyer’s Remorse)](https://www.youtube.com/watch?v=8AkpOYYTBZI) | 13.7 | 2,310 | 0.52 | Average | retirement_accounts_tax | statement_other | Y |
| 22 | 2026-03-05 | [Age 50 With Zero Retirement Savings (Too Late?)](https://www.youtube.com/watch?v=XMPPfELet4w) | 12.6 | 878 | 0.21 | Underperforming | retirement_accounts_tax | question | Y |
| 23 | 2026-03-07 | [The $50,000 Per Year Lifestyle That Makes Early Retirement Possible](https://www.youtube.com/watch?v=NZmvm28xWwg) | 13.3 | 1,620 | 0.36 | Underperforming | retirement_accounts_tax | statement_other | Y |
| 24 | 2026-03-09 | [If You Haven’t Hit These 7 Goals, Don’t Retire Yet (Pre-Retirement Goals)](https://www.youtube.com/watch?v=rrK4jxX1iqw) | 13.7 | 8,243 | 2.49 | Successful | retirement_accounts_tax | statement_other | Y |
| 25 | 2026-03-10 | [The 3 Bucket Strategy That Protects Your Retirement (No Market Panic)](https://www.youtube.com/watch?v=0Rx97OZUZYU) | 14.1 | 26,260 | 7.95 | Breakout | retirement_accounts_tax | how_to | Y |
| 26 | 2026-03-12 | [Why Wealthy Retirees Are Broke (The High Net Worth Trap)](https://www.youtube.com/watch?v=UB-UphJ0omU) | 14.5 | 8,496 | 2.05 | Successful | retirement_accounts_tax | warning_mistake | Y |
| 27 | 2026-03-14 | [Habits That Lead To A Happy Retirement (Most People Ignore This)](https://www.youtube.com/watch?v=mqvWSqNO55s) | 14.1 | 8,411 | 1.89 | Average | retirement_accounts_tax | statement_other | Y |
| 28 | 2026-03-16 | [The Best Retirement Formula That Works](https://www.youtube.com/watch?v=IHoUY2hghik) | 15.2 | 4,137 | 0.93 | Average | retirement_accounts_tax | statement_other | Y |
| 29 | 2026-03-17 | [The 5 Retirement Accounts Every Retiree Must Have](https://www.youtube.com/watch?v=HzqvqkTqHQw) | 14.2 | 2,739 | 0.61 | Average | retirement_accounts_tax | statement_other | Y |
| 30 | 2026-03-19 | [The Biggest Expenses in Retirement (and How Not To Go Broke)](https://www.youtube.com/watch?v=aMH-exqAEMM) | 14.7 | 2,359 | 0.57 | Average | retirement_accounts_tax | statement_other | Y |
| 31 | 2026-03-21 | [The 5 Rich Retirees Who Live Normal Lives (You Would Never Know)](https://www.youtube.com/watch?v=SivV3DDEJyI) | 14.3 | 17,678 | 4.27 | Successful | retirement_accounts_tax | warning_mistake | Y |
| 32 | 2026-03-23 | [These 9 Things Go Quiet After Retirement (It All Stops)](https://www.youtube.com/watch?v=H8kup-oSQmI) | 14.8 | 3,047 | 0.68 | Average | retirement_accounts_tax | list_countdown | Y |
| 33 | 2026-03-26 | [What Retirement Looks Like With a $2Million Portfolio](https://www.youtube.com/watch?v=6U9jXkpQBzE) | 14.5 | 146,923 | 35.51 | Breakout | retirement_accounts_tax | statement_other | Y |
| 34 | 2026-03-28 | [Things You Should Never Disclose in Retirement](https://www.youtube.com/watch?v=4tqLCvZ2SNQ) | 14.8 | 4,461 | 1.08 | Average | retirement_accounts_tax | warning_mistake | Y |
| 35 | 2026-03-30 | [Retire Rich Vs Retire Early (What They Don’t Tell You)](https://www.youtube.com/watch?v=fbRngtoFCok) | 13.4 | 3,384 | 0.82 | Average | retirement_accounts_tax | comparison | Y |
| 36 | 2026-04-02 | [You're Probably Stuck in The Wrong Retirement Wealth Stage (3 is The Hardest)](https://www.youtube.com/watch?v=Gz_-WMHyuYc) | 13.7 | 1,309 | 0.40 | Underperforming | retirement_accounts_tax | statement_other | Y |
| 37 | 2026-04-04 | [Why Retirement With Pension Changes Everything](https://www.youtube.com/watch?v=A5CbGErHp_I) | 14.2 | 24,516 | 8.05 | Breakout | retirement_accounts_tax | news_change_update | Y |
| 38 | 2026-04-06 | [Why Retirees Are Claiming Social Security At 62](https://www.youtube.com/watch?v=ZXmetN_HqKU) | 14.5 | 2,466 | 0.81 | Average | social_security | explainer | Y |
| 39 | 2026-04-09 | [When a Retiree is Considered Wealthy](https://www.youtube.com/watch?v=W-cQ90FFbi0) | 13.8 | 63,942 | 20.99 | Breakout | retirement_accounts_tax | statement_other | Y |
| 40 | 2026-04-11 | [The Worst Retirement Lies Told By Gurus](https://www.youtube.com/watch?v=X5fS1BiB77M) | 14.6 | 2,136 | 0.69 | Average | retirement_accounts_tax | statement_other | Y |
| 41 | 2026-04-16 | [Decisions Most Retirees Regret When It's Too Late](https://www.youtube.com/watch?v=IWYACxLwvXE) | 14.7 | 1,973 | 0.64 | Average | retirement_accounts_tax | statement_other | Y |
| 42 | 2026-04-18 | [Cheap Purchases That Make Your Retirement Better](https://www.youtube.com/watch?v=ArxgTzUVACA) | 13.2 | 3,261 | 1.32 | Average | retirement_accounts_tax | statement_other | Y |
| 43 | 2026-04-20 | [How Regular People Are Retiring Earlier Than Their Parents Ever Could](https://www.youtube.com/watch?v=IrxxZmRLsk4) | 12.8 | 1,279 | 0.45 | Underperforming | retirement_accounts_tax | statement_other | Y |
| 44 | 2026-04-25 | [Why The 4% Rule Is Failing Retirees](https://www.youtube.com/watch?v=ykiOiesXp1Q) | 14.0 | 1,344 | 0.55 | Average | retirement_accounts_tax | explainer | Y |
| 45 | 2026-04-27 | [The Truth About Retiring with $1.5 Million (Not as Rich as You Think)](https://www.youtube.com/watch?v=aNWMT8ERqJg) | 14.1 | 3,105 | 1.29 | Average | wealth_psychology_habits | explainer | Y |
| 46 | 2026-04-30 | [What Really Happens After You Retire: The 4 Phases Explained](https://www.youtube.com/watch?v=RzObK5U0fgY) | 13.0 | 2,412 | 1.11 | Average | retirement_accounts_tax | explainer | Y |
| 47 | 2026-05-02 | [Why Retirees Avoid ROTH Conversion](https://www.youtube.com/watch?v=3eX5gEQf-ig) | 13.1 | 13,803 | 6.46 | Breakout | retirement_accounts_tax | warning_mistake | Y |
| 48 | 2026-05-04 | [Why Some Retirees Look Poor But Retire Rich](https://www.youtube.com/watch?v=KiF6m_AtCnE) | 14.2 | 5,497 | 2.79 | Successful | retirement_accounts_tax | explainer | Y |
| 49 | 2026-05-07 | [Why So Many Retirees Still Feel Stuck (Retired But Not Free)](https://www.youtube.com/watch?v=DzkrfHOm84s) | 13.7 | 1,218 | 0.50 | Average | retirement_accounts_tax | explainer | Y |
| 50 | 2026-05-09 | [The Guardrails Approach Smart Retirees Use](https://www.youtube.com/watch?v=6woqo1NcxqM) | 14.4 | 2,816 | 1.29 | Average | retirement_accounts_tax | statement_other | Y |
| 51 | 2026-05-11 | [7 Things Wealthy Retirees Stopped Buying to Stay Rich](https://www.youtube.com/watch?v=5V1gCUvdqMs) | 14.1 | 1,084,237 | 498.27 | Breakout | retirement_accounts_tax | list_countdown | Y |
| 52 | 2026-05-14 | [The Major Areas Most Retirees Spend Their Money On (Wait For #4)](https://www.youtube.com/watch?v=XWjOboUVNLw) | 12.7 | 2,176 | 0.90 | Average | retirement_accounts_tax | statement_other | Y |
| 53 | 2026-05-16 | [4 Social Security Strategies Smart Retired Couples Use (Saves You Money)](https://www.youtube.com/watch?v=vHn0KvE_ku0) | 13.2 | 582 | 0.24 | Underperforming | social_security | list_countdown | Y |
| 54 | 2026-05-18 | [Why $1Million in Retirement is Not What it Used to Be](https://www.youtube.com/watch?v=cep3_UdQSYs) | 13.9 | 698 | 0.29 | Underperforming | retirement_accounts_tax | explainer | Y |
| 55 | 2026-05-21 | [Pay Off Your Mortgage or Invest Before Retirement: What The Maths Say](https://www.youtube.com/watch?v=pZOkjOKtjsk) | 13.6 | 652 | 0.27 | Underperforming | retirement_accounts_tax | statement_other | Y |
| 56 | 2026-05-23 | [7 Boring Assets Rich Retirees Use To Protect Wealth Over Time](https://www.youtube.com/watch?v=I3mUug_XsWo) | 14.8 | 1,253 | 0.51 | Average | retirement_accounts_tax | list_countdown | Y |
| 57 | 2026-05-25 | [Why You Should Retire Quietly and Tell No One](https://www.youtube.com/watch?v=PcIXzvdMyPw) | 13.4 | 3,002 | 1.32 | Average | retirement_accounts_tax | explainer | Y |
| 58 | 2026-05-28 | [6 Signs You Will Be Broke in Retirement](https://www.youtube.com/watch?v=4luWypoGeMY) | 13.3 | 2,268 | 0.93 | Average | retirement_accounts_tax | list_countdown | Y |
| 59 | 2026-05-30 | [The Tax Strategies Smart Retirees Use to Save Money](https://www.youtube.com/watch?v=TVkjF2uEOe8) | 14.5 | 776 | 0.32 | Underperforming | retirement_accounts_tax | statement_other | Y |
| 60 | 2026-06-01 | [The 3 Financial Classes of Retirement: Rich, Comfortable, and Broke](https://www.youtube.com/watch?v=SCKa6EUgmv8) | 14.3 | 20,551 | 9.06 | Breakout | retirement_accounts_tax | statement_other | Y |
| 61 | 2026-06-04 | [8 Valuable Skills You Must Have Before You Retire](https://www.youtube.com/watch?v=u5veLUVgkNw) | 14.6 | 2,445 | 0.95 | Average | retirement_accounts_tax | list_countdown | Y |
| 62 | 2026-06-06 | [Cheap Purchases Quietly Ruining Your Retirement Wealth](https://www.youtube.com/watch?v=OZmMwcvwfr0) | 13.6 | 2,797 | 1.14 | Average | retirement_accounts_tax | statement_other | Y |
| 63 | 2026-06-08 | [The Retirement Portfolio That Puts You in The Top 5%](https://www.youtube.com/watch?v=R0V1oQJdfBQ) | 13.5 | 5,910 | 2.41 | Successful | retirement_accounts_tax | statement_other | Y |
| 64 | 2026-06-11 | [7 Minimalist Money Rules Smart Retirees Live By (For a Stable Retirement)](https://www.youtube.com/watch?v=uEBUY_Sbsy0) | 14.1 | 2,755 | 1.12 | Average | retirement_accounts_tax | list_countdown | Y |
| 65 | 2026-06-13 | [The 7 Sacrifices Smart Retirees Make to Retire in Comfort](https://www.youtube.com/watch?v=_Gw6QdET-GA) | 14.1 | 2,580 | 0.94 | Average | retirement_accounts_tax | statement_other | Y |
| 66 | 2026-06-15 | [The 3 Points of Retirement Spending (Smiling Curve Explained)](https://www.youtube.com/watch?v=12-psgr_Zb4) | 13.9 | 975 | 0.35 | Underperforming | retirement_accounts_tax | explainer | Y |
| 67 | 2026-06-18 | [The Smartest Way To Exit Employment and Enter Full Retirement](https://www.youtube.com/watch?v=DUtgle50EeA) | 14.9 | 12,804 | 4.96 | Successful | retirement_accounts_tax | statement_other | Y |
| 68 | 2026-06-20 | [6 Bills Retirees Should Stop Paying (Silent Money Leaks)](https://www.youtube.com/watch?v=58VwbpqvC5s) | 14.0 | 2,455 | 0.88 | Average | retirement_accounts_tax | list_countdown | Y |
| 69 | 2026-06-22 | [5 Worst Debts To Have in Retirement (Pay These Off Before You Retire)](https://www.youtube.com/watch?v=1hlOdAGkp7w) | 14.1 | 4,800 | 1.72 | Average | retirement_accounts_tax | list_countdown | Y |
| 70 | 2026-06-27 | [9 Small Businesses Smart Retirees Are Starting to Earn Extra Income](https://www.youtube.com/watch?v=WQie_lgQjdU) | 14.1 | 1,943 | 0.40 | Underperforming | retirement_accounts_tax | list_countdown | Y |
| 71 | 2026-06-29 | [7 Financial Mistakes Rich Retirees Never Make in Retirement](https://www.youtube.com/watch?v=5hLuvp8-CWQ) | 14.7 | 1,493 | 0.30 | Underperforming | retirement_accounts_tax | list_countdown | Y |
| 72 | 2026-07-04 | [Retiring With $800,000: What Your Retirement Really Looks Like](https://www.youtube.com/watch?v=eqrZvFnYIKM) | 15.4 | 4,214 | 0.84 | Average | retirement_accounts_tax | statement_other | Y |
| 73 | 2026-07-06 | [Retirement is Short: Make Every Day Count](https://www.youtube.com/watch?v=exXS73GWt5Y) | 15.0 | 12,774 | 2.55 | Successful | retirement_accounts_tax | statement_other | Y |
| 74 | 2026-07-11 | [8 Signs You're Doing Better Than Most Retirees](https://www.youtube.com/watch?v=l95A18bBXa4) | 13.8 | 48,964 | 9.77 | Breakout | retirement_accounts_tax | list_countdown | Y |
| 75 | 2026-07-13 | [10 Things Retirees Just Stopped Caring About](https://www.youtube.com/watch?v=A-lvYmMpGSA) | 14.0 | 219,096 | 43.21 | Breakout | retirement_accounts_tax | list_countdown | Y |
| 76 | 2026-07-16 | [The New Retirement Trends Most Did Not Plan For](https://www.youtube.com/watch?v=rJnPlzH4sgs) | 14.7 | 5,010 | 0.63 | Average | retirement_accounts_tax | news_change_update | Y |
| 77 | 2026-07-18 | [7 People Smart Retirees Avoid For a Peaceful Retirement](https://www.youtube.com/watch?v=6rwLldjK_o4) | 13.6 | 12,373 | 1.55 | Average | retirement_accounts_tax | list_countdown | Y |
| 78 | 2026-07-20 | [Life Lessons Older Retirees Say Matter The Most (Learn Sooner)](https://www.youtube.com/watch?v=ashNsPI8QwU) | 13.7 | 6,014 | 0.57 | Average | retirement_accounts_tax | statement_other | Y |
| 79 | 2026-07-23 | [7 Goals Happy Retirees No Longer Chase](https://www.youtube.com/watch?v=xrpI4KzTkKE) | 13.7 | 12,862 | 1.38 | Average | retirement_accounts_tax | list_countdown | Y |
| 80 | 2026-07-25 | [12 Upgrades You Should Try To Do Before You Retire](https://www.youtube.com/watch?v=hk_OglfeiJ8) | 15.0 | 3,833 | 0.33 | Underperforming | retirement_accounts_tax | list_countdown | Y |
| 81 | 2026-07-27 | [Simple Routines Thriving Retirees Practice Daily](https://www.youtube.com/watch?v=Q1RP8c_9bKs) | 14.1 | 122,987 | 13.17 | Breakout | retirement_accounts_tax | statement_other | Y |
| 82 | 2026-07-30 | [7 People Worth Keeping Close in Retirement](https://www.youtube.com/watch?v=H3GffP79KG8) | 13.6 | 5,070 | 0.48 | Underperforming | retirement_accounts_tax | list_countdown | Y |
| 83 | 2026-08-01 | [Money Mindsets Wise Retirees Adopted Early](https://www.youtube.com/watch?v=flqWdbiJ2vM) | 13.7 | 4,766 | 0.45 | Underperforming | retirement_accounts_tax | statement_other | Y |
| 84 | 2026-08-03 | [9 Types of Retirees You'll Meet in Retirement](https://www.youtube.com/watch?v=TCMbOfokAsc) | 14.5 | 19,966 | 2.50 | Successful | retirement_accounts_tax | list_countdown | Y |
| 85 | 2026-08-06 | [8 Simple Systems Most Successful Retirees Rely On](https://www.youtube.com/watch?v=tBEJq4kQJBM) | 14.7 | 7,999 | 0.86 | Average | retirement_accounts_tax | list_countdown | Y |
| 86 | 2026-08-08 | [Why Retirement is Better Than You Think](https://www.youtube.com/watch?v=m1Icu2ZyJ9E) | 13.8 | 10,494 | 1.31 | Average | retirement_accounts_tax | explainer | Y |
| 87 | 2026-08-10 | [10 Life Truths Most Retirees Finally Accept](https://www.youtube.com/watch?v=LKy3IBs1XrE) | 14.5 | 9,338 | 1.17 | Average | retirement_accounts_tax | list_countdown | Y |
| 88 | 2026-08-13 | [Places Most Retirees Feel Out of Place](https://www.youtube.com/watch?v=Rh-dGeT4fZ8) | 14.2 | 11,500 | 1.44 | Average | retirement_accounts_tax | statement_other | Y |
| 89 | 2026-08-15 | [9 Things Wise Retirees Refuse To Give Up On](https://www.youtube.com/watch?v=0WWtt8BHX2M) | 13.8 | 4,353 | 0.47 | Underperforming | retirement_accounts_tax | list_countdown | Y |
| 90 | 2026-08-17 | [Why Retirees Are Not Downsizing Like They Used To](https://www.youtube.com/watch?v=xf-aMTJTHWc) | 14.0 | 19,140 | 2.39 | Successful | retirement_accounts_tax | explainer | Y |
| 91 | 2026-08-20 | [What Retirees Realized Wasn’t Worth The Worry](https://www.youtube.com/watch?v=YOyo0KZMxwU) | 14.8 | 4,921 | 0.53 | Average | retirement_accounts_tax | statement_other | Y |
| 92 | 2026-08-22 | [Why Less is More in Retirement](https://www.youtube.com/watch?v=biobbpiQFsc) | 14.8 | 4,136 | 0.44 | Underperforming | retirement_accounts_tax | explainer | Y |
| 93 | n/a | [The 7 Pillars of a Safe Retirement](https://www.youtube.com/watch?v=wj_-IyvrPPA) | 15.1 | 3,760 | 0.94 | Average | retirement_accounts_tax | statement_other | Y |
| 94 | n/a | [The Social Security Math Every Retiree Should Know](https://www.youtube.com/watch?v=jOE_Xdc91l8) | 14.9 | 1,039 | 0.26 | Underperforming | social_security | statement_other | Y |

## 4. Topic and sub-niche map
| topic | n | long | median views | median PI | succ/breakout | under | first | last |
|---|---|---|---|---|---|---|---|---|
| retirement_accounts_tax | 86 | 86 | 4,407 | 1.01 | 27 | 20 | 2026-01-31 | 2026-08-22 |
| social_security | 3 | 3 | 1,039 | 0.26 | 0 | 2 | 2026-04-06 | 2026-05-16 |
| wealth_psychology_habits | 2 | 2 | 1,726 | 0.67 | 0 | 1 | 2026-01-27 | 2026-04-27 |
| banking_cash | 1 | 1 | 201 | 0.03 | 0 | 1 | 2026-01-26 | 2026-01-26 |
| budgeting_debt | 1 | 1 | 646 | 0.10 | 0 | 1 | 2026-01-24 | 2026-01-24 |
| investing_stocks | 1 | 1 | 171 | 0.03 | 0 | 1 | 2026-01-29 | 2026-01-29 |

Title-format mix (INFERRED tags): statement_other: n=37.0, medPI=0.93 · list_countdown: n=24.0, medPI=0.94 · explainer: n=19.0, medPI=0.55 · warning_mistake: n=5.0, medPI=2.05 · comparison: n=3.0, medPI=0.82 · news_change_update: n=3.0, medPI=3.26 · question: n=2.0, medPI=5.26 · how_to: n=1.0, medPI=7.95

Before pivot (24–29 Jan 2026, VERIFIED dates): convenience trap, boring habits ("Meet Lucy, 28"), reverse budget, debt vs investing — PI 0.03-0.10, the channel's absolute bottom. After pivot: retirement accounts/lifestyle median PI 1.01 with 27 ≥2x videos. Social-Security strategy videos (3) underperform (median PI 0.26) — the audience comes for lifestyle/comparison, not claiming mechanics. Recurring series: "Things retirees stopped…", "Retirement with $X", "When a retiree is considered wealthy".

## 5. Winning video analysis
1. **7 Things Wealthy Retirees Stopped Buying to Stay Rich** (5V1gCUvdqMs, 1.08M, PI 498): identity + secret-habit promise ("they all share one weird habit. They quit buying stuff"), list format, observed-authority ("After watching how this actually plays out for years"). Thumbnail: flamboyant old character holding a bag + "RETIREES WHO BUY NOTHING" — contradiction (rich + buy nothing).
2. **Why People Get Richer After Retirement** (7mqI2YgRW1w, 223k, PI 77): story drop at a barbecue with neighbour Steve, 68: "I'm doing way better now than I was when I was working" — counter-intuitive claim delivered by a character.
3. **10 Things Retirees Just Stopped Caring About** (A-lvYmMpGSA, 219k, PI 43): pure story hook — "the strangest thing an old man ever said to me. His name was Ray, 76… mustard stain".
4. **What Retirement Looks Like With a $2Million Portfolio** / **If You have Saved $500,000…** (6U9jXkpQBzE PI 35; gR3EWBGXP2c PI 33): number reality-check; hook gives the hard number in second 1 ("$500,000… gives you exactly $1,667 per month… both completely true and potentially completely wrong") → paradox + 5-factor promise.
5. **The Average Person Actually Retires With This Much (Not Good)** (OYOOB6eOong, PI 24): shock stats ("27% of Americans have absolutely nothing saved").
Common thread: **retiree identity + social comparison**, a human character or a hard number in the first sentence, list/reality format, ~14 min.

### Evidence: top-PI long-form videos
- **7 Things Wealthy Retirees Stopped Buying to Stay Rich** — [5V1gCUvdqMs](https://www.youtube.com/watch?v=5V1gCUvdqMs) · 2026-05-11 · 14.13 min · 1,084,237 views · PI 498.27 (Breakout) · retirement_accounts_tax/list_countdown · face=True · thumb text: “RETIREES/38/WHO/BUY”
  - 0-30s: “The retirees who actually keep their money, the ones living comfortably with zero financial stress at 75, 80, 85 years old, they all share one weird habit. They quit buying stuff. Not the necessities, they've got plenty of those. I'm talking about specific categories of purchases that drain regular retirees dry, while the wealthy ones just pass right on by. After watching how this actually plays out for years, I've narrowed it…”
  - end: “ahead and hit subscribe. Drop a comment below and tell me which one of these seven hits closest to home for you. Be honest. I'm guilty of at least two of them myself, so this is a no judgment zone. I'll catch you in the …”
- **Why People Get Richer After Retirement** — [7mqI2YgRW1w](https://www.youtube.com/watch?v=7mqI2YgRW1w) · 2026-01-31 · 12.63 min · 223,088 views · PI 76.69 (Breakout) · retirement_accounts_tax/explainer · face=True · thumb text: “RICHER/AFTER”
  - 0-30s: “I was at a barbecue last summer and I'm talking to my neighbor Steve. Steve's 68 years old, retired for about 5 years now, and I'm asking him how retirement's going. Expecting the usual, "Oh, it's nice. We're getting by" kind of response. Instead, this guy looks at me and says, "Honestly, Matt, I'm doing way better now than I was when I was working." And I'm standing there with a burger in my hand”
  - end: “saving now, if you're investing consistently, if you're keeping your expenses under control, there's a good chance that you're going to be just fine. More than fine, actually. Are you surprised that people can get richer…” · sources: Academic / research study
- **10 Things Retirees Just Stopped Caring About** — [A-lvYmMpGSA](https://www.youtube.com/watch?v=A-lvYmMpGSA) · 2026-07-13 · 13.97 min · 219,096 views · PI 43.21 (Breakout) · retirement_accounts_tax/list_countdown · face=False · thumb text: “WHO/DON’T”
  - 0-30s: “I want to tell you about the strangest thing an old man ever said to me. His name was Ray, 76. I met him in the parking lot of a hardware store, and he had a mustard stain on his shirt. Not a small one, either. A real commitment of a stain, front and center, like a medal. And I did that thing you do, that polite glance and look away, and Ray caught it.”
  - end: “actually there. You don't have to be retired to walk off that stage. That's the part that gets me. Not one thing on this list requires a 401k, a pension, or a certain birthday. You can drop every single one of these toda…”
- **What Retirement Looks Like With a $2Million Portfolio** — [6U9jXkpQBzE](https://www.youtube.com/watch?v=6U9jXkpQBzE) · 2026-03-26 · 14.53 min · 146,923 views · PI 35.51 (Breakout) · retirement_accounts_tax/statement_other · face=False · thumb text: “THE/$2M/RETIREMENT/2M/REALITY”
  - 0-30s: “$2 million people argue about the magic retirement number all the time. Some say $1 million some say $3 million your brother-in-law who dabbles in crypto probably says something completely unhinged, but $2 million that's the number that keeps coming up as the sweet spot between technically enough and actually comfortable. And today, we're going to find out if that's true. What does retirement with a $2 million portfolio actual…”
  - end: “more than any version of wealth people try to sell you online. If you found this video helpful, smash that like button. It genuinely helps the channel more than you know. Drop a comment below. What's your retirement numb…” · sources: IRS
- **If You have Saved $500,000, This is Your Retirement Reality** — [gR3EWBGXP2c](https://www.youtube.com/watch?v=gR3EWBGXP2c) · 2026-02-05 · 14.72 min · 95,382 views · PI 32.79 (Breakout) · retirement_accounts_tax/statement_other · face=True · thumb text: “oy/RETIREMENT”
  - 0-30s: “$500,000 in your retirement account gives you exactly $1,667 per month to live on. That's it. That's what the math says. Now, before you close this video and go cry into your 401k statement, hold on because what I just told you is both completely true and potentially completely wrong depending on five critical factors that most people never talk about. What's up everyone? Matt here and today we're answering one question. Can I…”
  - end: “If you realize you need to make some changes, drop a comment and tell me which of the five factors you're going to optimize first. Subscribe if you want more straight talk about money. And remember, it's not about having…” · sources: Social Security Administration (SSA); Academic / research study
- **The Average Person Actually Retires With This Much (Not Good)** — [OYOOB6eOong](https://www.youtube.com/watch?v=OYOOB6eOong) · 2026-02-07 · 14.33 min · 71,159 views · PI 24.46 (Breakout) · retirement_accounts_tax/explainer · face=True · thumb text: “AVERAGE/RETIREE/HAS/Weal/THIS”
  - 0-30s: “Three out of every four Americans you pass on the street today are walking toward a retirement they cannot afford. More than half of American workers have less money saved for their entire retirement than they earned in a single year of work. And here's the digit that should terrify you. 27% of Americans have absolutely nothing saved. Not a little, not some modest amount they're embarrassed about, zero dollars. I'm Matt, and I…”
  - end: “changed how you think about retirement, hit that like button and subscribe. We're going to keep having these difficult conversations about money that most people avoid. This information matters. Your future matters. And …” · sources: Social Security Administration (SSA); Federal Reserve; Academic / research study
- **When a Retiree is Considered Wealthy** — [W-cQ90FFbi0](https://www.youtube.com/watch?v=W-cQ90FFbi0) · 2026-04-09 · 13.83 min · 63,942 views · PI 20.99 (Breakout) · retirement_accounts_tax/statement_other · face=False · thumb text: “SIGNS/OF/WEALTHY/or”
  - 0-30s: “So, picture this. You're 67 years old. You just retired. You've got $800,000 in your 401k, a paid-off house, social security coming in every month, and your neighbor Gary just told you that you're doing okay for yourself. Gary also drives a 2009 Chevy Malibu with a bumper sticker that says, "I'd rather be fishing." So, maybe Gary's opinion on wealth isn't exactly the gold standard here. But, here's the thing. It made you wonde…”
  - end: “all about. If you got value out of this video, drop a like. Subscribe if you haven't already, and let me know in the comments, what number do you personally consider wealthy in retirement? I'm genuinely curious because i…” · sources: IRS; Academic / research study
- **Simple Routines Thriving Retirees Practice Daily** — [Q1RP8c_9bKs](https://www.youtube.com/watch?v=Q1RP8c_9bKs) · 2026-07-27 · 14.07 min · 122,987 views · PI 13.17 (Breakout) · retirement_accounts_tax/statement_other · face=False · thumb text: “THE/THRIVING”
  - 0-30s: “Let me guess how you picture retirement. There's a beach, maybe a sunset, definitely a cruise ship. You got a golf club in one hand, a drink with a little umbrella in the other, and grandkids laughing around a Christmas tree in perfect matching sweaters. It's the highlight reel, the postcard, the version they put in the brochure for the retirement community with the suspiciously green lawns. The thing is, that stuff is real. T…”
  - end: “on. I read those and I love it when you hold yourself to it out loud. If this helped you, give it a like and subscribe if you're not already. We drop new videos every week on building wealth and building a retirement tha…”

## 6. Underperforming video analysis
- Pre-pivot budgeting cluster (xn5wQuIpoWQ 171 views, RBGsBXmWkwY 201, vlmT5prI1aQ 346, tGz3DaPPdMI 646): same narrator, same humour, same 14-min length and similar scene hooks ("It's 11:00 p.m. on a Wednesday… phone charger") — but the audience is a crowded 25-35 budgeting market. Diagnosis: **topic/audience**, not script (VERIFIED by holding format constant).
- **Sell These 5 Things Before You Retire** (3vOefiaKRzg, PI 0.13), **How Much You Actually Need To Retire Comfortably** (Xnr2DD_fwI4, PI 0.25), **Age 50 With Zero Retirement Savings** (XMPPfELet4w, PI 0.21): retirement topics framed as *instruction/fear* ("Too Late?", "Or You'll Regret It") and heavily supplied generic queries; openings start "So today we're tackling the question…" (slow) vs winners' character/number openers.
- **4 Social Security Strategies Smart Retired Couples Use** (vHn0KvE_ku0, PI 0.24): mechanics topic owned by specialist channels (Kevin Explains, Nia Prescott etc. in this dataset).

### Evidence: bottom-PI long-form videos
- **Debt Payoff Vs Investing: The Decision Keeping You Up At Night** — [xn5wQuIpoWQ](https://www.youtube.com/watch?v=xn5wQuIpoWQ) · 2026-01-29 · 13.75 min · 171 views · PI 0.03 (Underperforming) · investing_stocks/comparison · face=True · thumb text: “IGNORE/THE/DEBT?”
  - 0-30s: “So, today we're tackling the question that literally keeps people up at 2 a.m. scrolling through Reddit threads. Should you pay off your debt or start investing? And look, I know what you're thinking. Matt, I'm drowning in student loans. My credit card is giving me anxiety sweats, but everyone on Twitter is posting their Robin Hood gains, and I feel like I'm missing out on the rocket to the moon. I feel you. I've”
  - end: “are just ignoring their finances and hoping everything works out. If this video helped you figure out your strategy, hit that like button and subscribe. Drop a comment and let me know. Are you team pay off debt first, te…”
- **Why You Are Paying More To Be Lazy (The Convenience Trap)** — [RBGsBXmWkwY](https://www.youtube.com/watch?v=RBGsBXmWkwY) · 2026-01-26 · 15.20 min · 201 views · PI 0.03 (Underperforming) · banking_cash/warning_mistake · face=True · thumb text: “CONVENIENTLY/BROKE”
  - 0-30s: “It's 11:00 p.m. on a Wednesday. You're laying in bed scrolling through your phone, and you remember you need a new phone charger because your dog chewed through the last one. So, you open Amazon, find a charger for 12 bucks, and you're about to click buy now when you see it. Want it tomorrow? Add $3.99 for next day delivery. And you think to yourself, you know what? I do want it tomorrow. I”
  - end: “at me for attacking your lifestyle, hit that like button, subscribe to the channel, and let me know in the comments which convenience you're going to cut back on. Or tell me I'm completely wrong and that you deserve all …” · sources: News outlets
- **Boring Habits That Will Save You Serious Money** — [vlmT5prI1aQ](https://www.youtube.com/watch?v=vlmT5prI1aQ) · 2026-01-27 · 16.45 min · 346 views · PI 0.05 (Underperforming) · wealth_psychology_habits/statement_other · face=True · thumb text: “BORING/BUT/FY/RICH”
  - 0-30s: “Meet Lucy. Lucy's 28, works a decent job, making $65,000 a year, and somehow somehow she's broke by the 20th of every month. Not I can't buy that yacht broke. We're talking I just bought a single banana and had to check my account balance broke. Last Tuesday, Lucy treated herself to a $14 artisal oat milk latte with a pump of lavender syrup because Mercury was in retrograde and she deserved it. Thursday, she”
  - end: “to have an exciting, incredible, debt-free vacation. Lucy is still paying off that ceramic mushroom lamp. Be more like Janet. Be boring. Be wealthy. If you found this helpful, hit that like button and drop a comment tell…”
- **The Reverse Budget: Why Your Perfect Budget Fails By Day 3** — [tGz3DaPPdMI](https://www.youtube.com/watch?v=tGz3DaPPdMI) · 2026-01-24 · 14.17 min · 646 views · PI 0.10 (Underperforming) · budgeting_debt/explainer · face=False · thumb text: “LAZY/MAN'S”
  - 0-30s: “It's 11:00 p.m. on a Tuesday. You're lying in bed scrolling through your phone, and you make the mistake of opening your banking app. Your checking account balance stares back at you. $847. It's the 23rd of the month. You still have a week to go until payday, and you have absolutely no idea where your money went. You had a budget, a really good one, actually. Color-coded spreadsheet and everything. You allocated money to”
  - end: “and start trusting yourself a little. If you found this helpful, hit that like button. Subscribe if you want more money content that doesn't make you want to cry into your empty wallet. And drop a comment telling me, are…”
- **Sell These 5 Things Before You Retire (Or You'll Regret It)** — [3vOefiaKRzg](https://www.youtube.com/watch?v=3vOefiaKRzg) · 2026-02-03 · 14.62 min · 839 views · PI 0.13 (Underperforming) · retirement_accounts_tax/list_countdown · face=False · thumb text: “SELL/BEFORE/YOU/RETIRE”
  - 0-30s: “Most people think retirement planning is all about saving money and investing. And yeah, that's important. But nobody talks about the other side of the equation. Getting rid of the financial anchors that'll sink your retirement faster than the Titanic. I'm talking about the stuff that seemed like a great idea when you were 45 and pulling in six figures, but turns into a money pit when you're 65 and living on a fixed income.”
  - end: “want more content about building wealth and not being broke in retirement. Drop a comment and tell me which one of these you're guilty of. I genuinely want to know. And if you want to learn more about retirement planning…”
- **Age 50 With Zero Retirement Savings (Too Late?)** — [XMPPfELet4w](https://www.youtube.com/watch?v=XMPPfELet4w) · 2026-03-05 · 12.63 min · 878 views · PI 0.21 (Underperforming) · retirement_accounts_tax/question · face=False · thumb text: “00/WITH/NO/3)/RETIREMENT/SAVINGS”
  - 0-30s: “Here's the reality. Nearly one in three Americans between the ages of 45 and 59 have absolutely nothing saved for retirement. Not a little, not some, nothing. And a lot of them are convinced that it's already too late, that the train left the station, the ship sailed, pick your transportation metaphor, and that there's no point in even trying. So, they don't. And that decision, right there, is the most expensive mistake they w…”
  - end: “at all, share it with someone in your life who needs to hear it or drop a comment below and tell me where you're starting from. Seriously, no judgment in the comment section. This is a community of people who are trying …” · sources: IRS
- **4 Social Security Strategies Smart Retired Couples Use (Saves You Money)** — [vHn0KvE_ku0](https://www.youtube.com/watch?v=vHn0KvE_ku0) · 2026-05-16 · 13.18 min · 582 views · PI 0.24 (Underperforming) · social_security/list_countdown · face=False · thumb text: “RETIRED/COUPLES/CLAIMING”
  - 0-30s: “If you and your spouse are about to claim Social Security and your entire plan is, "We'll just file when we turn 65 and figure it out from there." I need you to pause right now. Put down the coffee because there's a really good chance you're about to make decisions that could shape your finances for the next 20, 30, even 40 years and most couples make these decisions in about 15 minutes on”
  - end: “Hit that like button, subscribe, and share this with the one couple in your life that you know is just about to file at 62 without thinking about it. Save them. Be the hero of the next family barbecue. And remember, reti…” · sources: Social Security Administration (SSA); IRS; Academic / research study
- **How Much You Actually Need To Retire Comfortably** — [Xnr2DD_fwI4](https://www.youtube.com/watch?v=Xnr2DD_fwI4) · 2026-02-02 · 14.98 min · 1,596 views · PI 0.25 (Underperforming) · retirement_accounts_tax/explainer · face=False · thumb text: “YOU/NEED/TO/RETIRE”
  - 0-30s: “So today we're tackling the question that keeps half of America up at night. How much money do you actually need to retire comfortably? And no, that magic number you've heard tossed around at barbecues, on Tik Tok, and by that one uncle who swears he's a financial genius. Yeah, it's probably wrong or at least wildly incomplete. Because retirement isn't a single number. It's a moving target shaped by your lifestyle, taxes, heal…”
  - end: “your retirement journey. Are you ahead of the game, behind? Completely terrified? Let's talk about it. And hey, if this video stressed you out, just remember at least you're thinking about it now instead of later. That a…” · sources: Academic / research study

## 7. Successful vs failed comparison
Upper vs lower half: "you" in titles 45% vs 30%; spoken numbers are *lower* in winners (1.52 vs 2.07 per 100 words) and data density lower (0.59 vs 0.70) → winners are **storytelling/lifestyle**, losers are **calculation-heavy**. Openers: winners = named older character or one hard number + paradox; losers = "So today we're tackling the question" or young-adult scenes. Thumbnail avatar **aged up** after the pivot (grey-bearded host in all six winners; brown-haired younger host in five of six losers — VERIFIED in montage), i.e. packaging was re-targeted to the new audience.

| feature | upper half | lower half |
|---|---|---|
| t_number | 55% | 51% |
| t_dollar | 9% | 9% |
| t_question | 4% | 2% |
| t_you | 45% | 30% |
| t_fear_risk | 13% | 17% |
| t_urgency | 6% | 6% |
| t_secret_truth | 23% | 28% |
| t_named_entity | 0% | 6% |
| t_caps_word | 2% | 0% |
| t_year | 0% | 0% |
| h_first_sentence_q | 6% | 9% |
| h_you_in_30s | 87% | 80% |
| h_number_30s | 74% | 83% |
| h_dollar_30s | 32% | 30% |
| h_stakes_30s | 11% | 20% |
| h_contrarian_30s | 40% | 39% |
| h_open_loop_30s | 47% | 35% |
| h_promise_30s | 47% | 48% |
| h_story_open | 2% | 7% |
| h_greeting_open | 0% | 0% |
| h_first_person_30s | 60% | 52% |
| s_cta_end | 91% | 96% |
| tx_words (median) | 2,492 | 2,490 |
| s_num_density (median) | 1.52 | 2.07 |
| s_q_density (median) | 0.29 | 0.33 |
| s_but_density (median) | 0.49 | 0.51 |
| s_example_density (median) | 0.12 | 0.10 |
| s_data_density (median) | 0.59 | 0.70 |
| s_loop_density (median) | 0.08 | 0.08 |
| s_you_density (median) | 5.65 | 4.84 |
| s_wpm (median) | 180 | 179 |
| h_title_overlap_150 (median) | 0.43 | 0.38 |
| i_promise_pos (median) | 148 | 148 |
| t_len (median) | 53.00 | 54.00 |
| th_text_words (median) | 3.00 | 3.00 |
| th_colorfulness (median) | 55.80 | 55.30 |
| thumbnail has face | 19% | 11% |



## 8. Topic discovery and research sources
Few cited sources (IRS 23, SSA 6, Fed 3; no description links). Idea source (INFERRED): the pivot followed audience response — first retiree video 31 Jan 2026 broke out (PI 77) and the channel then published almost only retiree topics (P01 strongly followed). Topics like "things retirees stopped buying/caring about" mirror a cross-niche senior-lifestyle trend also present in the senior-health dataset (HYPOTHESIS; cross-channel check in final synthesis). Only 3% of titles overlap other channels' word-sets.

Institutions named in transcripts/descriptions (rule-based; 'Academic / research study' matches generic words like “study/research” and is low-confidence): Academic / research study 48, IRS 23, Company filings / earnings 9, News outlets 6, Social Security Administration (SSA) 6, CBO / Treasury 4, Federal Reserve 3, Congress / legislation 3, BLS / CPI data 1, Trustees report 1
Description link domains: none
Per-video source map: `SOURCE_MAP.csv`.

## 9. Trend behaviour
Evergreen, identity-driven; zero news dependence (3 news-framed titles). Winners keep accumulating (May video at 1.08M by Nov). Not crisis-driven.

## 10. Thumbnail strategy
Consistent illustrated host (older after pivot), white/neutral background, 3-4 bold black words with one yellow-highlighted keyword ("RETIREMENT", "BUDGET"), one prop (vault, jar, trophies, cash). Winners pair the word "RETIREES" with a paradox (WHO BUY NOTHING / WHO DON'T CARE / RICHER AFTER). Losers show a young host and budgeting props.

## 11. Title strategy
Retiree-identity noun + surprising behaviour ("Wealthy Retirees Stopped Buying", "Retirees Just Stopped Caring") or a dollar reality ("$2Million", "$500,000"). Losers: generic how-much/how-to or fear ("Or You'll Regret It", "Too Late?").

## 12. Hook and introduction strategy
Two winning hooks: (a) **character anecdote** (Steve 68, Ray 76) with a surprising quote; (b) **hard number + paradox** ("$1,667 per month… true and potentially completely wrong"). Self-intro "Matt here" appears after the hook (~50-60 words) in some. Promise phrase median 148 words (~50 s).

## 13. Script and storytelling strategy
~14 min at ~180 wpm (fast, conversational), list or reality-check structure, humour asides, named characters, moderate numbers; endings: like/subscribe + "which one hits closest to home" comment prompt; no next-video tease.

## 14. Audience engagement model
Click: identity + comparison ("wealthy retirees", "average person"). Stay: anecdotes and list escalation. Return: weekly retiree series. Trust: peer-like, non-preachy ("no judgment zone"). Comments invited as confession ("which one are you guilty of").

## 15. Upload and publishing strategy
13.4 uploads/month, median gap 2 days, never >5 days, fixed ~14 min. Gaps/length unrelated to PI. The pivot, not cadence, changed outcomes.

## 16. PDF principle evaluation
Judge: *YouTube Automation – Complete Master Playbook* (556 pp., sha256 c630c24b…576d). Supporting authority: global-youtube-knowledge (DS-000011/18/31) — see `00_PROJECT_OVERVIEW/GLOBAL_KNOWLEDGE_MAP.md`. Automated evidence uses text proxies; verdict = analyst override where noted, else rule-based draft.

| ID | PDF principle (location) | What the PDF says | Evidence from channel (automated, incl. winners vs rest where testable) | Verdict | Analyst note |
|---|---|---|---|---|---|
| P01 | Module 2.1 Outlier Concept, pp.6-9; Method 1 Outlier Transplant, pp.34-35 | Find videos that beat the channel norm (5-10x strong, 10x+ clear outlier) and treat their TOPIC as proven demand; build the calendar from validated outliers. | 15 long-form ≥5x and 9 ≥10x own baseline; after 26 winners, next-10 uploads repeat the winner's topic 97% vs base rate 91% | **FOLLOWED** | after the 31-Jan retiree breakout the channel moved ~100% of output to retiree topics; P01 auto-metric cannot show it because the whole library became one topic. |
| P02 | Module 2.2 Niche vs Format vs Template, p.11 | A niche is an audience + persistent interest + monetisation path, not a topic; every video should feel like it belongs to the same channel. | top-2 topics (retirement_accounts_tax, social_security) = 95% of uploads; explicit audience marker in 94% of titles | **FOLLOWED** | post-pivot audience is sharply defined (retirees), with packaging re-targeted (aged avatar). |
| P03 | Module 2.2, pp.12-13 | One niche can carry many formats; add formats to grow without changing niche. | 3 title-format types each ≥10% of uploads (statement_other 39%, list_countdown 26%, explainer 20%, warning_mistake 5%) | **FOLLOWED** |  |
| P04 | Module 2.2 p.13; Masterclass Ch.23 p.351; Web research §7 p.555 | Avoid repetitive/mass-produced uploads; rotating templates alone is not enough — each video needs distinct substance (inauthentic-content policy). | near-duplicate-script flag on 0% of videos; repeated title word-sets within channel 0% | **FOLLOWED** |  |
| P05 | Module 2.3 Format Arbitrage pp.18-20; Module 2.4 Niche Bending pp.24-26 | Win by transplanting a proven format into a niche that lacks it, or by combining two overlapping niches. | requires historical competitor-format landscape at launch; analyst note in report if a bend is visible | **PARTIALLY FOLLOWED** | a niche bend (personal-finance storytelling → retiree lifestyle/psychology) is visible; launch-time competition unknown. |
| P06 | Module 2.7 Competitor Research pp.28-30; Method 1 p.34 | Study competitors’ top videos, titles, thumbnails, cadence and comments; cover proven topics with original content. | 3% of titles share a word-set with another channel; this channel published first on 3 of 3 | **PARTIALLY FOLLOWED** |  |
| P07 | Method 2 Title Template Injection pp.39-40; 100 Title Formats pp.52-64 | Inject niche topics into proven title psychology families (mystery, downfall, contradiction, revelation, practical, conflict…), but the content must deliver. | 37% of titles match a 100-format family; median PI with 0.88 (n=35) vs without 0.94 (n=59) | **PARTIALLY FOLLOWED** |  |
| P08 | 100 Title Formats p.53 (five-part engine), p.66 scorecard | A strong title names a recognisable subject, a situation, a trigger, a tension and a concrete promise/stakes. | 54% of titles carry a number/$/named entity; median PI with 0.94 vs without 0.93 | **FOLLOWED** |  |
| P09 | 100 Title Formats p.68 (12 mistakes); Masterclass Ch.19 p.345 | Avoid generic subjects, two promises, vague “this/they” openers, ALL CAPS overuse, overstated certainty. | titles with ≥3 ALL-CAPS words 0%; vague 'this/they' opener 1%; double-question 0% | **FOLLOWED** |  |
| P10 | 100 Title Formats p.66 (title+thumbnail one promise), p.68 #11 | Thumbnail should add a complementary clue, not repeat the title. | OCR thumbnail text found on 99%; median share of thumbnail words repeated from title 0.67 | **NOT FOLLOWED** |  |
| P11 | Module 2.7 Thumbnail Teardown p.28 (supporting: DS-000011 Packaging SOP) | Study colour, text amount, faces/expressions, focal object, contrast and template consistency; one clear idea. | thumbnail images 100%; median OCR words 3.0 (OCR undercounts stylised text); face/character detected 15% (cartoon faces often missed) | **FOLLOWED** |  |
| P12 | Engagement Playbook §1 p.265; Masterclass Zone 1 p.320 | The first ~3-5 seconds must create curiosity: question, shock stat, contradiction, mystery, story drop, direct challenge. | opening ~75 words contain question/number/contradiction/story/you-hook in 88%; greeting/channel-intro opening 0% | **FOLLOWED** |  |
| P13 | Masterclass Zone 2 p.320; Engagement §18 p.283 | Within ~5-15 s answer “why should I care?” — connect to the viewer’s money, safety or identity. | explicit stakes/why-it-matters language early in 22%; median PI with 0.74 vs without 0.94 | **NOT FOLLOWED** |  |
| P14 | Masterclass Zone 3 p.320; Ch.23 p.350 | Open at least one curiosity loop before ~30 s and keep it open. | explicit open-loop/promise phrase in first ~150 words of 41% | **PARTIALLY FOLLOWED** |  |
| P15 | Engagement §2 & §7 pp.267, 272 | Use bridging teases / micro-cliffhangers at segment transitions to prevent drop-off. | bridge/cliffhanger phrases per 100 words (median) 0.082 | **FOLLOWED** |  |
| P16 | Engagement §8 p.273 | Precise numbers, dates, named sources and expert quotes signal research and keep sceptical viewers. | data/citation terms per 100 words 0.63; videos naming an institution/source 70% | **PARTIALLY FOLLOWED** | winners use fewer numbers/data than losers; authority comes from anecdote and observed experience, contradicting the idea that more data drops always help. |
| P17 | Engagement §6 p.271 | Second-person address makes the viewer a participant (“if you own…”, “imagine you…”). | 'you/your' per 100 words (median) 5.05 | **FOLLOWED** |  |
| P18 | Engagement §15-16 pp.280-281; Deployment p.284 | Close loops, then future-pace to a next video; strongest CTA right after a payoff, not only at the end. | next-video tease in final ~60 words 75%; any CTA in final 10% 94% | **FOLLOWED** |  |
| P19 | Module 2.3 p.19 (8+ min sweet spot); Web research §8 p.555 | Course: formats should fill 8+ minutes; appendix: 8 min is a mid-roll eligibility rule, length should follow the story. | median long-form length 14.2 min; Spearman(duration, PI) -0.02 — 8+ min is an ad-eligibility rule, not a success rule (PDF p555) | **FOLLOWED** |  |
| P20 | Module 2.7 Posting cadence p.29 | Check upload frequency, consistency, dead periods and growth inflection points. | median gap 2.0 d, gap CV 0.49, longest pause 5 d | **FOLLOWED** |  |
| P21 | Topic Selection Masterclass intro p.33 | “A bad video on the right topic will outperform a great video on the wrong topic” — topic selection is the main lever. | spread of median PI across topics 3.88x (best retirement_accounts_tax) vs across title formats 5.98x (best news_change_update) | **FOLLOWED** | identical script craft produced PI 0.03-0.10 on young-adult budgeting and 20-498 on retiree topics: the strongest within-channel evidence for "topic is the production". |
| P22 | Method 2 warning p.40; 100 Formats p.68 #12; Masterclass Ch.19 p.345 | Title gets the click, content keeps the viewer: the opening must confirm and the video must deliver the title’s promise. | median share of title keywords that appear in the first ~150 spoken words 0.40 | **PARTIALLY FOLLOWED** |  |

## 17. Strengths and weaknesses
Audience pivot executed fast; storytelling hooks with named elderly characters; simple, identity-rich packaging; enormous outliers. Weakness: generic retirement-planning and Social-Security mechanics topics fail; few sources; formula titles risk fatigue.

## 18. Replicable working model
**"Retiree Life Observer"**: one retiree behaviour or dollar reality per video → open with a named older character's surprising quote or a hard number + paradox → 5-10 list items each with a mini-story → comment prompt "which one is you?". Packaging: older illustrated host, "RETIREES + paradox" in ≤4 words, one yellow keyword.

## 19. What to copy
The pivot discipline (follow the first breakout's audience); character-anecdote hooks; identity + paradox titles; avatar aligned with audience age.

## 20. What not to copy
Social Security claiming mechanics and "how much do I need" generic questions (owned by specialists, low PI here); fear-instruction titles ("Or You'll Regret It"); calculation-heavy scripts for a lifestyle audience; unverifiable anecdotes presented as fact (the neighbour stories are narrative devices — UNVERIFIED).

## 21. Missing evidence and limitations
Only Jan–Aug 2026 present; channel subscriber count missing; anecdotes (Steve, Ray) cannot be verified and may be illustrative; 1.08M outlier may include external promotion (UNKNOWN).

- Not available from this dataset for any channel: CTR, impressions, retention curves, traffic sources, subscriber growth history, comments text. Hook timings are word-position estimates (untimed transcripts).

## 22. Final channel diagnosis
1) Success = pivot to an underserved, high-attention audience (retirees) with lifestyle-comparison topics. 2) Advantage: retiree identity storytelling. 3) Model: list/reality videos with anecdote hooks. 4) Topic strategy: exploit breakout topic family relentlessly. 5) Packaging: aged illustrated host + RETIREES + paradox. 6) Script: conversational, anecdotal, fast. 7) Interest: social comparison and reassurance. 8) Failures: young-adult budgeting, mechanics topics, generic "how much" questions. 9) Learn: test audiences early and pivot to the one that responds. 10) Don't copy: invented-sounding anecdotes as evidence. 11) Repeatable: almost everything — no face, no credentials needed. 12) Reputation-dependent: little; breakouts began within a week of the pivot. 13) Lesson: **the same script on the right audience went from 200 views to 1M.**
"If I wanted to build a channel like this, I would study 5V1gCUvdqMs and 7mqI2YgRW1w and replicate: retiree-identity + surprising-behaviour titles, an older illustrated host, a named-character or hard-number paradox in the first sentence, and a list body with mini-stories — and I would keep Social Security mechanics out of it."
