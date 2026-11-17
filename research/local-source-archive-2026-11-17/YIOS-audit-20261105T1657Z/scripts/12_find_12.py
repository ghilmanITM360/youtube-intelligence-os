# Hash every historical blob at each target basename in mirror+canonical and compare with the 12 Finance/NICK targets. Read-only; no lazy fetch.
import subprocess,hashlib,csv,os,collections,json
A=os.path.expanduser('~/YIOS-audit-20261105T1657Z');M=A+'/scratch/remote_mirror.git';R=os.path.expanduser('~/workprojects/youtube-intelligence-os')
env=dict(os.environ,GIT_NO_LAZY_FETCH='1',GIT_OPTIONAL_LOCKS='0')
rows=[r for r in csv.DictReader(open(A+'/raw/hash/target_comparison.csv',newline='')) if r['source']=='machine_b_manifest_source_identities' and r['verdict']!='VERIFIED' and not r['verdict'].startswith('FOUND') ]
T={}
for r in rows:
    if int(r['found_count'] or 0)==0: T.setdefault(r['sha256'],[]).append(r)
print('targets',len(T))
names={os.path.basename(x[0]['recorded_path']) for x in T.values()}
out=[]
for label,repo in (('mirror',M),('canonical',R)):
    seen={}
    p=subprocess.Popen(['git','-C',repo,'rev-list','--objects','--all','--missing=allow-any'],stdout=subprocess.PIPE,text=True,env=env,errors='replace')
    for l in p.stdout:
        s=l.rstrip('\n').split(' ',1)
        if len(s)==2 and os.path.basename(s[1]) in names and s[0] not in seen: seen[s[0]]=s[1]
    print(label,'candidate blobs',len(seen))
    for b,path in seen.items():
        d=subprocess.run(['git','-C',repo,'cat-file','blob',b],capture_output=True,env=env)
        if d.returncode: out.append((label,'UNREADABLE',b,path,0,''));continue
        data=d.stdout
        if data.startswith(b'version https://git-lfs'):
            o=[x for x in data.decode().splitlines() if x.startswith('oid')]
            h=o[0].split(':')[1];sz=0;k='LFS_POINTER'
        else: h=hashlib.sha256(data).hexdigest();sz=len(data);k='BLOB'
        out.append((label,k,b,path,sz,h,'MATCH' if h in T else 'other_version'))
w=csv.writer(open(A+'/raw/hash/twelve_git_history.csv','w',newline=''));w.writerow('store kind blob path size sha256 result'.split());w.writerows(out)
print(collections.Counter((o[0],o[1],o[-1]) for o in out))
print('MATCHED targets:',sorted({o[5][:16] for o in out if o[-1]=='MATCH'}))
# same-basename files on disk in the hash index
idx=collections.defaultdict(list)
for l in open(A+'/raw/hash/index.tsv',errors='replace'):
    f=l.rstrip('\n').split('\t')
    if len(f)>=2 and os.path.basename(f[-1]) in names: idx[os.path.basename(f[-1])].append(f)
with open(A+'/raw/hash/twelve_local_samename.txt','w') as o:
    for n in sorted(names):
        print(n,len(idx[n]),file=o)
        for f in idx[n][:8]: print('  ',*f,sep='\t',file=o)
print({n:len(idx[n]) for n in sorted(names)})
