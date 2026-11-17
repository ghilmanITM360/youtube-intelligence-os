"""Read-only structured-data census for the YIOS algorithm audit (2026-10-26).

Usage: python3 -I census.py <repo_root> <out_dir>
Never writes inside repo_root. SQLite opened with mode=ro; other branches read via `git show`.
"""
import csv, hashlib, io, json, os, sqlite3, subprocess, sys, collections as C

REPO, OUT = sys.argv[1], sys.argv[2]
FIN = 'research/finance-economics-intelligence'
PR44 = 'origin/codex/what-if-archive-main-integration'
WIF = 'research/visual-forensics/channels/CH-000004/what-if-source-package/production_intelligence_brain'
csv.field_size_limit(10**9)


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def git(*a):
    return subprocess.run(['git', '-C', REPO, *a], capture_output=True, text=True, check=True).stdout


# ---------- SQLite ----------
def census_db(rel):
    p = os.path.join(REPO, rel)
    out = {'path': rel, 'bytes': os.path.getsize(p), 'sha256': sha(p), 'tables': []}
    if out['bytes'] == 0:
        out['status'] = 'EMPTY_FILE_ZERO_BYTES'
        return out
    db = sqlite3.connect(f'file:{p}?mode=ro', uri=True)
    out['integrity_check'] = db.execute('pragma quick_check').fetchone()[0]
    try:
        fk = db.execute('pragma foreign_key_check').fetchall()
        out['foreign_key_violations'] = len(fk)
        out['foreign_key_violations_by_table'] = dict(C.Counter(r[0] for r in fk))
    except sqlite3.Error as e:
        out['foreign_key_violations'] = f'NOT_CHECKED: {e}'
    for (t,) in db.execute("select name from sqlite_master where type='table' order by name"):
        rec = {'table': t}
        try:
            cols = db.execute(f'pragma table_info("{t}")').fetchall()
            rec['rows'] = db.execute(f'select count(*) from "{t}"').fetchone()[0]
            rec['columns'] = len(cols)
            pk = [c[1] for c in sorted(cols, key=lambda c: c[5]) if c[5]]
            if pk:
                q = ','.join(f'"{c}"' for c in pk)
                rec['pk'] = pk
                rec['pk_distinct'] = db.execute(f'select count(*) from (select distinct {q} from "{t}")').fetchone()[0]
            # null profile, all records scanned
            if rec['rows'] and len(cols) <= 60:
                sel = ','.join(f'sum("{c[1]}" is null or "{c[1]}"=\'\')' for c in cols)
                vals = db.execute(f'select {sel} from "{t}"').fetchone()
                rec['null_or_empty'] = {c[1]: v for c, v in zip(cols, vals) if v}
            rec['scan'] = 'FULL_RECORD_SCAN'
        except sqlite3.Error as e:
            rec['scan'] = f'NOT_SCANNED: {e}'
        out['tables'].append(rec)
    return out


