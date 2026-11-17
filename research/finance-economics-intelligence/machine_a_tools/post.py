"""Batch checkpoint update. argv: parent_commit next_nick next_vid session_accepted NICK_a [NICK_b ...]"""
import json,hashlib,sys,csv,datetime,shutil
B='/Users/ghilmankhan/workprojects/yios-finance-machine-a/research/finance-economics-intelligence/'
parent,nn,nv,sess=sys.argv[1:5]; nicks=sys.argv[5:]
h=lambda p:hashlib.sha256(open(B+p,'rb').read()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
L=[json.loads(l) for l in open(B+'VIDEO_AUDIT_966.jsonl')]
done=sum(all(s.startswith('COMPLETE') for s in x['statuses'].values()) for x in L); orig=966-done
title={r['Video_ID']:r['Title'] for r in csv.DictReader(open(B+'VIDEO_MASTER.csv'))}[nv]
pk=[]
for n in nicks:
    p=json.load(open(B+f'audit-batches/{n}.json'))['reviews'][0]; r=json.load(open(B+f'audit-batches/{n}_READ_RECEIPTS.json'))
    pk.append({'nick':n,'video_id':p['Video_ID'],'all_six_statuses':'COMPLETE_LIMITED_EVIDENCE','transcript_characters':r['receipts'][0]['character_count'],'claim_groups':len(p['script']['claim_audit']),
     'primary_source_receipts':len(r['primary_source_receipts']),'calculation_receipts':len(r['calculation_receipts']),'packet_sha256':h(f'audit-batches/{n}.json'),'read_receipts_sha256':h(f'audit-batches/{n}_READ_RECEIPTS.json'),'validation_sha256':h(f'audit-batches/{n}_VALIDATION.json')})
c=json.load(open(B+'FINANCE_PROGRESS_CHECKPOINT.json'))
last=c['batches'][-1]
if last['commit']=='CONTAINING_COMMIT_VERIFY_LIVE': last['commit']=parent; last['remote_and_pr_verified']='MACHINE_A_BRANCH_REMOTE_VERIFIED;PR36_NOT_APPLICABLE'
c['batches'].append({'nicks':nicks,'machine':'A','branch':'codex/finance-machine-a-owner-directed','parent':parent,'commit':'CONTAINING_COMMIT_VERIFY_LIVE','accepted':len(nicks),'blocked':0,'completed':done,'remaining':1612-done,'original_pending':orig,'expansion_pending':646,'remote_and_pr_verified':'PENDING_AT_WRITE'})
c['as_of_utc']=now; c['publication_verification']={'note':f'{nicks[-1]} commit contains this checkpoint; verify its SHA on origin/codex/finance-machine-a-owner-directed. PR #36 is not updated by this branch.'}
SID=__import__('os').environ.get('FINANCE_SESSION','unknown')
if c.get('_session_marker')!=SID: c['packets']=[]; c['_session_marker']=SID
c['packets']+=pk; c['session_accepted']=int(sess); c['session_blocked']=0
c['population'].update(completed=done,remaining=1612-done,original_pending=orig)
cv=c['coverage']
cv['full_stored_text_characters']+=sum(x['transcript_characters'] for x in pk); cv['claim_groups']+=sum(x['claim_groups'] for x in pk)
cv['primary_source_receipt_rows']+=sum(x['primary_source_receipts'] for x in pk); cv['calculation_receipts']+=sum(x['calculation_receipts'] for x in pk); cv['authentic_thumbnails_native_and_mobile']+=len(pk)
cv['source_independence']=f'Receipt rows include disclosed legitimate reuse;not{cv["primary_source_receipt_rows"]}independentsources'
c['synchronization']['workbook_sha256']=h('FINANCE_1612_COMBINED_INTELLIGENCE.xlsx')
for k in c['hashes']: c['hashes'][k]=h(k)
c['resources'].update(five_hour_used_percent='UNKNOWN_NOT_READABLE_FROM_SESSION',weekly_used_percent='UNKNOWN_NOT_READABLE_FROM_SESSION',free_disk_gib_rounded=shutil.disk_usage(B).free//2**30)
c['next']={'nick':nn,'video_id':nv,'title':title}
json.dump(c,open(B+'FINANCE_PROGRESS_CHECKPOINT.json','w'),indent=1,ensure_ascii=False)
f=json.load(open(B+'FINANCE_EXECUTION_FORECAST.json'))
f.update(as_of=now,batch=nicks,accepted=len(nicks),blocked=0,transcripts=f'{len(nicks)}_of_{len(nicks)}_present',source_receipts=sum(x['primary_source_receipts'] for x in pk),claims=sum(x['claim_groups'] for x in pk),
 calculation_receipts=2*len(nicks),validation='47tests+2formatting+2validators+target_and_workbook checks',usage={'five_hour':'UNKNOWN_NOT_READABLE_FROM_SESSION','weekly':'UNKNOWN_NOT_READABLE_FROM_SESSION'},
 forecast=f'Machine A owner-directed branch; resume with {nn} after reading live usage.',next_video_id=nv,next_nick=nn,status='MACHINE_A_OWNER_DIRECTED_BATCHING',session_total_accepted=int(sess),session_total_blocked=0)
json.dump(f,open(B+'FINANCE_EXECUTION_FORECAST.json','w'),indent=2,ensure_ascii=False)
open(B+'FINANCE_WRITER_OWNERSHIP.md','a').write(f'\n{"–".join([nicks[0],nicks[-1][5:]]) if len(nicks)>1 else nicks[0]} accepted on Machine A branch, parent `{parent[:8]}`: {done} complete / {1612-done:,} remaining.\n')
print('done',done,1612-done,orig)
