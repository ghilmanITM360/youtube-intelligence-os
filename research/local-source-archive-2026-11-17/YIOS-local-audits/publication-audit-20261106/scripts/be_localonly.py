import json,subprocess,hashlib,collections,sys
from pathlib import Path
R='repos/ghilmanITM360/youtube-intelligence-os'; N='bf6522a570995a01561348165855c25e0e727ffb'
t=json.loads(subprocess.check_output(['gh','api',f'{R}/git/trees/{N}?recursive=1']))['tree']
remote={e['path'] for e in t if e['type']=='blob'}
BE=Path.home()/'YIOS-local-audits/barely-evolved';ROOT='research/visual-forensics/channels/UCH59TmQhPOPhC3M17jCWpRQ/'
a=BE/'AUDIO_LISTENING_CAPABILITY_2026-11-03.json'
e=[x for x in t if x['path'].endswith('campaign/AUDIO_LISTENING_CAPABILITY_2026-11-03.json')][0]
d=a.read_bytes();print('audio-cap local gitsha match',hashlib.sha1(b'blob %d\0'%len(d)+d).hexdigest()==e['sha'],e['path'])
for vid,folder in [('uPQcyookL0Y','2026-11-02-uPQcyookL0Y-deep-ct-scan'),('mNLNb-Z4T0M','2026-11-03-mNLNb-Z4T0M-deep-ct-scan'),('GNaBxt_zIRA','2026-11-03-GNaBxt_zIRA-deep-ct-scan'),('channel_synthesis','channel_synthesis')]:
    f=BE/folder;c=collections.Counter();b=collections.Counter();ex=[]
    for x in f.rglob('*'):
        if not x.is_file():continue
        rel=x.relative_to(f)
        if ROOT+vid+'/'+str(rel) in remote:continue
        c[x.suffix.lower()]+=1;b[x.suffix.lower()]+=x.stat().st_size
        if x.suffix.lower() not in('.png','.jpg','.jpeg','.mp4','.wav','.index','.webm','.mkv','.pyc','.npy','.npz','.m4a'):ex.append(str(rel)+f' ({x.stat().st_size})')
    print('\n==',vid,dict(c));print({k:round(v/1e6,1) for k,v in b.items()})
    print('non-media local-only',len(ex));print('\n'.join(sorted(ex)[:70]))
print('\nBE root local:');
for x in sorted(BE.iterdir()):
    if x.is_file():print(x.name,x.stat().st_size,(ROOT+'campaign/'+x.name) in remote)
print('remote *lfs* gitattributes on tree?',[p for p in remote if p.endswith('.gitattributes')][:5])
