"""Sound design V3: Small_Variables.mp3 becomes the music bed; the V2 synthesised SFX library is pruned and retuned to the track's key.

Music (supplied by the owner, RIGHTS UNVERIFIED: no metadata in the file):
  * measured 134.98 BPM (4 bars = 7.112 s, from self-similarity), estimated key F major (chroma vs Krumhansl profiles, r = 0.77);
  * the film is 96.0 s, the track 91.27 s: track bars 48.47-55.58 s are played twice (seam chosen by spectral self-similarity,
    40 ms equal-power crossfade). Before the seam film time = track time, so the track's own 31 s break lands on "But hold on" and
    its 36-40 s breakdown on "mirror ... Actually, yes"; after it the 72 s breakdown lands on "So how does it work?" and the outro
    under the last line;
  * automation map (narrative), dialogue ducking, a 1-4 kHz anti-masking dip while the voice speaks, then one calibration trim so
    the music sits MUSIC_BELOW_VOICE dB under the narration in voiced windows of the main explanation (K-weighted RMS).
SFX: V2 library regenerated with pitched accents moved into F major; cues cut where the music already carries the emotion.
Outputs (renders/roughcut_v3/): stems/*.wav, final_mix_v3_review_music.wav (PRIVATE REVIEW: contains the unverified track),
final_mix_v3_rights_clear.wav (no supplied music), SLOT07_V3_mix_report.json, MUSIC_AUTOMATION_MAP.csv, SOUND_DESIGN_CUE_SHEET.csv
"""
import csv, json, os, re, subprocess, sys, wave
import numpy as np
from scipy.signal import butter, sosfilt, lfilter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(ROOT, 'animation'))
from uemotion.narration import MASTER_WAV, NAR
from proofs import opening as OP, p09, p11, p06, gaps as G
SR = 48000; DUR = 96.0; N = int(SR * DUR); rng = np.random.default_rng(2026)
MUSIC_SRC = os.path.join(ROOT, 'audio', 'music', 'Small_Variables.mp3')   # inside the project since the 2026-11-26 consolidation (was ../Small_Variables.mp3); same bytes, sha256 f781c977...
SEAM_B0, SEAM_LEN, SEAM_XF = 48.47, 7.112, 0.040
MUSIC_BELOW_VOICE = 21.0                       # target, dB (brief: 18-24 dB under narration in voiced windows)
OUT = os.path.join(ROOT, 'renders', 'roughcut_v3'); LIB = os.path.join(ROOT, 'audio', 'sfx_v3')
BEAT, BEAT0 = 60 / 134.98, 0.058
def db(x): return 10 ** (x / 20)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'band', fs=SR, output='sos'), x, axis=-1)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x, axis=-1)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x, axis=-1)
def tt(d): return np.arange(int(SR * d)) / SR
def norm(x, peak_db=-6): return x / (np.abs(x).max() + 1e-12) * db(peak_db)
def write(p, x):
    """mono (n,) or stereo (2, n) -> 16-bit wav"""
    os.makedirs(os.path.dirname(p), exist_ok=True); x = np.atleast_2d(x)
    with wave.open(p, 'wb') as w:
        w.setnchannels(x.shape[0]); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(x.T, -1, 1) * 32767).astype(np.int16).tobytes())
def read(p, ch=1):
    out = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', str(ch), '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    a = np.frombuffer(out, np.float32).astype(np.float64); return a.reshape(-1, ch).T if ch > 1 else a

# ============================================================ SFX library (V2 sounds; pitched ones retuned to F major)
def tone(f, d, dec=0.6, partials=((1, 1.0), (2.01, 0.25), (3.0, 0.08)), a=0.005):
    t = tt(d); e = np.exp(-t / dec) * np.clip(t / a, 0, 1)
    return sum(g * np.sin(2 * np.pi * f * m * t) for m, g in partials) * e
