"""Held-out validation of measured ledgers against the campaign's visually reviewed ledgers (videos NOT used for tuning)."""
import csv, sys, statistics as st
sys.path.insert(0, '.')
from pathlib import Path
import ledger_lib as L
from ledger_tune import campaign, match
C = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww')
OUT = Path(__file__).resolve().parent.parent
T = {r['video_id']: r for r in csv.DictReader(open(OUT / '06_ALIGNED_TIMING_TABLE.csv'))}
TUNE = {'-1-ldW4kpLM', '2LSyizrk8-0', '4ZVtHknKuvg', '2p305nzcVQE', '35KZm1yiyIE'}
rows = []
for v, r in T.items():
    if v == '8fADp43wJwU': continue  # deep pass used a different encode
    m = L.measure(L.media(v)); cuts, ev = L.segments(m); csh, cev = campaign(v); es = [e['start_frame'] for e in ev]
    shots_m = len(cuts) + 1; shots_c = len(csh) + 1
    rows.append(dict(video_id=v, fmt='LONG' if r['format'] == 'LONG_FORM' else 'SHORT', split='TUNE' if v in TUNE else 'HELDOUT',
        shots_campaign=shots_c, shots_measured=shots_m, cut_hit=match(csh, cuts, 2), events_campaign=len(cev), events_measured=len(es), event_hit=match(cev, es, 3),
        median_shot_campaign=r['median_shot_s'], median_shot_measured=round(st.median([(b - a) / m['fps'] for a, b in zip([0] + cuts, cuts + [m['n']])]), 2)))
    print(v, flush=True)
with open(OUT / 'ledgers_measured_validation_vs_campaign.csv', 'w', newline='') as o:
    w = csv.DictWriter(o, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for sp in ('HELDOUT', 'TUNE'):
    for fm in ('LONG', 'SHORT', None):
        R = [r for r in rows if r['split'] == sp and (fm is None or r['fmt'] == fm)]
        if not R: continue
        a = lambda k: sum(r[k] for r in R)
        print(sp, fm or 'ALL', len(R), 'videos | shot boundaries: campaign', a('shots_campaign') - len(R), 'measured', a('shots_measured') - len(R), 'hit', a('cut_hit'),
              f"P={a('cut_hit')/max(a('shots_measured')-len(R),1):.2f} R={a('cut_hit')/max(a('shots_campaign')-len(R),1):.2f} | events: campaign", a('events_campaign'), 'measured', a('events_measured'), 'hit', a('event_hit'),
              f"P={a('event_hit')/max(a('events_measured'),1):.2f} R={a('event_hit')/max(a('events_campaign'),1):.2f}")
