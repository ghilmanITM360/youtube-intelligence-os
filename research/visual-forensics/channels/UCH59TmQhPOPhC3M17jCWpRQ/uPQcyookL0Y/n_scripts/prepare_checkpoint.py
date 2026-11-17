from pathlib import Path
import csv,json,hashlib,subprocess,os,re
p=Path.cwd();repo=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');base='04ab57ff422b505533b49f4875b0c9e387c9b056';prefix='research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/uPQcyookL0Y/'
def rows(f):return list(csv.DictReader((p/f).open()))
def save(f,r):
 keys=list(dict.fromkeys(k for x in r for k in x))
 with (p/f).open('w') as h:w=csv.DictWriter(h,fieldnames=keys);w.writeheader();w.writerows(r)
def run(*args,**kw):return subprocess.check_output(args,cwd=repo,text=True,**kw).strip()
a=rows('agents/reviewer_16/art_audit_batch04.csv');rr=rows('agents/reviewer_16/evidence_reads.csv');n=rows('agents/reviewer_16/narration_relation_batch04.csv');expected=rows('tables/k_rep_frames_batch04.csv')
assert len(a)==10 and {x['state'] for x in a}=={f'W{i:03}' for i in range(31,41)}
assert len(rr)==30 and {x['path'] for x in rr}=={x['native_png'] for x in expected}
for x in rr:
 assert hashlib.sha256((p/x['path']).read_bytes()).hexdigest()==x['sha256']
 assert x['state'] in x['path'] and '_f'+x['frame']+'.png' in x['path']
assert {int(x['seg_index']) for x in n}==set(range(25,35))
for x in n:
 for loc in x['visual_frames_judged'].split(';'):
  loc=loc.strip()
  if not loc:continue
  assert (p/loc).exists(),loc
  f=int(re.search(r'_f(\d+)',loc).group(1));assert float(x['asr_start_s'])<=f*1001/30000<float(x['asr_end_s']),[x['seg_index'],f]
art=rows('tables/m_art_consolidated.csv')+a;assert len(art)==40;save('tables/n_art_consolidated.csv',art)
narr=[]
for file in ['tables/k_narration_relation_assessed_batch01.csv','tables/k_narration_relation_assessed_batch02.csv','tables/m_narration_batch03_adjudicated.csv','agents/reviewer_16/narration_relation_batch04.csv','tables/n_asr27_primary_supplement.csv']:
 for r in rows(file):r['source_assessment']=file;r['coverage_qualification']='SPARSE_PARTIAL_ASR_ONLY_NOT_LISTENED';narr.append(r)
for r in narr:
 r['effective_relation']=r['relation']
 if r['seg_index']=='4':r['effective_relation']='MIXED_PARTIAL';r['effective_correction']='Contradictory joke only witnessed coffee-face845; other portions literal/mixed. m_supplement_corrections.csv'
 if r['seg_index']=='8':r['effective_correction']='New Daddy? witness2041 within segment; retain UNRELATED_HOLD/lowconfidence for W011 and uncertainty elsewhere. m_supplement_corrections.csv'
 if r['seg_index']=='11':r['effective_correction']='Keep early literal and uncertain tail separately; no audio-timing signoff.'
 r['evidence_status']='PARTIAL_SPARSE; interval-specific context qualifiers in raw rationale remain authoritative'
