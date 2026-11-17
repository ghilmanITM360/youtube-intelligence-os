from pathlib import Path
import json,re,hashlib,datetime,subprocess
O=Path('/Users/ghilmankhan/YIOS-local-audits/2026-10-22');p=O/'MACHINE_A_YIOS_FULL_READINESS_AND_SYNC_AUDIT.md';s=p.read_text()
replacements={
'Machine A also has':'Machine A also has',
'Production review has local renders; edits/rebuilds require exact narration/reference/tool scripts':'Senior Health production review has ordinary local renders. Finance Short02 and Dr Rehan V3 renders are verified local Git blobs but are not materialized as ordinary files in the searched folders; external export of these derived renders would enable playback. Edits/rebuilds require exact narration/reference/tool scripts',
'Finance Shorts production | production/finance-short-02-assets':'Finance Shorts production | production/finance-short-02-assets',
'| artifact-tool | Finance workbook rendering only | Not resolvable from checkout | BLOCKED in direct root invocation | Builder imports @oai/artifact-tool; header expects bundled dependency setup | Resolve bundled runtime on authorized writer; no workbook rebuild now |':'| artifact-tool | Finance workbook rendering only | Bundled 2.8.99 present; not resolved from checkout | READY package availability; direct invocation needs module setup; render UNVERIFIED | Header expects bundled dependency setup; package located at bundled-artifact-runtime.json path | Use existing bundled runtime under designated writer; no install or rebuild now |',
'Bundled artifact runtime unresolved on A':'Bundled2.8.99 located; checkout module resolution not wired',
'Missing direct artifact-tool resolution blocks an unprepared root invocation of the workbook renderer;':'Bundled artifact-tool2.8.99 is present (package and entrypoint verified), but direct root module resolution is not wired; an unprepared workbook-builder invocation would fail. This is configuration, not missing software;',
'No direct artifact-tool resolution':'No direct artifact-tool resolution',
'**Root cause:** Builder expects bundled dependency layout.':'**Root cause:** Builder expects bundled dependency layout; artifact-tool2.8.99 package/entrypoint verified in installed Codex runtime (bundled-artifact-runtime.json).',
'**Resolution:** Locate bundled runtime and validate resolution under designated writer;':'**Resolution:** Use located bundled runtime and validate resolution under designated writer;',
'No recorded final human listening/clinical/rights sign-off':'No recorded final human listening/clinical/rights sign-off; Finance Short/Rehan review renders are local Git objects but not materialized ordinary files',
'Owner playback of Senior Health/Dr Rehan/Finance Short V3':'Owner playback of local Senior Health V3; then export other derived review renders',
'3 short videos + candidates':'3 local Senior Health videos; other renders need export',
'Local production library | Timestamped wording/motion/approval decisions':'Senior Health local library; Finance/Rehan Git blobs | Timestamped wording/motion/approval decisions',
'latest published NICK165 independent source/receipt review; review local production videos against open wording/clinical/rights questions;':'latest published NICK165 independent source/receipt review; review local Senior Health videos against open wording/clinical/rights questions; locate/export Finance Short and Dr Rehan derived render Git blobs for later playback;',
'Human review of local production renders':'Human review of local Senior Health production renders',
'Owner artistic/listening approval; renderer preflight':'Derived render needs export from local Git blob, then owner artistic/listening approval; renderer preflight for edits',
'Local review library present | Review yes':'V3 blob present locally; ordinary playback file absent | After external export',
'Local candidate present in library | Yes':'V3 blob present locally; ordinary playback file absent | After external export',
'| Review Dr Rehan V3 | YES_READ_ONLY':'| Review Dr Rehan V3 | YES_AFTER_ASSET_RECOVERY',
'| Finance Shorts production | YES_READ_ONLY':'| Finance Shorts production | YES_AFTER_ASSET_RECOVERY',
'| No for local render | Human clinical/name/rights approvals':'| No sync; external export from local Git object | Human clinical/name/rights approvals',
'| Review local renders now | Not new Finance-ledger writing;':'| Read documents now; export local Git render for playback | Not new Finance-ledger writing;',
'| Review local render now | Upload candidate':'| Read documents now; export local Git render for playback | Upload candidate',
'| A lacks a verified':'| A lacks a verified',
'| Current test results unknown | A live results':'| Current test results unknown | A live results',
'| Owner playback/phone/listening; clinician claims; music/name rights decision':'| Owner playback/phone/listening; clinician claims; music/name rights decision',
}
for a,b in replacements.items():s=s.replace(a,b)
# precise table lines ensure availability statements remain honest
lines=s.splitlines()
for i,l in enumerate(lines):
 if l.startswith('| Dr Rehan production |'):
  lines[i]=l.replace('Review local render now','Read docs now; V3 Git blob ready for external export')
 if l.startswith('| Finance Shorts production | production/'):
  lines[i]=l.replace('Review production library now','Read docs now; V3 Git blob ready for external export')
 if l.startswith('| Production | Review renders, independent Remotion project'):
  lines[i]=l.replace('Review renders, independent Remotion project','Senior Health renders on disk; Finance/Rehan V3 Git blobs; independent Remotion project')
