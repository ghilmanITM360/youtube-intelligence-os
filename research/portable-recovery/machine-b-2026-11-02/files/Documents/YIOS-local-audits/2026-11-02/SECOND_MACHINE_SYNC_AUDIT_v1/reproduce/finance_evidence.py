from audit import *
from data_audit import tree,blob,F
import sqlite3,re
def main():
 claims=[];sources=[];calcs=[];receipts=[];summaries=[];cache={}
 con=sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro',uri=True)
 texts={r[0]:r[1] for r in con.execute('SELECT youtube_video_id,transcript_text FROM transcripts')};con.close()
 for ref,label in [('origin/research/finance-economics-intelligence','canonical'),('origin/codex/finance-machine-a-owner-directed','machine-a-published')]:
  rows=[json.loads(l) for l in git('show',ref+':'+F+'VIDEO_AUDIT_966.jsonl').splitlines()];counts=Counter();witness=Counter()
  for row in rows:
   ca=row['script'].get('claim_audit')
   if not isinstance(ca,list):counts['narrative_claim_audit_videos']+=bool(ca);continue
   counts['structured_claim_audit_videos']+=1
   for c in ca:
    if not isinstance(c,dict):continue
    counts['structured_claim_rows']+=1;start=c.get('start_char');end=c.get('end_char');txt=c.get('stored_text_witness');status='NO_EXACT_RANGE_FIELDS'
    if isinstance(start,int) and isinstance(end,int) and isinstance(txt,str):
     status='MATCH' if texts.get(row['Video_ID'],'')[start:end]==txt else 'MISMATCH';witness[status]+=1
    assessment=c.get('assessment','');labels=re.findall(r'\[([A-Z_]+)\]',assessment)
    claims.append({'scope':label,'ref':ref,'video_id':row['Video_ID'],'batch_id':row['batch_id'],'claim_id':c.get('claim_id'),'claim':c.get('claim'),'assessment':assessment,'declared_source_confidence_labels':labels,'source_ids':c.get('source_ids'),'evidence_kind':c.get('evidence_kind'),'transcript_range_witness_check':status,'start_char':start,'end_char':end,'limitations':'Witness match proves quoted stored ASR span, not truth or primary-source entailment.'})
  for t in tree(ref):
   if not t['path'].startswith(F+'audit-batches/') or not t['path'].endswith('_READ_RECEIPTS.json'):continue
   if t['blob'] not in cache:cache[t['blob']]=json.loads(blob(t['blob']))
   d=cache[t['blob']]
   for r in d.get('receipts',[]):receipts.append({'scope':label,'path':t['path'],'batch_id':d.get('batch_id'),'video_id':r.get('Video_ID'),'scope_declared':r.get('scope'),'text_sha256':r.get('Text_SHA256'),'character_count':r.get('character_count'),'range_count':len(r.get('read_character_ranges',[])),'archive_path':r.get('archive_path') or r.get('archive'),'archive_member':r.get('archive_member')})
   for r in d.get('primary_source_receipts',[]):
    paths={k:v for k,v in r.items() if isinstance(v,str) and any(x in k.lower() for x in ['path','file'])}
    sources.append({'scope':label,'path':t['path'],'source_id':r.get('source_id'),'url':r.get('url'),'source_date':r.get('source_date'),'accessed':r.get('accessed'),'access_scope':r.get('access_scope'),'source_confidence':r.get('source_confidence','LEGACY_UNLABELLED_READ_ACCESS_SCOPE'),'locator':r.get('locator'),'finding':r.get('finding'),'limitations':r.get('limitations'),'publication_applicability':r.get('publication_applicability'),'explicit_file_paths':paths,'local_file_presence':{k:Path(v).exists() if v.startswith('/') else (ROOT/v).exists() for k,v in paths.items()},'authority':'PUBLISHED_ANALYST_RECEIPT_NOT_FRESH_PRIMARY_SOURCE_REVERIFICATION'})
   for r in d.get('calculation_receipts',[]):calcs.append({'scope':label,'path':t['path'],'receipt':r,'authority':'PUBLISHED_CALCULATION_RECEIPT; formulas not eval-executed during repository audit'})
  counts['primary_source_receipts']=sum(r['scope']==label for r in sources);counts['calculation_receipts']=sum(r['scope']==label for r in calcs);summaries.append({'scope':label,'counts':dict(counts),'structured_claim_witness_checks':dict(witness),'source_confidence_counts':dict(Counter(r['source_confidence'] for r in sources if r['scope']==label))})
 csvout('finance/claims.csv',claims);csvout('finance/primary_source_receipts.csv',sources);csvout('finance/calculation_receipts.csv',calcs);csvout('finance/transcript_read_receipts.csv',receipts);write('finance/evidence_counts.json',summaries)
 print(json.dumps(summaries,indent=2))
if __name__=='__main__':main()
