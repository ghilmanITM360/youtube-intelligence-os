# Build kit-mandated derived outputs (coverage/shot/event/AV/gate) for the three videos from existing validated tables.
# Derived files only: no raw reviewer output or earlier ledger is modified. Every row cites its source table.
import csv, json, hashlib
from pathlib import Path

B = Path('/Users/ghilmankhan/YIOS-local-audits/barely-evolved'); OUT = B / 'channel_synthesis/final_audit/kit_outputs'
V = {'uPQcyookL0Y': '2026-11-02-uPQcyookL0Y-deep-ct-scan', 'mNLNb-Z4T0M': '2026-11-03-mNLNb-Z4T0M-deep-ct-scan', 'GNaBxt_zIRA': '2026-11-03-GNaBxt_zIRA-deep-ct-scan'}
val = json.loads((B / 'channel_synthesis/final_audit/FINAL_VALIDATION.json').read_text())

def w(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)

for vid, d in V.items():
    p = B / d; man = json.loads((p / 'source_manifest.json').read_text()); sha8 = man['sha256'][:8]; o = OUT / f'{vid}_{sha8}'
    v1 = vid == 'uPQcyookL0Y'
    if v1:
        # consolidate the six reviewer prompt files (89/89) into one table; raw files untouched
        rows = []
        for f in ['agents/reviewer_22/state_prompts.csv', 'agents/reviewer_23/state_prompts.csv', 'agents/reviewer_18/state_prompts_batch06.csv',
                  'agents/reviewer_19/state_prompts_batch07.csv', 'agents/reviewer_20/state_prompts_batch08.csv', 'agents/reviewer_21/state_prompts_batch09.csv']:
            for r in csv.DictReader(open(p / f)): rows.append({**r, 'source_file': f})
        assert len({r['state'] for r in rows}) == 89
        w(o / 'state_prompts_consolidated.csv', rows)
        shot_src, ev_src, av_src = 'shot_ledger_v6.csv', 'visual_event_ledger.csv', 'audio_visual_alignment_v5.csv'
    else:
        st = list(csv.DictReader(open(p / 'tables/states_v1.csv')))
        w(o / 'shot_ledger.csv', [dict(state=s['state'], start_frame=s['start'], end_frame=s['end'], start_pts_s=s['start_pts_s'], end_pts_s=s['end_pts_s'],
            duration_frames=s['frames'], boundary_candidate=s['entry'].split(':')[0], transition_class=s['entry'].split(':')[-1],
            verification='boundary montage review (agents/*boundary_01) + D1/D2/D3 measurements; Claude sonnet reviewer', source='tables/states_v1.csv') for s in st])
        ev = list(csv.DictReader(open(p / 'tables/consolidated_motion_events.csv')))
        rows = [dict(event_id=f'E{i+1:04d}', state=r['state'], start_frame=r['first_frame'], end_frame=r['last_frame'], event_class=r['event_type'],
                     observation=r['description'], evidence_ref=r['strip_path'], evidence_label=r['evidence_label'], source=f"tables/consolidated_motion_events.csv ({r['batch']})") for i, r in enumerate(ev)]
        for c in csv.DictReader(open(p / 'tables/primary_corrections.csv')):
            rows.append(dict(event_id=c['id'], state=c['state'], start_frame='', end_frame='', event_class='PRIMARY_CORRECTION:' + c['status'],
                             observation=c['primary_observation'], evidence_ref=c['path'], evidence_label='OBSERVED/MEASURED by orchestrator', source='tables/primary_corrections.csv'))
        w(o / 'visual_event_ledger.csv', rows)
        asr = list(csv.DictReader(open(p / 'asr/asr_small_en_segments.csv')))
        rows = []
        for r in csv.DictReader(open(p / 'tables/consolidated_narration_relation.csv')):
            a = asr[int(r['seg_index'])]
            rows.append(dict(phrase_id=f"ASR{int(r['seg_index']):03d}", start_s=r['asr_start_s'], end_s=r['asr_end_s'], phrase_asr=a['text'],
                method='faster-whisper small.en (provisional ASR)', audio_status='ASR_UNCERTIFIED_NOT_LISTENED', overlapping_states=r['visual_states_overlapping'],
                visual_relation=r['relation'], lag_ms='NOT_MEASURED', timing_confidence=r['timing_confidence'], assessing_batch=r['batch']))
        w(o / 'audio_visual_alignment.csv', rows)
        shot_src, ev_src, av_src = f'final_audit/kit_outputs/{o.name}/shot_ledger.csv', f'final_audit/kit_outputs/{o.name}/visual_event_ledger.csv', f'final_audit/kit_outputs/{o.name}/audio_visual_alignment.csv'
    vv = val[vid]
    cov = dict(video_id=vid, source_sha256=man['sha256'], mode_requested='CT_SCAN', mode_achieved='DEEP within declared sparse visual coverage (VISUAL_ANALYSIS_PARTIAL)',
        temporal=dict(MEASURED=f"all {vv['partition']['decoded_frames']} decoded frames (FULL_FRAME_MEASUREMENTS.csv)", states=vv['partition']['states'],
                      gaps=vv['partition']['gaps'], overlaps=vv['partition']['overlaps'], covers_all=vv['partition']['covers_all']),
        visual_review=dict(native_frames='2-5 sparse native frames per state + 8-frame motion strips at measured peaks (480x270 tiles)',
                           blind_spots='long-state interiors between sampled frames; motion outside measured peaks; strip windows truncate spans >8 frames'),
        art_states=vv['art_coverage']['states_with_art'], prompt_states=89 if v1 else vv['prompt_coverage']['states_with_prompt'],
        narration_rows=vv['narration']['rows'], audio=dict(listening='BLOCKED_CAPABILITY (no audio playback/hearing in this agent)', asr='ASR_UNCERTIFIED', audio_verified=0),
        ledgers=dict(shot=shot_src, events=ev_src, audio_visual=av_src), final_audit_utc='2026-11-04', supersedes='coverage.json kept as historical' if v1 else 'first coverage.json')
    o.mkdir(parents=True, exist_ok=True); (o / 'coverage.json').write_text(json.dumps(cov, indent=1))
    print(vid, sorted(x.name for x in o.iterdir()))
