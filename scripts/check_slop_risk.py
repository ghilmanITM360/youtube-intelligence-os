"""AI-slop risk gate. Rules: docs/policies/AI-SLOP-RISK-RULES.md. Runs on EVERY new script/video before delivery.

PROXY ONLY: platform detectors also use account, infrastructure, API and upload-timing signals that a script
cannot show. PASS means "no risk signal found by these checks", never "safe from detection".
Purpose is to keep content non-templated and substantive, NOT to disguise templated content.

Production scripts live at productions/<project>/**/*SCRIPT*.md|txt and start with an optional header:
  ---
  title: ...      channel: CH-...      images: path/to/thumbnail-or-frames (repo-relative)
  ---
Automatic triggers: Claude Code SessionStart/UserPromptSubmit/PostToolUse hooks (--claude-hook), .githooks/pre-commit and CI (--only-scripts),
production_pipeline.py validate. Manual (repo root):
  uv run python scripts/check_slop_risk.py SCRIPT... [--title T] [--channel CH] [--images P ...]
      [--verified-presenter] [--exception R5="reason"]
Writes SCRIPT.slop-risk.json; exit 1 if any FAIL (delivery blocked)."""
import argparse, csv, datetime, hashlib, json, re, sqlite3, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / 'data/catalog/youtube_channel_registry.db'
JSONL_GLOB = 'data/extracted/channel-data/**/TRANSCRIPTS*.jsonl'
TITLE_CSVS = ['docs/research/senior-health-2026-11-11/01-unified-video-table.csv']
IMAGE_ROOTS = ['data/raw/competitors', 'research/finance-economics-intelligence/thumbnail-evidence']
PRODUCTIONS = ROOT / 'productions'
IMG_EXT = {'.jpg', '.jpeg', '.png', '.webp'}
COPY_FAIL, COPY_WARN = 0.15, 0.05      # share of our 5-gram shingles found in ONE other text
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


def norm(t):
    return re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", (t or '').lower())).strip()


def front_matter(text):
    """({key: value}, body) from a leading '---' header block; ({}, text) when there is none."""
    m = re.match(r"---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)", text, re.S)
    if not m: return {}, text
    meta = dict(kv.split(':', 1) for kv in m.group(1).splitlines() if ':' in kv)
    return {k.strip().lower(): v.strip() for k, v in meta.items()}, text[m.end():]


def split_sources(text):
    """(body, has_sources): body excludes the Sources section so citations don't count as copying."""
    m = SOURCES.search(text)
    if not m: return text, False
    return text[:m.start()], bool((m.group(1) or '').strip()) or any(line.strip() for line in text[m.end():].splitlines())


def rel(p):
    p = Path(p).resolve()
    return str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p)


def is_script(p):
    """Production script = productions/<project>/**/ file with 'script' in its name, .md or .txt."""
    r = Path(rel(p))
    return r.parts[:1] == ('productions',) and len(r.parts) > 2 and r.suffix.lower() in {'.md', '.txt'} and 'script' in r.name.lower()


