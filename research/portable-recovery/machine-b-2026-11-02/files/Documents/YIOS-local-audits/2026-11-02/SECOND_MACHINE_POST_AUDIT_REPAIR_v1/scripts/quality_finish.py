from audit import *
def main():
 write('OWNER_REPORT_ROMAN_URDU.md',f'''# YIOS audit — Roman Urdu owner report — 2 November 2026

1. **Yeh machine pehle kitni behind/ahead thi?** Apne configured upstream ke muqable mein tamam 24 local branches aur 3 checkouts **0 ahead / 0 behind** thay. Primary checkout Finance branch par tha, main par nahin. Machine A ki alag published branch canonical Finance se 44 commits aur 93 accepted videos aage hai. Yeh alag branch ka published kaam hai; isay apne upstream se missing sync nahin kehna.

2. **Ab kaun se checkouts verified current hain?** Authenticated fetch aur final GitHub read ne Finance aur Claude checkouts ka SHA `223f44981ee174988574e86d5e23ae83ee60ee5d`, coordination ka `205fc7ebadcbde6b5104e9cb2be53de8951511a8`, aur default main ka `08e719264e31ecd82de24f8eeb8f065c08359fe5` confirm kiya. Sab pehle se current thay, is liye fast-forward ki zarurat nahin thi. Machine A branch `9c6f42fb33e493314cced538d5c5fa599a29e6c5` bhi local Git mein recover ho chuki hai. PR #36 OPEN/DRAFT hai; us mein koi change nahin kiya.

3. **Cleanup kya hua aur space kitni bachi?** Sirf 3 verified disposable files hatin: Git refs ka Finder `.DS_Store` aur 2 workbook inspection logs. Gross 44,031,783 bytes remove huay; verified compressed recovery 3,883,529 bytes rakhi. Net logical saving **40,148,254 bytes — 38.29 MiB** hai. Raw evidence aur actual workbook preserve hain. Finder metadata ki wajah se Git integrity failure tha; ab check pass hai. Alag background Git packing ka observed space change cleanup savings mein shamil nahin kiya.

4. **Unique ya active local kaam preserve hua?** Koi uncommitted tracked ya nonignored untracked work nahin mila. Ek purana stash tracked completion-ledger edit ke ilawa 2,267 items / 843,095,575 bytes rakhta hai. Stash, external originals, 7 Codex recovery refs, private `.env`, ignored raw files aur tamam worktrees preserve hain. Zyada tar stash files ki matching copies mil gayin; ek 910,451-byte Finance experiment ZIP ki exact doosri container copy establish nahin hui, is liye woh bhi preserve hai. Local inactivity ko Machine A ka writer release nahin samjha.

5. **Kis branch mein kya kaam aur kitna data hai?** Complete matrix 46 remote branches aur 24 local refs cover karti hai. Canonical Finance mein 461/1,612 accepted limited-evidence audits hain; separate Machine A Finance mein 554/1,612. Purane PR21 corpus mein 16/18 selected Casually Finance structural packages, Casual Economics mein 11 sampled structural packages, aur older editing corpus mein 38 Shorts hain. CT001–005 mein 2 visual-only accepted aur 3 partial packages hain. Twelve-channel metadata mein 445 videos, Monkey mein 76 public videos, aur Barely Evolved mein 4 hain. Production candidates alag branches par hain. Yeh populations overlap karti hain; in ko jor kar independent video count nahin banana.

6. **Kaun se worktrees zaroori, redundant ya uncertain hain?** Ek independent Git common store aur 2 linked worktrees mile. Primary checkout sources/runtime ke liye important hai; coordination ka alag tooling role hai. Claude worktree Finance ke exact HEAD par logical duplicate hai, magar us ki writer assignment aur ignored dependencies ko release nahin mila. Is liye koi worktree nahin hataya. APFS physical sharing unknown hai; logical duplication ko automatically reclaimable disk space nahin kaha.

7. **Research complete, partial, blocked aur pending kitni hai?** Canonical Finance: **461 accepted limited / 16 partial / 17 source-blocked / 1,118 pending**. Separate Machine A version: **554 / 16 / 17 / 1,025**. Dono ek hi 1,612-video population ke versions hain. Full-evidence Finance completion 0 hai; full AV signoff bhi 0 hai. Latest published Machine A queue **NICK_279 — `pTyMmSZ2EVs`** hai. Canonical handoff ka purana NICK_186 Machine A branch par already complete hai; usay restart nahin karna.

8. **Kaunsa data yahan hai aur kaunsa Machine A par referenced hai?** Tamam 456 registered media files hash-match karti hain: 454 video + 2 audio, 4.06 GiB. Finance ke 26/26 frozen inputs verified hain. CT001–005 ke exact source MP4s yahan hain. CT006 ka purana 49,993,573-byte MP4 existing ZIP mein verified hai; lekin us ka naya reported Checkpoint B workspace aur recent unpublished reviewers yahan establish nahin huay. Transfer appendix mein 5,092 manifest/checksum entries hain, jin mein 12 ke local hash matches mile. Jahan source manifest size ya workspace path nahin deta, woh UNKNOWN hi rakha hai. 6 LFS payload versions absent hain; current frozen registry DB real aur verified hai.

9. **Data ko aaj practically kaise use kar sakte hain?** Nick Invests ke 363 registered video rows query kar sakte hain. Video ID se JSONL packet, read receipt, actual thumbnail aur stored transcript retrieve ho sakta hai. Same-channel strong/typical/weak comparisons, claim/source-receipt joins, visual DNA/state ledgers aur original storyboard references available hain. `DATA_USE_GUIDE.md` mein 10 workflows ke real paths, commands, expected outputs aur limits hain. Koi naya video audit ya content plan generate nahin kiya.

10. **Sab se important risks aur next steps kya hain?** Pehle Finance branch/writer reconciliation aur Machine A ka actual CT006 handoff recover karein. Finance universe CSV ka completion count 430 par stale hai; current JSONL aur workbooks 461/554 par agree kartay hain. DS28/30 ke shared `.gitattributes` fingerprints 2 ledger failures dete hain; raw source corruption prove nahin hui. 38 Finance tests aur 2 Node tests pass hain; full suite mein 459 pass, 1 skip aur 1 fail hai. Final Git integrity, registry, frozen-source aur media hash checks pass hain. Hosted CI billing ki wajah se 0 steps par blocked hai. Working Python 3.12 `.venv` use karein; system Python 3.14 ka XML runtime broken hai. Missing native visual/audio evidence aur semantic verification ko pass declare nahin kiya.

**Evidence ki hadd:** Git SHAs, filesystem bytes/hashes, recomputed counts aur local tests measured facts hain. Purane branch status/reviewer receipts published historical evidence hain. New CT006 B ke shards 1 aur 3 passed, 8 pending wala point owner ka historical report hai. Machine A ke ab ke local files/processes, unpublished CT006 workspace ka exact path/hash/size, private cloud restore aur absent remote LFS payload availability abhi unknown hain. Koi push, merge, PR edit, scheduler change, new reviewer wave ya V2 work nahin hua.

Complete reports aur recovery package: `{OUT}`.
''')
 # Correct prose spacing without modifying command blocks or inline paths/identifiers.
 replacements={
 'MachineA':'Machine A','Machine-A-version':'Machine A version','MachineB':'Machine B','fullAV':'full AV','sourceMP4':'source MP4','SourceMP4':'Source MP4','SHA256and':'SHA256 and','SHA256verified':'SHA256 verified','GitHEAD':'Git HEAD','Gitrefs':'Git refs','GitLFS':'Git LFS','LFSOID':'LFS OID','JSONLand':'JSONL and','JSONLpacket':'JSONL packet','CSVrows':'CSV rows','Video_IDwith':'Video_ID with','source_idsand':'source_ids and','scope/limitations':'scope / limitations','branch-specific':'branch-specific',
 'their6':'their 6','all6':'all 6','all3':'all 3','all24':'all 24','all46':'all 46','allrefs':'all refs','all456':'all 456','all26':'all 26','per-videoSOURCE':'per-video SOURCE','andconfidence':'and confidence','columns:source':'columns: source','→observed':'→ observed','→analyst':'→ analyst','→original':'→ original','→required':'→ required','receipt.source_id,including':'receipt.source_id, including','VERIFIEDclaim':'VERIFIED claim','confidence was only':'confidence was only','Dataset/source':'Dataset/source',
 'The30remote':'The 30 remote','Sixteen remote':'Sixteen remote','other15are':'other 15 are','with0steps':'with 0 steps','0steps':'0 steps','0error':'0 error','0domain':'0 domain','0duplicate':'0 duplicate','0null':'0 null','0first-party':'0 first-party','0findings':'0 findings','1FAIL':'1 FAIL','38PASS':'38 PASS','2PASS':'2 PASS','17PASS':'17 PASS','459PASS':'459 PASS','1SKIP':'1 SKIP','5warnings':'5 warnings','26/26frozen':'26/26 frozen','456/456media':'456/456 media','1,436unique':'1,436 unique','75channels':'75 channels','2,303videos':'2,303 videos','2,291real':'2,291 real','33datasets':'33 datasets','40standard':'40 standard','26datasets':'26 datasets','10channels':'10 channels','667videos':'667 videos','668transcript':'668 transcript','6,953source':'6,953 source','45,774discovered':'45,774 discovered','5,172visual':'5,172 visual','604classifications':'604 classifications','66tracked':'66 tracked','60unique':'60 unique','42channel':'42 channel','966detail':'966 detail','430complete':'430 complete','12placeholders':'12 placeholders','267video':'267 video','1,820structured':'1,820 structured','397canonical':'397 canonical','16source':'16 source','2visual':'2 visual','3partial':'3 partial','0full':'0 full','38Shorts':'38 Shorts','76parent':'76 parent','507states':'507 states','409states':'409 states','254compositions':'254 compositions','922motion':'922 motion','530states':'530 states','367compositions':'367 compositions','1037receipt':'1037 receipt','19stored':'19 stored','20locally':'20 locally','6missing':'6 missing','5,092path':'5,092 path','41external':'41 external','968/103':'968 / 103','695evidence':'695 evidence','701frames':'701 frames','280disputes':'280 disputes','384unique':'384 unique','26distinct':'26 distinct','19older':'19 older','1current':'1 current','6absent':'6 absent',
 }
 for p in OUT.glob('*.md'):
  if p.name=='OWNER_REPORT_ROMAN_URDU.md':continue
  s=p.read_text();parts=re.split(r'(```[\s\S]*?```|`[^`\n]*`)',s)
  for i in range(0,len(parts),2):
   for old,new in replacements.items():parts[i]=parts[i].replace(old,new)
  p.write_text(''.join(parts))
 # The final two workflow sections deserve full sentences, not compressed handoff notation.
 guide=OUT/'DATA_USE_GUIDE.md';s=guide.read_text();start=s.index('## 9. Resume');s=s[:start]+'''## 9. Resume the correct next research task

No research task was resumed during this audit. Read the live branch's `FINANCE_WRITER_OWNERSHIP.md`, `FINANCE_PROGRESS_CHECKPOINT.json` and latest `RESUME_HERE.md`, then verify its remote head and writer ownership before any write. Canonical Finance names NICK_186 `XP-26tqGFXc`; Machine A's separate branch already completed it and currently names NICK_279 `pTyMmSZ2EVs`. Reconcile publication and writer handback before selecting a queue. Do not restart accepted work from an older handoff.

The old Casually Finance Shorts pilot queue and CT003 checkpoint 6 guidance are stale. Current published gates are CT003 checkpoint 11, CT004 P and CT005 J. New CT006 B needs its actual unpublished workspace and current writer record; the older PR21 package cannot resume the new reviewers.

Coordination tooling exists in the separate existing coordination worktree. Read its `docs/YIOS_TWO_MAC_WORKFLOW.md`. The nonproduction test claim tips are RELEASED; they do not release protected legacy writers. Seventeen passing local tests do not establish actual second-Mac acceptance. Expected output is the correct existing queue and explicit ownership gate, not a new scheduled task.

## 10. Transfer or reconstruct the environment here

The existing checkout and runtime are usable: project Python 3.12.14, openpyxl, Pillow, pytest, Node, ffmpeg/ffprobe and Git LFS. No new clone or worktree is needed. Check the frozen hashes and `lfs_presence.csv` before deciding whether any missing LFS payload is needed. A later necessary exact path can be fetched with existing Git LFS, for example `git lfs fetch origin <branch> --include=<exact-path>`. This was not run for the six unneeded missing versions. Materialize only the intended absent file and verify its OID/hash; preserve any differing frozen source.

Use `YIOS_MEDIA_ROOT=/Users/ghilmanislam360/Documents/YIOS-Media-Library` in the consumer environment and read the media branch's registry. Older `data/local-channel-media` paths are stale. Preserve the private `.env`; do not copy credentials into Git or reports. Obtain only the required missing CT evidence from the documented Machine A roots, stage it, compare hashes and preserve collisions. Source MP4s for CT001–005 already exist here. The older CT006 source can be streamed from its existing ZIP; compare the newer checkpoint's source fingerprint first.

Install numpy, Whisper or PySceneDetect only if a future authorized forensic task requires them, in a compatible environment. System Python 3.14 has an XML runtime failure and is outside the project contract. A future workbook/document rebuild should locate bundled dependencies using the supported workspace-dependency loader instead of another Mac's cache path. No environment repair, regeneration, redownload, research wave or V2 infrastructure was needed for this audit.

Expected output is a usable existing Git/runtime/source map and a task-specific transfer/dependency list. The exact missing paths, hashes, known sizes and UNKNOWN fields are in the portability appendices.
''';guide.write_text(s)
 # Treat branch tests/declarations with a precise, path-based status rather than a generic promise.
 rows=read('branch_matrix.json')
 for r in rows:
  checkpoints=r.get('published_checkpoint_declarations',[])
  area=r['authority_paths'].split(';')[0].strip()
  prefix=area.rsplit('/',1)[0] if '.' in area.rsplit('/',1)[-1] else area
  relevant=[d for d in checkpoints if any(p.startswith(prefix) for p in d['paths'])] if prefix else []
  r['relevant_published_checkpoint_evidence']=relevant
  r['latest_validated_checkpoint']='FRESH_CANONICAL_FINANCE_VALIDATORS_38_PYTEST_2_NODE_AT_'+r['sha'] if r['name'] in ['research/finance-economics-intelligence','claude/finance-audits-machine-b-0044ae'] else ('FRESH_17_COORDINATION_TESTS_AT_'+r['sha'] if r['name']=='codex/yios-dual-machine-coordination' else 'PUBLISHED_DECLARATIONS_ONLY_NOT_RERUN; see relevant_published_checkpoint_evidence and exact branch authority paths')
 write('branch_matrix.json',rows);csvout('branch_matrix.csv',rows)
 # Small actual retrieval examples, retained with exact provenance.
 base=ROOT/'research/finance-economics-intelligence';records=[json.loads(l) for l in (base/'VIDEO_AUDIT_966.jsonl').read_text().splitlines()];ex=[]
 for vid in ['1GowFTjbUnk','9r-45QPLl-Y','AKrjI9m6fpk','XJ4ls6r2MCE']:
  r=next(r for r in records if r['Video_ID']==vid);ex.append({'ref':'origin/research/finance-economics-intelligence','sha':git('rev-parse','HEAD'),'video_id':vid,'batch_id':r['batch_id'],'title':r['identity']['Title'],'statuses':r['statuses'],'performance':r['performance'],'thumbnail_path':r['thumbnail'].get('image_path'),'transcript_source':r['script'].get('source')})
 write('retrieval_examples.json',ex)
 # Validate all report-internal links and all required deliverables.
 required=['README.md','SYNC_REPORT.md','BRANCH_AUDIT.md','WORKTREE_CLONE_AUDIT.md','DATA_INVENTORY.md','STRUCTURE_AUTHORITY_MAP.md','CLEANUP_RECOVERY.md','VALIDATION_REPORT.md','PORTABILITY_MISSING_EVIDENCE.md','DATA_USE_GUIDE.md','UNRESOLVED_ISSUES.md','OWNER_REPORT_ROMAN_URDU.md','branch_matrix.csv','worktree_clone_inventory.csv','cleanup_ledger.csv','population_counts.csv']
 assert all((OUT/n).is_file() and (OUT/n).stat().st_size for n in required)
 broken=[]
 for p in OUT.glob('*.md'):
  for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if '://' not in target and not target.startswith('#') and not (p.parent/target.split('#')[0]).exists():broken.append({'file':p.name,'target':target})
 assert not broken,broken
 assert len(rows)==70 and sum(r['kind']=='remote' for r in rows)==46
 assert len(read('worktree_clone_inventory.json'))==3
 for r in read('RECOVERY_MANIFEST.json'):assert sha(OUT/r['path'])==r['sha256']
 assert all(not git('status','--porcelain=v1','--untracked-files=all',cwd=Path(d['path'])) for d in read('before/checkouts.json'))
 write('PACKAGE_QA.json',{'checked_at':now(),'required_deliverables':len(required),'all_present':True,'broken_report_links':broken,'branch_rows':70,'remote_branches':46,'local_branches':24,'worktrees':3,'recovery_manifest_hashes':'MATCH','checkouts_clean':True,'workbook_jsonl_comparison':'0 mismatches on both audited Finance heads','note':'No complete semantic/source-availability certification inferred.'})
 for p in Path('/private/tmp/yios-sync-audit-v1').glob('*.py'):shutil.copy2(p,OUT/'reproduce'/p.name)
 print(json.dumps(read('PACKAGE_QA.json'),indent=2))
if __name__=='__main__':main()
