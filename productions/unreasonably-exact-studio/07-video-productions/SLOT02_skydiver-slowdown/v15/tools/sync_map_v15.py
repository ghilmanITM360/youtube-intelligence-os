"""V15 narration -> picture sync map (V15 events: x8 lens, net-force arrow on the body). For each line of the brief's table: where Hamza says it (word timings) and
where the matching visual event lands after the warp (V13 design time -> V15 film time).
Writes NARRATION_VISUAL_SYNC_MAP.csv. Run from v15/: .venv/bin/python tools/sync_map_v15.py
offset_s = event time - onset of the key word. status: ok | early (event > 0.30 s before the phrase starts) |
late (event > 1.0 s after the key word ends)."""
import csv, json, re, sys
from pathlib import Path
sys.argv = [sys.argv[0]]
sys.path.insert(0, str(Path(__file__).parent))
ROOT = Path(__file__).resolve().parents[1]
ns = {'__file__': str(Path(__file__).with_name('v15.py')), '__name__': 'sync'}
exec(open(Path(__file__).with_name('v15.py')).read(), ns)
WORDS = json.loads((ROOT / 'WORD_LEVEL_TIMESTAMPS.json').read_text())['words']
def norm(w): return re.sub(r"[^a-z0-9']", '', w.lower())

# (phrase as spoken, key word, V13 design time of the visual event, visual event, shot)
ROWS = [
 ("You're falling from 10 kilometers above the ground", 'falling', 0.0, 'Aircraft upper-middle and the falling figure below it, ground far below (establish)', 'A1'),
 ("You're falling from 10 kilometers above the ground", 'ground', 1.10, 'Camera starts to follow the figure down (tilt); depth layers separate', 'A1'),
 ('Your parachute is still closed', 'parachute', 3.30, 'Cut behind the faller: closed pack on the back', 'A2'),
 ('Your parachute is still closed', 'closed', 3.75, 'Closed pack circled, "parachute: closed"', 'A2'),
 ('Gravity is still pulling you down', 'gravity', 5.50, 'Weight arrow draws down from the centre of mass, "gravity"', 'B1'),
 ("And somehow, you're slowing down", 'somehow', 8.33, 'Forearm lifts, head turns to the wrist', 'B2'),
 ("And somehow, you're slowing down", 'slowing', 9.70, 'Cut to the wrist instrument; needle eases down', 'B3'),
 ('Wait, what?', 'wait', 11.15, 'Reaction: head snaps up from the wrist, blink, push on the face', 'C1'),
 ('Did gravity change its mind?', 'gravity', 12.90, 'Weight arrow re-measured against a fixed tick: "same"', 'D1'),
 ('Did the air suddenly grow brakes?', 'air', 14.40, 'Gust of air streaks past the body (air resistance idea)', 'D1'),
 ('Imagine the fall, starting from rest', 'imagine', 20.92, 'Model reset: world stills, MODEL frame draws in', 'F1'),
 ('Imagine the fall, starting from rest', 'rest', 21.85, '"starts at rest · fixed posture", altitude ruler at 10 km, speed zero', 'F1'),
 ('Up here, the air is thin', 'thin', 23.20, 'Thin-air box (sparse dots)', 'G1'),
 ('At first, gravity wins', 'gravity', 24.95, 'Weight arrow long, drag arrow short', 'H1'),
 ('You keep going faster', 'faster', 26.70, 'Speed arrow grows; streaks speed up', 'H1'),
 ("But as you fall, you're entering denser air", 'denser', 29.20, 'Second box fills: denser air (more dots)', 'I1'),
 ('The air pushes against you', 'pushes', 33.80, 'Upward drag arrow on the body ("same air · same posture")', 'J1'),
 ('and the faster you fall', 'faster', 34.95, 'Speed sweeps x1 -> x2; streaks speed up', 'J1'),
 ('the harder it pushes back', 'harder', 37.35, 'Drag arrow, growing with speed squared through both phrases, reaches x4 at speed x2', 'J1'),
 ('where your body position stays fixed', 'fixed', 41.00, '"posture: fixed" under the steady body', 'K1'),
 ('can actually become stronger than your weight', 'stronger', 43.75, 'Drag bar passes the weight line; excess turns violet', 'K1'),
 ('can actually become stronger than your weight', 'weight', 44.10, 'x8 lens opens on the bar tops; violet difference = net force', 'K1'),
 ("You're still moving down", 'moving', 47.90, 'Descending trail; dashed speed arrow points down', 'L1'),
 ('But the net force is now pointing up', 'net', 49.50, 'Violet net-force arrow points up beside the newest mark', 'L1'),
 ('So the downward speeds start to decrease', 'downward', 52.60, 'Speed arrow shortens, "slower"', 'M1'),
 ('The speedometer drops', 'speedometer', 55.35, 'First-person wrist: needle falls along the scale', 'N1'),
 ('the ground gets closer', 'ground', 57.16, 'Tilt from the wrist to the approaching ground', 'O1'),
 ('And your parachute is still closed', 'closed', 59.35, 'Behind the faller: pack still closed', 'P1'),
 ("That's the strange part", 'strange', 61.93, 'Speed-time graph builds: axes, rise, top speed', 'Q1'),
 ("Slowing down doesn't mean you have stopped falling", 'stopped', 64.05, 'Curve falls but stays above zero: "not zero" bracket', 'Q1'),
 ('It means the air is pushing back, harder than gravity', 'pushing', 66.20, 'Force bars again: drag slightly above weight; x8 lens and violet net-force arrow follow', 'Q2'),
 ('this is a model', 'model', 70.95, 'Model graph draws in inside the MODEL frame; assumptions line', 'R1'),
 ('Change the posture or the conditions', 'posture', 75.20, 'Alternative outcome: smaller drag area curve', 'S1'),
 ('Change the posture or the conditions', 'conditions', 76.00, 'Alternative outcome: larger drag area curve', 'S1'),
]
def find(phrase, after):
    p = [norm(w) for w in phrase.split()]
    seq = [norm(w['word']) for w in WORDS]
    for i in range(after, len(seq) - len(p) + 1):
        if seq[i:i + len(p)] == p: return i
    raise SystemExit(f'not found: {phrase}')
