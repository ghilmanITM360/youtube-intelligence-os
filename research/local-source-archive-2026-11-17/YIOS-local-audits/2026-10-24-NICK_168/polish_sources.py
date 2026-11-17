import json,hashlib
from pathlib import Path
O=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-NICK_168');B=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/research/finance-economics-intelligence');ss=json.loads((O/'primary-source-ledger.json').read_text())
findings=[
'March 2026 full-size pickup mean transaction price was $65,964; February was $66,141. Luxury full-size pickups are a separate category. The table excludes applied consumer incentives.',
'U.S. 2024 pretax household money-income median was $83,730. Table A-2 reports 10.1% at $150K–$199,999 and 16.0% at $200K or more, totaling 26.1% at $150K or more.',
'In Q4 2025, 20.3% of financed new purchases had monthly payments of at least $1,000. Mean term was 69.6 months and APR 6.7%.',
'In Q1 2026, 43% of new loans involving negative-equity trade-ins extended to 84 months. All-new-vehicle mean term was 70.3 months and APR 6.9%.',
'Nearly 30% of new financed vehicles had 73–84-month terms in Q4 2025. The mean new rate was 6.37%, versus 11.26% for used vehicles.',
'Purchase affordability requires considering financing, insurance, fuel, maintenance and other ownership costs alongside the household budget.',
'Compare APR, interest rate, term, amount financed and total cost rather than the payment alone.',
'Depreciation and loan amortization jointly determine vehicle equity; rolling negative equity into a replacement loan raises its principal.',
'For selected 2025 half-ton crew-cab models, modeled cost was $14,781 annually at 15K miles, including depreciation and finance charges. Insurance was $1,699 annually, license/registration/taxes $1,098, and maintenance/repair/tires 11.36 cents per mile.',
'Current 2026 XLT starting MSRP is $44,695 before $2,795 destination and other fees. The model adds to the base model and offers multiple cab, engine and bed configurations.',
'Current manufacturer 2026 page lists WT at $37,200 and LT at $48,200 starting. LT is not the lowest WT trim.',
'The original manufacturer fleet guide distinguishes Tradesman and Big Horn and lists different equipment groups. It does not independently certify the transcript’s exact historical $47,500 configuration.',
'NVES studies new U.S. car and light-truck owners. The claimed original truck-usage tables and 250K truck-specific sample were not recovered.',
'Q1 2026 median usual weekly earnings for full-time wage and salary workers were $1,235 before taxes and other deductions.',
'Stocks fluctuate and losses are possible. A future 8% return is not guaranteed.',
'The index publisher distinguishes price, net total and total returns across different annualized windows. Its current snapshot does not verify the video’s undefined historical 8% average.'
]
limits=[
'This is a mean, not a median, MSRP or out-the-door quote. The March report was in an April 2026 release file and contemporaneous coverage, before upload; its exact release day was not recovered. A full-year 2026 average was not yet observable.',
'Calendar 2024 income collected in the 2025 CPS ASEC; U.S. households, not individuals or truck purchasers. Money income is pretax and is not take-home pay. No 2026 income estimate is inferred.',
'The relevant denominator is financed new purchases in the transaction sample. Cash purchases and leases cannot silently enter it; dollar thresholds include exactly $1,000.',
'This covers new vehicles with negative-equity trade-ins, not trucks alone. Direct Python retrieval returned HTTP403; the original page was accessible through web extraction/search. Different samples and quarters must not be merged.',
'Original institutional release dated March 5, 2026. All-new financing term shares are not truck-specific; rate differences from Edmunds are not automatically errors.',
'Pre-upload review date displayed, but no upload-day HTML capture. This guidance gives no universal salary or 20/4/10 requirement.',
'Pre-upload review date displayed. APR can include credit costs beyond note interest; a fee-free monthly model does not certify an actual lender offer.',
'Original June 2024 PDF search extraction reviewed. This does not verify a universal instantaneous 20% truck loss or a particular residual value.',
'Five selected top-selling models per category and a five-year cost framework; this is not a quote for one $50K truck or a seven-year cash budget. Loan principal is not an additional expense alongside depreciation. September 2026 findings were not used.',
'Current page, not an archived May quote. Current builder lists XL below XLT; Ford pages differ on the XL starting configuration. Do not use current prices to declare an exact historical MSRP false.',
'Main URL now defaults to 2027; the explicit previous-year link was followed. Search index showed $47,900 while live page showed $48,200. Exact May price, destination basis and configuration remain unverified.',
'Original manufacturer search extraction and current Ram page reviewed. Exact issue date and historical price basis remain unverified; no equal towing or payload capacity is inferred.',
'Current institutional context only. Field dates, weighting, questions and the quoted 75/70/35/90 and 63/32/87 percentages remain unavailable. F-150 owners cannot stand for all truck owners.',
'Age16+ full-time wage/salary workers in the CPS; individual gross earnings are not household income or measured median take-home pay. Taxes and deductions are missing.',
'Current investor guidance with no recovered historical publication date. It does not establish a historical S&P500 average or a retirement outcome.',
'Later/current index snapshot is explicitly retrospective. No post-upload market return is used as evidence the creator could have known it. Period, dividends, fees and return convention remain essential.'
]
for s,f,m in zip(ss,findings,limits):s['finding']=f;s['methodology']=m;s.pop('source_definition_note',None)
ss[8]['source_date']='2025-09-16';ss[8]['release_confirmation_url']='https://newsroom.aaa.com/2025/09/aaa-new-vehicle-costs-drop-to-11577/'
for s in ss:
 s['access_scope']='ORIGINAL_INSTITUTION_RELEVANT_WEB_CONTENT_READ;NOT_A_FULL_PUBLICATION_READ_CERTIFICATE'
for i,name in [(0,'kbb-march-2026.pdf'),(1,'census-2024.pdf'),(8,'aaa-2025.pdf')]:
 p=O/name;ss[i]['saved_source_path']=str(p);ss[i]['saved_source_bytes']=p.stat().st_size;ss[i]['saved_source_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(O/'primary-source-ledger.json').write_text(json.dumps(ss,indent=2)+'\n')
p=B/'audit-batches/NICK_168_READ_RECEIPTS.json';r=json.loads(p.read_text());r['primary_source_receipts']=ss;p.write_text(json.dumps(r,indent=2)+'\n');(O/'NICK_168_RECEIPTS_DRAFT.json').write_text(p.read_text())
