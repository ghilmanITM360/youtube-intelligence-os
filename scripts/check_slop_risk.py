"""AI-slop risk gate. Rules: docs/policies/AI-SLOP-RISK-RULES.md. Run on EVERY new script/video before delivery.

PROXY ONLY: platform detectors also use account, infrastructure, API and upload-timing signals that a script
cannot show. PASS means "no risk signal found by these checks", never "safe from detection".
Purpose is to keep content non-templated and substantive, NOT to disguise templated content.

Usage (repo root):
  uv run python scripts/check_slop_risk.py SCRIPT --title "..." --channel CH-000001 [--project slug]
      [--images DIR_OR_FILE ...] [--verified-presenter] [--exception R2="reason"] [--no-ledger]
Writes SCRIPT.slop-risk.json; exit 1 on FAIL (delivery blocked)."""
import argparse, csv, datetime, hashlib, json, re, sqlite3, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / 'data/catalog/youtube_channel_registry.db'
JSONL_GLOB = 'data/extracted/channel-data/**/TRANSCRIPTS*.jsonl'
TITLE_CSVS = ['docs/research/senior-health-2026-11-11/01-unified-video-table.csv']
IMAGE_ROOTS = ['data/raw/competitors', 'research/finance-economics-intelligence/thumbnail-evidence']
LEDGER = ROOT / 'data/intelligence/system/slop-gate-ledger.jsonl'
IMG_EXT = {'.jpg', '.jpeg', '.png', '.webp'}
COPY_FAIL, COPY_WARN = 0.15, 0.05      # share of our 5-gram shingles found in ONE other video
TITLE_WARN = 0.8                       # word-set Jaccard
HASH_FAIL, HASH_WARN = 5, 10           # dHash Hamming distance (64-bit)

BOILERPLATE = ["in today's video", "let's dive in", "let's dive into", "dive deep", "delve into", "it's important to note",
    "it is important to note", "in this video we will", "without further ado", "buckle up", "game changer", "game-changer",
    "unlock the secrets", "the secret that", "doctors don't want you to know", "nobody is talking about",
    "you won't believe", "stay tuned", "smash that like", "in conclusion", "in today's fast-paced world",
    "the truth is", "here's the thing", "at the end of the day", "a testament to", "navigate the complexities"]
PERSONA = re.compile(r"\b(?:i am|i'm|as an?|speaking as an?)\s+(?:a\s+|your\s+)?(?:dr\b\.?|doctor|physician|cardiologist|"
                     r"neurologist|nurse|pharmacist|surgeon|dietitian|financial advisor|cpa)\b", re.I)
SOURCES = re.compile(r"^[ \t]*(?:#+[ \t]*)?(?:sources?|references?|citations?)[ \t]*(?::[ \t]*(.*))?$", re.I | re.M)
CHECKLIST = [  # signals the paper names that a script cannot show; a human confirms these
    "C1 Upload pacing is a human cadence (paper feature: avg upload pace, time to first upload); no bulk-scheduled bursts.",
    "C2 Our channels do not share accounts, devices, API keys, templates or upload scripts in a way that makes them one cluster.",
    "C3 Realistic synthetic/altered visuals or voice are disclosed with YouTube's altered/synthetic content setting.",
    "C4 No realistic AI depiction or voice clone of a real person; no invented expert persona.",
    "C5 Health/finance claims were checked against the listed sources by a human."]


def shingles(text):
    w = re.findall(r"[a-z']+", re.sub(r"\[[^\]]*\]", " ", text.lower()))
    return {tuple(w[i:i + 5]) for i in range(len(w) - 4)}


norm = lambda t: re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", (t or '').lower())).strip()


def split_sources(text):
    """(body, has_sources): body excludes the Sources section so citations don't count as copying."""
    m = SOURCES.search(text)
    if not m: return text, False
    return text[:m.start()], bool((m.group(1) or '').strip()) or any(l.strip() for l in text[m.end():].splitlines())


def dhash(path):
    from PIL import Image  # declared project dependency (pyproject); run with `uv run`
    with Image.open(path) as im: px = im.convert('L').resize((9, 8)).tobytes()
    return sum(1 << i for i, (a, b) in enumerate((px[r * 9 + c], px[r * 9 + c + 1]) for r in range(8) for c in range(8)) if a > b)


def image_files(paths):
    for p in map(Path, paths):
        if p.is_dir(): yield from (f for f in sorted(p.rglob('*')) if f.suffix.lower() in IMG_EXT)
        elif p.suffix.lower() in IMG_EXT: yield p


