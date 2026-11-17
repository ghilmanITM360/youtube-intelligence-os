"""Traceable per-video corrections on top of pe_finalize output (rerun after every finalize; idempotent).
1) reconstruction_test: PENDING was a hardcoded default. Campaign brief section 5 and ACCEPTANCE_RT_v1 define kit-bounded tests RT_L1 and RT_P1 only; no contract requires a per-video render.
2) hidden_region_audit: what the sheet label audit covered for this video. Usage: python3 -I pe_gate_corrections.py <video_dir>"""
import json, pathlib, sys
V = pathlib.Path(sys.argv[1]).resolve(); W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; q = V / "quality_gate.json"; g = json.loads(q.read_text())
if g["gates"].get("reconstruction_test") == "PENDING":
    g["gates"]["reconstruction_test"] = "NOT_APPLICABLE"
    g.setdefault("gate_corrections", []).append(dict(gate="reconstruction_test", old="PENDING", new="NOT_APPLICABLE", checkpoint="J", reason="Stale hardcoded default in pe_finalize.py. Campaign brief section 5 and reconstruction/ACCEPTANCE_RT_v1.md define only channel-level RT_L1 and RT_P1; kit reference 13 asks per-state prompts and blueprint, not a per-video render."))
    g["gate_evidence"]["reconstruction_test"] = "No per-video render test run or required. RT_L1 attempt 5 and RT_P1 attempt 6 pass as bounded animatic conformance at channel level only; that says nothing about reconstructing this video. production_blueprint stays PARTIAL, production_spec DRAFT_NOT_RENDERED."
g["gate_classification"] = dict(
    creative_design_review=dict(required_done="kit ref 13 Creative gate bullets 1-2, ref 08 attention timeline, ref 04 composition", remainder="OPTIONAL: native review of more states; state review stays tile scale, native sampled"),
    production_blueprint=dict(required_done="kit ref 13 Creative gate bullets 3-4, ref 09 per-state image/image-to-video/editor fields", remainder="OUTSIDE_SCOPE: per-video render. Brief section 5 and ACCEPTANCE_RT_v1 define channel-level bounded tests only. Prompts remain drafts"),
    independent_review=dict(required_done="brief section 3 tracked deliverable; reviewer plus primary spot-check", remainder="OPTIONAL: outside-family review; kit has no such gate. Limitation: same model family, sampled"),
    visual_script_mapping=dict(required_done="ASR-based overlap, relation labels", remainder="REQUIRED_BLOCKED: audio side, kit ref 13 Audio gate"))
if V.name == "uIG2U_1xynQ" and g["gates"]["meaningful_state_timing"] == "PASS":
    g.setdefault("gate_corrections", []).append(dict(gate="meaningful_state_timing", old="PARTIAL", new="PASS", checkpoint="K", reason="G0024/G0025 were held PARTIAL for object identity only. Onset f646 and cut f679 are measured; identity stays UNKNOWN in the ledger with the INFERRED reading labelled."))
s = json.loads((W / "campaign/hidden_audit/summary.json").read_text())["per_video"][V.name]
g["hidden_region_audit"] = dict(s, method="campaign/HIDDEN_REGION_AUDIT.md", unreviewed="Checkpoint K opened all DUP tiles and all EMPTY tiles with a residual mark. EMPTY tiles without a mark stay numeric only. Frames that were never sheet tiles are outside this audit unless listed in tables/strip_frames.csv.")
q.write_text(json.dumps(g, indent=2) + "\n")
