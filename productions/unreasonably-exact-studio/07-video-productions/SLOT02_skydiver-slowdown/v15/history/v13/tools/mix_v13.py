"""V13 sound design (V9-V12 design kept, retimed to the V13 picture): builds 5 stems + final mix with ffmpeg. Edit CUES / WIND_KEYS and rerun.

Environmental audio is an illustrative soundscape, not a measurement of airflow or speed.
Library clips (SFX Library/) have NO established licence: this mix is a PRIVATE REVIEW DRAFT.
Synthesised layers (wind bed, aircraft hum) are generated here and are rights-clear.

  python tools/mix_v13.py            -> audio/stems/*.wav, audio/V13_mix.wav, SOUND_DESIGN_CUE_SHEET.csv
"""
import array, csv, json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / 'audio/sfx_library_used'   # copies of the 8 clips used, from the project's SFX Library/
SR, DUR = 48000, 78.2
STEMS = ROOT / 'audio/stems'; STEMS.mkdir(parents=True, exist_ok=True)
TMP = ROOT / 'qa/_audio'; TMP.mkdir(parents=True, exist_ok=True)
PHRASES = json.loads((ROOT / 'audio/phrases.json').read_text())

def ff(*a): subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', *a], check=True)

# ---- wind intensity keys (film time s, 0..1). Follows the picture: rest = near-silent, fast = fuller.
WIND_KEYS = [(0, .16), (1.0, .22), (2.4, .40), (3.3, .66), (5.22, .66), (8.33, .62), (9.70, .52), (11.15, .60), (12.52, .64),
             (14.4, .72), (16.6, .70), (17.7, .62), (18.6, .76), (20.5, .62), (21.3, .05), (24.89, .07), (28.4, .55), (31.6, .66),
             (33.67, .60), (38.72, .68), (44.0, .66), (44.9, .54), (46.1, .54), (46.9, .66), (47.6, .64), (48.4, .50),
             (52.0, .50), (52.8, .70), (55.35, .70), (57.16, .74), (59.35, .66), (61.8, .58), (62.6, .44), (65.9, .44),
             (66.6, .56), (67.3, .50), (69.6, .50), (70.3, .52), (70.53, .48), (74.52, .24), (77.6, .06), (78.2, 0)]
# V13: the wind follows the FALL, not the foreground graphic. Every change is >= 0.7 s and at most ~-3 dB, except
# the deliberate model reset at 20.9-21.3 s ("starting from rest"). Under the bar push-in, the trail and the graph
# the bed eases down slightly so the narration and the small reveal cues stay clear.
AIRCRAFT_KEYS = [(0, 0), (.15, 1), (1.6, .9), (3.0, 0), (78.2, 0)]

def env_value(keys, t):
    if t <= keys[0][0]: return keys[0][1]
    for (a, va), (b, vb) in zip(keys, keys[1:]):
        if t <= b:
            u = (t - a) / (b - a) if b > a else 1; return va + (vb - va) * u
    return keys[-1][1]
def duck(t, depth=.45, fade=.18):
    """Gain for non-VO stems: dips while narration is active (smoothed edges)."""
    g = 1.0
    for p in PHRASES:
        a, b = p['start'] - fade, p['end'] + fade
        if a <= t <= b:
            k = min(1, (t - a) / fade, (b - t) / fade); g = min(g, 1 - (1 - depth) * k)
    return g
def write_env(path, fn, rate=1000):
    """Mono control envelope at 1 kHz (resampled by ffmpeg)."""
    arr = array.array('f', (fn(i / rate) for i in range(int(DUR * rate) + 1)))
    path.write_bytes(arr.tobytes())
def apply_env(src, env, dst, gain_db=0.0):
    ff('-i', str(src), '-f', 'f32le', '-ar', '1000', '-ac', '1', '-i', str(env),
       '-filter_complex', f'[1]aresample={SR},aformat=channel_layouts=stereo[e];[0][e]amultiply,volume={gain_db}dB[o]',
       '-map', '[o]', '-t', str(DUR), '-c:a', 'pcm_s24le', str(dst))

