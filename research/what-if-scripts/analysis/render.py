"""Render Deliverable 3 (comparison matrix) and sync the coverage ledger.
A VID is DONE only when audits/VID.md exists AND matrix.jsonl has its row.
Run: python3 research/what-if-scripts/analysis/render.py
"""
import json
from pathlib import Path
H = Path(__file__).resolve().parent
inv = {r["vid"]: r for r in json.loads((H / "inventory.json").read_text())}
rows = [json.loads(l) for l in (H / "matrix.jsonl").read_text().splitlines() if l.strip()]
assert len({r["vid"] for r in rows}) == len(rows), "duplicate matrix row"
led = json.loads((H / "coverage_ledger.json").read_text())
done = {r["vid"] for r in rows if (H / "audits" / f"{r['vid']}.md").exists()}
for v in led:
    led[v]["status"] = "DONE" if v in done else "NOT_STARTED"
    led[v]["audit"] = f"audits/{v}.md" if v in done else None
(H / "coverage_ledger.json").write_text(json.dumps(led, indent=1) + "\n")
cols = ["topic", "hook", "structure", "curiosity", "emotion", "payoff", "cta", "distinctive", "confidence"]
L = [f"# Deliverable 3: Comparison matrix ({len(done)}/83 audited)\n",
     "| VID | Title | Format | " + " | ".join(c.title() for c in cols) + " |", "|" + "---|" * (len(cols) + 3)]
for r in sorted(rows, key=lambda r: r["vid"]):
    cell = lambda c: "; ".join(r[c]) if isinstance(r[c], list) else r[c]
    L.append(f"| [{r['vid']}](audits/{r['vid']}.md) | {inv[r['vid']]['title']} | {inv[r['vid']]['format']} | " + " | ".join(cell(c) for c in cols) + " |")
nxt = next((v for v in sorted(led) if led[v]["status"] != "DONE"), None)
L += ["", f"Coverage: {len(done)}/83 DONE. Next unprocessed: {nxt}."]
(H / "03_COMPARISON_MATRIX.md").write_text("\n".join(L) + "\n")
print(f"{len(done)}/83 done; next {nxt}")
