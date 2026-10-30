"""Research ledger only. Never generate semantic findings from lexical features."""
import csv
import hashlib
import json
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
DIMENSIONS = ('TITLE', 'THUMBNAIL', 'SCRIPT', 'TOPIC', 'PERFORMANCE', 'VIRALITY')
STATUSES = {'COMPLETE_EVIDENCE_BACKED', 'COMPLETE_LIMITED_EVIDENCE', 'IN_PROGRESS', 'BLOCKED_MISSING_SOURCE', 'NOT_STARTED'}

def read(name):
    with (BASE / name).open(newline='') as f:
        return list(csv.DictReader(f))

def index(name):
    rows = read(name)
    assert len(rows) == len({r['Video_ID'] for r in rows}), name
    return {r['Video_ID']: r for r in rows}

def initial_statuses(has_script):
    statuses = {d+'_REVIEW': 'NOT_STARTED' for d in DIMENSIONS}
    if not has_script:
        statuses['SCRIPT_REVIEW'] = 'BLOCKED_MISSING_SOURCE'
    return statuses

def csv_out(name, rows):
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with (BASE / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys, lineterminator='\n')
        w.writeheader()
        for r in rows:
            w.writerow({k: json.dumps(v, ensure_ascii=False, sort_keys=True) if isinstance(v, (dict,list)) or isinstance(v, str) and ('\n' in v or '\r' in v) else v for k,v in r.items()})

def batch_identity_errors(canonical_ids, batch_ids):
    return sorted(set(batch_ids)-set(canonical_ids))

