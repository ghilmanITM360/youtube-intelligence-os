import csv,os,collections,json,statistics as st
H=os.path.expanduser('~/YIOS-local-audits/')
ids=['CFrVTZBYa3Q','10nEByVLya0','turJ6VMfUjI','SYSUh-oow6M','eePIUX0Sd6c','yViMyIVOHkQ','Xkk9GnnJHBg','DKyJABtbF2o','RXFBHYxyqdk','hbsYaLaN_F8','dPoDyl9Ys38','7K991LgY3tc','WCS1bK3KB3U','KTnp2OlQJHA','Im-N3K9Pnf0']
HELD=['10nEByVLya0','Xkk9GnnJHBg','7K991LgY3tc','SYSUh-oow6M']  # 2 shorts-era mix chosen before fitting: one short x2, two long
def norm(c):
    c=c.split('+')[0].strip()
    return c if c in('CUT','POP_IN','POSE','TEXT_SWAP','START') else 'OTHER'
def ctype(a,prev):
    t=set(x.split('_')[0] for x in a.split(';') if x)
    key='CH' if 'CH' in t else ('GFX' if 'GFX' in t else ('OBJ' if 'OBJ' in t else ('IMG' if 'IMG' in t or 'ICON' in t else 'OTHER')))
    return key
rows=[]
for v in ids:
    p=H+f'2026-11-08-{v}-deep-ct-scan/visual_states.csv'
    prev=None
    for r in csv.DictReader(open(p)):
        r['vid']=v;r['cls']=norm(r['entering_class']);r['ct']=ctype(r['asset_ids'],prev);r['dur']=float(r['duration_s']);rows.append(r)
tr=[r for r in rows if r['vid'] not in HELD];te=[r for r in rows if r['vid'] in HELD]
# rule: content type + previous entering class -> entering class
def fit(tr):
    m=collections.defaultdict(collections.Counter);m1=collections.defaultdict(collections.Counter);base=collections.Counter()
    prev=None
    for i,r in enumerate(tr):
        pc=tr[i-1]['cls'] if i and tr[i-1]['vid']==r['vid'] else 'NONE'
        m[(r['ct'],pc)][r['cls']]+=1;m1[r['ct']][r['cls']]+=1;base[r['cls']]+=1
    return m,m1,base
m,m1,base=fit(tr)
def pred(i,te):
    r=te[i];pc=te[i-1]['cls'] if i and te[i-1]['vid']==r['vid'] else 'NONE'
    k=(r['ct'],pc)
    if k in m and sum(m[k].values())>=5:return m[k].most_common(1)[0][0]
    if r['ct'] in m1:return m1[r['ct']].most_common(1)[0][0]
    return base.most_common(1)[0][0]
acc=sum(pred(i,te)==r['cls'] for i,r in enumerate(te))/len(te)
bm=base.most_common(1)[0][0];bacc=sum(r['cls']==bm for r in te)/len(te)
# duration: median by (ct, cls) vs global median; MAE
med=collections.defaultdict(list)
for r in tr:med[(r['ct'],r['cls'])].append(r['dur'])
g=st.median(r['dur'] for r in tr)
e1=[abs(r['dur']-st.median(med[(r['ct'],r['cls'])]) if (r['ct'],r['cls']) in med else abs(r['dur']-g)) for r in te]
e0=[abs(r['dur']-g) for r in te]
# per-video accuracy
pv={}
for v in HELD:
    idx=[i for i,r in enumerate(te) if r['vid']==v];pv[v]=round(sum(pred(i,te)==te[i]['cls'] for i in idx)/len(idx),3)
out=dict(train_states=len(tr),test_states=len(te),held_out=HELD,accuracy=round(acc,3),majority_baseline=bm,baseline_acc=round(bacc,3),per_video=pv,dur_mae_model=round(st.mean(e1),3),dur_mae_global_median=round(st.mean(e0),3),
 class_dist_train=dict(base))
print(json.dumps(out,indent=1))
json.dump(out,open('de.json','w'))
tbl=[]
for (ct,pc),c in sorted(m.items(),key=lambda x:-sum(x[1].values())):
    n=sum(c.values())
    if n>=15: tbl.append((ct,pc,n,c.most_common(1)[0][0],round(c.most_common(1)[0][1]/n,2)))
print(tbl[:12])
json.dump(tbl,open('rules.json','w'))
