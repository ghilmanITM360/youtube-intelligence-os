"""Validate portable reviewed packaging records without reading raw image bytes.

This checks joins, arithmetic and provenance. It does not claim new visual QA.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKET = ROOT / 'docs/research/packaging-validated-2026-10-11/records.json'
SCORE_LIMITS = {
    'thumbnail': dict(story_score=15, psychological_hook_score=15, title_partnership_score=15, hierarchy_score=10, mobile_readability_score=10, composition_score=10, emotion_subject_alignment_score=10, credibility_score=10, distinctiveness_score=5),
    'package': dict(title_clarity=10, title_curiosity_specificity=10, thumbnail_visual_proposition=10, thumbnail_hierarchy=10, title_thumbnail_complementarity=15, one_second_comprehension_score=10, curiosity_gap=10, credibility=10, mobile_viability=5, distinctiveness=5, promise_alignment=5),
}


def row_hash(row):
    return hashlib.sha256(json.dumps(row, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def validate(packet):
    errors = []
    if packet.get('schema_version') != 'validated-packaging-research-1':
        errors.append('Unsupported packaging research schema')
    seen = set()
    for row in packet.get('records', []):
        video, thumbnail, channel = row['Video_ID'], row['Thumbnail_ID'], row['Channel_ID']
        if not re.fullmatch(r'[A-Za-z0-9_-]{11}', video) or video in seen or not channel:
            errors.append('Invalid/duplicate exact identity: ' + video)
        seen.add(video)
        provenance, package, audit, qa = row['provenance'], row['package_audit'], row['thumbnail_audit'], row['qa']
        digest = provenance.get('source_sha256', '')
        if not re.fullmatch(r'[a-f0-9]{64}', digest) or thumbnail != 'THB-' + digest:
            errors.append('Invalid thumbnail hash: ' + video)
        if not provenance.get('source_url') and not provenance.get('evidence_locator'):
            errors.append('Missing source locator: ' + video)
        if not provenance.get('creative_temporal_alignment') or not provenance.get('audit_version') or not provenance.get('source_observed_at'):
            errors.append('Missing temporal/version provenance: ' + video)
        if (package['Video_ID'], package['Thumbnail_ID'], package['Package_ID']) != (video, thumbnail, 'PKG-' + video):
            errors.append('Package identity mismatch: ' + video)
        if audit['Thumbnail_ID'] != thumbnail or row['title_audit']['Video_ID'] != video:
            errors.append('Title/thumbnail identity mismatch: ' + video)
        if qa.get('status') not in {'PASS', 'PASS_WITH_CORRECTIONS', 'HISTORICAL_SAMPLE'}:
            errors.append('Missing explicit QA: ' + video)
        review = qa['review']
        if review.get('Video_ID', video) != video or review.get('Package_ID', 'PKG-'+video) != 'PKG-'+video or review.get('Thumbnail_ID', thumbnail) != thumbnail:
            errors.append('QA identity mismatch: ' + video)
        for kind, value, origin in [('title', row['title_audit'], provenance['title_audit_origin']), ('thumbnail', audit, provenance['thumbnail_audit_origin']), ('package', package, provenance['package_audit_origin']), ('qa', review, qa['source'])]:
            if row_hash(value) != origin['row_sha256'] or packet['source_artifacts'].get(origin['research_path']) != origin['file_sha256']:
                errors.append('Invalid ' + kind + ' audit provenance: ' + video)
        for kind, value in [('thumbnail', audit), ('package', package)]:
            scores = [value.get(key) for key in SCORE_LIMITS[kind]]
            if not all(isinstance(value.get(key), int) and 0 <= value[key] <= limit for key, limit in SCORE_LIMITS[kind].items()) or sum(score for score in scores if isinstance(score, int)) != value['score_100']:
                errors.append('Invalid ' + kind + ' score arithmetic: ' + video)
            if value.get('content_promise_verified') != 'NOT_CHECKED':
                errors.append('Unsupported content-verification claim: ' + video)
    if not seen:
        errors.append('Empty packaging research packet')
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet', type=Path, default=DEFAULT_PACKET)
    parser.add_argument('--registry', type=Path, default=ROOT / 'data/catalog/youtube_channel_registry.db')
    args = parser.parse_args(argv)
    packet = json.loads(args.packet.read_text())
    errors = validate(packet)
    with sqlite3.connect(args.registry.resolve().as_uri() + '?mode=ro', uri=True) as conn:
        for row in packet['records']:
            identity = conn.execute('SELECT canonical_channel_id FROM videos WHERE youtube_video_id=?', (row['Video_ID'],)).fetchall()
            if identity != [(row['Channel_ID'],)]:
                errors.append('Canonical registry identity mismatch: ' + row['Video_ID'])
    print(json.dumps({'records': len(packet['records']), 'errors': errors, 'raw_images_read': 0, 'status':'PASS' if not errors else 'FAIL'}, indent=2))
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
