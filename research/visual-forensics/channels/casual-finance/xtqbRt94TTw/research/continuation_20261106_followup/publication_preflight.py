"""Casual Finance Video006 text-only publication gate. No mutations or pushes.
Candidate tree, including content, is checked. Inherited known violations remain
visible and byte-pinned; this is preservation, not a clean-tree certification.
"""
import argparse, hashlib, json, subprocess, re
from pathlib import PurePosixPath,Path
REPO='/Users/ghilmankhan/workprojects/youtube-intelligence-os'
PREFIX='research/visual-forensics/channels/casual-finance/xtqbRt94TTw/'
TEXT_SUFFIXES={'.md','.json','.csv','.py','.txt','.html','.css','.js','.sh'}
def violations(entries,inherited):
 bad=[]
 for path,data in entries.items():
  if path in inherited and hashlib.sha256(data).hexdigest()==inherited[path]:continue
  p=PurePosixPath(path)
  if p.is_absolute() or '..' in p.parts:bad.append([path,'unsafe path']);continue
  if p.suffix.lower() not in TEXT_SUFFIXES and not re.fullmatch(r'(?:EVIDENCE_)?SHA256SUMS(?:_[A-Za-z0-9_]+)?',p.name):
   bad.append([path,'not approved text format']);continue
  try:txt=data.decode('utf-8')
  except UnicodeDecodeError:bad.append([path,'binary/non-UTF8 content']);continue
  if any(ord(c)<32 and c not in '\t\r\n' for c in txt):bad.append([path,'binary control bytes'])
 return bad
def git(*a,input_data=None):return subprocess.check_output(['git','-C',REPO,*a],input=input_data)
def check_tree(parent,tree,defects):
 # Full scoped tree checked; only exact, documented inherited media is tolerated.
 known={x['path']:x['sha256'] for x in defects['unexpected_media']}
 entries={};bad=[];blobs=[]
 for record in git('ls-tree','-r','-z',tree,'--',PREFIX).split(b'\0'):
  if not record:continue
  meta,path=record.split(b'\t',1);mode,kind,blob=meta.decode().split();path=path.decode()
  if mode not in {'100644','100755'} or kind!='blob':bad.append([path,'non-regular file']);continue
  blobs.append((path,blob))
 batch=git('cat-file','--batch',input_data=(''.join(blob+'\n' for _,blob in blobs)).encode())
 offset=0
 for path,blob in blobs:
  end=batch.index(b'\n',offset);header=batch[offset:end].split();size=int(header[2]);offset=end+1
  entries[path]=batch[offset:offset+size];offset+=size+1
 bad+=violations(entries,known)
 # Every changed path must stay within authorized Video006 scope.
 changed=git('diff','--name-only','-z',parent,tree).split(b'\0')
 bad += [[x.decode(),'outside Video006 scope'] for x in changed if x and not x.decode().startswith(PREFIX)]
 # Pin exceptions to parent too; an unknown/mismatching baseline cannot silently whitelist a new file.
 for path,h in known.items():
  try:data=git('show',parent+':'+path)
  except subprocess.CalledProcessError:bad.append([path,'inherited exception absent in parent']);continue
  if hashlib.sha256(data).hexdigest()!=h:bad.append([path,'inherited exception parent hash mismatch'])
 return {'status':'REJECT' if bad else 'PASS_WITH_DOCUMENTED_INHERITED_MEDIA','violations':bad,'inherited_media':[{'path':x,'sha256':h,'still_in_tree':x in entries} for x,h in known.items()], 'scoped_blobs_checked':len(entries),'new_or_modified_media_allowed':False,'history_unchanged':True}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('parent');a.add_argument('tree');a.add_argument('--defects',required=True);a.add_argument('--receipt',required=True);o=a.parse_args()
 result=check_tree(o.parent,o.tree,json.loads(Path(o.defects).read_text()));Path(o.receipt).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));raise SystemExit(bool(result['violations']))
