"""Seal a text-only recoverable sampled-narration milestone; no CT or AV promotion."""
from pathlib import Path
import csv
import hashlib
import json
import shutil

R = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
S = R / 'session_20261104'
C = Path('/Users/ghilmankhan/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104')
assert not (R / 'EVIDENCE_SHA256SUMS_checkpoint_P').exists()
stats = json.loads((R / 'production_v1/narration_visual_alignment_stats_v3.json').read_text())
assert stats['visually_sampled_relation_rows_reviewed'] == 199 and stats['pending_count'] == 0
partition = list(csv.DictReader((R / 'integrated_v4/frame_partition_v4.csv').open()))
counts = [0] * 19862
for row in partition:
    for frame in range(int(row['start']), int(row['end']) + 1):
        counts[frame] += 1
assert set(counts) == {1}
copies = ['ASR156_supplemental_review_v1.json', 'target_roster_v1.json', 'target_roster_v1.csv', 'source_identity_baseline_v1.json',
          'SHA256SUMS_roster_v1', 'SHA256SUMS_source_identity_baseline_v1']
campaign = R / 'campaign_35_v1'
campaign.mkdir(exist_ok=False)
for name in copies:
    shutil.copyfile(C / name, campaign / name)
    assert hashlib.sha256((C / name).read_bytes()).digest() == hashlib.sha256((campaign / name).read_bytes()).digest()
known = (R / 'session_20261103/KNOWN_ISSUES_LEDGER_v4.md').read_text()
known = known.replace('# V006 known issues v3', '# V006 known issues v5 — checkpoint P')
known = known.replace('- OPEN:34ASR visual-relation items fromASR156,22reviewed-but-undetermined relation rows,5potentialASR/source-text mismatches; actual hearing required.',
                      '- SAMPLED CROSSWALK REVIEWED: all199 ASR relation rows now reviewed,0unreviewed;30UNDETERMINED and5POTENTIAL_MISMATCH remain. These are not certified speech, economic errors or continuous sound/visual synchronization. Actual hearing required. Eleven rows have an outside-interval sample requiring source-aligned followup:56,57,74,120,121,133,136,152,162,166,171.')
known += '\n- PRODUCTION LOCATOR FIX: S0000 blank f0–1 had referenced a representative atf36. Versioned draftv2 now references independently viewed nativef0. All447 draft-state representative locators lie within their declared draft intervals. Other originality/motion/static-anchor gates stay partial.\n'
(S / 'KNOWN_ISSUES_LEDGER_v5.md').write_text(known)
coverage = json.loads((R / 'session_20261103/coverage_checkpoint_O.json').read_text())
coverage.update(narration_reviewed=199, narration_pending=0, narration_new_image_returns=356,
                narration_visual_semantic_review='ALL199_SAMPLED_ASR_RELATION_ROWS_REVIEWED;30UNDETERMINED;5POTENTIAL_MISMATCH;notcontinuoussync',
                narration_outside_interval_followup_ids=[56,57,74,120,121,133,136,152,162,166,171],
                production='447state draftv2; S0000 representative repaired; original timing test bounded3.125s only; no whole-video production pass')
(S / 'coverage_checkpoint_P.json').write_text(json.dumps(coverage, indent=2) + '\n')
quality = json.loads((R / 'session_20261103/QUALITY_GATE_checkpoint_O.json').read_text())
quality.update(status='VISUAL_ANALYSIS_PARTIAL_INTEGRATED_V4_CHECKPOINT_P', CT_SCAN_COMPLETE=False,
               coverage_ref='research/session_20261104/coverage_checkpoint_P.json',
               known_issues='research/session_20261104/KNOWN_ISSUES_LEDGER_v5.md',
               narration_review=stats, active_task='ONE_BOUNDED_REVIEWER: four missing motion objects; see live output status',
               next_task='Audit/integrate four motion reviews, source-aligned followup for11outside-interval rows and5potential mismatches, then semantic/native/productionQA; qualified full-source hearing still required')
