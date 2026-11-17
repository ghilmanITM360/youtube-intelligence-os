#!/usr/bin/python3 -I
# SQLite audit opened read-only (mode=ro). Never writes to source DBs. Skips -wal/-shm.
import os,sqlite3,json,time,sys
H=os.path.expanduser('~');A=H+'/YIOS-audit-20261105T1657Z/raw/'
out=[]
sha={}
paths=[]
for l in open(A+'hash/index.tsv',encoding='utf8',errors='surrogateescape'):
    s,z,m,p=l.rstrip('\n').split('\t',3)
    if int(z)<100: continue
    if p.endswith(('.db','.sqlite','.sqlite3')): paths.append((p,s,int(z)))
FTS=('_data','_idx','_content','_docsize','_config')
for p,s,z in paths:
    r=dict(path=p,sha256=s,size=z)
    try:
        c=sqlite3.connect('file:'+p.replace('?','%3f').replace('#','%23')+'?mode=ro',uri=True,timeout=3)
        c.execute('PRAGMA query_only=1')
        r['integrity']=c.execute('PRAGMA quick_check' if z>(300<<20) else 'PRAGMA integrity_check').fetchone()[0]
        r['fk_violations']=len(c.execute('PRAGMA foreign_key_check').fetchall())
        T=[x for x in c.execute("select name,sql from sqlite_master where type='table' and name not like 'sqlite_%'")]
        fts=[n for n,q in T if q and 'fts' in q.lower() and 'virtual' in q.lower()]
        shadow=[n for n,q in T if any(n==f+e for f in fts for e in FTS)]
        tb={}
        for n,q in T:
            if n in shadow or n in fts: continue
            try: tb[n]=c.execute(f'select count(*) from "{n}"').fetchone()[0]
            except Exception as e: tb[n]='ERR '+str(e)[:40]
        r['tables']=tb;r['fts']=fts;r['shadow_count']=len(shadow)
        r['user_version']=c.execute('PRAGMA user_version').fetchone()[0]
    except Exception as e: r['error']=str(e)[:120]
    out.append(r)
json.dump(out,open(A+'db/db_audit.json','w'),indent=0)
print(len(out))
