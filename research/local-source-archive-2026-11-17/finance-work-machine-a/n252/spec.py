DIR=__import__('os').environ['FINANCE_WORK']+'/n252/'
VID='kVpJ1Elw680'; NICK='NICK_252'
RANGES=[(0,None)]; DIMS=[1280,720]
FIRST_END='helps clear things up.'
COMPLETENESS_EXTRA='; stored text ends on "...absolutely achievable with the right strategy." with no sign-off; two passages are scrambled out of order (around "Here, many people off guard. That catches..." and "having enough money to survive of security effects...") so sentence order there is unreliable; ASR artefacts "milliondoll", "or geese", "sir charges", "PartB"'
IMAGE_ACQ='REGISTERED_MAXRESDEFAULT_URL_HTTP200_GET;ORIGINAL_BYTES_PRESERVED;NATIVE_AND_320x180_MOBILE_INSPECTED'
CLAIMS=[
("In 2018 the market delivered negative returns.","Back in 2018, the market","Correct: the S&P 500 total return was about -4.4% in 2018 (analyst recall).",[]),
("Withdrawal rates: 3% = $30,000, 5% = $50,000, 4% = $40,000 on $1M; at 3% inflation year two is about $41,200.","up to about $41,200","K02: 1,000,000 x 0.03/0.04/0.05; 40,000 x 1.03 = 41,200. Reproduces.",[]),
("The 4% rule assumes a 50/50 stock/bond portfolio and is designed for 30 years with very low failure probability.","assumes your portfolio is split 50/50","Consistent by analyst recall with Bengen (1994, 50-75% stocks) and the Trinity study; 'extremely low probability' depends on the historical window.",[]),
("The average 65-year-old can expect to live another 18 to 20 years.","the average 65-year-old can expect to","Consistent by analyst recall with SSA period life tables (about 18 years for men, 20-21 for women).",[]),
("The average Social Security benefit is about $1,800 a month ($21,600 a year).","average Social Security benefit","Stale for August 2025: SSA's August 2025 snapshot shows about $2,008 for retired workers (about $1,865 across all beneficiaries). $1,800 was roughly the 2023 retired-worker level.",['SSA1']),
("$40,000 plus Social Security is about $61,600; a couple both receiving benefits about $83,000.","combined annual income of approximately","K02: 40,000 + 21,600 = 61,600; + 2 x 21,600 = 83,200. Arithmetic reproduces, but spousal benefits are often lower than a second full worker benefit.",['SSA1']),
("Replacement of 70-80% of pre-retirement income: $75,000 means $52,000-$60,000.","roughly 70 to 80% of your","K02: 52,500-60,000. Reproduces; common rule of thumb.",[]),
("Retiring at 62 means money may need to last 40 years or more.","Retiring at 62 means your money","Overstated as a planning base: 40 years means living to 102; a 30-35 year horizon is the usual conservative case.",[]),
("Medicare Part B premiums are income-based, with surcharges adding hundreds of dollars a month.","Medicare PartB premiums are incomebased","Correct by analyst recall: IRMAA brackets raise 2025 Part B premiums from $185 to as much as $628.90 a month.",[]),
("Nursing-home care now exceeds $100,000 a year in many areas.","nursing home care now exceeds $100,000","Consistent by analyst recall with Genworth Cost of Care 2024 (national median above $100,000 for semi-private and private rooms).",[]),
("A million dollars gives roughly $40,000 to $60,000 a year assuming you add Social Security.","roughly $40,000 to $60,000 annually","Internally inconsistent: $40,000 is the 4% withdrawal without Social Security; with it the script's own figure is $61,600 (single) or $83,000 (couple).",[]),
]
TITLE='Authentic title "Retire on $1,000,000? The Shocking Reality" frames a negative surprise. The script concludes a million plus Social Security supports a middle-class retirement ("not yacht money, but not cat food money"), so "shocking" overstates. The question form matches the content.'
THUMB='Registered maxresdefault 1280x720 (HTTP 200, real image). White background: the recurring cartoon man (glasses, open mouth) beside a swimming pool and a lounger holding a green-glowing stack of cash, with "$1,000,000 CAN YOU RETIRE?" in heavy black type. At 320x180 the dollar figure and question read clearly. Consistent with the title and the script\'s question.'
SCRIPT='A single-narrator, joke-heavy explainer: hook on hitting $1M, market volatility and 2018, inflation, 3%/4%/5% withdrawal rates, 4% rule assumptions, longevity, Social Security top-up, account taxes, state taxes and geography, health care, replacement ratio, retirement age, alternative income, sequence risk and cash buffer, taxable-account events, a practical $60K budget, IRMAA and long-term care, and a summary. Arithmetic reproduces; the Social Security average is stale, two passages are scrambled, and the summary range contradicts the body.'
BEATS=['Hook: the $1M milestone.','Market volatility; 2018.','Inflation.','Withdrawal rates 3%, 5%.','The 4% rule.','Allocation and 30-year horizon.','Longevity.','Social Security.','Account taxes.','State taxes and geography.','Health care.','Replacement ratio.','Retirement age.','Alternative income.','Sequence risk; cash buffer.','Taxable events.','$60K budget reality.','IRMAA; long-term care.','Summary.']
TOPIC={'analysis':'Realistic income from a $1M retirement portfolio with the 4% rule and Social Security.',
 'audience_problem':'Savers who treat $1M as a finish line without converting it to annual income.',
 'economic_mechanism':'SAFE_WITHDRAWAL_RATE_AND_RETIREMENT_INCOME',
 'demand_type':'MILESTONE_QUESTION_EXPLAINER_HYPOTHESIS','time_sensitivity':'Low: evergreen; benefit levels and premiums are year-specific.',
 'narrative_angle':'A million is not yacht money, but it is not cat-food money either.'}
