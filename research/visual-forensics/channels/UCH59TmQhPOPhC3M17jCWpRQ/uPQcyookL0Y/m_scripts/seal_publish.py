from pathlib import Path
import csv,json,hashlib,subprocess,os,datetime
p=Path.cwd();repo=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');base='3a027c1de42956c1dadb0705074a81755449c45e';prefix='research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/uPQcyookL0Y/'
def run(*args,**kw):return subprocess.check_output(args,cwd=repo,text=True,**kw).strip()
def readcsv(f):return list(csv.DictReader(f.open()))
art=p/'agents/reviewer_15/art_audit_batch03.csv';nar=p/'agents/reviewer_15/narration_relation_batch03.csv';reads=p/'agents/reviewer_15/evidence_reads.csv'
assert art.exists() and nar.exists() and reads.exists(),'reviewer output pending'
a=readcsv(art); n=readcsv(nar); rr=readcsv(reads);assert len(a)==10 and len(rr)==34
assert {r['state'] for r in a}=={f'W{i:03}' for i in range(21,31)}
expected=readcsv(p/'tables/k_rep_frames_batch03.csv')
for r in expected:assert (p/r['native_png']).exists()
# Retain prior assessments verbatim, with additions and corrections separate.
allart=[]
for f in [p/'agents/reviewer_12/art_audit_batch01.csv',p/'tables/k_art_audit_batch02_combined.csv',art]:allart+=readcsv(f)
fields=list(dict.fromkeys(k for r in allart for k in r))
with (p/'tables/m_art_consolidated.csv').open('w') as h:w=csv.DictWriter(h,fieldnames=fields);w.writeheader();w.writerows(allart)
assert len(allart)==30
states=readcsv(p/'tables/states_v5_draft.csv');assert len(states)==89
assert int(states[0]['start'])==0 and int(states[-1]['end'])==14646
assert all(int(x['end'])+1==int(y['start']) for x,y in zip(states,states[1:]))
# Audit tool-call provenance from the dedicated reviewer session, never copy unrelated chats.
trans=Path('/Users/ghilmankhan/.codex/sessions/2026/11/03/rollout-2026-11-03T00-52-11-01a19dd1-c126-7751-aa35-ccf9cbe6f449.jsonl')
t=trans.read_text();opened=[r['native_png'] for r in expected if r['native_png'] in t or Path(r['native_png']).name in t]
assert len(opened)==34,'transcript locator audit failed'
(p/'tables/m_reviewer_provenance.json').write_text(json.dumps({'reviewer':'reviewer_15','transcript_path':str(trans),'transcript_sha256_at_audit':hashlib.sha256(trans.read_bytes()).hexdigest(),'expected_native_frames':34,'transcript_path_witnesses':len(opened),'self_reported_reads':len(rr),'art_rows':len(a),'narration_rows':len(n),'limitation':'Tool-call locator audit and reviewer witness ledger; primary has not independently re-viewed all34frames. No different-model or human independence claimed.'},indent=2)+'\n')
report={'status':'PARTIAL','art_coverage':{'start':20,'end':30,'total':89,'mode':'sparse native representatives'},'narration':{'assessed_segments':'0-25;26/76 with sparse/partial evidence, NOT fully completed','caveats':'ASR8 partial/low confidence with new Daddy? visual witness;11 early literal/tail uncertain retained;4 narrowed MIXED_PARTIAL;0 primary adjudication;16 head and25 tail outside batch03'},'boundary_exceptions':{'reviewed':8,'retained':7,'pending_taxonomy':['W058'],'states':'v5 unchanged89; W047/W086 corrections and W085b fade retained'},'production_specs':{'count':3,'scope':'W001 subevent only; W015 title card; W016 globe/thickness; draft untested'},'audio_listening':'PENDING','reconstruction_test':'NOT_RUN','resources':{'five_hour_initial':15,'five_hour_resume':26,'five_hour_latest':8,'weekly_initial':26,'weekly_latest':41,'disk_free_GiB':92,'memory_pressure_level':2,'swap_used_MB_latest':10176.44,'credits_used':0,'context_percent':'UNAVAILABLE'},'validation':{'states_contiguous':True,'reviewer_rows':10,'native_frames':34,'sequential_decode_mismatches':0},'next_operation':'After fresh usage/ownership checks: audit reviewer15 witnesses semantically; adjudicate W058 taxonomy; then batch04 indexes30:40=W031-W040. No remeasurement/ASR/onboarding.'}
(p/'quality_gate_M.json').write_text(json.dumps(report,indent=2)+'\n')
(p/'CONTINUATION_HANDOFF_M.md').write_text('# Barely Evolved checkpoint M — PARTIAL\n\nLatest continuation supplement; checkpoint L handoff preserved unchanged.\n\n'+json.dumps(report,indent=2)+'\n\nSource/evidence workspace: '+str(p)+'\nSource MP4 and full hash: source_manifest.json. Starting/published predecessor SHA: '+base+'\nPublication receipt: evidence/M_PUBLICATION_RECEIPT.json (written after remote verification).\nBE lock released after successful publication. No Finance branch/index/worktree changes.\nCorrections: tables/m_supplement_corrections.csv; asset aliases: tables/m_asset_alias_crosswalk.csv; narration timing: tables/m_timing_reconciliation.json. Raw reviewer15 outputs preserved.\nW010 supplementary samples are ~1second apart; intermediate motion remains uninspected. First-changed-frame rules preserved with explicit transition states.\n')
# Validate local evidence locators in new production specs and retained raw checksums.
for spec in json.loads((p/'production_specs/specifications_v1.json').read_text()):
 for loc in spec['evidence']:assert (p/loc).exists(),loc
