"""Validate full-population identity, evidence preservation and completion honesty."""
import hashlib
import json
import sqlite3
from collections import Counter
from build_audit_966 import BASE, ROOT, DIMENSIONS, STATUSES, read

COMPLETE={'COMPLETE_EVIDENCE_BACKED','COMPLETE_LIMITED_EVIDENCE'}

def identity_errors(baseline, actual):
    errors=[]
    if len(actual)!=len(set(actual)): errors.append('duplicate IDs')
    if set(baseline)!=set(actual): errors.append('missing or substituted IDs')
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

def semantic_errors(row):
    errors=[]
    for d,status in row['statuses'].items():
        if status not in STATUSES: errors.append('invalid status '+d)
        if status not in COMPLETE or d=='PERFORMANCE_REVIEW': continue
        section=row.get(d.removesuffix('_REVIEW').lower(),{})
        if section.get('review_scope') not in {'FULL_STORED_TEXT','ACTUAL_TITLE','ACTUAL_IMAGE','FULL_TRANSCRIPT_TOPIC','INDIVIDUAL_PUBLIC_EVIDENCE'}:
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
        errors+=image_errors(vid,r['thumbnail'])
        for section in ['title','thumbnail','script','topic','virality']:
            errors+=reference_errors(r[section].get('source_refs',[]))
        if not r['performance'].get('methodology'): errors.append('performance method '+vid)
    for name in ['VIDEO_AUDIT_966','VIDEO_COMPLETION_MATRIX','THUMBNAIL_ANALYSIS_966','SCRIPT_ANALYSIS_966','TITLE_ANALYSIS_966','TOPIC_ANALYSIS_966','VIRALITY_INTELLIGENCE_966']:
        errors+=identity_errors([r['Video_ID'] for r in ids],[r['Video_ID'] for r in read(name+'.csv')])
    sources=json.loads((BASE/'audit-batches/EVENT_SOURCES.json').read_text())
    source_ids={r['id'] for r in sources['sources']}
    for row in rows:
        if set(row['event'].get('source_ids',[]))-source_ids: errors.append('unknown event source '+row['Video_ID'])
    expanded=sum(all(s in COMPLETE for s in row['statuses'].values()) for row in rows)
    full_evidence=sum(all(s=='COMPLETE_EVIDENCE_BACKED' for s in row['statuses'].values()) for row in rows)
    coverage={d:dict(Counter(r['statuses'][d+'_REVIEW'] for r in rows)) for d in DIMENSIONS}
    outstanding=[r['Video_ID'] for r in rows if any(s in {'NOT_STARTED','IN_PROGRESS'} for s in r['statuses'].values())]
    report={'validation':'PASS' if not errors else 'FAIL','research_status':'FULL_POPULATION_RESEARCH_IN_PROGRESS' if outstanding else 'ALL_966_COVERED_WITH_EVIDENCE_GAPS','registered':len(rows),'fully_analyzed_complete_evidence':full_evidence,'analyzed_partial_evidence':expanded-full_evidence,'source_blocked_videos':sum(any(s=='BLOCKED_MISSING_SOURCE' for s in r['statuses'].values()) for r in rows),'coverage':coverage,'distinct_full_stored_text_reads':sum(r['script'].get('review_scope')=='FULL_STORED_TEXT' for r in rows),'outstanding_videos':len(outstanding),'next_master_order_id':outstanding[0] if outstanding else None,'source_hashes_checked':len(frozen['source_hashes']),'errors':errors,'semantic_content_validation':'STRUCTURAL_ONLY; analyst reasoning and source entailment require review','causal_inference':'Public metadata cannot establish causation; private metrics unavailable','exact_head_ci':'CHECK_PR_36_AFTER_PUSH'}
    (BASE/'VALIDATION_966.json').write_text(json.dumps(report,indent=2)+'\n')
    assert not errors, errors
    print(json.dumps(report,indent=2))
    return report

if __name__=='__main__':validate()
