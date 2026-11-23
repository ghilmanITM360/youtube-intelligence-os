import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

home = Path.home()
out = Path(__file__).parent
repo = home / 'workprojects/visual-audit-worktrees/casually-finance'
channel = repo / 'CHANNEL_VISUAL_AUDIT/CHANNEL_001'
motion = repo / 'research/visual-audit/CHANNEL_001_CasuallyFinance'
archive = home / 'Downloads/CasuallyFinance-Forensic-Research'

def read(path):
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream))

def write(path, rows):
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

rows = read(channel / 'COVERAGE_MATRIX.csv')
meta = {r['video_id']: r for r in read(archive / '01_CHANNEL_METADATA/all-videos-metadata.csv')
        if r['channel_id'] == 'UCrNfRFWnLC3tCy1TnyhVQ7g'}
alias_candidates = defaultdict(set)
for alias in read(archive / '00_MANIFEST/REPOSITORY_SOURCE_ALIASES.csv'):
    alias_candidates[alias['sha256']].add(alias['video_id'])
aliases = {digest: next(iter(ids)) for digest, ids in alias_candidates.items() if len(ids) == 1}
profiles = {r['video_id']: r for r in read(motion / '21_AUTO_MOTION_PROFILE_ALL_VIDEOS.csv')}
idless = {(r['file'], r['key']): r for r in read(motion / '22_IDLESS_MOTION_PROFILE.csv')}
sequence_codes = defaultdict(set)
for seq in read(channel / 'EVIDENCE_SEQUENCES.csv'):
    description = ' '.join(seq[k] or '' for k in ('label', 'assets')).lower()
    for family, words in {
        'document': r'article|headline|screenshot|report',
        'character': r'character|stick|uncle sam|presenter',
        'real_person_photo': r'portrait|headshot|host photo|photo head',
        'chart': r'chart|graph',
    }.items():
        if re.search(words, description):
            sequence_codes[seq['video']].add(family)

counts = Counter(r['sha256'] for r in rows)
for r in rows:
    vid = r['source_id'].split()[0]
    basis = 'coverage matrix'
    if r['sha256'].startswith('a57768bd5a32a8b0'):
        vid, basis = 'Uumnx2Fo6cE', 'legacy manifest and local SHA-256'
    if vid == 'FILE-?':
        vid = aliases.get(r['sha256'], '')
        basis = 'historical SHA-linked repository alias' if vid else 'unresolved ID'
    md = meta.get(vid, {})
    profile = profiles.get(vid) or idless.get((r['title'], 'FILE-' + r['sha256'][:8])) or {}
    codes = sequence_codes[vid]
    r.update(
        reconciled_video_id=vid, identity_basis=basis, physical_hash_multiplicity=counts[r['sha256']],
        published_at=md.get('published_at', ''), publication_year=md.get('published_at', '')[:4],
        topic_metadata_heuristic=md.get('topic_derived_heuristic', ''),
        change_events_per_min=profile.get('change_events_per_min', ''),
        mean_changed_pct=profile.get('mean_changed_pct', ''),
        still_frames_pct=profile.get('still_frames_pct', ''),
        document_lead='indexed sequence lead' if 'document' in codes else 'unknown',
        character_lead='indexed sequence lead' if 'character' in codes else 'unknown',
        real_person_photo_lead='indexed sequence lead' if 'real_person_photo' in codes else 'unknown',
        chart_lead='indexed sequence lead' if 'chart' in codes else 'unknown',
        composition_density='unknown', visual_complexity='unknown',
        historical_event_lead='unknown', mechanism_lead='unknown', market_news_lead='unknown',
        editing_family='unknown', animation_family='unknown', current_batch='',
    )
    if vid in ('Uumnx2Fo6cE', 'hbsYaLaN_F8', 'dlBhLhn8lL0', '965yZYhY_f4'):
        r['current_batch'] = 'B01 targeted frame review'
        r['character_lead'] = 'observed in targeted windows'
        r['real_person_photo_lead'] = 'observed in targeted windows'
        r['composition_density'] = 'sparse and dense states observed'
        r['document_lead'] = ('observed in targeted windows' if vid in ('Uumnx2Fo6cE', '965yZYhY_f4')
                              else 'provenance unclear within reviewed window')
        r['editing_family'] = 'hard replacements observed within windows'
        r['animation_family'] = 'document marker and pose changes observed' if vid in ('Uumnx2Fo6cE', '965yZYhY_f4') else 'held composite sampled'
    if vid == 'YEhsWyY_WKQ':
        r['current_batch'] = 'H01 segment holdout'
        for field in ('document_lead', 'chart_lead', 'character_lead', 'market_news_lead'):
            r[field] = 'observed in holdout sample'
        r['composition_density'] = 'sparse and dense states observed'
    if vid == 'Uumnx2Fo6cE':
        r['historical_event_lead'] = 'outside reviewed windows'
        r['note'] += ' | recovered 507-state legacy ledger; separate historical contract'
write(out / 'FULL_CORPUS_VISUAL_CLASSIFICATION.csv', rows)
print(len(rows), len(counts), Counter(r['tier'] for r in rows), Counter(r['format'] for r in rows))
for k in ('reconciled_video_id','published_at','topic_metadata_heuristic','change_events_per_min'):
    print(k, sum(bool(r[k]) for r in rows))
