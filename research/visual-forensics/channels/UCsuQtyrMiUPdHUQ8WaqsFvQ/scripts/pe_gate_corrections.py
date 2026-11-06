"""Traceable per-video corrections on top of pe_finalize output (rerun after every finalize; idempotent).
1) reconstruction_test: PENDING was a hardcoded default. Campaign brief section 5 and ACCEPTANCE_RT_v1 define kit-bounded tests RT_L1 and RT_P1 only; no contract requires a per-video render.
2) hidden_region_audit: what the sheet label audit covered for this video. Usage: python3 -I pe_gate_corrections.py <video_dir>"""
import json, pathlib, sys
V = pathlib.Path(sys.argv[1]).resolve(); W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; q = V / "quality_gate.json"; g = json.loads(q.read_text())
if g["gates"].get("reconstruction_test") == "PENDING":
    g["gates"]["reconstruction_test"] = "NOT_APPLICABLE"
    g.setdefault("gate_corrections", []).append(dict(gate="reconstruction_test", old="PENDING", new="NOT_APPLICABLE", checkpoint="J", reason="Stale hardcoded default in pe_finalize.py. Campaign brief section 5 and reconstruction/ACCEPTANCE_RT_v1.md define only channel-level RT_L1 and RT_P1; kit reference 13 asks per-state prompts and blueprint, not a per-video render."))
    g["gate_evidence"]["reconstruction_test"] = "No per-video render test run or required. RT_L1 attempt 5 and RT_P1 attempt 6 pass as bounded animatic conformance at channel level only; that says nothing about reconstructing this video. production_blueprint stays PARTIAL, production_spec DRAFT_NOT_RENDERED."
s = json.loads((W / "campaign/hidden_audit/summary.json").read_text())["per_video"][V.name]
g["hidden_region_audit"] = dict(s, method="campaign/HIDDEN_REGION_AUDIT.md", unreviewed="Tiles marked DUP were compared numerically, not opened. Frames that were never sheet tiles are outside this audit unless listed in tables/strip_frames.csv.")
q.write_text(json.dumps(g, indent=2) + "\n")
