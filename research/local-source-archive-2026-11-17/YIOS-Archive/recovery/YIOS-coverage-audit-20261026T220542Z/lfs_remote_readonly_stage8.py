import subprocess,json,urllib.request,urllib.error,base64
from pathlib import Path
O=Path(__file__).parent;ps=json.load(open(O/'evidence/LFS_POINTER_IDENTITIES.json'));token=subprocess.check_output(['gh','auth','token'],stderr=subprocess.PIPE).decode().strip();body={'operation':'download','transfers':['basic'],'objects':[{'oid':x['sha256'],'size':x['bytes']} for x in ps]};auth=base64.b64encode(('x-access-token:'+token).encode()).decode();req=urllib.request.Request('https://github.com/ghilmanITM360/youtube-intelligence-os.git/info/lfs/objects/batch',data=json.dumps(body).encode(),headers={'Authorization':'Basic '+auth,'Content-Type':'application/vnd.git-lfs+json','Accept':'application/vnd.git-lfs+json'},method='POST');out={'method':'Git LFS batch operation=download metadata only; no object transfer/fetch/pull, no upload operation','remote_payload_bytes_downloaded':0,'objects_requested':len(ps)}
try:
 with urllib.request.urlopen(req,timeout=40) as r:d=json.load(r);out['http_status']=r.status
 out['objects']=[{'oid':a.get('oid'),'size':a.get('size'),'download_action_offered':bool(a.get('actions',{}).get('download')),'provider_error':a.get('error'),'full_remote_bytes_sha256_verified':False} for a in d.get('objects',[])];out['download_links_and_tokens_retained']=False
except urllib.error.HTTPError as e:out.update(http_status=e.code,error='Provider refused read-only LFS download metadata; no payload transfer')
except Exception as e:out.update(error=type(e).__name__)
(O/'evidence/LFS_REMOTE_DOWNLOAD_METADATA.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
