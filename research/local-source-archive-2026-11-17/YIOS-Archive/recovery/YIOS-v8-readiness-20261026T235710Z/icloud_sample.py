import os,json,csv,subprocess,hashlib,time
from pathlib import Path
O=Path(__file__).parent;A=Path('/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z');paths=json.load(open(O/'evidence/ICLOUD_SAMPLE_PATHS.json'));results=[]
# Read at most 20KB in total from eight already selected tiny placeholders; never requestDownload / whole folder hydration.
for i,p in enumerate(paths):
 before=os.stat(p);row={'path':p,'before_bytes':before.st_size,'before_flags':before.st_flags,'before_mtime_ns':before.st_mtime_ns,'before_inode':before.st_ino}
 if before.st_size>20000:row['result']='SKIPPED_SIZE'
 else:
  code='import sys,pathlib; b=pathlib.Path(sys.argv[1]).read_bytes(); assert len(b)<=20000; sys.stdout.buffer.write(b)'
  try:
   r=subprocess.run(['python3','-c',code,p],capture_output=True,timeout=12)
   if r.returncode:row.update(result='READ_FAILED',error=r.stderr.decode()[:200])
   else:
    b=r.stdout;dest=O/'scratch-private'/('icloud-sample-'+str(i));dest.write_bytes(b);row.update(result='FULL_BYTES_READ',actual_bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),scratch=str(dest),parse='UTF8_PASS' if b.decode('utf8',errors='replace').encode()==b else 'BINARY_OR_NONUTF8')
  except subprocess.TimeoutExpired:row.update(result='READ_TIMEOUT',reason='No retry/bulk hydration; account or provider access unresolved')
 after=os.stat(p);row.update(after_flags=after.st_flags,after_bytes=after.st_size,after_mtime_ns=after.st_mtime_ns,after_inode=after.st_ino,identity_size_mtime_stable=(before.st_ino,before.st_size,before.st_mtime_ns)==(after.st_ino,after.st_size,after.st_mtime_ns));results.append(row)
 (O/'evidence/ICLOUD_READ_SAMPLE.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
