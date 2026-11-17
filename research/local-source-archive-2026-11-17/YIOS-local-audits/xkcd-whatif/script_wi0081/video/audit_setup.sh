#!/bin/zsh
# builds two audit copies of hf/: art-only (text hidden) and text-only (non-text hidden, text at 50% so stacked text darkens), renders both to video/audit/
cd /Users/ghilmankhan/YIOS-local-audits/xkcd-whatif/script_wi0081
mkdir -p video/audit
for v in art txt; do
  rsync -a --delete --exclude .hyperframes --exclude node_modules hf/ hf_audit_$v/
  if [ $v = art ]; then CSS='#world text{visibility:hidden}'; else CSS='#world :is(path,circle,ellipse,rect,image,line,polygon){visibility:hidden} #world text{filter:opacity(.5)}'; fi
  python3 - "$v" "$CSS" <<'PY'
import sys
v,css=sys.argv[1],sys.argv[2]
p=f'hf_audit_{v}/index.html'; s=open(p).read().replace('</style>',css+'\n</style>',1); open(p,'w').write(s)
PY
  (cd hf_audit_$v && npx hyperframes render -o ../video/audit/$v.mp4 -f 24 2>&1 | tail -1)
done
