#!/usr/bin/env python3
"""Build animation/AUDIO_ALIGNMENT.json from the owner's WAV.

Word timings come from openai-whisper (base) word timestamps; phrase onsets are
snapped to ffmpeg silencedetect boundaries. This is ASR + waveform evidence only,
not human listening. Usage (from the project directory):

  python3 animation/tools/align_audio.py --asr-json <whisper.json>   # reuse a saved whisper result
  python3 animation/tools/align_audio.py                             # runs whisper base locally
"""
import argparse, hashlib, json, re, subprocess, sys, wave, array
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WAV = ROOT / 'animation/audio/cartesia_2026-10-14T09_09_17Z_Skylar_sonic-3.6-2026-08-27.wav'
SCRIPT = ROOT / 'editable_sources/original/APPROVED_NARRATION.txt'
OUT = ROOT / 'animation/AUDIO_ALIGNMENT.json'

# Approved phrases (storyboard narration_phrase granularity) -> inclusive ASR word index range.
PHRASES = [
    ('P01', 'The Federal Reserve raised interest rates.', 0, 5),
    ('P02', 'And its own interest bill went up.', 6, 12),
    ('P03', 'In September, the Fed raised rates by a quarter point.', 13, 22),
    ('P04', "Here's the problem:", 23, 25),
    ('P05', 'banks keep roughly three trillion dollars in reserves at the Fed,', 26, 35),
    ('P06', 'and the Fed pays them interest.', 36, 41),
    ('P07', 'Just that quarter-point increase', 42, 46),
    ('P08', 'would add about seven and a half billion dollars a year in interest costs,', 47, 56),
    ('P09', 'if reserves stayed the same.', 57, 61),
    ('P10', "But much of the Fed's bond income doesn't rise as quickly.", 62, 72),
    ('P11', 'When expenses outweigh income,', 73, 76),
    ('P12', "losses build into what's called a deferred asset.", 77, 84),
    ('P13', 'By early October, that balance was roughly two hundred and thirty-four billion dollars.', 85, 93),
    ('P14', 'Until future earnings cover it,', 94, 98),
    ('P15', "the Fed's normal payments to the Treasury stay paused.", 99, 107),
    ('P16', 'In twenty twenty-one, those payments were more than one hundred and seven billion dollars.', 108, 116),
    ('P17', 'Higher rates can fight inflation.', 117, 121),
    ('P18', "But they can also make the Fed's own finances harder to repair.", 122, 133),
]
# Spoken-number spellings in the approved text and the digit form whisper prints.
NUMBERS = [('three trillion dollars', '$3 trillion'), ('seven and a half billion dollars', '$7.5 billion'),
           ('two hundred and thirty-four billion dollars', '$234 billion'), ('twenty twenty-one', '2021'),
           ('one hundred and seven billion dollars', '$107 billion')]


def norm(s):
    s = s.lower().replace('quarter-point', 'quarter point')
    return re.sub(r'[^a-z0-9$.\' ]', ' ', s).replace('. ', ' ').split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--asr-json')
    a = ap.parse_args()
    if a.asr_json:
        asr = json.load(open(a.asr_json))
    else:
        import whisper
        asr = whisper.load_model('base').transcribe(str(WAV), language='en', word_timestamps=True, fp16=False, temperature=0)

    raw = [w for s in asr['segments'] for w in s['words']]
    # whisper splits "$7.5" into "$7" + ".5"; merge so indices match the PHRASES table
    words = []
    for w in raw:
        t = w['word'].strip()
        if words and re.fullmatch(r'\.\d+', t):
            words[-1]['text'] += t; words[-1]['end'] = w['end']; continue
        words.append({'text': t, 'start': w['start'], 'end': w['end'], 'p': w['probability']})
    assert len(words) == 134, len(words)

    sd = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', str(WAV), '-af', 'silencedetect=noise=-40dB:d=0.18', '-f', 'null', '-'],
                        capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', sd)]
    ends = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', sd)]
    silences = [[round(s, 3), round(e, 3)] for s, e in zip(starts, ends)]
    for i, w in enumerate(words):
        w['i'] = i
        w['start_refined'] = w['start']
    # each silence end marks the onset of the first word after it (ASR onsets drift ~0.1-0.3 s)
    for _, e in silences:
        near = [w for w in words if w['end'] > e and e - 0.6 <= w['start'] <= e + 0.30]
        if near:
            near[0]['start_refined'] = e
    for w in words:
        for k in ('start', 'start_refined', 'end', 'p'):
            w[k] = round(w[k], 3)

    with wave.open(str(WAV)) as f:
        sr, ch, sw, n = f.getframerate(), f.getnchannels(), f.getsampwidth(), f.getnframes()
        pcm = array.array('h', f.readframes(n))
    peak = max(max(pcm), -min(pcm))
    import math
    approved = SCRIPT.read_text().strip()
    ap_norm = approved.lower()
    for spoken, digits in NUMBERS:
        ap_norm = ap_norm.replace(spoken, digits)
    asr_tokens, ap_tokens = norm(' '.join(w['text'] for w in words)), norm(ap_norm)
    match = asr_tokens == ap_tokens

    out = {
        'source': {
            'original_path': '/Users/ghilmankhan/Downloads/' + WAV.name, 'project_copy': str(WAV.relative_to(ROOT)),
            'sha256': hashlib.sha256(WAV.read_bytes()).hexdigest(), 'bytes': WAV.stat().st_size,
            'format': f'WAV PCM s{8 * sw}le', 'sample_rate': sr, 'channels': ch, 'duration_sec': round(n / sr, 4),
            'sample_peak_dbfs': round(20 * math.log10(peak / 32768), 2), 'clipped_samples': sum(1 for x in pcm if abs(x) >= 32767),
        },
        'method': 'openai-whisper base word timestamps (ASR) + ffmpeg silencedetect -40 dB / 0.18 s. Phrase onsets snapped to silence ends. No human listening.',
        'approved_script': {'path': str(SCRIPT.relative_to(ROOT)), 'sha256': hashlib.sha256(SCRIPT.read_bytes()).hexdigest(), 'words': len(approved.split())},
        'asr_text': asr['text'].strip(),
        'comparison': {
            'status': 'MATCH_AFTER_NUMBER_NORMALIZATION' if match else 'MISMATCH',
            'asr_tokens': len(asr_tokens), 'approved_tokens_after_normalization': len(ap_tokens),
            'normalization_only_differences': [f'{s!r} printed by ASR as {d!r}' for s, d in NUMBERS] + ['punctuation/capitalisation; "quarter-point" hyphen'],
            'not_resolvable_by_asr': 'Exact spoken realisation of numbers (e.g. "seven and a half" vs "seven point five", and each spoken "dollars") is inferred, not heard. Unbroken speech after "$234 billion" (33.88-34.76 s) and "$107 billion" (43.32-44.46 s) is consistent with the approved "dollars".',
        },
        'silences': silences,
        'speech_start_sec': words[0]['start'], 'speech_end_sec': words[-1]['end'],
        'phrases': [{'id': pid, 'text': t, 'first_word': a0, 'last_word': a1, 'start': words[a0]['start_refined'], 'end': words[a1]['end']}
                    for pid, t, a0, a1 in PHRASES],
        'words': [{k: w[k] for k in ('i', 'text', 'start', 'start_refined', 'end', 'p')} for w in words],
    }
    OUT.write_text(json.dumps(out, indent=1) + '\n')
    print(out['comparison']['status'], out['source']['duration_sec'], 's', out['source']['sha256'][:12])
    return 0 if match else 1


if __name__ == '__main__':
    sys.exit(main())
