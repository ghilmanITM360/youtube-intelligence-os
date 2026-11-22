"""Reads existing deep-scan workspaces (13 long-form CH001), emits:
 EVIDENCE_SEQUENCES.csv  - states showing real-source/evidence graphics + narration + callout lag
 BEAT_TABLE_long.csv     - narration sentence -> visual families used + narration-pattern flags
 BEAT_STATS.md           - conditional frequencies vs overall base rate (control)"""
import csv,glob,json,os,re,collections
C='CHANNEL_VISUAL_AUDIT/CHANNEL_001/'
cov=[r for r in csv.DictReader(open(C+'COVERAGE_MATRIX.csv')) if r['level']=='L3v' and r['format']=='long']
EVID=re.compile(r'(statista|EIA|SEC|NEWS|ARTICLE|HEADLINE|SCREENSHOT|SCREEN|DOC|_IMG|IMG_|CHART|NEWSPAPER|REPORT|TWEET|REDDIT|FORUM|PAGE|PHOTO|LOGO|STOCK_CARD|TABLE|WEBSITE)',re.I)
CALL=re.compile(r'(RED_ELLIPSE|RED_ARROW|RED_CIRCLE|HIGHLIGHT|UNDERLINE|RED_CROSS|RED_X|YELLOW)',re.I)
def fam(a):
    if CALL.search(a): return 'callout'
    if EVID.search(a): return 'evidence'
    if a.startswith('CH') or 'stick' in a.lower(): return 'character'
    if a.startswith('TXT') or 'text' in a.lower() or 'board' in a.lower(): return 'text'
    if a.startswith('OBJ') or a.startswith('ICON'): return 'object'
    if 'MAP' in a: return 'map'
    return 'other'
PAT={'number':r'\d|percent|million|billion|trillion|dollar','date':r'\b(19|20)\d\d\b|years? ago|decade|century','question':r'\?|\bwhy\b|\bhow\b|\bwhat\b','contrast':r'\bbut\b|however|actually|instead|yet\b','cause':r'because|so that|which means|therefore|leads? to','org':r'fed\b|federal reserve|government|bank|sec\b|congress|company|china|russia|usa|america|japan','example':r'imagine|say you|for example|let.s say|picture'}
ev=[];beats=[]
for r in cov:
    d=r['evidence'].split(';')[0]; vid=os.path.basename(d).split('2026-11-08-')[1].replace('-deep-ct-scan','')
    st=list(csv.DictReader(open(d+'/visual_states.csv')))
    asr=json.load(open(glob.glob(d+'/audio/*small_en.json')[0]))['segments']
    # sentence split on words
    words=[w for s in asr for w in s.get('words',[])]
    sents=[];cur=[]
    for w in words:
        cur.append(w)
        if re.search(r'[.?!]$',w['word'].strip()) and len(cur)>3: sents.append(cur);cur=[]
    if cur: sents.append(cur)
    for i,s in enumerate(sents):
        t0,t1=s[0]['start'],s[-1]['end']; txt=''.join(w['word'] for w in s).strip()
        ov=[x for x in st if float(x['start_pts_seconds'])<t1 and float(x['end_pts_seconds'])>t0]
        fams=collections.Counter()
        for x in ov:
            for a in x['asset_ids'].split(';'):
                if a and a!='-': fams[fam(a)]+=1
        flags={k:int(bool(re.search(p,txt,re.I))) for k,p in PAT.items()}
        beats.append(dict(video=vid,i=i,t0=round(t0,2),t1=round(t1,2),dur=round(t1-t0,2),text=txt[:200],n_states=len(ov),**{'f_'+k:v for k,v in fams.items()},**{'p_'+k:v for k,v in flags.items()}))
    # evidence sequences: contiguous run of states whose assets include evidence family, with callout lag
    for j,x in enumerate(st):
        a=[y for y in x['asset_ids'].split(';') if y and y!='-']
        if any(fam(y)=='evidence' for y in a):
            ent=float(x['start_pts_seconds'])
            call=None
            for y in st[j+1:j+6]:
                if any(fam(z)=='callout' for z in y['asset_ids'].split(';')):
                    call=float(y['start_pts_seconds'])-ent;break
            seg=[w['word'] for w in words if ent-0.3<=w['start']<=float(x['end_pts_seconds'])]
            ev.append(dict(video=vid,state=x['visual_state_id'],t0=ent,dur=x['duration_s'],entering=x['entering_class'],label=x['label'],assets=x['asset_ids'],visible_text=x['visible_text'][:120],callout_lag_s=None if call is None else round(call,2),narration=''.join(seg).strip()[:160]))
for name,rows in(('EVIDENCE_SEQUENCES.csv',ev),('BEAT_TABLE_long.csv',beats)):
    keys=sorted({k for r in rows for k in r},key=lambda k:(not k in('video','i','state','t0'),k))
    with open(C+name,'w',newline='') as f:
        w=csv.DictWriter(f,keys);w.writeheader()
        for r in rows: w.writerow({k:r.get(k,'') for k in keys})
print(len(ev),'evidence states',len(beats),'beats')
# conditional stats
F=['evidence','callout','character','text','object','map']
def rate(sub,f): return sum(1 for b in sub if b.get('f_'+f))/max(1,len(sub))
out=['# BEAT_STATS (13 long-form CH001, ASR-sentence vs visual-state families; generated)\n','Base rate = share of ALL narration sentences whose time window contains the family. Conditional = share among sentences with the narration pattern. Lift = cond/base. Correlational only: window overlap, ASR unverified, asset_ids come from prior ledgers.\n',f'Sentences: {len(beats)}\n','| narration pattern | n | '+' | '.join(f'{f} (lift)' for f in F)+' |','|---|---|'+'---|'*len(F)]
out.append('| ALL (base) | %d | '%len(beats)+' | '.join('%.2f'%rate(beats,f) for f in F)+' |')
for p in PAT:
    sub=[b for b in beats if b.get('p_'+p)]
    out.append(f'| {p} | {len(sub)} | '+' | '.join('%.2f (%.2f)'%(rate(sub,f),rate(sub,f)/max(1e-9,rate(beats,f))) for f in F)+' |')
open(C+'BEAT_STATS.md','w').write('\n'.join(out)+'\n')
print('\n'.join(out))
