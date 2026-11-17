import sys,zipfile,re,openpyxl
a,b=sys.argv[1],sys.argv[2]
wa=openpyxl.load_workbook(a);wb=openpyxl.load_workbook(b)
print('sheets',wa.sheetnames==wb.sheetnames,wb.sheetnames)
ch=[];styles=0;formulas=0;errs=0
for n in wa.sheetnames:
    x,y=wa[n],wb[n]
    if (x.max_row,x.max_column)!=(y.max_row,y.max_column): print('dims',n,x.dimensions,y.dimensions)
    for r in range(1,max(x.max_row,y.max_row)+1):
        for c in range(1,max(x.max_column,y.max_column)+1):
            p,q=x.cell(r,c),y.cell(r,c)
            if p.value!=q.value:
                ch.append((n,q.coordinate))
                if str(p.value).startswith('=') or str(q.value).startswith('='): formulas+=1
            if p.style_id!=q.style_id or p.number_format!=q.number_format: styles+=1
            if isinstance(q.value,str) and q.value.startswith('#'): errs+=1
print('changed',len(ch),ch,'styles',styles,'formulas',formulas,'errs',errs)
za,zb=zipfile.ZipFile(a),zipfile.ZipFile(b)
print('zip ok',zb.testzip() is None,'members equal',za.namelist()==zb.namelist())
for m in za.namelist():
    if 'worksheets/sheet' in m or 'sharedStrings' in m: continue
    A=re.sub(rb'rId\w+',b'R',za.read(m));B=re.sub(rb'rId\w+',b'R',zb.read(m))
    if A!=B: print('part differs',m)
