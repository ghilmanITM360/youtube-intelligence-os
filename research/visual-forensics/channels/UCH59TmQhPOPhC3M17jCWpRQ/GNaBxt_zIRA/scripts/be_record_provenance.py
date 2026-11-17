import json,sys,hashlib,re
from pathlib import Path
rv,batch,agent,spot=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4:]
T=Path(f'/Users/ghilmankhan/.claude/projects/-Users-ghilmankhan-workprojects-youtube-intelligence-os/7a28d062-11cb-4600-a99d-27b9caa812d6/subagents/agent-{agent}.jsonl')
txt=T.read_text();reads=sorted(set(re.findall(r'"name":"Read","input":\{"file_path":"([^"]+\.png)"',txt)))
out={'reviewer':rv,'batch':batch,'transcript_path':str(T),'transcript_sha256':hashlib.sha256(T.read_bytes()).hexdigest(),'unique_png_read_calls':len(reads),'image_results':txt.count('"type":"image"'),'model':'sonnet subagent (Claude Code general-purpose), same model family as primary orchestrator claude-opus-5-5; no human, no different-vendor review','primary_spot_checks':spot,'single_model_no_listening':True}
Path(f'tables/provenance_{rv}.json').write_text(json.dumps(out,indent=1));print(out['unique_png_read_calls'],out['image_results'])