oldfail=[]
for line in (p/'EVIDENCE_SHA256SUMS_checkpoint_L').read_text().splitlines():
 h,name=line.split(None,1);q=Path(name.lstrip('*'));q=q if q.is_absolute() else p/q
 if hashlib.sha256(q.read_bytes()).hexdigest()!=h:oldfail.append(str(q))
assert not oldfail,oldfail
selected=[]
for pat in ['m_scripts/*.py','tables/m_*','tables/k_rep_frames_batch03.csv','agents/reviewer_15/*','production_specs/*.json','quality_gate_M.json','CONTINUATION_HANDOFF_M.md']:
 selected+=list(p.glob(pat))
selected=sorted(set(x for x in selected if x.is_file()))
# Seal all prior checkpoint entries plus new artifacts and native evidence, outside Git.
files=set(selected)
for line in (p/'EVIDENCE_SHA256SUMS_checkpoint_L').read_text().splitlines():
 _,name=line.split(None,1);q=Path(name.lstrip('*'));files.add(q if q.is_absolute() else p/q)
files.update(x for x in (p/'frames/checkpoint_M').rglob('*') if x.is_file());files.update((p/'frames/native_rep/batch03').glob('*.png'))
seal=p/'EVIDENCE_SHA256SUMS_checkpoint_M';seal.write_text(''.join(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+str(f)+'\n' for f in sorted(files)))
selected.append(seal)
# Dedicated external index; no checkout, local branch, active index, stash or working-file mutations.
remote=run('git','ls-remote','origin','refs/heads/research/barely-evolved-visual-forensics').split()[0];assert remote==base,remote
index=p/'evidence/M_publication.index';assert not index.exists();env=dict(os.environ,GIT_INDEX_FILE=str(index))
run('git','read-tree',base,env=env)
for f in selected:
 blob=run('git','hash-object','-w',str(f));dest=prefix+str(f.relative_to(p));run('git','update-index','--add','--cacheinfo','100644',blob,dest,env=env)
tree=run('git','write-tree',env=env)
diff=run('git','diff','--stat',base,tree);(p/'evidence/M_INTENDED_DIFF.txt').write_text(diff+'\n');print(diff)
paths=run('git','diff','--name-only',base,tree).splitlines();assert all(x.startswith(prefix) for x in paths)
assert not any(x.endswith(('.png','.jpg','.mp4','.wav')) for x in paths)
commit=run('git','commit-tree',tree,'-p',base,input='Preserve Barely Evolved checkpoint M: batch03 and bounded corrections\n')
run('git','push','origin',commit+':refs/heads/research/barely-evolved-visual-forensics')
remote=run('gh','api','repos/ghilmanITM360/youtube-intelligence-os/git/ref/heads/research/barely-evolved-visual-forensics','--jq','.object.sha');assert remote==commit
receipt={'checkpoint':'M','parent_sha':base,'commit_sha':commit,'authenticated_remote_sha':remote,'seal_entries':len(files),'seal_failures':0,'publication_paths':paths,'source_evidence_path':str(p),'local_checkout_head_unchanged':run('git','rev-parse','HEAD'),'pr':'not created or changed','utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(p/'evidence/M_PUBLICATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
with (p.parent/'BE_OPS_LOG.txt').open('a') as h:h.write(receipt['utc']+' checkpoint M published '+commit+'; authenticated remote verified; BE lock released\n')
lock=p.parent/'.be_writer_lock';owner=json.loads((lock/'owner.json').read_text());assert owner['session']=='01a19dcb-9bb0-7fc1-bc1e-2bec450b309d'
(p/'evidence/M_LOCK_RELEASED.json').write_text(json.dumps(owner,indent=2)+'\n');(lock/'owner.json').unlink();lock.rmdir()
print(json.dumps(receipt,indent=2))
