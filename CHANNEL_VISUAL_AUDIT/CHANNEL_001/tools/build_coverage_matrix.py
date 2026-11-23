import csv,json,os,glob,collections
R='research/visual-audit/CHANNEL_001_CasuallyFinance/'
C='CHANNEL_VISUAL_AUDIT/CHANNEL_001/'
inv=list(csv.DictReader(open(R+'01_DATA_INVENTORY.csv')))
ws={}
for d in glob.glob(os.path.expanduser('~/YIOS-local-audits/*-deep-ct-scan')):
    try: m=json.load(open(d+'/source_manifest.json'))
    except: continue
    h=m.get('source_sha256') or m.get('sha256')
    if h: ws[h]=d
mv={}
for f in glob.glob(C+'MULTI_VIDEO_MEASUREMENTS/states_*.csv'):
    mv[os.path.basename(f)[7:-4]]=f
prof=set(r['video_id'] for r in csv.DictReader(open(R+'21_AUTO_MOTION_PROFILE_ALL_VIDEOS.csv')))
prof|=set(r['key'] for r in csv.DictReader(open(R+'22_IDLESS_MOTION_PROFILE.csv')))
rows=[]
for r in inv:
    vid=r['video_id'] or ''; key=vid or 'FILE-?'
    lvl='L0';miss='';ev='';shots=0;note=''
    if vid in prof: lvl='L1'; ev='auto motion profile (coarse)'
    d=ws.get(r['sha256'])
    if d and not vid: key=os.path.basename(d)[11:].replace('-deep-ct-scan','')+' (id from workspace name)'
    if d:
        q=json.load(open(d+'/quality_gate.json')) if os.path.exists(d+'/quality_gate.json') else None
        n=lambda f:(sum(1 for _ in open(d+'/'+f))-1) if os.path.exists(d+'/'+f) else 0
        shots=n('shot_ledger.csv');st=n('visual_states.csv')
        if q and str(q['gates'].get('ct_scan_complete','')).startswith('PASS_VISUAL_ONLY'):
            lvl='L3v'; ev=f'{d}; {shots} shots/{st} states; all frames measured'
            miss='no human listening; narration alignment ASR-provisional subset; small on-screen text unread; no beat-function layer'
        else: lvl='L1'; ev=d; miss='workspace incomplete (no ledger)'; note='partial workspace'
    elif vid in mv or any(k in r['file_name'] for k in mv):
        lvl='L2'; ev='MULTI_VIDEO_MEASUREMENTS states csv'; miss='states measured, no narration alignment'
    if vid=='10nEByVLya0': note='same-video reconstruction attempted (v25), gate NOT passed; not L4'
    sh8=r['sha256'][:8]; hashkey=any(sh8 in k for k in mv)
    partial = (lvl=='L2') or (d is not None and lvl=='L1') or hashkey or vid=='o3FQcd91MIs'
    if vid=='o3FQcd91MIs' and lvl=='L1': ev='2026-10-24-o3FQcd91MIs-deep-ct-scan (47 shot rows, 76 state rows; not a gated visual scan)'; miss='partial workspace'
    if hashkey and lvl=='L1': ev='MULTI_VIDEO_MEASUREMENTS hash-keyed states csv'; miss='states measured; counted as partial by the 2026-11-22 Codex reconciliation'
    tier='gated' if lvl=='L3v' else ('partial' if partial else 'coarse')
    rows.append(dict(tier=tier,source_id=key,title=r['file_name'],format='long' if r['orientation']=='long' else 'short',res=f"{r['width']}x{r['height']}",duration_s=round(float(r['duration_s']),1),sha256=r['sha256'],level=lvl,shots=shots,evidence=ev,missing=miss,note=note))
# mark duplicate sha
c=collections.Counter(x['sha256'] for x in rows)
for x in rows:
    if c[x['sha256']]>1: x['note']+=' DUPLICATE_SHA'
with open(C+'COVERAGE_MATRIX.csv','w',newline='') as f:
    w=csv.DictWriter(f,rows[0].keys());w.writeheader();w.writerows(rows)
for fmt in('long','short'):
    print(fmt,collections.Counter(x['level'] for x in rows if x['format']==fmt))
print('tier counts',collections.Counter(x['tier'] for x in rows))
print('total',len(rows),'unique sha',len(c),'shots in L3v',sum(x['shots'] for x in rows if x['level']=='L3v'))
