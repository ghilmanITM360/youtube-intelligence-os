DIR=__import__('os').environ['FINANCE_WORK']+'/n232/'
VID='epr30mUtEMw'; NICK='NICK_232'
RANGES=[(0,None)]; DIMS=[1280,720]
FIRST_END='pretty close to it.'
COMPLETENESS_EXTRA='; stored text ends on "Don\'t let that be the end of the story." with no sign-off; two sentences end mid-thought ("Americans seem to instinctively", "wondering how"); the 55-64 median is given as $320,700 then $364,500; Derek\'s salary shifts between $115,000 combined, $75,000 and $82,000 across benchmarks'
IMAGE_ACQ='REGISTERED_MAXRESDEFAULT_URL_HTTP200_GET;ORIGINAL_BYTES_PRESERVED;NATIVE_AND_320x180_MOBILE_INSPECTED'
CLAIMS=[
("Fed SCF 2022: mean net worth $1,063,700 vs median $192,700, a 5.5x gap.","That is the official Federal Reserve figure","SCF22: consistent with the 2022 SCF (Fed Bulletin, October 2023). K02: 1,063,700 / 192,700 = 5.52. Correct.",['SCF22']),
("Median net worth by age: under 35 $39,000; 35-44 $135,600; 45-54 $247,200; 55-64 $364,500; 65-74 $409,900; 75+ $335,600.","Under 35, median net worth $39,000","SCF22: verified within rounding (secondary tables show $39,040, ~$135,300, $364,500). The script first states 55-64 as $320,700, then $364,500; only the second matches.",['SCF22']),
("The next SCF lands late 2026; 2022 is the most current.","The next one lands late 2026","Consistent: the 2025 survey results are expected in autumn 2026 (analyst recall); correct at the 15 March 2026 upload.",['SCF22']),
("Top 1% hold 31% of wealth, top 10% 67%, bottom half 2.5%.","The top 1% of households controls 31% of all wealth","Consistent by analyst recall of Federal Reserve Distributional Financial Accounts (2025).",[]),
("Fidelity targets 3x salary by 40, 6x by 50, 8x by 60.","Fidelity says you should have three times your salary saved by 40","Consistent by analyst recall of Fidelity guidelines. Derek's 6x figure ($490,000) uses $82,000 while the scene says $115,000 combined, and the 8x example switches to $75,000, so the comparisons are internally inconsistent.",[]),
("Average new car payment $748; $8,976 a year; auto loans crossed $1.67 trillion.","The average new car payment in 2026 is $748 a month","K02: 748 x 12 = 8,976. Payment and NY Fed auto balance (~$1.66T late 2025) consistent by analyst recall.",[]),
("Student debt $1.84 trillion; average balance $39,500; rate 6.53%; payment ~$440.","$1.84 trillion in total debt","Not checked; federal portfolio about $1.7T plus private loans makes $1.8T plausible.",[]),
("Median homeowner net worth ~$400,000 vs renter $10,400, a 38x gap.","The median net worth of a renter is $10,400","Consistent by analyst recall of SCF 2022 ($396,200 vs $10,400). K02: 38.1x. Correct.",[]),
("Auto-enrolment plans average $158,000 vs $107,000 for opt-in plans.","average balances of $158,000","Not checked; source not named.",[]),
("$7,500 a year at 8% from 25 gives ~$1.94M at 65; from 35 ~$875,000.","you'll have roughly $1.94 million by 65","K02: $1,942,924 from 25 (correct) and $849,624 from 35 (overstated by ~$25,000).",[]),
("2026 limits: 401(k) $24,500, IRA $7,500, catch-up $8,000, ages 60-63 super catch-up $11,250 (extra $3,250 a year, $13,000 over four years).","Max the 401k at $24,500","Correct by analyst recall of IRS 2026 limits (cross-referenced NICK_223). K02: 3,250 x 4 = 13,000.",[]),
("Delaying Social Security from 62 to 70 raises the benefit by about 76%.","increases your monthly benefit by roughly 76%","Correct by analyst recall: 70% at 62 vs 124% at 70 for an FRA of 67 is +77%.",[]),
("Derek at 52 with $143,000, maxing with catch-ups and a 4% match on $82,000 for 15 years, retires with about $1.1M.","retires at 67 with approximately $1.1 million","K02: about $1.31M at 7% and $1.44M at 8% under those assumptions, so $1.1M is conservative; the return assumed is not stated.",[]),
("Ramsey surveyed 10,000 millionaires: 79% no inheritance; a third never earned six figures; eight in ten used 401(k)s.","Ramsey Solutions surveyed 10,000 everyday millionaires","Consistent by analyst recall of the Ramsey Solutions National Study of Millionaires.",[]),
]
TITLE='Authentic title "2026 Average Net Worth By Age (Are You Behind?)" is a benchmark-anxiety frame. The script explains mean vs median and then gives 2022 SCF medians by age (the newest data), so "2026" refers to the viewing year, not new data; the promise is delivered with that caveat stated.'
THUMB='Registered maxresdefault 1280x720 (HTTP 200, real image). White three-panel layout: "$0.02" over a child version of the recurring cartoon man holding a bill, "$950K" over the adult man with arms crossed, "$300" over an elderly version in a rocking chair, mouth open. At 320x180 all three numbers and life stages read clearly. None of the three figures appears in the script; the panels imply a life-cycle arc (rise and collapse) the video does not present.'
SCRIPT='A single-narrator data explainer with a composite (Derek): hook (friends near "the number"), mean vs median and wealth concentration, SCF medians by age with Fidelity benchmarks, lifestyle inflation, car and student debt, the emotional experience, homeowner vs renter gap, auto-enrolment, generational comparisons and the wealth transfer, decade-by-decade actions (start, max, catch-ups, super catch-up, Social Security), Derek\'s catch-up plan and Ramsey close. Core data are accurate; the 55-64 median and Derek\'s salary are inconsistent within the video.'
BEATS=['Hook: dinner-table comparison.','Mean vs median; concentration.','Under 35 (Derek at 34).','35-44 and Fidelity 3x.','45-54 and lifestyle creep.','55-64, 65-74, 75+.','How the machine works: raises, cars, student loans.','Emotional experience.','Homeowner vs renter; auto-enrolment.','Generations and wealth transfer.','Decade-by-decade actions.','Derek\'s plan; Ramsey; close.']
TOPIC={'analysis':'US household net worth by age from the 2022 SCF, benchmarks, and the behaviours that separate savers from high earners who build little.',
 'audience_problem':'Mid-career earners unsure whether they are behind.',
 'economic_mechanism':'WEALTH_DISTRIBUTION_BY_AGE_AND_ACCUMULATION_BEHAVIOUR',
 'demand_type':'BENCHMARK_ANXIETY_DATA_EXPLAINER_HYPOTHESIS','time_sensitivity':'High: recurring annual title; data refresh due with the 2025 SCF.',
 'narrative_angle':'The median, not the mean, shows where you really stand.'}