def registry_checks():
    db = sqlite3.connect(f'file:{REPO}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
    q = lambda s: db.execute(s).fetchall()
    return {
        'video_type_labels': q('select coalesce(video_type,"<NULL>"),count(*) from videos group by 1'),
        'videos_without_channel_row': q('select count(*) from videos v left join channels c using(canonical_channel_id) where c.canonical_channel_id is null')[0][0],
        'videos_in_multiple_datasets': q('select count(*) from (select youtube_video_id from dataset_videos group by 1 having count(*)>1)')[0][0],
        'videos_in_no_dataset': q('select count(*) from videos where youtube_video_id not in (select youtube_video_id from dataset_videos)')[0][0],
        'transcripts_placeholder': q('select sum(is_placeholder),count(*) from transcripts')[0],
        'transcripts_short_lt200chars': q('select count(*) from transcripts where coalesce(length(transcript_text),0)<200')[0][0],
        'duplicate_transcript_hash_groups': q('select count(*) from (select transcript_sha256 from transcripts where transcript_sha256 is not null group by 1 having count(*)>1)')[0][0],
        'duplicate_titles_within_channel': q('select count(*) from (select canonical_channel_id,title from videos group by 1,2 having count(*)>1)')[0][0],
        'views_null': q('select count(*) from videos where views is null')[0][0],
        'published_at_not_iso_datetime': q("select count(*) from videos where published_at not like '____-__-__T%'")[0][0],
        'channels_with_videos': q('select count(distinct canonical_channel_id) from videos')[0][0],
        'channels_total': q('select count(*) from channels')[0][0],
        'first_party_analytics_status': q('select first_party_analytics_status,count(*) from channels group by 1'),
        'forensic_video_status': q('select forensic_video_status,count(*) from channels group by 1'),
    }


# ---------- Flat files ----------
ID_COLS = ('Video_ID', 'video_id', 'youtube_video_id', 'Channel_ID', 'channel_id')


def census_table(rel, text=None):
    p = os.path.join(REPO, rel)
    rec = {'path': rel}
    if text is None:
        rec['bytes'], rec['sha256'] = os.path.getsize(p), sha(p)
        text = open(p, newline='', encoding='utf-8', errors='replace').read()
    else:
        rec['bytes'], rec['sha256'] = len(text.encode()), hashlib.sha256(text.encode()).hexdigest()
        rec['source'] = 'git show ' + PR44
    if rel.endswith('.jsonl'):
        rows = [json.loads(l) for l in text.splitlines() if l.strip()]
        flat = [dict(r, **(r.get('identity') or {})) for r in rows]
    else:
        flat = list(csv.DictReader(io.StringIO(text)))
    rec['rows'] = len(flat)
    rec['columns'] = len(flat[0]) if flat else 0
    for k in ID_COLS:
        if flat and k in flat[0]:
            ids = [r[k] for r in flat]
            rec['id_column'] = k
            rec['distinct_ids'] = len(set(ids))
            rec['duplicate_ids'] = sum(v - 1 for v in C.Counter(ids).values() if v > 1)
            break
    if flat and not rel.endswith('.jsonl'):
        rec['empty_cells_by_column_top'] = dict(C.Counter({k: sum(1 for r in flat if not (r.get(k) or '').strip()) for k in flat[0]}).most_common(8))
    rec['scan'] = 'FULL_RECORD_SCAN'
    return rec, flat


def main():
    os.makedirs(OUT, exist_ok=True)
    res = {'repo_head': git('rev-parse', 'HEAD').strip(), 'branch': git('branch', '--show-current').strip(),
           'pr44_ref': git('rev-parse', PR44).strip(), 'worktree_dirty_files': len(git('status', '--porcelain').splitlines())}
    res['sqlite'] = [census_db(f'data/catalog/{n}') for n in sorted(os.listdir(f'{REPO}/data/catalog')) if n.endswith('.db')]
    res['registry_checks'] = registry_checks()

    files = [f'{FIN}/{n}' for n in sorted(os.listdir(f'{REPO}/{FIN}')) if n.endswith(('.csv', '.jsonl'))]
    for d in ('expansion-12-channel-2026-10-20', 'expansion-monkey-explains-1999-2026-10-21', 'reconciliation-all-repository-2026-10-21'):
        files += [f'{FIN}/{d}/{n}' for n in sorted(os.listdir(f'{REPO}/{FIN}/{d}')) if n.endswith(('.csv', '.jsonl'))]
    files += ['research/visual-forensics/INDEX.csv']
    res['flat_files'], tables = [], {}
    for f in files:
        r, flat = census_table(f)
        res['flat_files'].append(r)
        tables[f] = flat

    # What If brain (PR #44, unmerged) read via git show
    res['what_if_pr44'] = []
    for n in git('ls-tree', '-r', '--name-only', PR44, WIF).splitlines():
        if n.endswith('.csv'):
            r, flat = census_table(n, git('show', f'{PR44}:{n}'))
            res['what_if_pr44'].append(r)
            tables[n] = flat

    # checksum manifests shipped with expansion/reconciliation folders
    res['checksum_verification'] = []
    for d in ('expansion-12-channel-2026-10-20', 'expansion-monkey-explains-1999-2026-10-21', 'reconciliation-all-repository-2026-10-21'):
        m = json.load(open(f'{REPO}/{FIN}/{d}/FILE_CHECKSUMS_SHA256.json'))
        items = m.get('files', m) if isinstance(m, dict) else m
        items = items.items() if isinstance(items, dict) else [(i.get('path'), i.get('sha256')) for i in items]
        ok = bad = missing = 0
        mism = []
        for path, h in items:
            if isinstance(h, dict):
                h = h.get('sha256')
            cand = [f'{REPO}/{FIN}/{d}/{path}', f'{REPO}/{path}', f'{REPO}/{FIN}/{path}']
            p = next((c for c in cand if os.path.isfile(c)), None)
            if not p:
                missing += 1
            elif sha(p) == h:
                ok += 1
            else:
                bad += 1
                mism.append(path)
        res['checksum_verification'].append({'manifest': f'{FIN}/{d}/FILE_CHECKSUMS_SHA256.json', 'match': ok, 'mismatch': bad, 'missing': missing, 'mismatched_paths': mism})

    # population overlap
    uni = tables[f'{FIN}/reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv']
    aud = tables[f'{FIN}/VIDEO_AUDIT_966.jsonl']
    rdb = sqlite3.connect(f'file:{REPO}/data/catalog/youtube_channel_registry.db?mode=ro', uri=True)
    idb = sqlite3.connect(f'file:{REPO}/data/catalog/youtube_inventory.db?mode=ro', uri=True)
    reg = {r[0] for r in rdb.execute('select youtube_video_id from videos')}
    inv = {r[0] for r in idb.execute('select youtube_video_id from videos')} if 'youtube_video_id' in [c[1] for c in idb.execute('pragma table_info(videos)')] else set()
    U = {r['video_id'] for r in uni}
    done = {r['Video_ID'] for r in aud if all(v == 'COMPLETE_LIMITED_EVIDENCE' for v in r['statuses'].values())}
    res['population'] = {
        'finance_universe_ids': len(U), 'finance_universe_layers': dict(C.Counter(r['population_layer'] for r in uni)),
        'universe_audit_status_frozen_2026_10_21': dict(C.Counter(r['audit_status'] for r in uni)),
        'live_ledger_records': len(aud), 'live_ledger_all_six_complete': len(done),
        'live_ledger_status_patterns': dict(C.Counter('|'.join(f'{k[:4]}={v[:8]}' for k, v in sorted(r['statuses'].items())) for r in aud)),
        'expansion_ledger_records': len(tables[f'{FIN}/expansion-12-channel-2026-10-20/EXPANSION_AUDIT_LEDGER.jsonl']),
        'registry_db_videos': len(reg), 'inventory_db_videos': len(inv),
        'universe_in_registry_db': len(U & reg), 'universe_in_inventory_db': len(U & inv), 'registry_and_inventory_overlap': len(reg & inv),
        'deep_complete_in_original_966': len(done & {r['Video_ID'] for r in aud}),
        'what_if_registry_videos': rdb.execute("select count(*) from videos where canonical_channel_id='UC6IxnFzHofFJ5X2PycSMsww'").fetchone()[0],
    }
    json.dump(res, open(f'{OUT}/census.json', 'w'), indent=1, default=str)
    print(json.dumps(res['population'], indent=1), json.dumps(res['checksum_verification'], indent=1), json.dumps(res['registry_checks'], indent=1, default=str))


if __name__ == '__main__':
    main()