out, pos, bad = [], 0, 0
for phrase, key, t13, what, shot in ROWS:
    i = find(phrase, pos); pos = i
    k = next(j for j in range(i, i + len(phrase.split())) if norm(WORDS[j]['word']) == key)
    p0, p1 = WORDS[i]['start'], WORDS[i + len(phrase.split()) - 1]['end']
    ev = ns['unwarp'](t13) if t13 > 0 else 0.0
    off = ev - WORDS[k]['start']
    st = 'ok'
    if ev < p0 - .30 and t13 > 0: st = 'early'
    if ev > WORDS[k]['end'] + 1.0: st = 'late'
    bad += st != 'ok'
    out.append(dict(phrase=phrase, phrase_start=round(p0, 2), phrase_end=round(p1, 2), key_word=WORDS[k]['word'], key_start=WORDS[k]['start'],
                    key_end=WORDS[k]['end'], visual_event=what, shot=shot, v13_design_time=t13, v15_event_time=round(ev, 3),
                    v15_event_frame=round(ev * 24), offset_s=round(off, 2), status=st))
with open(ROOT / 'NARRATION_VISUAL_SYNC_MAP.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, list(out[0])); w.writeheader(); w.writerows(out)
for r in out: print(f"{r['status']:5} {r['key_start']:7.2f} {r['v15_event_time']:7.2f} {r['offset_s']:+5.2f}  {r['key_word']:12} {r['visual_event'][:60]}")
print(len(out), 'rows,', bad, 'flagged')
