"""Build the staging tree (outside the repo) from candidates.csv. Sources are only read. usage: python3 -I build_stage.py"""
import os, csv, shutil, json, hashlib, subprocess, collections, datetime
SP = os.path.dirname(os.path.abspath(__file__))
STAGE = SP + '/stage'
ARCH = 'research/xkcd-what-if-research-archive/'
REPO = '/Users/ghilmanislam360/Documents/youtube-intelligence-os'
if os.path.exists(STAGE): shutil.rmtree(STAGE)
rows = list(csv.DictReader(open(SP + '/candidates.csv')))
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''): h.update(c)
    return h.hexdigest()
def cat(path, ext):
    b = os.path.basename(path).lower()
    if ext == '.md': return 'report_or_doc_markdown'
    if ext in ('.csv', '.tsv'): return 'dataset_csv'
    if ext in ('.json', '.jsonl'): return 'dataset_json'
    if ext == '.py': return 'script_python'
    if ext in ('.txt', '.srt'): return 'transcript_or_text'
    if ext == '.log': return 'run_log'
    if ext == '.xml': return 'feed_snapshot_xml'
    if ext == '.npy': return 'numpy_array'
    return 'other_' + (ext.strip('.') or 'noext')
man = []
for r in rows:
    if r['decision'] != 'INCLUDE': continue
    status = 'INCLUDED'; mapped = ''
    if r['in_origin_main_as']:
        status = 'DEDUPED_ON_ORIGIN_MAIN'; mapped = r['in_origin_main_as']
    else:
        dst = STAGE + '/' + r['repo_path']
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(r['source_path'], dst)
        assert sha(dst) == r['sha256'], r['source_path']
    man.append(dict(repo_path=r['repo_path'] if status == 'INCLUDED' else '', source_path=r['source_path'], size_bytes=int(r['size']),
                    sha256=r['sha256'], git_blob_sha1=r['git_blob_sha1'], category=cat(r['source_path'], r['ext']),
                    source_group=r['label'], status=status, existing_repo_path_on_origin_main=mapped))
# internal exact-duplicate groups (kept, since they are version/provenance copies); recorded only
g = collections.defaultdict(list)
for m in man:
    if m['status'] == 'INCLUDED': g[m['sha256']].append(m['repo_path'])
dups = [(k, v) for k, v in g.items() if len(v) > 1]
w = csv.writer(open(STAGE + '/' + ARCH + 'DEDUP_MAP.csv', 'w', newline=''))
w.writerow(['kind', 'sha256', 'copy_count', 'paths_or_mapping'])
for k, v in sorted(dups): w.writerow(['internal_exact_duplicate_kept', k, len(v), ' | '.join(v)])
for m in man:
    if m['status'] == 'DEDUPED_ON_ORIGIN_MAIN':
        w.writerow(['not_copied_identical_on_origin_main', m['sha256'], 1, m['source_path'] + ' => ' + m['existing_repo_path_on_origin_main'] + ' (git blob ' + m['git_blob_sha1'] + ')'])
# manifest csv
cols = ['repo_path', 'source_path', 'size_bytes', 'sha256', 'git_blob_sha1', 'category', 'source_group', 'status', 'existing_repo_path_on_origin_main']
with open(STAGE + '/' + ARCH + 'MANIFEST.csv', 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=cols); wr.writeheader(); wr.writerows(sorted(man, key=lambda m: (m['repo_path'] or m['source_path'])))
# excluded csv
ex = [r for r in rows if r['decision'] == 'EXCLUDE']
with open(STAGE + '/' + ARCH + 'EXCLUDED_FILES.csv', 'w', newline='') as f:
    wr = csv.writer(f); wr.writerow(['source_path', 'category', 'reason', 'size_bytes', 'sha256', 'source_group'])
    for r in sorted(ex, key=lambda r: r['source_path']): wr.writerow([r['source_path'], r['reason'] if r['reason'] != 'image' else 'image', r['reason'], r['size'], r['sha256'], r['label']])
inc = [m for m in man if m['status'] == 'INCLUDED']
summ = dict(included_files=len(inc), included_bytes=sum(m['size_bytes'] for m in inc),
            deduped_not_copied=sum(1 for m in man if m['status'] != 'INCLUDED'),
            by_category=dict(collections.Counter(m['category'] for m in inc)), by_source_group=dict(collections.Counter(m['source_group'] for m in inc)),
            excluded_by_reason=dict(collections.Counter(r['reason'] for r in ex)), excluded_bytes_by_reason={k: sum(int(r['size']) for r in ex if r['reason'] == k) for k in set(r['reason'] for r in ex)},
            internal_duplicate_groups=len(dups), venv_pruned_files=json.load(open(SP + '/classify_meta.json'))['venv_pruned_files'])
json.dump(summ, open(SP + '/stage_summary.json', 'w'), indent=1); print(json.dumps(summ, indent=1))
json.dump(man, open(SP + '/manifest_entries.json', 'w'))
