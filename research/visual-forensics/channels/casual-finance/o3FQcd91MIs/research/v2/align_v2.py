import csv,json,bisect,statistics as S
al=list(csv.DictReader(open('audio_visual_alignment.csv')))
base=list(csv.DictReader(open('/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research/02_VIDEO_FORENSICS/o3FQcd91MIs/TRANSCRIPT.csv')))
bs=[float(x['start_sec']) for x in base]
w=json.load(open('audio/o3FQ_16k.json'));W=[(x['start'],x['end'],x['word'].strip()) for s in w['segments'] for x in s['words']]
ws=[x[0] for x in W]
mic=list(csv.DictReader(open('v2/intra_state_events.csv')))
def near(arr,t):
    i=bisect.bisect_left(arr,t);c=[k for k in (i-1,i) if 0<=k<len(arr)];return min(c,key=lambda k:abs(arr[k]-t))
rows=[]
for a in al:
    t=float(a['visual_start_pts']);k=near(bs,t);lb=round(t-bs[k],3);l=float(a['lead_lag_seconds'])
    rows.append(dict(a,event_type='STATE_BOUNDARY',lag_base_asr=lb,outside_0p2_small_en=abs(l)>0.2,asr_agreement=('BOTH_WITHIN_0.2' if abs(l)<=0.2 and abs(lb)<=0.2 else ('BOTH_OUTSIDE_0.2 (genuine lead/lag under both ASR runs)' if abs(l)>0.2 and abs(lb)>0.2 else 'ASR_DISAGREE (one run within, one outside; timing unreliable)'))))
for m in mic:
    t=float(m['pts']);j=near(ws,t);k=near(bs,t);l=round(t-W[j][0],3);lb=round(t-bs[k],3)
    ctx=' '.join(x[2] for x in W[max(0,j-3):j+4])
    rows.append(dict(video_id='o3FQcd91MIs',event_id=m['event_id'],audio_source='local ASR openai-whisper small.en',audio_listening_status='ASR_UNCERTIFIED - NO HUMAN LISTENING',phrase_or_sound=f"[{W[j][2]}] …{ctx}…",audio_start_pts=round(W[j][0],3),audio_end_pts=round(W[j][1],3),visual_start_pts=t,visual_end_pts=t,lead_lag_seconds=l,timestamp_method='visual PTS minus nearest ASR word start',confidence='MEDIUM',limitations='intra-state micro event; ASR text unverified',event_type='INTRA_STATE_MICRO',lag_base_asr=lb,outside_0p2_small_en=abs(l)>0.2,asr_agreement=('BOTH_WITHIN_0.2' if abs(l)<=0.2 and abs(lb)<=0.2 else ('BOTH_OUTSIDE_0.2 (genuine lead/lag under both ASR runs)' if abs(l)>0.2 and abs(lb)>0.2 else 'ASR_DISAGREE (one run within, one outside; timing unreliable)'))))
with open('v2/audio_visual_alignment_v2.csv','w',newline='') as f:
    q=csv.DictWriter(f,fieldnames=list(rows[0]));q.writeheader();q.writerows(rows)
L=[float(r['lead_lag_seconds']) for r in rows]
print(len(rows),'median',S.median(L),'within0.2',sum(abs(x)<=0.2 for x in L),'outside',sum(abs(x)>0.2 for x in L))
import collections;print(collections.Counter(r['asr_agreement'] for r in rows if r['outside_0p2_small_en']))
print([ (r['event_id'],r['lead_lag_seconds'],r['phrase_or_sound'][:50]) for r in rows if r['event_type']=='INTRA_STATE_MICRO'])
