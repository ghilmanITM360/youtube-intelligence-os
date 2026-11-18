"""Explicit topic scoring for the What-If-style channel (report 03).

Usage: python3 score_topics.py <data_dir>
Reads question_bank_63.csv + m4_demand_supply_scan_2026-11-18.tsv + xkcd_census_scored_2026-11-04.json,
writes topic_scores_2026-11-18.csv.

Inputs are labelled:
  D, G  = DERIVED from observed search data (M4 scan), with ANALYST overrides listed in D_OVERRIDE.
  C     = DERIVED from xkcd upload dates (collision with xkcd's own recent coverage).
  F,V,P = INTERPRETATION (analyst ratings 0-5), recorded per topic below; not measurements.
Weights are a proposal, not a validated model.
"""
import csv, json, sys, os
from datetime import date

W = dict(D=.25, G=.15, F=.25, C=.15, V=.10, P=.10)
SNAP = date(2026, 11, 18)

# Analyst ratings: id: (family, F format-fit, V verifiability/safety, P production-feasibility, note)
# Families: L=every-X ladder, R=runaway/escalation, S=scale/POV simulation, T=timeline/disaster, H=whole-humanity, Q=one-off calculation
A = {
 'WIB-01': ('T',5,5,4,''), 'WIB-02': ('R',4,5,4,''), 'WIB-03': ('Q',3,5,4,''),
 'WIB-04': ('T',4,4,3,'time-skip timeline'), 'WIB-05': ('Q',2,4,4,'not physics'),
 'WIB-06': ('Q',3,5,4,''), 'WIB-07': ('L',5,5,3,'ladder through periodic-table rows'),
 'WIB-08': ('H',4,5,4,''), 'WIB-09': ('R',4,5,4,''), 'WIB-10': ('R',4,4,4,'escalating-temperature timeline'),
 'WIB-11': ('T',5,5,4,'after-humans timeline (OminiAM 1.3M, Astrum 4M)'), 'WIB-12': ('Q',3,3,4,'firearms'),
 'WIB-13': ('R',5,5,5,'runaway per-second format'), 'WIB-14': ('Q',3,5,4,''),
 'WIB-15': ('L',5,5,4,'every-location ladder'), 'WIB-16': ('Q',2,5,3,''),
 'WIB-17': ('S',4,5,4,''), 'WIB-18': ('L',5,5,4,'drop-height ladder'), 'WIB-19': ('Q',2,5,3,''),
 'WIB-20': ('Q',2,3,3,'medical claims'), 'WIB-21': ('Q',3,5,4,''),
 'WIB-22': ('L',5,4,4,'light-year distance ladder'), 'WIB-23': ('T',4,4,4,''),
 'WIB-24': ('L',5,5,4,'every-planet ladder'), 'WIB-25': ('Q',1,3,3,'EXCLUDE: fictional IP'),
 'WIB-26': ('Q',2,4,3,''), 'WIB-27': ('Q',3,5,4,''), 'WIB-28': ('H',4,5,4,''),
 'WIB-29': ('Q',1,2,2,'EXCLUDE: sensitive'), 'WIB-30': ('L',4,5,4,'throw on every planet'),
 'WIB-31': ('S',4,5,4,'distance ladder'), 'WIB-32': ('L',5,5,4,'speed ladder'),
 'WIB-33': ('T',3,4,3,''), 'WIB-34': ('Q',3,5,4,''), 'WIB-35': ('Q',2,5,3,''),
 'WIB-36': ('L',5,5,4,'altitude ladder'), 'WIB-37': ('Q',2,3,3,'EXCLUDE: weapons/violence'),
 'WIB-38': ('T',5,5,4,''), 'WIB-39': ('T',4,5,4,''), 'WIB-40': ('Q',2,5,3,''),
 'WIB-41': ('Q',3,5,4,''), 'WIB-42': ('Q',3,5,4,''), 'WIB-43': ('Q',1,4,3,''),
 'WIB-44': ('R',5,5,4,'runaway per-second format'), 'WIB-45': ('Q',2,5,4,''),
 'WIB-46': ('T',5,5,4,''), 'WIB-47': ('Q',3,5,4,''), 'WIB-48': ('T',3,4,3,''),
 'WIB-49': ('Q',2,4,3,''), 'WIB-50': ('Q',2,5,3,''), 'WIB-51': ('Q',4,5,4,''),
 'WIB-52': ('Q',3,5,3,''), 'WIB-53': ('Q',3,5,4,''), 'WIB-54': ('Q',1,5,3,''),
 'WIB-55': ('S',4,5,4,''), 'WIB-56': ('L',5,5,4,'magnitude ladder'),
 'WIB-SA1': ('Q',2,4,3,''), 'WIB-SA2': ('Q',4,5,4,'adjacent to fresh xkcd nuke video'),
 'WIB-SA3': ('Q',2,5,3,''), 'WIB-SA4': ('Q',2,5,3,''), 'WIB-SA5': ('R',3,5,4,''),
 'WIB-SA6': ('S',3,5,4,''), 'WIB-SA7': ('Q',1,1,2,'EXCLUDE: explosives'),
 'NEW-01': ('S',5,5,4,'crowded'), 'NEW-02': ('L',5,5,4,'Lightbound/D.A did it'), 'NEW-03': ('S',4,5,4,''),
 'NEW-04': ('H',3,3,3,'biology speculation'), 'NEW-05': ('R',4,5,4,''), 'NEW-06': ('T',4,5,4,''),
 'NEW-07': ('S',5,5,4,'Kian Odyssey 356K recent'), 'NEW-08': ('R',5,5,4,'WhatIfAnimations 433K'),
 'NEW-09': ('T',3,4,3,''), 'NEW-10': ('S',4,5,4,''), 'NEW-11': ('L',4,5,4,'mountain on every planet'),
 'NEW-12': ('L',4,5,4,'xkcd made digging video 7mo ago'),
}
NEW_LABEL = {'NEW-01':'Fall into a black hole','NEW-02':'Sun seen from every planet','NEW-03':'Earth with rings',
 'NEW-04':'Humans live 1000 years','NEW-05':'Gravity doubles','NEW-06':'Moon disappears','NEW-07':'Fall into Jupiter',
 'NEW-08':'Slower speed of light','NEW-09':'Oxygen doubles','NEW-10':'Hollow Earth','NEW-11':'Tallest possible mountain',
 'NEW-12':'Deepest possible hole'}