def evaluate(text, title, corpus, titles, ref_hashes, own, images=(), verified_presenter=False):
    """Pure check. corpus: iterable (id, text); titles: iterable (id, title); ref_hashes: [(id, hash)];
    own: [ledger entries of OTHER projects]; images: [(path, hash)]. Returns findings list."""
    f = []
    add = lambda rule, level, detail: f.append({'rule': rule, 'level': level, 'detail': detail})
    body, has_sources = split_sources(text)
    s = shingles(body)
    # R1 copy vs competitor/registry transcripts; R4 copy vs our own other projects
    def copy_rule(rule, items, what):
        best = max(((len(s & shingles(t)) / max(len(s), 1), i) for i, t in items), default=(0, None))
        if best[0] >= COPY_FAIL: add(rule, 'FAIL', f'{best[0]:.0%} of script 5-grams match {what} {best[1]}')
        elif best[0] >= COPY_WARN: add(rule, 'WARN', f'{best[0]:.0%} of script 5-grams match {what} {best[1]}')
    if len(s) < 50: add('R1', 'WARN', f'script too short for a reliable copy check ({len(s)} 5-grams)')
    copy_rule('R1', corpus, 'existing video')
    own_texts = [(o['path'], (ROOT / o['path']).read_text(errors='ignore')) for o in own if (ROOT / o['path']).is_file()]
    copy_rule('R4', own_texts, 'our other project')
    # R2 title duplicates (competitors + our own)
    if title:
        nt, wt = norm(title), set(norm(title).split())
        all_titles = list(titles) + [(o['path'], o.get('title')) for o in own]
        exact = [i for i, t in all_titles if t and norm(t) == nt]
        if exact: add('R2', 'FAIL', f'title identical to existing video/project {exact[:5]}')
        else:
            near = [(round(len(wt & set(norm(t).split())) / max(len(wt | set(norm(t).split())), 1), 2), i) for i, t in all_titles if t]
            near = sorted(x for x in near if x[0] >= TITLE_WARN)[::-1]
            if near: add('R2', 'WARN', f'title near-identical to {near[:5]}')
    else: add('R2', 'WARN', 'no title given; title duplicate check skipped')
    # R3 stock AI boilerplate
    low = body.lower()
    hits = sorted({p for p in BOILERPLATE if p in low})
    if len(hits) >= 3: add('R3', 'WARN', f'{len(hits)} stock AI/clickbait phrases: {hits}')
    # R5 substance: sources section required
    if not has_sources: add('R5', 'FAIL', 'no "Sources" section with at least one item (own data, study, document, URL)')
    # R6 invented expert persona
    m = PERSONA.findall(body)
    if m and not verified_presenter: add('R6', 'FAIL', f'expert persona claim without --verified-presenter: {sorted(set(x.strip() for x in m))}')
    # R7 visuals: near-identical to competitor thumbnails, or to our own other projects (template reuse)
    for p, h in images:
        best = min(((bin(h ^ rh).count('1'), i) for i, rh in ref_hashes), default=(64, None))
        if best[0] <= HASH_FAIL: add('R7', 'FAIL', f'{p} near-identical to competitor image {best[1]} (distance {best[0]})')
        elif best[0] <= HASH_WARN: add('R7', 'WARN', f'{p} similar to competitor image {best[1]} (distance {best[0]})')
        mine = min(((bin(h ^ oh).count('1'), o['path']) for o in own for oh in o.get('image_hashes', [])), default=(64, None))
        if mine[0] <= HASH_FAIL: add('R7', 'WARN', f'{p} near-identical to visual of our project {mine[1]} (template reuse across projects)')
    return f


def load_corpus():
    if REGISTRY.exists():
        con = sqlite3.connect(f'file:{REGISTRY}?mode=ro', uri=True)
        yield from ((f'{c}/{v}', t) for v, c, t in con.execute(
            'select t.youtube_video_id, v.canonical_channel_id, t.transcript_text from transcripts t '
            'join videos v using(youtube_video_id) where t.is_placeholder=0 and t.transcript_text is not null'))
    for fp in ROOT.glob(JSONL_GLOB):
        for line in open(fp):
            r = json.loads(line)
            if r.get('text'): yield f"{r.get('channel_handle')}/{r.get('video_id')}", r['text']


