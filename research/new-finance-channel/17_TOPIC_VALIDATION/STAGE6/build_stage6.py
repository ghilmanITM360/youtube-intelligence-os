import csv,re,sys,os,markdown
sys.path.insert(0,'../STAGE5'); os.chdir('../STAGE5'); import build_stage5 as b5; os.chdir('../STAGE6')
W=list(csv.DictReader(open('../../09_TOPIC_DISCOVERY/STAGE4/winners_2026-11-19.csv')))
KW={"E01":"hous|mortgage|home|sellers|rent","E03":"rate|fed |yield|interest","E04":"debt","E06":"inflation|cpi","E07":"ram |memory|chip|shortage","E09":"oil|hormuz|fuel|gas|iran","E11":"job|employ","E12":"population|korea|aging|ageing","F01":"ai |openai|nvidia|anthropic|bubble","F02":"ipo|spacex","F04":"crash|depression|2008|nobody|crisis","F05":"dot|bubble|boom","F08":"credit card|visa","F10":"japan|yen"}
def comp(i):
    k=KW.get(i)
    if not k: return "none in the six channels (0 winners matched)"
    m=[w for w in W if re.search(k,w['title'].lower()+' ')]
    m.sort(key=lambda w:-int(w['views']))
    return "; ".join(f"[{w['channel']}: {w['title'][:60]}]({w['url']}) {int(w['views']):,} views, {w['date']}" for w in m[:3]) or "none matched"
# legs: winners, demand, low competition, live hook
L={"E06":"YYNY","E01":"YYNY","F02":"YYYN","E11":"NYYY","E03":"YYNN","F04":"YNYN","E04":"YYNY","F01":"YYNN","F08":"YNYN","E08":"NNYY","E02":"NNYY","F10":"YNNY","E07":"YNNY","F05":"YNNN","E09":"YYNN","E12":"YNNN"}
D={"E06":1.4,"E01":1.0,"F02":1.1,"E11":.22,"E03":.23,"F04":.1,"E04":.25,"F01":2.8,"F08":.08,"E08":.05,"E02":.02,"F10":.01,"E07":0,"F05":.01,"E09":.6,"E12":.02}
T={t[0]:t for t in b5.T}
tier=lambda i:{"GO":0,"GO-CONDITIONAL":1,"HOLD":2}[T[i][8]]
order=sorted(T,key=lambda i:(tier(i),-L[i].count("Y"),-D[i]))
md=["# Stage 6 — Final Topic Ranking and Validation Sheets (2026-11-19)\n",
"## Ranking rule (stated, not weighted)\nDecision tier from Stage 5 first (GO, then GO-CONDITIONAL, then HOLD). Inside a tier: number of four evidence legs present (Y/N: competitor winner exists; Trends demand at least ~0.2 of the 'mortgage rates' anchor; competition not High-saturated; a live news/data hook in 2026-11), then the Trends ratio. No numeric weights are invented. A leg is a binary reading of Stage 5 evidence and inherits its limits (visual Trends, secondary news).\n",
"## Ranking\n","| Rank | ID | Topic | Decision | Legs (win/demand/competition/hook) | Trends ratio |\n|---|---|---|---|---|---|"]
for n,i in enumerate(order,1): md.append(f"| {n} | {i} | {T[i][1]} | {T[i][8]} | {L[i]} | {D[i]} |")
md+=["\nObservations (INFERRED):\n- Owner topics rank low on evidence: V1 Rent (E02) is rank %d and V2 Airfares (E08) rank %d of 16. Both lack a six-channel winner and have near-floor search demand; their case rests on owner choice, low competition and live data hooks (rent: missing-October-2025 CPI gap; airfares: record holiday fares, but V2's date 2026-12-21 is after holiday booking). This is a decision for the owner, not a result.\n- Highest-evidence topics are the inflation-basket (E06), housing lock-in (E01) and IPO mechanics (F02). E01 and E03 compete directly with Casual Finance's strongest clusters.\n- AI company finances (F01) has the highest demand of all and the highest saturation; it stays conditional.\n- Evergreen reserves (HOLD): fuel shocks (E09), ageing economies (E12).\n"%(order.index("E02")+1,order.index("E08")+1),
"## Nine-item validation sheets\nItems follow the strict audit's list: (1) competitor coverage, (2) upload date and recency, (3) competitor performance, (4) relevance to owner themes, (5) Google Trends, (6) news, (7) YouTube search, (8) DS-000011/18 and framework application, (9) original angle; then the final decision. The nine-item sheet was not defined in one place in the repository; the list above is the audit's own wording, so the owner should confirm it.\n"]
theme={"E01":"housing/rent (owner theme)","E02":"housing/rent (owner theme)","E03":"inflation-rates-debt (owner theme)","E04":"inflation-rates-debt (owner theme)","E06":"inflation-rates-debt (owner theme)","F04":"crises/history (owner theme)","F01":"AI bubble/IPO (owner theme)","F02":"AI bubble/IPO (owner theme)","F05":"AI bubble + crises/history (owner themes)","F10":"crises/history (partial)"}
for n,i in enumerate(order,1):
    t=T[i]
    md+=[f"### {n}. {i} — {t[1]}  **[{t[8]}]**\n",
    f"1. Competitor coverage (six channels): {t[2]}",
    f"2. Upload date / recency and performance of the top matched winners: {comp(i)} (keyword match on titles, so some rows may be only loosely related)",
    f"3. Competitor performance: see item 2 and the cluster note in item 8",
    f"4. Relevance to owner themes: {theme.get(i,'not an owner theme (Stage 4 evidence-derived)')}",
    f"5. Google Trends: {t[4]}",
    f"6. News: {t[5]}",
    f"7. YouTube search: {t[3]}",
    f"8. DS-000011/18 and framework: {t[6]}",
    f"9. Original angle (HYPOTHESIS): {t[7]}",
    f"- **Final decision: {t[8]}** — {t[9]}\n"]
s="\n".join(md); open("STAGE6_FINAL_RANKING_2026-11-19.md","w").write(s)
css="body{font:15px/1.5 system-ui;max-width:900px;margin:2em auto;padding:0 1em}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:4px 8px}"
open("STAGE6_FINAL_RANKING_2026-11-19.html","w").write(f"<meta charset=utf-8><style>{css}</style>"+markdown.markdown(s,extensions=["tables"]))
print(order)
