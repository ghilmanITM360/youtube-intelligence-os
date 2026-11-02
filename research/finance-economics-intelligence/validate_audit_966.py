"""Validate full-population identity, evidence preservation and completion honesty."""
import hashlib
import json
import sqlite3
import zipfile
from collections import Counter
from build_audit_966 import BASE, ROOT, DIMENSIONS, STATUSES, read

COMPLETE={'COMPLETE_EVIDENCE_BACKED','COMPLETE_LIMITED_EVIDENCE'}

def reference_gate_errors():
    """Framework gate (structural only): every accepted NICK_281+ batch needs a validating reference comparison; every ledger reanalysis file must validate."""
    import sys
    sys.path.insert(0,str(BASE/'reference-framework'))
    import reference_comparison
    return ['reference gate: '+m for m in reference_comparison.check_coverage()]

def identity_errors(baseline, actual):
    errors=[]
    if len(actual)!=len(set(actual)): errors.append('duplicate IDs')
    if set(baseline)!=set(actual): errors.append('missing or substituted IDs')
    return errors

def projection_errors(source, display):
    by_id={r['Video_ID']:r for r in display}
    errors=[]
    for r in source:
        actual=by_id.get(r['Video_ID'],{})
        for dimension,status in r['statuses'].items():
            if actual.get(dimension)!=status: errors.append('matrix status mismatch '+r['Video_ID']+':'+dimension)
    return errors

def image_errors(vid, image):
    errors=[]
    if image.get('image_path'):
        path=ROOT/image['image_path']
        if vid not in path.name or '/'+vid+'/' not in image.get('image_source',''):
            errors.append('image association '+vid)
        if not path.is_file(): errors.append('image absent '+vid)
        elif hashlib.sha256(path.read_bytes()).hexdigest()!=image.get('image_sha256'):
            errors.append('image drift '+vid)
    return errors

def reference_errors(refs):
    errors=[]
    for ref in refs:
        filename, _, key=ref.partition(':')
        path=ROOT/filename if (ROOT/filename).exists() else BASE/filename
        if not path.is_file():
            errors.append('missing reference '+ref)
        elif key and path.suffix=='.csv':
            import csv
            with path.open(newline='') as f:
                rows=list(csv.DictReader(f))
            if not any(r.get('Video_ID')==key for r in rows): errors.append('missing reference ID '+ref)
    return errors

REQUIRED={
    'TITLE_REVIEW':['analysis','peer_comparison_ids','search_demand'],
    'THUMBNAIL_REVIEW':['analysis','image_path','image_source','image_sha256','dimensions','mobile_review_width'],
    'SCRIPT_REVIEW':['analysis','beat_map','claim_audit','opening_words','ending_words','timing','source'],
    'TOPIC_REVIEW':['analysis','novelty_and_corpus_angle','competition'],
    'VIRALITY_REVIEW':['analysis','observed_result','topic_demand','trend_timing','competition','format_fit','channel_context','alternative_explanations','original_content_lesson','causal_status']}
SCOPES={'TITLE_REVIEW':'ACTUAL_TITLE','THUMBNAIL_REVIEW':'ACTUAL_IMAGE','SCRIPT_REVIEW':'FULL_STORED_TEXT','TOPIC_REVIEW':'FULL_TRANSCRIPT_TOPIC','VIRALITY_REVIEW':'INDIVIDUAL_PUBLIC_EVIDENCE'}

def contiguous_range_errors(ranges, length):
    errors=[]
    if not isinstance(ranges, list) or not ranges:
        return ['missing read ranges']
    cursor=0
    for item in ranges:
        if not isinstance(item, list) or len(item)!=2 or not all(isinstance(v,int) for v in item):
            return ['invalid read ranges']
        start,end=item
        if start!=cursor or end<=start or end>length:
            errors.append('noncontiguous read ranges')
            break
        cursor=end
    if cursor!=length: errors.append('incomplete read ranges')
    return errors

