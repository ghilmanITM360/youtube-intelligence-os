import csv,json,copy,os,hashlib
rd=lambda p:list(csv.DictReader(open(p)))
def run(states,comps,C,A,specs,V2C,src_sha):
    e=[];sid={s['id'] for s in states};cid={c['composition_id'] for c in comps}
    if src_sha!='8fd0c2bfd7b89d46e49280b7329626b7656dca7f5f2fd98c8046998af0c95b73':e.append('source sha')
    ids=[c['id'] for c in C]
    if len(ids)!=len(set(ids)) or len(ids)!=1032:e.append('candidate count/dup')
    if not {c['id'] for c in V2C}<=set(ids):e.append('lost candidate vs v2')
    v2={c['id']:c for c in V2C}
    for c in C:
        if c['id'] in v2 and (c['verdict']!=v2[c['id']]['verdict'] or c['desc']!=v2[c['id']]['desc']):e.append('first-pass provenance altered '+c['id']);break
        if c['smp_status'].startswith('REVIEWED') and not c['smp_reason'].strip():e.append('sample provenance lost '+c['id']);break
    for a in A:
        for s in a['states'].split():
            if s not in sid:e.append('asr bad state '+s);break
    if len(A)!=192:e.append('asr sentences')
    if len(specs)!=530 or {x['state_id'] for x in specs}!=sid:e.append('spec state set')
    for x in specs:
        if x['composition_id'] not in cid:e.append('spec bad composition');break
        if 'UNAVAILABLE' not in x['colour_values']:e.append('spec invented colour');break
    return e
if __name__=='__main__':
    st=rd('integrated_v5/reviewed_states_v5.csv');cp=rd('integrated_v5/compositions_v5.csv');C=rd('integrated_v5/reviewed_candidates_v5.csv');A=rd('phaseB/asr_sentence_to_state_v4.csv');sp=rd('production/per_state_specs_v5.csv');V2=rd('integrated_v2/reviewed_candidates_v2.csv')
    sha=json.load(open('source_manifest.json')).get('sha256') or hashlib.sha256(open(json.load(open('source_manifest.json'))['source_path'],'rb').read()).hexdigest()
    res={'positive':run(st,cp,C,A,sp,V2,sha) or 'PASS'};print(res)
    n={}
    n['source sha mismatch']=run(st,cp,C,A,sp,V2,'0'*64)
    c2=copy.deepcopy(C);c2.pop();n['missing candidate']=run(st,cp,c2,A,sp,V2,sha)
    c3=copy.deepcopy(C);c3[0]['verdict']='X';n['altered first-pass verdict']=run(st,cp,c3,A,sp,V2,sha)
    a4=copy.deepcopy(A);a4[0]['states']='S9999';n['invalid asr ref']=run(st,cp,C,a4,sp,V2,sha)
    s5=copy.deepcopy(sp);s5.pop();n['missing spec']=run(st,cp,C,A,s5,V2,sha)
    s6=copy.deepcopy(sp);s6[0]['composition_id']='CMP9999';n['bad spec ref']=run(st,cp,C,A,s6,V2,sha)
    c7=copy.deepcopy(C);k=[x for x in c7 if x['smp_status'].startswith('REVIEWED')][0];k['smp_reason']='';n['lost sample provenance']=run(st,cp,c7,A,sp,V2,sha)
    c8=copy.deepcopy(C);c8[1]['id']=c8[0]['id'];n['duplicate candidate id']=run(st,cp,c8,A,sp,V2,sha)
    for k,v in n.items():print('NEG',k,'DETECTED' if v else 'MISSED')
    res['negative']={k:('DETECTED' if v else 'MISSED') for k,v in n.items()};json.dump(res,open('integrated_v5/validation_results_v5_extended.json','w'),indent=1)
