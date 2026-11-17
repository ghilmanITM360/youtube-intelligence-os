"""Helpers for the versioned historical-reanalysis layer. Original accepted audits are never edited.
finalize(spec): builds comparisons with exact witnesses, reveals the K01 tier ONLY after the content assessment is fixed, validates structure,
writes reanalysis/videos/<video_id>.json and advances the campaign ledger to SEMANTIC_REVIEW_PENDING (structural pass is not semantic approval)."""
import csv, json, pathlib, sys
H = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(H.parent / 'reference-framework'))
import reference_comparison as rc
LEDGER = H / 'REANALYSIS_CAMPAIGN_LEDGER.csv'
def finalize(spec):
    vid = spec['video_id']; t = rc.transcript(vid); comps = []
    for rule, w, j, why, unc in spec['comparisons']:
        wit = rc.witness(t, w[1]) if w and w[0] == 'T' else ({'kind': 'TITLE' if w[0] == 'TITLE' else 'THUMBNAIL_OBSERVATION', 'text': w[1]} if w else {})
        comps.append(rc.row(rule, wit, j, why, unc))
    rows = list(csv.DictReader(open(LEDGER))); led = next(r for r in rows if r['video_id'] == vid)
    out = {'video_id': vid, 'framework_version': 'v1', 'rule_index_version': 'v1', 'assessment_mode': 'HISTORICAL_REANALYSIS_CONTENT_FIRST',
           'original_audit_row_sha256': led['original_row_sha256'], 'original_packets': led['packet_files'].split('|'), 'transcript_chars_read': len(t),
           'read_scope': 'full stored transcript read; title/metadata snapshot from registry; thumbnail inspected natively and at mobile size' if spec.get('thumbnail_inspected') else 'full stored transcript read; thumbnail NOT inspected (no local authentic file)',
           'comparisons': comps, **{k: spec[k] for k in ('title', 'dimension_notes', 'financial_checks', 'strengths', 'weaknesses', 'contradictions', 'improvement_opportunities', 'unavailable')},
           'measured_public_performance': {'k01_tier_revealed_after_assessment': led['k01_tier'], 'lifetime_rate_ratio': led['lifetime_rate_ratio'], 'age_days': led['age_days'], 'views_likes_comments_snapshot': spec['snapshot']},
           'performance_association_note': spec['performance_note'], 'timing': 'SINGLE_SNAPSHOT: upload date plus lifetime views is not a growth curve; breakout date, velocity and time-to-viral cannot be reconstructed.',
           'limits': 'Heuristics are lenses, not platform facts; conformity is not causation; no CTR, retention, impressions or audio evidence.'}
    p = H / 'videos' / f'{vid}.json'; json.dump(out, open(p, 'w'), indent=1, ensure_ascii=False)
    e = rc.validate(str(p))
    if not e:
        led['campaign_status'] = 'SEMANTIC_REVIEW_PENDING'; led['reanalysis_file'] = f'reanalysis/videos/{vid}.json'
        w = csv.DictWriter(open(LEDGER, 'w', newline=''), list(rows[0])); w.writeheader(); w.writerows(rows)
    return e
