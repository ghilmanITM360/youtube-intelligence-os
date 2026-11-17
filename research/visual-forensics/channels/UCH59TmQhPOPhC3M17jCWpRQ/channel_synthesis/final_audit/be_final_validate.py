# Final-audit deterministic validator for the three Barely Evolved videos (read-only over evidence; writes one JSON).
# Checks: latest seal hashes, remote-tree vs local readback, state partition vs decoded frames, per-state art/prompt
# coverage, narration coverage vs ASR segments, JSON parse of every published .json.
import csv, hashlib, json, subprocess, sys
from pathlib import Path

B = Path('/Users/ghilmankhan/YIOS-local-audits/barely-evolved'); REPO = '/Users/ghilmankhan/workprojects/youtube-intelligence-os'
REF = 'origin/research/barely-evolved-visual-forensics'; PFX = 'research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/'
V = {'uPQcyookL0Y': ('2026-11-02-uPQcyookL0Y-deep-ct-scan', 'P', 'tables/states_v6_draft.csv', 'state_v4', 'tables/o_art_consolidated.csv', None, 'audio_visual_alignment_v5.csv'),
     'mNLNb-Z4T0M': ('2026-11-03-mNLNb-Z4T0M-deep-ct-scan', 'C1', 'tables/states_v1.csv', 'state', 'tables/consolidated_art_audit.csv', 'tables/consolidated_state_prompts.csv', 'tables/consolidated_narration_relation.csv'),
     'GNaBxt_zIRA': ('2026-11-03-GNaBxt_zIRA-deep-ct-scan', 'C', 'tables/states_v1.csv', 'state', 'tables/consolidated_art_audit.csv', 'tables/consolidated_state_prompts.csv', 'tables/consolidated_narration_relation.csv')}
git = lambda *a: subprocess.check_output(['git', *a], cwd=REPO)
sha = lambda b: hashlib.sha256(b).hexdigest()
out = {}
remote_files = git('ls-tree', '-r', '--name-only', REF).decode().splitlines()
for vid, (d, seal, stf, sk, artf, promptf, narf) in V.items():
    p = B / d; r = {}
    bad = []; n = 0
    for line in (p / f'EVIDENCE_SHA256SUMS_checkpoint_{seal}').read_text().splitlines():
        h, f = line.split(None, 1); n += 1
        if not Path(f).exists() or sha(Path(f).read_bytes()) != h: bad.append(f)
    r['seal'] = dict(file=f'EVIDENCE_SHA256SUMS_checkpoint_{seal}', entries=n, mismatches=bad)
    mine = [f for f in remote_files if f.startswith(PFX + vid + '/')]; mm = []; jbad = []; missing = []
    for f in mine:
        blob = git('show', f'{REF}:{f}'); loc = p / f[len(PFX + vid + '/'):]
        if not loc.exists(): missing.append(f); continue
        if sha(blob) != sha(loc.read_bytes()): mm.append(f)
        if f.endswith('.json'):
            try: json.loads(blob)
            except Exception: jbad.append(f)
    r['remote_readback'] = dict(remote_files=len(mine), sha_mismatch_vs_local=mm, remote_only_or_unmapped=len(missing), invalid_json=jbad)
    nfr = sum(1 for _ in open(p / 'FULL_FRAME_MEASUREMENTS.csv')) - 1
    st = list(csv.DictReader(open(p / stf))); gaps = []; ov = []
    for a, b in zip(st, st[1:]):
        if int(b['start']) > int(a['end']) + 1: gaps.append((a[sk], b[sk]))
        if int(b['start']) <= int(a['end']): ov.append((a[sk], b[sk]))
    r['partition'] = dict(states=len(st), first=int(st[0]['start']), last=int(st[-1]['end']), decoded_frames=nfr,
                          covers_all=int(st[0]['start']) == 0 and int(st[-1]['end']) == nfr - 1, gaps=gaps, overlaps=ov)
    ids = {s[sk] for s in st}
    art = {a['state'] for a in csv.DictReader(open(p / artf))}
    r['art_coverage'] = dict(states_with_art=len(ids & art), missing=sorted(ids - art))
    if promptf:
        pr = {a['state'] for a in csv.DictReader(open(p / promptf))}
        r['prompt_coverage'] = dict(states_with_prompt=len(ids & pr), missing=sorted(ids - pr))
    nar = list(csv.DictReader(open(p / narf)))
    asr = list(csv.DictReader(open(p / 'asr/asr_small_en_segments.csv'))) if (p / 'asr/asr_small_en_segments.csv').exists() else []
    r['narration'] = dict(rows=len(nar), asr_segments=len(asr) or 'see asr/', audio_verified=0)
    out[vid] = r
cs = B / 'channel_synthesis'; bad = []
for line in (cs / 'EVIDENCE_SHA256SUMS_checkpoint_S1').read_text().splitlines():
    h, f = line.split(None, 1)
    if sha(Path(f).read_bytes()) != h: bad.append(f)
out['channel_synthesis'] = dict(seal_mismatches=bad)
Path(sys.argv[1]).write_text(json.dumps(out, indent=1)); print(json.dumps(out, indent=1))
