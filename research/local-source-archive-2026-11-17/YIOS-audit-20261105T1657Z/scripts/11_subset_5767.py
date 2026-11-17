# For large manifests: does a single categorical value, or a path-keyword subset, yield exactly/near 5,767 distinct SHA-256 values?
import csv,re,sys,glob,os,collections
csv.field_size_limit(10**9)
rx=re.compile(r'^(sha256:)?[0-9a-f]{64}$')
files=[l.split('\t')[3].strip() for l in open(sys.argv[1]) if l.count('\t')==3 and l.rstrip().endswith('.csv')]
files=sorted(set(files))
for p in files:
  try:
    rows=list(csv.DictReader(open(p,newline='',errors='replace')))
  except Exception as e: print('ERR',p,e);continue
  if not rows: continue
  cols=rows[0].keys()
  sc=[c for c in cols if c and sum(1 for r in rows[:300] if rx.match((r.get(c) or '').strip()))>10]
  if not sc: continue
  for hc in sc:
    tot=set((r.get(hc) or '').replace('sha256:','').strip() for r in rows if rx.match((r.get(hc) or '').strip()))
    flag=' <<<' if 5760<=len(tot)<=5775 else ''
    print(f'{len(tot)}\t{hc}\tALL\t-\t{p}{flag}')
    for c in cols:
      if c==hc: continue
      vals=collections.defaultdict(set)
      for r in rows:
        v=(r.get(c) or '')[:60]; h=(r.get(hc) or '').replace('sha256:','').strip()
        if rx.match(h): vals[v].add(h)
      if not 1<len(vals)<=40: continue
      for v,s in vals.items():
        if 5700<=len(s)<=5830: print(f'{len(s)}\t{hc}\t{c}\t{v}\t{p}{" <<<" if 5760<=len(s)<=5775 else ""}')
