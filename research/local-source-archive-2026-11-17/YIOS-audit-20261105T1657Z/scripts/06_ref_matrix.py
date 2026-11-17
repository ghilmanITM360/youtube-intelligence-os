#!/usr/bin/python3 -I
# Read-only. Inputs: canonical repo refs, fresh ls-remote, mirror. Output: raw/refs/ref_matrix.csv
import subprocess as sp,csv,os,json,re
H=os.path.expanduser('~');A=H+'/YIOS-audit-20261105T1657Z/';R=H+'/workprojects/youtube-intelligence-os';M=A+'scratch/remote_mirror.git'
E=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
def g(*a,d=R):
    p=sp.run(['git','-C',d,*a],capture_output=True,text=True,env=E,errors='replace');return p.stdout.strip() if p.returncode==0 else None
wt={}
cur=None
for l in (g('worktree','list','--porcelain') or '').splitlines():
    if l.startswith('worktree '):cur=l[9:]
    if l.startswith('branch '):wt[l[7:]]=cur
lr={}
for l in open(A+'raw/refs/ls_remote_final.txt'):
    s,n=l.split('\t');lr[n.strip()]=s
prs={x['headRefName']:x for x in json.load(open(A+'raw/remote/prs.json'))}
rows=[]
F='%(refname)\t%(objectname)\t%(objecttype)\t%(committerdate:iso-strict)\t%(upstream)\t%(subject)'
L=[('local',l) for l in (g('for-each-ref','--format='+F) or '').splitlines()]
Mr=[('mirror',l) for l in (g('for-each-ref','--format='+F,d=M) or '').splitlines()]
def inm(s): return g('cat-file','-e',s,d=M) is not None
main=g('rev-parse','refs/heads/main',d=M)
rep=dict()
for src,l in L+Mr:
    n,s,t,dt,up,sub=l.split('\t',5)
    if src=='mirror' and n.startswith('refs/heads/') and False: continue
    d=dict(store=src,ref=n,sha=s,type=t,date=dt,upstream=up,subject=sub[:90])
    d['on_remote_same_name']=lr.get(n.replace('refs/remotes/origin/','refs/heads/'),'')==s if src=='local' else True
    d['remote_sha_same_name']=lr.get(n.replace('refs/remotes/origin/','refs/heads/'),'')
    d['object_in_independent_mirror']=inm(s) if src=='local' else True
    D=R if src=='local' else M
    if t=='commit':
        if up: 
            ab=g('rev-list','--left-right','--count',f'{n}...{up}',d=D); d['ahead_upstream'],d['behind_upstream']=(ab.split() if ab else ('',''))
        m='refs/remotes/origin/main' if src=='local' else 'refs/heads/main'
        ab=g('rev-list','--left-right','--count',f'{n}...{m}',d=D)
        if ab: d['ahead_main'],d['behind_main']=ab.split()
        if src=='local':
            lst=[x for x in (g('rev-list',n) or '').splitlines()]
            un=[c for c in lst[:4000] if not inm(c)] if not d['object_in_independent_mirror'] else []
            d['commits_absent_from_mirror']=len(un)
            if un:
                base=un[-1]
                fl=g('diff','--name-only',base+'^',n) or ''
                d['files_changed_since_first_unique']=len(fl.splitlines())
    b=n.replace('refs/heads/','').replace('refs/remotes/origin/','')
    d['worktree']=wt.get(n,'')
    p=prs.get(b)
    if p: d['pr']=p['number'];d['pr_state']=p['state'];d['pr_draft']=p['isDraft'];d['ci']=','.join(sorted({(c.get('conclusion') or '') for c in p['statusCheckRollup']}))
    rows.append(d)
K=['store','ref','sha','type','date','upstream','ahead_upstream','behind_upstream','ahead_main','behind_main','on_remote_same_name','remote_sha_same_name','object_in_independent_mirror','commits_absent_from_mirror','files_changed_since_first_unique','worktree','pr','pr_state','pr_draft','ci','subject']
w=csv.DictWriter(open(A+'raw/refs/ref_matrix.csv','w'),K,extrasaction='ignore');w.writeheader();w.writerows(rows)
print(len(rows))
