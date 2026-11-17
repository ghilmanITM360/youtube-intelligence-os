# Content-based: every local non-media file -> git blob sha -> present in stream-branch tip / any remote history?
import subprocess,hashlib,json,collections,os,sys,time
from pathlib import Path
S=Path(sys.argv[0]).parent;repo=str(Path.home()/'workprojects/youtube-intelligence-os');A=Path.home()/'YIOS-local-audits'
out=subprocess.run('git rev-list --objects --missing=print --remotes=origin | cut -d" " -f1 | sed s/^?//',shell=True,cwd=repo,capture_output=True,text=True).stdout.split()
hist=set(out);print('remote history objects',len(hist))
def tip(ref):
    o=subprocess.check_output(['git','ls-tree','-r',ref],cwd=repo,text=True);return {l.split()[2] for l in o.splitlines()}
MEDIA={'.png','.jpg','.jpeg','.mp4','.wav','.mp3','.m4a','.webm','.mkv','.mov','.index','.pyc','.npy','.npz','.zip','.bundle','.db','.gif','.webp','.mpg','.pack','.bin','.pt','.pth','.onnx','.ttf','.otf'}
SKIP={'__pycache__','.venv','venv','asr-venv','node_modules','.git','visual-ct-scan-venv'}
CF='origin/research/casually-finance-editing-forensics';FM='origin/codex/finance-machine-a-owner-directed'
streams=[('PrimitiveEducation',A/'primitive-education','origin/research/primitive-education-visual-forensics'),
('xkcd',A/'xkcd-whatif','origin/research/xkcd-whatif-visual-forensics'),
('BarelyEvolved',A/'barely-evolved','origin/research/barely-evolved-visual-forensics'),
('CF-V003-5umJ',A/'2026-10-24-5umJ63d3rzQ-deep-ct-scan',CF),('CF-V004-0ll9',A/'2026-10-31-0ll9rEtoRrs-deep-ct-scan',CF),('CF-V005-X6Yz',A/'2026-11-01--X6YzlY_8tM-deep-ct-scan',CF),('CF-V006-xtqb',A/'2026-11-01--xtqbRt94TTw-deep-ct-scan',CF),
('CF-V006-EP0002',A/'Casual-Finance-Video006-EP0002-20261105T184819Z',CF),('CF-V006-progress',A/'Casual-Finance-Video006-progress-20261105T1844Z',CF),('CF-V006-followup(ACTIVE)',A/'Casual-Finance-Video006-followup-20261106T0330Z',CF),('CF-35target',A/'CASUALLY_FINANCE_35_VIDEO_TARGET_20261104',CF),
('Uumnx',A/'2026-10-24-Uumnx2Fo6cE-deep-ct-scan',CF),('o3FQ',A/'2026-10-24-o3FQcd91MIs-deep-ct-scan',CF),('7ch-readiness',A/'2026-10-24-seven-channel-visual-forensics-readiness',CF),
('NICK166',A/'2026-10-24-NICK_166',FM),('NICK167',A/'2026-10-24-NICK_167',FM),('NICK168',A/'2026-10-24-NICK_168',FM),('NICK169',A/'2026-10-25-NICK_169',FM),('NICK170',A/'2026-10-25-NICK_170',FM),('phase0',A/'2026-10-25-machine-a-phase0',FM),('phase1a',A/'2026-10-25-machine-a-phase1a',FM),('phase1b',A/'2026-10-25-machine-a-phase1b',FM),
('YIOS-bulk',A/'YIOS-bulk-20261025T2140Z-chat-01a174dd',FM),('YIOS-pilot',A/'YIOS-pilot-20261025T2120Z-chat-01a174dd',FM),('2026-10-21',A/'2026-10-21',FM),('2026-10-22',A/'2026-10-22',FM),('2026-10-23',A/'2026-10-23',FM),('2026-10-24',A/'2026-10-24',FM),
('untracked:finance-short-02',Path(repo)/'finance-short-02-visual-calibration','origin/production/finance-short-02-assets'),('untracked:productions',Path(repo)/'productions','origin/production/senior-health-casually-finance-three-videos'),('untracked:cf-script-intel',Path(repo)/'research/casually-finance-script-intelligence',CF),
('cf-local-evidence',Path.home()/'workprojects/yio-cf-editing-forensics-local-evidence',CF),('yios-recovery-status',Path.home()/'workprojects/yios-recovery-status',CF)]
res={}
for name,d,ref in streams:
    if not d.exists():print(name,'NO DIR');continue
    T=tip(ref);n=at=inh=0;absent=[];media=collections.Counter();mb=0;latest=0
    for r,ds,fs in os.walk(d):
        ds[:]=[x for x in ds if x not in SKIP]
        for f in fs:
            if f=='.DS_Store':continue
            x=Path(r)/f
            try:st=x.stat()
            except OSError:continue
            if x.suffix.lower() in MEDIA:media[x.suffix.lower()]+=1;mb+=st.st_size;continue
            if st.st_size>50_000_000:media['big']+=1;mb+=st.st_size;continue
            b=x.read_bytes();g=hashlib.sha1(b'blob %d\0'%len(b)+b).hexdigest();n+=1;latest=max(latest,st.st_mtime)
            if g in T:at+=1
            if g in hist:inh+=1
            else:absent.append((str(x.relative_to(d)),st.st_size,int(st.st_mtime)))
    res[name]=dict(ref=ref,nonmedia=n,at_tip=at,in_history=inh,absent=absent,media=dict(media),media_mb=round(mb/1e6,1))
    top=collections.Counter(a[0].split('/')[0] for a in absent).most_common(6)
    print(f"{name}: nonmedia {n} at_tip {at} in_history {inh} absent {len(absent)} media {sum(media.values())} ({mb/1e6:.0f}MB) newest {time.strftime('%m-%dT%H:%MZ',time.gmtime(latest))} | absent_top {top}")
json.dump(res,open(S/'stream_compare.json','w'),indent=1)
# stash / local-only refs: new blobs vs remote history
def blobs_of(c):return {l.split()[2]:l.split('\t')[1] for l in subprocess.check_output(['git','ls-tree','-r',c],cwd=repo,text=True).splitlines() if l.split()[1]=='blob'}
for label,c in [('stash',"5b6c3042"),('stash-index','d114cc36'),('stash-untracked','e9b7c70c'),('backup/decode','backup/decode-15cbe9f-original'),('cand-v003','be0079e7'),('cand-554a','554a8335')]:
    try:b=blobs_of(c)
    except Exception as e:print(label,'ERR',e);continue
    miss=[p for s,p in b.items() if s not in hist];print(label,'blobs',len(b),'not-in-remote-history',len(miss),miss[:15])
