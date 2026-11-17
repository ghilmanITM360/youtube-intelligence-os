"""Read-only Finance reconciliation: canonical vs Machine A, from actual git objects."""
import csv, io, json, subprocess, sys, hashlib
from collections import Counter
REPO = sys.argv[1]; OUT = sys.argv[2]
C, M = "origin/research/finance-economics-intelligence", "origin/codex/finance-machine-a-owner-directed"
D = "research/finance-economics-intelligence/"
COMPLETE = {"COMPLETE_EVIDENCE_BACKED", "COMPLETE_LIMITED_EVIDENCE"}
def git(*a): return subprocess.check_output(["git", "-C", REPO, *a], text=True)
def load(ref):
    rows = [json.loads(l) for l in git("show", f"{ref}:{D}VIDEO_AUDIT_966.jsonl").splitlines()]
    return {r["identity"]["Video_ID"]: r for r in rows}, len(rows)
def acc(r): return all(s in COMPLETE for s in r["statuses"].values())
c, nc = load(C); m, nm = load(M)
ca = {k for k, r in c.items() if acc(r)}; ma = {k for k, r in m.items() if acc(r)}
added = sorted(ma - ca)
h = lambda r: hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest()
changed = sorted(k for k in ca & ma if h(c[k]) != h(m[k]))
lost = sorted(ca - ma)
chg_detail = []
for k in changed:
    diffs = [f for f in c[k] if c[k][f] != m[k].get(f)]
    chg_detail.append({"video_id": k, "batch": c[k].get("batch_id"), "fields_changed": diffs,
                       "status_before": c[k]["statuses"], "status_after": m[k]["statuses"]})
conf = Counter(s for k in added for s in m[k]["statuses"].values())
confc = Counter(s for k in ca for s in c[k]["statuses"].values())
res = {"canonical_sha": git("rev-parse", C).strip(), "machine_a_sha": git("rev-parse", M).strip(),
       "merge_base": git("merge-base", C, M).strip(),
       "left_right": git("rev-list", "--left-right", "--count", f"{C}...{M}").split(),
       "patch_equivalent_commits": git("cherry", C, M).count("\n-"),
       "unique_machine_a_commits": git("rev-list", "--count", f"{C}..{M}").strip(),
       "canonical_ledger_rows": nc, "machine_a_ledger_rows": nm,
       "canonical_accepted": len(ca), "machine_a_accepted": len(ma),
       "additional_ids_count": len(added), "additional_ids": added,
       "ids_lost_in_machine_a": lost, "existing_records_changed": chg_detail,
       "machine_a_duplicate_ids": nm - len(m),
       "status_mix_added": dict(conf), "status_mix_canonical": dict(confc),
       "files_diff": [l.split("\t") for l in git("diff", "--name-status", C, M).splitlines() if "audit-batches/" not in l],
       "audit_batch_files_added": sum(1 for l in git("diff", "--name-status", C, M).splitlines() if "audit-batches/" in l)}
json.dump(res, open(f"{OUT}/finance_reconciliation.json", "w"), indent=1)
print({k: v for k, v in res.items() if k not in ("additional_ids", "files_diff", "existing_records_changed")}, "changed", len(changed))