# ---- library cues: (stem, file, start_in_film, clip_in, clip_dur, gain_db, fade_in, fade_out, pan, purpose)
CUES = [
 ('TRANSITIONS', '03_Whooshes_and_Transitions/short_whoosh__part_133_05.wav', 1.25, 0, .84, -13, .05, .2, 0,
  'V13: camera starts to follow the falling figure (tilt down)'),
 ('WIND_AMB', '01_Nature_and_Ambience/wind_gust__part_132_05.wav', 2.55, 0, 2.6, -10, .4, .8, -.2,
  'V13: approach toward the faller, continues over the cut behind the faller (no cloud wipe)'),
 ('FOLEY', '02_Foley_and_Objects/flag__part_136_02.wav', 5.25, 0, 3.0, -15, .4, .8, .15,
  'Suit fabric flutter under gravity beat (side tracking)'),
 ('FOLEY', '02_Foley_and_Objects/flag__part_136_02.wav', 8.38, .4, .5, -19, .05, .2, .2,
  'Sleeve rustle as the forearm lifts'),
 ('FOLEY', '02_Foley_and_Objects/mouse_click__part_134_02.wav', 9.72, .0, .12, -11, .005, .05, .1,
  'Single tick on the cut to the instrument close-up'),
 ('WIND_AMB', '01_Nature_and_Ambience/windy_gust__part_134_04.wav', 14.3, 0, 2.6, -13, .4, .9, .2,
  '"Did the air grow brakes?": gust of streaks past the body'),
 ('WIND_AMB', '01_Nature_and_Ambience/windy_gust__part_134_04.wav', 17.9, 0, 2.6, -13, .5, .9, -.2,
  'V13: camera locks on the faller, the air now streams up past them (relative airflow)'),
 ('OTHER_SFX', '02_Foley_and_Objects/paper__part_125_06.wav', 19.35, 0, .9, -21, .02, .3, 0,
  'V13: drag arrow draws on (the air pushes back)'),
 ('TRANSITIONS', '03_Whooshes_and_Transitions/reverse_whoosh__part_135_03.wav', 19.6, .66, 1.3, -16, .3, .03, 0,
  'Reverse swell into the MODEL reset (fall restarts from rest)'),
 ('OTHER_SFX', '02_Foley_and_Objects/paper__part_125_06.wav', 29.2, 0, .9, -22, .02, .3, .1,
  'V13: denser-air box fills'),
 ('OTHER_SFX', '02_Foley_and_Objects/paper__part_125_06.wav', 40.35, 0, .9, -20, .02, .3, .15,
  'V13: force bars appear side by side'),
 ('OTHER_SFX', '02_Foley_and_Objects/paper__part_125_06.wav', 43.75, 0, .9, -21, .02, .3, .15,
  'V13: drag bar passes the weight line (net force revealed)'),
 ('OTHER_SFX', '02_Foley_and_Objects/paper__part_125_06.wav', 47.66, 0, .9, -19, .02, .3, 0,
  'Equal-time trail appears'),
 ('FOLEY', '02_Foley_and_Objects/flag__part_136_02.wav', 54.33, .4, .5, -19, .05, .2, .2,
  'Sleeve rustle as the forearm lifts again'),
 ('FOLEY', '02_Foley_and_Objects/mouse_click__part_134_02.wav', 55.40, .0, .12, -11, .005, .05, .1,
  'Single tick on the cut to the first-person instrument'),
 ('FOLEY', '02_Foley_and_Objects/flag__part_136_02.wav', 59.3, .3, 2.4, -16, .3, .7, -.15,
  'Fabric flutter on the closed-pack callback'),
 ('OTHER_SFX', '02_Foley_and_Objects/paper__part_125_06.wav', 66.2, 0, .9, -20, .02, .3, .15,
  'V13: recap force bars'),
 ('TRANSITIONS', '03_Whooshes_and_Transitions/deep_whoosh__part_127_06.wav', 70.3, 0, 2.6, -11, .2, .9, 0,
  'Pull-back to the wide model frame'),
]
# find the first click's real onset/length in mouse_click (3 clicks in the clip)
def first_click(path):
    out = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(path), '-af', 'silencedetect=n=-40dB:d=0.03', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    ends = [float(l.split('silence_end: ')[1].split()[0]) for l in out.splitlines() if 'silence_end' in l]
    return ends[0] if ends else 0.0