F3, A3, C4, F4, G4, A4, C5, D5, F5, G5, A5, C6 = 174.61, 220.0, 261.63, 349.23, 392.0, 440.0, 523.25, 587.33, 698.46, 783.99, 880.0, 1046.5
def adsr(d, a=0.01, r=0.3): t = tt(d); return np.clip(t / a, 0, 1) * np.clip((d - t) / r, 0, 1)
def lib():
    L = {}
    t = tt(8.5)                                                              # rights-clear version only: the V2 curiosity pad, moved to F
    pad = sum(np.sin(2 * np.pi * f * t + 0.8 * np.sin(2 * np.pi * 0.11 * t + k)) for k, f in enumerate((87.31, 130.81, 174.61, 87.6)))
    L['music_alt/curiosity_pad_f.wav'] = norm(lp(pad, 900) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.07 * t) ** 2) * adsr(8.5, 1.8, 2.5), -8)
    q = np.zeros(int(SR * 1.6))                                              # question: D5 F5 A5 rising (was E5 A5 B5: B clashes with F major)
    for k, f in enumerate((D5, F5, A5)):
        s = tone(f, 1.6 - 0.18 * k, 0.5); q[int(SR * 0.18 * k):int(SR * 0.18 * k) + len(s)] += s * (0.8 - 0.15 * k)
    L['illustrative/question_glass_rise.wav'] = norm(q, -8)
    nn = np.zeros(int(SR * 0.7))                                             # playful 'no': C5 -> A4 (both in F major)
    for k, f in enumerate((C5, A4)):
        s = tone(f, 0.45, 0.12, ((1, 1), (4.0, 0.15)), 0.003); nn[int(SR * 0.16 * k):int(SR * 0.16 * k) + len(s)] += s
    L['illustrative/not_this_two_note.wav'] = norm(lp(nn, 3000), -8)
    d = 10.0; x = rng.standard_normal(int(SR * d))
    L['ambience/observatory_night_air.wav'] = norm((lp(x, 240) * (0.7 + 0.3 * np.sin(2 * np.pi * 0.09 * tt(d) + 1.0)) + hp(lp(x, 5000), 2500) * 0.04) * adsr(d, 0.5, 0.5), -10)
    def motor(d, f0, rise, noise_f):
        t = tt(d); f = f0 * (1 + (rise - 1) * t / d); ph = 2 * np.pi * np.cumsum(f) / SR
        return (0.6 * np.sin(ph) + 0.3 * np.sin(2 * ph) + 0.12 * lp(rng.standard_normal(len(t)), noise_f)) * adsr(d, 0.08, 0.15)
    L['mechanical/dome_shutter_motor.wav'] = norm(motor(0.9, 55, 1.08, 400), -8)
    L['mechanical/telescope_servo.wav'] = norm(motor(1.85, 140, 1.15, 900), -8)
    t = tt(0.25); L['mechanical/shutter_end_stop.wav'] = norm(lp(rng.standard_normal(len(t)), 300) * np.exp(-t / 0.04) + 0.5 * np.sin(2 * np.pi * 62 * t) * np.exp(-t / 0.08), -8)
    t = tt(0.12); L['mechanical/laser_fire_tick.wav'] = norm(np.sin(2 * np.pi * 2200 * t) * np.exp(-t / 0.05), -8)
    d = 1.2; t = tt(d); L['ambience/soft_air_swell.wav'] = norm(bp(rng.standard_normal(len(t)), 200, 1200) * np.sin(np.pi * t / d) ** 2, -10)
    L['illustrative/reveal_bell_f5.wav'] = norm(tone(F5, 2.2, 1.1), -8)
    L['illustrative/reveal_bell_c5.wav'] = norm(tone(C5, 2.2, 1.1), -8)
    L['illustrative/answer_fifth_f.wav'] = norm(tone(F4, 2.4, 1.2) + 0.7 * tone(C5, 2.4, 1.2), -8)      # was A + E
    t = tt(0.4); L['illustrative/pulse_glint.wav'] = norm(np.sin(2 * np.pi * 1760 * t) * np.exp(-t / 0.12) * np.clip(t / 0.004, 0, 1), -10)   # A6: in key
    L['character_foley/settle_tone.wav'] = norm(tone(F3, 0.5, 0.18, ((1, 1), (2, 0.3))), -8)            # was G3; vacuum: a musical marker, no thud
    t = tt(0.03); L['illustrative/stopwatch_tick.wav'] = norm(np.sin(2 * np.pi * 3200 * t) * np.exp(-t / 0.012), -8)
    L['illustrative/detector_blip.wav'] = norm(tone(C6, 0.35, 0.08, ((1, 1), (2.0, 0.2))), -8)         # was E6
    t = tt(0.6); L['illustrative/lock_click_tone.wav'] = norm(lp(rng.standard_normal(len(t)), 2500) * np.exp(-t / 0.01) * 0.4 + tone(A5, 0.6, 0.25), -8)   # was B5
    L['illustrative/corrected_tick.wav'] = norm(tone(G5, 0.9, 0.3) + tone(C6, 0.9, 0.25) * 0.5, -8)    # was G5 + D6
    for k, v in L.items(): write(os.path.join(LIB, k), v)
    return L

