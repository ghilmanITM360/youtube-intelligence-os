import os,re,csv,hashlib,sys,time,collections
H='/Users/ghilmanislam360/Documents/'
F=['YIOS-Visual-Forensics-Discovery-2026-10-28','YIOS-handoffs','YIOS-Creator-Intelligence-Audit-2026-10-26','YIOS-Algorithm-Audit-2026-10-26','YIOS-local-audits','yios-worktree-preservation-2026-10-21','YIOS-Media-Library','YIOS-recovery-2026-10-19-finance-short-experiment-01','yios-local-preservation-2026-10-12']
NAME=re.compile(r'xkcd|what[ _-]?if|whatif|munroe|ch-?000004|ds-?000017|UC6IxnFzHofFJ5X2PycSMsww',re.I)
TXT={'.md','.txt','.csv','.json','.tsv','.sh','.py','.srt','.vtt','.html','.yaml','.yml'}
SELF='2026-11-23-xkcd-what-if-complete-forensics'
def cat(p):
    e=os.path.splitext(p)[1].lower()
    return {'.mp4':'video','.mov':'video','.wav':'audio','.mp3':'audio','.m4a':'audio','.png':'image','.jpg':'image','.jpeg':'image','.csv':'table','.tsv':'table','.json':'json','.md':'doc','.txt':'text','.srt':'subtitle','.vtt':'subtitle','.pdf':'pdf','.xlsx':'sheet','.db':'database'}.get(e,e or 'noext')
rows=[];stat=collections.defaultdict(lambda:[0,0,0])
for f in F:
    for dp,dn,fn in os.walk(H+f):
        if SELF in dp: dn[:]=[];continue
        for n in fn:
            p=os.path.join(dp,n); stat[f][0]+=1
            try: sz=os.path.getsize(p)
            except: continue
            hit=bool(NAME.search(p[len(H):]))
            ch=''
            if not hit and os.path.splitext(n)[1].lower() in TXT and sz<2_000_000 and f!='YIOS-local-audits':
                try:
                    if NAME.search(open(p,errors='ignore').read()): hit=True;ch='CONTENT'
                except: pass
            if hit:
                stat[f][1]+=1
                sha=''
                if sz<30_000_000 and not n.endswith('.mp4'):
                    h=hashlib.sha256();h.update(open(p,'rb').read());sha=h.hexdigest()
                rows.append(dict(folder=f,path=p,category=cat(p),size=sz,mtime=time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime(os.path.getmtime(p))),sha256=sha,match='NAME' if not ch else 'CONTENT'))
w=csv.DictWriter(open('02_WHAT_IF_RELATED_FILE_REGISTER.csv','w'),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for f in F: print(f,'total files',stat[f][0],'related',stat[f][1])
c=collections.Counter((r['folder'],r['category']) for r in rows)
for k,v in sorted(c.items()): print(k,v)
