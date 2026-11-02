import json, subprocess, csv, io, sys
REPO=sys.argv[1]; D="research/finance-economics-intelligence/"
C="origin/research/finance-economics-intelligence"; M="origin/codex/finance-machine-a-owner-directed"; V="origin/codex/casually-finance-forensic-research"
def show(ref,p): return subprocess.check_output(["git","-C",REPO,"show",f"{ref}:{p}"],text=True)
def sha(ref): return subprocess.check_output(["git","-C",REPO,"rev-parse",ref],text=True).strip()
res={}
# canonical video
rows={json.loads(l)["Video_ID"]:json.loads(l) for l in show(C,D+"VIDEO_AUDIT_966.jsonl").splitlines()}
r=rows["XJ4ls6r2MCE"]; res["canonical_video"]={"ref":C,"sha":sha(C),"id":"XJ4ls6r2MCE","batch":r["batch_id"],"statuses":set(r["statuses"].values()).pop() if len(set(r["statuses"].values()))==1 else r["statuses"]}
# machine A only
ma={json.loads(l)["Video_ID"]:json.loads(l) for l in show(M,D+"VIDEO_AUDIT_966.jsonl").splitlines()}
vid="pFs8QGikczo"; a=ma[vid]
res["machine_a_only_video"]={"ref":M,"sha":sha(M),"id":vid,"batch":a["batch_id"],"canonical_status":sorted(set(rows[vid]["statuses"].values())),"machine_a_status":sorted(set(a["statuses"].values()))}
# source/claim receipt join
pk=json.loads(show(M,D+f"audit-batches/{a['batch_id']}.json")); rc=json.loads(show(M,D+f"audit-batches/{a['batch_id']}_READ_RECEIPTS.json"))
claims=pk["reviews"][0]["script"]["claim_audit"]
srcids={s for c in claims for s in (c.get("source_ids") or [])} if isinstance(claims,list) else set()
rkeys=list(rc.keys()) if isinstance(rc,dict) else []
res["claim_receipt_join"]={"ref":M,"sha":sha(M),"packet":a["batch_id"],"claim_groups":len(claims),"source_ids_in_claims":len(srcids),"receipt_top_keys":rkeys[:8]}
# performance sensitivity
ps=list(csv.DictReader(io.StringIO(show(C,D+"PERFORMANCE_SENSITIVITY.csv"))))
p=[x for x in ps if "9r-45QPLl-Y" in x.values()]
res["performance_sensitivity"]={"ref":C,"sha":sha(C),"rows":len(ps),"rows_for_9r-45QPLl-Y":len(p),"cols":list(ps[0].keys())[:6]}
# visual DNA
t=show(V,"data/extracted/forensic-analysis/casually-finance/2026-10-12/04_PRODUCTION_DNA/VISUAL_DNA.md")
res["visual_dna"]={"ref":V,"sha":sha(V),"chars":len(t),"first_line":t.splitlines()[0]}
json.dump(res,open(sys.argv[2],"w"),indent=1,default=list); print(json.dumps(res,indent=1,default=list))
