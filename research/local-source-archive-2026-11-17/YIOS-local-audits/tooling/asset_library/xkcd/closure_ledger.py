"""Rebuild ct_closure/CLOSURE_LEDGER_v1.csv from every videos/*/quality_gate_visual_v1.json (read-only on evidence)."""
import csv, glob, json, pathlib
root = pathlib.Path.home() / "YIOS-local-audits/xkcd-whatif"; out = root / "asset_library/_channel/ct_closure/CLOSURE_LEDGER_v1.csv"
fmt = {r["video_id"]: r["format_class"] for r in csv.DictReader(open(root / "census/census.csv"))}
rows = []
for f in sorted(glob.glob(str(root / "videos/*/quality_gate_visual_v1.json"))):
    q = json.load(open(f)); rows.append([q["video_id"], fmt.get(q["video_id"], ""), q["source_sha256"], q["final_video_status"], q["generated_utc"],
        ";".join(k for k, v in q["visual_gates"].items() if v != "PASS") or "none", f"videos/{q['video_id']}/quality_gate_visual_v1.json", f"videos/{q['video_id']}/closure_v1/CLOSURE.md"])
rows.sort(key=lambda r: r[4])
with open(out, "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["video_id", "format", "source_sha256", "status", "closed_utc", "failing_gates", "gate_file", "closure_record"]); w.writerows(rows)
print(sum(r[3] == "VISUAL_ANALYSIS_COMPLETE" for r in rows), "complete of", len(rows))
