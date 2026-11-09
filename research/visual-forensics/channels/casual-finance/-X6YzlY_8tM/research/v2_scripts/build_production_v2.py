import csv,json,os,statistics as st,collections,bisect
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
rd=lambda p:list(csv.DictReader(open(p)))
FPS=24;N=21410;MIN=N/FPS/60
S=sorted(rd('integrated_v1/states_integrated.csv'),key=lambda s:int(s['start']))
C=rd('integrated_v2/candidates_v2.csv');G=rd('integrated_v2/gaps_v2.csv');CG=rd('integrated_v2/composition_groups_v2.csv')
s2c={m:c['comp_id'] for c in CG for m in c['members'].split(';')}
starts=[int(s['start']) for s in S]
EV=[c for c in C if c['final_verdict'] in('CONFIRMED','RECLASSIFIED','SPLIT_PROPOSED_UNVERIFIED')]
ev_by=collections.defaultdict(list)
for c in EV:
    i=bisect.bisect_right(starts,int(c['start']))-1
    if i>=0 and int(c['start'])<=int(S[i]['end']):ev_by[S[i]['id']].append(c)
pct=lambda L,p:sorted(L)[min(len(L)-1,int(len(L)*p))]
dur=[int(s['n_frames'])/FPS for s in S]
tc=collections.Counter(c['final_type'] for c in EV)
fam=collections.defaultdict(lambda:[0,[]])
for s in S:fam[s['family']][0]+=int(s['n_frames']);fam[s['family']][1].append(int(s['n_frames'])/FPS)
stats=dict(label='MEASURED from integrated_v2 (structure only, not semantically certified)',video='-X6YzlY_8tM',frames=N,fps=FPS,duration_s=round(N/FPS,1),
 states=len(S),states_per_min=round(len(S)/MIN,1),compositions=len(CG),compositions_per_min=round(len(CG)/MIN,1),
 state_duration_s=dict(median=round(st.median(dur),2),mean=round(st.mean(dur),2),p10=round(pct(dur,.1),2),p90=round(pct(dur,.9),2),max=round(max(dur),2)),
 composition_duration_s=dict(median=round(st.median([c['n_frames']/FPS for c in map(lambda c:dict(c,n_frames=int(c['n_frames'])),CG)]),2)),
 events=dict(n=len(EV),per_min=round(len(EV)/MIN,1),by_type=dict(tc.most_common()),note='final types after second pass where reviewed; 429 candidates remain first-pass only'),
 gap_frames=sum(int(g['n_frames']) for g in G),gap_frames_pct=round(100*sum(int(g['n_frames']) for g in G)/N,1),
 families={k:dict(frames_pct=round(100*v[0]/sum(int(s['n_frames']) for s in S),1),states=len(v[1]),median_s=round(st.median(v[1]),2)) for k,v in sorted(fam.items(),key=lambda kv:-kv[1][0])},
 UNAVAILABLE=['colour values','typeface','easing curves','audio content (not heard)'])
json.dump(stats,open('production/dna_statistics_v2.json','w'),indent=1)
hdr='state_id,composition_id,start,end,n_frames,duration_s,family,events_in_state(MEASURED_FRAMES+type),objects(OBSERVED_FIRST_PASS),background,typography,camera_motion,entry_exit,story_function(INFERRED),readable_text,confidence_first_pass,original_asset_prompt(ORIGINAL_CREATIVE_INSTRUCTION),colour_typeface_easing'.split(',')
rows=[]
for s in S:
    ev=';'.join(f"f{c['start']}:{c['final_type']}" for c in ev_by[s['id']][:12])
    prompt=("Create an ORIGINAL composition of the same function ("+(s['story_function'] or 'beat')[:90]+"): new characters, props and typography of your own; layout family "+s['family']+"; stage elements in sequence at 0.3-1.5 s spacing; do not reuse source characters, logos, footage or text.")
    rows.append([s['id'],s2c[s['id']],s['start'],s['end'],s['n_frames'],round(int(s['n_frames'])/FPS,2),s['family'],ev,s['objects'][:160],s['background'][:80],s['typography'][:80],s['camera_motion'][:60],s['entry_exit'][:80],s['story_function'][:120],s['readable_text'][:100],s['confidence'],prompt,'UNAVAILABLE'])
csv.writer(open('production/per_state_specs_v2.csv','w',newline='')).writerows([hdr]+rows)
csv.writer(open('production/composition_family_specs_v2.csv','w',newline='')).writerows([['family','frames_pct','states','median_s']]+[[k,v['frames_pct'],v['states'],v['median_s']] for k,v in stats['families'].items()])
print(json.dumps({k:stats[k] for k in('states','states_per_min','compositions','state_duration_s','events','gap_frames_pct')},indent=1)[:1500]);print(len(rows),stats['families'])
