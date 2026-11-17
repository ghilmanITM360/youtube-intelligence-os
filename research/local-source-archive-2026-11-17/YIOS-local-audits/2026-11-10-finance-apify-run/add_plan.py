import sys
lab,name,uc,r,s,st,cap=sys.argv[1:]
p='build_outputs.py';t=open(p).read()
line=f"    '{lab}': ({name!r}, '{uc}', 'T2', None, [{r}, {s}, {st}], {cap}),\n"
assert f"'{lab}'" not in t
t=t.replace("}\nPILOTS",line+"}\nPILOTS",1);open(p,'w').write(t)
