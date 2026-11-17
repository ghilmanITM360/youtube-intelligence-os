import json,hashlib,urllib.request
from pathlib import Path
urls={
 'policy_contract':'https://www.federalreserveconsumerhelp.gov/loans-mortgage/',
 'fixed_arm':'https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-fixed-rate-and-adjustable-rate-mortgage-arm-loan-en-100/',
 'escrow':'https://www.consumerfinance.gov/ask-cfpb/on-a-mortgage-whats-the-difference-between-my-principal-and-interest-payment-and-my-total-monthly-payment-en-1941/',
 'refinance':'https://www.consumerfinance.gov/consumer-tools/mortgages/answers/key-terms/',
 'model_card':'https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX/raw/main/README.md',
 'kokoro_license':'https://raw.githubusercontent.com/hexgrad/kokoro/main/LICENSE',
 'remotion_render':'https://www.remotion.dev/docs/render',
}
Path('evidence/sources').mkdir(exist_ok=True);out=[]
for name,url in urls.items():
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'});b=urllib.request.urlopen(req,timeout=20).read();suffix='.txt' if name.endswith('license') or name=='model_card' else '.html';p=Path(f'evidence/sources/{name}{suffix}');p.write_bytes(b);out.append({'id':name,'url':url,'retrieved_date':'2026-10-13','cache':str(p),'sha256':hashlib.sha256(b).hexdigest()})
 except Exception as ex:out.append({'id':name,'url':url,'retrieved_date':'2026-10-13','cache':'UNAVAILABLE','error':str(ex)})
Path('evidence/web-source-cache.json').write_text(json.dumps(out,indent=2))
req=urllib.request.Request('https://huggingface.co/api/models/onnx-community/Kokoro-82M-v1.0-ONNX',headers={'User-Agent':'Mozilla/5.0'});model=json.load(urllib.request.urlopen(req,timeout=20));rev=model['sha']
p=Path('tools/voice.mjs');s=p.read_text().replace("dtype:'q8',device:'cpu'","dtype:'q8',device:'cpu',revision:'"+rev+"'");p.write_text(s)
model_hashes=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}for p in Path('.cache').rglob('*') if p.is_file()]
Path('evidence/model-provenance.json').write_text(json.dumps({'id':model['id'],'revision_checked':rev,'licence':model.get('cardData',{}).get('license'),'revision_check_date':'2026-10-13','files':model_hashes,'limits':'Revision checked after generation; file hashes identify actual cached assets. Frozen audio stems are the rendering source of truth, so rerender does not redownload or regenerate speech.'},indent=2));print('Cached web sources and model hashes; pinned future generation revision')