# ============================================================ cues (V3: 115 -> fewer; every removal is logged with its reason)
W = NAR.ws
STEM = {'ambience': 'ambience', 'mechanical': 'mechanical', 'illustrative': 'illustrative', 'character_foley': 'foley', 'music_alt': 'music_alt'}
def on_grid(t): return BEAT0 + round((t - BEAT0) / (BEAT / 2)) * (BEAT / 2)     # snap to the music's eighth-note grid
def cue_list():
    c = []; removed = []
    def add(t, f, g, why): c.append(dict(t=float(t), file=f, gain_db=g, why=why))
    def cut(t, f, why): removed.append(dict(t=float(t), file=f, why=why))
    add(0.00, 'ambience/observatory_night_air.wav', -30, 'mountain night air under the observatory opening (diegetic, Earth)')
    cut(0.00, 'curiosity_pad_low', 'replaced by the Small_Variables intro (music carries the opening curiosity)')
    add(0.12, 'mechanical/dome_shutter_motor.wav', -27, 'dome shutter opens (P03 0.12-0.95 s)')
    add(0.95, 'mechanical/shutter_end_stop.wav', -30, 'shutter reaches its stop')
    add(0.90, 'mechanical/telescope_servo.wav', -31, 'telescope swings up 0.9-2.75 s')
    add(OP.N_UP - 0.32, 'illustrative/not_this_two_note.wav', -29, '"Not to light it up": the NO mark (playful, in key)')
    add(OP.N_TO + 0.05, 'illustrative/question_glass_rise.wav', -31, '"To ask it a question": brackets lock (in key)')
    add(OP.T_LAUNCH, 'mechanical/laser_fire_tick.wav', -27, 'the laser fires inside the dome (in air)')
    add(OP.T_LAUNCH, 'illustrative/pulse_glint.wav', -35, 'the pulse leaves; its 1.28 s flight is silent (vacuum)')
    add(OP.T_ARRIVE, 'illustrative/pulse_glint.wav', -38, 'arrives on "reflector": the same glint, quieter')
    cut(9.45, 'soft_air_swell', 'the groove (entered at 7.0 s) carries the push to the Moon')
    cut(NAR.start('B06') + 0.4, 'soft_rise_to_silence', 'replaced by a music reduction before the answer (automation row "pre-answer")')
    add(NAR.anchor('B07') - 0.10, 'illustrative/answer_fifth_f.wav', -31, '"About two and a half seconds": lands as the music returns (F + C, in key)')
    cut(NAR.start('B14') - 0.05, 'hold_breath_low', 'the track has its own break at 31.0 s, exactly on "But hold on"')
    add(NAR.anchor('B17'), 'illustrative/reveal_bell_f5.wav', -31, '"Actually, yes": the real array replaces the imagined mirror (in the track breakdown)')
    add(40.08 + p06.T_LAND, 'character_foley/settle_tone.wav', -32, 'reflector set down on the Moon: musical marker, no thud (no air)')
    cut(43.9, 'soft_air_swell', 'music rebuild covers the push on the array')
    cut(NAR.anchor('B19') - 0.1, 'reveal_bell_c5', 'redundant: the groove is at full energy here')
    add(50.75, 'ambience/soft_air_swell.wav', -36, '"Back on Earth": air returns with the observatory')
    add(51.01, 'ambience/observatory_night_air.wav', -32, 'observatory ambience returns with the Earth scene')
    add(G.N_DET, 'illustrative/detector_blip.wav', -31, 'V3 schematic: the one photon reaches the detector on "detector"')
    for r, x in p09.EVENTS:
        tv = p09.T_ROW(r) + 0.10
        if 60.44 <= tv <= 63.53: add(tv, 'illustrative/detector_blip.wav', -34, 'one detected photon (sparse)')
    for k, (x, y, dl) in enumerate(p09.THREE): add(p09.N_FEW + dl, 'illustrative/detector_blip.wav', -31, '"A few photons": one blip per dot (music pulled back)')
    add(G.T29 + G.TA_AIR, 'illustrative/stopwatch_tick.wav', -31, 'G29: the pulse through air arrives late')
    add(G.N_ATM + 0.72, 'illustrative/corrected_tick.wav', -31, 'G29: "corrected"')
    add(G.N_PREC + 0.3, 'illustrative/lock_click_tone.wav', -32, 'the caliper closes on about 1 mm')
    add(NAR.anchor('B35'), 'illustrative/reveal_bell_c5.wav', -32, '"then divide by two": the path folds in half')
    cut(87.9, 'soft_air_swell', 'the outro begins the resolution; no transition effect needed')
    for k in range(0, 9, 2): add(G.N_EACH - 0.4 + 0.42 * k + 0.4, 'illustrative/detector_blip.wav', -37 - k * 0.2, '"With each faint return": measured points (every other one: 9 -> 5)')
    for k in range(1, 9, 2): cut(G.N_EACH - 0.4 + 0.42 * k + 0.4, 'detector_blip', 'thinned: alternate points stay silent under the outro')
    add(G.N_WHERE + 0.6, 'illustrative/lock_click_tone.wav', -32, 'reticle locks on the Moon (bookend)')
    cut(G.N_WHERE + 0.6, 'payoff_chord_g', 'the music outro is the resolution; a G-major chord would clash with F major')
    # stopwatch ticks: V2 had a tick every 0.1 s in four runs (~65 cues). V3 keeps two runs, on the music's eighth-note grid, quieter.
    for a, b, why in ((p11.N_EMIT, p11.N_STOP, 'P11 stopwatch runs to the answer'), (NAR.start('B32'), NAR.start('B32') + 1.0, 'G30 "cosmic stopwatch" sweep')):
        for k in np.arange(on_grid(a), b, BEAT / 2): add(k, 'illustrative/stopwatch_tick.wav', -39, why + ' (on the beat grid)')
    for a, b, why in ((21.9, 25.5, 'P08 one-way legs'), (28.9, 30.2, 'G12 timing changes')):
        cut(a, 'stopwatch_tick x%d' % len(np.arange(a, b, 0.1)), why + ': excessive ticking; music carries the rhythm')
    return sorted(c, key=lambda r: r['t']), removed

