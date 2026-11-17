import json,datetime,collections,hashlib
from pathlib import Path
R=Path(__file__).parent;B=R/'recovery-20261026-machine-b-handoff'
def read(p):return json.loads(p.read_text())
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ');D=R/('checkpoint-'+now);D.mkdir(mode=0o700)
objects=read(B/'SOURCE_TO_DRIVE_INVENTORY.json')['files'];uploaded=read(B/'HANDOFF_DRIVE_RECEIPT.json')['total_uploaded_bytes_including_source_backup'];verified=uploaded;members=[];aliases=[];batch_reports=[]
for p in sorted(R.glob('CONTROL-UPLOAD-*.json')):
 u=read(p);v=read(R/('CONTROL-VERIFY-'+p.name[len('CONTROL-UPLOAD-'): ]));assert v['status']=='VERIFIED';uploaded+=u['uploaded_bytes'];verified+=v['retrieved_bytes']
for d in sorted(R.glob('batch-*')):
 if int(d.name.split('-')[1])<10:continue
 assert (d/'RECEIPT.json').exists(),'UNFINISHED_BATCH'
 r=read(d/'RECEIPT.json');assert r['status']=='VERIFIED';uploaded+=r['uploaded_bytes'];verified+=r['independently_retrieved_bytes'];batch_reports.append({k:r[k] for k in ['batch','status','uploaded_bytes','independently_retrieved_bytes','mapped_source_files']})
 for x in r['files']:
  objects.append({'source':x['source_absolute'],'restore_relative':x['restore_relative'],'bytes':x['bytes'],'sha256':x['fresh_sha256'],'remote_id':x['remote_id'],'remote_url':x['remote_url'],'batch':d.name,'status':'VERIFIED','independently_retrieved_bytes':x.get('retrieval',{}).get('retrieved_bytes',0),'duplicate_of_verified':x.get('duplicate_of_verified',False),'verification_receipt':str(d/'RECEIPT.json'),'priority':x['backup_priority'],'video_id':x.get('video_id'),'type':'evidence_archive' if x.get('package_manifest') else 'original_media','package_manifest':x.get('package_manifest'),'package_original_source_root':x.get('package_original_source_root'),'package_group_key':x.get('package_group_key'),'package_part':x.get('package_part'),'package_group_parts':x.get('package_group_parts')})
  if x.get('package_manifest'):
   pm=read(Path(x['package_manifest']));v=x['retrieval'];assert v['package_source_members_verified']==len(pm['members'])
   for alias in pm.get('duplicate_aliases',[]):aliases.append(dict(alias,source_package_remote_id=x['remote_id'],source_package_manifest=x['package_manifest'],verification_status='FRESH_SOURCE_HASH_EQUALS_REVALIDATED_PILOT_REMOTE_OBJECT'))
   for m in pm['members']:members.append({k:m[k] for k in ['source_absolute','restore_relative','bytes','sha256','video_id','role']}|{'remote_archive_id':x['remote_id'],'remote_archive_sha256':x['fresh_sha256'],'archive_member':m['restore_relative'],'verification_status':'COMPLETE_REMOTE_DECOMPRESSION_MEMBER_SHA256_VERIFIED','batch':d.name})
known_media={m['sha256']:m['video_id'] for m in read(B/'MACHINE_B_REQUIRED_MEDIA.json')['files'] if m['role']=='ORIGINAL_MP4'}
for x in objects:
 if x['sha256'] in known_media:x['video_id']=known_media[x['sha256']]
 s=x['source'];p=Path(s)
 if '/Downloads/videos in mp3/' in s:x['channel']=s.split('/Downloads/videos in mp3/')[1].split('/')[0]+' (source-folder provenance)'
 elif '/selected-evidence-packages-' in s and '/yio-cf-editing-forensics-local-evidence' in (x.get('package_original_source_root') or ''):x['channel']='Casual Finance (registered forensic source root)'
 elif '/selected-evidence-packages-' in s and 'video data of what if' in (x.get('package_original_source_root') or ''):x['channel']='WHATIF production archive (source-root provenance; public ID unassigned)'
 elif '/finance-publication-evidence-' in s:x['channel']='Finance publication research evidence (public channel ID unassigned)'
 elif '/workprojects/video data of what if/' in s:x['channel']='WHATIF forensic/production sources (source-root provenance; public channel ID unassigned)'
 elif '/ct-evidence-packages-' in s or '/yio-cf-editing-forensics-local-evidence/' in s or '5umJ63d3rzQ-deep-ct-scan' in s:x['channel']='Casual Finance'
 elif '/productions/senior-health-casually-finance-3/' in s:x['channel']='Owner senior-health production; public channel unconfirmed'
 else:x['channel']='UNASSIGNED'