def strict_receipt_required(batch_id):
    if not batch_id.startswith('NICK_'): return False
    try: return int(batch_id.split('_',1)[1]) >= 156
    except ValueError: return False

def strict_receipt_errors(row, transcript_text, master_by_id):
    """Enforce the current receipt standard without inventing evidence for older batches."""
    vid=row['Video_ID']; batch=row['batch_id']; errors=[]
    path=BASE/'audit-batches'/f'{batch}_READ_RECEIPTS.json'
    if not path.is_file(): return ['missing strict receipt '+vid]
    doc=json.loads(path.read_text())
    receipts=[r for r in doc.get('receipts',[]) if r.get('Video_ID')==vid]
    if len(receipts)!=1: return ['strict receipt cardinality '+vid]
    receipt=receipts[0]; raw=transcript_text.encode()
    expected_hash=hashlib.sha256(raw).hexdigest()
    checks={
        'scope': 'FULL_STORED_TEXT',
        'Text_SHA256': expected_hash,
        'character_count': len(transcript_text),
        'canonical_utf8_bytes': len(raw),
    }
    for key,expected in checks.items():
        if receipt.get(key)!=expected: errors.append(f'strict receipt {key} {vid}')
    if not isinstance(receipt.get('audio_verified'),bool): errors.append('strict receipt audio status '+vid)
    errors += [e+' '+vid for e in contiguous_range_errors(receipt.get('read_character_ranges'),len(transcript_text))]
    normalized=' '.join(transcript_text.split())
    if not receipt.get('first_text_witness') or not normalized.startswith(receipt['first_text_witness']): errors.append('first witness '+vid)
    if not receipt.get('last_text_witness') or not normalized.endswith(receipt['last_text_witness']): errors.append('last witness '+vid)
    locator=row['script']['source'].get('Evidence_locator','')
    archive_name,sep,member=locator.partition('::')
    if not sep or member!=receipt.get('archive_member'): errors.append('archive locator '+vid)
    else:
        archive=ROOT/archive_name
        try:
            with zipfile.ZipFile(archive) as zf: archive_bytes=zf.read(member)
        except (FileNotFoundError,KeyError,zipfile.BadZipFile):
            errors.append('archive member unavailable '+vid)
        else:
            if hashlib.sha256(archive_bytes).hexdigest()!=receipt.get('archive_member_sha256'): errors.append('archive hash '+vid)
            if len(archive_bytes)!=receipt.get('archive_member_bytes'): errors.append('archive bytes '+vid)
            if len(archive_bytes.splitlines())!=receipt.get('archive_member_lines'): errors.append('archive lines '+vid)
    image_path=ROOT/row['thumbnail'].get('image_path','')
    if not image_path.is_file(): errors.append('strict image absent '+vid)
    else:
        image_bytes=image_path.read_bytes()
        if hashlib.sha256(image_bytes).hexdigest()!=receipt.get('image_sha256'): errors.append('strict image hash '+vid)
        if len(image_bytes)!=receipt.get('image_bytes'): errors.append('strict image bytes '+vid)
    sizes=receipt.get('image_inspected_sizes',[])
    if row['thumbnail'].get('dimensions') not in sizes or [row['thumbnail'].get('mobile_review_width'),180] not in sizes:
        errors.append('native/mobile inspection sizes '+vid)
    if not doc.get('primary_source_receipts'): errors.append('missing primary source receipts '+vid)
    if not doc.get('calculation_receipts'): errors.append('missing calculation receipts '+vid)
    perf=[r for r in doc.get('calculation_receipts',[]) if str(r.get('method','')).startswith('Frozen lifetime-view-rate')]
    if len(perf)!=1: errors.append('performance calculation receipt '+vid)
    else:
        results=perf[0].get('results',{}); master=master_by_id[vid]
        peers=master['Peer_Video_IDs'].split('|') if master['Peer_Video_IDs'] else []
        if results.get('peer_ids_10')!=peers or results.get('peer_ids_5')!=peers[:5]: errors.append('peer cohort receipt '+vid)
        if results.get('tier_10')!=master['Performance_tier']: errors.append('ten-peer tier receipt '+vid)
        if abs(float(results.get('peer_ratio_10',-1))-float(master['Lifetime_rate_ratio']))>0.00001: errors.append('ten-peer ratio receipt '+vid)
    if receipt.get('audio_verified') is False and 'audio, timed delivery and editing unverified' not in row['script'].get('stored_text_completeness',''):
        errors.append('audiovisual limitation '+vid)
    if row['virality'].get('causal_status')!='DESCRIPTIVE_ASSOCIATION_NOT_CAUSAL': errors.append('causal boundary '+vid)
    return errors

