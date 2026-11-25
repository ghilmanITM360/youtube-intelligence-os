"""Phase 6 reconciliation: one definition-aligned timing table for every campaign video that has a
shot ledger + visual event ledger + ASR word timestamps. Read-only on the repo.
Definitions (all MEASURED from existing campaign tables, nothing new is perceived):
  shot            = row of shot_ledger.csv (hard-cut span)
  visual event    = row of visual_event_ledger.csv (onset measured from frame differences)
  event gap       = difference between consecutive event start times (campaign calls this a "hold")
  narration pace  = ASR words / (last word end - first word start)  [ASR_UNCERTIFIED, NOT listening]
  pause           = gap between consecutive ASR words >= 0.35 s
"""
import csv, json, statistics as st
from pathlib import Path
C = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww')
OUT = Path(__file__).resolve().parent.parent
mat = {r['video_id']: r for r in csv.DictReader(open(C / 'campaign/campaign_matrix.csv'))}
cen = {r['video_id']: r for r in csv.DictReader(open(C / 'census/census.csv'))}
def med(x): return round(st.median(x), 2) if x else ''
rows = []
for d in sorted((C / 'videos').iterdir()):
    vid = d.name
    sl, ev, asr = d / 'shot_ledger.csv', d / 'visual_event_ledger.csv', d / 'asr/asr_small_en.json'
    if not (sl.exists() and ev.exists()): continue
    shots = list(csv.DictReader(open(sl))); events = list(csv.DictReader(open(ev)))
    dur = float(cen[vid]['duration_s']) if vid in cen else float(shots[-1]['end_pts_seconds'])
    sd = [float(s['end_pts_seconds']) - float(s['start_pts_seconds']) for s in shots]
    es = sorted(float(e['start_pts_seconds']) for e in events)
    gaps = [b - a for a, b in zip(es, es[1:]) if b > a]
    r = dict(video_id=vid, format=mat[vid]['format'], role=mat[vid]['role'], duration_s=round(dur, 1), shots=len(shots),
             hard_cuts_per_min=round((len(shots) - 1) / (dur / 60), 2), median_shot_s=med(sd), events=len(events),
             events_per_min=round(len(events) / (dur / 60), 1), median_event_gap_s=med(gaps), first_event_s=round(es[0], 2) if es else '')
    if asr.exists():
        a = json.loads(asr.read_text()); W = a.get('words') or []
        if W:
            ws = [(w['start'], w['end']) for w in W]
            span = ws[-1][1] - ws[0][0]
            pz = [b[0] - a_[1] for a_, b in zip(ws, ws[1:]) if b[0] - a_[1] >= .35]
            r.update(asr_words=len(W), asr_pace_wps=round(len(W) / span, 2), asr_first_word_s=round(ws[0][0], 2),
                     pauses_per_min=round(len(pz) / (dur / 60), 1), median_pause_s=med(pz),
                     events_per_100_words=round(100 * len(events) / len(W), 1), words_per_shot=round(len(W) / len(shots), 1))
    rows.append(r)
keys = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
with open(OUT / '06_ALIGNED_TIMING_TABLE.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
print('videos with ledgers', len(rows))
for fmt in ('LONG_FORM', 'SHORT_FORM', 'SHORT'):
    S = [r for r in rows if r['format'] == fmt]
    if not S: continue
    g = lambda k: [r[k] for r in S if r.get(k) not in (None, '')]
    print(fmt, 'n', len(S))
    for k in ('duration_s', 'hard_cuts_per_min', 'median_shot_s', 'events_per_min', 'median_event_gap_s', 'asr_pace_wps', 'pauses_per_min', 'median_pause_s', 'events_per_100_words', 'words_per_shot', 'first_event_s', 'asr_first_word_s'):
        x = g(k)
        if x: print(f'  {k:22s} n={len(x)} median={med(x)} min={min(x)} max={max(x)}')
print('formats', {r['format'] for r in rows})
