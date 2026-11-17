from pathlib import Path
import json
r=Path(__file__).parent;out=r.parent/'MACHINE_A_NICK_165_RETIREMENT_WITHDRAWAL_REVIEW.md'
claims=json.loads((r/'transcript-claim-inventory.json').read_text())
head='''# Machine A — NICK_165 retirement statistics and withdrawal review

**MACHINE_A_NICK_165_RETIREMENT_REVIEW_COMPLETE**  
Dated 2026-10-23, Asia/Karachi. Video SsHQ-TtXhRQ, *Why a $70,000 Truck Costs $1M in Retirement*, published 2026-02-11. One-agent, external, read-only independent research. Machine B remains sole canonical Finance writer.

## 1. Executive summary

The transcript explicitly invokes the **4% withdrawal rule** using **$500,000**, not an illustrative $1M portfolio. Its first-year arithmetic, $20,000 annually or $1,666.67 monthly, is correct. Its promise of that income for life without using principal is incorrect. The published audit already identifies that error; this review adds original research receipts and a precise policy definition, not a newly discovered audit reversal.

Additional evidence establishes important statistical qualifications: $87K is not established as the mean retirement wealth of all Americans; the familiar SCF statistic is a conditional family median. The $185K figure is a conditional retirement-account median for families whose reference person is 55–64, not all individuals of those ages. The $1.26M figure is a 2025 survey-reported savings expectation, not a measured universal requirement. Subtracting these different quantities does not establish a typical person's measured $1M funding deficit. The creator provides no source citations in the stored text, so matching numbers to plausible source series is an evidence-based identification, not proof of which source he used.

One additional small analyst arithmetic discrepancy surfaced: published script claim_audit[4].assessment says about $42,985 for 36 end-month deposits of $1,076 at 7% nominal monthly compounding. The result is **$42,964.79**, about **$42,965**. The video's rounded $43K remains reasonable. This is separate from the previously identified $271,355/$271,377 typo.

The broader opportunity-cost mechanism and the existing conditional headline assessment survive. No change to the previously validated $618K–$672K financed illustration follows from this retirement review. Future accumulated wealth and a retiree's subsequent spending policy are separate calculations.

## 2. Published checkpoint and provenance

Host **Ghilmans-Laptop.local**; repository `/Users/ghilmankhan/workprojects/youtube-intelligence-os`; branch `research/finance-economics-intelligence`. Local HEAD, freshly read published remote Finance HEAD and PR #36 HEAD all equal **7e70f061aae849e9929b531c4bc855b23edda179**. PR #36 was open, base **08e719264e31ecd82de24f8eeb8f065c08359fe5**, updated 2026-10-22T09:00:12Z. No advanced published NICK_165 version existed at preflight; no fetch, synchronization or branch switch was needed. GitHub connector returned 404; authenticated read-only `gh api` supplied PR metadata and `git ls-remote` supplied the remote SHA. This establishes published state, not Machine B's unpublished filesystem/session state. No writer ownership change was attempted.

Tracked status was clean. Existing untracked `finance-short-02-visual-calibration/`, `productions/` and `research/casually-finance-script-intelligence/` were preserved. Live preflight usage: **2% five-hour, 0% weekly**. No context/compaction warning was exposed; no numeric context-capacity meter was available. Paid balance 0; reset credits untouched. No purchases, suites, workbook regeneration, commits, pushes, PR mutations, branches, worktrees, clones or NICK_166 execution.

Read the complete registered transcript from `data/catalog/youtube_channel_registry.db`, opened `mode=ro&immutable=1`, `transcripts.youtube_video_id='SsHQ-TtXhRQ'`. 18,252 characters; SHA-256 **697d0545e42e6b2a060a1dda252f3c0a75c7d4aefb3d933f3c324b085c8f1bdd**, matching the published receipt and prior external snapshot. Auto-generated untimed captions; audio remains unverified. The four previous named Machine A reports were read for continuity; their completed vehicle investigations were not reopened. Full individual audit and receipts were read and byte-matched to HEAD Git objects. Relevant source paths:

- `research/finance-economics-intelligence/audit-batches/NICK_165.json`
- `research/finance-economics-intelligence/audit-batches/NICK_165_READ_RECEIPTS.json`
- Registered archive member: `data/extracted/channel-data/DS-000022/packages/nick-invests/NickInvests_Transcripts_363_Videos.zip::200_SsHQ-TtXhRQ_Why_a_70000_Truck_Costs_1M_in_Retirement.txt`

External evidence is in the sibling `retirement-evidence/` folder. `registered-transcript.txt`, exact claim inventories, source originals, extracted text, selected statistical cells and `calculations.json` provide reproducibility. `preflight-hashes.json` and `final-checks.json` record preservation. No source evidence was edited.

## 3. Exact transcript claims and attribution

Locations below are **zero-based, start-inclusive/end-exclusive character offsets in the registered text**, not invented timestamps. Quotes collapse whitespace only; original line breaks and exact slices are retained in `transcript-claim-inventory.json`. Each material retirement assertion is included, including repeated guarantees and retirement-age rhetoric. A compound quote can have multiple component classifications explained in §§4–9.

'''
notes={
'T01':'Headline outcome is conditional; no universal million-dollar loss is established.',
'T02':'Accumulation arithmetic mostly approximate; “today\'s dollars” needs an explicit real-return definition. Funding comparability was already reviewed; no loan recomputation here.',
'T03':'Illustrative ages 62/74 are not a measured average retirement age or an established causal consequence.',
'T04':'$43K is a reasonable rounded account value; gains versus contributions and the claimed wealth gap were already distinguished in prior review. New analyst rounding discrepancy is addressed below.',
'T05':'Cost-difference and replacement inputs remain conditional. 7% real and 10% nominal describe different purchasing-power units; the dollar range cannot be treated as comparable real retirement wealth.',
'T06':'“Average” $87K is unverified as a mean of all individuals. See the separate SCF median and Northwestern Mutual mean candidates below.',
'T07':'Approximate arithmetic under end-year contributions; savings input is not independently verified here.',
'T08':'Fails inherited 7%/30-year lump-sum convention; already flagged, no new vehicle finding.',
'T09':'Fails inherited 7%/30-year lump-sum convention; already flagged.',
'T10':'Investment outputs fail the same convention; total is a sum of overstated components. Configuration findings remain in previous reports.',
'T11':'Approximate investment arithmetic; underlying annual cost gap remains unverified. “Became a millionaire” is a hypothetical outcome.',
'T12':'Multipliers depend on each dollar\'s timing and return; they are not universal. A $70K gross expenditure is not automatically $70K incremental investable savings.',
'T13':'A half-million retirement-wealth loss is not established for every buyer; happiness wording is outside this review.',
'T14':'$87K/$185K require family/account-holder denominators. $1.26M is a stated expectation; $1M short is not an observed matched-population deficit.',
'T15':'Age 65/40-year career and “stayed broke” are rhetoric, not a sourced retirement-age distribution.',
'T16':'Arithmetic MATHEMATICALLY_REPRODUCED for year one; lifetime and principal guarantees MISINTERPRETED_WITHDRAWAL_RULE / CONFIRMED_ERROR. Universal planner recommendation is UNSUPPORTED_OR_UNVERIFIED.',
'T17':'Restates the incorrect lifetime guarantee; lost future capital is also conditional.',
'T18':'No defined duration or common unit establishes the asserted $2-of-income exchange rate.',
'T19':'Approximately true for a one-time $1K invested for 40 years at effective annual 7%, before tax/fees; not for all purchases or later-career dollars.',
'T20':'Specific six-year deposit stream can exceed $900K under the monthly convention; not a guarantee or a matched transportation comparison.',
'T21':'Repeats the conditional headline; separate gross investment counterfactual.',
'T22':'13×$35K=$455K is correct; 13-car population average and $3.2M timing schedule unverified. No assumption that all lifetime spending was available on day one.',
'T23':'No model proves that one payment causes work at 67.',
'T24':'Retirement at 55 after 30 years implies start age 25; no spending, longevity or asset/liability plan establishes the promised beach/retirement outcome.'}
parts=[head]
for c in claims:
 parts.append(f"**{c['id']} · [{c['start_char_inclusive']},{c['end_char_exclusive']}) · {c['classification']}**\n\n> {c['display_wording']}\n\n{notes[c['id']]}\n\n")
