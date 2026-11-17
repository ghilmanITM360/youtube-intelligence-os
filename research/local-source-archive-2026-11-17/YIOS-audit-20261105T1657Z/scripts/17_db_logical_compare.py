import sqlite3,hashlib,sys,json
a,b=sys.argv[1:3]
def t(p):
    c=sqlite3.connect(f'file:{p}?mode=ro',uri=True);out={}
    names=[r[0] for r in c.execute("select name from sqlite_master where type='table' and name not like 'sqlite_%'")]
    vs={r[0] for r in c.execute("select name from sqlite_master where type='table' and sql like 'CREATE VIRTUAL%'")}
    shadow=lambda n:any(n.startswith(v+'_') for v in vs)
    for n in names:
        if shadow(n):continue
        h=hashlib.sha256();k=0
        for r in sorted((repr(x) for x in c.execute(f'select * from "{n}"'))):h.update(r.encode());k+=1
        out[n]=(k,h.hexdigest()[:16])
    return out,c.execute('pragma integrity_check').fetchone()[0],len(c.execute('pragma foreign_key_check').fetchall())
x,ix,fx=t(a);y,iy,fy=t(b)
same=[n for n in x if y.get(n)==x[n]];diff=[(n,x[n][0],y.get(n,(None,))[0]) for n in sorted(set(x)|set(y)) if x.get(n)!=y.get(n)]
print(json.dumps({'a':a.split('/')[-1],'b':b.split('/')[-1],'integrity':[ix,iy],'fk':[fx,fy],'tables_a':len(x),'tables_b':len(y),'identical_tables':len(same),'different':diff},indent=0))
