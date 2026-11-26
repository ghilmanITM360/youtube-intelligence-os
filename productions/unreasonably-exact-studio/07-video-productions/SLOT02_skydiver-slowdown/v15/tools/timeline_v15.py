"""timeline/V15_TIMELINE.json: editable timeline (shots in V15 film time, the warp, narration, sound cues). Run from v15/ after the mix."""
import csv, json, sys
from pathlib import Path
sys.argv = [sys.argv[0]]
ROOT = Path(__file__).resolve().parents[1]
ns = {'__file__': str(Path(__file__).with_name('v15.py')), '__name__': 'tl'}
exec(open(Path(__file__).with_name('v15.py')).read(), ns)
unwarp, FPS, DUR = ns['unwarp'], ns['FPS'], ns['DUR']
NARR = json.loads((ROOT / 'audio/narration_v14.json').read_text())
shots = []
for sid, a, b, kind, purpose in ns['SHOTS']:
    s, e = (0.0 if a == 0 else unwarp(a)), (DUR if b >= 78.2 else unwarp(b))
    words = [q['text'] for q in NARR['cues'] if q['speech_start'] < e and q['speech_end'] > s]
    shots.append(dict(id=sid, kind=kind, purpose=purpose, start=round(s, 3), end=round(e, 3), start_frame=round(s * FPS), end_frame=round(e * FPS),
                      duration=round(e - s, 3), v13_design_start=a, v13_design_end=b, narration=words))
for x, y in zip(shots, shots[1:]): assert x['end_frame'] == y['start_frame']
(ROOT / 'timeline/V15_TIMELINE.json').write_text(json.dumps(dict(
    title='Why Can a Skydiver Slow Down Without a Parachute? (V15 final, Hamza narration)', fps=FPS, width=1080, height=1920,
    duration=DUR, frames=round(DUR * FPS),
    how_to_edit='Shot drawing code: tools/v15_shots.py (times there are V13 design seconds). Timing: audio/warp.json (V15 film time -> design time), '
                'rebuilt by tools/align_v14.py from word matches; add an EVENTS entry there to pin a reveal to a word. Render: tools/v15.py.',
    narration=dict(file='HAMZA_VOICEOVER_CLEAN.wav', starts_at=NARR['vo_at'], words='WORD_LEVEL_TIMESTAMPS.json', sentences=NARR['sentences']),
    captions=dict(srt='SKYDIVER_SLOWDOWN_FINAL_V15.srt', cues=[{k: q[k] for k in ('text', 'start', 'end')} for q in NARR['cues']]),
    warp=json.loads((ROOT / 'audio/warp.json').read_text()),
    shots=shots,
    sound=dict(mix='audio/V15_mix.wav', stems='audio/stems/', cues=list(csv.DictReader(open(ROOT / 'SOUND_DESIGN_CUE_SHEET.csv')))),
    sync_map='NARRATION_VISUAL_SYNC_MAP.csv'), indent=1))
for s in shots: print(f"{s['id']:3} {s['start']:7.2f} {s['end']:7.2f} {s['duration']:5.2f}  {s['kind']}")