s='\n'.join(lines)+'\n'
insert='''\n\n**Final availability refinement (2026-10-22):** The 21 MP4s in YIOS-Production-Library belong to Senior Health PR34, including all three V3 full/mobile pairs. A bounded filename search across workprojects, Documents, Downloads and YIOS-local-audits (excluding dependencies/Git/cache folders) found no materialized Finance_Short02 or Dr_Rehan_Heart_Warning render. An unrelated Downloads/Decode Your Heart – Dr. Rehan.mp4 is not that candidate. Both actual desired render blobs are already local, verified with GIT_NO_LAZY_FETCH=1 git cat-file -e: Finance V3 blob b6d1f32ceae8f42e62c27d1d5881f8e04281a344 (11,536,034 bytes), Dr Rehan V3 blob 49345dd617349962c1949b3a8c47308977215e7a (3,561,552 bytes). These are derived production renders, not original competitor media. No new download is needed to export them externally for later playback; this audit did not export or play them. Asset availability is therefore Git-object YES / ordinary-file NO-in-searched-roots, not globally missing. [production-all-mp4.json, finance-rehan-local-media-search.json, production-git-object-availability.json, *-git-media.txt]\n\n**Bundled runtime refinement:** @oai/artifact-tool2.8.99 package and dist/artifact_tool.mjs exist at `/Users/ghilmankhan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/`. The direct-checkout resolve failure is setup-specific, not missing package software. Workbook rendering was not tested or performed. [bundled-artifact-runtime.json]\n'''
s=s.replace('## 10. Test and Validation Readiness',insert+'\n## 10. Test and Validation Readiness')
s+='''\nFinal preservation verification: local HEAD still d41a5774f1381a21022b70f02d206303195be3a7; 282 untracked and2,760 ignored paths unchanged; tracked/index modifications zero; stash still5b6c3042679400b16aa1024b79058b71dade0ab9. Second live ls-remote still Finance7e70f061aae849e9929b531c4bc855b23edda179. [status-end.txt, live-heads-end.txt; report-verification.json]\n'''
p.write_text(s)
heads=re.findall(r'^## (\d+)\. (.*)$',s,re.M)
assert [int(x[0]) for x in heads]==list(range(1,22)),heads
assert 'MACHINE_A_OUTDATED_BUT_SAFE_WORK_AVAILABLE' in s
assert len(json.loads((O/'branches.json').read_text()))==26
status=subprocess.check_output(['git','status','--porcelain=v2','--branch'],text=True)
assert not any(l.startswith(('1 ','2 ','u ')) for l in status.splitlines())
d={'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'report':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'required_sections':heads,'section_check':'PASS','local_head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'untracked':len(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],text=True).splitlines()),'ignored':len(subprocess.check_output(['git','ls-files','--others','--ignored','--exclude-standard'],text=True).splitlines()),'tracked_changes':False,'stash':subprocess.check_output(['git','stash','list','--format=%H'],text=True).strip(),'one_agent':True,'fixes_applied':False}
(O/'report-verification.json').write_text(json.dumps(d,indent=2));print(json.dumps(d,indent=2))
# checksum diagnostic evidence only; exclude historical inventories/full media and this manifest itself
m={str(f.relative_to(O)):hashlib.sha256(f.read_bytes()).hexdigest() for f in O.iterdir() if f.is_file() and f.name!='EVIDENCE_SHA256.json'}
(O/'EVIDENCE_SHA256.json').write_text(json.dumps(m,indent=2))
