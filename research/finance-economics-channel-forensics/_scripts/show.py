import sys,glob,re
p=glob.glob(f"{sys.argv[1]}/01_CHANNEL_REPORTS/{sys.argv[2]}_*/EVIDENCE_DOSSIER.md")[0]
skip=re.compile(r"^\| (h_|s_cta|t_year|t_caps|t_named|s_q_|s_example|t_len|t_urgency|tx_words|s_wpm|i_promise|s_but|th_color)")
import itertools
lines=open(p).read().splitlines()[4:]
out=[];cnt=0;sec=''
for l in lines:
    if l.startswith('## '): sec=l;cnt=0
    if l.startswith('- **'): cnt+=1
    if cnt>5 and ('PI long-form' in sec): continue
    out.append(l)
for l in out:
    if skip.match(l): continue
    if l.startswith('  - 0-30s:'): l=l[:280]+'…'
    if l.startswith('  - end:'): l=l[:150]+'…'
    print(l)
