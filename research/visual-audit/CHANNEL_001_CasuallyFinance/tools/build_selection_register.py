import csv,collections
R='research/visual-audit/CHANNEL_001_CasuallyFinance/'
inv=list(csv.DictReader(open(R+'01_DATA_INVENTORY.csv')))
mp={r['video_id']:r for r in csv.DictReader(open(R+'21_AUTO_MOTION_PROFILE_ALL_VIDEOS.csv'))}
idp={r['key']:r for r in csv.DictReader(open(R+'22_IDLESS_MOTION_PROFILE.csv'))}
m2={r['file']:r for r in csv.DictReader(open(R+'22_IDLESS_MATCH.csv'))}
seen={};rows=[]
dupkey={}
for f,x in m2.items():
    if x['grey_diff'] and float(x['grey_diff'])<0.4:
        a,b=sorted([x['key'],x['best_match'].split(' | ')[0]]); dupkey[x['key']]=a
def dbin(d,o): return ('S<30' if d<30 else 'S30-60' if d<60 else 'S60+') if o=='short' else ('L<8m' if d<480 else 'L8-20m' if d<1200 else 'L20m+')
for r in inv:
    vid=r['video_id'] or 'FILE-'+r['sha256'][:8]
    d=float(r['duration_s']); o=r['orientation']
    m=mp.get(r['video_id']) if r['video_id'] else idp.get(vid)
    ev=float(m['change_events_per_min']) if m else None
    pace='unprofiled' if ev is None else 'slow' if ev<30 else 'mid' if ev<60 else 'fast'
    dup=seen.get(r['sha256']); seen.setdefault(r['sha256'],vid)
    k=dupkey.get(vid)
    if not dup and k and k!=vid: dup=k+' (fingerprint, grey diff<0.4)'
    deep=bool(r['visual_workspace'])
    res=r['width']+'x'+r['height']
    rows.append(dict(video_id=vid,path='~/workprojects/videos in mp3/CasuallyFinance/'+r['file_name'],eligible='yes (ffprobe valid)',duration=round(d,1),
      existing_analysis='deep-ct-scan workspace + visual ledger' if deep else 'none',visual_cluster=f"{o}|{res}|{dbin(d,o)}|{pace}",
      candidate_novelty='',estimated_value='',selection_status='DUPLICATE_SKIP' if dup else ('DEEP_VERIFIED' if deep else 'INVENTORIED'),
      selection_reason=('duplicate of '+dup) if dup else ('pre-existing ledger, counted (R27 step 2); blueprint depth PARTIAL' if deep else 'T0 only'),
      identified_unique_techniques='',deep_analysis_done='ledger (PARTIAL blueprints)' if deep else 'no',holdout='no',deferred_reason='',next_trigger='',_deep=deep))
for x in rows:
    if x['video_id']=='FILE-379b7617': x['selection_status']='DUPLICATE_SKIP'; x['selection_reason']='duplicate of FILE-73641860 (fingerprint grey diff 0.0, different sha = re-encode)'
cnt=collections.Counter(x['visual_cluster'] for x in rows if x['selection_status']!='DUPLICATE_SKIP')
dc=collections.Counter(x['visual_cluster'] for x in rows if x['_deep'])
unc=sorted([c for c in cnt if not dc[c] and 'unprofiled' not in c],key=lambda c:-cnt[c])
sel=[];hold=[]
for c in unc:
    cr=sorted([x for x in rows if x['visual_cluster']==c and x['selection_status']=='INVENTORIED'],key=lambda x:x['video_id'])
    if len(sel)<4 and cr:
        cr[0].update(selection_status='SELECTED_FOR_DEEP',candidate_novelty='high: cluster has 0 deep examples',selection_reason=f'first of uncovered cluster (size {cnt[c]})');sel.append(cr[0])
        if len(cr)>1 and len(hold)<2: cr[-1].update(selection_status='VALIDATION_HOLDOUT',holdout='yes',selection_reason='blind spot-check holdout (R27.3-7)');hold.append(cr[-1])
for x in rows:
    if x['selection_status']=='INVENTORIED': x.update(selection_status='DEFERRED',deferred_reason='cluster already has deep example or lower novelty rank',next_trigger='failed recon/novel test or spot check reveals new family')
cols=['video_id','path','eligible','duration','existing_analysis','visual_cluster','candidate_novelty','estimated_value','selection_status','selection_reason','identified_unique_techniques','deep_analysis_done','holdout','deferred_reason','next_trigger']
w=csv.DictWriter(open('CHANNEL_VISUAL_AUDIT/CHANNEL_001/VIDEO_SELECTION_REGISTER.csv','w',newline=''),cols,extrasaction='ignore');w.writeheader();w.writerows(rows)
print(len(rows),dict(collections.Counter(x['selection_status'] for x in rows)))
print('clusters',len(cnt),'covered',sum(1 for c in cnt if dc[c]),'unc',len(unc))
print('unprofiled',sum(1 for x in rows if 'unprofiled' in x['visual_cluster']))
for x in sel+hold:print(x['selection_status'],x['video_id'],x['visual_cluster'],x['duration'])