def build():
    rows = []
    # VOICEOVER: owner narration, decoded unaltered (no gain, no timing change)
    ff('-i', str(ROOT / 'audio/narration_preserved.m4a'), '-ar', str(SR), '-ac', '2', '-c:a', 'pcm_s24le', str(STEMS / 'VOICEOVER.wav'))
    rows.append(dict(stem='VOICEOVER', filename='audio/narration_preserved.m4a', start=0, end=78.2, purpose='Owner narration (recovered V6 AAC stream), unaltered',
                     volume='0 dB', fades='none', source='Owner recording', rights='Owner-supplied'))
    # synthesised wind bed (two decorrelated noise layers, slow stereo drift) and aircraft hum
    ff('-f', 'lavfi', '-i', f'anoisesrc=d={DUR}:c=brown:r={SR}:s=11:a=.9', '-f', 'lavfi', '-i', f'anoisesrc=d={DUR}:c=pink:r={SR}:s=29:a=.5',
       '-filter_complex', '[0]highpass=f=70,lowpass=f=900,volume=6dB[a];[1]highpass=f=900,lowpass=f=5200,volume=-14dB,tremolo=f=0.17:d=0.35[b];'
       '[a][b]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo,apulsator=hz=0.07:amount=0.25[o]', '-map', '[o]', '-c:a', 'pcm_s24le', str(TMP / 'wind_raw.wav'))
    ff('-f', 'lavfi', '-i', f'anoisesrc=d={DUR}:c=brown:r={SR}:s=5:a=.8', '-f', 'lavfi', '-i', f'sine=f=88:d={DUR}:r={SR}', '-f', 'lavfi', '-i', f'sine=f=176.5:d={DUR}:r={SR}',
       '-filter_complex', '[0]lowpass=f=320,volume=2dB[n];[1]volume=-20dB,tremolo=f=11:d=0.3[s1];[2]volume=-27dB[s2];[n][s1][s2]amix=inputs=3:normalize=0,aformat=channel_layouts=stereo[o]',
       '-map', '[o]', '-c:a', 'pcm_s24le', str(TMP / 'aircraft_raw.wav'))
    write_env(TMP / 'wind.env', lambda t: env_value(WIND_KEYS, t) * duck(t))
    write_env(TMP / 'air.env', lambda t: env_value(AIRCRAFT_KEYS, t) * duck(t, .6))
    apply_env(TMP / 'wind_raw.wav', TMP / 'wind.env', TMP / 'wind_bed.wav', -5)
    apply_env(TMP / 'aircraft_raw.wav', TMP / 'air.env', TMP / 'aircraft.wav', -6)
    rows.append(dict(stem='WIND_AMB', filename='synth: brown+pink noise (tools/mix_v13.py)', start=0, end=78.2,
                     purpose='Continuous relative-air bed; level follows picture state (near-silent at model rest 20.9-24.9 s)',
                     volume='-5 dB x envelope (WIND_KEYS), ducked ~-7 dB under VO', fades='keyframed', source='Generated in this project', rights='Rights-clear (generated)'))
    rows.append(dict(stem='WIND_AMB', filename='synth: brown noise + 88/176 Hz hum', start=0, end=3.0, purpose='Restrained aircraft ambience, establishing shot only',
                     volume='-6 dB, fade out 1.6-3.0 s', fades='in .15 / out 1.4', source='Generated in this project', rights='Rights-clear (generated)'))
    # library cues per stem
    click_in = first_click(LIB / '02_Foley_and_Objects/mouse_click__part_134_02.wav')
    per = {k: [] for k in ('WIND_AMB', 'FOLEY', 'TRANSITIONS', 'OTHER_SFX')}
    per['WIND_AMB'] += [TMP / 'wind_bed.wav', TMP / 'aircraft.wav']
    for n, (stem, f, at, cin, cd, g, fi, fo, pan, purpose) in enumerate(CUES):
        if 'mouse_click' in f: cin = max(0, click_in - .005)
        out = TMP / f'cue{n:02}.wav'
        ff('-ss', str(cin), '-t', str(cd), '-i', str(LIB / f), '-filter_complex',
           f'aresample={SR},aformat=channel_layouts=stereo,afade=t=in:d={fi},afade=t=out:st={max(0, cd - fo)}:d={fo},'
           f'stereotools=balance_out={pan},volume={g}dB,adelay={int(at * 1000)}:all=1,apad=whole_dur={DUR}[o]',
           '-map', '[o]', '-t', str(DUR), '-c:a', 'pcm_s24le', str(out))
        # duck library cues lightly under narration too
        env = TMP / f'cue{n:02}.env'; write_env(env, lambda t: duck(t, .6)); apply_env(out, env, TMP / f'cue{n:02}_d.wav')
        per[stem].append(TMP / f'cue{n:02}_d.wav')
        rows.append(dict(stem=stem, filename=f'SFX Library/{f}', start=round(at, 2), end=round(at + cd, 2), purpose=purpose,
                         volume=f'{g} dB, pan {pan:+.2f}, ducked under VO', fades=f'in {fi}s / out {fo}s',
                         source='Supplied SFX Library (extracted from 16 videos)', rights='NOT CLEARED: licence not established; private review draft only'))
    for stem, files in per.items():
        ins = sum((['-i', str(f)] for f in files), [])
        ff(*ins, '-filter_complex', f'{"".join(f"[{i}]" for i in range(len(files)))}amix=inputs={len(files)}:normalize=0[o]',
           '-map', '[o]', '-t', str(DUR), '-c:a', 'pcm_s24le', str(STEMS / f'{stem}.wav'))
    names = ['VOICEOVER', 'WIND_AMB', 'FOLEY', 'TRANSITIONS', 'OTHER_SFX']
    ins = sum((['-i', str(STEMS / f'{n}.wav')] for n in names), [])
    ff(*ins, '-filter_complex', '[0][1][2][3][4]amix=inputs=5:normalize=0,alimiter=limit=0.89:level=false[o]', '-map', '[o]', '-c:a', 'pcm_s24le', str(ROOT / 'audio/V13_mix.wav'))
    # rights-clear alternative mix: VO + generated layers only (for publication until library clips are cleared)
    ff('-i', str(STEMS / 'VOICEOVER.wav'), '-i', str(TMP / 'wind_bed.wav'), '-i', str(TMP / 'aircraft.wav'),
       '-filter_complex', '[0][1][2]amix=inputs=3:normalize=0,alimiter=limit=0.89:level=false[o]', '-map', '[o]', '-c:a', 'pcm_s24le', str(ROOT / 'audio/V13_mix_rights_clear.wav'))
    with (ROOT / 'SOUND_DESIGN_CUE_SHEET.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['stem', 'filename', 'start', 'end', 'purpose', 'volume', 'fades', 'source', 'rights'])
        w.writeheader(); w.writerows(rows)
    print('stems + mix written;', len(CUES), 'library cues')

if __name__ == '__main__':
    build()
