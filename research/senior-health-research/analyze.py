#!/usr/bin/env python3
"""Senior-health top-viewed topics + hook patterns. Read-only on data/catalog/senior_health_complete.db.
Facts = DB numbers. Topic/hook labels = rule-based keyword classifiers (AI-interpretation, see README)."""
import sqlite3, re, csv, statistics as st, collections, os
OUT=os.path.dirname(os.path.abspath(__file__))
db=sqlite3.connect(os.path.join(OUT,'../../data/catalog/senior_health_complete.db'))
rows=db.execute("""select v.video_id,v.channel_id,c.name,c.tier,v.title,v.views,v.duration_seconds,v.video_type,v.published,
 t.text from videos v join channels c using(channel_id) left join transcripts t using(video_id)
 where v.views is not null""").fetchall()
cols="vid cid chan tier title views dur vtype pub text".split()
V=[dict(zip(cols,r)) for r in rows]
# long-form only: not shorts/streams, >=181s (excludes shorts)
V=[v for v in V if v['vtype'] not in('shorts','streams') and (v['dur'] or 0)>=180]
bych=collections.defaultdict(list)
for v in V: bych[v['cid']].append(v)
ok={c for c,l in bych.items() if len(l)>=10}
V=[v for v in V if v['cid'] in ok]
for c in ok:
    m=st.median(x['views'] for x in bych[c]); 
    for x in bych[c]: x['rel']=x['views']/m if m else 0   # views / channel median