quality['gates']['narration_visual_semantics'] = 'ALL199_SAMPLED_ROWS_REVIEWED;PARTIAL30UNDETERMINED_AND5POTENTIAL_MISMATCH;ASR_ONLY'
quality['gates']['production_state_prompts'] = 'DRAFT447_v2;S0000representative_fixed;originality_motion_static_anchor_validation_pending'
quality['campaign_35'] = dict(target=35, roster='research/campaign_35_v1/target_roster_v1.json',
                            source_identity_baseline='research/campaign_35_v1/source_identity_baseline_v1.json',
                            complete_count_certified=0, note='35selected unique source hashes are readiness, not35fully analyzed videos')
(S / 'QUALITY_GATE_checkpoint_P.json').write_text(json.dumps(quality, indent=2) + '\n')
handoff = '''# Video006 checkpoint P — sampled narration crosswalk milestone
Status VISUAL_ANALYSIS_PARTIAL / ASR_UNCERTIFIED / ACTUAL_LISTENING0 / NOT_CT_COMPLETE.
Source xtqbRt94TTw, SHA256030a85ad15c25a5ac36cf0a8c8fc67e3b303ba7b3c1883af064a151ebefa7a66; original unchanged in Downloads/videos in mp3/CasuallyFinance. Workspace /Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan.
Remote parentO217671d5aaf3c706ffdce947e75224a389430645; local checkout HEADf4dc5d14d6ad03c1edd92e48fac779e7a8555fc5, localresearchref2b10f104c1edf0562e2628d1dab1afba2546bd8e deliberately unchanged. Existing private-index/commit-tree normal-push method preserves checkout/index; no PR created/merged/closed. Published P SHA/readbacks will be in session_20261103/publication_receipt_P.json and the post-publication handoff; do not assume a local seal was pushed.
All10first-pass shards reused, newly0/pending0. Integratedv4 still19862frames exactly once,0numerical gaps/overlaps/unresolvedowners;123gap reviews and146merge/split rulings preserved.329composition intervals are not a certified shot count. Global native event/cut timing and SUB032 semantic microfeature remain partial.
Narration visual crosswalkv3 now has199/199sampled ASR-qualified relation rows,0unreviewed:165prior+rootASR156+33part03. New actual image-return audit:2root+56agent scaled960x540 returns, exact bytes/multiplicity verified; prior165 raw outputs immutable.30UNDETERMINED and5POTENTIAL_MISMATCH remain, not errors proven by listening. Outside-interval sample rows56,57,74,120,121,133,136,152,162,166,171 require in-interval source frames. Actual listening0seconds, no qualified hearing tool available; no ASR=hearing or AV signoff.
Production draftv2 keeps447historical source states and repairs S0000 representativef36→nativef0. Other446 representative locators are inside draft intervals. Originality, static anchors, per-state motion/native and whole-video reconstruction QA remain open; original75-frame timing test remains bounded only.
NEXT: inspect actual status of sole reviewer at motion_missing_fields_review_v1/OUT_motion_missing_fields_review_v1.json, audit actual image bytes, then integrate new motion version without changing raw first-pass outputs. Prepared evidence:40consecutive nativeROIs+8scaledcontexts, not viewed merely because extracted. Do not duplicate a live/finished reviewer. Then source-aligned11-row/5numeric-mismatch followup, remaining semantic/native/production requirements and qualified human/source audio listening. Continue other executable gates and then35selected videos while preserving truth labels; no CT promotion.
35-video roster and source identity baseline copied byte-identically into campaign_35_v1 for text-only recovery.35present sources,35uniqueSHA256s,35video+audio streams; hash/filename attribution does not independently confirm every videoID. Originals and every derived image/audio/video remain LOCAL_ONLY; remote text hashes are not remote media availability.
Resources at milestone: last16%five-hour,18%weekly,credits0;1reset credit observed remaining; this continuation did not invoke any reset/paid tool, external reset origin unestablished. Disk83GiB free,memory free38%,swap7906.75MiB. Refresh before next bounded operation. Heartbeat updated to2hourly once capacity cleared. Own session v3 lock is held by actual Codex executablePID1455 at seal; release only private token in session_20261104/owner_receipt_private.txt when stopping. Never alter Finance/Barely Evolved locks/processes/schedulers or unrelated index/untracked evidence. No Graphify.
'''
(S / 'CONTINUATION_HANDOFF_checkpoint_P.md').write_text(handoff)
assert 'CONTINUATION_HANDOFF.md' not in [x.split(maxsplit=1)[1].strip() for x in (R / 'EVIDENCE_SHA256SUMS_checkpoint_O').read_text().splitlines()]
(R / 'CONTINUATION_HANDOFF.md').write_text(handoff)
report = '# Video006 checkpoint P visual-forensics report\n\n' + handoff.split('\n', 1)[1]
(R / 'visual_ct_scan_report_v3.md').write_text(report)
files = [str(p.relative_to(R)) for p in campaign.iterdir()]
files += ['agents/narration_visual_review_03/' + x for x in ['BRIEF.md', 'items.json', 'output_row_schema_example.json', 'OUT_narration_visual_review_03.json']]
files += ['production_v1/' + x for x in ['narration_visual_alignment_v3.csv', 'narration_visual_alignment_stats_v3.json', 'per_state_production_spec_DRAFT_v2.csv']]
files += ['session_20261104/' + x for x in ['ASR156_independent_image_return_audit_v1.json', 'narration_part03_independent_validation_v1.json', 'production_representative_locator_audit_v1.json', 'production_representative_locator_fix_v1.json', 'resume_live_evidence_v1.json', 'checkpoint_O_revalidation_v1.json', 'KNOWN_ISSUES_LEDGER_v5.md', 'coverage_checkpoint_P.json', 'QUALITY_GATE_checkpoint_P.json', 'CONTINUATION_HANDOFF_checkpoint_P.md']]
files += ['integrated_v4/' + x for x in ['frame_partition_v4.csv', 'composition_intervals_v4.csv', 'visual_event_ledger_v4.csv', 'merge_split_rulings_v4.csv', 'integration_stats_v4.json']]
files += ['v2_scripts/integrate_narration_part03_v3.py', 'v2_scripts/seal_checkpoint_P.py', 'visual_ct_scan_report_v3.md']
assert all('private' not in x.lower() for x in files)
seal = ''.join(hashlib.sha256((R / x).read_bytes()).hexdigest() + '  ' + x + '\n' for x in sorted(files))
(R / 'EVIDENCE_SHA256SUMS_checkpoint_P').write_text(seal)
for line in seal.splitlines():
    expected, name = line.split(maxsplit=1)
    assert hashlib.sha256((R / name).read_bytes()).hexdigest() == expected
mapping = {x: 'research/' + x for x in files}
mapping['EVIDENCE_SHA256SUMS_checkpoint_P'] = 'research/EVIDENCE_SHA256SUMS_checkpoint_P'
mapping['CONTINUATION_HANDOFF.md'] = 'research/CONTINUATION_HANDOFF.md'
shutil.copyfile(S / 'QUALITY_GATE_checkpoint_P.json', S / 'QUALITY_GATE_checkpoint_P_mirror.json')
mapping['session_20261104/QUALITY_GATE_checkpoint_P_mirror.json'] = 'QUALITY_GATE.json'
(R / 'publication_P.json').write_text(json.dumps(dict(message='research(visual-forensics): V006 checkpoint P 199 sampled ASR relations audited; partial CT with35-source target recovery\n', files=mapping), indent=2) + '\n')
print('Sealed P:', len(files), 'immutable text entries;', len(mapping), 'publication artifacts; NOT_CT_COMPLETE')