# Analyst corrections where the title regex still admitted off-topic hits (see report 03 §M4 caveats)
D_OVERRIDE = {'WIB-12':2,'WIB-26':1,'WIB-54':1,'WIB-SA1':1,'WIB-SA3':2,'WIB-SA5':0,'WIB-07':2,'WIB-41':3,
              'WIB-32':3,'WIB-04':1,'WIB-05':2,'WIB-49':2,'WIB-17':4}
C_OVERRIDE = {'WIB-SA2':2,'NEW-12':0,'NEW-06':4}

def views(s): return float(s.rstrip('K'))*1e3 if s else 0
def d_score(v): return 5 if v>=20e6 else 4 if v>=8e6 else 3 if v>=3e6 else 2 if v>=1e6 else 1 if v>=2e5 else 0
def g_score(n, recent):
    g = 5 if n<=1 else 4 if n<=3 else 3 if n<=5 else 2 if n<=8 else 1 if n<=11 else 0
    return max(0, g-1) if recent>=3 else g

def main(d):
    m4 = {}
    for line in open(os.path.join(d,'m4_demand_supply_scan_2026-11-18.tsv')):
        if line.startswith('#') or line.startswith('id|'): continue
        f = line.rstrip('\n').split('|'); m4[f[0]] = f
    cen = {r['video_id']: r for r in json.load(open(os.path.join(d,'xkcd_census_scored_2026-11-04.json')))}
    extra = {'rGZ6TsXvi8E':'2026-08-18'}  # Short published after the census snapshot (from RSS / bank)
    bank = {x['bank_id']: x for x in csv.DictReader(open(os.path.join(d,'question_bank_63.csv')))}
    out = []
    for tid, (fam, F, V, P, note) in A.items():
        b = bank.get(tid, {}); r = m4.get(tid)
        D = D_OVERRIDE.get(tid, d_score(views(r[4])) if r else 0)
        G = g_score(int(r[2]), int(r[3])) if r else 0
        if tid in C_OVERRIDE: C = C_OVERRIDE[tid]
        elif b.get('xkcd_video_status') == 'MADE':
            ids = b['xkcd_video_ids'].replace(';',' ').split()
            last = max(date.fromisoformat(cen[i]['published'] if i in cen else extra[i]) for i in ids)
            C = 0 if (SNAP-last).days <= 365 else 1
        else: C = 5
        excl = note.startswith('EXCLUDE')
        total = 0 if excl else round(20*sum(W[k]*v for k,v in dict(D=D,G=G,F=F,C=C,V=V,P=P).items()),1)
        out.append(dict(id=tid, topic=b.get('unit', NEW_LABEL.get(tid,'')), xkcd=b.get('xkcd_video_status','NEW'),
            family=fam, D=D, G=G, F=F, C=C, V=V, P=P, score=total, m4_grade=r[6] if r else '',
            d_overridden=tid in D_OVERRIDE, note=note))
    out.sort(key=lambda x: -x['score'])
    with open(os.path.join(d,'topic_scores_2026-11-18.csv'),'w',newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    return out

if __name__ == '__main__':
    rows = main(sys.argv[1])
    assert len(rows) == 75 and all(0 <= r['score'] <= 100 for r in rows)
    assert all(r['score'] == 0 for r in rows if r['note'].startswith('EXCLUDE'))
    for r in rows[:30]: print(r['score'], r['id'], r['topic'], r['xkcd'], r['family'], 'D%d G%d F%d C%d V%d P%d' % tuple(r[k] for k in 'DGFCVP'), r['m4_grade'], '*' if r['d_overridden'] else '')
