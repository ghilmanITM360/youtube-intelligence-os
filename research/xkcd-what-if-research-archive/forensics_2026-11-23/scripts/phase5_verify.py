"""Phase 5 verification (continuation): (1) link each playbook rule to video IDs and paragraph/word locators, recomputed from the 83 raw transcripts,
(2) separate videos from content families, (3) temporal split-half holdout on the 43 long videos (older 21 vs newer 22 by publish date).
Read-only. Run: python3 -I scripts/phase5_verify.py  -> 05_RULE_EVIDENCE_LINKS.csv, 05_HOLDOUT_TEMPORAL_SPLIT.csv, prints a summary."""
import csv, json, re, random, statistics as st
from pathlib import Path
A = Path(__file__).resolve().parent.parent
RS = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/what-if-scripts')
inv = {i['vid']: i for i in json.loads((RS / 'analysis/inventory.json').read_text())}
mat = {m['vid']: m for m in map(json.loads, (RS / 'analysis/matrix.jsonl').read_text().splitlines() if False else open(RS / 'analysis/matrix.jsonl'))}
met = {r['vid']: r for r in csv.DictReader(open(A / '05_SCRIPT_METRICS.csv'))}
fam = {r['vid']: r for r in csv.DictReader(open(A / '05_FAMILY_AND_REUSE_TABLE.csv'))}
def paras(v): return [p for p in (RS / inv[v]['script']).read_text().split('## Script\n', 1)[1].split('\n\n') if p.strip()]
LONG = [v for v in inv if inv[v]['format'] == 'long']; SHORT = [v for v in inv if inv[v]['format'] != 'long']
rows = []
def add(rid, rule, cls, hits, N, ex, loc, rec, note=''):
    fams = {fam[v]['family'] for v in hits}; allf = {fam[v]['family'] for v in N}
    rows.append(dict(rule_id=rid, rule=rule, rule_class=cls, videos_with=len(hits), videos_of=len(N), families_with=len(fams), families_of=len(allf),
                     exception_ids=';'.join(ex), example_locators=';'.join(loc[:6]), recompute=rec, note=note))
# R01 attributed opening question: audit label vs independent text check on paragraph 1-2
att_pat = re.compile(r"(comes from|asks?|asked|writes?|wants to know|question (is )?from|from [A-Z][a-z]+)", re.I)
audit_att = {v for v in LONG if any('attributed' in h.lower() for h in mat[v]['hook'])}
text_att = {v for v in LONG if att_pat.search(' '.join(paras(v)[:2]))}
man = audit_att | {'V015'}  # V015 para1 read by hand in this audit: 'This question comes from AJ, who wrote' (audit labelled it 'story hook')
add('R01', 'Long script opens with a viewer-attributed question (audit label + V015 read by hand)', 'OBSERVED', sorted(man), LONG, sorted(set(LONG) - man),
    [f'{v} para1' for v in sorted(man)], 'matrix.jsonl hook labels; text regex agreement below',
    f'independent regex on para 1-2: {len(text_att)}/43; agree with audit on {len(audit_att & text_att)}; audit-only {sorted(audit_att - text_att)}; regex-only {sorted(text_att - audit_att)}')
# R02 no CTA wording
cta = re.compile(r"\b(subscribe|like and subscribe|patreon|sponsor(ed)?|next video|link in the description|check out my|my book|pre-?order)\b", re.I)
hit = {}
for v in inv:
    for i, p in enumerate(paras(v), 1):
        m = cta.search(p)
        if m: hit.setdefault(v, []).append(f'para{i}:{m.group(0)}')
cta_lab = {v: mat[v]['cta'] for v in LONG}; nocta = [v for v in LONG if cta_lab[v].lower().startswith('none')]
add('R02', 'No CTA in the script text (audit cta label begins "None"; 38 plain, 3 with a qualifier)', 'OBSERVED', nocta, LONG, [v for v in LONG if v not in nocta],
    [f'{v} cta=None' for v in nocta], 'matrix.jsonl cta field; regex cross-check scans all 83 scripts',
    f'exceptions: ' + '; '.join(f'{v}: {cta_lab[v][:60]}' for v in LONG if v not in nocta) + f' | regex (subscribe/sponsor/patreon/next video/link in description/my book/pre-order) hits across 83 scripts: {len(hit)} (regex does not see the book-promo wording in V019)')