summary={'observed_utc':now,'physical_uploaded_bytes_before_this_handoff':uploaded,'physical_independently_verified_bytes_before_this_handoff':verified,'unique_source_backup_remote_objects':len({x['remote_id'] for x in objects}),'mapped_container_and_direct_source_paths':len(objects),'direct_original_source_paths':sum(x['type']!='evidence_archive' for x in objects),'exact_pilot_alias_paths_reused':len(aliases),'remote_archive_members_sha256_verified':len(members),'remote_archive_logical_member_bytes':sum(x['bytes'] for x in members),'covered_original_source_paths_including_archive_members':sum(x['type']!='evidence_archive' for x in objects)+len(members)+len(aliases),'package_logical_bytes_are_not_added_to_physical_upload_or_download_bytes':True,'budget_remaining_before_this_handoff':12000000000-uploaded,'batch_reports':batch_reports}
groups=collections.defaultdict(lambda:{'mapped_paths':0,'independently_retrieved_physical_bytes':0,'logical_bytes_at_paths':0})
for x in objects:
 g=groups[x['channel']];g['mapped_paths']+=1;g['independently_retrieved_physical_bytes']+=x['independently_retrieved_bytes'];g['logical_bytes_at_paths']+=x['bytes']
for n,x in [('SOURCE_TO_DRIVE_INVENTORY.json',{'summary':summary,'channel_groups':dict(groups),'objects':objects,'archive_members':members,'exact_duplicate_pilot_aliases':aliases}),('SUMMARY.json',summary)]:
 p=D/n;p.write_text(json.dumps(x,indent=2,ensure_ascii=False));p.chmod(0o400)
old=(B/'YIOS_MACHINE_B_HANDOFF_20261026.md').read_text();finance_visual=old[old.index('## Finance / Economics published checkpoint'):old.index('## Required Machine B evidence transfer')]
media=read(B/'MACHINE_B_REQUIRED_MEDIA.json')['files']
for m in media:
 m['verified_remote_objects']=[{'remote_id':x['remote_id'],'remote_url':x['remote_url'],'batch':x['batch']} for x in objects if x['source']==m['path'] and x['sha256']==m['sha256']]
 m['verified_archive_members']=[x for x in members if x['source_absolute']==m['path'] and x['sha256']==m['sha256']]
