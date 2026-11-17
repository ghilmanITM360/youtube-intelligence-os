# Checkpoint O: consolidate batches05-09 (reviewers17-21), seal, prepare external-index tree. Push is a separate step (o_scripts/push.py).
from pathlib import Path
import csv,json,hashlib,subprocess,os,datetime
p=Path.cwd();repo=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');base='76b1e2a378e1d803dc3cbf1987c8400f5bbd1367';prefix='research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/uPQcyookL0Y/'
run=lambda *a,**k:subprocess.check_output(a,cwd=repo,text=True,**k).strip()
rows=lambda f:list(csv.DictReader(open(p/f)))
def save(f,r):
    keys=list(dict.fromkeys(k for x in r for k in x))
    with open(p/f,'w',newline='') as h:w=csv.DictWriter(h,fieldnames=keys);w.writeheader();w.writerows(r)
B=[('reviewer_17','batch05'),('reviewer_18','batch06'),('reviewer_19','batch07'),('reviewer_20','batch08'),('reviewer_21','batch09')]
for rv,b in B:assert json.loads((p/f'tables/o_validation_{rv}_{b}.json').read_text())['errors']==[],rv
art=rows('tables/n_art_consolidated.csv')
for rv,b in B:art+=[r|{'reviewer':rv,'batch':b} for r in rows(f'agents/{rv}/art_audit_{b}.csv')]
S=[r['state_v4'] for r in rows('tables/states_v6_draft.csv')];assert [r['state'] for r in art]==S,'art order/coverage';save('tables/o_art_consolidated.csv',art)
nar=rows('tables/n_narration_assessments_consolidated.csv')
for rv,b in B:
    for r in rows(f'agents/{rv}/narration_relation_{b}.csv'):
        r.update(source_assessment=f'agents/{rv}/narration_relation_{b}.csv',coverage_qualification='SPARSE_PARTIAL_ASR_ONLY_NOT_LISTENED',effective_relation=r['relation'],reviewer=rv);nar.append(r)
segs={int(r['seg_index']) for r in nar if r['seg_index'].strip().isdigit()};assert segs==set(range(76)),sorted(set(range(76))-segs);save('tables/o_narration_consolidated.csv',nar)
mo=[];pr=[]
for rv,b in B:
    mo+=[r|{'reviewer':rv} for r in rows(f'agents/{rv}/motion_events_{b}.csv')]
    if (p/f'agents/{rv}/state_prompts_{b}.csv').exists():pr+=[r|{'reviewer':rv,'basis':'reviewer viewed native+strip frames'} for r in rows(f'agents/{rv}/state_prompts_{b}.csv')]
save('tables/o_motion_events_W041_W088.csv',mo);save('tables/o_state_prompts_W051_W088.csv',pr);assert len(pr)==39
res={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'five_hour':'UNKNOWN (no readable meter: Chrome extension disconnected; no CLI meter)','weekly':'UNKNOWN','paid_or_reset_credits_used':0,'reviewer_tokens_this_session':{'r17':171220,'r18':163166,'r19':160577,'r20':188626,'r21':173483},'disk_free':subprocess.check_output(['df','-h',str(p)],text=True).splitlines()[1],'memory':subprocess.check_output(['memory_pressure'],text=True).splitlines()[-1]}
(p/'evidence/O_resources.json').write_text(json.dumps(res,indent=1))
gate={'status':'PARTIAL','video_id':'uPQcyookL0Y','checkpoint':'O','parent':base,
 'art':{'states_with_native_art_audit':89,'of':89,'mode':'sparse native representatives (2-4 per state)','W041_W088_intra_state_motion_strips':'68 measured-peak strips reviewed (8 consecutive frames each)','W001_W040_motion_strips':'generated (59), review in progress by reviewer_22/23 — NOT in O'},
 'narration':{'segments_with_partial_visual_assessment':'0-75 (76/76)','qualification':'SPARSE_PARTIAL_ASR_ONLY_NOT_LISTENED','full_audio_verified_segments':0,'preserved_uncertainties':'8,11,22; seg25 head/tail; seg27 primary supplement; seg0 primary adjudication; seg4 MIXED_PARTIAL; reviewer15 corrections 18/19','new_open_items':'seg67 ocean insert vs ASR rivers (unresolved); W085b fade-out not seen in strip f14026-14033'},
 'boundaries':{'states':'v6 unchanged 89 contiguous, 14647 frames','new_unresolved_candidate':'UBC-001 W062 f10316->10317 discontinuity (tables/o_primary_corrections.csv)'},
 'state_prompts':{'W051_W088':39,'W001_W050':'PENDING (reviewer_22/23)'},
 'asset_crosswalk':'m_asset_alias_crosswalk.csv unchanged; reviewers17-21 raw IDs preserved, cross-reviewer reconciliation PENDING',
 'production_specs':'production_specifications v1 (3 scoped drafts) unchanged; v2 PENDING','actual_listening':'BLOCKED_CAPABILITY (../AUDIO_LISTENING_CAPABILITY_2026-11-03.json)','reconstruction_test':'NOT_RUN',
 'review_relationship':'reviewers17-21 = Claude sonnet subagents; orchestrator Claude opus-5-5; same vendor; no human review; primary spot checks on 3 batches (tables/o_primary_corrections.csv, o_reviewer_*_provenance.json)',
 'validation':'o_validation_reviewer_*.json all errors=[] (coverage, sha256, witness, locator, in-segment time ±0.2s); sequential decode mismatches 0 for all batches',
 'resources':res,'CT_SCAN_COMPLETE':False,
 'next_operation':'validate reviewer_22/23 (strips W001-W040, prompts W001-W050) -> asset crosswalk extension -> production specs v2 + blueprint v2 -> bounded reconstruction test; videos mNLNb-Z4T0M (ingested, 145 boundary candidates) and GNaBxt_zIRA (ingest running)'}