# ============================================================ music: edit, automation, ducking
AUTOMATION = [   # (film time s, dB offset, section, intent) - linear between rows; the calibration trim is added on top
    (0.0, 13.0, 'Opening 0-3 s', 'the track intro is ~20 dB quieter than its groove: lifted so curiosity is audible from frame 0'),
    (3.0, 13.0, 'Opening 3-7 s', 'intro develops under "Not to light it up / To ask it a question": anticipation'),
    (6.6, 13.0, 'Groove enters', 'the groove enters at 7.0 s, just before "You fire a pulse"; the lift is ramped off so the entry is felt, not a jump'),
    (7.2, 1.0, 'Main explanation', ''),
    (7.6, 0.0, 'Main explanation', 'stable motif under the narration'),
    (14.8, 0.0, 'Pre-answer', ''),
    (15.4, -12.0, 'Pre-answer reduction', 'music drops away under "comes home?" so the answer arrives in near silence'),
    (16.0, -12.0, 'Answer', '"About two and a half seconds"'),
    (17.1, -2.0, 'Let the answer breathe', 'music returns in the pause after "seconds."'),
    (17.7, 0.0, 'Main explanation', ''),
    (36.6, 0.0, 'Mirror question', 'track breakdown (no bass) under "Did someone leave a mirror on the moon?"'),
    (37.2, -6.0, 'Before the surprise', 'a brief further reduction before "Actually, yes"'),
    (38.9, -6.0, 'Before the surprise', ''),
    (39.6, 2.0, 'Apollo discovery', 'gentle wonder: the track rebuilds 40-42.5 s under "Apollo astronauts left special reflectors"'),
    (44.3, 0.0, 'Main explanation', ''),
    (54.6, 0.0, 'Strange part', ''),
    (55.2, -3.0, 'Strange part', 'pulled back for "And here\'s the really strange part" (seam of the 4-bar repeat at 55.58 s hidden under it)'),
    (60.2, -3.0, 'A few photons', ''),
    (60.9, -7.0, 'A few photons', 'restrained curiosity: sparse detection blips must read'),
    (67.2, -7.0, 'Atmosphere', ''),
    (67.8, -3.0, 'Atmosphere', ''),
    (77.4, -3.0, 'Before "how does it work?"', ''),
    (78.0, -7.0, 'Before the cosmic stopwatch', 'reduction; the track breakdown (79.1-81.6 s) follows'),
    (80.0, 0.0, 'Cosmic stopwatch', 'groove re-enters at 81.6 s under "Take the round trip time": satisfying progression'),
    (82.0, 1.0, 'Cosmic stopwatch', ''),
    (88.0, 1.0, 'Final Earth-Moon scene', ''),
    (89.0, 3.0, 'Final Earth-Moon scene', 'more music: the track outro (from 91.1 s) resolves under the last line'),
    (95.2, 3.0, 'End', ''),
    (96.0, -60.0, 'End', 'fade to silence with the picture')]