LESSON='Test an original net-worth-by-age video that keeps median-first framing, fixes internal inconsistencies, and refreshes when the 2025 SCF is released.'
VIRAL='TYPICAL (1.082x) at about 179 days old against peers 174-184 days old; four of ten peers STRONG (including a 294,309-view house video), one WEAK. Comment rate is computed in observed_result; impressions and CTR unknown.'
TREND='Published 15 Mar 2026; no authenticated attention series'
FORMAT='A single-narrator long-form data explainer with one composite and no promotion; retention unverified'
ALTS=['Unknown impressions, traffic sources and subscriber distribution','Annual net-worth-by-age titles attract search traffic that peers may not share','Thumbnail numbers unrelated to script; effect unknown']
EVENT='SCF 2022 age medians checked via search summaries; mean/median, renter gap, car payment, start-age, super catch-up and Derek projections reproduced. Wealth shares, Fidelity multiples, auto-loan totals, 2026 limits, Social Security and Ramsey by analyst recall; student-loan and auto-enrolment figures unverified.'
S='SEARCH_SUMMARY_OF_PRIMARY_OR_REPORTED_SOURCE'
SOURCES=[
 {'source_id':'SCF22','url':'https://www.boldin.com/retirement/average-net-worth-by-age/','source_date':'2023-10-18','access_scope':S,'locator':'Federal Reserve 2022 Survey of Consumer Finances (Fed Bulletin October 2023) via secondary age tables','finding':'Median net worth under 35 about $39,000 ($39,040); 35-44 about $135,300-135,600; 55-64 $364,500; overall mean $1,063,700 and median $192,700.','limitations':'Fed tables not read directly; homeowner/renter medians not confirmed in these results.','publication_applicability':'BEFORE_PUBLICATION'},
]
K02={'method':'Mean/median, ratio, annuity and catch-up projections',
 'results':{'mean_median_ratio':5.52,'owner_renter_ratio':38.1,'car_annual':8976,'start25_7500_8pct':1942924,'start35_7500_8pct':849624,'super_catchup_extra':13000,'derek_7pct':1311335,'derek_8pct':1443571,'derek_gap':349000},
 'limitations':'Annual compounding; Derek projection assumes max contributions each year including catch-ups and a 4% match on $82,000.'}
LIMITS='No audio, video, private analytics or native Excel verification; one source via search summaries; several figures by analyst recall. No paid purchases.'
