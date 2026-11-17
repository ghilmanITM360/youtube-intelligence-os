import os,csv,hashlib,json,collections,time
out='/Users/ghilmankhan/YIOS-targeted-ssd-cleanup-20261029T0010PKT'
roots={
'CF':'/Users/ghilmankhan/Downloads/CasuallyFinance-Forensic-Research',
'V7':'/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd',
'WI_D':'/Users/ghilmankhan/Downloads/video data of what if',
'WI_W':'/Users/ghilmankhan/workprojects/video data of what if',
'SHORTS':'/Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence'}
mapfile='/Users/ghilmankhan/YIOS-coverage-audit-20261026T220542Z/checkpoints/VERIFIED_DRIVE_SOURCE_MAP.json'
vm=json.load(open(mapfile)); remote={x['source']:x for x in vm['objects']}; members={x['source_absolute']:x for x in vm['members']}; aliases={x['source_absolute']:x for x in vm['aliases']}
rows=[]
for label,root in roots.items():
 for base,dirs,files in os.walk(root,followlinks=False):
  dirs.sort();files.sort()
  for f in files:
   p=os.path.join(base,f)
   try:
    st=os.lstat(p)
    if not os.path.isfile(p) or os.path.islink(p): status='NONREGULAR';sha=''
    elif st.st_size and st.st_blocks==0: status='DATALESS';sha=''
    else:
     h=hashlib.sha256()
     with open(p,'rb') as z:
      while True:
       b=z.read(4*1024*1024)
       if not b:break
       h.update(b)
     sha=h.hexdigest();status='READ'
    r=remote.get(p);m=members.get(p);a=aliases.get(p); rec=r or m or a or {}
    rh=rec.get('sha256','');remote_match=bool(sha and sha==rh and status=='READ')
    rows.append(dict(group=label,path=p,relative=os.path.relpath(p,root),size=st.st_size,allocated=st.st_blocks*512,sha256=sha,status=status,remote_sha=rh,remote_match=remote_match,remote_id=rec.get('remote_id',rec.get('remote_archive_id','')),remote_status=rec.get('status',rec.get('verification_status',rec.get('verification_basis',''))),receipt=rec.get('verification_receipt',''),inode=st.st_ino,nlink=st.st_nlink,flags=getattr(st,'st_flags',0)))
   except Exception as e:
    rows.append(dict(group=label,path=p,relative=os.path.relpath(p,root),size='',allocated='',sha256='',status='ERROR:'+type(e).__name__,remote_sha='',remote_match=False,remote_id='',remote_status='',receipt='',inode='',nlink='',flags=''))
 with open(os.path.join(out,'progress.txt'),'a') as z:z.write(f'{label} done {sum(a["group"]==label for a in rows)} files\n')
fields=list(rows[0]);
with open(os.path.join(out,'TARGET_FILE_HASH_CROSSWALK.csv'),'w',newline='') as z:
 w=csv.DictWriter(z,fields);w.writeheader();w.writerows(rows)
bygroup=collections.defaultdict(list)
for x in rows:bygroup[x['group']].append(x)
summary={g:{'files':len(v),'logical':sum(int(x['size']) for x in v if x['size']!=''),'allocated':sum(int(x['allocated']) for x in v if x['allocated']!=''),'read':sum(x['status']=='READ' for x in v),'remote_exact':sum(x['remote_match'] for x in v),'remote_exact_allocated':sum(int(x['allocated']) for x in v if x['remote_match'])} for g,v in bygroup.items()}
a={x['relative']:x for x in bygroup['WI_D']};b={x['relative']:x for x in bygroup['WI_W']};wi=[]
for rel in sorted(set(a)|set(b)):
 x=a.get(rel);y=b.get(rel)
 verdict='ONLY_DOWNLOADS' if not y else 'ONLY_WORKPROJECTS' if not x else 'EXACT_COMMON' if x['sha256'] and x['sha256']==y['sha256'] else 'SAME_PATH_DIFFERENT'
 wi.append(dict(relative=rel,downloads_path=x['path'] if x else '',workprojects_path=y['path'] if y else '',downloads_sha256=x['sha256'] if x else '',workprojects_sha256=y['sha256'] if y else '',downloads_allocated=x['allocated'] if x else '',workprojects_allocated=y['allocated'] if y else '',verdict=verdict))
with open(os.path.join(out,'WHAT_IF_RELATIVE_SHA_COMPARISON.csv'),'w',newline='') as z:
 w=csv.DictWriter(z,wi[0].keys());w.writeheader();w.writerows(wi)
summary['whatif_verdicts']=dict(collections.Counter(x['verdict'] for x in wi));summary['whatif_exact_downloads_allocated']=sum(int(x['downloads_allocated']) for x in wi if x['verdict']=='EXACT_COMMON')
json.dump(summary,open(os.path.join(out,'TARGET_SUMMARY.json'),'w'),indent=2)
