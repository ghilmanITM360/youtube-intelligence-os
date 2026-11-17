"""Read-only structural validation and master reconciliation for one evidence unit."""
import csv
import hashlib
import json
import sys
from pathlib import Path

KEYS = {'SENTENCES': 'sentence_id', 'SHOTS': 'shot_id', 'STATES': 'state_id',
        'MOTIONS': 'motion_id', 'ASSETS': 'asset_id', 'AUDIO_EVENTS': 'audio_event_id',
        'AUDIO_VISUAL_SYNC': 'sync_id', 'SEMANTIC_BEATS': 'beat_id',
        'FINANCE_CLAIMS': 'claim_id', 'SOURCE_CLAIMS': 'source_claim_id'}


def validate(root, vid, scratch=None):
    base = root / 'data/extracted/forensic-analysis/casual-economics/2026-10-12'
    d = base / '02_VIDEO_FORENSICS' / vid
    source = json.loads((d / 'SOURCE.json').read_text())
    duration = source['duration_sec']
    sha = source['sha256']
    checks = {'source_identity': source['video_id'] == vid}
    tables = {}
    for name, key in KEYS.items():
        path = d / (name + '.csv')
        if name == 'SOURCE_CLAIMS' and not path.exists():
            continue  # Earlier evidence units did not have a separate source-claim table.
        with path.open() as f:
            rows = list(csv.DictReader(f))
        tables[name] = rows
        checks[name + '_unique'] = len({x[key] for x in rows}) == len(rows)
        checks[name + '_identity'] = bool(rows) and all(x['video_id'] == vid for x in rows)
        checks[name + '_hashes'] = all(x.get('source_sha256', sha) == sha for x in rows) if name != 'SENTENCES' else all(x['source_sha256'] == source['public_caption_source']['sha256'] for x in rows)
        if rows and 'start_sec' in rows[0]:
            checks[name + '_bounded'] = all(0 <= float(x['start_sec']) < float(x['end_sec']) <= duration + .001 for x in rows)
        with (base / '03_MASTER_DATA' / ('MASTER_' + name + '.csv')).open() as f:
            all_master = list(csv.DictReader(f))
        checks[name + '_master_unique'] = len({(x['video_id'], x[key]) for x in all_master}) == len(all_master)
        checks[name + '_master_equal'] = rows == [x for x in all_master if x['video_id'] == vid]
    ids = {name: {x[KEYS[name]] for x in rows} for name, rows in tables.items()}
    shotmap = {x['shot_id']: x for x in tables['SHOTS']}
    statemap = {x['state_id']: x for x in tables['STATES']}
    capmap = {x['sentence_id']: x for x in tables['SENTENCES']}
    audiomap = {x['audio_event_id']: x for x in tables['AUDIO_EVENTS']}
    checks['state_shots'] = all(x['shot_id'] in ids['SHOTS'] and float(shotmap[x['shot_id']]['start_sec']) <= float(x['start_sec']) < float(x['end_sec']) <= float(shotmap[x['shot_id']]['end_sec']) + .001 for x in tables['STATES'])
    checks['state_assets'] = all(set(x['asset_ids'].split(';')) <= ids['ASSETS'] for x in tables['STATES'])
    checks['state_evidence'] = all((d / x['evidence_sheet']).is_file() for x in tables['STATES'])
    checks['motion_refs'] = all(x['shot_id'] in ids['SHOTS'] and x['target_state_id'] in ids['STATES'] and statemap[x['target_state_id']]['shot_id'] == x['shot_id'] for x in tables['MOTIONS'])
    checks['sync_refs'] = all(x['shot_id'] in ids['SHOTS'] and x['state_id'] in ids['STATES'] and x['sentence_id'] in ids['SENTENCES'] and x['audio_event_id'] in ids['AUDIO_EVENTS'] for x in tables['AUDIO_VISUAL_SYNC'])
    checks['sync_intervals'] = all(float(x['start_sec']) == max(float(statemap[x['state_id']]['start_sec']), float(capmap[x['sentence_id']]['start_sec'])) and float(x['end_sec']) == min(float(statemap[x['state_id']]['end_sec']), float(capmap[x['sentence_id']]['end_sec'])) and float(audiomap[x['audio_event_id']]['start_sec']) <= float(x['start_sec']) < float(audiomap[x['audio_event_id']]['end_sec']) for x in tables['AUDIO_VISUAL_SYNC'])
    checks['linked_states'] = all(set(x['state_ids'].split(';')) <= ids['STATES'] for name in ['FINANCE_CLAIMS', 'SEMANTIC_BEATS', 'SOURCE_CLAIMS'] if name in tables for x in tables[name])
    checks['asset_occurrences'] = all(int(a['state_occurrences']) == sum(a['asset_id'] in s['asset_ids'].split(';') for s in tables['STATES']) for a in tables['ASSETS'])
    if 'SOURCE_CLAIMS' in tables:
        checks['source_claim_links'] = all(x['finance_claim_id'] in ids['FINANCE_CLAIMS'] and set(x['sentence_ids'].split(';')) <= ids['SENTENCES'] and set(x['shot_ids'].split(';')) <= ids['SHOTS'] for x in tables['SOURCE_CLAIMS'])
    trackpath = root / 'data/extracted/channel-data/DS-000036/caption-tracks.json'
    track = json.loads(trackpath.read_text())['tracks'][vid]
    checks['caption_inline_provenance'] = hashlib.sha256(track['srt'].encode()).hexdigest() == source['public_caption_source']['sha256'] == track['srt_utf8_sha256']
    checks['caption_not_audio_certification'] = all('UNVERIFIED' in x['confidence'] for x in tables['SENTENCES'])
    thumbnail = json.loads((d / 'evidence/THUMBNAIL_PROVENANCE.json').read_text())
    checks['thumbnail_hashes'] = all(hashlib.sha256((d / 'evidence' / n).read_bytes()).hexdigest() == h for n, h in thumbnail['files'].items()) if isinstance(thumbnail.get('files'), dict) else True
    if scratch:
        work = scratch / vid
        va = json.loads((work / 'visual_auto.json').read_text())
        pts = json.loads((work / ('PTS_VALIDATION.json' if (work / 'PTS_VALIDATION.json').exists() else 'DECODE_VALIDATION.json')).read_text())
        checks['scratch_identity'] = va['video_id'] == vid and pts.get('video_id', vid) == vid
        checks['native_frame_count'] = va['frames'] == pts['native_pts_frames']
        checks['scratch_not_adjusted'] = not pts.get('timestamp_offset_applied_to_candidate_tables', False)
        checks['all_representatives'] = {x['state_id'] for x in va['states']} == ids['STATES']
        offset = pts['first_pts']
        for kind in ['STATES', 'SHOTS']:
            checks[kind + '_offset_once'] = len(tables[kind]) == len(va[kind.lower()]) and all(float(x['start_sec']) == round(s['start'] + offset, 6) and float(x['end_sec']) == round(s['end'] + offset, 6) for x, s in zip(tables[kind], va[kind.lower()]))
        checks['representative_seek_unchanged'] = all(float(x['representative_source_seek_sec']) == s['rep_t'] for x, s in zip(tables['STATES'], va['states']))
        checks['representative_interval_tolerance'] = all(float(x['start_sec']) - 1/va['fps'] - .001 <= float(x['representative_source_seek_sec']) <= float(x['end_sec']) + 1/va['fps'] + .001 for x in tables['STATES'])
        episodes = [x for x in va['episodes'] if x['cls'] != 'MICRO_CHANGE']
        checks['motions_offset_once'] = len(episodes) == len(tables['MOTIONS']) and all(x['motion_id'] == e['ep_id'] and float(x['start_sec']) == round(e['t0'] + offset, 6) and float(x['end_sec']) == round(e['t1'] + offset, 6) for x, e in zip(tables['MOTIONS'], episodes))
        checks['saved_frames'] = all((work / 'frames' / (x['state_id'] + '.jpg')).is_file() for x in tables['STATES'])
        import numpy as np
        with np.load(work / 'features.npz') as features:
            checks['feature_geometry'] = int(features['N']) == va['frames'] and (work / 'gray.u8').stat().st_size == int(features['N']) * int(features['W']) * int(features['H']) and all(len(features[k]) == va['frames'] for k in ['mad', 'cnt', 'lum', 'bbox', 'cen'])
        sourcefile = Path('/Users/ghilmanislam360') / source['source_locator']
        with sourcefile.open('rb') as f:
            checks['actual_source_hash'] = hashlib.file_digest(f, 'sha256').hexdigest() == sha
    return {'video_id': vid, 'checks': checks, 'all_pass': all(checks.values()), 'counts': {n: len(rows) for n, rows in tables.items()}, 'stable_state_seconds': round(sum(float(s['end_sec'])-float(s['start_sec']) for s in tables['STATES']), 6), 'container_duration_sec': duration}

if __name__ == '__main__':
    result = validate(Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd(), sys.argv[1], Path(sys.argv[3]) if len(sys.argv) > 3 else None)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['all_pass'] else 1)
