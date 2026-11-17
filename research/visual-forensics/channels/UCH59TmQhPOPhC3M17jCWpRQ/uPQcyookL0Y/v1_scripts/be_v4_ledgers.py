# Kit-contract ledgers from v4 states + reviews. All rows keep their evidence label; nothing here is validated or audio-verified.
import csv,json,collections
T='tables/'
S=list(csv.DictReader(open(T+'states_v4_draft.csv')))
rev1={r['seq']:r for r in csv.DictReader(open(T+'review_verdicts_sparse_montage.csv'))} if False else None
# shot ledger
cand={}
for fn in ('review_verdicts_sparse_montage.csv','second_detector_review_sparse_montage.csv'):
    for r in csv.DictReader(open(T+fn)):
        cand[r.get('entry') or r.get('id') or r.get('cand') or list(r.values())[0]]=r
with open('shot_ledger.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow("state_v4,start_frame,end_frame,start_pts_s,end_pts_s,duration_s,entry_candidate,parent_v3,transition_class,verification,status".split(','))
    for s in S:
        b=s['basis'].lower()
        tc='START' if s['entry']=='START' else ('FADE_OR_DISSOLVE_TRANSITION_INSIDE_STATE' if any(k in b for k in('fade','dissolve','wipe')) else 'ENTRY_PER_REVIEW_SEE_candidates_tables')
        ver='SPARSE_MONTAGE_REVIEW_plus_dense_where_noted'
        if any(k in b for k in('dense','native','reviewer_11','reviewer_9')):ver='DENSE_CONSECUTIVE_FRAMES_downscaled_single_reviewer'
        w.writerow([s['state_v4'],s['start'],s['end'],s['start_pts_s'],s['end_pts_s'],s['dur_s'],s['entry'],s['parent_state_v3'],tc,ver,'DRAFT_UNVALIDATED'])
# visual event ledger
ev=[]
def add(eid,state,f0,f1,cls,src,who,label,note):ev.append([eid,state,f0,f1,cls,src,who,label,note[:240]])
def st(f):
    for s in S:
        if int(s['start'])<=f<=int(s['end']):return s['state_v4']
for fn in ('burst_sample_review_sparse_montage.csv','burst_rest_review_sparse_montage.csv'):
    for r in csv.DictReader(open(T+fn)):
        k=r.get('observation_OBSERVED_sparse') or r.get('observation') or ''
        fr=int(r.get('burst_frame') or r.get('frame'));add('BURST_'+(r.get('seq') or ''),st(fr),fr,'',r.get('verdict') or r['reviewer_verdict'],fn,r.get('reviewer','reviewer_3'),'OBSERVED_sparse_4frame_downscaled',k)
for r in csv.DictReader(open(T+'onset_rest_review_dense_v4.csv')):
    fr=int(r['frame']);add('ONSET_'+r['seq'],st(fr),fr,r['end_frame'],r['what_changed_visible'],'onset_rest_review_dense_v4.csv','reviewer_10','OBSERVED_6tile_320px_single_reviewer',r['observation'])
for r in csv.DictReader(open('agents/reviewer_9/review_9_merges_discrepancies_unclear.csv')):
    a=r['first_change_frame'];b=r['last_change_frame']
    import re
    na=re.findall(r'\d{3,5}',a);nb=re.findall(r'\d{3,5}',b)
    f0=int(na[0]) if na else '';f1=int(nb[0]) if nb else ''
    add('REV9_'+r['item'].split()[0],st(f0) if f0 else '',f0,f1,r['verdict'][:60],'reviewer_9','reviewer_9','OBSERVED_dense_consecutive_480x270_single_reviewer',r['observation'])
for r in csv.DictReader(open('agents/reviewer_11/review_11_inside_state_candidates.csv')):
    na=__import__('re').findall(r'\d{3,5}',r['first_change_frame']);f0=int(na[0]) if na else ''
    add('REV11_'+r['item'],st(f0) if f0 else '',f0,'',r['kind'],'reviewer_11','reviewer_11','OBSERVED_dense_consecutive_480x270_single_reviewer',r['observation'])
w=csv.writer(open('visual_event_ledger.csv','w',newline=''));w.writerow("event_id,state_v4,start_frame,end_frame,event_class,source_table,reviewer,evidence_label,observation".split(','));w.writerows(ev)
# AV alignment (ASR_ONLY_NOT_AUDIO_VERIFIED)
A=json.load(open('asr/asr_small_en.json'));rows=[]
for i,sg in enumerate(A['segments'],1):
    sts=[s['state_v4'] for s in S if float(s['start_pts_s'])<sg['end'] and float(s['end_pts_s'])+0.034>sg['start']]
    rows.append([f'ASR{i:03d}',sg['start'],sg['end'],sg['text'],'faster-whisper small.en int8 (segment times, word times in asr_small_en.json)','ASR_ONLY_NOT_AUDIO_VERIFIED','|'.join(sts),'NOT_ASSESSED','NOT_MEASURED',sg['avg_logprob']])
w=csv.writer(open('audio_visual_alignment.csv','w',newline=''));w.writerow("phrase_id,start_s,end_s,phrase_asr,method,audio_status,overlapping_states_v4,visual_relation,lag_ms,asr_avg_logprob".split(','));w.writerows(rows)
c=collections.Counter(e[4] for e in ev if e[0].startswith('BURST'));o=collections.Counter(e[4] for e in ev if e[0].startswith('ONSET'))
print(len(S),'shots',len(ev),'events',len(rows),'av rows');print(c);print(o)
