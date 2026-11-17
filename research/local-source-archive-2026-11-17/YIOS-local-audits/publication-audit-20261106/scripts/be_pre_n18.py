import json,re,subprocess,sys
from pathlib import Path
S=Path(sys.argv[0]).parent;r=json.load(open(S/'stream_compare.json'))['BarelyEvolved']
BE=Path.home()/'YIOS-local-audits/barely-evolved';repo=str(Path.home()/'workprojects/youtube-intelligence-os')
ab=[a for a in r['absent']]
print('root/non-evidence absent:');[print(' ',a[1],a[0]) for a in ab if '/evidence/' not in a[0]]
pat=re.compile(r'(ghp_|gho_|github_pat_|sk-[A-Za-z0-9]{16}|token=|AKIA|BEGIN .*PRIVATE|password|api[_-]?key|secret)',re.I)
print('sensitive hits in absent files:')
for a in ab:
    t=(BE/a[0]).read_text(errors='replace')
    for m in pat.finditer(t):
        ln=t[:m.start()].count('\n')+1;print(' ',a[0],'L',ln,m.group(0));
print('ops log hits:',[m.group(0) for m in pat.finditer((BE/'BE_OPS_LOG.txt').read_text())])
print('receipts:')
rc=sorted(a[0] for a in ab if a[0].endswith('_PUBLICATION_RECEIPT.json'))
for p in rc:
    d=json.loads((BE/p).read_text());c=d.get('published_sha') or d.get('commit') or d.get('sha');ok=None
    if c:
        ok=subprocess.run(['git','merge-base','--is-ancestor',c,'origin/research/barely-evolved-visual-forensics'],cwd=repo).returncode==0
    print(' ',p,(c or '?')[:10],ok,d.get('readback_sha256_mismatches'))
