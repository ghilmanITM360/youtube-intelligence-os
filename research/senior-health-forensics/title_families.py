#!/usr/bin/env python3
"""Cross-channel near-identical title clusters over the 44 queue channels (read-only DB).
Jaccard>=0.75 on lowercase word sets, union-find. Views/dates are DB values (mixed capture times; see reports). Output: title_families.csv"""
import sqlite3,re,csv,os
H=os.path.dirname(os.path.abspath(__file__))
c=sqlite3.connect(f'file:{H}/../../data/catalog/senior_health_complete.db?mode=ro',uri=True)
q=list(csv.DictReader(open(f'{H}/queue.csv'))); num={r['channel_id']:r['n'] for r in q}
rows=c.execute("select video_id,channel_id,title,substr(published,1,10),views,source from videos where channel_id in (%s)"%','.join('?'*len(num)),list(num)).fetchall()
tok=[frozenset(re.sub(r'[^a-z0-9 ]',' ',r[2].lower()).split()) for r in rows]
p=list(range(len(rows)))
def f(x):
    while p[x]!=x: p[x]=p[p[x]]; x=p[x]
    return x
for i in range(len(rows)):
    for j in range(i+1,len(rows)):
        if rows[i][1]!=rows[j][1]:
            u=tok[i]|tok[j]
            if u and len(tok[i]&tok[j])/len(u)>=0.75: p[f(i)]=f(j)
g={}
for i in range(len(rows)): g.setdefault(f(i),[]).append(i)
out=[]; k=0
for m in sorted(g.values(),key=lambda m:-len({rows[i][1] for i in m})):
    if len({rows[i][1] for i in m})<2: continue
    k+=1
    for i in sorted(m,key=lambda i:rows[i][3] or '9'):
        r=rows[i]; out.append([k,num[r[1]],r[0],r[3] or '',r[4] if r[4] is not None else '',r[5],r[2]])
w=csv.writer(open(f'{H}/title_families.csv','w',newline=''),lineterminator='\n'); w.writerow(['family','channel_n','video_id','date','db_views','db_source','title']); w.writerows(out)
print(k,'families,',len(out),'videos,',len({o[1] for o in out}),'channels')
