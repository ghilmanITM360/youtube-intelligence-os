import csv
from pathlib import Path
p=Path('02_VIDEO_FORENSICS/0ll9rEtoRrs')
s={r['sentence_id']:r for r in csv.DictReader(open(p/'SENTENCES.csv'))}
data='''1|1|US debt crosses $40T; Treasury doubles buybacks|S002.1-S003.3|UNVERIFIED|Headline snapshot; not independently fact-checked.
5|6|Six countries have elevated long bond yields in the same week|S006.2-S006.10|PARTLY_CHECKED|Displayed chart dates differ; simultaneity not established.
12|13|Germany has smallest G7 debt load and highest yield in 15 years|S012.2-S012.5|PARTLY_CHECKED|2025 debt ratio shown as 64%; time scopes differ.
22|23|Fictional pension pays $2000 monthly for life|S019.6-S020.0|ILLUSTRATIVE_NOT_EMPIRICAL|Teaching scenario.
33|41|Long bonds match pension cash-flow obligations|S027.4-S033.11|ILLUSTRATIVE_SIMPLIFICATION|Mortality, inflation, defaults and reinvestment omitted.
46|51|Defined-benefit funds are patient price-insensitive buyers|S035.8-S038.3|SOURCE_INTERPRETATION_UNVERIFIED|Absolute wording omits solvency and collateral constraints.
69|70|Defined-benefit prevalence falls from 80% to 36% to 14%|S050.5-S051.2|PARTLY_CHECKED_SCOPE_CHANGE|Historical full-time medium/large participation versus modern all-worker access denominator.
74|76|401k employers owe nothing past payday|S051.11-S053.5|UNVERIFIED|Absolute legal-obligation interpretation not established.
77|77|401k portfolios exceed 70% equities with about 5% standalone bonds|S053.6-S053.11|PARTLY_CHECKED|Displayed equity allocation 75%; mixed funds contain bond exposure.
78|80|OECD pension ownership of domestic bonds falls from 8% to 4%|S053.18-S055.0|PARTLY_CHECKED|Ownership share is not portfolio allocation; membership/date scope unverified.
82|83|Fed describes shift toward private price-sensitive buyers|S056.0-S057.0|PARTLY_CHECKED|Term-premium implications are conditional, not demonstrated causality.
85|86|UK pension gilt holdings fall from about 27% GDP to below 6%|S060.0|SPEECH_SCREEN_FIGURE_CONFLICT|Screen OBR 28.7% to 5.6% in early 2070s; ASR 27% retained.
87|87|UK modeled 80bp rise adds £22B annual interest|S060.3|PARTLY_CHECKED|Scenario assumptions include debt/GDP; not guaranteed outcome.
89|89|Dutch pensions hold nearly €2T|S063.2-S064.1|PARTLY_CHECKED|Displayed 1,741,575 and 152.4% GDP; rounding and units require care.
90|92|Thirty Dutch funds and ten million people convert January 2026|S064.2-S065.0|PARTLY_CHECKED|Parliamentary source excerpt; approximate first-wave counts.
93|95|Dutch mandate drives holdings including 10% of German bonds|S066.0-S067.3|PARTLY_CHECKED|IPE excerpt 20% Dutch and 10% German; regardless-yield wording is interpretation.
97|97|DNB expects €100-150B long-bond and swap unwinding|S069.0-S069.1|PARTLY_CHECKED|Forecast, not completed sales; maturities at least 25 years.
98|99|ABP converts January 2027; nearly €1T converts in 2027|S071.1-S072.0|PARTLY_CHECKED|ABP €530B rounded to €500B; relative dates belong to video's 2026 context.
100|100|PIMCO models €115B reduction in thirty-year-equivalent demand|S072.4-S074.3|PARTLY_CHECKED|Duration/hedging model is not nominal sales volume.
101|103|Dutch withdrawal equals half European annual net risk issuance|S075.0-S075.1|UNVERIFIED|Nomura attribution visible; underlying methodology unrecovered.
105|107|Auctions clear but buyers require higher yields|S077.0-S077.7|UNVERIFIED|Displayed auction does not establish all-market behavior.
110|113|UK long issuance declines from 30% to below 10%|S077.24-S077.26|PARTLY_CHECKED|DMO chart and Treasury demand excerpt have dated scopes.
114|115|Japan cuts issuance to ¥17T, seventeen-year low|S077.29-S077.33|MODALITY_CONFLICT|Reuters excerpt says likely and would consider; narration treats cuts as realized.
117|118|US bills are 22% versus TBAC guidance of 15-20%|S078.1-S080.0|PARTLY_CHECKED|Historical 2024 guidance and later projection have different dates.
119|120|OECD bill issuance exceeds fixed bonds; long share lowest since 2008|S080.1-S082.0|PARTLY_CHECKED|Gross issuance turnover is not outstanding stock.
122|131|Short debt increases rollover frequency and debt is never repaid|S083.3-S088.5|ILLUSTRATIVE_SIMPLIFICATION|Possible surpluses and debt retirement omitted.
133|137|Average interest 3.5%, new debt 4%, thirty-year yield 5.2%|S088.7-S089.2|PARTLY_CHECKED|Treasury July 2026 and CNBC spot dates differ; one-year 4.02% does not price all bills.
138|139|33%, more than $10T, matures within twelve months|S089.3-S089.4|PARTLY_CHECKED|JEC public marketable debt denominator; not independently updated.
140|140|Average interest must rise as debt rolls over|S089.9-S090.0|UNVERIFIED|Conditional on refinancing rates staying above existing averages.
141|143|Interest exceeds $1T and defense/veterans; Medicare overtaken in 2028|S091.0-S091.4|PARTLY_CHECKED|Gross versus net interest denominators differ; 2028 is a forecast.
149|152|OECD refinancing $13.5T in 2025 near 80%, another $1T in 2026|S094.1-S094.7|PARTLY_CHECKED|Principal refinancing flow is not interest expense; borrowing-cost ASR ambiguous.
153|154|One-third fixed debt due by 2027; 60% issued by 2021, about $9T|S096.5-S099.2|PARTLY_CHECKED|Stock as of 2024 in 2025 report; dated projection.
155|158|New issuance rates rise approximately two percentage points|S097.1-S099.2|PARTLY_CHECKED|Historical since-2023 comparison, not guaranteed future rate per bond.
159|160|One-fifth of 2025 fixed issuance above 4%, highest share since 2015|S100.1|PARTLY_CHECKED|Share above threshold is not highest market rate.
161|161|Technology companies borrowed $122B in 2025 for AI|S101.0-S102.4;S104.0|UNVERIFIED|Allocation of borrowing specifically to AI not traced.
162|163|AI capex $4.1T 2026-2030; high debt-finance case 15% of issuance|S103.0-S104.0|PARTLY_CHECKED|Forecast assumptions, including 50% debt financing, are not actual outcomes.
163|163|Global 2026 borrowing $29T, $4T above 2024; long share low since 2009|S105.0-S107.0|PARTLY_CHECKED|Projection; gross borrowing differs from net new debt.
166|170|Money funds exceed $8T but patient long-term capital is scarce|S114.0-S117.1|SOURCE_INTERPRETATION_UNVERIFIED|FRED supports growth; patient-capital thesis remains interpretation.
173|177|Short debt inevitably becomes more expensive, described as not a forecast|S118.2-S120.6|FORECAST_PRESENTED_AS_CERTAINTY|Maturities known; future refinancing rates remain conditional.'''
rows=[]
for i,line in enumerate(data.splitlines(),1):
 a,b,claim,support,status,note=line.split('|'); a,b=int(a),int(b)
 rows.append(dict(claim_id=f'C{i:02}',start_sec=s[f'T{a:04}']['start_sec'],end_sec=s[f'T{b:04}']['end_sec'],sentence_ids=f'T{a:04}-T{b:04}',claim_summary=claim,claim_class='SOURCE_CLAIM' if 'ILLUSTRATIVE' not in status else 'ILLUSTRATIVE',on_screen_support=support,verification_status=status,fact_check_priority='HIGH',notes=note+' ASR numbers/proper nouns remain uncertified; audio not directly listened; supplied-source review only.'))
assert len(rows)==39
q=p/'FINANCE_CLAIMS.csv.tmp'
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
q.replace(p/'FINANCE_CLAIMS.csv')
print('Saved',len(rows),'claims')
