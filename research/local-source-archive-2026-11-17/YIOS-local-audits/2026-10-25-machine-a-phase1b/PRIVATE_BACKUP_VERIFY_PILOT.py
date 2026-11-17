"""Offline verifier for a future independently retrieved pilot. No uploads or writes.
Run ONLY after destination approval and actual independent retrieval.
"""
import argparse
import hashlib
import json
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,required=True)
    parser.add_argument('--restored-root',type=Path,required=True)
    args=parser.parse_args()
    manifest=json.loads(args.manifest.read_text())
    root=args.restored_root.resolve(strict=True)
    results=[]
    for row in manifest['files']:
        rel=Path(row['restore_relative'])
        if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe restoration mapping')
        p=root/rel
        source=Path(row['source'])
        if p.is_symlink() or not p.resolve(strict=True).is_relative_to(root):raise ValueError('Unsafe restored path')
        if p.resolve()==source.resolve():raise ValueError('Original source is not an independent restore')
        if source.exists() and p.samefile(source):raise ValueError('Hardlinked original is not an independent restore')
        before=p.stat();h=hashlib.sha256()
        with p.open('rb') as f:
            for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
        after=p.stat()
        stable=(before.st_size,before.st_mtime_ns,before.st_ino)==(after.st_size,after.st_mtime_ns,after.st_ino)
        ok=stable and after.st_size==row['bytes'] and h.hexdigest()==row['sha256']
        results.append({'restore_relative':row['restore_relative'],'bytes':after.st_size,'sha256':h.hexdigest(),'content_result':'PASS' if ok else 'FAIL'})
    passed=all(x['content_result']=='PASS' for x in results) and len(results)==4
    print(json.dumps({'content_result':'PASS' if passed else 'FAIL','files':results,
      'transport_independence':'MUST_BE_ATTESTED_SEPARATELY; this verifier cannot prove remote retrieval origin',
      'standalone_media_or_project_reproducibility':'NOT_VERIFIED'},indent=2))
    return 0 if passed else 1

if __name__=='__main__':raise SystemExit(main())