(p/'quality_gate_O.json').write_text(json.dumps(gate,indent=2)+'\n')
(p/'CONTINUATION_HANDOFF_O.md').write_text('# Barely Evolved uPQcyookL0Y checkpoint O — PARTIAL\n\nEarlier handoffs (L/M/N) preserved unchanged.\n\n```json\n'+json.dumps(gate,indent=2)+'\n```\n\nWorkspace: '+str(p)+'\nBranch research/barely-evolved-visual-forensics; publication via external GIT_INDEX_FILE + commit-tree, normal push; canonical checkout untouched. Lock: ~/YIOS-local-audits/barely-evolved/.be_writer_lock (session 7a28d062).\n')
sel=[]
for pat in ['o_scripts/*','tables/o_*','tables/k_rep_frames_batch0[5-9].csv','agents/reviewer_1[7-9]/*','agents/reviewer_2[01]/*','quality_gate_O.json','CONTINUATION_HANDOFF_O.md','evidence/O_resources.json']:sel+=[x for x in p.glob(pat) if x.is_file()]
sel.append(p.parent/'AUDIO_LISTENING_CAPABILITY_2026-11-03.json')
files=set(x for x in sel)
for line in (p/'EVIDENCE_SHA256SUMS_checkpoint_N').read_text().splitlines():
    h,f=line.split(None,1);q=Path(f);assert hashlib.sha256(q.read_bytes()).hexdigest()==h,f;files.add(q)
files.add(p/'EVIDENCE_SHA256SUMS_checkpoint_N')
for d in ['batch05','batch06','batch07','batch08','batch09']:files.update((p/'frames/native_rep'/d).glob('*.png'))
files.update(x for x in (p/'frames/motion_strips').rglob('*.png'))
seal=p/'EVIDENCE_SHA256SUMS_checkpoint_O';seal.write_text(''.join(hashlib.sha256(x.read_bytes()).hexdigest()+'  '+str(x)+'\n' for x in sorted(files)));sel.append(seal)
assert run('git','ls-remote','origin','refs/heads/research/barely-evolved-visual-forensics').split()[0]==base,'remote moved'
index=p/'evidence/O_publication.index';assert not index.exists();env=dict(os.environ,GIT_INDEX_FILE=str(index));run('git','read-tree',base,env=env)
def dest(f):return prefix+(str(f.relative_to(p)) if f.is_relative_to(p) else 'campaign/'+f.name)
for f in sorted(set(sel)):run('git','update-index','--add','--cacheinfo','100644',run('git','hash-object','-w',str(f)),dest(f),env=env)
tree=run('git','write-tree',env=env);paths=run('git','diff','--name-only',base,tree).splitlines()
assert all(x.startswith(prefix) for x in paths) and not any(x.endswith(('.png','.jpg','.mp4','.wav')) for x in paths)
(p/'evidence/O_INTENDED_DIFF.txt').write_text(run('git','diff','--stat',base,tree)+'\n')
(p/'evidence/O_PREPARED.json').write_text(json.dumps({'base':base,'tree':tree,'seal_entries':len(files),'paths':paths,'checkout_head':run('git','rev-parse','HEAD')},indent=1))
print('seal',len(files),'paths',len(paths),'tree',tree)
