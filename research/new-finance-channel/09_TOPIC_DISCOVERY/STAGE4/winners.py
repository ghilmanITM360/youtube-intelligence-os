import sys,csv,statistics as st
sys.path.insert(0,'../../03_PRIMARY_REFERENCE_CHANNELS/STAGE2_SIX_REPORTS'); import build_data as B
out=[]
for s in B.CH:
    nm,cid,R=B.load(s)
    for kind,flt in (('L',lambda r:not r['short']),('S',lambda r:r['short'])):
        V=[r for r in R if flt(r) and r['views'] and not r['member']]
        if len(V)<3: continue
        cm=st.median([r['views'] for r in V])
        for r in V:
            pi=r['views']/cm
            if (kind=='L' and pi>=2) or (kind=='S' and pi>=5):
                out.append([nm,kind,r['id'],r['date'],r['views'],round(pi,1),r['cat'],r['kind'],r['title'],r['url']])
out.sort(key=lambda x:(-x[5] if x[1]=='L' else 0,))
with open('winners_2026-11-19.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['channel','type','id','date','views','pi','sub_niche','fe','title','url']); w.writerows(out)
print(len(out),sum(1 for o in out if o[1]=='L'))
for o in out: print(o[0][:9],o[1],o[3],o[4],o[5],o[6][:12],'|',o[8][:70])