print('long-form videos',len(V),'channels',len(ok))
TOP={
 'knee':r'\bknees?\b','shoulder/rotator':r'shoulder|rotator|rhomboid','back/spine/sciatica':r'\bback\b|spine|sciatica|lumbar|disc\b|stenosis',
 'neck':r'\bneck\b|pinched nerve','hip':r'\bhips?\b|glute','feet/plantar/neuropathy':r'\bfeet\b|\bfoot\b|plantar|neuropathy|toe|ankle',
 'hands/arthritis':r'arthritis|\bhands?\b|fingers?|carpal|joint',
 'balance/falls':r'balance|\bfalls?\b|falling|dizz','memory/brain/dementia':r'memory|brain|dementia|alzheimer|cognitive',
 'heart/blood pressure':r'heart|blood pressure|cholesterol|stroke|artery|arteries','diabetes/blood sugar':r'diabet|blood sugar|glucose|insulin',
 'sleep':r'\bsleep|insomnia','vitamins/supplements':r'vitamin|supplement|magnesium|collagen|omega|b12|creatine|probiotic',
 'food/diet':r'\beat\b|food|diet|protein|fruit|breakfast|egg|fasting|drink|coffee|water\b',
 'chair/seated':r'\bchair\b|seated|sitting','walking':r'\bwalk','strength/muscle':r'strength|muscle|sarcopenia|squat|weights?\b|dumbbell|resistance',
 'stretching/mobility':r'stretch|mobility|flexib|yoga|tai chi','weight loss/belly':r'weight loss|belly|lose weight|fat\b',
 'eyes/hearing':r'\beyes?\b|vision|cataract|glaucoma|hearing','gut/digestion':r'\bgut\b|digest|constipation|bowel',
 'bone/osteoporosis':r'osteopor|bone','longevity/aging':r'longevity|anti-?aging|live longer|aging|ageing|young',
 'kidney/liver':r'kidney|liver','medications/drugs':r'medication|drugs?\b|statin|pills?\b',
}
FMT={
 'number in title':r'\b\d+\b','age callout (over 50/60/70..)':r'(over|after|above|at|past)\s*(age\s*)?(4\d|5\d|6\d|7\d|8\d)|\b(5|6|7|8)0s?\b|seniors?|elderly|older adults?',
 'question':r'\?|^(why|how|what|should|can|is|are|do|does)\b','warning/avoid/stop':r'\b(never|avoid|stop|don.t|dont|mistakes?|worst|danger|warning|bad for|ruin)',
 'how-to/fix':r'^how to|\bfix|relief|remedy|cure|heal|get rid','"exercise/workout" format':r'exercise|workout|routine|movements?',
 'ALL-CAPS word':r'\b[A-Z]{4,}\b','emoji/symbol':r'[☀-➿\U0001F300-\U0001FAFF]',
 'secret/doctor/truth':r'secret|doctor|truth|nobody|no one|they don.t|hidden|shocking|surprising',
}
def lab(v,D): return [k for k,p in D.items() if re.search(p,v['title'],0 if k=='ALL-CAPS word' else re.I)]
def table(D,name):
    res=[]
    for k in D:
        s=[v for v in V if k in lab(v,D)]
        if len(s)<15: continue
        chs=collections.defaultdict(list)
        for v in s: chs[v['cid']].append(v['rel'])
        allc=collections.defaultdict(list)
        for v in V: allc[v['cid']].append(v['rel'])
        # per-channel: label median vs rest-of-channel median, only channels with >=3 labelled
        wins=tot=0
        for c,l in chs.items():
            if len(l)>=3:
                rest=[x['rel'] for x in bych[c] if k not in lab(x,D)]
                if len(rest)>=3: tot+=1; wins+= st.median(l)>st.median(rest)
        res.append((k,len(s),len(chs),round(st.median(v['rel'] for v in s),2),round(st.mean(v['views'] for v in s)),wins,tot,
                    sum(v['views'] for v in s)))
    res.sort(key=lambda r:-r[3])
    with open(f'{OUT}/{name}.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['label','n_videos','n_channels','median_rel_views(1=channel median)','mean_views','channels_where_label_beats_rest','channels_testable','total_views']); w.writerows(res)
    return res
t1=table(TOP,'topics_by_relative_views'); t2=table(FMT,'title_formats_by_relative_views')
# top 100 raw-view videos with provenance
top=sorted(V,key=lambda v:-v['views'])[:100]
with open(f'{OUT}/top100_videos_by_views.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['video_id','channel_id','channel','tier','title','views','rel_to_channel_median','duration_s','published','topic_labels'])
    for v in top: w.writerow([v['vid'],v['cid'],v['chan'],v['tier'],v['title'],v['views'],round(v['rel'],1),v['dur'],v['pub'],';'.join(lab(v,TOP))])
# topics among top 100 vs base rate
base=collections.Counter(k for v in V for k in lab(v,TOP)); tc=collections.Counter(k for v in top for k in lab(v,TOP))
with open(f'{OUT}/topics_top100_vs_base.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['topic','share_in_top100','share_in_all_longform','lift'])
    for k in sorted(base,key=lambda k:-(tc[k]/100)/(base[k]/len(V))):
        w.writerow([k,round(tc[k]/100,3),round(base[k]/len(V),3),round((tc[k]/100)/(base[k]/len(V)),2)])
# ---------- hooks ----------
H=[v for v in V if v['text']]
def first(v,n=60): return ' '.join(v['text'].split()[:n])
HOOK={
 'greeting/welcome opener':r'\b(hi|hello|hey|welcome|good (morning|day))\b|welcome back',
 'question in first 60 words':r'\?', 'second-person "you/your"':r'\byou(r|\'re|\'ve)?\b',
 'age/senior address (over 50/60..)':r'(over|after|above)\s*(the age of\s*)?(4\d|5\d|6\d|7\d|8\d)|seniors?|older adults?|elderly|\b(5|6|7|8)0s\b',
 'number/statistic':r'\b\d+(\.\d+)?\s*(%|percent|million|billion|years?|minutes?|seconds?|days?|weeks?|times)\b|\b\d+ (things|ways|exercises|foods|mistakes|signs|tips|reasons|minutes)',
 'warning/danger/mistake':r'\b(danger|dangerous|never|stop|avoid|mistake|warning|risk|worst|harm|damage|ruin)\b',
 'promise/benefit':r'\b(by the end|i.ll show|i will show|you.ll learn|you will learn|in this video|today (i|we)|going to (show|teach|share|learn))\b',
 'credential/authority (doctor, PT, years)':r'\b(dr\.?|doctor|physical therap|physio|years of experience|clinic|i.m a|my patients|research shows|studies?)\b',
 'personal story/first person':r'\b(my (mother|mom|father|dad|grand|patient|client|wife|husband)|i remember|years ago|a patient|i was)\b',
 'direct command / do-this-now':r'\b(try this|do this|grab|stand up|sit down|let.s (start|begin|get))\b',
}
def hl(v): return [k for k,p in HOOK.items() if re.search(p,first(v),re.I)]
res=[]
for k in HOOK:
    s=[v for v in H if k in hl(v)]
    if len(s)<15: continue
    chs=collections.defaultdict(list)
    for v in s: chs[v['cid']].append(v['rel'])
    wins=tot=0
    for c,l in chs.items():
        if len(l)>=3:
            rest=[x['rel'] for x in H if x['cid']==c and k not in hl(x)]
            if len(rest)>=3: tot+=1; wins+=st.median(l)>st.median(rest)
    rest_all=[v['rel'] for v in H if k not in hl(v)]
    res.append((k,len(s),len(chs),round(st.median(v['rel'] for v in s),2),round(st.median(rest_all),2),wins,tot))
res.sort(key=lambda r:-r[3])
with open(f'{OUT}/hook_patterns_by_relative_views.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['hook_label','n_videos','n_channels','median_rel_views_with','median_rel_views_without','channels_where_beats_rest','channels_testable']); w.writerows(res)
# hook samples: first 40 words of top 25 transcripted videos by rel views and bottom 25
H2=sorted([v for v in H if v['views']>1000],key=lambda v:-v['rel'])
with open(f'{OUT}/hook_samples_top_vs_bottom.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['group','video_id','channel','title','views','rel','first_40_words'])
    for g,l in(('TOP',H2[:30]),('BOTTOM',H2[-30:])):
        for v in l: w.writerow([g,v['vid'],v['chan'],v['title'],v['views'],round(v['rel'],2),first(v,40)])
print('transcripted long-form',len(H),'channels',len({v['cid'] for v in H}))
for name,r in(('TOPICS',t1),('FORMATS',t2)):
    print(name)
    for x in r: print(' ',x[:7])
print('HOOKS'); 
for x in res: print(' ',x)