save('tables/n_narration_assessments_consolidated.csv',narr)
report={'status':'PARTIAL','art_start_checkpoint_L':20,'art_end':40,'states_total':89,'art_scope':'W001-W040 sparse native review; intermediate motion not fully inspected','narration':{'assessed_unique_segments':35,'segment_ids':'0-34','primary_supplement_segment_ids':[27],'ledger_unique_segments':35,'full_audio_verified_segments':0,'coverage':'All35 have partial sampled visual evidence only; segment27 primary two-frame supplement supersedes raw reviewer uninspected status; no full segment completion claimed. Segment25 has separate head/tail judgments across batches.','prior_uncertain_segments':[8,11,22],'batch04_uncertain_segments':[int(x['seg_index']) for x in n if 'UNCERTAIN' in x['relation']],'corrections':'m_supplement_corrections.csv controls seg4 narrowed MIXED_PARTIAL and seg8 Daddy? witness. m_reviewer15_corrections.json controls18/19. Preserve raw differing11 judgments and0 primary adjudication.'},'boundaries':{'eight_exceptions_reviewed':True,'remaining':[],'v6_change':'Only W058 kind→TRANSITION_STATE; all89 IDs/bounds unchanged; earlier state versions immutable'},'production_specifications':{'scoped_drafts':3,'fully_reconstructed':0,'file':'production_specs/specifications_v1.json'},'actual_listening':'PENDING','reconstruction_test':'NOT_STARTED','source':'source_manifest.json; durable MP4 outside Git','validation':{'batch04_native_frames':30,'sequential_pixel_mismatches':0,'witness_ID_hash_checks':'PASS','state_coverage':'89 contiguous states,14647frames; identity map validated'},'resources':json.loads((p/'evidence/N_resources.json').read_text()),'next_operation':'Fresh usage/ownership gate; inspect batch05 indices40:50=W041–W050, reuse existing valid frames, run one bounded native-art/overlapping-ASR reviewer. Continue original specs; actual listening remains separate.'}
(p/'quality_gate_N.json').write_text(json.dumps(report,indent=2)+'\n')
(p/'CONTINUATION_HANDOFF_N.md').write_text('# Barely Evolved checkpoint N — PARTIAL\n\nLatest handoff. Original L and M immutable.\n\n'+json.dumps(report,indent=2)+'\n\nWorkspace: '+str(p)+'\nPredecessor full SHA: '+base+'\nPublished full SHA and authenticated remote verification: evidence/N_PUBLICATION_RECEIPT.json (local postpublication receipt).\nBranch: research/barely-evolved-visual-forensics. Active canonical checkout remains unrelated branch unchanged; publication uses external index and commit-tree, no new checkout.\nBE lock released after successful publication. Finance/CF untouched. No PR created or changed.\nCorrections and reviewer provenance preserved in tables/m_* and tables/n_*; raw reviewers12–16 preserved. Eight shared asset families in explicit reviewer13/14 alias crosswalk, no invented normalization assets.\nIce Age title observed86.92s;20,000years text91.76s;ice landscape v5cut107.373933s: no editorial mismatch established without listening.\n')
selected=[]
for pat in ['n_scripts/*.py','tables/n_*','tables/states_v6_draft.csv','shot_ledger_v6.csv','tables/k_rep_frames_batch04.csv','agents/reviewer_16/*','quality_gate_N.json','CONTINUATION_HANDOFF_N.md','evidence/N_resources.json']:
 selected.extend(x for x in p.glob(pat) if x.is_file())
files=set(selected)
for line in (p/'EVIDENCE_SHA256SUMS_checkpoint_M').read_text().splitlines():
 h,f=line.split(None,1);q=Path(f);assert hashlib.sha256(q.read_bytes()).hexdigest()==h,f;files.add(q)
files.update(x for x in (p/'frames/checkpoint_N').rglob('*') if x.is_file());files.add(p/'EVIDENCE_SHA256SUMS_checkpoint_M');files.update((p/'frames/native_rep/batch04').glob('*.png'))
seal=p/'EVIDENCE_SHA256SUMS_checkpoint_N';seal.write_text(''.join(hashlib.sha256(x.read_bytes()).hexdigest()+'  '+str(x)+'\n' for x in sorted(files)));selected.append(seal)
assert run('git','ls-remote','origin','refs/heads/research/barely-evolved-visual-forensics').split()[0]==base
index=p/'evidence/N_publication.index';assert not index.exists();env=dict(os.environ,GIT_INDEX_FILE=str(index));run('git','read-tree',base,env=env)
for f in sorted(set(selected)):
 blob=run('git','hash-object','-w',str(f));run('git','update-index','--add','--cacheinfo','100644',blob,prefix+str(f.relative_to(p)),env=env)
tree=run('git','write-tree',env=env);paths=run('git','diff','--name-only',base,tree).splitlines();assert all(x.startswith(prefix) for x in paths);assert not any(x.endswith(('.png','.jpg','.mp4','.wav')) for x in paths)
receipt={'base':base,'tree':tree,'seal_entries':len(files),'paths':paths,'checkout_head':run('git','rev-parse','HEAD')};(p/'evidence/N_PREPARED.json').write_text(json.dumps(receipt,indent=2)+'\n');print(run('git','diff','--stat',base,tree))
