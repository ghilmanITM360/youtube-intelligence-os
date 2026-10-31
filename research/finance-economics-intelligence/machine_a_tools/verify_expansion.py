"""Read-only verification of the 30 Casually Finance expansion transcript candidates.
Reads git blobs from origin refs (never checks out or writes to those branches); writes a packet to argv[1]."""
import csv, io, json, hashlib, subprocess, sys, collections
W = '/Users/ghilmankhan/workprojects/yios-finance-machine-a'
B = W + '/research/finance-economics-intelligence/'
OUT = sys.argv[1]
git = lambda *a: subprocess.run(['git', '-C', W, *a], capture_output=True, check=True).stdout
sha = lambda b: hashlib.sha256(b).hexdigest()

uni = {r['video_id']: r for r in csv.DictReader(open(B + 'reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv', encoding='utf-8-sig'))}
meta = {}
for r in uni.values():
    if r['channel_name'] == 'Casually Finance' and not meta:
        src = git('show', f"{r['source_commit']}:{r['source_dataset']}").decode('utf-8-sig')
        meta = {m['Video_ID']: m for m in csv.DictReader(io.StringIO(src))}
        meta_ref = f"{r['source_commit']}:{r['source_dataset']}"
rows = [r for r in csv.DictReader(open(B + 'FINANCE_SOURCE_READINESS_QUEUE.csv', encoding='utf-8-sig')) if r['readiness_class'] == 'CANDIDATE_TRANSCRIPT_ON_ORIGIN_BRANCH']

def words_of(path, blob):
    """Return (ordered words, max_end_sec, id_values_in_file) for a supported transcript blob, else None."""
    t = blob.decode('utf-8-sig')
    if path.endswith('TRANSCRIPT.csv'):
        rs = list(csv.DictReader(io.StringIO(t)))
        rs.sort(key=lambda x: (float(x['start_sec']), x['word_id']))  # word_index restarts per sentence
        return [x['word'] for x in rs], max(float(x['end_sec']) for x in rs), {x['video_id'] for x in rs}
    if path.endswith('asr_words.csv'):
        rs = list(csv.DictReader(io.StringIO(t)))
        rs.sort(key=lambda x: int(x['word_index']))
        return [x['word'] for x in rs], max(float(x['end_sec']) for x in rs), set()
    return None  # caption-event files and readable text are corroboration only

packet, texts = [], collections.defaultdict(list)
for r in rows:
    vid = r['video_id']
    locs = [l.strip() for l in r['candidate_locators'].split('|')]
    if any('casually-finance-editing-forensics' in l for l in locs):
        ref = 'origin/research/casually-finance-editing-forensics'
        locs.append(f'{ref}:research/casually-finance-editing-forensics/videos/{vid}/auto/asr_words.csv')
    cands = []
    for l in locs:
        ref, _, path = l.partition(':')
        try:
            blob = git('show', f'{ref}:{path}'); oid = git('rev-parse', f'{ref}:{path}').decode().strip()
        except subprocess.CalledProcessError:
            cands.append({'locator': l, 'status': 'MISSING_ON_REF'}); continue
        c = {'locator': l, 'ref_head': git('rev-parse', ref).decode().strip(), 'git_blob': oid, 'sha256': sha(blob), 'bytes': len(blob),
             'path_contains_video_id': vid in path}
        w = words_of(path, blob)
        if w:
            words, end, ids = w; text = ' '.join(words)
            c.update(kind='WORD_LEVEL_ASR', words=len(words), max_end_sec=round(end, 2), text_sha256=sha(text.encode()),
                     in_file_ids=sorted(ids), id_match=(not ids) or ids == {vid}, asr_source='WHISPER_BASE_WORD_TIMESTAMPS' if path.endswith('TRANSCRIPT.csv') else 'EDITING_FORENSICS_AUTO_ASR')
            texts[c['text_sha256']].append(vid)
        else:
            c['kind'] = 'CORROBORATION_ONLY_NOT_A_TRANSCRIPT'
        cands.append(c)
    m = meta.get(vid, {})
    dur = float(m['Duration_Sec']) if m.get('Duration_Sec') else None
    asr = [c for c in cands if c.get('kind') == 'WORD_LEVEL_ASR']
    best = max(asr, key=lambda c: c['words'], default=None)
    cov = round(best['max_end_sec'] / dur, 3) if best and dur else None
    distinct = sorted({c['text_sha256'] for c in asr})
    checks = {
        'has_word_level_asr': bool(asr),
        'all_ids_match': all(c['id_match'] and c['path_contains_video_id'] for c in asr) if asr else False,
        'copies_identical': len(distinct) <= 1,
        'coverage_vs_duration_ge_0_9': cov is not None and cov >= 0.9,
        'metadata_row_present': bool(m),
    }
    packet.append({'video_id': vid, 'title': uni[vid]['title'], 'format': m.get('Format'), 'duration_sec': dur, 'publish_date': m.get('Publish_Date'),
                   'universe_transcript_status': uni[vid]['transcript_status'], 'candidates': cands, 'distinct_asr_texts': distinct,
                   'best_candidate': best['locator'] if best else None, 'asr_coverage_ratio': cov, 'checks': checks})

for p in packet:
    p['duplicate_text_with_other_ids'] = sorted({v for h in p['distinct_asr_texts'] for v in texts[h]} - {p['video_id']})
    ok = all(p['checks'].values()) and not p['duplicate_text_with_other_ids']
    p['verdict'] = 'VERIFIED_CANDIDATE_NOT_REGISTERED' if ok else 'NEEDS_REVIEW'
    p['caption_type'] = 'MACHINE_ASR_NOT_CREATOR_CAPTIONS'

summary = {'generated_by': 'machine_a read-only verifier', 'metadata_source': meta_ref, 'candidates': len(packet),
           'verdicts': dict(collections.Counter(p['verdict'] for p in packet)),
           'failed_checks': dict(collections.Counter(k for p in packet for k, v in p['checks'].items() if not v)),
           'registration': 'NONE; registry writes are outside Machine A authority; audit contract requires registry Text_SHA256 and archive containment',
           'videos': packet}
json.dump(summary, open(OUT, 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in summary.items() if k != 'videos'}, indent=1))
for p in packet:
    print(p['video_id'], p['format'], p['duration_sec'], p['asr_coverage_ratio'], len(p['distinct_asr_texts']), p['verdict'], [k for k, v in p['checks'].items() if not v], p['duplicate_text_with_other_ids'])
