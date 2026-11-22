# Authoring for -Vr8JhCIv08 (360p, full-bleed, DEPTH_C). Run from research dir.
import json
v='videos/-Vr8JhCIv08/'
B=[0,117,206,250,280,303,391,582,692,767,789,891,971,1003,1163,1254,1323,1455,1491]
info=[
("US-map character; news card; DEBT papers pop in; red '$40T' pops","map character; news card; DEBT papers x6; red $40T; caption","CH_USMAP,SS_NEWS_CARD,PR_DEBTDOC,TY_RED","Hook: America crossed $40 trillion","START"),
("National-debt-clock banner screenshot; two figures with a gift box appear","banner screenshot; figures; caption","SS_DEBT_CLOCK,CH_FIG,CH_PEOPLE","More than $117,000 per person",None),
("Gross National Debt article page with a surprised man; red 'doubled'","article; man; red word; caption","SS_ARTICLE,CH_MAN,TY_RED","Doubled in 10 years",None),
("Same article; 'and quadrupled in the last 20'","article; man; caption","SS_ARTICLE,CH_MAN","Quadrupled in 20 years",None),
("Debt-clock banner with map character","banner; map character; caption","SS_DEBT_CLOCK,CH_USMAP","Hit $40 trillion ahead of schedule",None),
("Debt-clock banner + map character reaction","banner; map character; caption","SS_DEBT_CLOCK,CH_USMAP","Hit $40 trillion ahead of schedule",None),
("CBO baseline projections page with red '2028' and a host figure; map character grows; 'only deadline Washington has ever beaten'","CBO document pages (scroll/zoom); red 2028; host; map character; caption","SS_CBO_DOC,TY_RED,CH_HOST,CH_USMAP","CBO projected 2028; we got there two years early",None),
("Giant red '$40T' with DEBT papers and a man","red $40T (large); DEBT papers; man; caption","TY_RED,PR_DEBTDOC,CH_MAN","The $40 trillion number is the least interesting thing",None),
("Map character with DEBT paper and cash: 'a big debt at a low enough price'; bubble 'I can handle this!'","map character; DEBT paper; cash; bubble; caption","CH_USMAP,PR_DEBTDOC,PR_CASH,OV_BUBBLE","A big debt at a low price is survivable",None),
("Mortgage document, house and a woman: 'like a mortgage'","mortgage doc; house; woman; caption","PR_MORTGAGE,PR_HOUSE,CH_WOMAN","Analogy: mortgage",None),
("Host beside a DEBT document (glasses appear); 'what makes debt dangerous'","host; DEBT doc; caption","CH_HOST,PR_DEBTDOC","Not how much you owe, but what it costs",None),
("Host, money bags and a flattening map: 'it's what it costs to carry'","host; bags; map; caption","CH_HOST,PR_BAGS,CH_USMAP","Cost to carry",None),
("US interest-expense-per-day chart appearing","chart; caption","SS_INTEREST_CHART","'And right now...'",None),
("Interest chart then map character 'A DAY?!?'; second chart scene begins ('Over the next decade')","chart; map character; bubble; caption","SS_INTEREST_CHART,CH_USMAP,OV_BUBBLE","Three billion dollars a day",None),
("CBO interest-cost chart with money bags","CBO chart; logo; bags; caption","SS_CBO_CHART,LOGO_CBO,PR_BAGS","More than $16 trillion on interest",None),
("'That's money that buys...' bill; crossed-out roads, schools and research","bill; red X on road/school/research props; caption","PR_CASH,PR_ROAD,PR_SCHOOL,OV_REDX","Interest buys nothing",None),
("'Back then / And now': map characters split by a red line","two map characters; DEBT documents; red divider; bubbles; caption","CH_USMAP,PR_DEBTDOC,OV_DIVIDER,OV_BUBBLE","Rental fee on decisions already made",None),
("FRED interest-to-GDP chart with host pointing; red circle on 2025 value","chart; red circle; host; caption (end)","SS_FRED_CHART,OV_REDCIRCLE,CH_HOST","Interest eats 3.2% of GDP, seen only once before",None)]
S=[]
for k,(lab,lay,ass,pur,start) in enumerate(info):
    d=dict(id="S%02d"%(k+1),f0=B[k],f1=B[k+1],label=lab,layers=lay,assets=ass,transition_in="START" if start else "HARD_CUT",purpose=pur+" [ART_DIRECTION_INFERENCE]",notes="")
    if start: d["no_auto_cut"]=True
    S.append(d)
E=[]
json.dump(S,open(v+'review/scenes.json','w'),indent=1); json.dump(E,open(v+'review/events.json','w'),indent=1)
SC={s['id']:s for s in S}; A=[]
H="CHARACTER_STICK_FIGURE"
def fam(a):
    p=a.split('_')[0]
    return {"CH":H,"PR":"PROP_FINANCIAL","SS":"SOURCE_SCREENSHOT","TY":"TYPOGRAPHY_EMPHASIS","OV":"OVERLAY_ANNOTATION","LOGO":"SOURCE_LOGO"}[p]
over={"CH_USMAP":"CHARACTER_COUNTRY_MAP","PR_DEBTDOC":"PROP_FINANCIAL_PAPER","PR_MORTGAGE":"PROP_FINANCIAL_PAPER","PR_CASH":"PROP_MONEY","PR_BAGS":"PROP_MONEY","PR_HOUSE":"PROP_HOUSING","PR_ROAD":"PROP_OBJECT","PR_SCHOOL":"PROP_HOUSING"}
for s in S:
    for aid in s['assets'].split(','):
        A.append(dict(asset_id=aid,family=over.get(aid,fam(aid)),variant=s['label'][:60],scene=s['id'],f0=s['f0'],f1=s['f1'],role="",desc=""))
A.append(dict(asset_id="TY_CAPTION",family="TYPOGRAPHY_CAPTION",variant="hand-lettered marker caption",scene="S01",f0=0,f1=1491,role="captions",desc=""))
json.dump(A,open(v+'review/assets.json','w'),indent=1)
print(len(S),'scenes',len(A),'assets',S[-1]['f1'])