def build():
    master = read('VIDEO_MASTER.csv')
    identities = read('audit-baseline/VIDEO_IDS.csv')
    assert len(master) == len({r['Video_ID'] for r in master}) == 966
    assert {(r['Video_ID'],r['Channel_ID']) for r in master} == {(r['Video_ID'],r['Channel_ID']) for r in identities}
    transcripts = index('TRANSCRIPT_COVERAGE.csv')
    thumbs = index('THUMBNAIL_COVERAGE.csv')
    semantic = index('SEMANTIC_REVIEWS.csv')
    titles = index('TITLE_SEMANTIC_REVIEWS.csv')
    visual = index('THUMBNAIL_REVIEWS.csv')
    maps = index('DEEP_SCRIPT_MAPS.csv')
    transcript_recovery = {r['Video_ID']:r for r in json.loads((BASE/'audit-batches/TRANSCRIPT_RECOVERY_001.json').read_text())['attempts']}
    thumbnail_recovery_path = BASE/'audit-batches/LEGACY_THUMBNAIL_RECOVERY_001.json'
    thumbnail_recovery = {r['Video_ID']:r for r in json.loads(thumbnail_recovery_path.read_text())['receipts']} if thumbnail_recovery_path.exists() else {}
    batches = {}
    for path in sorted((BASE/'audit-batches').glob('*.json')):
        batch = json.loads(path.read_text())
        for r in batch.get('reviews', []):  # validation/receipt companions carry no reviews
            assert r['Video_ID'] not in batches, 'Duplicate analyst batch ID'
            batches[r['Video_ID']] = (batch['batch_id'],r)
    assert not batch_identity_errors({r["Video_ID"] for r in master}, batches), "Unknown batch video"
    con = sqlite3.connect(f'file:{ROOT}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
    con.row_factory = sqlite3.Row
    result = []
    for v in master:
        vid = v['Video_ID']; t = transcripts[vid]; th = thumbs[vid]
        source = con.execute('SELECT likes, comments, description, description_unavailable_reason FROM videos WHERE youtube_video_id=?', (vid,)).fetchone()
        identity = {**v, **dict(source), 'Metadata_source':'data/catalog/youtube_channel_registry.db:videos:'+vid}
        statuses = initial_statuses(t['Status']=='TEXT_AVAILABLE')
        row = {'Video_ID':vid, 'Channel_ID':v['Channel_ID'], 'identity':identity,
               'statuses':statuses, 'title':{}, 'thumbnail':{'coverage':th},
               'script':{'source':t, 'review_scope':'NOT_REVIEWED'}, 'topic':{},
               'performance':{k:v[k] for k in ['Performance_tier','Peer_count','Lifetime_rate_ratio','Peer_Video_IDs','Tier_basis','Metric_snapshot_date','Format','Age_days']},
               'virality':{}, 'event':{'status':'NOT_RESEARCHED'},
               'private_metrics':{'CTR':'UNAVAILABLE_PRIVATE_METRIC','retention':'UNAVAILABLE_PRIVATE_METRIC','impressions':'UNAVAILABLE_PRIVATE_METRIC','revenue':'UNAVAILABLE_PRIVATE_METRIC','traffic_sources':'UNAVAILABLE_PRIVATE_METRIC'},
               'batch_id':'LEGACY_OR_PENDING'}
        row['script']['availability']='TEXT_AVAILABLE' if t['Status']=='TEXT_AVAILABLE' else 'TRANSCRIPT_UNAVAILABLE'
        if vid in transcript_recovery: row['script']['recovery_attempt']=transcript_recovery[vid]
        if vid in thumbnail_recovery: row['thumbnail']['recovery_attempt']=thumbnail_recovery[vid]
        # Existing reviews remain useful but do not satisfy the expanded rubric.
        statuses['PERFORMANCE_REVIEW'] = 'COMPLETE_LIMITED_EVIDENCE'
        row['performance']['methodology'] = 'METHODS.md; build_baseline.compare'
        row['performance']['evidence_kind'] = 'OBSERVED_FACT'
        if vid in titles:
            row['title']={'legacy_review':titles[vid], 'expanded_rubric':'PENDING'}
            statuses['TITLE_REVIEW']='IN_PROGRESS'
        if vid in semantic:
            s=semantic[vid];row['topic']={'legacy_review':s,'expanded_rubric':'PENDING'}
            statuses['TOPIC_REVIEW']='IN_PROGRESS'
            row['script'].update({'legacy_review':s,'review_scope':s['Review_scope']})
            if vid in maps: row['script']['legacy_beat_map']=maps[vid]
            statuses['SCRIPT_REVIEW']='IN_PROGRESS'
        if vid in visual:
            row['thumbnail']['legacy_review']=visual[vid]
            statuses['THUMBNAIL_REVIEW']='IN_PROGRESS'
        if vid in batches:
            batch_id, review=batches[vid]
            row['batch_id']=batch_id
            for section in ['title','thumbnail','script','topic','virality','event']:
                if section in review: row[section].update(review[section])
            statuses.update(review.get('statuses',{}))
        result.append(row)
    with (BASE/'VIDEO_AUDIT_966.jsonl').open('w') as f:
        for r in result: f.write(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n')
    csv_out('VIDEO_AUDIT_966.csv',[{**r['identity'], **r['statuses'], 'Batch':r['batch_id'], **{k:r[k] for k in ['title','thumbnail','script','topic','performance','virality','event','private_metrics']}} for r in result])
    csv_out('VIDEO_COMPLETION_MATRIX.csv',[{'Video_ID':r['Video_ID'],'Channel_ID':r['Channel_ID'],**r['statuses'],'Batch':r['batch_id']} for r in result])
    for section, name in [('title','TITLE_ANALYSIS_966'),('thumbnail','THUMBNAIL_ANALYSIS_966'),('script','SCRIPT_ANALYSIS_966'),('topic','TOPIC_ANALYSIS_966'),('virality','VIRALITY_INTELLIGENCE_966')]:
        csv_out(name+'.csv',[{'Video_ID':r['Video_ID'],'Channel_ID':r['Channel_ID'],'Channel':r['identity']['Channel'],'Title':r['identity']['Title'],'Views':r['identity']['Views'],'Performance_tier':r['performance']['Performance_tier'],'Metric_snapshot_date':r['performance']['Metric_snapshot_date'],'Status':r['statuses'][section.upper()+'_REVIEW'],**r[section]} for r in result])
    return result

if __name__=='__main__':
    print('Registered',len(build()),'audit records; semantic completion is evidence-gated.')
