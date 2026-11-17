# pairs from on-screen text: for each state whose visible_text has a content word also spoken within +-2.5 s, pair the
# state onset with the nearest raw ASR token of that word; drop |lag| > 1.5 s. usage: pairs_example_7k99.py WS VIDEO_ID FPS
import json, sys, re
ws, vid, FPS = sys.argv[1], sys.argv[2], float(sys.argv[3])
sys.path.insert(0, f'{ws}/build'); from states_data import D
a = json.load(open(f'{ws}/audio/{vid}_small_en.json'))
W = [(x['start'], x['word'].strip()) for s in a['segments'] for x in s['words']]
norm = lambda w: re.sub(r"[^a-z0-9$%.']", '', w.lower()).strip(".'")
STOP = set('the and that this what with from have here they your about more just over into some only for not all its it\'s'.split())
out, dropped = [], []
for d in D:
    f, txt = d[0], d[4]
    if txt == 'none': continue
    t0 = f / FPS; words = [norm(x) for x in re.split(r'[\s;:,/>()!?]+', txt)]
    words = [w for w in words if len(w) >= 4 and w not in STOP]
    c = sorted([(abs(t - t0), t, raw) for t, raw in W if norm(raw) in words and abs(t - t0) <= 2.5])
    if not c: dropped.append((f, 'noword')); continue
    _, t, raw = c[0]; out.append([f, raw, round(t, 2)])
keep = [o for o in out if abs(o[0] / FPS - o[2]) <= 1.5]; far = [(o[0], o[1], round(o[0] / FPS - o[2], 2)) for o in out if abs(o[0] / FPS - o[2]) > 1.5]
json.dump(keep, open(f'{ws}/build/phrase_pairs.json', 'w'))
lags = sorted(round(f / FPS - t, 3) for f, w, t in keep)
print('text states', len(out) + len(dropped), 'matched', len(out), 'kept', len(keep), 'noword', len(dropped), 'dropped-lag>1.5', far)
print('lag min/median/max', lags[0], lags[len(lags) // 2], lags[-1], 'early', sum(l < 0 for l in lags), 'late', sum(l > 0 for l in lags), 'within0.3', sum(abs(l) <= 0.3 for l in lags))
