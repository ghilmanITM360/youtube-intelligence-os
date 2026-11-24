"""Phase 9 (no listening available): (1) machine alignment of ASR segments with measured visual events for all 88 videos (campaign ledgers for 44, audit ledgers for 44),
(2) a timestamped listening and synchronisation review pack for a human listener. Nothing here is listening: ASR timing is provisional (whisper small.en), loudness is machine-measured.
Outputs: 09_AV_ALIGNMENT_ALL88.csv (per video summary), 09_LISTENING_REVIEW_PACK.csv (per ASR segment), 09_LISTENING_REVIEW_PROTOCOL.md is written by hand. Run: python3 -I scripts/phase9_listening_pack.py"""
import csv, json, os, statistics as st, bisect
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = '/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/videos/'
inv = {r['video_id']: r for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv'))}
lev = {r['video_id']: r for r in csv.DictReader(open(A + '/09_AUDIO_LEVELS_88.csv'))}
def segs(v):
    for d, s in (('phase7b_asr', 'audit_7b'), ('phase7c_asr', 'audit_7c')):
        f = f'{A}/{d}/{v}.json'
        if os.path.exists(f): return s, [(x['offsets']['from'] / 1000, x['offsets']['to'] / 1000, x['text'].strip()) for x in json.load(open(f))['transcription']]
    j = json.load(open(f'{V}{v}/asr/asr_small_en.json')); return 'campaign', [(x['start'], x['end'], x['text'].strip()) for x in j['segments']]
def ledger(v):
    for base in (f'{V}{v}', f'{A}/ledgers_measured/{v}'):
        if os.path.exists(base + '/shot_ledger.csv') and os.path.exists(base + '/visual_event_ledger.csv'):
            sh = [(float(r['start_pts_seconds']), float(r['end_pts_seconds']), r['shot_id']) for r in csv.DictReader(open(base + '/shot_ledger.csv'))]
            ev = sorted(float(r['start_pts_seconds']) for r in csv.DictReader(open(base + '/visual_event_ledger.csv')))
            return ('campaign' if base.startswith(V) else 'audit'), sh, ev
    return None
pack, summ = [], []
for v, r in inv.items():
    if r['local_media_status'] == 'MISSING': continue
    src, sg = segs(v); led = ledger(v)
    if not led: continue
    lsrc, sh, ev = led; deltas = []; prev_end = 0.0
    for i, (a, b, t) in enumerate(sg, 1):
        k = bisect.bisect_left(ev, a); cand = [ev[j] for j in (k - 1, k) if 0 <= j < len(ev)]
        ne = min(cand, key=lambda x: abs(x - a)) if cand else None; d = round(ne - a, 2) if ne is not None else ''
        if d != '': deltas.append(abs(d))
        shot = next((s[2] for s in sh if s[0] <= a < s[1]), ''); cuts = sum(1 for s in sh if a < s[0] < b)
        pause = round(a - prev_end, 2); prev_end = b
        flag = []
        if d != '' and abs(d) > 1.0: flag.append('NEAREST_EVENT_GT_1S')
        if pause >= 1.0: flag.append('PAUSE_GE_1S')
        if cuts >= 2: flag.append('MULTI_CUT_SEGMENT')
        pack.append(dict(video_id=v, fmt=r['format'], seg_no=i, seg_start_s=round(a, 2), seg_end_s=round(b, 2), asr_text=t, nearest_event_s=round(ne, 2) if ne is not None else '', event_minus_seg_start_s=d,
                         shot_at_seg_start=shot, cuts_inside_segment=cuts, pause_before_s=pause, machine_flags=';'.join(flag), asr_source=src, ledger_source=lsrc,
                         listening_status='UNREVIEWED_NO_LISTENING', listener_verdict='', listener_notes=''))
    wl = lev[v]
    summ.append(dict(video_id=v, fmt=r['format'], ledger_source=lsrc, asr_source=src, segments=len(sg), median_abs_nearest_event_s=round(st.median(deltas), 2) if deltas else '',
                     share_within_0p5s=round(sum(x <= .5 for x in deltas) / len(deltas), 2) if deltas else '', share_within_1s=round(sum(x <= 1 for x in deltas) / len(deltas), 2) if deltas else '',
                     lufs=wl.get('integrated_lufs', wl.get('lufs', '')), status='MACHINE_PROVISIONAL_NOT_LISTENED'))
for name, rows in (('09_LISTENING_REVIEW_PACK.csv', pack), ('09_AV_ALIGNMENT_ALL88.csv', summ)):
    w = csv.DictWriter(open(A + '/' + name, 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(summ), 'videos', len(pack), 'segments', sum(1 for p in pack if p['machine_flags']), 'flagged')
for f in ('LONG_FORM', 'SHORT'):
    for s in ('campaign', 'audit'):
        x = [r for r in summ if r['fmt'] == f and r['ledger_source'] == s and r['median_abs_nearest_event_s'] != '']
        print(f, s, len(x), 'median of per-video median |delta|', round(st.median(r['median_abs_nearest_event_s'] for r in x), 2), 'within0.5', round(st.median(r['share_within_0p5s'] for r in x), 2), 'within1', round(st.median(r['share_within_1s'] for r in x), 2))
print(list(lev[next(iter(lev))].keys()))
