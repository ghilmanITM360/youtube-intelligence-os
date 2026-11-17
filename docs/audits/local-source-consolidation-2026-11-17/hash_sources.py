import os,sys,hashlib,csv
from concurrent.futures import ThreadPoolExecutor
H=os.path.expanduser('~'); W=H+'/workprojects/'
SRC={'yios-preserve-2026-11-17':H+'/yios-preserve-2026-11-17','YIOS-audit-20261105T1657Z':H+'/YIOS-audit-20261105T1657Z','finance-work-machine-a':H+'/finance-work-machine-a','YIOS-Archive':H+'/YIOS-Archive','YIOS-local-audits':H+'/YIOS-local-audits','what if book':W+'what if book','dr rehan video':W+'dr rehan video','yios-finance-machine-a':W+'yios-finance-machine-a','yio-cf-editing-forensics-local-evidence':W+'yio-cf-editing-forensics-local-evidence','yios-recovery-status':W+'yios-recovery-status','video data of what if':W+'video data of what if'}
def h(a):
    src,p=a
    try:
        st=os.lstat(p)
        if os.path.islink(p): return (src,p,'SYMLINK',st.st_size,os.readlink(p),'',int(st.st_mtime))
        s=hashlib.sha256(); g=hashlib.sha1(b'blob %d\0'%st.st_size)
        with open(p,'rb') as f:
            while True:
                b=f.read(8<<20)
                if not b: break
                s.update(b); g.update(b)
        return (src,p,'FILE',st.st_size,s.hexdigest(),g.hexdigest(),int(st.st_mtime))
    except Exception as e: return (src,p,'ERR',0,str(e),'',0)
def walk():
    for k,r in SRC.items():
        for d,dn,fn in os.walk(r,followlinks=False):
            for n in fn+[x for x in dn if os.path.islink(os.path.join(d,x))]: yield (k,os.path.join(d,n))
out=sys.argv[1]
with ThreadPoolExecutor(8) as ex, open(out,'w',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for i,r in enumerate(ex.map(h,walk(),chunksize=64)): w.writerow(r)
print('done')
