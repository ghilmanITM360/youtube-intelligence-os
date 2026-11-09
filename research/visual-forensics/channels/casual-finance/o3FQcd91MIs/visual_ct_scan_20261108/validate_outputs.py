import csv,json,hashlib,os,sys
ok=True
def chk(n,c):
    global ok; print(('PASS ' if c else 'FAIL ')+n); ok&=bool(c)
st=list(csv.DictReader(open('visual_states.csv')));ev=list(csv.DictReader(open('visual_event_ledger.csv')));sh=list(csv.DictReader(open('shot_ledger.csv')));al=list(csv.DictReader(open('audio_visual_alignment.csv')))
chk('76 states',len(st)==76);chk('47 shots',len(sh)==47);chk('75 events',len(ev)==75);chk('75 alignment rows',len(al)==75)
t=[(float(s['start_pts_seconds']),float(s['end_pts_seconds'])) for s in st]
chk('states start 0',t[0][0]==0);chk('states end at duration',abs(t[-1][1]-277.933)<0.05)
chk('states contiguous (gap<=0.034)',all(0<=t[i+1][0]-t[i][1]<=0.0345 for i in range(75)))
chk('frames in range',all(0<=int(e['start_frame'])<=int(e['end_frame'])<=8337 for e in ev))
chk('events ordered',all(int(ev[i]['start_frame'])<int(ev[i+1]['start_frame']) for i in range(74)))
ids={s['visual_state_id'] for s in st};chk('event states resolve',all(e['after_state'] in ids and e['before_state'] in ids for e in ev))
chk('shot ids resolve',{s['shot_id'] for s in st}<={s['shot_id'] for s in sh})
fm=list(csv.DictReader(open('tables/frame_metrics.csv')));chk('8338 frames measured',len(fm)==8338)
m=json.load(open('source_manifest.json'));h=hashlib.sha256(open(m['source_path'],'rb').read()).hexdigest();chk('manifest sha == recomputed',h==m['source_sha256'])
for f in ['source_manifest.json','coverage.json','shot_ledger.csv','visual_event_ledger.csv','audio_visual_alignment.csv','visual_ct_scan_report.md','reconstruction_blueprint.md','quality_gate.json','continuation_handoff.md']:
    chk('exists '+f,os.path.exists(f) and os.path.getsize(f)>0)
q=json.load(open('quality_gate.json'));chk('CT_SCAN not falsely complete',q['gates']['ct_scan_complete']!='PASS');chk('AV signoff blocked',q['gates']['final_av_signoff']=='BLOCKED')
print('ALL PASS' if ok else 'FAILURES');sys.exit(0 if ok else 1)
