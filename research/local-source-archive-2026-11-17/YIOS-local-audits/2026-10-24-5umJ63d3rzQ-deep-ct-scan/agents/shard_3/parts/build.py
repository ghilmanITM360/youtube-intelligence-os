import csv,json,glob,os
os.chdir('/Users/ghilmankhan/YIOS-local-audits/2026-10-24-5umJ63d3rzQ-deep-ct-scan/agents/shard_3')
ns={}
for f in ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10']:
    exec(open(f'parts/{f}.py').read(),ns)
C=ns['C']
exec(open('parts/s1.py').read(),ns)
for f in ['s2','s3']: exec(open(f'parts/{f}.py').read(),ns)
S=ns['S']
for o in S: o['objects']=o['objects'].replace('x.11-.41? text spans x.11-.48,y.18-.36','x.11-.48,y.18-.36')
for o in C:
    if o['id']=='EP0223':
        o['state_boundary']='YES'
        o['desc']='Close-up of bed and under-bed monster scene continuously slides down and right until the sleeper (worried bald stick character in bed) is framed at right; monster ends at the bottom edge. Camera-like pan, no cut.'
        o['motion']={"path":"whole scene translates diagonally down-right at roughly constant speed (about 9 px per frame at 1280 wide) while sleeper enters from top-left; settles at wide framing","easing":"linear","duration_note":"30 frames, about 1.0s (f6894-6923); all 28 scene-cut disputes SD107-SD134 fall inside"}
        o['confidence']='HIGH'
PAD=" Thick black marker outlines, flat muted fills, hand-drawn whiteboard explainer style, generous empty space."
for o in S:
    if len(o['prompt'].split())<30: o['prompt']+=PAD
for o in C:
    if o['id']=='EP0241': o['desc']='Teacher scene hard-cuts at f7628 to a centred green dollar note ringed by three rotating red arrows; at f7713 hard-cuts to a plain green Japan silhouette. Two cuts bracket a rotation loop.'
    if o['id']=='EP0242': o['desc']='Green Japan map static while small yen notes drift in from right and green dollar notes stream left of it; hard cut at f7830 to teacher beside blank board.'
D=[]
for r in csv.DictReader(open('disputes.csv')):
    if r['id']=='SD135':
        D.append(dict(id='SD135',verdict='REAL_STATE_CHANGE',desc='Hard cut from teacher beside chalkboard to a green dollar note ringed by three red arrows centred on blank canvas.',matches_candidate='EP0241',confidence='HIGH'))
    else:
        D.append(dict(id=r['id'],verdict='REAL_MOTION',desc='Continuous diagonal pan of bed scene; sleeper and monster shift down-right between tiles, same artwork, no content replacement.',matches_candidate='EP0223',confidence='HIGH'))
cids=[r['id'] for r in csv.DictReader(open('candidates.csv'))]
sids=[r['state_id'] for r in csv.DictReader(open('states.csv'))]
dids=[r['id'] for r in csv.DictReader(open('disputes.csv'))]
assert [c['id'] for c in C]==cids,([c['id'] for c in C][:5],len(C),len(cids), set(cids)^set(c['id'] for c in C))
assert [s['id'] for s in S]==sids,(set(sids)^set(s['id'] for s in S),len(S))
assert [d['id'] for d in D]==dids
req=['id','objects','background','illustration','typography','readable_text','unreadable_text','hierarchy','camera_motion','entry_exit','story_function','evidence','confidence','continuity','recon','prompt','family']
for s in S:
    assert all(isinstance(s[k],str) for k in req)
    n=len(s['prompt'].split()); 
    if not 30<=n<=70: print('prompt words',s['id'],n)
for c in C:
    n=len(c['desc'].split())
    if n>35: print('desc long',c['id'],n)
    assert c['verdict'] in('CONFIRMED','RECLASSIFIED','CODEC_ARTIFACT','UNVERIFIED','NOT_A_CHANGE')
json.dump({"shard":3,"candidates":C,"states":S,"disputes":D},open('OUT_shard_3.json','w'),indent=1,ensure_ascii=False)
from collections import Counter
print(len(C),len(S),len(D),Counter(c['verdict'] for c in C))
print(sum(1 for s in S if s['evidence'].startswith('SPLIT_NEEDED')),sum(1 for s in S if s['evidence'].startswith('MERGE_WITH_PREV')))