LESSON='Test an original $1M-retirement explainer that uses the current SSA average, keeps the summary range equal to the body math, and avoids a "shocking" frame for a reassuring conclusion.'
VIRAL='WEAK (0.152x) at about 379 days old against ten peers 371-387 days old; six peers STRONG and four WEAK, so the peer median is high. Comment rate is computed in observed_result; impressions and CTR unknown.'
TREND='Published 28 Aug 2025; no authenticated attention series'
FORMAT='A single-narrator long-form explainer with heavy humour and no composites; retention unverified'
ALTS=['Unknown impressions, traffic sources and subscriber distribution','"Retire on $1M" is a crowded search topic (no data)','Peer cohort contains several unusually strong videos']
EVENT='SSA August 2025 benefit located through a search summary; withdrawal, inflation, Social Security and replacement arithmetic reproduced; 2018 returns, 4% rule, life expectancy, IRMAA and nursing-home costs by analyst recall.'
S='SEARCH_SUMMARY_OF_PRIMARY_OR_REPORTED_SOURCE'
SOURCES=[
 {'source_id':'SSA1','url':'https://www.ssa.gov/policy/docs/quickfacts/stat_snapshot/2025-08.html','source_date':'2025-08-01','access_scope':S,'locator':'SSA Monthly Statistical Snapshot, August 2025','finding':'All-beneficiary average $1,864.87; retired-worker average about $2,008 (reported by secondary sources).','limitations':'Retired-worker row not read directly from the SSA table.','publication_applicability':'BEFORE_PUBLICATION'},
]
K02={'method':'Withdrawal-rate income, inflation step, Social Security sums and replacement ratio','results':{'w3':30000,'w4':40000,'w5':50000,'year2_at_3pct':41200,'single_total':61600,'couple_total':83200,'replace_low':52500,'replace_high':60000,'ssa_retired_aug2025':2008},'limitations':'Uses the script\'s $1,800 benefit for its sums; current average is higher.'}
LIMITS='No audio, video, private analytics or native Excel verification; one source via search summary; most claims by analyst recall. No paid purchases.'
