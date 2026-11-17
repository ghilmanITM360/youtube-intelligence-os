# Write per-batch reviewer briefs from video_batch_brief_template.md. Args: video_id rv_prefix "b01:0:15,b02:15:30,..."
import csv,os,re,sys
vid,pre,spec=sys.argv[1],sys.argv[2],sys.argv[3]
S=[r['state'] for r in csv.DictReader(open('tables/states_v1.csv'))];t=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'video_batch_brief_template.md')).read()
for item in spec.split(','):
    b,a,z=item.split(':');a,z=int(a),int(z);rv=f'{pre}_{b}';os.makedirs(f'agents/{rv}',exist_ok=True)
    s=t.replace('VIDEOID',vid).replace('WS',os.getcwd()).replace('BATCH',b).replace('RANGE',f'{S[a]}-{S[z-1]}').replace('STATES',f'index {a}-{z-1} ({S[a]}..{S[z-1]}, {z-a} rows)')
    open(f'agents/{rv}/BRIEF.md','w').write(re.sub(r'\bRV\b',rv,s))
print('ok')
