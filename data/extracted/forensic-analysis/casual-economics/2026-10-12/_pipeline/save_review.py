import sys,json
from pathlib import Path
# Legacy sheet-only invocation retains Singapore; explicit video argument selects other sources.
args=sys.argv[1:]
vid=args[0] if len(args)>1 else 'kbPauzdHhcI'
sheet=int(args[1] if len(args)>1 else args[0])
w=(Path(args[2]) if len(args)>2 else Path('/private/tmp/yios-finance-execution-evidence/economics-work'))/vid
j=json.load(open(w/'visual_auto.json'));st=j['states'][(sheet-1)*12:sheet*12];lines=[s for s in sys.stdin.read().splitlines() if s.strip()];assert len(lines)==len(st),(sheet,len(lines),len(st));p=w/'visual_review.json';old=json.load(open(p)) if p.exists() else {}
for state,line in zip(st,lines):
 assert state['state_id'] not in old
 parts=line.split('|');assert len(parts)==3
 old[state['state_id']]={'description':parts[0],'assets':parts[1].split(';'),'state_change_observation':parts[2],'reviewed_sheet':f'sheet_{sheet:03d}.jpg','representative_frame_sec':state['rep_t'],'confidence':'OBSERVED_REPRESENTATIVE_FRAME; transition path and tool attribution not established'}
p.write_text(json.dumps(old,indent=2)+'\n');print('Saved',sheet,len(st),'total',len(old))