def load_titles():
    if REGISTRY.exists():
        con = sqlite3.connect(f'file:{REGISTRY}?mode=ro', uri=True)
        yield from ((f'{c}/{v}', t) for v, c, t in con.execute('select youtube_video_id, canonical_channel_id, title from videos'))
    csv.field_size_limit(10 ** 9)
    for fp in TITLE_CSVS:
        if (ROOT / fp).exists(): yield from ((f"{r['channel']}/{r['video_id']}", r['title']) for r in csv.DictReader(open(ROOT / fp)))


def load_ref_hashes():
    out = []
    for f in image_files(ROOT / r for r in IMAGE_ROOTS):
        try: out.append((str(f.relative_to(ROOT)), dhash(f)))
        except Exception: pass  # unreadable reference image: skip, it is not our content
    return out


def read_ledger():
    latest = {}
    if LEDGER.exists():
        for line in open(LEDGER): e = json.loads(line); latest[e['path']] = e
    return list(latest.values())


def rel(p):
    p = Path(p).resolve()
    return str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p)


def run(script, title=None, channel=None, project=None, images=(), verified_presenter=False, exceptions=None, ledger=True):
    script = Path(script); text = script.read_text(errors='ignore'); project = project or script.parent.name
    own = [o for o in read_ledger() if o.get('project') != project]
    imgs = []
    for p in image_files(images):
        try: imgs.append((rel(p), dhash(p)))
        except Exception as e: imgs.append((rel(p), None)); print(f'cannot hash {p}: {e}', file=sys.stderr)
    bad_imgs = [p for p, h in imgs if h is None]; imgs = [(p, h) for p, h in imgs if h is not None]
    findings = evaluate(text, title, load_corpus(), load_titles(), load_ref_hashes() if imgs else [], own, imgs, verified_presenter)
    if bad_imgs: findings.append({'rule': 'R7', 'level': 'WARN', 'detail': f'unreadable images not checked: {bad_imgs}'})
    if not images: findings.append({'rule': 'R7', 'level': 'WARN', 'detail': 'no --images given; visual check skipped'})
    for f in findings:  # documented exceptions downgrade FAIL, never silently
        if f['level'] == 'FAIL' and (exceptions or {}).get(f['rule']): f['level'] = 'EXCEPTION'; f['exception_reason'] = exceptions[f['rule']]
    levels = {f['level'] for f in findings}
    verdict = 'FAIL' if 'FAIL' in levels else 'WARN' if levels & {'WARN', 'EXCEPTION'} else 'PASS'
    report = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'script': rel(script),
              'sha256': hashlib.sha256(text.encode()).hexdigest(), 'title': title, 'channel': channel, 'project': project,
              'verdict': verdict, 'delivery_blocked': verdict == 'FAIL', 'findings': findings, 'manual_checklist': CHECKLIST,
              'rules': 'docs/policies/AI-SLOP-RISK-RULES.md',
              'note': 'PROXY ONLY: account/infrastructure/upload-timing signals are not visible here; PASS is not a guarantee.'}
    Path(f'{script}.slop-risk.json').write_text(json.dumps(report, indent=2) + '\n')
    if ledger:
        with open(LEDGER, 'a') as fh: fh.write(json.dumps({k: report[k] for k in ('checked_at', 'sha256', 'title', 'channel', 'project', 'verdict')}
                                                          | {'path': rel(script), 'image_hashes': [h for _, h in imgs]}) + '\n')
    return report


def main(argv=None):
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument('script'); a.add_argument('--title'); a.add_argument('--channel'); a.add_argument('--project')
    a.add_argument('--images', nargs='*', default=[]); a.add_argument('--verified-presenter', action='store_true')
    a.add_argument('--exception', action='append', default=[], help='RULE=reason; downgrades that rule\'s FAIL, recorded in report')
    a.add_argument('--no-ledger', action='store_true')
    o = a.parse_args(argv)
    exc = dict(e.split('=', 1) for e in o.exception)
    r = run(o.script, o.title, o.channel, o.project, o.images, o.verified_presenter, exc, not o.no_ledger)
    print(f"{r['verdict']}  {r['script']}")
    for f in r['findings']: print(f"  {f['level']:9} {f['rule']}  {f['detail']}")
    print('  manual checklist:'); [print('   -', c) for c in CHECKLIST]
    print(f"  report: {r['script']}.slop-risk.json")
    return 1 if r['delivery_blocked'] else 0


if __name__ == '__main__':
    sys.exit(main())