def music_edit():
    x = read(MUSIC_SRC, 2); src_dur = x.shape[1] / SR
    b0 = int(SEAM_B0 * SR); b1 = int((SEAM_B0 + SEAM_LEN) * SR); xf = int(SEAM_XF * SR)
    a = x[:, :b1 + xf].copy(); b = x[:, b0:].copy()
    w = np.linspace(0, np.pi / 2, xf); a[:, -xf:] *= np.cos(w); b[:, :xf] *= np.sin(w)
    y = np.concatenate([a[:, :-xf], a[:, -xf:] + b[:, :xf], b[:, xf:]], axis=1)
    y = np.pad(y, ((0, 0), (0, max(0, N - y.shape[1]))))[:, :N]
    return y, src_dur
def automation_curve():
    t = np.arange(N) / SR; ts, gs = zip(*[(r[0], r[1]) for r in AUTOMATION]); return np.interp(t, ts, gs)
def kweight(x):
    """ITU-R BS.1770 K-weighting at 48 kHz (pre-filter + RLB)."""
    x = lfilter([1.53512485958697, -2.69169618940638, 1.19839281085285], [1.0, -1.69065929318241, 0.73248077421585], x)
    return lfilter([1.0, -2.0, 1.0], [1.0, -1.99004745483398, 0.99007225036621], x)
def ebur(p):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', p, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    I = re.findall(r'I:\s+(-?[\d.]+) LUFS', r); TP = re.findall(r'Peak:\s+(-?[\d.]+|-inf) dBFS', r); LRA = re.findall(r'LRA:\s+(-?[\d.]+) LU', r)
    return dict(I=float(I[-1]) if I else None, TP=float(TP[-1]) if TP and TP[-1] != '-inf' else None, LRA=float(LRA[-1]) if LRA else None)