packages=[x for x in objects if x['type']=='evidence_archive'];coverage=read(R/'batch-0012/REFERENCED_EVIDENCE_COVERAGE.json')
finance_visual='Preserved production checkpoint observed '+read(B/'FINANCE_PUBLISHED_CHECKPOINT.json')['observed_utc']+'. This backup update does not recertify current production ownership or newer PR heads; Machine B must independently accept/validate before production writes.\n\n'+finance_visual
text=f'''# YIOS Machine A → Machine B: verified preservation update {now}

Owner direction now is to continue eligible priority backup within the existing 12,000,000,000-byte cap and 2,000,000,000-byte free Drive reserve, including continuation after natural usage reset. This supersedes the older handoff's stop-after-Batch9 instruction. All other protections remain. No Finance or Visual Forensics ownership transfer is certified by this document.

## Latest verified cloud checkpoint

Pilot and batches1–12 are VERIFIED. Batch9 all20 recovered without re-upload. Batches10–12 complete-source/remote SHA checks passed. One exact duplicate source maps to an already verified remote object; it was not re-uploaded and adds zero new downloaded bytes.

Physical bytes uploaded before this MD: **{uploaded:,}**. Physical complete bytes independently retrieved and SHA-256 verified before this MD: **{verified:,}**. These include the previous183,330-byte handoff document. This new MD also counts toward the cap; its exact bytes/remote ID/hash and verified retrieval are recorded in separate CONTROL-UPLOAD/CONTROL-VERIFY receipts after upload. No attempt is counted as successful upload.

There are **{summary['unique_source_backup_remote_objects']} unique source-backup remote objects**, mapping {len(objects)} direct-source/container paths. Three are compressed evidence archives containing **{len(members):,} original source members**, independently streamed/decompressed and SHA-256 verified from fresh remote reads. Those members represent **{summary['remote_archive_logical_member_bytes']:,} uncompressed bytes**; do not add them to physical uploaded/downloaded bytes. Covered original paths including archive members: {summary['covered_original_source_paths_including_archive_members']:,}. This includes one exact duplicate content mapping and excludes archive-container paths from the original-path count.

Earlier supplied pilot+1–8 narrative total was 3,000,000 bytes too high. Frozen receipts sum to1,257,792,933 pre-Batch9 bytes; corrected source total after Batch9 was1,447,376,649. Historical receipts are unchanged.

## Machine B evidence now available in private Drive

All three original Video001/002/003 MP4s now have verified cloud mappings and refreshed source SHA-256 values (see media appendix). Original MP4s remain outside Git. Three bounded CT packages also preserve the existing audit snapshot and explicit SOURCE.json, SENTENCES.csv and registered thumbnail companions. No entire backup-payload staging copy was made; archives are durable bounded artifacts outside the checkout, originals untouched.

Archive verification checked every expected tar member's full byte length and SHA-256 during authenticated remote streaming, then the complete compressed response's byte length/SHA-256, plus original source stability. No local source substituted for remote bytes, no extraction overwrote any local path, no archived program was executed. Embedded member-manifest status records the historical pre-upload packaging step; the outer VERIFIED batch receipts are the current cloud status.

Restore locators: each archive member below names the actual remote archive ID, archive SHA-256, original absolute path, restorable relative path, member SHA-256 and size. On Machine B, download by those IDs, verify compressed bytes, then safely restore only under an owner-selected durable destination with no overwrites and verify every member. Download the separate original MP4s and pilot checkpoint6 checksum manifest too. Machine B full runtime recovery and writer acceptance have **not** been executed or certified.

Referenced evidence coverage: Video001105/105 hashes and Video0021,103/1,103 hashes match. Video0031,822/1,823 match; only .DS_Store Finder directory cache was intentionally excluded as reproducible non-evidence. The original .DS_Store and historical checksum manifest remain unchanged. Do not call the package a byte-identical full directory mirror. Files created after the original bounded inventory, other historical source folders and dependencies outside the named packages are not automatically included.

## Legitimate transfer capabilities

Connector local-file upload materialization is limited to104,857,600 bytes; its HTTP413 for117,441,481 bytes occurred before Drive action invocation. Two smaller CT packages used the supported connector. Video003 package used owner-authenticated Google Drive File upload UI into the exact private bulk folder; visible completion, actual row data-id, independent connector metadata, fresh raw remote retrieval and every member hash all passed. No payment, installation, credential invention or security bypass occurred. For future files over100MiB, use this qualified browser upload path; do not repeatedly retry the size-limited connector. Rename only a newly created unfinished upload to its collision-safe planned name if needed, with supported metadata action, before freeze; never change previously verified objects. Always preserve actual returned identities.

Connector name search returned empty even for a newly UI-confirmed object; empty search is not authoritative proof of absence. Use actual UI object identity and fresh metadata to reconcile uncertain uploads; never blindly upload duplicates. The initial unsaved upload response was an observability error; exact second-call HTTP413 and all recovery evidence are retained. No unresolved Batch12 upload remains.

## Resources, privacy and next continuation

Authenticated owner kgk2930@gmail.com. Exact yios folder1oMMnSUdeXvQe4do6i6__Dj-diKzD1dvr; bulk folder12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf; MyDrive parent0AIBUCbMhIl95Uk9PVA. Fresh metadata: owner-only, shared=false, consistent Restricted inherited access. No permission changes. Google provider-managed encryption approved; owner-held client encryption key not established. Retain until explicit owner removal approval.

Fresh owner Google One UI after Batch12:2.92GB of15GB used; approximately12.08GB available (rounded UI, not exact API bytes). Drive2.62GB; Gmail302.23MB. Account usage is not YIOS source uploaded bytes. Conservative next-batch free-space observation11.98GB; re-observe quota before every batch. Payload cap remainder before this MD:{12000000000-uploaded:,} bytes.

Latest limits32% five-hour,31% weekly; paid credits0 and none spent/reset. Mac df available19,018,772KiB (about18.14GiB). Exact context meter unavailable; continuation checkpoints preserve long-running context. One preserved protected Claude writer has not been released; other named Codex preservation and Finance chats were notLoaded at last app observation, which does not prove MachineB/Claude inactivity. No competing source modification detected by fresh stability checks.

Continue from latest immutable batch receipts with **ORDERED_PLAN_V4.json** and reviewed continue_backup.py. The 30-minute heartbeat automation yios-verified-backup-continuation belongs to this same chat, checks natural limits, and resumes remaining eligible backup when safe and the Mac/Codex/network are available. Never use reset credits. Start no new expensive batch near90% five-hour/95% weekly; freeze a verified atomic checkpoint first. Authentication/privacy/quota/source/hash/ownership/charge or unsupported-method failure stops uploads until legitimately resolved. Do not start another inventory, repeat a verified upload or assume partial packages complete. After the selected plan, consider remaining unique recovery/checkpoint scope from existing manifests within cap/reserve; exclude credentials, agent settings and unrelated documents.

No local source deletion, move or cleanup; no Git branch/HEAD/stash/LFS mutations, PR36/44 merges, Finance audit writes or Video003 completion-status edits. Current preserved canonical checkout remains codex/what-if-archive-main-integration at badec432bbf5610748123b3f0e0bcb9cdb25fa10; Finance and protected forensic heads are below. Updated receipts are external under {D}. This is file-level cloud recovery, not independent-machine disaster recovery.

{finance_visual}
## Original media identities and cloud locators

```json
{json.dumps(media,indent=2,ensure_ascii=False)}
```

## Physical object inventory and channel/source-folder coverage

```json
{json.dumps({'summary':summary,'channel_groups':dict(groups)},indent=2,ensure_ascii=False)}
```

```jsonl
'''
text+='\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in objects)+'\n```\n\n## Archive source-member recovery mappings\n\n```jsonl\n'
text+='\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in members)+'\n```\n';text+='\n## Exact duplicate pilot aliases (no new upload)\n\n```json\n'+json.dumps(aliases,indent=2,ensure_ascii=False)+'\n```\n'
latest=read(sorted(R.glob('batch-*/RECEIPT.json'))[-1])['postflight'];last_batch=batch_reports[-1]['batch'];text=text.replace('batches1–12',f'batches1–{last_batch}').replace('Batches10–12',f'Batches10–{last_batch}').replace('Three are compressed evidence archives',f'{len(packages)} are compressed evidence archives');text=text.replace('Latest limits32% five-hour,31% weekly',f"Latest recorded limits{latest['five_hour_used']}% five-hour,{latest['weekly_used']}% weekly");text=text.replace('Fresh owner Google One UI after Batch12:2.92GB of15GB used; approximately12.08GB available (rounded UI, not exact API bytes). Drive2.62GB; Gmail302.23MB.',f"Latest recorded owner quota observation: {latest['storage_ui']} at {latest['observed_at']}; rounded provider UI, not exact API bytes.");text=text.replace('Conservative next-batch free-space observation11.98GB',f"Conservative recorded free-space lower bound {latest['conservative_free_bytes']:,} bytes");text=text.replace('ORDERED_PLAN_V4.json','newest ORDERED_PLAN_V*.json (V5 or later)');text=text.replace('Machine B full runtime recovery and writer acceptance have', 'A fourth Finance handoff companion package, when present in the inventory, covers252 external research/publication files for NICK166–170, with10 machine/account-resource/secret-scan files intentionally excluded. It is declared source scope, not a full directory mirror. Machine B full runtime recovery and writer acceptance have');
local_index=R/'SELECTED_PACKAGE_GROUP_INDEX_20261026.json'
if local_index.exists():
 pending=read(local_index);text+='\n## Prepared remaining selected scope — not yet cloud verified unless mapped above\n\n'+f"The previously selected3527 B/C original paths are represented by53 bounded archives (3524 actual members and3 proven pilot aliases), totaling1,282,800,729 compressed bytes versus4,934,692,936 raw source bytes. Local creation/readback is not cloud backup. Only objects in the VERIFIED inventory above are claimed cloud recovered. Exact source member manifests remain with each pending package and the newest immutable ordered plan; all existing originals/prototypes are retained.\n"
import shutil
text=text.replace('Mac df available19,018,772KiB (about18.14GiB).',f'Mac free bytes at this handoff generation: {shutil.disk_usage(str(R)).free:,}.')
text=text.replace('The 30-minute heartbeat automation','The five-minute opportunistic heartbeat automation')
text=text.replace('newest ORDERED_PLAN_V*.json (V5 or later)','newest numbered ORDERED_PLAN_V*.json (currently V7)')
text+='\n## Current transfer and preservation qualification\n\nBatch16 and later use the qualified owner-authenticated standard browser multi-file chooser into one fresh private bounded child namespace per batch. Exact selected basenames are unique, returned remote IDs are grounded by live direct namespace listing and independent owner/private/parent/size metadata. Upload phase ends before fresh authenticated complete raw reads and SHA-256 verification. No directory upload or raw staging copy. Per-batch DESTINATION.json is authoritative; do not assume a flat bulk folder. Existing mappings are immutable.\n\nHeartbeat execution is opportunistic and requires this Mac, Codex and network availability; five-minute cadence is configured, not a guaranteed wall-clock start. Natural usage reset only; no credits redeemed or paid. Protected Claude writer and Machine B production ownership remain untouched. The prior canonical branch/HEAD observations below are historical, not a new repository audit. App-managed refs/codex/turn-diffs capture-key changes were separately recorded at checkpoint-20261026T084937Z; all observed referenced object hashes were unchanged. No production Git mutation was performed by this preservation chat.\n'
text+='\n## Current owner writer policy and selected media coverage\n\nThe current owner-provided AGENTS.md names Machine B as the sole Finance/expansion and channel-metadata writer. Machine A preservation remains read-only toward production. Claude session873b9a27-ba03-4183-aa61-f82d01f65998 remains the designated sole writer on research/casually-finance-editing-forensics; this preservation chat has not interrupted, retired or taken over that writer. Historical published ownership notes above are snapshots, not a grant to Machine A to write. Named Machine B operational acceptance, runtime installation and independent-machine disaster recovery remain unverified. No Finance/Visual review completion status was changed.\n\n'
for channel,expected_count,expected_bytes in [('PrimateEconomics-MP4 (source-folder provenance)',29,504214667),('PrimitiveEducation-MP4 (source-folder provenance)',45,203774483),('casual_economics (source-folder provenance)',11,659321738),('xkcd Channel (source-folder provenance)',88,557421212)]:
 g=groups.get(channel)
 if g and g['mapped_paths']==expected_count and g['logical_bytes_at_paths']==expected_bytes:text+=f'{channel}: all{expected_count}selected source paths, {expected_bytes:,}bytes, have VERIFIED recovery mappings. '
text+='These are the explicitly selected local inputs, not all public-channel videos or completed analysis. WHATIF source audio is classified by its actual source root; it does not establish a complete forensic package.\n\nBatch24 original20-row candidate manifest was retained unchanged. Immutable SELECTION.json finalized15unique-basename files before upload; omitted five candidates remain pending. The browser operation was interrupted after8objects. All8were independently retrieved/hash-verified before only7absent objects were resumed into the same original private namespace; no repeated upload. Both upload phases ended before their respective independent reads; all15source files passed exact byte/SHA checks. Future preparation stops before repeated basenames without source or remote renames. The external helper change and original pre-change helper are preserved alongside receipts.\n'
text=text.replace('omitted five candidates remain pending.', 'omitted five candidates were subsequently verified in Batches25–29; original receipts remain unchanged.')
text=text.replace('Current preserved canonical checkout remains', 'Historically observed canonical checkout was')
text=text.replace('Covered original paths including archive members:', 'Source-path representation sum including archive members (not deduplicated original-file count):')
text+='\n## Batch29 coverage and bounded read recovery\n\nAll23 selected direct WHATIF source paths,272,801,402 bytes, are now verified, including the original selected videos and audio. This excludes53 still-local forensic/editing packages and is not whole-channel or independent-machine recovery. Batch29 added20 objects/186,625,515 bytes. Seq477 first full read timed out after6,291,456 bytes; a bounded fresh authenticated retry retrieved all11,798,080 bytes with matching SHA-256. Partial read bytes are excluded from verified unique payload totals; no re-upload occurred. The helper resume accepts either nested-folder or direct validated metadata DESTINATION receipts; original receipts and previous helper remain preserved.\n'
p=D/('YIOS_MACHINE_B_HANDOFF_'+now+'.md');p.write_text(text);p.chmod(0o400)
print(json.dumps({'checkpoint_dir':str(D),'handoff_path':str(p),'handoff_bytes':p.stat().st_size,'handoff_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'summary':summary}))
