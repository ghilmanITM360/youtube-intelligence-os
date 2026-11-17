from pathlib import Path
import json
O=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-NICK_168');p=O/'financial-claims.json';cs=json.loads(p.read_text())
a=[
'Undated price-history rhetoric is not a comparable trim or real-dollar series. A $50K universal minimum for new full-size pickups is not demonstrated.',
'About $66K agrees with the March 2026 mean of $65,964. A mean is not the typical buyer’s median, an out-the-door quote or a completed 2026 annual average. The source excludes applied consumer incentives.',
'XLT, LT and Big Horn are not the respective lowest XL, WT and Tradesman trims. The exact historical prices and XLT popularity rank remain unverified. Cab, bed, drivetrain, engine and destination basis are missing; current prices cannot prove May quotations wrong.',
'Options, taxes and fees can raise an out-the-door price above $50K, but the state, configuration and negotiated deal matter. The later $50K loan example does not itemize those costs.',
'$84K reasonably rounds the 2024 CPS household median of $83,730 released September 2025. This was an available estimate, not observed 2026 income. $50K/$84K=59.52%; using $83,730 gives 59.72%. Household median is not individual mean income.',
'No model, mileage, condition or residual-value source establishes 50% retention. Later $10K plus $9K cumulative depreciation implies $31K remaining, or 62% retention, contradicting the earlier assumption.',
'The $50K floor and $113K Raptor R depend on missing configurations and historical price receipts. Selected middle trims do not establish the lowest full-size price. No equal towing or payload comparison is asserted here.',
'The degree comparison lacks tuition versus attendance, public versus private, residency and period definitions. Parents’ first house and sports cars from 20 years ago are also undated rhetorical comparisons.',
'Edmunds Q4 mean term was 69.6 months (5.8 years); Q1 was 70.3. Experian’s nearly 30% at 73–84 months describes new financed vehicles, not trucks specifically. Even 69 months is 5.75 years, not 5.5.',
'43% is verified for Q1 2026 new loans involving negative-equity trade-ins across vehicles, not a truck-only subset. The earlier Q4 figure differs by period and need not contradict it.',
'Instantaneous 20% depreciation is unverified for this unspecified truck. The script later applies 20% after one year. Depreciation risk is real, but its size and timing require a vehicle-specific resale assumption.',
'Zero down and 7% are explicit hypothetical inputs. 7% is close to Edmunds Q1 6.9%, not a universal offer; Experian Q4 6.37% covers a different sample. The rhetorical claim that nobody has $10K cash is unsupported. Note interest, APR and financed fees must be distinguished.',
'Standard monthly amortization gives $754.634, $63,389.256 total and $13,389.256 interest. The quoted $754.85/$63,407/$13,407 differ by $0.216 monthly and about $17.74 total, a minor precision error. $754.85×84=$63,407.40; no additional fees explain the exact quoted payment.',
'After 12 monthly payments, balance is $44,262.638, not $45,700. With assumed $40K resale, negative equity is $4,262.638, not $5,700. Principal repaid is $5,737.362. Resale itself remains conditional.',
'20.3% describes financed new purchases, not all new purchases or all buyers. The source threshold is at least $1,000, not strictly above $1,000. Cash transactions and leases cannot silently enter that denominator.',
'$1,000 as one-third implies $3,000 monthly net pay. BLS reports $1,235 median gross weekly earnings, about $5,351.67 monthly. Taxes, filing status and deductions are needed; gross earnings do not verify a national median take-home figure.',
'No buyer-income distribution verifies a blanket top-15% purchaser claim. Individual and household denominators switch. The later statement that most truck buyers earn $60K–$100K conflicts with this framing. A 14% used APR is possible, not a universal observed mean.',
'Loan approval and household residual-income affordability are different. Claims about banks expecting ramen or skipped dentistry are rhetoric, not observed underwriting requirements.',
'$185 insurance, 18 mpg, $4 gasoline, 15K miles and $90 maintenance are assumptions, not a VIN-specific quote. Fuel computes to $277.78/month, close to $275. AAA’s model differs; its insurance and maintenance averages do not establish this buyer’s bill.',
'Tire prices of $800–$1,600 or $3K and a 50K-mile life lack size, brand and installation receipts. 50K miles at 15K annually lasts 3.33 years. $90 registration/taxes is near AAA’s annual modeled amount, but state and upfront-versus-recurring treatment are unspecified.',
'$10K year-one plus another $9K by year five implies $31K residual and 38% cumulative loss, versus the earlier 50% loss. Neither is verified for a specific truck. Do not assume the additional $9K occurs every year.',
'Quoted cash-flow items sum to $1,395 and reasonably round to $1,400. Formula payment and exact fuel give $1,397.412. This is a cash budget, not a complete economic TCO calculation. Financing ends after month 84 and operating costs vary. Adding depreciation to full principal installments double-counts capital cost.',
'The fictional budget sums exactly: $1,850+$1,200+$800+$350+$1,400=$5,600. Net pay is an assumption, not a verified tax result. CRV expenses, healthcare and other debts are omitted. A 76-mile workday over 260 days already totals 19,760 miles; at 18 mpg/$4, fuel is $365.93 monthly before errands. The transmission failure is a narrative assumption.',
'The original 250K truck-owner sample, field dates, weighting and questions were not recovered. None of the 75/70/35/90% or F-150 63/32/87% pairs is independently verified. Rarely/never is not identical to once per year or less. F-150 owners are not all truck owners, and errands and work can overlap.',
'Dave and the unused kayak are fictional illustrations. They do not establish an average truck owner or a causal identity motive.',
'No retention or first-party analytics supports most viewers having left during the math. This is a persistence appeal, not an observed audience result.',
'The $20K five-year-old Camry and $700 total monthly cost lack APR, term, down payment, mileage and resale inputs. $1,400−$700=$700 is correct conditionally. Loans end and vehicles need replacement over 30 years; no equal towing or payload claim is made.',
'The 8% historical claim omits its period, dividends, nominal/real basis and arithmetic/geometric definition. Treat 8% as a modeling assumption, not a verified mean for all windows or a guaranteed return.',
'$700 at each month-end for 360 months at 8%/12 gives $1,043,251.614 nominal before taxes, fees and inflation, including $252K contributions. Converting an effective annual 8% to a monthly rate gives $985,985.411. Saving for only seven years and then growing to year 30 gives $491,139.834 in an analyst sensitivity case.',
'Retiring at 65 rather than 75, inheritance and certainty of retirement cannot follow without age, other assets, Social Security, spending, longevity, tax and inflation assumptions. No 4% withdrawal rule appears in the transcript. A constant market path and a 30-year cost gap are not established.',
'Future opportunity cost is a useful separate counterfactual, not another cash price to add on top of purchase and loan payments. Down payment, installments, resale and terminal investment wealth must reconcile over one horizon. A 30-year replacement strategy is missing.',
'Absolute claims that nobody profits from investing and only the buyer loses overlook fund fees, transportation utility and business use. These are incentive arguments, not proof that every purchase destroys buyer welfare; no Fidelity pricing audit is implied.',
'Under the script’s TOTAL transportation ≤10% of gross rule, a $40K/7%/48-month payment of $957.85 plus $185+$275+$90+$90 requires $191,741.97 annual gross income. Exact fuel raises this to $192,075.31. At $150K gross, the $1,250 monthly allowance leaves only $292.15 after financing. The heuristic is not a universal rule.',
'20% of $50K is $10K; financing the remaining $40K for 48 months at 7% gives $957.85, reasonably near $950. Taxes/fees and the down payment’s investment opportunity cost are excluded; the same APR across terms is assumed.',
'CPS 2024 table A-2 places 26.1% of households at $150K or more (10.1% plus 16.0%), not 15%. An individual-earner percentile cannot replace a household one. This income alone proves neither necessary nor sufficient affordability.',
'The claim that most truck purchasers earn $60K–$100K lacks a purchaser-distribution source and conflicts with the earlier blanket top-15% framing. Garcia truck cost is 25% of $5,600 take-home, not 30%; another household might differ. Geography, debt and assets remain necessary.',
'Adding full installment cash flow and depreciation double-counts financed principal in an economic-cost total. Use a cash affordability ledger without additional depreciation, or interest plus depreciation and operating costs, or purchase minus resale over a consistent horizon. Do not merge a gross-income rule with a net-income budget.',
'A widest-ever approval-versus-affordability gap needs a consistent historical series. None is provided. Broad industry intent and identity arguments remain editorial interpretations.',
'The work, towing, hauling and location exception usefully qualifies blanket anti-truck framing. Specific capability requirements and commercial value remain unquantified; no model-equivalence or maximum-towing comparison needs importing from NICK_165.'
]
assert len(a)==len(cs)
for c,t in zip(cs,a):c['assessment']=t
p.write_text(json.dumps(cs,indent=2)+'\n')
# Improve readability of institution receipts without manufacturing historical availability.
p=O/'primary-source-ledger.json';ss=json.loads(p.read_text())
for s in ss:
 s['finding']=s['finding'].replace('mean ATP','mean transaction price').replace('half-ton','half-ton')
 s['source_definition_note']='See claim assessments for population, product basis, date and uncertainty; no source confirms an unspecified personal quote.'
p.write_text(json.dumps(ss,indent=2)+'\n')
print('Refined',len(cs),'claim assessments')