def master(pre, fin):
    I0 = ebur(pre)['I']; g = -16.0 - I0
    for lim in (-2.0, -2.5, -3.0):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', pre, '-af', 'aresample=192000,volume=%.2fdB,alimiter=limit=%.4f:attack=0.5:release=40:level=false,aresample=%d' % (g, db(lim), SR), fin], check=True)
        if ebur(fin)['TP'] <= -1.0: break
    return dict(premaster_I=I0, gain_db=round(g, 2), limiter_ceiling_dbfs=lim, final=ebur(fin))

def main():
    L = lib(); cs, removed = cue_list()
    stems = {k: np.zeros(N) for k in ('ambience', 'mechanical', 'illustrative', 'foley', 'music_alt')}
    for c in cs:
        x = L[c['file']] * db(c['gain_db'] + 12)          # +12: V2's +6 library offset + BED_TRIM 6 (same absolute levels as V2)
        if c['file'] == 'ambience/observatory_night_air.wav':
            seg_end = 9.9 if c['t'] < 10 else 57.3        # V3: air stops where the schematic panel begins (57.15 s)
            ln = int(SR * (seg_end - c['t'])); x = np.resize(x, ln) * np.clip(np.arange(ln) / (SR * 0.4), 0, 1) * np.clip((ln - np.arange(ln)) / (SR * 0.6), 0, 1)
        i0 = int(SR * c['t']); x = x[:max(0, N - i0)]; stems[STEM[c['file'].split('/')[0]]][i0:i0 + len(x)] += x
    pad = L['music_alt/curiosity_pad_f.wav'] * db(-31 + 12); stems['music_alt'][:len(pad)] += pad
    nar = read(MASTER_WAV); nar = np.pad(nar, (0, max(0, N - len(nar))))[:N]
    e = lfilter([1 - np.exp(-2 * np.pi * 8 / SR)], [1, -np.exp(-2 * np.pi * 8 / SR)], np.abs(nar)); e = e / (e.max() + 1e-9)
    speech = np.clip(e / 0.08, 0, 1); sp = speech > 0.5
    duck_sfx = lp(db(-8) + (1 - db(-8)) * (1 - speech), 4)                    # V2 SFX ducking kept
    duck_mus = lp(db(-6) + (1 - db(-6)) * (1 - speech), 3)                    # gentle music ducking (-6 dB while speaking)
    band_cut = lp(1 - (1 - db(-4)) * speech, 4)                               # extra -4 dB in 1-4 kHz while speaking (anti-masking)
    def duck(v, d): vb = bp(v, 1000, 4000); return (v - vb) * d + vb * d * band_cut
    for k in list(stems): stems[k] = duck(stems[k], duck_sfx)
    mus, src_dur = music_edit(); auto = db(automation_curve())
    mus = np.stack([duck(ch * auto, duck_mus) for ch in mus])
    # calibration: voiced windows of the main explanation (7.4-14.8, 17.7-36.6, 44.3-54.6 s), K-weighted RMS, voice vs music (mono sum)
    t = np.arange(N) / SR; main = sp & (((t > 7.4) & (t < 14.8)) | ((t > 17.7) & (t < 36.6)) | ((t > 44.3) & (t < 54.6)))
    kv, km = kweight(nar), kweight(mus.mean(0))
    rms = lambda x, m: 10 * np.log10(np.mean(x[m] ** 2) + 1e-20)
    trim = rms(kv, main) - rms(km, main) - MUSIC_BELOW_VOICE; mus *= db(trim); km *= db(trim)
    peak = np.abs(mus).max()
    sfx = stems['ambience'] + stems['mechanical'] + stems['illustrative'] + stems['foley']
    os.makedirs(os.path.join(OUT, 'stems'), exist_ok=True)
    write(os.path.join(OUT, 'stems', 'stem_01_narration.wav'), nar); write(os.path.join(OUT, 'stems', 'stem_02_music_small_variables_UNVERIFIED_RIGHTS.wav'), mus)
    write(os.path.join(OUT, 'stems', 'stem_03_ambience.wav'), stems['ambience']); write(os.path.join(OUT, 'stems', 'stem_04_mechanical_sfx.wav'), stems['mechanical'])
    write(os.path.join(OUT, 'stems', 'stem_05_scientific_illustrative_fx.wav'), stems['illustrative']); write(os.path.join(OUT, 'stems', 'stem_06_character_foley.wav'), stems['foley'])
    write(os.path.join(OUT, 'stems', 'stem_alt_rights_clear_pad.wav'), stems['music_alt'])
    rep = dict(music=dict(source=MUSIC_SRC, source_duration_s=round(src_dur, 3), bpm=134.98, key_estimate='F major', seam=dict(repeat_from_s=SEAM_B0, length_s=SEAM_LEN, crossfade_s=SEAM_XF, seam_film_s=round(SEAM_B0 + SEAM_LEN, 3)),
                          calibration_trim_db=round(trim, 2), peak_after_trim=round(float(peak), 3), rights='UNVERIFIED: owner must confirm licence before any upload'))
    mixes = {}
    for name, bed in (('review_music', np.stack([nar + sfx] * 2) + mus), ('rights_clear', np.stack([nar + sfx + stems['music_alt']] * 2))):
        pre = os.path.join(OUT, 'final_mix_v3_%s_premaster.wav' % name); write(pre, bed / max(1.0, np.abs(bed).max() / db(-1)))
        fin = os.path.join(OUT, 'final_mix_v3_%s.wav' % name); mixes[name] = master(pre, fin); os.remove(pre)
    import shutil; shutil.copy(os.path.join(OUT, 'final_mix_v3_review_music.wav'), os.path.join(OUT, 'stems', 'stem_07_final_master_review_music.wav'))
    rep['mixes'] = mixes; rep['narration'] = ebur(MASTER_WAV)
    # per-section measurement for the automation map
    rows = []
    for i, (t0, g, sec, why) in enumerate(AUTOMATION[:-1]):
        t1 = AUTOMATION[i + 1][0]; m = (t >= t0) & (t < t1)
        v = m & sp; q = m & ~sp
        d_voiced = round(rms(kv, v) - rms(km, v), 1) if v.sum() > SR * 0.2 else ''
        mus_pause = round(rms(km, q) - rms(kv, main), 1) if q.sum() > SR * 0.2 else ''
        rows.append([sec, '%.2f' % t0, '%.2f' % t1, g, round(g + trim, 2), d_voiced, mus_pause, why])
    with open(os.path.join(OUT, 'MUSIC_AUTOMATION_MAP.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['section', 'from_s', 'to_s', 'automation_db_at_from', 'music_gain_db_incl_trim', 'voice_minus_music_db_voiced_windows', 'music_in_pauses_vs_voice_db', 'intent'])
        w.writerows(rows)
    rep['main_voiced_voice_minus_music_db'] = round(rms(kv, main) - rms(km, main), 1); rep['cues'] = len(cs); rep['cues_removed_vs_v2'] = len(removed)
    rep['listening_verified'] = False
    json.dump(rep, open(os.path.join(OUT, 'SLOT07_V3_mix_report.json'), 'w'), indent=1)
    with open(os.path.join(OUT, 'SOUND_DESIGN_CUE_SHEET.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['cue', 'status', 'time_s', 'file', 'gain_db', 'stem', 'narration_at_time', 'purpose_or_reason'])
        for i, c in enumerate(cs, 1):
            p = NAR.phrase_at(c['t']); txt = ' '.join(x['word'] for x in NAR.words[p['first']:p['last'] + 1]) if p else '(no speech)'
            w.writerow(['V3-%03d' % i, 'kept', '%.2f' % c['t'], 'audio/sfx_v3/' + c['file'], c['gain_db'], STEM[c['file'].split('/')[0]], txt, c['why']])
        for c in sorted(removed, key=lambda r: r['t']):
            w.writerow(['', 'REMOVED', '%.2f' % c['t'], c['file'], '', '', '', c['why']])
    print(json.dumps({k: rep[k] for k in ('main_voiced_voice_minus_music_db', 'cues', 'cues_removed_vs_v2')}, indent=1)); print(json.dumps(rep['music'], indent=1)); print(json.dumps(mixes, indent=1))

if __name__ == '__main__': main()
