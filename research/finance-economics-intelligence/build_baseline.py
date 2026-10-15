"""Read canonical evidence without mutation; emit deterministic research tables."""
import csv
import hashlib
import json
import re
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import median

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
DB = ROOT / 'data/catalog/youtube_channel_registry.db'
COLLECTED = {'DS-000020': '2026-09-12', 'DS-000021': '2026-09-12',
             'DS-000023': '2026-09-13', 'DS-000024': '2026-09-13'}


def read_csv(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f))


def write_csv(name, rows):
    with (BASE / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def date(value):
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00')).replace(tzinfo=timezone.utc)
    except (ValueError, TypeError, AttributeError):
        return None


def format_of(value):
    value = (value or '').lower()
    return 'SHORTS' if value in ('short', 'shorts') else 'LONG_FORM' if value in ('regular video', 'video') else 'UNKNOWN'


def compare(v, videos):
    """Nearest publication-age peers; lifetime rate is not current velocity."""
    if v['Age_days'] == '' or v['Age_days'] < 7 or v['Format'] == 'UNKNOWN' or v['Views'] is None:
        return ('INSUFFICIENT_DATA', '', '', '', 'MISSING_DATE_FORMAT_VIEWS_OR_YOUNG')
    peers = [p for p in videos if p['Video_ID'] != v['Video_ID']
             and p['Channel_ID'] == v['Channel_ID'] and p['Format'] == v['Format']
             and p['Metric_snapshot_date'] == v['Metric_snapshot_date']
             and p['Age_days'] != '' and p['Age_days'] >= 7 and p['Views'] is not None
             and 0.5 <= p['Age_days'] / v['Age_days'] <= 2]
    peers = sorted(peers, key=lambda p: (abs(p['Age_days'] - v['Age_days']), p['Video_ID']))[:10]
    if len(peers) < 5:
        return ('INSUFFICIENT_DATA', len(peers), '', '|'.join(p['Video_ID'] for p in peers), 'FEWER_THAN_FIVE_AGE_PEERS')
    baseline = median(p['Views'] / p['Age_days'] for p in peers)
    if baseline <= 0:
        return ('INSUFFICIENT_DATA', len(peers), '', '|'.join(p['Video_ID'] for p in peers), 'ZERO_BASELINE')
    ratio = v['Views'] / v['Age_days'] / baseline
    return ('STRONG' if ratio >= 2 else 'WEAK' if ratio < 0.5 else 'TYPICAL', len(peers), round(ratio, 5), '|'.join(p['Video_ID'] for p in peers), 'DESCRIPTIVE_LIFETIME_RATE')


TOPICS = [
 ('retirement', r'retir|pension|social security|401k|401\(k\)'),
 ('housing_mortgages', r'hous|mortgage|rent\b|real estate|homeowner|home buy'),
 ('debt_credit_banking', r'debt|credit|bank|loan|borrow'),
 ('investing', r'invest|stock|portfolio|dividend|index fund|etf|s&p|compound'),
 ('macro_policy', r'inflat|econom|recession|interest rate|central|federal reserve|tariff|gdp'),
 ('business_models', r'business|company|companies|tesla|byd|costco|profit'),
 ('personal_finance', r'money|wealth|rich|poor|paycheck|salary|saving|budget|spend|financial'),
 ('economic_history', r'crash|depression|history|1973|2008|1929'),
 ('geopolitics', r'china|japan|america|europe|war|country|countries')]


def main():
    before = hashlib.sha256(DB.read_bytes()).hexdigest()
    con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
    con.row_factory = sqlite3.Row
    inventory = read_csv(BASE / 'EXISTING_DATA_INVENTORY.csv')
    selected = [r for r in inventory if r['Scope'] == 'CANONICAL' and r['Niche'] != 'ADJACENT']
    channels, videos, transcripts, thumbs, features, title_features = [], [], [], [], [], []
    seen_hash = {}
    for ch in selected:
        cid = ch['Channel_ID']
        channel_videos = list(con.execute('SELECT * FROM videos WHERE canonical_channel_id=? ORDER BY youtube_video_id', (cid,)))
        channels.append({'Channel_ID': cid, 'Channel': ch['Channel'], 'Scope': 'CANONICAL_FINANCE',
                         'Dataset': ch['Dataset'], 'Videos': len(channel_videos), 'Niche': ch['Niche'],
                         'Research_depth': 'AUTOMATED_BASELINE', 'Current_growth': 'UNKNOWN'})
        for source in channel_videos:
            s = dict(source); vid = s['youtube_video_id']; title = s['title'] or ''
            ds = list(con.execute('SELECT * FROM dataset_videos WHERE youtube_video_id=? ORDER BY dataset_id', (vid,)))
            dataset = ds[0]['dataset_id']
            snapshot = COLLECTED.get(dataset, '')
            published = date(s['published_at']); collected = date(snapshot)
            age = round((collected - published).total_seconds()/86400, 4) if published and collected else ''
            if age != '' and age <= 0:
                age = ''
            tags = [label for label, pattern in TOPICS if re.search(pattern, title, re.I)]
            videos.append({'Video_ID': vid, 'Channel_ID': cid, 'Channel': ch['Channel'], 'Dataset': dataset,
                'Title': title, 'Published_at_raw': s['published_at'], 'Metric_snapshot_date': snapshot,
                'Snapshot_precision': 'MANIFEST_COLLECTION_DAY' if snapshot else 'UNKNOWN_INGESTION_IS_NOT_COLLECTION',
                'Views': s['views'], 'Current_views': 'NOT_FETCHED', 'Format': format_of(s['video_type']),
                'Format_source_value': s['video_type'], 'Duration_seconds': s['duration_seconds'], 'Age_days': age,
                'Topic_tags_provisional': '|'.join(tags) or 'UNCLASSIFIED', 'Classification_method': 'TITLE_KEYWORD_HEURISTIC_NOT_SEMANTIC_REVIEW',
                'Audience_problem': 'REQUIRES_SEMANTIC_REVIEW', 'Economic_mechanism': 'REQUIRES_SEMANTIC_REVIEW',
                'Demand_type': 'UNVERIFIED', 'Time_sensitivity': 'UNVERIFIED', 'Narrative_angle': 'UNVERIFIED',
                'Evidence_locator': ds[0]['evidence_locator'], 'URL': s['canonical_url']})
            title_features.append({'Video_ID': vid, 'Title_characters': len(title), 'Title_words': len(title.split()),
                'Question_mark': int('?' in title), 'Question_opener': int(bool(re.match(r'(why|how|what|when|where|who|is|are|do|does|can)\b', title, re.I))),
                'Numbers': int(bool(re.search(r'\d',title))), 'Financial_stakes_tokens': len(re.findall(r'\b(money|wealth|rich|poor|debt|retire|retirement|million|billion)\b', title,re.I)),
                'Negative_tokens': len(re.findall(r'\b(crash|crisis|wrong|never|trap|poor|broke|worst|collapse|scam)\b',title,re.I)),
                'Urgency_tokens': len(re.findall(r'\b(now|today|before|urgent|warning)\b',title,re.I)),
                'Curiosity_tokens': len(re.findall(r'\b(secret|hidden|why|actually|nobody|truth)\b',title,re.I)),
                'Paradox_specificity_search_consistency': 'REQUIRES_SEMANTIC_AND_VISUAL_REVIEW'})
            thumbs.append({'Video_ID': vid, 'Thumbnail_URL': s['thumbnail_url'], 'URL_status': 'PRESENT_NOT_FETCHED' if s['thumbnail_url'] else 'MISSING_REGISTRY_FIELD',
                           'Local_asset': '', 'Association_verified': 'NO', 'Mobile_review': 'NOT_REVIEWED', 'Historical_design': 'UNKNOWN'})
            ts = list(con.execute('SELECT * FROM transcripts WHERE youtube_video_id=? ORDER BY dataset_id', (vid,)))
            if not ts:
                transcripts.append({'Video_ID':vid,'Dataset':dataset,'Status':'MISSING','Words':0,'Text_SHA256':'','Duplicate_of':'','Caption_type':'','Evidence_locator':'','Timing':'NOT_ASSESSED','Human_verified':'NO'})
            for t in ts:
                txt = t['transcript_text'] or ''; valid = not t['is_placeholder'] and bool(txt.strip())
                digest = hashlib.sha256(txt.encode()).hexdigest() if valid else ''
                duplicate = seen_hash.get(digest, '') if digest else ''
                if digest: seen_hash.setdefault(digest, vid)
                words = re.findall(r"\b[\w’'-]+\b",txt)
                transcripts.append({'Video_ID':vid,'Dataset':t['dataset_id'],'Status':'TEXT_AVAILABLE' if valid else 'PLACEHOLDER',
                    'Words':len(words),'Text_SHA256':digest,'Duplicate_of':duplicate,'Caption_type':t['caption_type'],
                    'Evidence_locator':t['evidence_locator'],'Timing':'PLAINTEXT_NO_TIMED_SEGMENTS_EXTRACTED','Human_verified':'NO'})
                if not valid: continue
                sentences = [s for s in re.split(r'[.!?]+',txt) if s.strip()]
                features.append({'Video_ID':vid,'Dataset':t['dataset_id'],'Text_SHA256':digest,'Word_count':len(words),
                    'Opening_40_words':' '.join(txt.split()[:40]),'Ending_40_words':' '.join(txt.split()[-40:]),
                    'Sentence_word_mean_proxy':round(len(words)/max(len(sentences),1),2),
                    'Question_marks':txt.count('?'),'Numeric_tokens':len(re.findall(r'\b\d[\d,.%]*',txt)),
                    'Causal_marker_count':len(re.findall(r'\b(because|therefore|so that|as a result)\b',txt,re.I)),
                    'Example_marker_count':len(re.findall(r'\b(imagine|for example|suppose|picture this)\b',txt,re.I)),
                    'Transition_marker_count':len(re.findall(r'\b(but|however|meanwhile|then)\b',txt,re.I)),
                    'Evidence_marker_count':len(re.findall(r'\b(according to|study|research|report|data)\b',txt,re.I)),
                    'CTA_marker_count':len(re.findall(r'\b(subscribe|like this video|leave a comment)\b',txt,re.I)),
                    'Opening_3_10_30_seconds':'UNAVAILABLE_PLAINTEXT', 'Narration_density':'NOT_RELIABLE_WITHOUT_TIMED_NARRATION',
                    'Semantic_hook_loops_payoff':'REQUIRES_DEEP_REVIEW'})
    for v in videos:
        values = compare(v, videos)
        v.update(dict(zip(['Performance_tier','Peer_count','Lifetime_rate_ratio','Peer_Video_IDs','Tier_basis'],values)))
    review_path = BASE / 'SEMANTIC_REVIEWS.csv'
    if review_path.exists():
        semantic = {r['Video_ID']: r for r in read_csv(review_path)}
        for v in videos:
            r = semantic.get(v['Video_ID'])
            if r:
                for key in ['Audience_problem', 'Economic_mechanism', 'Demand_type', 'Narrative_angle']:
                    v[key] = r[key]
                v['Classification_method'] = r['Review_scope'] + ';ANALYST_INTERPRETATION'
    visual_path = BASE / 'THUMBNAIL_REVIEWS.csv'
    if visual_path.exists():
        reviewed = {r['Video_ID'] for r in read_csv(visual_path)}
        assets = {}
        for name in ['THUMBNAIL_FETCH_REGISTER.csv', 'THUMBNAIL_FALLBACK_REGISTER.csv']:
            path = BASE / name
            if path.exists():
                assets.update({r['Video_ID']: r for r in read_csv(path) if r['Path']})
        for t in thumbs:
            r = assets.get(t['Video_ID'])
            if r:
                t['Local_asset'] = r['Path']
                t['Association_verified'] = 'VIDEO_ID_IN_CDN_URL'
                t['Mobile_review'] = 'REVIEWED_320_WIDE' if t['Video_ID'] in reviewed else 'NOT_REVIEWED'
    write_csv('CANONICAL_CHANNELS.csv', channels)
    universe = list(channels)
    landscape = BASE / 'LANDSCAPE_CHANNELS.csv'
    if landscape.exists():
        for r in read_csv(landscape):
            universe.append(dict(Channel_ID=r['Channel_ID'], Channel=r['Name'], Scope='RESEARCH_ONLY_LANDSCAPE',
                Dataset=r['Evidence'], Videos=int(r['Visible_videos']), Niche='SEE_LANDSCAPE_RESEARCH',
                Research_depth=r['Depth'], Current_growth=r['Growth']))
    for ident, name, count in [('UCrNfRFWnLC3tCy1TnyhVQ7g','Casual Finance / @CasuallyFinance',206),
                               ('RESEARCH_ONLY_NOT_PROMOTED','Casual Economics',11)]:
        universe.append(dict(Channel_ID=ident,Channel=name,Scope='REUSED_RESEARCH_OVERLAY',Dataset='REUSED_SOURCE_REGISTER.csv',
            Videos=count,Niche='FINANCE_ECONOMICS',Research_depth='EXISTING_REPORTS_AND_TABLES_REUSED',Current_growth='UNKNOWN'))
    write_csv('CHANNEL_UNIVERSE.csv', universe)
    write_csv('VIDEO_MASTER.csv', videos)
    write_csv('TRANSCRIPT_COVERAGE.csv',transcripts)
    write_csv('THUMBNAIL_COVERAGE.csv',thumbs)
    write_csv('SCRIPT_FEATURES.csv',features)
    write_csv('TITLE_FEATURES.csv',title_features)
    coverage=[]
    for ch in channels:
        ids={v['Video_ID'] for v in videos if v['Channel_ID']==ch['Channel_ID']}
        coverage.append({'Channel':ch['Channel'],'Channel_ID':ch['Channel_ID'],'Videos':len(ids),
            'Titles':sum(bool(v['Title']) for v in videos if v['Video_ID'] in ids),
            'Transcript_records':sum(t['Status']=='TEXT_AVAILABLE' for t in transcripts if t['Video_ID'] in ids),
            'Thumbnail_URLs':sum(bool(t['Thumbnail_URL']) for t in thumbs if t['Video_ID'] in ids),
            'Mobile_images_reviewed':0,'Dated_metrics':sum(bool(v['Metric_snapshot_date']) for v in videos if v['Video_ID'] in ids),
            'Comparable_tiers':sum(v['Performance_tier']!='INSUFFICIENT_DATA' for v in videos if v['Video_ID'] in ids)})
    write_csv('BASELINE_COVERAGE.csv',coverage)
    stats={'channels':len(channels),'unique_videos':len({v['Video_ID'] for v in videos}),
        'nonplaceholder_transcript_records':len(features),'transcript_unique_text_hashes':len(seen_hash),
        'duplicate_text_records':sum(bool(t['Duplicate_of']) for t in transcripts),
        'titles':sum(bool(v['Title']) for v in videos),'thumbnail_urls':sum(bool(t['Thumbnail_URL']) for t in thumbs),
        'formats':dict(Counter(v['Format'] for v in videos)), 'tiers':dict(Counter(v['Performance_tier'] for v in videos)),
        'db_sha256_before':before,'db_sha256_after':hashlib.sha256(DB.read_bytes()).hexdigest(),
        'metric_dates':'Historical collection dates only; ingestion-only datasets not age-ranked',
        'complete_phase_2':False}
    assert stats['channels']==13 and stats['unique_videos']==966 and len(features)==955
    assert before==stats['db_sha256_after']
    (BASE/'BASELINE_VALIDATION.json').write_text(json.dumps(stats,indent=2)+'\n')
    print(json.dumps(stats,indent=2))


if __name__=='__main__':
    main()
