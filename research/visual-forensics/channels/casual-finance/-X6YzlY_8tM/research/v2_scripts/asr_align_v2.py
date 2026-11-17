import json,csv,bisect,random,re,os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
S=sorted(csv.DictReader(open('integrated_v1/states_integrated.csv')),key=lambda s:int(s['start']))
G=list(csv.DictReader(open('integrated_v2/gaps_v2.csv')))
CG=list(csv.DictReader(open('integrated_v2/composition_groups_v2.csv')));s2c={m:c['comp_id'] for c in CG for m in c['members'].split(';')}
bounds=sorted([int(s['start']) for s in S]+[int(g['start']) for g in G])
st=[int(s['start']) for s in S];ids=[s['id'] for s in S]
seg=json.load(open('asr/asr_whisper_base.json'))['segments']
def owner(f):
    i=bisect.bisect_right(st,f)-1
    if i>=0 and f<=int(S[i]['end']):return ids[i]
    for g in G:
        if int(g['start'])<=f<=int(g['end']):return g['gap_id']
    return ''
def near(f):return min(abs(f-b) for b in bounds)
rows=[];num=re.compile(r'\d|million|billion|trillion|percent|%',re.I)
for k,s in enumerate(seg):
    f=int(s['start']*24);o=owner(f)
    rows.append(dict(asr_id='T%04d'%k,start_s=round(s['start'],2),end_s=round(s['end'],2),start_frame=f,owner=o,composition=s2c.get(o,''),nearest_boundary_frames=near(f),numeric=int(bool(num.search(s['text']))),text=s['text'],label='MACHINE_ASR_UNVERIFIED_NOT_HEARD'))
csv.DictWriter(open('production/asr_sentence_to_state_v2.csv','w',newline=''),rows[0].keys()).writeheader() if False else None
w=csv.DictWriter(open('production/asr_sentence_to_state_v2.csv','w',newline=''),rows[0].keys());w.writeheader();w.writerows(rows)
hit=sum(r['nearest_boundary_frames']<=6 for r in rows)/len(rows)  # 0.25 s
random.seed(5);base=[]
for _ in range(500):
    off=random.uniform(2,30);base.append(sum(near(int((s['start']+off)*24)%21410)<=6 for s in seg)/len(seg))
base.sort()
stats=dict(sentences=len(rows),within_0_25s_of_boundary=round(hit,3),shuffled_baseline_mean=round(sum(base)/len(base),3),shuffled_p95=round(base[475],3),numeric_sentences=sum(r['numeric'] for r in rows),
 unowned_gap_sentences=sum(r['owner'].startswith('G') for r in rows),label='MEASURED overlap of machine-ASR (Whisper base) timing vs state/gap starts; text and word timing unverified; not heard')
json.dump(stats,open('production/asr_alignment_stats_v2.json','w'),indent=1);print(stats)
num_rows=[r for r in rows if r['numeric']]
with open('production/claim_evidence_map_v2.csv','w',newline='') as f:
    x=csv.writer(f);x.writerow(['asr_id','time_s','owner','sentence(machine_asr)','visual_evidence_status','claim_verification'])
    for r in num_rows:x.writerow([r['asr_id'],r['start_s'],r['owner'],r['text'],'state/gap '+r['owner']+' (visual support not individually verified)','NOT_VERIFIED_NO_EXTERNAL_SOURCE_CHECK'])
print(len(num_rows))
# audio checklist
with open('production/AUDIO_HUMAN_REVIEW_CHECKLIST_v2.md','w') as f:
    f.write('# Human listening checklist - Video 005 (-X6YzlY_8tM)\nStatus: AUDIO_NOT_VERIFIED, AV_CERTIFICATION_BLOCKED. Nobody has listened. Source: /Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/The SpaceX IPO... It\'s Worse Than You Think - Casual Finance (720p, h264).mp4 (aac 44.1 kHz, 892.18 s). Tick only after genuinely listening.\n\n| Done | Time | ASR id | Machine-ASR text (check) | State |\n|---|---|---|---|---|\n')
    for r in rows:
        if r['numeric'] or r['asr_id'] in('T0000',) or int(r['asr_id'][1:])%20==0:
            f.write(f"| [ ] | {int(r['start_s']//60)}:{int(r['start_s']%60):02d} | {r['asr_id']} | {r['text']} | {r['owner']} |\n")
    f.write('\nAlso check: music/SFX presence and cuts, loudness jumps at hard cuts, voice-over vs on-screen text agreement, whether narration lands before or with each reveal.\n')
