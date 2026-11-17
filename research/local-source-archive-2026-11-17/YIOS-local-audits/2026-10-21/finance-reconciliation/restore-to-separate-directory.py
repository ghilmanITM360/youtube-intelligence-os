"""Recover the 31 historical local versions to a NEW external directory, never over YIOS."""
import pathlib,sys,json,hashlib,shutil,os
D=pathlib.Path(__file__).resolve().parent
manifest=json.loads((D/'restoration-manifest.json').read_text())
dest=pathlib.Path(sys.argv[1]);assert dest.is_absolute() and not dest.exists(),'Specify a NEW absolute external directory'
repo=pathlib.Path(manifest['root']).resolve();assert not dest.resolve().is_relative_to(repo)
# Verify all sources before creating output.
for x in manifest['files']:assert hashlib.sha256(pathlib.Path(x['archive']).read_bytes()).hexdigest()==x['local_sha256']
dest.mkdir(mode=0o700,parents=True)
for x in manifest['files']:
 q=dest/x['path'];q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(x['archive'],q)
 os.chmod(q,x['mode']);os.utime(q,ns=(x['mtime_ns'],x['mtime_ns']))
 assert hashlib.sha256(q.read_bytes()).hexdigest()==x['local_sha256']
print('Recovered 31 verified historical files to',dest)
