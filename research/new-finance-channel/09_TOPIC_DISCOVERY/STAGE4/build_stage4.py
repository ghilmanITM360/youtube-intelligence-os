import sys,csv,json,pathlib,markdown,statistics as st
sys.path.insert(0,'../../03_PRIMARY_REFERENCE_CHANNELS/STAGE2_SIX_REPORTS'); import build_data as B
ALL=[]
for s in B.CH:
    nm,cid,R=B.load(s)
    for r in R: r['channel']=nm; ALL.append(r)
def find(sub):
    m=[r for r in ALL if sub.lower() in r['title'].lower() and not r['member']]
    assert m,sub
    m.sort(key=lambda r:-(r['views'] or 0)); return m[0]
def ev(subs):
    out=[]
    for s in subs:
        r=find(s); out.append(f"{r['channel']}: [{r['title'][:60]}]({r['url']}) {r['views']:,} ({r['date']}{', Short' if r['short'] else ''})")
    return '<br>'.join(out)
# id, F/E, working topic, evidence substrings, competitor coverage, original angle (HYPOTHESIS), candidate data source, saturation, decision
C=[
('E01','E','Why sellers outnumber buyers but house prices hold (the lock-in gap)',['Housing Crisis Has Landed','58% More Home Sellers'],'Casual Finance: 13 housing titles (long 2.42M, 738K; Short 168K); Monkey Economics mortgage Short 2.07M; MonkeyExplains housing-bubble long 276K (1.0x)','Show the gap between existing mortgage rates and today’s rate by metro, using public series, so the viewer can see why owners do not sell','FRED/Freddie Mac mortgage rates, Redfin/Realtor.com inventory (not yet opened)','High (Casual Finance has 13 housing videos)','ADVANCE (owner theme: housing)'),
('E02','E','Rent: why official rent inflation lags the rent you actually pay',['Housing Crisis Has Landed'],'No six-channel video on rent; housing cluster has 3 long videos on 2 channels','Explain the CPI shelter measure and its ~6-month lag against market rent series (earlier work: BLS CPI, Zillow ZORI read in Phase D)','BLS CPI shelter table, Zillow ZORI (opened earlier)','Low on rent specifically','ADVANCE (owner V1; derived indirectly from the housing winner, no rent winner)'),
('E03','E','Rates: why the 30-year yield and the Fed decision hit a household budget',['To Save the Economy','Walking Into Something','Safest Market Is Breaking','Interest Rates Are Going Up'],'Casual Finance 3 winners (1.43M to 1.81M) among 8 rates titles; Monkey Economics and MonkeyExplains 4 more; median PI of the Fed/rates cluster 1.88x','Translate one yield move into a mortgage, car loan and credit-card payment with a worked example per week of release','Treasury auction data, FRED DGS30/MORTGAGE30US (not yet opened)','High (Casual Finance 8 titles)','ADVANCE'),
('E04','E','National debt: the interest bill per household and what it crowds out',['National Debt Crisis Explained','Quietly Drowning in Debt','Inevitable'],'MonkeyExplains 1.92M breakout (7.0x); Casual Finance 119K and 88K; debt cluster median PI 0.21x, so the breakout is one-off','Use the Monthly Treasury Statement to compare interest outlays with defence, Medicare, education per household','Treasury MTS, CBO (not yet opened)','High (26 debt titles, Casual Finance 18)','ADVANCE conditional: one breakout, weak cluster'),
('E06','E','Inflation basket: which prices are actually rising and which are not',['New Inflation Is Here','Mathematically'],'Monkey Economics 21.5K winner (2.1x); Casual Finance Short 389K (17.5x); cluster 1.88x','One-chart-per-category CPI components for the latest release; "official number vs your basket"','BLS CPI release tables (opened earlier)','Medium','ADVANCE (owner theme: inflation)'),
('E07','E','One price decomposed: why memory/RAM and other hardware got expensive',['RAM Prices Are Worse'],'MonkeyExplains only (688K, 2.5x)','Same "who gets each dollar" decomposition used for the gas and airfare ideas, applied to DRAM contract prices and demand from AI data centres','DRAM contract price trackers, company filings (not yet opened)','Low (1 channel)','ADVANCE'),
('E08','E','Airfares: what an airline ticket pays for (owner V2)',['RAM Prices Are Worse','Strait of Hormuz'],'No six-channel video on airfares (strict audit finding); related only through the price-decomposition and fuel winners','BLS CPI airline fares and IATA cost breakdown read earlier (airfares +22.4% in the CPI table)','BLS, IATA (opened earlier)','Low','ADVANCE CONDITIONAL: no direct competitor winner; Stage 5 must prove demand'),
('E09','E','Fuel shocks: how a strait closure becomes a pump price',['Strait of Hormuz','One Shortage America','Oil Crisis Is'],'Capital Case 250K (4.6x), MonkeyExplains 283K, Casual Finance 137K; Iran/oil cluster median 0.62x','EIA pump-price breakdown (earlier L4, rejected in Phase D as "gasoline", kept only if an event angle exists)','EIA gasoline composition (opened earlier)','High (20 oil/fuel titles, MonkeyExplains 9)','ADVANCE conditional (earlier rejection must be re-justified)'),
('E11','E','Jobs: what the monthly jobs number measures and why it is revised',['Job Market Is Completely','Stop Being Good'],'MonkeyExplains 301K (1.1x); Monkey Economics careers 212K (20.7x); jobs cluster has 4 long videos','Household vs payroll survey, revisions, with the actual release (earlier L3)','BLS CPS and Employment Situation notes (opened earlier)','Low','ADVANCE'),
('E12','E','Ageing economies: what a shrinking population does to growth',['South Korean Population','Economy Is Awful'],'MonkeyExplains 501K; Casual Finance Short 279K (12.5x); China/other-countries cluster median 1.48x','Country comparison on one chart (working-age population vs GDP per worker) using UN and World Bank series','UN WPP, World Bank (not yet opened)','Low for ageing itself; Japan is covered by Casual Finance (11 titles)','ADVANCE'),
('F01','F','AI companies: the revenue-versus-spend arithmetic behind the bubble debate',['AI Bubble Popped','OpenAI Bubble','Hidden Debt','Biggest IPO in History'],'MonkeyExplains 6 winners, Casual Finance, Paper Billions, Crayon: 5 channels, 28 long videos, 19.4M views','Only with a distinct data angle: capex per dollar of revenue from company filings, per company, updated each quarter','SEC filings (not yet opened)','**Very high** (most saturated cluster)','ADVANCE with warning (owner theme: AI bubble/IPO)'),
('F02','F','How an IPO works and why very large IPOs worry markets',['SpaceX IPO... It','Dumping Ground','IPO Boom Is the Danger','Rise of Anthropic'],'Casual Finance 1.71M, 1.46M, Short 145K; Crayon 1.12M; Capital Case 55K; SpaceX/IPO cluster median 1.25x','Explain lock-up, float and index inclusion with a worked example; avoids guessing a company’s future','SEC S-1 and index rules (not yet opened)','High','ADVANCE'),
('F04','F','Crashes people forgot: the same chart for 1929, 1973, 2000, 2008 and now',['Great Depression Explained','2008 Financial Crisis Explained','1973 Stock Market Crash','Fatal Decisions'],'5 channels, 13 long videos, 6 winners, median 1.65x; "nobody remembers" framing worked at Casual Finance (1.28M)','One drawdown-and-recovery chart per crash on a common axis; add less-covered crashes (1987, 1998, 2000)','FRED/S&P series (not yet opened)','High for 1929/2008, low for forgotten ones','ADVANCE (owner theme: crises/history)'),
('F05','F','AI boom versus dot-com and railroads: is the spending bigger?',['AI Bubble Explained Like','Dot-Com Bubble','AI Bubble Popped'],'Intersection of two top clusters; Crayon dot-com 393K (1.3x) and AI bubble 438K','Capex as a share of GDP on one chart for three booms','FRED, company capex (not yet opened)','High on AI, low on the comparison','ADVANCE'),
('F08','F','How the credit-card fee system works (interchange and the duopoly)',['2 Companies Ruined'],'MonkeyExplains only (666K, 2.4x)','Use public interchange and network-fee data to show where a $100 swipe goes','Fed/CFPB interchange data (not yet opened)','Low (3 channels touch credit cards, 1 long winner)','ADVANCE'),
('F09','F','The consumer-debt wave: cards, car loans and who is late',['2.5 Trillion Credit Wave','2 Trillion Credit Wave'],'Casual Finance 717K (1.3x) and MonkeyExplains 228K on the same idea','Use delinquency series by loan type','NY Fed household debt report (not yet opened)','Medium (2 channels)','HOLD: no winner (717K is 1.3x, 228K is 0.8x); fails the decision rule'),
('F10','F','Japan, the yen and why its bond market matters to the US',['Bailed Out Japan','Economy Is Awful','Yen Carry'],'Casual Finance long 779K (1.4x), Shorts 279K (12.5x) and 16K','Explain the carry trade with one number path; do not predict','BoJ/Treasury data (not yet opened)','High (Casual Finance has 11 Japan titles)','ADVANCE'),
('E10','E','Tariffs: who actually pays',['Tariff Wars Explained','Tariff War'],'MonkeyExplains 653K and 228K; event-timed','Import price evidence by product','BLS import prices (not yet opened)','Medium','HOLD: one channel, event-driven, tariffs cluster only 2 videos'),
('E13','E','France and European debt',['Next Great Crisis Just Started'],'Casual Finance 1.36M (2.4x)','Spread chart of French vs German yields','ECB data (not yet opened)','Low','HOLD: event-timed'),
('E14','E','Government shutdown economics',['Shutdown Explained'],'MonkeyExplains 726K (2.6x)','Cost of shutdown by sector','CBO','Low','HOLD: only valid on a live event'),
('E15','E','Country development stories (Singapore)',['Singapore in One Generation'],'Crayon 974K (3.2x)','Development chart story','World Bank','Low','HOLD: narrative and illustration load; one winner'),
('F06','F','Company and billionaire origin stories',['Rockefeller: The First','Bezos Actually','Rockefeller Explained'],'Crayon 1.33M, 1.01M; Capital Case 385K; cluster median 0.78x with 12 videos','n/a','n/a','Medium','HOLD: production-heavy, rated a poor core in Phase F, cluster median below 1'),
('F07','F','Famous frauds and scams',['Wolf of Wall Street Scam','Sold Nothing'],'Crayon 4.22M breakout (14x), Enron 920K; cluster median 0.58x with 14 videos','Forensic accounting angle','n/a','Medium','HOLD: one breakout plus legal-risk care'),
('E16','E','Gold and the dollar system',['Why Gold Always Go Up','WTF Is Happening To Gold','Petrodollar'],'0 winners in cluster; median 0.64x','n/a','n/a','Medium','DROP: no winners'),
('F11','F','Crypto and Bitcoin "scam" claims',['Crypto Is a Brilliant Scam','Bitcoin Is a Brilliant Scam'],'Casual Finance 587K and 358K; crypto/fraud cluster 0.58x','n/a','n/a','Medium','DROP: weak cluster, legal and policy risk'),
('F12','F','Private credit and personal-investing basics',['Private Credit','Every Type of Investor','Money Traps'],'Casual Finance 48K and 192K; Monkey Economics 9K','n/a','n/a','Medium','DROP: all below channel medians'),
]
rows=[]
for c in C:
    rows.append(c)