parts.append('''**Absent claims:** Social Security benefit levels, benefit replacement rates, a measured national mean/median retirement age, a specified retirement stock/bond allocation, a 30-year withdrawal horizon, inflation-indexed withdrawals and a withdrawal success probability are **NOT_PRESENT_IN_TRANSCRIPT**. In particular, Social Security has zero textual occurrences. Those details below are independent comparison evidence, not additional creator claims. A $1M retirement-income portfolio example is not supplied by the creator; the withdrawal example is $500K. References to $1M elsewhere concern accumulation/headline wealth.

**Published analyst wording:** `NICK_165.json:/reviews/0/script/claim_audit/16` expressly describes the $500K/4% claim. Its assessment says: “The arithmetic is correct for the first year, but the guarantee is false. A withdrawal rule is a planning heuristic subject to horizon, allocation, fees, inflation, taxes, market sequence and spending changes; withdrawals can reduce principal.” This is analyst commentary, independently supported here. The full analyst-language inventory, including every matching exact string and JSON pointer, is `audit-retirement-language-inventory.json`; the complete immutable checkpoint audit is alongside it. No withdrawal claim has been imported from NICK_163.

Other material analyst statements: claim_audit[3] gives the $55K age-path and nominal/real qualification; [4] gives the ~$42,985 three-year account estimate; [5] gives ~$1.938M/~$4.085M for 35-year monthly contributions; [10] and [13] give annual-contribution future values; [11]–[12] correct overstated lump/fuel values; [14] qualifies the multiplier; [18] gives ~$1.029M for six-year contributions followed by growth; [19] rejects unscheduled lifetime-cost compounding; [20] contains the conditional headline and $618K–$672K illustration. These are analyst calculations/interpretations, not extra video quotations. Their classifications and inputs are addressed in §8. The audit's script analysis calls retirement-balance figures unsourced; that caution is supported, with more precise evidence now available.

## 4. Retirement statistic verification and denominator checks

**S1 — Federal Reserve 2022 SCF, released October 18, 2023.** The [original report](https://www.federalreserve.gov/publications/files/scf23.pdf), Table 3 (PDF p21, printed p15), reports 54.3% of U.S. families holding retirement accounts and a conditional median $86,900, in 2022 dollars. The mean is roughly $334K, not $87K. Appendix A (PDF p39) defines family/primary economic unit; age is the reference person's age. Most interviews were May–December 2022; 25% occurred January–April 2023. Balances concern accounts, not all financial assets, housing, capitalized Social Security or defined-benefit pension rights. The sample includes working and retired families; it is not a worker-only or retiree-only individual statistic. These details fit the video's approximate median number only after narrowing its population. **DENOMINATOR_MISMATCH** as spoken; numeric magnitude **CONDITIONALLY_SUPPORTED** for holders.

The latest pre-upload SCF results were the 2022 edition; using them in February 2026 is legitimate if labeled. The live [SCF portal](https://www.federalreserve.gov/econres/scfindex.htm) now advertises a 2025 edition released **October 9, 2026**. That edition was unavailable to the creator. Current downloads also re-express historical survey balances in 2025 dollars; they must not silently replace original 2022-dollar estimates.

**S2 — Age 55–64, $185K.** The [Department of Labor's January 29, 2024 original governmental publication](https://www.federalregister.gov/documents/2024/01/29/2024-01208/automatic-portability-transaction-regulations), discussion around footnote 53, explicitly reports only **57%** of households headed by 55–64-year-olds held retirement savings accounts in 2022 and the median among those accounts/households was **$185,000**. This pre-upload corroboration prevents treating the number as invented. It does not describe all 55–64 individuals or only retirees. **CONDITIONALLY_SUPPORTED** number; **DENOMINATOR_MISMATCH** wording.

A separate retrospective extraction from the Fed's [current nominal historical tables](https://www.federalreserve.gov/econres/files/scf2025_tables_internal_nominal_historical.xlsx) confirms 2022 Table 6, sheet `Table 6 22 %s & medians`: H6=54.3%, H22=57%, H80=87 ($thousands), H96=185 ($thousands), header B78 says conditional on holding. This is a **2026 retrieval/revision**, not authenticated upload-day workbook bytes. Its $87K versus original PDF $86.9K rounding/revision is immaterial; do not manufacture a substantive contradiction from it. Selected cells are preserved externally. Current real-dollar chart data show different historical numbers because of rebasing; those are not 2026 observed retirement balances.

**S3 — Alternative provenance for “average $87K.”** [Northwestern Mutual's October 25, 2022 release](https://news.northwesternmutual.com/2022-10-25-Northwestern-Mutual-Study-Finds-Americans-Now-Believe-They-Will-Need-1-25-Million-for-Comfortable-Retirement) reports mean self-reported savings **$86,869**, rounding to $87K, and a contemporaneous expected need of $1.25M. Harris Poll fieldwork February 8–17, 2022; 2,381 U.S. adults 18+, online, weighted. This is a plausible match to the earlier “average” sentence, but the stored text does not identify it. It cannot also substantiate the later median claim. Release-level reporting does not fully establish the balance-item response base or treatment of missing/zero answers; do not invent it. **HISTORICAL_VINTAGE_MISMATCH** if presented as a current 2026 mean or paired as a same-survey observation with a 2025 target; actual source attribution **UNSUPPORTED_OR_UNVERIFIED**.

**S4 — $1.26M.** [Northwestern Mutual's April 14, 2025 release](https://news.northwesternmutual.com/2025-04-14-Americans-Believe-They-Will-Need-1-26-Million-to-Retire-Comfortably-According-to-Northwestern-Mutual-2025-Planning-Progress-Study) and [original Work & Retirement tables](https://filecache.mediaroom.com/mr5mr_nwmutual/179133/2025%20P%26P%20Wave%20II%20-%20Retirement%20and%20Work%20-%20FINAL.pdf), pp2–3, trace the number to survey answers about expected savings needed. Fieldwork January 2–19, 2025; 4,626 U.S. adults 18+ including a high-net-worth oversample, weighted; question Q54 reports qualified-response n=3,934. It is a mean dollar expectation, not a median balance, actuarial adequacy estimate, universal target or inflation-standardized 2022 amount. Mixed ages/employment statuses are not specifically the SCF 55–64 account-holder cohort. **VERIFIED_PRIMARY_SOURCE** as a stated expectation; the video's universal “They need” formulation is **UNSUPPORTED_OR_UNVERIFIED**. The PDF's stray debt-summary reference to February does not supersede its explicit January methodology for this survey.

**S5 — Readiness cross-check, not video claims.** [Federal Reserve SHED 2024 savings section](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-savings-and-investments.htm), Table25, reports **35% of non-retired adults** perceived their savings as on track; 61% had a tax-preferred account and 21% a DB pension. These overlap and must not be summed. [Methodology](https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-description-survey.htm): October18–31,2024 U.S. adult survey; [release May28,2025](https://www.federalreserve.gov/newsevents/pressreleases/other20250528a.htm). Perception is not observed wealth adequacy. SHED's May2026 report is post-upload and was not used to judge the creator.

[EBRI/Greenwald original 2025 report](https://www.ebri.org/docs/default-source/rcs/2025-rcs/2025-rcs-release-report.pdf?sfvrsn=f5e3042f_3), released April24,2025, pp2/4/7: **67% of workers**, separately **78% of retirees**, were somewhat/very confident about comfortable retirement. Online fieldwork January2–February3,2025, U.S. ages25+, general sample2,047 (1,042 workers/1,005 retirees), plus720 Black respondents oversampled; weighted population results. Those are distinct populations and confidence outcomes, not national retirement-account medians or contradictions of SHED's differently worded measure. Neither percentage appears in NICK_165.

**S6 — Social Security absence and context.** The [SSA statistical-publications index](https://www.ssa.gov/policy/docs/statcomps/) was checked as a starting point. No transcript benefit claim needs correction. The [2026 COLA fact sheet](https://www.ssa.gov/cola/factsheets/2026.html), associated with [October24,2025 announcement](https://www.ssa.gov/news/en/press/releases/2025-10-24.html), estimates January2026 average retired-worker benefits **$2,071/month**, versus **$3,208** for an aged couple both receiving benefits. These are estimated nominal group averages, not observed individualized guarantees, medians, all-retiree household income or portfolio withdrawals. The input COLA compares Q3 2024/Q3 2025 CPI-W. Do not append either average to the creator's hypothetical income as if it were his buyer's entitlement. **NOT_PRESENT_IN_TRANSCRIPT**, independently **VERIFIED_PRIMARY_SOURCE** context only.

## 5. Four-percent rule: original and later independent evidence

[Bengen, October1994, “Determining Withdrawal Rates Using Historical Data”](https://obj.portfolioconstructionforum.edu.au/articles_perspectives/retailinvestor.org_pdf_Bengen1.pdf), Journal of Financial Planning pp171–180: initial portfolio percentage followed by inflation-adjusted dollar withdrawals; U.S. historical stock/intermediate-Treasury returns and inflation, using Ibbotson data. His initial illustrations use 50/50, and he discusses 50%–75% stocks. The minimum planning criterion is 30 years, not perpetuity. Figures show retirement starts1926–1976; historical portfolio longevity is the outcome. This is not a forward probability guarantee. The conclusion (p179) explicitly stops reapplying the original percentage after year one. Tax-deferred assets are assumed in the allocation discussion (p177). No universal net-of-tax/management-fee income promise follows. Original PDF is preserved from the supplied primary-document mirror; index/appendix OCR is imperfect, and the complete underlying licensed Ibbotson series was not acquired. No claim to have rerun Bengen's entire backtest.

[Cooley, Hubbard and Walz, February1998 original AAII paper](https://athenaconsulenza.it/wp-content/uploads/2025/05/Retirement-Savings-Choosing-a-withdrawal-rate-that-is-sustainable.pdf), pp16–21, independently evaluates annual U.S. stock/corporate-bond returns1926–1995, 15/20/25/30-year horizons and several allocations. It distinguishes fixed nominal and CPI-adjusted spending. Table3's inflation-adjusted 4%/30-year historical success is about95% at50/50 and98% at75/25, not a guaranteed100%. “Success” means positive ending value, not intact initial capital. Taxes/transaction costs are excluded. This is an original paper on a third-party mirror, not an official publisher archive. Its bond series and sample differ from Bengen's; different percentages are not proof one study is mathematically wrong.

[Morningstar, December3,2025 comparison](https://www.morningstar.com/retirement/whats-safe-retirement-withdrawal-rate-2026) was available before upload: **3.9%** maximum base-case starting rate for fixed-real spending over30 years at90% modeled success, portfolios30%–50% equities. The [original 2025 research PDF](https://www.morningstar.com/content/cs-assets/v3/assets/blt9415ea4cc4157833/bltb73b87c5d0c70ead/692f43f57737a31596684522/working_file_11.19_FINAL_REVISE.pdf), p7, uses1,000 simulated return paths; >=900 must fund scheduled withdrawals and finish positive. Even a tiny positive terminal balance qualifies. It uses forward-looking assumptions (inputs dated September30,2025), permits consumption of capital, and excludes taxes/expenses. Flexible-spending strategies have different tradeoffs. The article initially returned403; search-indexed full publisher text and the directly downloaded original report supplied the evidence. A crawl's “published” relative-age label is not a replacement for the document/article date.

## 6. Historical source dates and fair-vintage rule

All above original editions were available by2026-02-11, except the explicitly labeled current SCF extraction/portal state. Access date throughout:2026-10-23. For interview data, survey year, publication year and dollar base are separate. October2023 release of2022 SCF does not make its balances2023/2026 nominal wealth. January2025 expectations are not2022 account balances. An older last-available dataset is not an error merely because it is old. Current portal revisions do not prove upload-day webpage content. Later SHED/SCF releases were not substituted in the creator's knowledge set.

## 7. What the policies and risk conditions actually mean

The following is this review's mathematical interpretation, not additional transcript wording:

| Policy | Formula / meaning | Implication |
|---|---|---|
| Conventional fixed-real starting rule | W1=.04×P0; Wt=W1×product(1+inflation) for subsequent years | Dollar amount follows inflation, not current portfolio percentage |
| Constant fraction of current assets | Wt=.04×Pt immediately before withdrawal | Spending falls/rises with the account; does not promise a fixed real income |
| Fixed nominal dollars | Wt=$20,000 every year | Purchasing power falls with positive inflation |
| Dynamic spending | A specified rule changes dollars after market/spending conditions | Must disclose guardrails, cuts, caps and decision timing |
| Income-only capital-preservation promise | Spend only an actually available income yield under stated constraints | Not implied by a total-return withdrawal percentage |

Initial balance is the account at retirement, not the vehicle price or the current value of a future balance. The initial withdrawal amount, year-one monthly equivalent and later inflation-adjusted amounts are different objects. A total-return portfolio can fund withdrawals by dividends, interest and selling holdings; remaining principal can fall. Sequence risk means losses near the start can require selling more units before recovery. Average return alone cannot establish longevity. Volatility, inflation, horizon, allocation, taxes, fees, spending shocks and investment behavior affect outcomes. A30-year survival criterion cannot promise funding to an unknown death date, especially for retirement at55. Modeled90% success is conditional on the model, not a guaranteed real-world90% probability or an income contract. Success does not guarantee terminal capital, nominal principal or real principal. No universal allocation/rate fits every retiree.

## 8. Independent numerical reproductions

These are accumulation calculations only until explicitly labeled withdrawal examples. All savings inputs are transcript assertions, not newly verified vehicle costs. No amortization, resale/configuration or previously resolved loan-equity finding was recomputed. Exact machine-readable results: `calculations.json`.

Let L(P,r,n)=P(1+r)^n for a time-zero lump; A(C,r,n)=C[(1+r)^n−1]/r for end-year contributions; M(C,j,N)=C[(1+j)^N−1]/j for end-month deposits. All below exclude taxes, fees and return volatility.

| Actual claim / inputs | Independent result | Classification / interpretation |
|---|---:|---|
| $55K at effective annual7%,10/20/30/40y | $108,193.32 / $212,832.65 / $418,674.03 / $823,595.18 | MATHEMATICALLY_REPRODUCED; video approximates $108K/$212K/$417K/$820K. Today's dollars only if7% real |
| $1,076 monthly,36 deposits,j=.07/12 | $42,964.79; contributions$38,736; gain$4,228.79 | MATHEMATICALLY_REPRODUCED. Video$43K fair; analyst~$42,985 needs small correction |
| $1,076 monthly,420 deposits,j=.07/12 or.10/12 | $1,937,934.75 / $4,085,182.54 | CONDITIONALLY_SUPPORTED; second does not reproduce$3.8M under this convention |
| Same420 deposits,monthly rate=(1+annual rate)^(1/12)−1 | $1,841,481.07 at7%; $3,657,099.13 at10% | Convention sensitivity, not source verification. Do not infer a unique intended convention |
| $14,900 end-year,7%,30y | $1,407,465.72 | MATHEMATICALLY_REPRODUCED approximate$1.406M |
| $35,650/$23,000/$42,000 lumps,7%,30y | $271,376.89 / $175,081.87 / $319,714.71 | CONFIRMED_ERROR in video's$679K/$439K/$801K, already flagged |
| $2,400 end-year,7%,30y | $226,705.89; plus$42K lumpFV=$546,420.60 | CONFIRMED_ERROR in$715K/$1.516M, already flagged |
| $11,800 end-year,7%,30y | $1,114,637.28 | MATHEMATICALLY_REPRODUCED approximate$1.113M |
| $1 one-time,7%,30/40y | $7.612255 / $14.974458 | CONDITIONALLY_SUPPORTED multiplier; timing essential |
| $70K/$18K time-zero,7%,40y | $1,048,212.05 / $269,540.24 | Gross illustrative FVs; not comparable net transportation savings |
| $1K time-zero,7%,40y | $14,974.46 | Approximately$15K; not every purchase dollar |
| $1,076 monthly for72 months then408 months no deposits,j=.07/12 | $1,029,448.77 at65 from age25 | CONDITIONALLY_SUPPORTED >$900K; contributions end at31, then34y growth; no40y contribution stream |
| $1,076×72 | $77,472 | Rounded$77,500; gross contributions, not an independent retirement-loss estimate |
| 13×$35K | $455,000 | MATHEMATICALLY_REPRODUCED;13-car population assertion unverified |
| $455K time-zero,7%,30/40y | $3,463,576.04 / $6,813,378.32 | Not a reproduction of unspecified$3.2M lifetime schedule |
| $1.26M−$185K; or−$87K | $1,075,000; $1,173,000 | MATHEMATICALLY_REPRODUCED subtraction; DENOMINATOR_MISMATCH as adequacy inference |

**Previously completed findings:** the table restates investment conventions relevant to retirement, without reopening vehicle inputs. Existing $271,355 typo remains in the previous handoff. $618,136–$671,788 is carried forward from the completed financed-comparison review, not recomputed here. Its $5K/$8K/$10K alternative resale figures and constant monthly return remain illustrative assumptions.

**New withdrawal arithmetic using the creator's actual $500K example:**

- W1=.04×500,000=$20,000; W1/12=$1,666.6667, reasonably rounded$1,667. This is a first-year gross draw, not guaranteed net spendable income. No assumption of a constant7% return during retirement is needed or justified.
- Own explanatory inflation assumption3%, not supplied by video: Wt=20,000×1.03^(t−1). Year2=$20,600; year10=$26,095.46; year30=$47,131.31. Constant$20K nominal is a different policy. The inflation-adjusted sequence's starting year is retirement, not the accumulation start date.
- Own constant-percentage example: if the next prewithdrawal account value is$400K,4%=$16K, monthly equivalent$1,333.33. It is not the fixed-real$20K-based policy.
- Own capital-loss illustration, beginning-year$20K withdrawal then−20% return: (500,000−20,000)×.8=$384,000. Principal is plainly not protected.
- Own sequence demonstration, beginning-year$20K withdrawals, two years, no inflation/taxes/fees: returns−20%,+25% finish$455,000; +25%,−20% finish$464,000. Both return sequences have the same product1.00 before withdrawals. Different outcomes demonstrate why a long-run accumulation average cannot guarantee withdrawals.
- A3.9% comparison on$500K gives$19,500/year or$1,625/month initially. The$500 annual difference from4% is model-specific, not a required universal correction to every planner's rate. The error to correct is the guarantee, not simply replacing4 with3.9.
- The “$2 of retirement income for every dollar” claim has no defined income duration. Own age25-to65 example at effective annual7%: $1 becomes$14.97446 capital, which at4% supports only a conditional **$0.59898 first-year annual withdrawal**, or$0.04991 monthly equivalent, per original dollar. Lifetime cumulative income is a different metric needing a horizon and spending/return assumptions. Do not label it a demonstrated2:1 exchange rate.

**Lifetime schedule:** $3.2M/$455K implies28.8301 years if all spending were one lump, a timing assumption the video does not supply. Own illustration only: thirteen$35K purchases at ages25,28,…61, compared at65, give sum[35,000×1.07^(40−3k),k=0..12]=$2,649,158.41 before alternative transportation costs. This does not replace the video's claim with a forecast; it shows that a schedule matters. The original audit correctly calls the$3.2M unreproducible as stated.

**Purchasing-power treatment:** FV_real=FV_nominal/(1+inflation)^years; r_real=(1+r_nominal)/(1+inflation)−1. If7% is nominal and inflation3%, the real annual rate is3.8835%, not7%. A future nominal$500K's$20K initial draw is in retirement-year dollars; it is not automatically today's grocery budget. Conversely, labeling7% a real accumulation rate requires explicit real contribution units and a much stronger assumption. Do not add an inflation discount twice. Taxes/fees and retirement-spending risks remain separate from this conversion.

## 9. Supported claims and incorrect or unsupported statements

Supported: a real reduction in incremental vehicle spending can increase investable resources; the actual$500K first-year withdrawal arithmetic; qualified SCF conditional medians; Northwestern Mutual's reported expectation; several conditional FV examples. These findings do not establish actual saving behavior, exact future returns, identical lifestyles or a buyer's ability to retire at55/62/65.

Incorrect/unsupported: lifelong principal-preserving4% income; a universal safe rate recommendation; mean/median/population substitutions; a universal$1.26M need; an observed$1M national shortfall inferred from unmatched sources; the unexplained2:1 income ratio; an unscheduled$3.2M lifetime FV; and retirement ages portrayed as determined by a single truck choice. Existing investment overstatements remain as already flagged. Lack of a matched definition is not evidence that no American has a$1M shortfall or that financial insecurity is fictitious.

## 10. Effect on NICK_165's original conclusions

The headline remains **conditional**, not proved as a universal invoice for a truck. The published audit's skeptical retirement-withdrawal conclusion is strengthened by source receipts. The new statistical findings justify a narrow explicit claim assessment; they do not overturn its existing caution or its nominal-versus-real distinction. No accepted return or resale input in the separate$618K–$672K illustration is changed here. Accumulating that sum never guaranteed any particular lifelong income stream.

## 11. Minimal canonical correction recommendations

Machine B may add a retirement-statistics claim entry identifying the$87K/$185K account-holder family denominators and the mean/median inconsistency; label the$1.26M as a2025 self-reported expectation and the implied deficit as an unmatched inference. Attribute source candidates with uncertainty. Add dated SCF/DOL/Northwestern Mutual receipts, retaining survey year/dollar basis.

Keep the existing four-percent error finding. Strengthen its source receipt with Bengen1994 and pre-upload Morningstar2025; specify first-year percentage then inflation-adjusted dollars, finite horizon, risky total-return draw and no principal/lifetime guarantee. No need to insert Social Security into a transcript that never mentioned it, or to prescribe3.9% universally. Add one sentence flagging the undefined$2-of-income-per-dollar conversion if desired.

Correct only the newly confirmed analyst estimate in claim_audit[4]: **about$42,985 → about$42,965** for the explicitly end-month7%/12 convention. Keep the video's approximate$43K classification. Do not reopen the previously prepared loan/configuration/$271,377 correction batch. No competing patch was made.

## 12. Additive Machine B handoff

Checkpoint **7e70f061aae849e9929b531c4bc855b23edda179**, NICK_165/SsHQ-TtXhRQ; remote and PR36 matched. Review this external report plus `retirement-evidence/transcript-claim-inventory.json`, `audit-retirement-language-inventory.json`, `scf-selected-cells.json`, `calculations.json` and archived source manifest. Reconcile against your latest unpublished revision first.

| Additional item | Evidence / proposed acceptance action |
|---|---|
| Statistical-definition gap, newly substantiated | T06/T14: distinguish conditional family account medians from all-American mean/wealth; qualify$1.26M expectation and unmatched shortfall. S1–S4 source receipts. No universal replacement “true retirement need” number |
| Undefined income conversion, newly isolated | T18:$2 retirement income per current dollar lacks horizon/units. Mark unsupported as a universal conversion, not a new guaranteed ratio |
| Small analyst arithmetic discrepancy, new | `/reviews/0/script/claim_audit/4/assessment`: 36 end-month$1,076 deposits at.07/12=$42,964.7884, not~$42,985. Correct prose to~$42,965; video's$43K remains approximate |
| Existing withdrawal finding, evidence enrichment only | T16/T17 already correctly criticized. Append original research and inflation-policy/horizon clarification; do not call this a newly discovered canonical error |

Machine B alone accepts/rejects canonical findings, edits the individual audit, appends source/correction provenance and updates/validates affected JSONL/workbook through its normal workflow. This review neither edits those artifacts nor authorizes merge/closure of PR36. No cross-chat message was sent.

## 13. Unresolved evidence gaps

Creator's actual citations; original audio/on-screen qualifications; exact response-base/missing-value handling for Northwestern Mutual2022 balance question; authenticated February2026 SCF workbook bytes; full licensed Bengen input series/backtest replication; individual tax status, fees, allocation, inflation path, benefit entitlement, spending needs and lifespan. Current historical SCF tables were explicitly segregated from pre-upload documents. These gaps limit source attribution and individualized outcome claims; they do not block the specific denominator and guarantee findings. No retirement-age distribution was inferred from hypothetical ages.

## 14. Next safe independent Machine A task

After owner selection, a bounded external **NICK_165 source-receipt reconciliation** against Machine B's eventual published correction checkpoint: check that accepted retirement definitions and policy wording propagated consistently into audit/JSONL/workbook text, without regenerating or editing them. Until that checkpoint exists, no production action is needed. Remain read-only, do not start NICK_166, and do not reopen the completed vehicle investigations.

## 15. Preservation and verification

All protected files must match preflight SHA-256 at completion; exact final command outcomes are in `retirement-evidence/final-checks.json`. External source originals are hashed in `artifact-hashes.json`; attempted access failures are recorded separately and not represented as successfully archived evidence. The reviewer did not claim to observe Machine B's live sessions or unpushed work.
''')
out.write_text(''.join(parts));print(out);print('words',len(out.read_text().split()))
