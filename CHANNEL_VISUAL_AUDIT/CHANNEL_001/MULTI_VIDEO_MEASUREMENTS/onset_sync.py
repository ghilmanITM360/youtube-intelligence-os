"""Visual-state boundaries vs ASR word onsets / word ends (internal timing reference). Whisper base word times; 10nE uses small_en."""
import an, json, os, sys, numpy as np, subprocess
H = os.path.expanduser('~/YIOS-local-audits/')
def bounds(p):
    W, Hh = 216, 384
    pr = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-i', p, '-vf', f'fps=6,scale={W}:{Hh}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    fs = []
    while True:
        b = pr.stdout.read(W * Hh * 3)
        if len(b) < W * Hh * 3: break
        fs.append(np.abs(np.frombuffer(b, np.uint8).reshape(Hh, W, 3).astype(np.int16) - 253).sum(-1) > 60)
    bd, a = [], 0
    for i in range(1, len(fs)):
        u = (fs[a] | fs[i]).sum()
        if u and (fs[a] & fs[i]).sum() / u < .8: bd.append(i / 6); a = i
    return np.array(bd), len(fs) / 6
def words(v):
    f = H + '2026-11-08-10nEByVLya0-deep-ct-scan/audio/10nEByVLya0_small_en.json' if v.startswith('10nE') else H + f'CF_TRANSCRIPTS_ASR_20261109/transcripts/{v}.json'
    w = [x for s in json.load(open(f))['segments'] for x in s['words']]
    return np.array([x['start'] for x in w]), np.array([x['end'] for x in w])
for v in sys.argv[1:]:
    b, dur = bounds(an.find(v)); st, en = words(v); rs = np.random.RandomState(0).uniform(0, dur, 5000)
    out = []
    for nm, pts in (('onset', st), ('end', en)):
        d = lambda x: np.abs(x[:, None] - pts[None]).min(1); r, q = d(b), d(rs)
        out.append('%s med %.2f/%.2f in0.1s %.2f/%.2f' % (nm, np.median(r), np.median(q), (r < .1).mean(), (q < .1).mean()))
    print(v, len(b), 'words', len(st), '|', ' | '.join(out), flush=True)