adv=[c for c in C if c[8].startswith('ADVANCE')]; hold=[c for c in C if c[8].startswith('HOLD')]; drop=[c for c in C if c[8].startswith('DROP')]
W=list(csv.DictReader(open('winners_2026-11-19.csv')))
wl=sum(1 for w in W if w['type']=='L'); ws=len(W)-wl
tab='| ID | F/E | Working topic | Winner evidence (competitor, views, date) | Competitor coverage | Original-angle hypothesis | Candidate data source | Saturation | Decision |\n|---|---|---|---|---|---|---|---|---|\n'
for c in C:
    tab+=f"| {c[0]} | {c[1]} | {c[2]} | {ev(c[3])} | {c[4]} | {c[5].replace(chr(92),'')} | {c[6]} | {c[7]} | **{c[8]}** |\n"
wtab='| Channel | Type | Date | Views | x median | Sub-niche | Title |\n|---|---|---|---:|---:|---|---|\n'+'\n'.join(f"| {w['channel']} | {w['type']} | {w['date']} | {int(w['views']):,} | {w['pi']} | {w['sub_niche']} | [{w['title'].replace('|','/')}]({w['url']}) |" for w in sorted(W,key=lambda w:(w['type'],-float(w['pi']))))
md=f"""# Stage 4: Finance and Economics topic discovery from the six channels' winners (2026-11-19)

Scope: Casual Finance, Monkey Economics, MonkeyExplains, Crayon Capital, PaperBillionsTV, Capital Case only. Discovery only: nothing below is validated (Google Trends, news, YouTube search, demand and competition checks, nine-item sheets are Stages 5 and 6). Read-only on the DB; no spend; nothing committed. Builder `build_stage4.py`, winners list `winners_2026-11-19.csv`, candidates `topic_candidates_2026-11-19.csv`.

## 1. Method (how topics were found)

1. **Winners and breakouts**: every public long-form video at >= 2x its own channel's long-form median ({wl} videos) and every Short at >= 5x its channel's Shorts median ({ws} Shorts). Member Edition items excluded. Views are snapshots from 2026-11-17 to 2026-11-19; recent videos have had fewer days, so older videos are favoured (see Stage 3 age caveat).
2. **Seeds**: winners grouped by theme with the first-match clusters of Stage 3 (crisis history, AI bubble, IPOs, rates/Fed, debt, housing, prices, jobs, demographics, origin stories, scams, geopolitics/energy).
3. **Candidates**: each seed became one or more candidate topics with the winning video(s) that justify it, how many of the six channels already cover it, a hypothesis for an original angle, and a data source that would have to be opened in Stage 5. Where no winner supports a candidate it is flagged, not hidden.
4. **Decision rule for advancing to Stage 5** (INFERRED rule, our own): at least one competitor winner in the topic's cluster, or an explicit owner theme; an angle that uses public data rather than a news reaction; not dependent on a live event; not dependent on cinematic illustration load. Topics that fail go to HOLD (revisit) or DROP (cluster without winners).
5. Framework use: Playbook P01/P06 (cross-validated outliers, competitor overlap), DS-000018 REC-009 (net-new information), and the Stage 3 result that no title or hook rule can be used as a gate.

Result: **{len(C)} candidates; {len(adv)} advance to Stage 5, {len(hold)} on hold, {len(drop)} dropped.** Finance and Economics both advance: Economics {sum(1 for c in adv if c[1]=='E')}, Finance {sum(1 for c in adv if c[1]=='F')}.

## 2. Candidate topics

{tab}
## 3. Reading the table

- **Open gaps (low saturation with at least one winner):** rent/CPI shelter lag (0 titles in all six channels), hardware price spikes (1 channel), ageing economies as a theme, credit-card fees (1 long winner), jobs-report mechanics. Japan/yen is NOT a gap: Casual Finance has 11 titles on it. Each rests on a single channel's winner or on none, so Stage 5 demand checks are essential.
- **Saturated (competitor winners on 4 to 5 channels):** AI companies and crisis history. These advance only because the owner chose those themes; they need a distinct data angle (F01, F04, F05).
- **Not derived from any competitor winner:** airfares (E08) and the earlier gasoline idea (E09 in its earlier form). The strict audit found no airfare video in any of the six channels; the only link is the price-decomposition format of the RAM winner. Treat E08 as owner-chosen, not evidence-chosen.
- **Strongest single-video evidence:** the AI-bubble question (2.66M), national debt (1.92M breakout), housing crisis (2.42M), crisis history (Crayon 2.76M, 2.29M), and the stock-market-structure trio at Casual Finance. These were mostly delivered by the channels with large subscriber bases (Casual Finance 440K, MonkeyExplains 261K, Crayon 319K), so a new channel should not assume the same reach.
- **Shorts:** the highest-view Shorts are basic concept explainers (Monkey Economics bank, laundering, minimum wage, inflation: 3.1M to 7.7M) and short "one claim" Shorts at Casual Finance (up to 389K). Stage 3 and Stage 2 found Shorts did not carry long-form reach, so Shorts concepts stay a format question for Stage 7, not a topic source.

## 4. Winners list (the evidence base)

{wtab}

## 5. Review of this report (done 2026-11-19, before Stage 5)

| # | Issue | Check | Fix |
|---|---|---|---|
| R1 | Coverage strings were typed by hand | Keyword search of all six channels' titles (long and Shorts) per candidate | E01 said "other 5 channels none": wrong, Monkey Economics has a 2.07M mortgage Short and MonkeyExplains a housing-bubble video. E04 debt (26 titles, Casual Finance 18), E09 oil/fuel (20 titles, MonkeyExplains 9), F10 Japan (Casual Finance 11) and E03 rates were rated Medium/Low saturation: corrected to High. E02 rent and E08 airfares confirmed at 0 titles |
| R2 | Decision rule requires a competitor winner or an owner theme | Checked each ADVANCE | F09 consumer debt has no winner (717K = 1.3x, 228K = 0.8x) and no owner theme: **moved to HOLD**. E02 and E08 stay only as owner-chosen conditional topics; E11 (jobs-report mechanics) rests on a careers winner (Stop Being Good at Your Job, 20.7x), not on a jobs-report video |
| R3 | Winner threshold is relative to each channel's median | Noted | Small channels' "winners" can be below large channels' averages; unchanged, stated in Limits |
| R4 | Dates | Many winners are old (the 1.92M debt video is 2025-06-13) | Age is shown in every evidence cell; no change |

After review: **{len(C)} candidates; {len(adv)} advance, {len(hold)} hold, {len(drop)} drop.**

## 6. Limits
- Keyword/theme grouping is ours (INFERRED); a topic can be mis-grouped.
- Winner status uses each channel's own median, so a small channel's "winner" can be below a large channel's average video.
- Competitor topic coverage is counted from the DB holdings, not from the full channels (MonkeyExplains 136 of 149; 13 Member items missing).
- No demand, competition, Trends, news or search checks yet: Stage 5.
"""
pathlib.Path('STAGE4_TOPIC_DISCOVERY_2026-11-19.md').write_text(md)
css=open('../../03_PRIMARY_REFERENCE_CHANNELS/STAGE2_SIX_REPORTS/build_reports.py').read().split('css="')[1].split('"\n')[0]
pathlib.Path('STAGE4_TOPIC_DISCOVERY_2026-11-19.html').write_text(f"<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>Stage 4 topic discovery</title><style>{css}</style><p><a href='../../START_HERE.html'>&larr; START HERE</a></p>"+markdown.markdown(md,extensions=['tables']))
with open('topic_candidates_2026-11-19.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['id','fe','topic','coverage','angle_hypothesis','data_source','saturation','decision']); 
    for c in C: w.writerow([c[0],c[1],c[2],c[4],c[5].replace(chr(92),''),c[6],c[7],c[8]])
print(len(C),len(adv),len(hold),len(drop),wl,ws)