def project_of(p):
    r = Path(rel(p))
    return r.parts[1] if is_script(p) else Path(p).resolve().parent.name


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
    own: [(path, title, text)] scripts of OUR other projects; images: [(path, hash)]. Returns findings."""
    f = []
    def add(rule, level, detail): f.append({'rule': rule, 'level': level, 'detail': detail})
    body, has_sources = split_sources(text)
    s = shingles(body)
    # R1 copy vs competitor/registry transcripts; R4 copy vs our own other projects
    def copy_rule(rule, items, what):
        best = max(((len(s & shingles(t)) / max(len(s), 1), i) for i, t in items), default=(0, None))
        if best[0] >= COPY_FAIL: add(rule, 'FAIL', f'{best[0]:.0%} of script 5-grams match {what} {best[1]}')
        elif best[0] >= COPY_WARN: add(rule, 'WARN', f'{best[0]:.0%} of script 5-grams match {what} {best[1]}')
    if len(s) < 50: add('R1', 'WARN', f'script too short for a reliable copy check ({len(s)} 5-grams)')
    copy_rule('R1', corpus, 'existing video')
    copy_rule('R4', [(p, split_sources(t)[0]) for p, _, t in own], 'our other project')
    # R2 title duplicates (competitors + our own)
    if title:
        nt, wt = norm(title), set(norm(title).split())
        all_titles = list(titles) + [(p, t) for p, t, _ in own]
        exact = [i for i, t in all_titles if t and norm(t) == nt]
        if exact: add('R2', 'FAIL', f'title identical to existing video/project {exact[:5]}')
        else:
            near = [(round(len(wt & set(norm(t).split())) / max(len(wt | set(norm(t).split())), 1), 2), i) for i, t in all_titles if t]
            near = sorted((x for x in near if x[0] >= TITLE_WARN), reverse=True)
            if near: add('R2', 'WARN', f'title near-identical to {near[:5]}')
    else: add('R2', 'WARN', 'no title (header `title:` or --title); title duplicate check skipped')
    # R3 stock AI boilerplate
    low = body.lower()
    hits = sorted({p for p in BOILERPLATE if p in low})
    if len(hits) >= 3: add('R3', 'WARN', f'{len(hits)} stock AI/clickbait phrases: {hits}')
    # R5 substance: sources section required
    if not has_sources: add('R5', 'FAIL', 'no "Sources" section/line with at least one item (own data, study, document, URL)')
    # R6 invented expert persona
    m = PERSONA.findall(body)
    if m and not verified_presenter: add('R6', 'FAIL', f'expert persona claim without --verified-presenter: {sorted(set(x.strip() for x in m))}')
    # R7 visuals near-identical to competitor thumbnails
    for p, h in images:
        best = min(((bin(h ^ rh).count('1'), i) for i, rh in ref_hashes), default=(64, None))
        if best[0] <= HASH_FAIL: add('R7', 'FAIL', f'{p} near-identical to competitor image {best[1]} (distance {best[0]})')
        elif best[0] <= HASH_WARN: add('R7', 'WARN', f'{p} similar to competitor image {best[1]} (distance {best[0]})')
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


def load_own(project):
    """Scripts of our OTHER production projects (reuse across our channels = coordination signal)."""
    out = []
    for p in sorted(PRODUCTIONS.rglob('*')) if PRODUCTIONS.is_dir() else []:
        if p.is_file() and is_script(p) and project_of(p) != project:
            meta, body = front_matter(p.read_text(errors='ignore')); out.append((rel(p), meta.get('title'), body))
    return out


def run(script, title=None, channel=None, project=None, images=(), verified_presenter=False, exceptions=None):
    script = Path(script); raw = script.read_text(errors='ignore'); meta, text = front_matter(raw)
    title = title or meta.get('title'); channel = channel or meta.get('channel'); project = project or project_of(script)
    images = list(images) or ([ROOT / meta['images']] if meta.get('images') else [])
    imgs, bad_imgs = [], []
    for p in image_files(images):
        try: imgs.append((rel(p), dhash(p)))
        except Exception: bad_imgs.append(rel(p))
    findings = evaluate(text, title, load_corpus(), load_titles(), load_ref_hashes() if imgs else [], load_own(project),
                        imgs, verified_presenter)
    if bad_imgs: findings.append({'rule': 'R7', 'level': 'WARN', 'detail': f'unreadable images not checked: {bad_imgs}'})
    if not images: findings.append({'rule': 'R7', 'level': 'WARN', 'detail': 'no images (header `images:` or --images); visual check skipped'})
    elif not imgs and not bad_imgs: findings.append({'rule': 'R7', 'level': 'WARN', 'detail': f'no image files found at {[str(i) for i in images]}'})
    for f in findings:  # documented exceptions downgrade FAIL, never silently
        if f['level'] == 'FAIL' and (exceptions or {}).get(f['rule']): f['level'] = 'EXCEPTION'; f['exception_reason'] = exceptions[f['rule']]
    levels = {f['level'] for f in findings}
    verdict = 'FAIL' if 'FAIL' in levels else 'WARN' if levels & {'WARN', 'EXCEPTION'} else 'PASS'
    report = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'script': rel(script),
              'sha256': hashlib.sha256(raw.encode()).hexdigest(), 'title': title, 'channel': channel, 'project': project,
              'verdict': verdict, 'delivery_blocked': verdict == 'FAIL', 'findings': findings, 'manual_checklist': CHECKLIST,
              'rules': 'docs/policies/AI-SLOP-RISK-RULES.md',
              'note': 'PROXY ONLY: account/infrastructure/upload-timing signals are not visible here; PASS is not a guarantee.'}
    Path(f'{script}.slop-risk.json').write_text(json.dumps(report, indent=2) + '\n')
    return report


def summary(r):
    lines = [f"AI-slop gate {r['verdict']}  {r['script']}"] + [f"  {f['level']:9} {f['rule']}  {f['detail']}" for f in r['findings']]
    return '\n'.join(lines + ['  manual checklist (human confirms):'] + [f'   - {c}' for c in CHECKLIST] +
                     [f"  report: {r['script']}.slop-risk.json  rules: {r['rules']}"])


GUARD = ("AI-slop gate ACTIVE (docs/policies/AI-SLOP-RISK-RULES.md). Any script, voiceover or video package you produce "
         "must be saved as productions/<project>/**/*SCRIPT*.md (header: title/channel/images) so the gate runs on it; "
         "never deliver a script only in chat. Show the user the gate verdict, findings and checklist with every delivery; "
         "a PASS is a proxy, never 'won't be detected'.")


def claude_hook():
    """Claude Code hook (SessionStart / UserPromptSubmit / PostToolUse), dispatched on stdin's hook_event_name.
    systemMessage is shown to the user directly; additionalContext/reason go to Claude."""
    ev = json.load(sys.stdin); name = ev.get('hook_event_name', 'PostToolUse')
    if name == 'SessionStart':
        print(json.dumps({'systemMessage': 'AI-slop gate active: every new script/video in productions/ is checked; '
                          'FAIL blocks delivery.', 'hookSpecificOutput': {'hookEventName': name, 'additionalContext': GUARD}}))
        return 0
    if name == 'UserPromptSubmit':
        print(json.dumps({'hookSpecificOutput': {'hookEventName': name, 'additionalContext': GUARD}})); return 0
    path = (ev.get('tool_input') or {}).get('file_path')
    if not path or not Path(path).is_file() or not is_script(path): return 0
    r = run(path); s = summary(r)
    alert = f"AI-slop gate {r['verdict']}: {r['script']}" + ''.join(f"\n  {f['level']} {f['rule']}: {f['detail']}" for f in r['findings'])
    if r['delivery_blocked']:
        print(json.dumps({'systemMessage': alert + '\nDelivery BLOCKED.', 'decision': 'block', 'reason': s +
                          '\nFix with original work (no paraphrasing/noise to beat thresholds) '
                          'before delivering, or record a reasoned --exception the user sees.'}))
    else:
        print(json.dumps({'systemMessage': alert, 'hookSpecificOutput': {'hookEventName': 'PostToolUse', 'additionalContext': s +
                          '\nShow this verdict, findings and checklist to the user with the delivery.'}}))
    return 0


def main(argv=None):
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument('scripts', nargs='*'); a.add_argument('--title'); a.add_argument('--channel'); a.add_argument('--project')
    a.add_argument('--images', nargs='*', default=[]); a.add_argument('--verified-presenter', action='store_true')
    a.add_argument('--exception', action='append', default=[], help='RULE=reason; downgrades that rule\'s FAIL, recorded in report')
    a.add_argument('--only-scripts', action='store_true', help='skip paths that are not production scripts (hooks/CI)')
    a.add_argument('--claude-hook', action='store_true', help='read a Claude Code hook event from stdin')
    o = a.parse_args(argv)
    if o.claude_hook: return claude_hook()
    paths = [p for p in o.scripts if not o.only_scripts or (Path(p).is_file() and is_script(p))]
    if not paths: print('AI-slop gate: no production scripts to check'); return 0 if o.only_scripts else 2
    exc = dict(e.split('=', 1) for e in o.exception); blocked = False
    for p in paths:
        r = run(p, o.title, o.channel, o.project, o.images, o.verified_presenter, exc)
        print(summary(r)); blocked |= r['delivery_blocked']
    return 1 if blocked else 0


if __name__ == '__main__':
    sys.exit(main())