# R03 Shorts are excerpts of a long parent
sh_der = [v for v in SHORT if fam[v]['role'] == 'DERIVED_SHORT']
add('R03', 'Shorts are contiguous excerpts or abridgements of a long parent (8-gram containment >= 0.30)', 'MEASURED', sh_der, SHORT, [v for v in SHORT if v not in sh_der],
    [f'{v}->{fam[v]["best_parent"]} ({float(fam[v]["containment_8gram"]):.2f})' for v in sh_der], 'scripts/phase5_corpus.py (8-gram containment)',
    f'median containment {st.median(float(fam[v]["containment_8gram"]) for v in sh_der):.3f}; "contiguous" is not measured here, only containment')
# R04 length and rate numbers in the playbook
wm = st.median(int(met[v]['words']) for v in LONG); wp = st.median(float(met[v]['wps']) for v in LONG)
add('R04', 'Long script median 680 words, 3.59 words/s', 'MEASURED', LONG, LONG, [], [f'{v} words={met[v]["words"]}' for v in LONG[:6]], 'recomputed from 05_SCRIPT_METRICS.csv', f'median words {wm}, median wps {wp}; playbook says 680 / 3.59')
# R05 spine keywords from matrix 'structure'
for rid, kw in (('R05', 'ladder'), ('R06', 'cascade'), ('R07', 'tournament'), ('R08', 'audit')):
    h = [v for v in LONG if kw in mat[v]['structure'].lower()]
    add(rid, f'Spine keyword "{kw}" in the audit structure label', 'OBSERVED_KEYWORD', h, LONG, [], [f'{v}: {mat[v]["structure"][:50]}' for v in h[:5]], 'matrix.jsonl structure field substring', 'approximate: keyword tagging, not a coded taxonomy')
w = csv.DictWriter(open(A / '05_RULE_EVIDENCE_LINKS.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
# holdout
L = sorted(LONG, key=lambda v: inv[v]['date']); dev, tst = L[:21], L[21:]
def num(v, k): return float(met[v][k])
mets = ['words', 'wps', 'paragraphs', 'question_marks', 'numerals_per_100w', 'you_per_100w']
random.seed(20261123); out = []
for k in mets:
    a = [num(v, k) for v in dev]; b = [num(v, k) for v in tst]
    obs = abs(st.median(a) - st.median(b)); allv = a + b; c = 0; T = 5000
    for _ in range(T):
        random.shuffle(allv); c += abs(st.median(allv[:len(a)]) - st.median(allv[len(a):])) >= obs
    out.append(dict(metric=k, older_n=len(a), older_median=st.median(a), newer_n=len(b), newer_median=st.median(b), abs_diff=round(obs, 3), perm_p=round((c + 1) / (T + 1), 3)))
for nm, f_ in (('opens_attributed_audit', lambda v: v in audit_att), ('no_cta_regex', lambda v: v not in hit)):
    a = sum(f_(v) for v in dev); b = sum(f_(v) for v in tst)
    out.append(dict(metric=nm, older_n=len(dev), older_median=f'{a}/{len(dev)}', newer_n=len(tst), newer_median=f'{b}/{len(tst)}', abs_diff=round(abs(a / len(dev) - b / len(tst)), 3), perm_p=''))
wr = csv.DictWriter(open(A / '05_HOLDOUT_TEMPORAL_SPLIT.csv', 'w', newline=''), fieldnames=list(out[0])); wr.writeheader(); wr.writerows(out)
print('older', dev[0], inv[dev[0]]['date'], '..', dev[-1], inv[dev[-1]]['date'], '| newer', tst[0], inv[tst[0]]['date'], '..', tst[-1], inv[tst[-1]]['date'])
for r in rows: print(r['rule_id'], r['videos_with'], '/', r['videos_of'], 'fam', r['families_with'], '/', r['families_of'], 'exc', r['exception_ids'][:60], '|', r['note'][:300])
for r in out: print(r)
