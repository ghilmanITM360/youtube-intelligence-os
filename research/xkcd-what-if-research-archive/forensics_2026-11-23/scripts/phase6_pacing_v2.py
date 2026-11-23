"""Pacing by definition, one row per (source, format). Sources: campaign ledgers (06_ALIGNED_TIMING_TABLE.csv, 44 videos), audit measured ledgers (ledgers_measured/, 44 other videos),
Brain (MASTER_SHOTS, 14 slugs). Never pooled: detectors and unit definitions differ. Run: python3 -I scripts/phase6_pacing_v2.py"""
import csv, os, statistics as st, json
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
probe = {r['video_id']: r for r in csv.DictReader(open(A + '/media_probe_88.csv'))}
inv = {r['video_id']: r for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv'))}
def q(x):
    x = sorted(x); n = len(x)
    return (round(x[0], 2), round(st.median(x), 2), round(x[-1], 2)) if n else ('', '', '')
rows = []
camp = list(csv.DictReader(open(A + '/06_ALIGNED_TIMING_TABLE.csv')))
for fmt in ('LONG_FORM', 'SHORT'):
    s = [r for r in camp if r['format'].upper().startswith(fmt[:4])]
    rows.append(dict(source='campaign_ledgers', fmt=fmt, n_videos=len(s), shot_med=q([float(r['median_shot_s']) for r in s]), cuts_per_min=q([float(r['hard_cuts_per_min']) for r in s]),
                     event_gap_med=q([float(r['median_event_gap_s']) for r in s if r['median_event_gap_s']]), events_per_min=q([float(r['events_per_min']) for r in s])))
new = {'LONG_FORM': [], 'SHORT': []}
for v in sorted(os.listdir(A + '/ledgers_measured')):
    f = f'{A}/ledgers_measured/{v}/shot_ledger.csv'
    if not os.path.exists(f) or v not in probe: continue
    shots = list(csv.DictReader(open(f))); ev = list(csv.DictReader(open(f'{A}/ledgers_measured/{v}/visual_event_ledger.csv')))
    dur = float(probe[v]['duration']); fmt = 'SHORT' if inv[v]['format'] == 'SHORT' else 'LONG_FORM'
    sd = [float(s['duration_s']) for s in shots]; es = sorted(float(e['start_pts_seconds']) for e in ev); gaps = [b - a for a, b in zip(es, es[1:]) if b > a]
    new[fmt].append((v, st.median(sd), (len(shots) - 1) / (dur / 60), st.median(gaps) if gaps else None, len(ev) / (dur / 60)))
for fmt, L in new.items():
    rows.append(dict(source='audit_measured_ledgers', fmt=fmt, n_videos=len(L), shot_med=q([x[1] for x in L]), cuts_per_min=q([x[2] for x in L]), event_gap_med=q([x[3] for x in L if x[3]]), events_per_min=q([x[4] for x in L])))
rows.append(dict(source='brain_MASTER_SHOTS', fmt='MIXED(11 long-like, 3 odd/Short)', n_videos=14, shot_med='(200 shots) median 7.77, mean 10.54', cuts_per_min='not recorded', event_gap_med='not recorded', events_per_min='not recorded'))
w = csv.DictWriter(open(A + '/06_PACING_BY_DEFINITION.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r)
