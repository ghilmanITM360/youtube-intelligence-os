import struct,zlib,hashlib,json,subprocess,os
from pathlib import Path
O=Path(__file__).parent;P=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os');B=Path('/Users/ghilmankhan/yios-git-recovery/cleanup-2026-10-13/local-only-history.bundle');data=B.read_bytes();start=data.index(b'\n\n')+2;pack=data[start:];assert pack[:4]==b'PACK';version,count=struct.unpack('>II',pack[4:12]);pos=12;entries=[];byoff={};byid={};names={1:'commit',2:'tree',3:'blob',4:'tag'};external=[]
def vint(d,p):
 s=0;v=0
 while True:
  b=d[p];p+=1;v|=(b&127)<<s;s+=7
  if not b&128:return v,p
def apply(base,d):
 n,p=vint(d,0);outsize,p=vint(d,p);assert n==len(base);out=bytearray()
 while p<len(d):
  b=d[p];p+=1
  if b&128:
   off=0;size=0
   for i in range(4):
    if b&(1<<i):off|=d[p]<<(8*i);p+=1
   for i in range(3):
    if b&(1<<(4+i)):size|=d[p]<<(8*i);p+=1
   out+=base[off:off+(size or 65536)]
  else:assert b;out+=d[p:p+b];p+=b
 assert len(out)==outsize;return bytes(out)
for k in range(count):
 off=pos;b=pack[pos];pos+=1;typ=(b>>4)&7;size=b&15;shift=4
 while b&128:b=pack[pos];pos+=1;size|=(b&127)<<shift;shift+=7
 base=None
 if typ==6:
  c=pack[pos];pos+=1;dist=c&127
  while c&128:c=pack[pos];pos+=1;dist=((dist+1)<<7)+(c&127)
  base=('offset',off-dist)
 elif typ==7:base=('oid',pack[pos:pos+20].hex());pos+=20
 z=zlib.decompressobj();payload=z.decompress(pack[pos:]);assert z.eof;consumed=len(pack[pos:])-len(z.unused_data);pos+=consumed;assert len(payload)==size
 e={'offset':off,'type':typ,'data':payload,'base':base};entries.append(e);byoff[off]=e
# Resolve deltas using only in-memory pack and existing read-only prerequisites
pending=entries[:]
while pending:
 progress=False
 for e in pending[:]:
  typ=e['type'];payload=e['data']
  if typ in (6,7):
   mode,key=e['base'];parent=byoff.get(key) if mode=='offset' else byid.get(key)
   if parent and 'oid' not in parent:continue
   if parent:typ=parent['type'];base=parent['data']
   elif mode=='oid':
    env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1');t=subprocess.check_output(['git','cat-file','-t',key],cwd=P,env=env).decode().strip();typ={v:k for k,v in names.items()}[t];base=subprocess.check_output(['git','cat-file',t,key],cwd=P,env=env);external.append(key)
   else:continue
   payload=apply(base,payload)
  oid=hashlib.sha1((names[typ]+' '+str(len(payload))+'\0').encode()+payload).hexdigest();e.update(type=typ,data=payload,oid=oid);byid[oid]=e;pending.remove(e);progress=True
 assert progress,'Unresolved delta'
claims=['15cbe9f0112596c1e07c1c1504302cce77bfd97a','5b6c3042679400b16aa1024b79058b71dade0ab9'];out={'bundle':str(B),'bundle_sha256':hashlib.sha256(data).hexdigest(),'pack_version':version,'pack_object_count':count,'pack_trailer_sha1_pass':hashlib.sha1(pack[:-20]).digest()==pack[-20:],'pack_consumed_exact':pos==len(pack)-20,'claimed_objects':[],'external_delta_prerequisites':external,'live_git_writes':0,'isolated_full_restore':'NOT_PERFORMED; bundle header prerequisites remain required'}
for oid in claims:
 e=byid.get(oid);out['claimed_objects'].append({'oid':oid,'present_in_pack':e is not None,'type':names[e['type']] if e else None,'commit_text':e['data'].decode() if e else None})
(O/'evidence/BUNDLE_PACK_VERIFICATION.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='claimed_objects'},indent=2));print([(x['oid'],x['present_in_pack']) for x in out['claimed_objects']])