def semantic_errors(row):
    errors=[]
    for d,status in row['statuses'].items():
        if status not in STATUSES: errors.append('invalid status '+d)
        if status not in COMPLETE or d=='PERFORMANCE_REVIEW': continue
        section=row.get(d.removesuffix('_REVIEW').lower(),{})
        if section.get('review_scope') != SCOPES.get(d):
            errors.append('no semantic scope '+d)
        if not section.get('source_refs'): errors.append('no source references '+d)
        if not section.get('analysis'): errors.append('no individual analysis '+d)
        for field in REQUIRED.get(d,[]):
            if not section.get(field): errors.append('missing rubric '+d+':'+field)
        if d=='SCRIPT_REVIEW':
            if not section.get('source',{}).get('Text_SHA256'): errors.append('missing transcript hash')
            if section.get('timing')!='OPENING_WORDS_ONLY': errors.append('unsupported timing')
        if d=='THUMBNAIL_REVIEW':
            if not all(section.get(k) for k in ['image_path','image_sha256','dimensions','image_source']): errors.append('missing image receipt')
    return errors

def validate():
    frozen=json.loads((BASE/'audit-baseline/MANIFEST.json').read_text())
    ids=read('audit-baseline/VIDEO_IDS.csv'); master=read('VIDEO_MASTER.csv')
    rows=[json.loads(s) for s in (BASE/'VIDEO_AUDIT_966.jsonl').read_text().splitlines()]
    master_by_id={r['Video_ID']:r for r in master}
    errors=[]
    assert len(ids)==len({r['Video_ID'] for r in ids})==966
    errors+=identity_errors([r['Video_ID'] for r in ids],[r['Video_ID'] for r in rows])
    assert hashlib.sha256((BASE/'audit-baseline/VIDEO_MASTER.csv').read_bytes()).hexdigest()==frozen['frozen_master_sha256']
    for path,expected in frozen['source_hashes'].items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=expected: errors.append('source drift '+path)
    channel={r['Video_ID']:r['Channel_ID'] for r in ids}
    con=sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro',uri=True)
    for r in rows:
        vid=r['Video_ID'];errors += [vid+': '+e for e in semantic_errors(r)]
        if r['Channel_ID']!=channel.get(vid): errors.append('channel mismatch '+vid)
        if set(r['statuses'])!={d+'_REVIEW' for d in DIMENSIONS}: errors.append('status dimensions '+vid)
        source=r['script']['source']; digest=source.get('Text_SHA256')
        if digest:
            text=con.execute('select transcript_text from transcripts where youtube_video_id=?',(vid,)).fetchone()[0]
            if hashlib.sha256(text.encode()).hexdigest()!=digest: errors.append('transcript drift '+vid)
            if strict_receipt_required(r['batch_id']): errors += strict_receipt_errors(r,text,master_by_id)
        errors+=image_errors(vid,r['thumbnail'])
        for section in ['title','thumbnail','script','topic','virality']:
            errors+=reference_errors(r[section].get('source_refs',[]))
        if not r['performance'].get('methodology'): errors.append('performance method '+vid)
    for name in ['VIDEO_AUDIT_966','VIDEO_COMPLETION_MATRIX','THUMBNAIL_ANALYSIS_966','SCRIPT_ANALYSIS_966','TITLE_ANALYSIS_966','TOPIC_ANALYSIS_966','VIRALITY_INTELLIGENCE_966']:
        errors+=identity_errors([r['Video_ID'] for r in ids],[r['Video_ID'] for r in read(name+'.csv')])
    errors+=projection_errors(rows,read('VIDEO_COMPLETION_MATRIX.csv'))
    errors+=projection_errors(rows,read('VIDEO_AUDIT_966.csv'))
    for dimension in ['THUMBNAIL','SCRIPT','TITLE','TOPIC','VIRALITY']:
        display={r['Video_ID']:r for r in read(dimension+'_ANALYSIS_966.csv' if dimension!='VIRALITY' else 'VIRALITY_INTELLIGENCE_966.csv')}
        for r in rows:
            cell=display.get(r['Video_ID'],{})
            if cell.get('Status')!=r['statuses'][dimension+'_REVIEW']: errors.append('component CSV status mismatch '+r['Video_ID'])
            if cell.get('analysis','')!=r[dimension.lower()].get('analysis',''): errors.append('component CSV analysis mismatch '+r['Video_ID'])
    sources=json.loads((BASE/'audit-batches/EVENT_SOURCES.json').read_text())
    source_ids={r['id'] for r in sources['sources']}
    for row in rows:
        if set(row['event'].get('source_ids',[]))-source_ids: errors.append('unknown event source '+row['Video_ID'])
    expanded=sum(all(s in COMPLETE for s in row['statuses'].values()) for row in rows)
    full_evidence=sum(all(s=='COMPLETE_EVIDENCE_BACKED' for s in row['statuses'].values()) for row in rows)
    readings={'titles':sum(bool(r['title'].get('analysis') or r['title'].get('legacy_review')) for r in rows),
              'thumbnails':sum(bool(r['thumbnail'].get('analysis') or r['thumbnail'].get('legacy_review')) for r in rows),
              'topics':sum(bool(r['topic'].get('analysis') or r['topic'].get('legacy_review')) for r in rows)}
    errors+=reference_gate_errors()
    batches=[]
    for path in sorted((BASE/'audit-batches').glob('*.json')):
        batch=json.loads(path.read_text())
        if batch.get('reviews'): batches.append({'batch_id':batch['batch_id'],'status':batch.get('status','UNDECLARED'),'registered_reviews':len(batch['reviews'])})
    coverage={d:dict(Counter(r['statuses'][d+'_REVIEW'] for r in rows)) for d in DIMENSIONS}
    outstanding=[r['Video_ID'] for r in rows if any(s in {'NOT_STARTED','IN_PROGRESS'} for s in r['statuses'].values())]
    report={'validation':'PASS' if not errors else 'FAIL','research_status':'FULL_POPULATION_RESEARCH_IN_PROGRESS' if outstanding else 'ALL_966_COVERED_WITH_EVIDENCE_GAPS','registered':len(rows),'fully_analyzed_complete_evidence':full_evidence,'analyzed_partial_evidence':expanded-full_evidence,'source_blocked_videos':sum(any(s=='BLOCKED_MISSING_SOURCE' for s in r['statuses'].values()) for r in rows),'coverage':coverage,'distinct_readings_including_legacy_and_in_progress':readings,'batches':batches,'distinct_full_stored_text_reads':sum(r['script'].get('review_scope')=='FULL_STORED_TEXT' for r in rows),'outstanding_videos':len(outstanding),'next_master_order_id':outstanding[0] if outstanding else None,'source_hashes_checked':len(frozen['source_hashes']),'errors':errors,'reference_framework_gate':'STRUCTURAL_ONLY_check_coverage','semantic_content_validation':'STRUCTURAL_ONLY; analyst reasoning and source entailment require review','causal_inference':'Public metadata cannot establish causation; private metrics unavailable','exact_head_ci':'CHECK_PR_36_AFTER_PUSH'}
    (BASE/'VALIDATION_966.json').write_text(json.dumps(report,indent=2)+'\n')
    assert not errors, errors
    print(json.dumps(report,indent=2))
    return report

if __name__=='__main__':validate()
